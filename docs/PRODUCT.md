# BatchReady product plan

## ICP, JTBD, and MVP
**ICP:** founder/ops lead at a 2–10 person packaged-food brand preparing a regional grocery launch. **JTBD:** “When a buyer asks for a new SKU, show me exactly what evidence is missing and assemble an internally reviewed packet before the deadline.” **MVP:** one SKU + one retailer → evidence inventory → deterministic requirement map → named blockers → owner/due date → founder-approved packet. No filing, advice, lab ordering, or autonomous retailer submission.

## Data model
`Brand`, `SKU`, `RetailerProgram`, `Requirement` (jurisdiction/version/source), `EvidenceArtifact` (type, provenance, expiry, hash), `RequirementMatch`, `ActionItem`, `ReadinessSnapshot`, and append-only `ReviewEvent`. The demo fixture is fictional and shared by frontend/API.

## Technical architecture
Static Next.js demonstrates the workflow on Pages. FastAPI owns the deterministic `/assess` operation. Production adds PostgreSQL, encrypted object storage, a versioned rules service, extraction queue, and audit log. Every claim traces to a requirement version and evidence artifact. Python needs separately approved hosting and is not live here.

## AI/model strategy
Rules decide completeness; models may only propose document classification and field extraction. Use structured output with citations, confidence thresholds, schema validation, and human confirmation. Never infer an absent artifact, make a compliance determination, or submit. Evaluate precision/recall by document type.

## Economics and offer ladder
Test a **$499 one-SKU sprint**; target ≤2.5 hours delivery and ≥70% gross margin after review. If repeat demand exists, test $149/month expiry tracking plus $199 per added retailer packet. The source-reported $1,999 roadmap is an adjacent anchor, not proof. Avoid SaaS pricing until repeat usage and maintenance costs are measured.

## Validation and GTM
Prospect from local shelves, food incubators, co-packers, brokers, and specialty-retail networks. Run 10 qualified pitches, 5 observed sessions, and seek 3 paid sprints in 30 days. Measure deposit rate, current prep time, missing count, time-to-ready, buyer corrections, support minutes, and second-SKU intent. Kill below 2 deposits; fewer than 10 qualified pitches is distribution failure.

## Moat and risks
Moat: current retailer mappings, artifact provenance/expiry, correction history, and accepted-outcome data—not prompts. Risks: stale rules, fabricated evidence, advice expectations, confidential formulas, PII, report authenticity, trademark confusion, portal terms, extraction errors, and over-trust. Use citations, freshness labels, least-privilege storage, deletion controls, review, and escalation.

## 30/60/90 roadmap
- **0–30:** five observations, ten pitches, manual maps, three paid-sprint target.
- **31–60:** encrypted artifacts, rule registry, reviewer queue, expiry alerts, correction analytics, one referral partner.
- **61–90:** two retailer templates, outcome tracking, second-SKU workflow, extraction eval set, subscription test only if repeat/margin pass.
