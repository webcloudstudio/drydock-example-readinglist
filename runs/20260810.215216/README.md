# ReadingList: PASSED

Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

- Target: `ReadingList`
- Run: `20260810.215216`
- Provider and model: `codex` / `gpt-5.6-luna`
- Elapsed: 949.7s
- Build passes: 2
- LLM calls: 12
- Tokens: cached 1,428,992; uncached 284,909; output 35,691
- LLM elapsed: 793.6s
- Advisory scores: acceptance=exit 1, build-report=exit 0, release=exit 1

## Manual verification required

The release gate completed. It could not settle the following project guardrails from evidence, so each needs a manual check before release.

- Guardrail st-008 is UNPROVEN (criterion st-008 has no supplied evidence): The application shall never transmit a reader's list to a third-party service.

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock init ReadingList` | 0 | 0.8s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import ReadingList sources --format markdown` | 0 | 0.9s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock analyze ReadingList` | 0 | 67.0s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock plan ReadingList --override` | 0 | 188.6s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) |
| 05-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.5s | [stdout](evidence/commands/05-after-plan-build-status.stdout.log) · [stderr](evidence/commands/05-after-plan-build-status.stderr.log) |
| 06-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.7s | [stdout](evidence/commands/06-after-plan-target-status.stdout.log) · [stderr](evidence/commands/06-after-plan-target-status.stderr.log) |
| 07-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 1.0s | [stdout](evidence/commands/07-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/07-after-plan-workspace-status.stderr.log) |
| 08-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 0 | 0.6s | [stdout](evidence/commands/08-initial-ready.stdout.log) · [stderr](evidence/commands/08-initial-ready.stderr.log) |
| 09-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build ReadingList --override` | 0 | 488.1s | [stdout](evidence/commands/09-initial-build-1.stdout.log) · [stderr](evidence/commands/09-initial-build-1.stderr.log) |
| 10-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 1 | 0.7s | [stdout](evidence/commands/10-initial-ready.stdout.log) · [stderr](evidence/commands/10-initial-ready.stderr.log) |
| 11-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --check` | 0 | 0.6s | [stdout](evidence/commands/11-initial-complete.stdout.log) · [stderr](evidence/commands/11-initial-complete.stderr.log) |
| 12-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.5s | [stdout](evidence/commands/12-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/12-after-initial-build-build-status.stderr.log) |
| 13-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 1.7s | [stdout](evidence/commands/13-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-target-status.stderr.log) |
| 14-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.5s | [stdout](evidence/commands/14-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/14-after-initial-build-workspace-status.stderr.log) |
| 15-import-update-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import ReadingList --update` | 0 | 0.4s | [stdout](evidence/commands/15-import-update-1.stdout.log) · [stderr](evidence/commands/15-import-update-1.stderr.log) |
| 16-refit-update-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock refit ReadingList --sources` | 0 | 16.3s | [stdout](evidence/commands/16-refit-update-1.stdout.log) · [stderr](evidence/commands/16-refit-update-1.stderr.log) |
| 17-after-refit-1-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.7s | [stdout](evidence/commands/17-after-refit-1-build-status.stdout.log) · [stderr](evidence/commands/17-after-refit-1-build-status.stderr.log) |
| 18-after-refit-1-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 1.1s | [stdout](evidence/commands/18-after-refit-1-target-status.stdout.log) · [stderr](evidence/commands/18-after-refit-1-target-status.stderr.log) |
| 19-after-refit-1-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.4s | [stdout](evidence/commands/19-after-refit-1-workspace-status.stdout.log) · [stderr](evidence/commands/19-after-refit-1-workspace-status.stderr.log) |
| 20-refit-1-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 0 | 0.2s | [stdout](evidence/commands/20-refit-1-ready.stdout.log) · [stderr](evidence/commands/20-refit-1-ready.stderr.log) |
| 21-refit-1-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build ReadingList --override` | 0 | 144.6s | [stdout](evidence/commands/21-refit-1-build-1.stdout.log) · [stderr](evidence/commands/21-refit-1-build-1.stderr.log) |
| 22-refit-1-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --ready` | 1 | 0.2s | [stdout](evidence/commands/22-refit-1-ready.stdout.log) · [stderr](evidence/commands/22-refit-1-ready.stderr.log) |
| 23-refit-1-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList --check` | 0 | 0.3s | [stdout](evidence/commands/23-refit-1-complete.stdout.log) · [stderr](evidence/commands/23-refit-1-complete.stderr.log) |
| 24-after-refit-1-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status ReadingList` | 0 | 0.5s | [stdout](evidence/commands/24-after-refit-1-build-build-status.stdout.log) · [stderr](evidence/commands/24-after-refit-1-build-build-status.stderr.log) |
| 25-after-refit-1-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status ReadingList` | 0 | 0.5s | [stdout](evidence/commands/25-after-refit-1-build-target-status.stdout.log) · [stderr](evidence/commands/25-after-refit-1-build-target-status.stderr.log) |
| 26-after-refit-1-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.5s | [stdout](evidence/commands/26-after-refit-1-build-workspace-status.stdout.log) · [stderr](evidence/commands/26-after-refit-1-build-workspace-status.stderr.log) |
| 27-test | `sh bin/test.sh` | 0 | 2.9s | [stdout](evidence/commands/27-test.stdout.log) · [stderr](evidence/commands/27-test.stderr.log) |
| 28-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score ac ReadingList` | 1 | 0.7s | [stdout](evidence/commands/28-score-acceptance.stdout.log) · [stderr](evidence/commands/28-score-acceptance.stderr.log) |
| 29-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score build ReadingList` | 0 | 0.4s | [stdout](evidence/commands/29-score-build-report.stdout.log) · [stderr](evidence/commands/29-score-build-report.stderr.log) |
| 30-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score release ReadingList` | 1 | 24.8s | [stdout](evidence/commands/30-score-release.stdout.log) · [stderr](evidence/commands/30-score-release.stderr.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`result.json`](result.json) — the machine-readable record of this run
