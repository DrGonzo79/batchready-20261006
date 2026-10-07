# CEO review

**Mode:** scope reduction. A broad autonomous agent is unjustified; validate an evidence-backed one-SKU packet.

## Premise and alternatives
The outcome is not “have AI”; it is “avoid a late retail-launch blocker with a packet the founder trusts.” Doing nothing preserves spreadsheet/email chaos, but the source does not quantify loss. The 12-month ideal is a versioned evidence graph across retailers; this prototype moves toward it through provenance and deterministic readiness.

1. **Concierge checklist (minimal, S/low):** expert assembles one packet. Fast proof; weak leverage.
2. **Evidence workspace (recommended, M/medium):** versioned requirements, artifacts, blockers, review packet. Best trust/repeatability balance.
3. **Autonomous agent (ideal, XL/high):** integrations/submissions. Premature, high liability, portal fragility.

## Review findings and decisions
- **Architecture:** keep extraction, rules, and submission separate; production uses versioned rules and immutable review events.
- **Errors:** name missing evidence, unknown SKU/type, invalid pack, stale rule, unreadable artifact, timeout, and storage failure—never generic “not ready.”
- **Security:** tenant isolation, encryption, retention/deletion, malware scanning, access logs, and no training on customer artifacts.
- **Data/interaction:** nil evidence means blocked. Make generation idempotent, preserve drafts, and warn on stale snapshots.
- **Code quality:** deterministic rules stay small/testable; model adapters remain outside readiness logic.
- **Tests:** complete/incomplete, unknown IDs, bounds, empty/loading/error, switching, and mobile. Add artifact/stale-rule tests pre-production.
- **Observability:** latency/errors, rule age, extraction confidence, overrides, correction rate, packet acceptance; alert on stale rules/overrides.
- **State:** unique brand/SKU, artifact hashes, expiry indexes, append-only reviews. No database in demo.
- **API:** production needs auth, versioning, idempotency, rate limits, snapshot IDs.
- **Performance:** parsing bottlenecks; queue scans/extraction, cap size/pages, cache by hash.
- **UX:** blockers lead; claims are user-controlled; fictional boundaries stay visible; review precedes handoff.

**Strongest challenges:** unverified WTP, rule maintenance, and over-trust/liability. **Accepted:** one-SKU assessment and review packet. **Deferred:** integrations, uploads, extraction, storage, monitoring. **Out:** compliance approval, lab work, filing, autonomous submission.
