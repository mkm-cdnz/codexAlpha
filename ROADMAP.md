# Product Roadmap

This roadmap is organized around two themes highlighted in earlier planning conversations: **Foundational Enhancements** that shore up the core workflow, and **Expansion Initiatives** that layer on insights once the base is stable.

## Foundational Enhancements

### Google Sheets Syncing
- **Objective**: Establish reliable two-way syncing between the application tracker Google Sheet and the structured source of truth so that application data and document inputs stay aligned.
- **BA Value**: Removes manual reconciliation, reduces data latency, and unlocks faster fit assessments by ensuring the LLM references the freshest data.
- **Deliverables**: Apps Script jobs or API connectors for CRUD operations, sync status logging, and error handling dashboards.
- **Enablers/Dependencies**: Google Workspace API access, secure credential storage, versioned schema for Sheets ↔ XML mapping.
- **Status**: In design
- `GAP: Determine whether to prioritize Apps Script (embedded) or external service account orchestration for sync execution.`

### JD Ingestion Pipeline
- **Objective**: Automate structured capture of job descriptions (JD) from links, uploads, or pasted text into a consistent format consumable by the LLM.
- **BA Value**: Speeds up pipeline initiation, ensures requirements are normalized for comparison, and reduces context loss when prompting the LLM.
- **Deliverables**: Parsing scripts, canonical JD schema, validation prompts, and storage hooks into the source repository.
- **Enablers/Dependencies**: Reliable scraping/OCR utilities, content sanitization rules, and storage quotas.
- **Status**: Discovery
- `GAP: Decide on canonical JD intake channel (browser extension, email forward, or manual upload) and acceptable file types.`

### Automated Document Output
- **Objective**: Generate resume and cover letter drafts automatically using versioned templates tied to applicant data and JD insights.
- **BA Value**: Delivers consistent, rapid first drafts while maintaining traceability between inputs and outputs for auditability.
- **Deliverables**: Template rendering pipeline, variant selection rules, PDF export automation, and review checkpoints.
- **Enablers/Dependencies**: Stable template library, environment variable resolver for PII, and PDF rendering tooling.
- **Status**: MVP operational with manual trigger
- `GAP: Confirm whether to migrate templates to a dedicated templating engine or continue with HTML + inline CSS for maintainability.`

## Expansion Initiatives

### Analytics & Insight Layer
- **Objective**: Provide dashboards and trend analysis on application outcomes, industry segments, and experiment results to inform future targeting strategies.
- **BA Value**: Enables data-driven iteration on job targeting, highlights ROI of automation, and surfaces blockers early.
- **Deliverables**: Aggregated data model, KPI definitions, visualization layer (e.g., Looker Studio or embedded charts), and narrative commentary prompts.
- **Enablers/Dependencies**: Reliable synced data, analytics workspace access, and privacy-safe aggregation rules.
- **Status**: Backlog
- `GAP: Select analytics platform (Looker Studio vs. lightweight in-app dashboards) and define refresh cadence.`

### Expansion Connector Ideas
- **Objective**: Explore integrations beyond the core workflow, such as CRM syncing or interview preparation modules, once foundational pieces are stable.
- **BA Value**: Expands value proposition, supports multi-channel follow-ups, and strengthens differentiation for the MVP portfolio.
- **Deliverables**: Discovery briefs, prototype connectors, and stakeholder validation sessions.
- **Enablers/Dependencies**: Stable APIs from target platforms, legal/privacy review, and capacity for support.
- **Status**: Ideation
- `GAP: Prioritize which downstream systems (e.g., Airtable, Notion, CRM) deliver the highest marginal benefit for the next iteration.`
