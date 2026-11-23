# Connector topology — planned, not integrated into static v3

The user named a broad tool ecosystem. **The standalone HTML app does not call any connected app.** The following is a sensible division of responsibility to avoid indiscriminate access to private accounts, duplicate data cost, and overlapping agents.

| Domain | Proposed adapters and systems | Scope and permission |
| --- | --- | --- |
| Market data and quantitative research | Hey-Traders, FactorWeave, TickerLayer, The Economist – Graphs, Exum, CoinGecko, Blockscout, Zacks, Public Equity Investing, Institutional Equity Analyst, EdgePilot Research, DayTrading.Monster, U.S. Gold Bureau Metal Spots, FMP, Bybit, Massive, Next Stock, Unusual Whales | Read-only public evidence by default; separate normalized symbol, timing and source contracts |
| Private finance | Finances | Opt-in user-scoped finance data; never intermix with public demo datasets or publish automatically |
| Research and verification | Scite, Exa, Tavily, Parallel, Firecrawl, Hugging Face, NVIDIA Skills, omgskills, Deep Research | Evidence sourcing, literature, public code, model/dataset discovery and reproducibility constraints |
| Engineering governance | Codex Coordinator, Baton Pass, Founder Pulse, Superpowers, Astral Orchestrator, Akinator, Capability Orchestrator, Trellis, EW AI Coding | Task ownership, verified handoff, explicit execution observations, repository-change controls and reviews |
| Repository and deployment | GitHub, Linear, Supabase, Railway | Repository, work tracking, database, streaming, CI/CD and environment deployment only after a named target and authorization |
| Motion and interactive design | MotionDesign, MagicPath, Figma | User experience, motion, editable screens and the architectural FigJam map |
| Visual and video production | Cecil-IA Labs FFmpeg, Videomagic, HyperFrames by HeyGen, Runway, Hypernatural, Voyager 3D, PINOC | Cinematic exports, rigged/3D assets and video-model workflows on supported media; no fake claims of feature equivalence |
| Growth and measurement | Marketing Swarm, Master Metrics | Consent-based analytics, marketing experiments and outcome measurement |
| Additional exploration | Akinator and other user-named special-purpose skills | Only if the actual bounded task matches a supported operation |

## Current access observations from the session

- FMP, TickerLayer, CoinGecko and Bybit returned market/macro data used as *static session examples*; price timestamps and definitions are retained.
- Figma generated an interactive architectural diagram in the pre-existing FigJam board at <https://www.figma.com/board/XWSGtbBiFEMxJOieJ7d3dO>.
- TickerLayer's bond-yield endpoint returned a plan-access restriction; the FMP treasury series was usable instead.
- Unusual Whales' market-state endpoint returned a free-plan restriction.
- The U.S. Gold Bureau request was blocked by service IP authorization.
- The Blockscout request required an explicit unlock/session step; no blockchain data were ingested.
- No matching EPOCH Linear project or GitHub EPOCH repository was discovered in the available read-only checks.
- No cloud project was created, no repo was modified, and no API credentials or private finance records were acquired.

## Integration acceptance contract

Every new source adapter must document: exact method and authentication scope, licensed usage, instrument and unit identities, event and availability timestamps, delay and revision semantics, failure behavior, rate limiting, schema validation, retry/idempotency behavior, provenance fields, and a source-vs-destination reconciliation test. Only adapters meeting that contract can feed a model gate.
