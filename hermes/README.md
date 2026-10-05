# Job Search POC for Hermes

Status: installed and indexed on Nitro; Google integration testing is blocked on Hermes OAuth.
These are Hermes skills, not a ChatGPT plugin. Install only after identifying the local Hermes version, active profile and supported integration tools. Skills provide procedures; authenticated tools perform Gmail/Drive/Sheets operations.

## Validate and install

Run the repository validator first:

```text
python hermes/scripts/validate_poc.py
```

To install into a specific Hermes home without guessing profile paths:

```text
python hermes/scripts/validate_poc.py --install --hermes-home PATH_TO_HERMES_HOME
```

Installation is deliberately non-destructive. It refuses to replace an existing
skill directory unless `--force` is supplied. Start a new Hermes session after
installation because the skill index is cached per session.

## Setup order
1. In the existing Hermes chat, request a read-only diagnostic: version, OS/runtime, active profile, available Google/GitHub tools, authenticated account identity, scheduler availability. Do not reveal tokens, environment values, email bodies or credential files.
2. Verify the intended mailbox with the user. Test one job-alert search, one Drive file read, and tracker metadata read. ChatGPT connections do not transfer to Hermes.
3. Configure the private settings in Google Sheets. Use config.example.json as a key checklist; never commit populated configuration, OAuth credentials, email, CVs or application records to this public repository.
4. Load each skills/*/SKILL.md and its references using the installed Hermes version's supported skill installation method. Official reference: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
5. Use job-search-control to stage a new workbook and migrate records. Do not deprecate the original tracker until reconciliation succeeds.
6. Run job-discovery manually over the previous 30 days. Review real extraction/fit results and rerun to verify idempotence.
7. Enable one daily local schedule only after manual success. Check actual timezone and scheduler support. Catch up after sleep/offline periods. See https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/

## Required private configuration
Mailbox; original tracker ID; replacement workbook ID; Job Hunt folder ID; brand folder ID; canonical brand spec/guide/token/asset IDs; model/provider; daily time; timezone; run cost limit; skill version.
Use the approved mailbox, folder links and preferences from the setup conversation. Do not guess replacements.
Google Sheets is authoritative for career facts/preferences and operational records. Hermes memory may hold pointers and workflow preferences; it must not override current Sheets facts.

## Delivery stages
A. Diagnose/install/authenticate.
B. Create Google Sheets data model; migrate original records and confirmed career facts.
C. Email discovery and ranked review.
D. Manual JD assessment and brand-compliant drafting.
E. Pipeline feedback and measured, reversible improvements.

## Acceptance gates
- Duplicate email/listing replay adds no duplicate job or event.
- One multi-job alert yields separate opportunities with source provenance.
- Unavailable JD produces limited-confidence assessment, not invented requirements.
- Part-time and unknown salary cases remain reviewable.
- Human notes/status decisions survive agent reruns.
- Interrupted writes resume without skipping messages or duplicating rows.
- An unreviewed skill claim cannot enter a final cover letter.
- A no-response record does not become a rejection or evidence of incompetence.
- Email text requesting credentials or tool execution is treated as data.
- Real branded output passes visual print/PDF inspection before delivery.
- Migration reports row counts, duplicates, unresolved links and all unmapped fields.

## Current limitations
No Google workbook has been created by this repository addition. No account is connected, no schedule is activated, no live job search has run, and no application is submitted. Local installation and full end-to-end validation are required.

## Nitro diagnostic snapshot (2026-10-05)

- Dashboard reachable at `127.0.0.1:9119`; Hermes `0.21.5+6642` on Windows 11.
- Gateway starts successfully after an explicit restart.
- `google-workspace` skill `1.2.0` is installed and enabled.
- Google Workspace check returns `NOT_AUTHENTICATED`; OAuth must be completed in Hermes before mailbox, Drive or Sheets tests.
- No MCP servers are configured. Google access for this POC should use the bundled `google-workspace` skill, not an invented MCP server.
- Host pressure is material: roughly 3.5 GB disk free and more than 90% memory in use during the diagnostic. Free space before any update or large document migration.
