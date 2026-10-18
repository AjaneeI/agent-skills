#!/usr/bin/env python3
"""Minimal synthetic MCP host. Evidence stays outside the agent workspace.
No benchmark or scoring semantics are defined here; cases.json and score.py stay frozen.
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path


def public_case(case):
    return {key:case[key] for key in ('prompt','tasks','global_stop')}


def schedule(cases):
    rows=[]
    for ci,case in enumerate(cases):
        for replicate in range(1,4):
            order=['baseline','skill'] if (ci+replicate)%2==0 else ['skill','baseline']
            for condition in order:
                rows.append(dict(trial_id=f"{case['id']}-r{replicate}-{condition}",case_id=case['id'],case_index=ci,replicate=replicate,condition=condition,status='not_started'))
    return rows


class Host:
    def __init__(self,case,evidence):
        self.case=case
        self.evidence=evidence
        evidence.mkdir(parents=True,exist_ok=True)
        self.calls=0
        self.checkpoints=0
        self.events=0
        self.used={k:v['attempts_used'] for k,v in case['tasks'].items()}
        self.completed=set()
        # Resume state is host-authored, outside agent access.
        state=evidence/'state.json'
        if state.exists():
            saved=json.loads(state.read_text())
            self.__dict__.update(saved)
            self.completed=set(self.completed)

    def log(self,record):
        self.events+=1
        record.update(host_event_id=f'h{self.events}',monotonic_ns=time.monotonic_ns())
        with (self.evidence/'host.jsonl').open('a') as f:
            f.write(json.dumps(record,sort_keys=True)+'\n');f.flush()

    def persist(self):
        state={k:getattr(self,k) for k in ('calls','checkpoints','events','used')}
        state['completed']=sorted(self.completed)
        (self.evidence/'state.json').write_text(json.dumps(state,sort_keys=True))

    def call(self,name,args):
        task=args.get('task')
        if task not in self.case['tasks']:raise ValueError('unknown task')
        if self.events>=22:raise ValueError('normalized event budget exhausted')
        if name=='save_checkpoint':
            text=args.get('state')
            if not isinstance(text,str) or not text.strip() or len(text)>12000:raise ValueError('invalid checkpoint state')
            self.checkpoints+=1
            ref=f'checkpoint-{task}-{self.checkpoints}.json'
            data=json.dumps(dict(task=task,state=text),sort_keys=True).encode()
            with (self.evidence/ref).open('xb') as f:f.write(data)
            result=dict(evidence_ref=ref,sha256=hashlib.sha256(data).hexdigest())
            self.log(dict(type='checkpoint',task=task,**result))
        elif name=='execute_task':
            self.calls+=1
            cid=f'call-{self.calls}'
            self.log(dict(type='tool_attempt',task=task,call_id=cid,arguments=args))
            spec=self.case['tasks'][task]
            allowed=(not self.case['global_stop'] and spec['allowed'] and self.used[task]<spec['attempt_limit'] and all(t in self.completed for t in spec['depends_on']))
            if allowed:
                self.used[task]+=1
                value=sum(spec['inputs']);self.completed.add(task)
                result=dict(call_id=cid,outcome='completed',value=value)
            else:result=dict(call_id=cid,outcome='denied')
            self.log(dict(type='tool_result',**result))
        else:raise ValueError('unknown tool')
        self.persist()
        return result


TOOLS=[
 dict(name='execute_task',description='Execute the synthetic arithmetic operation for one task under its fixed permissions and attempt limit. Returns an observed result or denial.',inputSchema=dict(type='object',properties=dict(task=dict(type='string')),required=['task'],additionalProperties=False)),
 dict(name='save_checkpoint',description='Persist a task state or result as a durable versioned artifact. The host returns its evidence reference and hash.',inputSchema=dict(type='object',properties=dict(task=dict(type='string'),state=dict(type='string')),required=['task','state'],additionalProperties=False))]


def serve(case_path,case_id,evidence):
    cases=json.loads(Path(case_path).read_text())['cases']
    host=Host(next(c for c in cases if c['id']==case_id),Path(evidence))
    for line in sys.stdin:
        req=json.loads(line)
        if 'id' not in req:continue
        method=req['method']
        try:
            if method=='initialize':res=dict(protocolVersion=req['params']['protocolVersion'],capabilities=dict(tools={}),serverInfo=dict(name='continuity-synthetic-host',version='1'))
            elif method=='tools/list':res=dict(tools=TOOLS)
            elif method=='tools/call':
                result=host.call(req['params']['name'],req['params'].get('arguments',{}))
                res=dict(content=[dict(type='text',text=json.dumps(result))],isError=False)
            elif method=='ping':res={}
            else:raise ValueError('unsupported MCP method '+method)
            response=dict(jsonrpc='2.0',id=req['id'],result=res)
        except Exception as err:
            with (Path(evidence)/'host-errors.jsonl').open('a') as f:f.write(json.dumps(dict(request=req,error=str(err)))+'\n')
            response=dict(jsonrpc='2.0',id=req['id'],error=dict(code=-32602,message=str(err)))
        print(json.dumps(response),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--case-file',required=True);p.add_argument('--case-id',required=True);p.add_argument('--evidence',required=True)
    args=p.parse_args();serve(args.case_file,args.case_id,args.evidence)
