# AI Film Studio v1.1.0

## الهدف
تحويل AI Film Studio من منهج إنتاج متعدد الوكلاء إلى إطار تشغيل قابل للتتبع، مع الحفاظ على الوكلاء الحالية.

## التغييرات
- إصلاح بوابة الاعتماد: بعد M5 وقبل M6، بدل التعارض السابق بين M3/M4.
- إضافة Production State Machine.
- إضافة Agent Contract موحد.
- إضافة Shot Contract.
- إضافة Asset Registry.
- إضافة Continuity Ledger.
- إضافة Approval Log.
- إضافة Generation Log.
- إضافة Version Lineage.
- إضافة Text Execution Matrix.
- إضافة Repair/Revalidation Loop.
- ربط جميع الوكلاء بعقد تشغيل v1.1.
- تحويل `state/` من مفهوم ضمني إلى بنية فعلية.

## مبدأ التوافق
لا تزال ملفات الوكلاء الأصلية هي مصدر الاختصاص. طبقة v1.1 تضيف التحكم والتتبع ولا تستبدل الخبرة المتخصصة لكل وكيل.


## v1.1.1 — Output & Interaction Layer

- Added `references/output-protocol.md` for clean, progressive, copy-ready user-facing output.
- Added `references/interaction-flow.md` for a single-voice studio interaction model.
- First clarification round is now exactly 3 high-impact questions; second round is up to 3 only when required.
- Internal agent/state/validation details are hidden from normal user output.
- Added standardized response modes: DISCOVER, BUILD, DELIVER, REPAIR.
- Added `APPROVE / EDIT` single production approval interaction after M5.
- Updated Intake Agent to follow the new interaction protocol.
- Version bumped to 1.1.1.


## v1.2.0 — Adaptive Intelligence Layer

- Added `references/intent-router.md` for minimum-sufficient routing.
- Added `references/decision-policy.md` for user-vs-studio decision ownership.
- Added `references/scene-shot-dna.md` for Scene DNA / Shot DNA inheritance.
- Added `references/context-assembly.md` for tiered context loading and stale-context protection.
- Changed M0–M13 from mandatory universal flow to an adaptive full-production path selected by intent.
- Added a no-ask threshold so professional reversible decisions are made internally.
- Preserved v1.1.1 Output & Interaction Layer and single-voice user experience.
- Version bumped to 1.2.0.


## v1.3.0 — Prompt Runtime
- Added `references/prompt-compiler.md`
- Added `references/model-adapters.md`
- Added `references/prompt-quality-gate.md`
- Added canonical prompt schema and compilation rules.
- Added capability-aware model adaptation.
- Added hard prompt quality gates and targeted repair loop.
- Established single-source Prompt Spec to prevent inconsistent prompt writing across agents.


## v1.4.0 — Project Memory System
- Added persistent project memory architecture.
- Added canonical memory schema, lifecycle, context policy, and session continuation protocol.
- Added `state/project-memory.md`, `state/decision-log.md`, and `state/session-checkpoint.md`.
- Added memory hierarchy, conflict resolution, versioning, compaction, and durable-fact rules.
- Added automatic continuation behavior for short follow-up commands without restarting Intake.
- Preserved v1.3 Prompt Compiler / Model Adapter / Quality Gate architecture.

## v1.4.1 — Arabic Typography + Validation Integration

- Preserved the Arabic copywriting and exact-text rendering rules from the prior production branch.
- Preserved the boundary between static Arabic text rendered in image models and time-based text rendered as editable motion/compositing layers.
- Adapted the structural and functional verification suite to the M0–M13 state-machine architecture.
- Added validation for agent contracts, prompt compiler, model adapters, memory state, continuity ledger, approval protocol, and text execution matrix.
- Corrected the package version metadata to `1.4.0` and expanded the skill description to include project memory and session continuation.
