# Validation and Release Gates

## Current tested status

- **Executed in headless Chromium:** 1440×900 desktop, 390×844 phone, 768×1024 tablet.
- **Executed UI checks:** no page JavaScript errors, no horizontal overflow, initial observations rendered, source gap $16.03, three model systems rendered, nine court verdicts displayed, filters and capture cutoff work, forced-selling scenario runs, deterministic seeded replay, valid import increments rows, malformed JSON/records rejected, malicious HTML strings displayed as inert text, state restored, evidence passport downloaded and parsed, and SHA-256 export computed with portable algorithm.
- **Result:** implementation smoke tests passed. These tests do not certify scientific accuracy or compatibility on all browsers.

## The nine Reality Court checks

| Check | Actual scope | Scientific inference |
| --- | --- | --- |
| Bitemporal types | Check field types and timestamp parseability | No as-of integrity proof |
| Append-only keys | Check no duplicated keys in in-memory dataset | No database concurrency proof |
| Deterministic replay | Compare two same-seed matching runs | No physical/market fidelity proof |
| Stress sensitivity | Compare normal and forced-selling toy regimes | No predictive validation |
| Provider conflict | Compare compatible BTC/USD quote values | A discrepancy is not source fraud |
| Model identifiability | Report Model A/B medians disagreement | Structural mechanisms remain underidentified |
| Causal identification | **Blocked** until real causal design | Cannot infer intervention effects |
| Blind holdout | **Blocked** until untouched released-before-decision data | No empirically supported forecast |
| Live capital gate | **Blocked**; no execution path | No permission for real trading |

## Proposed production gates (NOT passed or implemented)

1. **Source & legal:** every source has contractual commercial usage rights, verified symbol mapping, latency and revision semantics, raw archive, hashes, and source-health monitoring.
2. **Causal discipline:** identify estimand, manipulable intervention, assumptions, placebo and negative-control checks; downgrade claims to associative when identification fails.
3. **Time integrity:** no feature or filing is visible before the documented availability time; purge and embargo overlapping labels; freeze a fully untouched forward period.
4. **Model calibration:** compare microstructure distributions, spread/depth/impact, tail risk, volatility clustering, and conditional return distributions to real observation sets. Use independent baseline models.
5. **Model selection:** log all attempted parameter families and prompts; use nested temporal validation and a preregistered final evaluation to avoid research overfitting.
6. **Uncertainty:** publish proper scoring rules, calibration curves, regime-conditional interval coverage, parameter sensitivity, and breakdown under distribution shift. Nominal conformal coverage does not automatically survive arbitrary distribution shift.
7. **Execution economics:** explicitly model fees, bid/ask spread, slippage, impact, funding, market hours, session limits, and contract rolls; never use synthetic matching results as proof of live fills.
8. **Adversarial safety:** injection attempts, malicious files, poisoned claims, privilege escalation, runaway costs, arbitrary tool output, stale prices, and accidental cross-tenant data access must fail safely.
9. **Operations:** replayable immutable run manifests, signed deployment packages, audit trails, kill switches, independent review, current monitoring and rollback.

**Stop condition:** Any unaddressed data leakage, unauthorized execution, false causal claim, audit log corruption, or unsupported empirical performance statement blocks real-capital and production claims regardless of scores from easier tests.
