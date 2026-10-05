---
name: job-application
description: Assess roles and draft grounded applications.
version: 0.1.0
author: Matt Millar, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [jobs, applications, cover-letters, evidence]
    related_skills: [google-workspace]
---
# Job Application

This skill assesses a role against confirmed evidence and drafts application
material for review. It does not send messages, complete forms or submit an
application.

## When to Use
Use when Matt provides a JD, title and employer, selects a shortlisted role, or requests a CV/cover letter revision.

## Prerequisites
- Load `job-search-control`, its data model and the current confirmed profile facts before making personal claims.
- Load the installed `google-workspace` skill before reading private Drive or Sheets sources.
- Resolve and read the canonical V2 brand specification before describing output as brand-validated.

## Procedure
1. Load current confirmed profile facts, preferences and source-linked job requirements. Persist the supplied JD and reuse an existing job ID where matched.
2. Map each material requirement to confirmed fact IDs, transferable evidence, a gap or unknown. Separate essential eligibility from trainable preferences. Explain strong/transferable/stretch/insufficient-information fit without fabricated numeric probability.
3. Research the employer from identifiable sources when useful. Record links and date. Do not confuse generic company marketing with the actual team's culture. Offer a clear apply/research/consider/deprioritise recommendation.
4. Draft for the specific employer and JD using grounded examples. Identify where the user needs to supply a missing fact. Do not invent metrics, scope, certifications, tool proficiency or dates. Never import private tracker notes, sensitive personal context or criticisms of former employers into outward documents without specific user direction.
5. Read the configured current brand-spec.json first, then canonical SVG assets, brand guide, templates/examples and legacy materials in that precedence. Fetch privately from the official brand folder. If the specification cannot be read, report the unresolved dependency; do not call the result fully brand-validated.
6. Known V2 guide constraints: warm, practical plain English; no hype; Segoe UI/Tahoma/Geneva/Verdana/sans-serif; cover letter single column; 11pt print body at approximately 1.45 line height; approved dark gradient header optional. Resume A4 with 35/65 sidebar/main layout. Primary #2c3e50, secondary #34495e, accent #3498db, accent dark #2980b9, body #333333, muted #7f8c8d, border #ecf0f1, white background. Confirm all against the live spec before final rendering.
7. Use canonical logo assets unchanged. If unavailable, the V2 guide permits exact numeric geometry only; never improvise a monogram. Use contact values from confirmed configuration, with mailto/tel links. Old 11px instructions do not override V2 11pt print typography.
8. Store structured letter content separately from its HTML template so text revisions do not change branding. Generate HTML/PDF when requested; review A4 print layout, font fallback, contrast, clickable contacts, clipping and page breaks. Do not shrink text merely to force a page limit.
9. Save each draft/revision privately with source fact IDs, JD hash, brand/template/model/skill versions. Record Matt's edits and reasons as feedback. Preserve the exact version used for an application.
10. Advance pipeline stages only on evidence or Matt's decision. Drafting does not authorize sending, filling external forms or submitting an application.

## Pitfalls
Past generated applications are writing examples, not independent factual corroboration. Keep employer facts distinct from speculation. Optimize relevance and truth, not keyword repetition.

## Verification
Every material personal claim maps to a confirmed fact. All placeholders are resolved in final documents. Verify official brand precedence and rendered output before marking ready. Record any unresolved factual or branding limitation.
