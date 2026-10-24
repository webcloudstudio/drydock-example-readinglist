# READINGLIST

- Short description: A web application for maintaining an ordered list of books to read.
- Status: PROJECT COMPLETE

4 of 4 receipt claims proven. Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

## Receipt

| Claim | Verdict | Recorded outcome | Proof |
|---|---|---|---|
| Lifecycle completed | PASS | 19 lifecycle commands executed; the run ended at 19-score-release. | [result.json](result.json) |
| External conformance suite passed | PASS | sh sources/full_test.sh exited 0. | [evidence/commands/16-test.stdout.log](evidence/commands/16-test.stdout.log) |
| Release score passed | PASS | drydock score release exited 0. | [evidence/commands/19-score-release.stdout.log](evidence/commands/19-score-release.stdout.log) |
| Integrity verification passed | PASS | 484 files digested; verify with sha256sum -c SHA256SUMS. | [SHA256SUMS](SHA256SUMS) |

## Run facts

- Drydock: `0.2.0` (commit `412caa6978444394f4fedca66b481b2233fb1068`)
- Provider and model: `codex` / `gpt-5.6-luna`
- Platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` on Python `3.12.13`
- Run: `20261023.210132`
- Elapsed: 877.3s
- LLM calls: 15
- Tokens: cached 2,044,288; uncached 389,090; output 57,073
- LLM elapsed: 603.8s
- Build passes: 1; repairs: 6 attempts allowed
- Conformance: passed
- Advisory scores: acceptance=exit 1, build-report=exit 0, release=exit 0

## RUN SUMMARY

- Input specification: [`sources/reading-list.md`](sources/reading-list.md)
- Delivered Code: [`build/ReadingList/`](build/ReadingList)
- Test Results: [`evidence/commands/16-test.stdout.log`](evidence/commands/16-test.stdout.log)

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock init ReadingList` | 0 | 5.3s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock import ReadingList sources --format markdown` | 0 | 3.4s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock analyze ReadingList` | 0 | 34.2s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) · [llm](evidence/commands/03-analyze.llm.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan ReadingList --override` | 0 | 133.8s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) · [llm](evidence/commands/04-plan.llm.log) |
| 05-plan-verify | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan verify ReadingList` | 0 | 8.6s | [stdout](evidence/commands/05-plan-verify.stdout.log) · [stderr](evidence/commands/05-plan-verify.stderr.log) |
| 06-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock build status ReadingList` | 0 | 0.8s | [stdout](evidence/commands/06-after-plan-build-status.stdout.log) · [stderr](evidence/commands/06-after-plan-build-status.stderr.log) |
| 07-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status ReadingList` | 0 | 0.9s | [stdout](evidence/commands/07-after-plan-target-status.stdout.log) · [stderr](evidence/commands/07-after-plan-target-status.stderr.log) |
| 08-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status` | 0 | 0.4s | [stdout](evidence/commands/08-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/08-after-plan-workspace-status.stderr.log) |
| 09-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status ReadingList --ready` | 0 | 0.8s | [stdout](evidence/commands/09-initial-ready.stdout.log) · [stderr](evidence/commands/09-initial-ready.stderr.log) |
| 10-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock build ReadingList --override --repair-attempts 6` | 0 | 609.4s | [stdout](evidence/commands/10-initial-build-1.stdout.log) · [stderr](evidence/commands/10-initial-build-1.stderr.log) · [llm](evidence/commands/10-initial-build-1.llm.log) |
| 11-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status ReadingList --ready` | 1 | 0.8s | [stdout](evidence/commands/11-initial-ready.stdout.log) · [stderr](evidence/commands/11-initial-ready.stderr.log) |
| 12-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status ReadingList --check` | 1 | 0.5s | [stdout](evidence/commands/12-initial-complete.stdout.log) · [stderr](evidence/commands/12-initial-complete.stderr.log) |
| 13-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock build status ReadingList` | 0 | 0.7s | [stdout](evidence/commands/13-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-build-status.stderr.log) |
| 14-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status ReadingList` | 0 | 0.5s | [stdout](evidence/commands/14-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/14-after-initial-build-target-status.stderr.log) |
| 15-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock status` | 0 | 0.5s | [stdout](evidence/commands/15-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/15-after-initial-build-workspace-status.stderr.log) |
| 16-test | `sh sources/full_test.sh` | 0 | 6.3s | [stdout](evidence/commands/16-test.stdout.log) · [stderr](evidence/commands/16-test.stderr.log) |
| 17-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock score ac ReadingList` | 1 | 28.9s | [stdout](evidence/commands/17-score-acceptance.stdout.log) · [stderr](evidence/commands/17-score-acceptance.stderr.log) |
| 18-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock score build ReadingList` | 0 | 0.4s | [stdout](evidence/commands/18-score-build-report.stdout.log) · [stderr](evidence/commands/18-score-build-report.stderr.log) |
| 19-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock score release ReadingList` | 0 | 37.1s | [stdout](evidence/commands/19-score-release.stdout.log) · [stderr](evidence/commands/19-score-release.stderr.log) · [llm](evidence/commands/19-score-release.llm.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`evidence/llm_logs/`](evidence/llm_logs) — call banners and token accounting
- [`result.json`](result.json) — the machine-readable record of this run
