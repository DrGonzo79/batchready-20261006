# Phased build prompts

1. **Demand-first concierge:** Add authenticated brands/SKUs and reviewer-owned manual maps. Preserve source URL, version, and last-checked. Write migrations/auth tests first.
2. **Artifact evidence:** Add encrypted uploads, MIME/size limits, malware quarantine, hashes, retention/deletion, and expiry. Empty/failed scans stay blocked; add integration tests/runbook.
3. **Assisted extraction:** Queue OCR/model extraction behind typed adapters. Require citations/confidence, measure precision/recall, and forbid readiness changes without review.
4. **Operational launch:** Add idempotent snapshots, reviewer queue, SLA metrics, stale-rule alerts, audit export, backups, and incident runbooks. No retailer submission without written permission/rollback.
