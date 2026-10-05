---
name: job-search-learning
description: Improve job ranking from reviewed outcomes.
version: 0.1.0
author: Matt Millar, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [jobs, feedback, experiments, ranking]
    related_skills: [google-workspace]
---
# Job Search Learning

This skill proposes reversible ranking and workflow improvements from reviewed
feedback. It does not silently change career facts, preferences or policy.

## When to Use
Use after shortlist feedback, document revisions, pipeline outcomes or a requested periodic review.

## Prerequisites
- Load `job-search-control` and its data model before reading feedback or recording an experiment.
- Load the installed `google-workspace` skill and verify access to the canonical workbook.
- Require Matt's review before activating a proposed preference, policy or prompt change.

## Procedure
1. Read Feedback, PipelineEvents, Assessments, Artifacts and current confirmed Preferences. The durable workbook is the learning record; conversational memory is supplementary.
2. Capture explicit interest decisions with reasons: role content, pay, commute, culture, seniority, eligibility, scope, timing or another user-stated factor. Keep predicted interest separate from Matt's enthusiasm.
3. Record screening/interview/offer/rejection/withdrawal events with dates and source evidence. Preserve pending/no-response states and unknown reasons. Do not infer that rejection proves poor fit or that an offer proves a letter caused success.
4. Link each event to the assessment and exact submitted document versions. Record application preparation effort when supplied, so review can consider worthwhile opportunities per hour, not only application count.
5. Report descriptive counts and denominators: reviewed-to-pursue, submitted-to-screening, screening-to-interview, interview-to-offer, and known time spent. Show observation windows, sample sizes and pending records. Do not mix opportunities not applied for into employer response rates.
6. Separate three questions: what Matt wants; what evidence supports qualification; what employer outcomes have been observed. Avoid learning away from an entire role family based on a few rejections or overdue replies. Keep plausible adjacent/stretch roles visible.
7. Propose a small, explainable change tied to evidence: search expansion, ranking adjustment, missing profile evidence, a letter structure or phrasing preference. Store it in Experiments with baseline/candidate versions, expected benefit and evaluation conditions.
8. User corrections update confirmed facts/preferences with provenance. Inferred preferences, learned ranking changes and skill/prompt revisions require review before adoption. Never rewrite employment facts or branding constraints from outcomes.
9. Evaluate approved changes prospectively and report uncertainty and selection bias. Retain rollback. Do not claim statistical significance, causal improvement or model training from a small observational pipeline.

## Pitfalls
More applications is not necessarily better. Employer silence is not a reliable label. Do not train on private notes as outward-facing language or treat self-critical remarks as factual capability assessments.

## Verification
A recommendation change is explainable through linked feedback and a versioned policy. Historical assessments and documents remain reproducible. Matt can inspect, correct and reverse learned preferences.
