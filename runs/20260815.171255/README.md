# ReadingList: PASSED

6 of 6 receipt claims proven. Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

## Receipt

| Claim | Verdict | Recorded outcome | Proof |
|---|---|---|---|
| Lifecycle completed | PASS | 30 lifecycle commands executed; the run ended at 30-score-release. | [result.json](result.json) |
| External conformance suite passed | PASS | sh bin/test.sh exited 0. | [evidence/commands/27-test.stdout.log](evidence/commands/27-test.stdout.log) |
| Target completion check passed | PASS | drydock status ReadingList --check exited 0. | [evidence/commands/23-refit-1-complete.stdout.log](evidence/commands/23-refit-1-complete.stdout.log) |
| Acceptance score passed | PASS | drydock score acceptance exited 0. | [evidence/commands/28-score-acceptance.stdout.log](evidence/commands/28-score-acceptance.stdout.log) |
| Release score passed | PASS | drydock score release exited 0. | [evidence/commands/30-score-release.stdout.log](evidence/commands/30-score-release.stdout.log) |
| Integrity verification passed | PASS | 949 files digested; verify with sha256sum -c SHA256SUMS. | [SHA256SUMS](SHA256SUMS) |

## Run facts

- Drydock: `unknown` (commit `4d3bb927bfd3a4c7bc31b51fa27713be9ae48cd4`)
- Provider and model: `codex` / `gpt-5.6-luna`
- Platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` on Python `3.12.13`
- Target: `ReadingList`
- Run: `20260815.171255`
- Ran: 2026-08-15 13:12:55 EDT — 2026-08-15 13:40:26 EDT
- Elapsed: 1650.8s
- LLM calls: 17
- Tokens: cached 3,759,104; uncached 526,184; output 56,892
- LLM elapsed: 1381.7s
- Build passes: 2; repairs: 6 attempts allowed
- Conformance: passed
- Verdict: expected PASSED, observed PASSED
- Advisory scores: acceptance=exit 0, build-report=exit 0, release=exit 0

## RUN SUMMARY

- Input specification: [`sources/reading-list.md`](sources/reading-list.md)
- Delivered Code: [`build/ReadingList/`](build/ReadingList)
- Test Results: [`evidence/commands/27-test.stdout.log`](evidence/commands/27-test.stdout.log)

## RUN NOTES:

- One run is evidence of one run. It is not a benchmark.
- It is not a security certification of the delivered code.

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock init ReadingList` | 0 | 2.2s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import ReadingList sources --format markdown` | 0 | 1.9s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock analyze ReadingList` | 0 | 57.9s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) · [llm](evidence/llm_logs/20260815.171300.938Z_readinglist_analyze_codex.llm.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock plan ReadingList --override` | 0 | 218.9s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) · [llm](evidence/llm_logs/20260815.171359.143Z_readinglist_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.171452.254Z_readinglist_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.171609.224Z_readinglist_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.171713.601Z_readinglist_lineage_attribute_codex.llm.log) |
| 05-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 2.2s | [stdout](evidence/commands/05-after-plan-build-status.stdout.log) · [stderr](evidence/commands/05-after-plan-build-status.stderr.log) |
| 06-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.9s | [stdout](evidence/commands/06-after-plan-target-status.stdout.log) · [stderr](evidence/commands/06-after-plan-target-status.stderr.log) |
| 07-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.3s | [stdout](evidence/commands/07-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/07-after-plan-workspace-status.stderr.log) |
| 08-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 0 | 0.7s | [stdout](evidence/commands/08-initial-ready.stdout.log) · [stderr](evidence/commands/08-initial-ready.stderr.log) |
| 09-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build ReadingList --override --repair-attempts 6` | 0 | 1092.5s | [stdout](evidence/commands/09-initial-build-1.stdout.log) · [stderr](evidence/commands/09-initial-build-1.stderr.log) |
| 10-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 1 | 0.3s | [stdout](evidence/commands/10-initial-ready.stdout.log) · [stderr](evidence/commands/10-initial-ready.stderr.log) |
| 11-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --check` | 0 | 0.3s | [stdout](evidence/commands/11-initial-complete.stdout.log) · [stderr](evidence/commands/11-initial-complete.stderr.log) |
| 12-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.7s | [stdout](evidence/commands/12-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/12-after-initial-build-build-status.stderr.log) |
| 13-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.9s | [stdout](evidence/commands/13-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-target-status.stderr.log) |
| 14-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.4s | [stdout](evidence/commands/14-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/14-after-initial-build-workspace-status.stderr.log) |
| 15-import-update-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import ReadingList --update` | 0 | 2.4s | [stdout](evidence/commands/15-import-update-1.stdout.log) · [stderr](evidence/commands/15-import-update-1.stderr.log) |
| 16-refit-update-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock refit ReadingList --sources` | 0 | 19.1s | [stdout](evidence/commands/16-refit-update-1.stdout.log) · [stderr](evidence/commands/16-refit-update-1.stderr.log) · [llm](evidence/llm_logs/20260815.173559.126Z_readinglist_refit_sources_route_codex.llm.log) |
| 17-after-refit-1-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.7s | [stdout](evidence/commands/17-after-refit-1-build-status.stdout.log) · [stderr](evidence/commands/17-after-refit-1-build-status.stderr.log) |
| 18-after-refit-1-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.9s | [stdout](evidence/commands/18-after-refit-1-target-status.stdout.log) · [stderr](evidence/commands/18-after-refit-1-target-status.stderr.log) |
| 19-after-refit-1-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.5s | [stdout](evidence/commands/19-after-refit-1-workspace-status.stdout.log) · [stderr](evidence/commands/19-after-refit-1-workspace-status.stderr.log) |
| 20-refit-1-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 0 | 1.0s | [stdout](evidence/commands/20-refit-1-ready.stdout.log) · [stderr](evidence/commands/20-refit-1-ready.stderr.log) |
| 21-refit-1-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build ReadingList --override --repair-attempts 6` | 0 | 147.1s | [stdout](evidence/commands/21-refit-1-build-1.stdout.log) · [stderr](evidence/commands/21-refit-1-build-1.stderr.log) |
| 22-refit-1-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 1 | 0.3s | [stdout](evidence/commands/22-refit-1-ready.stdout.log) · [stderr](evidence/commands/22-refit-1-ready.stderr.log) |
| 23-refit-1-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --check` | 0 | 0.3s | [stdout](evidence/commands/23-refit-1-complete.stdout.log) · [stderr](evidence/commands/23-refit-1-complete.stderr.log) |
| 24-after-refit-1-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.6s | [stdout](evidence/commands/24-after-refit-1-build-build-status.stdout.log) · [stderr](evidence/commands/24-after-refit-1-build-build-status.stderr.log) |
| 25-after-refit-1-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.8s | [stdout](evidence/commands/25-after-refit-1-build-target-status.stdout.log) · [stderr](evidence/commands/25-after-refit-1-build-target-status.stderr.log) |
| 26-after-refit-1-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.3s | [stdout](evidence/commands/26-after-refit-1-build-workspace-status.stdout.log) · [stderr](evidence/commands/26-after-refit-1-build-workspace-status.stderr.log) |
| 27-test | `sh bin/test.sh` | 0 | 3.2s | [stdout](evidence/commands/27-test.stdout.log) · [stderr](evidence/commands/27-test.stderr.log) |
| 28-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score ac ReadingList` | 0 | 36.6s | [stdout](evidence/commands/28-score-acceptance.stdout.log) · [stderr](evidence/commands/28-score-acceptance.stderr.log) |
| 29-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score build ReadingList` | 0 | 0.3s | [stdout](evidence/commands/29-score-build-report.stdout.log) · [stderr](evidence/commands/29-score-build-report.stderr.log) |
| 30-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score release ReadingList` | 0 | 52.4s | [stdout](evidence/commands/30-score-release.stdout.log) · [stderr](evidence/commands/30-score-release.stderr.log) · [llm](evidence/llm_logs/20260815.173931.006Z_readinglist_score-release_codex.llm.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`evidence/llm_logs/`](evidence/llm_logs) — call banners and token accounting
- [`result.json`](result.json) — the machine-readable record of this run
