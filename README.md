# AI Film Studio

> **AI-powered end-to-end film production system.** Transform a one-line idea into a complete production package: concept, script, shot list, image & motion prompts (10-Layer A-J), audio plan, and assembly guide.

[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Standard](https://img.shields.io/badge/standard-Agent%20Skills%20Standard-orange.svg)](#)

## What is it?

AI Film Studio is a **production-system skill** for AI agents (Claude, GPT, Gemini, etc.) that simulates a complete film studio. It contains:

- **31 specialist roles** (Creative Director, DP, Sound Designer, Editor, Colorist, Continuity Supervisor, etc.)
- **12 production stages** (M0–M11) materialized as **31 workflows** (see `workflows/M*.md`)
- **10-Layer Prompt Architecture (A–J)** for any image/video generation model
- **8 Quality Gates** with hard gates at G4 (prompts) and G8 (master)
- **5 production packages** as final deliverables
- **Orchestration Runtime**: 10 executable routes (REPAIR، SINGLE_PROMPT، IMAGE_GEN، I2V، MOTION_GFX، LIPSYNC، CONCEPT، SHOT_BUILD، SCENE_BUILD، FULL_PRODUCTION) — see `references/protocols/orchestration-runtime.md`
- **Memory Conflict Resolution**: 6 conflict types (NoConflict، ShotOverride، SceneOverride، ProjectCanonical، UserApproved، Ambiguous) — see `references/knowledge/memory-conflict-contract.md`

## Quick Start

```bash
# 1. Clone
git clone https://github.com/zoih6/ai-film-studio.git

# 2. For an agent: read SKILL.md first
# For humans: read this README + workflows/intent-router.md

# 3. Run verification
bash scripts/verify_all.sh
```

## Repository Structure

```
ai-film-studio/
├── SKILL.md                 ← entry point (agents read this first)
├── README.md                ← you are here
├── CHANGELOG.md
├── LICENSE
│
├── workflows/               ← tier 2: how to execute (12 stages / 31 workflows)
│   ├── intent-router.md     ← start here
│   ├── M0-intake.md
│   ├── M1a-creative-direction.md, M1b-concept-expansion.md, M1c-research-lab.md
│   ├── M2-narrative.md
│   ├── M3a-shot-design.md, M3b-shot-list.md
│   ├── M4a-continuity.md, M4b-character-world.md, M4c-continuity-qc.md, M4d-transitions.md
│   ├── M5a-graphics.md, M5b-text-motion.md
│   ├── M6-audio.md, M6b-sound-design.md, M6c-dialogue-lipsync.md
│   ├── M7a-prompt-architecture.md, M7b-image-prompts.md
│   ├── M8a-motion-prompts.md, M8b-motion-direction.md, M8c-animation-ready.md, M8d-motion-graphics.md
│   ├── M9a-executive-producer.md, M9b-quality-gates.md, M9c-preflight.md, M9d-localization.md
│   ├── M10a-production-architecture.md, M10b-hybrid-assembly.md, M10c-edit-color.md
│   ├── M11a-reference-analyst.md, M11b-visual-research.md
│   └── shortcuts/           ← quick paths (single-prompt, image-gen, etc.)
│
├── references/protocols/    ← orchestration & state machine
│   ├── production-state-machine.md   ← AUTHORITATIVE stage model (M0–M11)
│   ├── orchestration-runtime.md      ← executable spec for 9 routes
│   ├── agent-contract.md, decision-policy.md, output-protocol.md, interaction-flow.md
│
├── schemas/                 ← tier 3: data structures (output templates)
│   ├── production-blueprint.md
│   ├── image-prompts-package.md
│   ├── motion-prompts-package.md
│   ├── audio-package.md
│   ├── assembly-guide.md
│   └── state/               ← runtime state files
│
├── references/              ← tier 3: deep knowledge
│   ├── protocols/           ← output protocol, decision policy, etc.
│   ├── specs/               ← 10-Layer A-J, transitions, audio, models
│   └── knowledge/           ← failure modes, memory, context assembly
│
├── quality/                 ← tier 3: 8 quality gates
│   ├── quality-gates.md
│   ├── checklist.md
│   └── self-audit.md
│
├── examples/                ← 2 live end-to-end examples
├── scripts/                 ← 5 verification scripts
└── assets/                  ← static assets (placeholders)
```

## Progressive Disclosure

This skill follows the **Agent Skills Standard** with three loading tiers:

| Tier | When loaded | Size | What |
|---|---|---|---|
| **1** | Always | ≤ 5KB | `SKILL.md` + `README.md` + `CHANGELOG.md` |
| **2** | Project start | ~50KB | `workflows/` (intent-router + relevant M-stage) |
| **3** | Specialized task | ~200KB | `references/` + `schemas/` + `quality/` |

The agent reads tier 1, uses `workflows/intent-router.md` to pick a path, then loads only the relevant tier 2/3 files.

## Use Cases

| Use case | Path | Time |
|---|---|---|
| One prompt only | `workflows/shortcuts/single-prompt.md` | 2 min |
| Single image | `workflows/shortcuts/image-generation.md` | 5 min |
| Image to video | `workflows/shortcuts/image-to-video.md` | 5 min |
| Lip-sync dialogue | `workflows/shortcuts/dialogue-lipsync.md` | 5 min |
| Motion graphics | `workflows/shortcuts/motion-graphics.md` | 10 min |
| Concept only | `workflows/shortcuts/concept-only.md` | 15 min |
| Single scene (3-8 shots) | `workflows/M0` → M3 | 30 min |
| Short film / ad (30-60s) | `workflows/M0` → M11 | 90 min |

## The 5 Output Packages

Every full project produces these 5 files:

1. **`schemas/production-blueprint.md`** — Concept, story, script, characters, locations
2. **`schemas/image-prompts-package.md`** — All image prompts (10-Layer A-J)
3. **`schemas/motion-prompts-package.md`** — All video prompts (with start/end frames)
4. **`schemas/audio-package.md`** — Voice, music, SFX, foley, ambience + lip-sync plan
5. **`schemas/assembly-guide.md`** — Step-by-step assembly in Premiere/DaVinci

See `examples/energy-drink-ad.md` for a complete 30-second ad using all 5 packages.

## Quality System

8 Quality Gates enforce standards:

- **G0** — Intake clarity
- **G1** — Idea quality
- **G2** — Narrative quality
- **G3** — Continuity quality
- **G4** — **HARD GATE** — Prompt quality (10 layers A-J)
- **G5** — Transition quality
- **G6** — Text quality
- **G7** — Audio quality
- **G8** — **HARD GATE** — Master quality (all 5 files complete)

Any critical fail on G4 or G8 = **project blocked**. See `quality/quality-gates.md`.

## Models Supported

Tested with (see `references/specs/model-matrix.md` for full matrix):

- **Image:** bytedance/seedream-4, midjourney-v6, stability/sdxl, gemini-3-pro-image
- **Video:** bytedance/seedance-2.0, runwayml/gen4, kling-2.1, veo-3, sora
- **Audio:** ElevenLabs, Suno, Udio, Cartesia, Stability Audio
- **Lip-sync:** Hedra, Omniverse Audio2Face, Veo 3 (native)

## Verification

```bash
# All checks
bash scripts/verify_all.sh

# Individual
python3 scripts/verify_structure.py    # 75+ files, structure
python3 scripts/verify_functional.py    # 30/30 functional checks
python3 scripts/verify_motion.py        # 46/46 motion path checks
python3 scripts/verify_example.py       # 29/29 example validation
```

Latest run: **4/4 passed**.

## License

MIT — see [LICENSE](LICENSE).

## Contributing

Issues and PRs welcome. See `CHANGELOG.md` for the evolution of design decisions.

## Maintainer

AI Film Studio Team · github.com/zoih6
