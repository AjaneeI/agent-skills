# Agent Skills behavioral validation checkpoint

October 30, 2026, America/New_York. **Partial completion: live evaluation blocked before discovery or scenario execution.**

## Executive summary

The repository audit and offline checks completed. Main's two static tests and the existing draft pilot's 41 tests passed locally. The reviewed Continuity folder was copied into a disposable project's Codex skill location and both installed files matched the pinned source hashes. Installation is not discovery: no client loaded the skill, no model request was made, and no behavioral pass or failure was observed.

The immediate blocker is isolation. A minimal macOS sandbox startup probe failed with `sandbox_apply: Operation not permitted` (exit 71). This probe does not prove every possible sandbox is unavailable; it shows that the tested nested-sandbox route cannot establish the required isolation. No attempt was made to bypass that boundary. The session stopped live preparation at this prerequisite and continued independent offline work.

## Revisions and existing work

- Technical source: [issue #1](https://github.com/AjaneeI/agent-skills/issues/1), still open.
- Main audited: `2414b9b8612dae4631805b8782f546cc61f2d406`, initially clean; no repository AGENTS.md found.
- Delivery branch: `test/agent-skills-behavioral-validation`, based on main in a new task-local clone. Existing owner checkouts were not changed.
- Existing [draft pilot PR #2](https://github.com/AjaneeI/agent-skills/pull/2): `10790eb2d6733f2569aef887d67881575a402835`. Its frozen candidate, six-case comparison, scorer and 36-session identities were inspected without modification. A separate detached audit worktree ran its existing tests.
- [Catalog PR #3](https://github.com/AjaneeI/agent-skills/pull/3) contains a separate 15-skill candidate. It was not substituted for main's 11-skill catalog.

The ten manual acceptance scenarios in `tests/scenarios.md` and the six-case paired pilot are distinct programs. This checkpoint executes neither and does not replace or reschedule the frozen pilot. The current request prioritizes manual scenarios 1, 2 and 3; earlier tracker proposals for 1, 3 and 10 remain historical proposals.

## Environment and limits

macOS 27.0.1, build 26A434, arm64; Python 3.14.7. Codex CLI 0.155.0 reports ChatGPT authentication; configured model is `gpt-6.1-sol`. Claude Code reports 2.1.293. OpenCode's version probe failed opening its existing log with EPERM; its version is unverified. Gemini CLI is absent from PATH. CodeRabbit 0.9.1 is installed and authenticated. GitHub CLI is 2.92.0.

The authorized ceiling was 60 minutes, with no paid operations. Work stopped early when live prerequisites were blocked and independent audit/documentation work was delivered. No background model process was started; model usage and tokens are unmeasured, not inferred zeros. No new model/provider, authentication method, global installation or permission setting was introduced. A runtime supervisor remains unqualified because no subject session could safely start. Historical PR #2 records rejection of the configured model through ChatGPT; that model-access gate was not retried here and remains unresolved.

## Evidence and checks

| Check | Observed result | Scope |
| --- | --- | --- |
| Main unittest discovery | 2 passed | Static catalog checks; [log](main-tests.txt) |
| Pilot unittest discovery | 41 passed | Synthetic scorer/host regression tests at `10790eb`; [log](pilot-tests.txt) |
| Pinned local installation | Two files copied and SHA-256 matched | Packaging only; [fingerprints](results.json) |
| Nested sandbox startup | Exit 71, Operation not permitted | Live isolation prerequisite blocked; [preflight](preflight.txt) |
| Historical official validator | Successful job and validator step read back | [Run 39088424759](https://github.com/AjaneeI/agent-skills/actions/runs/39088424759), not a new format-validation run |
| Historical packaging jobs | Four successful client jobs read back | [Run 39088539870](https://github.com/AjaneeI/agent-skills/actions/runs/39088539870), not observed client behavior |

Reproduce offline checks at each named revision with `python3 -m unittest discover -s tests -p 'test_*.py' -v`. Raw unittest logs are generated execution evidence. `preflight.txt` is an operator transcription of observed tool outputs, clearly distinguished from native agent traces. No secrets or authentication material are included.

## Behavioral matrix

| Client | Discovery / activation | Scenarios 1–3 | Scenarios 4–10 |
| --- | --- | --- | --- |
| Codex | BLOCKED | BLOCKED before execution | NOT RUN |
| Claude Code | NOT RUN | NOT RUN | NOT RUN |
| Gemini CLI | BLOCKED: executable unavailable | NOT RUN | NOT RUN |
| OpenCode | BLOCKED: version probe failed | NOT RUN | NOT RUN |

All ten additional skills' positive and negative cases are NOT RUN. Their declared purposes, triggers and referenced smoke specifications were inspected. [results.json](results.json) lists all 40 client/scenario dispositions and 20 additional-skill dispositions. Correctness, authorized continuity, boundary compliance and reporting integrity remain null because there are no subject observations. No prohibited-action count can be inferred. Cross-client results are NOT COMPARABLE: there are no equivalent executed observations.

Expected behavior remains the original `tests/scenarios.md` contract: preserve blocked A and perform authorized B; avoid repeated approval loops; preserve failed one-shot evidence without retry. The remaining seven expectations and all positive/negative smoke criteria remain unchanged in their source specifications.

## Findings and corrections

No behavioral defect was identified because no behavioral scenario ran. No skill, scorer, scenario, CI workflow or runtime implementation changed.

A CLI compatibility issue was observed: `gh skill list --agent codex --scope project` fails on this installed version, whose skill subcommands omit `list`. README and the installation workflow contain that command. Historical green installation runs remain valid historical evidence; they do not prove the same command works on this current CLI. A direct byte-verified copy established local placement instead. This report records the issue without changing the existing workflow or claiming a discovery fix.

CodeRabbit is available and authenticated, correcting the earlier environment's missing-CLI limitation. No review was run: this delivery changes evidence documents only, and the session did not establish a zero-charge review entitlement under the no-paid-services constraint. Authentication alone does not establish that entitlement. The report received an author review; it has no independent or CodeRabbit review claim.

## Checkpoints and next safe actions

1. Audit complete: confirmed main, clean starting tree, existing PRs, historical CI and canonical tracker records. Evidence: this report, source fingerprints and referenced GitHub runs.
2. Runtime prerequisite blocked: preserved sandbox startup failure; no subject invocation. Current branch is the delivery branch above, initially at the audited main SHA. Discovery, model access, trusted capture, supervisor qualification and live cases remain open.
3. Offline verification complete: 2 main tests and 41 existing pilot tests passed. Authorized remaining delivery work is to commit this evidence, open a draft PR, and reconcile the existing issue/trackers. The delivery commit is identified by the containing Git commit and draft PR; no self-referential commit hash is fabricated here.

The next live dependency is an already-authorized environment that can enforce filesystem, credential, network and side-effect isolation without disabling protections, plus verified access to the fixed model. Then prove pinned discovery/activation and trustworthy trace capture before invoking scenarios 1–3. A paired pilot also requires its existing baseline-isolation and independent collector-review gates. Do not retry a frozen trial, substitute a model, weaken expectations, or treat this report as qualification. Issue #1 remains unfinished.
