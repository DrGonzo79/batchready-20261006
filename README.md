# BatchReady

A runnable retail-readiness prototype for small packaged-food founders. Choose a fictional SKU, declare the evidence actually on hand, inspect barcode/label/testing/logistics blockers, validate case-pack inputs, and generate a founder-review packet.

## What works
- Responsive Next.js App Router + TypeScript UI with SKU switching, evidence controls, blocker filtering, validation, loading, error, empty, and generated-packet states.
- FastAPI `/assess` reads the shared demo fixture and returns deterministic requirements, blockers, and readiness.
- Python integration tests, Playwright desktop/mobile tests, locked dependencies, GitHub Actions, and repo-base-path-aware static export.

All brands, UPCs, retailers, evidence, and launch state are fictional. This is not regulatory advice or retailer approval. No document is invented or submitted. Python is tested source and is not publicly deployed.

## Run and verify
```bash
npm ci && npm run dev
uv sync --directory api --locked
uv run --directory api uvicorn main:app --reload
npm run typecheck
uv run --directory api pytest
npm run test:e2e
npm run audit:prod
npm run build
```

See `docs/` for the diagnostic, score, plan, CEO review, architecture, and phased build prompts; `research/notes.md` summarizes the source and access limits.
