# Google Sheets contract v0.1

A single private workbook is the initial shared store. Every record has a stable UUID, created_at, updated_at, updated_by and revision. UTC ISO timestamps plus Pacific/Auckland display; preserve source dates and uncertainty. Never use row position as identity. IDs and versions are text, not formulas. Write external strings as literal values to prevent formula interpretation.

## Tabs
- Settings: key, value, origin, confirmation_status. Includes IDs, mailbox, schedule, timezone, limits, schema version, canonical workbook and policy version.
- ProfileFacts: fact_id, category (employment/skill/project/achievement/qualification/contact), subject, statement, employer_or_project, start_date, end_date, proficiency, source_id, evidence_excerpt, confirmation_status (unverified/confirmed/disputed/retired), confirmed_at, supersedes_fact_id.
- Preferences: preference_id, dimension, value, strength (guideline/hard), reason, source, confirmed_at. Salary guidelines permit part-time and high-interest exceptions. Auckland/remote remain provisional until confirmed.
- Sources: source_id, type, private_url_or_file_id, title, modified_at, captured_at, content_hash, extraction_status. Preserve raw source privately; never republish emails.
- Opportunities: job_id, employer, title, requisition_id, canonical_url, source_ids, location, work_arrangement, contract_type, hours_per_week, salary_min, salary_max, salary_currency, salary_basis (annual/hourly/unknown), salary_actual_or_fte, posted_at, closes_at, availability (open/closed/unknown), jd_source_id, jd_hash, first_seen, last_seen, dedupe_key, legacy_payload.
- Assessments: assessment_id, job_id, assessed_at, profile_revision, policy_version, model_id, skill_version, fit_band (strong/transferable/stretch/insufficient_information), recommendation (apply/research/consider/deprioritise), matches_with_fact_ids, gaps, hard_constraints, unknowns, interest_hypothesis, rationale, confidence. Append revisions.
- Shortlist: job_id, employer, title, recommendation, fit_band, why_worth_time, gaps_unknowns, salary_summary, location, closing_date, listing_link, review_decision (unreviewed/pursue/maybe/skip), matt_enthusiasm_1_5, decision_reason, next_action, assessment_id. Agent owns factual/assessment columns; Matt owns decisions, enthusiasm and notes.
- Applications: application_id, job_id, current_stage, submitted_at, last_activity_at, next_action, next_action_date, cv_artifact_id, letter_artifact_id, private_notes, legacy_source_id. Stages: shortlisted/researching/drafting/ready/submitted/screening/interview/offer/accepted/rejected/withdrawn/closed. Stage must be evidenced or user-set; a draft is never submitted.
- PipelineEvents: event_id, application_id, job_id, occurred_at, event_type, old_stage, new_stage, actor, source_id, reason, certainty, dedupe_key. Append-only; corrections link to superseded events. Store actual event timing separately from discovery timing. No response is a pending condition, not a rejection.
- Artifacts: artifact_id, application_id, type, version, private_drive_id, content_hash, fact_ids, jd_hash, brand_version, template_version, model_id, skill_version, review_status, generated_at, submitted_at. Preserve the exact submitted version.
- Feedback: feedback_id, job_id, application_id, assessment_id, artifact_id, actor, type, reason_code, comment, recorded_at. Separate Matt decisions, recruiter statements and agent hypotheses.
- Experiments: experiment_id, hypothesis, proposed_change, evidence_ids, baseline_version, candidate_version, status (proposed/approved/running/evaluated/reverted), evaluation_window, results, limitations, approved_at.
- ReviewQueue: issue_id, affected_ids, issue_type, question, sources, priority, status, resolution.
- Runs: run_id, started_at, ended_at, window_start, window_end, cursor, status, messages_seen, jobs_added, jobs_updated, failures, retry_ids, checkpoint, cost_if_available, model_id, skill_version.

## Write contract
Use upserts only where appropriate; append assessments/events/artifact versions. Before writing, read the current row by ID and verify revision. Sheets does not provide database transactions: serialize agent writes, verify each batch and reconcile partial writes before moving the run checkpoint. Maintain stable event/message keys and pending retries across failures. Never wipe a workbook to rebuild the shortlist. Presentation sorting must not change record identity.

## Migration
Copy historical values without interpreting self-critical notes as career facts. Preserve the original even if it appears wrong. Unknown dates stay unknown. Keep conflicting statements in ReviewQueue. Historical application dates, blank statuses and document-name links need explicit reconciliation. Do not calculate historical conversion rates from unverified timestamps.
