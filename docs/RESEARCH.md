# Research evidence and disciplined uses

## Foundations relevant to EPOCH

| Research/source | Contribution | What it does **not** validate |
| --- | --- | --- |
| FABS — ACM ICAIF 2025, [paper](https://dl.acm.org/doi/10.1145/3768292.3770369), [repository](https://github.com/sonnets-project/fabs-twin) | Large-scale financial agent-based simulation and stylized facts | Market-specific predictive causality or production trading |
| TwinMarket — NeurIPS 2025, [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5bf234ecf83cd77bc5b77a24ba9338b0-Abstract-Conference.html), [repository](https://github.com/FreedomIntelligence/TwinMarket) | Socially interacting LLM agent behaviors and intervention experiments *inside* a simulator | Real-world intervention effect identification |
| Interventionally Consistent Surrogates — NeurIPS 2024, [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/26b8e3dc3a21fcd660d80c63b767f324-Abstract-Conference.html) | Preserving a parent simulator's intervention responses in an accelerated surrogate | Real-world validity beyond the parent model |
| LOB-Bench — ICML 2025, [paper](https://proceedings.mlr.press/v267/nagy25a.html), [project](https://lobbench.github.io/) | Order-book distribution and conditional-response fidelity benchmarks | Any EPOCH model quality without running the actual benchmarks |
| EconAgent — ACL 2024, [paper](https://aclanthology.org/2024.acl-long.829/) | LLM household-agent macroeconomic experiments | Empirically validated national-economy digital twin |
| INVESTORBENCH — ACL 2025, [paper](https://aclanthology.org/2025.acl-long.126/) | Financial-agent sequential decision evaluation | Real-world autonomous-trading permission or profitability |
| Ai and Ren — ICML 2024, [paper](https://proceedings.mlr.press/v235/ai24a.html) | Robust conformal prediction considerations under shift | Guaranteed coverage under unknown shifts |
| FRED/ALFRED API, [docs](https://fred.stlouisfed.org/docs/api/fred/) | Economic data source revisions and historical vintages | A point-in-time series built from ordinary latest-value queries |
| W3C PROV, [specification](https://www.w3.org/TR/prov-o/) | Provenance entity/activity/agent graph | Enforced data policy, complete audit storage or signatures |
| OpenLineage, [specification](https://openlineage.io/docs/spec/overview/) | Operational dataset/job/run lineage | Scientific causal validity |
| OpenUSD, [overview](https://openusd.org/release/intro.html) | Scene-description compositing and 3D interoperability | Real-world physical fidelity without calibration |

Research references were found through connected research services and are conceptual inputs; the current offline app does **not** bundle, train or call these research implementations. Code, dataset and model licenses require individual review before incorporation.

## Research program to beat the prototype

- Add **historical data vintages** from ALFRED, publication-timestamped SEC releases, market feed definitions and revision-aware aggregates. Test what was actually known at each decision time.
- Add **actual order-book messages** with source entitlements, session and timezone treatment, contract rolls and a held-out benchmark. Compare against LOB-Bench-style spread, depth, imbalance, event intervals, price response and order flow.
- Add **interventional consistency** instead of teaching an observational surrogate to masquerade as a causal model.
- Add **uncertainty under shifts** and do not advertise nominal conformal coverage outside validated exchangeability assumptions.
- Add a **failure-first public benchmark ledger**: version every trial and expose failed regimes and counterexamples alongside improved metrics.
