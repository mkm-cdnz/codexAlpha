# Targeting Job Applications with LLMs (MVP)

I’m building a lightweight workflow to generate **targeted resumes and cover letters** from a single source of truth (XML + HTML templates with Internal CSS). I keep content in GitHub so I can version changes, print to PDF with clickable links, and interact directly with my custom GPT.

## Why I’m doing this

- Tailoring applications takes time, different roles need different emphasis/keywords, and squeezing everything I've done into one page is hard. This MVP helps me assemble truthful, role-specific materials faster.
- This forms part of a portfolio artifact to showcase BA thinking, documentation, and prompt design—not a finished product.
- The lessons learned from this project can be spun off & applied to generate a wide range of documentation and copy well beyond resumes & cover letters

### Pain Points

- Takes a long time to tailor my resume & cover letter
- Different industries and job titles require different emphasis and different keywords (e.g. logistics vs professional services vs creative)
- Difficult to condense all of my skills/experience into a single page
- My word processor (Google Docs) does not easily allow for columns, reorganization of layout, or inserting mailto links, leading to wasted whitespace and wasted time.

### User Stories
- As a job seeker, I want to automate the creation of bespoke resumes and cover letters that align with a given job description, so that I can target job postings with relevant factual information.

## How I use it (end-to-end)

1. **Collect the JD** (title, company, key requirements).
2. **Compare JD ↔ my employment data** and let the LLM estimate fit (green/amber/red) and call out missing skills.
3. **Generate first drafts**: a one-page resume variant and a cover-letter body (plain text/markup).
4. **Human pass**: I review, rewrite, and decide what to keep—nothing ships without my edits.
5. **Export**: I use the HTML templates and print to PDF so links stay clickable.
6. **Evaluate**: I track my applications in a Google Sheet (to log responses, industry, companies, pay bands, interview dates, outcome etc.). OpenAI's Google Drive connector means I can ask the LLM about my application history directly from the interface. Every conversation I have with my documents iteratively improves future documents.

> I originally kept work history in JSON but moved to **XML** because it’s easier for me to edit and more explicit for LLMs to parse.

## What’s here (MVP snapshot)

- Structured **work history** and **skills** (XML).
- **HTML resume** and **HTML cover-letter** templates I can quickly tailor and export to PDF.
- **System prompt** that instructs the LLM on (1) its purpose, and (2) my branding requirements

*(The repo is a work-in-progress; files and structure will evolve.)*

## Process Flow
![A screenshot of process flow in MVP](images/ProcessFlowMVP.jpg)
[Process flow on Miro](https://miro.com/app/board/uXjVJGAOjGw=/?share_link_id=19281139838)


## Guardrails & ethics (human-in-the-loop)
- I keep myself **in the loop at every stage.** I always review, rewrite, and fact-check so the output reflects my voice and thinking. No automated slop for recruiters.
- I never invent achievements or inflate scope; content must be grounded in my source data and real work.
- PDFs are exported from HTML so readers get clean layout and clickable links without gimmicks.

## Notes

- This MVP follows my process flow: fit assessment, gap spotting, drafting, and final review/export.
- I drew on prior ATS experience to keep outputs competitive yet honest.
- See [ROADMAP.md](ROADMAP.md) for forward-looking themes and planned enhancements.

## Roadmap
- For future iterations, I plan on implementing a Google Apps Sheet web scraper within my Google Sheets 'Application Tracker', to allow for bulk resume & cover letter creation, and remove pain points with manual data entry bottlenecks.  

## Contact data configuration
As I intend to make this project a public repo, I need to ensure that I do not expose PII to the entire Internet. Storing PII as variables will also future-proof the system, allowing dynamic insertion of names//email/phone numbers, etc.

- Sensitive contact fields inside `work_history_v_1_0_1.xml` use `env:` placeholders (for example, `env:CONTACT_EMAIL`) instead of storing the literal values in Git.
- When a generator or other tool needs to output a resume or cover letter, resolve each placeholder by reading the environment variable named after the suffix (e.g., `CONTACT_EMAIL`).
- Example `.env` snippet for local runs:

  ```env
  CONTACT_EMAIL="matt@example.com"
  CONTACT_PHONE="+64 22 000 0000"
  CONTACT_LINKEDIN="https://www.linkedin.com/in/example"
  CONTACT_GITHUB="https://github.com/example"
  ```
