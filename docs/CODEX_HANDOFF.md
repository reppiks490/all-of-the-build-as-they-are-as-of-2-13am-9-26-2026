# EPOCH Ω — Engineering Handoff

## Current state

Prototype v3 is an offline, one-file HTML implementation at `app/index.html`. It is not deployed and is not integrated with GitHub or cloud accounts. The shell, feature styling, and v2 aggregate and network models live within `app/index.html`. New Phase III–V feature code is maintained in `src/phase3-engine.js` and `src/phase3-styles.css` as an extractable mirror of the inline additions. Do **not** blindly append the mirror files to the HTML without preventing duplication.

## Instructions for the next engineering session

1. Inspect the supplied project, its current implementation, and `README.md` before changing anything. Preserve users' unrelated work and existing features.
2. Establish one named GitHub repository and target branch. Verify authorization and repository-specific `AGENTS.md`, ownership rules, and current HEAD before modifying tracked files.
3. Convert the monolithic app into an accessible, componentized Vite/React/TypeScript application **only if** the migration preserves behavior and improves testability. Preserve a standalone export path.
4. Introduce a bitemporal immutable event ledger and typed source-adapter interfaces; do not treat session snapshots as live data.
5. Add source entitlements and claims classification, robust market symbol normalization, safe data imports, and time-vintage tests.
6. Move heavy simulations into Web Workers and profile memory/FPS on target iOS devices; optimize measured bottlenecks rather than claiming impossible frame rates.
7. Implement a real benchmark harness against licensed historical data. Keep Models A/B/C labeled synthetic until externally calibrated.
8. Establish accessible visual and motion design and a live diagnostic panel with FPS, frame time, memory and long-task reporting where supported.
9. Add adversarial evaluation and permissioned deployment gates. Live capital execution stays disabled pending a separate, explicit operating mandate and safety review.
10. Run tests, report exact results and failures, and do not claim any PR, merge, production launch or live-integration success without verifying it.

## Acceptance criteria for next phase

- Production-ready source contracts with unit/timestamp provenance and no future leakage.
- Replay of imported point-in-time market observations is deterministic, and late corrections preserve previous knowledge state.
- Every simulation records seed, version, inputs, statistics, and comparison baselines in a signed or hash-linked manifest.
- Tests cover same-seed repeatability, data corruption, source disagreement, no unauthorized tool execution, malicious JSON, mobile accessibility, and low-performance fallback.
- External model scores (if any) are reproduced on untouched data, contain realistic trading costs, and distinguish prediction from causality.
- Public deployments, new costs, real account access and financial execution are authorized separately.

## Known deficiencies / do not misrepresent

- The built-in sample quotes have day-granular capture dates; they do not certify historical availability at their observation timestamps.
- The order-flow engine is a simplified synthetic continuous matching model; the input shock coefficients are not empirically fitted.
- The Reality Court has 9 checks, of which some are explicitly blocked on missing empirical or causal evidence. Passing engineering checks is not a green light for deployment.
- The SHA-256 digest on a locally exported JSON is an integrity checksum over that report, not an externally witnessed or cryptographically signed provenance proof.
- The file is not a replacement for a scalable data platform; backend services are a separate, unimplemented roadmap.
