# EPOCH Ω — Reality Foundry (Version 3)

**A self-contained, offline, interactive world-model laboratory.**

Start with `app/index.html` in any standards-compliant modern browser. The browser application has no runtime dependencies, no login requirement, no network polling, no brokerage connections, and no execution endpoints. It can be opened on a laptop or smartphone browser. The source files in `src/` document the Phase III–V additions; the standalone HTML includes those additions inline.

## What works today

| Module | Implementation | Epistemic status |
| --- | --- | --- |
| World graph | Animated, pointer-reactive 12-system canvas network | Visual system map |
| Aggregate scenarios (Model A) | 2,048 fixed-seed hypothetical paths, quantile bands | Synthetic; not fitted |
| Sector network (Model B) | 768 fixed-seed runs across nine directed, coupled sectors | Synthetic; not fitted |
| Kinetic exchange (Model C) | Deterministic 240-step, price-time-priority toy matching engine; partial fills, order expiry, liquidity and forced-selling regimes | Synthetic; not exchange-validated |
| Evidence spine | User-importable source records; two-clock observations and captured-at cutoff replay | Data records can be user-supplied and unverified |
| Reconciliation | BTC/USD FMP and TickerLayer quote disagreement, timestamped and visually compared | Observational, definitions may differ |
| Reality Court | Nine executable verification and validity boundary checks | Basic engineering checks; **real-world validity blocked** |
| Evidence Passport | Manifest with records, assumptions, model summaries, test outcomes and SHA-256 digest | SHA-256 is a local checksum, **not** a signed audit attestation |
| Scenario memory | Save five hypothetical forks; user-controlled local export | No historical trading results |

## How to use

Open `app/index.html`, run the original reality reactor, inspect sectors in the lattice, import market observations into the Evidence Spine, stress the Kinetic Exchange, and run the Reality Court. Export an evidence passport to retain a reproducibility and provenance record for the captured demo state.

For imports, use `schemas/observation.v1.schema.json` and `sample-data/observation-example.json` as the contract and reference. `observedAt` is the time the value refers to. `capturedAt` is the time *this platform first obtained that value*, not necessarily the public release time. A date-only `capturedAt` only supports **day-granular** replay. Imported timestamps are self-reported and are **not automatically trusted**.

## How to test

The standalone build was tested with headless Chromium at 1440×900, 390×844 and 768×1024, including imports, provenance exports, model reruns and horizontal-overflow checks. To rerun a portable smoke test:

```bash
python -m pip install playwright
python -m playwright install chromium
python tests/smoke.py
```

The test uses Playwright `set_content` to avoid loopback/browser security restrictions in some execution environments. Tests do **not** validate market predictions. Exact result counts depend on the test fixtures and version. The complete engineering procedure, release gates and architecture are in `docs/`.

## Boundaries

- Prices and macro observations are historical **session samples**, not a streaming public data service.
- No data is silently sent to third-party services by the static HTML app.
- The models have hand-selected parameters; no causal effect in the real world is identified.
- There is no untouched point-in-time validation dataset and no verified forecast skill.
- Simulation-generated order flow is **not** a backtest of a real strategy; it is a synthetic microstructure exercise.
- No live trading, broker account access, GPU backend, cloud job, autonomous worker, or deployed service is part of this artifact.
- No claims of profitability, prediction guarantees, or production readiness.

## Research foundations

See `docs/RESEARCH.md`. The system architecture owes ideas to financial agent-based simulation, LOB validation, interventional surrogates, data vintages, causal inference, and data provenance. Citing research **does not imply this prototype implements or has validated those third-party models**.
