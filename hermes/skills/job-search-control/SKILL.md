---
name: job-search-control
description: Set up and maintain a Google Sheets job-search system.
version: 0.1.0
---
# Job Search Control

## When to Use
Use for setup, migration, profile correction, pipeline maintenance or routing job-search work.

## Procedure
1. Read private settings and references/data-model.md before any write. Verify the active Google account and exact workbook IDs. The original tracker is a migration source.
2. Diagnose installed tools and runtime from local help/metadata. Use actual supported tools; never invent connector names or CLI commands. Keep credentials private. If missing access, report the exact blocked operation and the smallest local setup step.
3. Create a separate private native Google workbook in the user's Job Hunt folder. Put Shortlist first. Apply readable frozen headers, filters, wrapped explanations and validated statuses. Present key columns first and technical IDs later.
4. Migrate all original tabs and populated fields, including dates, notes, enthusiasm, salaries, outcomes and document links. Preserve original source tab/row/reference and raw values. Resolve filenames to Drive IDs where unambiguous. Retain unmapped values in legacy_payload. Record duplicate candidates without destructive merging.
5. Reconcile imported counts and field coverage against the source; explicitly queue contradictory dates, ambiguous statuses, duplicate records and unresolved links. Keep the original available as historical evidence.
6. Import employment, skills, achievements, projects and qualifications as separate stable facts with sources. User-confirmed facts may be marked confirmed; old generated prose alone is unverified. Unknown does not mean absent. Ask focused questions only when a fact affects an active decision or document.
7. Preserve manual notes and decisions. Re-read before updating agent-owned cells by stable ID. If a target changed, refresh and reconcile instead of overwriting. Use a single writer/run lock for agent runs; queue conflicting edits.
8. Route email discovery to job-discovery, JD/letter work to job-application, and feedback evaluation to job-search-learning. Skills must read the current shared workbook, not stale chat summaries.
9. After migration is verified, mark the replacement canonical in Settings and describe the original as deprecated. Do not delete the original.

## Pitfalls
Do not treat inferred seniority, an old aspiration, a CV keyword, or a repeated generated claim as verified employment experience. Do not publish private profile/application data in GitHub.

## Verification
Read back changed records, verify stable IDs and original history preservation, record run results, and report unresolved facts without claiming migration complete.
