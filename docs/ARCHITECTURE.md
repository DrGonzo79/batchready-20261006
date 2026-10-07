# Architecture

```text
Fictional shared JSON fixture
        ├── Next.js static UI → local evidence state → founder-review packet
        └── FastAPI /assess → validation → requirement/evidence join → blockers
```

GitHub Pages serves only the static export; it does not run FastAPI. The API is independently runnable/tested source. Builds derive `basePath` and `assetPrefix` from `GITHUB_REPOSITORY`.

Production: authenticated Next.js → versioned FastAPI → PostgreSQL metadata + encrypted object storage; separate worker for scanning/OCR/model extraction. Deterministic rules generate readiness. Model fields carry source locations/confidence until confirmed. Audit events record overrides and packet generation.
