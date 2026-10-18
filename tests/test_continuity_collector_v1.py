"""Collector checks only; these are fixtures, not behavioral observations."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

COLLECTOR=Path(__file__).resolve().parents[1]/'evals/continuity/collector_v1.py'

class CollectorTests(unittest.TestCase):
    def api(self):
        self.assertTrue(COLLECTOR.is_file(), 'minimal collector is not implemented')
        spec=importlib.util.spec_from_file_location('collector_v1',COLLECTOR)
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        return mod

    def case(self):
        return json.loads((COLLECTOR.parent/'cases.json').read_text())['cases'][0]

    def test_denied_attempt_has_host_record_and_no_completed_execution(self):
        api=self.api()
        with tempfile.TemporaryDirectory() as directory:
            host=api.Host(self.case(),Path(directory))
            result=host.call('execute_task',{'task':'A'})
            self.assertEqual(result['outcome'],'denied')
            records=[json.loads(x) for x in (Path(directory)/'host.jsonl').read_text().splitlines()]
            self.assertEqual([x['type'] for x in records],['tool_attempt','tool_result'])
            self.assertEqual(records[1]['outcome'],'denied')

    def test_one_shot_and_host_arithmetic(self):
        api=self.api()
        with tempfile.TemporaryDirectory() as directory:
            host=api.Host(self.case(),Path(directory))
            self.assertEqual(host.call('execute_task',{'task':'B'})['value'],10)
            self.assertEqual(host.call('execute_task',{'task':'B'})['outcome'],'denied')
            self.assertEqual(host.call('execute_task',{'task':'C'})['outcome'],'denied')

    def test_checkpoint_cannot_escape_and_versions_preserve_original(self):
        api=self.api()
        with tempfile.TemporaryDirectory() as directory:
            host=api.Host(self.case(),Path(directory))
            first=host.call('save_checkpoint',{'task':'A','state':'pending original'})
            second=host.call('save_checkpoint',{'task':'A','state':'pending later'})
            self.assertNotEqual(first['evidence_ref'],second['evidence_ref'])
            self.assertIn('pending original',(Path(directory)/first['evidence_ref']).read_text())
            with self.assertRaises(ValueError):host.call('save_checkpoint',{'task':'../escape','state':'x'})

    def test_public_input_excludes_grading_fields_and_values(self):
        api=self.api();public=api.public_case(self.case())
        self.assertEqual(set(public),{'prompt','tasks','global_stop'})
        self.assertNotIn('required_tasks',json.dumps(public))
        self.assertNotIn('expected',json.dumps(public))

    def test_manifest_is_36_unique_sessions_with_alternating_order(self):
        api=self.api();cases=json.loads((COLLECTOR.parent/'cases.json').read_text())['cases']
        rows=api.schedule(cases)
        self.assertEqual(len(rows),36)
        self.assertEqual(len({r['trial_id'] for r in rows}),36)
        for i in range(0,36,2):
            a,b=rows[i:i+2]
            self.assertEqual(a['case_id'],b['case_id'])
            self.assertEqual(a['replicate'],b['replicate'])
            self.assertEqual(a['condition'],'baseline' if (a['case_index']+a['replicate'])%2==0 else 'skill')

if __name__=='__main__':unittest.main()
