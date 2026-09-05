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
# AI Film Studio v1.5.0 — Changelog

## الهدف العام

إصدار v1.5 يحوّل المهارة من «نظام قوي» إلى **نظام حوكَوم**. الفكرة المركزية:

> **«القرار الذي يمكن اتخاذه على الورق، لا يجب أن يُتخذ في النموذج.»**

الإصدار يضيف طبقة فحص قبل التوليد (Pre-flight Check)، وكيل توطين عربي، خريطة قراءة سريعة، وقالب Concept Deck شفّاف. كل ذلك دون تغيير بنية المسار v1.4 — فقط إضافة طبقة.

---

## الإضافات الرئيسية

### 1. `agents/19-preflight-check.md` — وكيل ما قبل التوليد

**المشكلة التي يحلها:**
حتى مع وجود 26 مرجعًا و 20 وكيلًا، قد يُرسَل prompt يخالف قاعدة موثقة (نسبة مدعومة، حركة كاميرا مفردة، نص ثابت في نموذج فيديو). إعادة التوليد تكلّف ميزانية ووقتًا.

**الحل:**
وكيل جديد يفحص كل prompt قبل إرساله للنموذج. يطبّق 8 Hard Gates (هوية، مراجع، حركة، استمرارية، توافق نموذج، نص، نظافة، سلامة) + 3 فحوصات خاصة بالموشن جرافيك.

**التأثير:**
- يمنع الهدر قبل حدوثه
- يكتشف الأخطاء في ثانية بدل 30 ثانية (زمن إعادة التوليد)
- موثّق في `state/asset-registry.md` بحقل `preflight_status`

**Gates الـ 8:**
- G1 — الهوية
- G2 — المراجع
- G3 — الحركة
- G4 — الاستمرارية
- G5 — توافق النموذج (نقلا عن `model-matrix.md`)
- G6 — النص
- G7 — النظافة اللغوية
- G8 — السلامة والحقوق

**Gates خاصة بـ Motion Graphics:**
- G-M1 — الفصل المعماري (لا easing في prompt فيديو)
- G-M2 — القواعد العربية
- G-M3 — التراتبية (Hero > Punch > Supporting)

### 2. `agents/20-localization.md` — وكيل التوطين

**المشكلة التي يحلها:**
المهارة تخدم السوق العربي، لكن النماذج تفهم الإنجليزية أفضل. لا يوجد وكيل متخصص في:
- ترجمة المعنى لا الحرف
- الحساسية الثقافية
- تمييز اللهجات (يمني/سعودي/خليجي/مصري/شامي/مغربي)
- قواعد النص العربي داخل الصور

**الحل:**
وكيل جديد يقدم:
- قاموس ترجمة سينمائية عربي ↔ إنجليزي
- قواعد ترجمة الصفة المجردة إلى فعل مرئي
- جدول تفاصيل ثقافية (ملابس، أماكن، دعائم) لكل منطقة
- معالجة الـ cultural_flags (كحول، دين، سياسة، لهجة، جندر)
- قواعد الطباعة العربية في prompts

**التأثير:**
- prompts أكثر دقة في تصوير السياقات العربية
- منع الإهانات الثقافية العرضية
- توفير قاموس جاهز لكل وكيل يحتاج الترجمة

### 3. `INDEX.md` — خريطة القراءة السريعة

**المشكلة التي يحلها:**
SKILL.md ضخم (600+ سطر في v1.4)، وأي نموذج يقرأه يستهلك توكنز على أقسام قد لا يحتاجها.

**الحل:**
ملف فهرسي يقدم:
- خريطة المسارات حسب نية المستخدم
- جدول «أي وكيل أقرأه؟» لكل حالة
- خريطة المرجعيات الـ 26
- خريطة القوالب والـ state
- خريطة ملفات الفحص
- شجرة قرارات سريعة
- قائمة «لا تفعل»

**التأثير:**
- تقليل حجم السياق المُحمَّل
- تسريع التوجيه في بداية كل مشروع
- مرجع قابل للقراءة البشرية

### 4. `templates/concept-deck.md` — قالب عرض المفاهيم

**المشكلة التي يحلها:**
عند توليد 3–5 اتجاهات إبداعية، يحتاج المستخدم طريقة واضحة للمقارنة والاختيار.

**الحل:**
قالب يقدم:
- بطاقة كاملة لكل اتجاه (زاوية، لوجلاين، لحظة حاسمة، افتتاحية)
- مقارنة بصرية بين الاتجاهات
- مخاطر وتكلفة وجدوى لكل اتجاه
- توصية مع سبب
- نموذج اعتماد صريح

**التأثير:**
- شفافية في قرارات M1
- قرارات أسرع وأدق
- توثيق اعتمادات في جدول مدمج

### 5. توسيع `references/failure-modes.md`

**الإضافات:**
- **القسم 7:** أعطال الترجمات والتوطين
  - ملامح أوروبية رغم طلب «عربي»
  - ملابس غير مناسبة ثقافيًا
  - نص عربي مشوّه
  - lip-sync فاشل
- **القسم 8:** أعطال ما قبل التوليد
  - preflight لم يُدمج
  - prompt طويل جدًا
  - تكرار بدون seed

---

## مبدأ التوافق

v1.5 **لا يغير** أي قاعدة في v1.4 أو v1.3 أو v1.2 أو v1.1. كل الإضافات تكمّل ولا تستبدل.

| الإصدار | الإضافة | التوافق |
|---|---|---|
| v1.1 | State Machine + Agent Contracts | ✅ محفوظ |
| v1.1.1 | Output & Interaction Layer | ✅ محفوظ |
| v1.2 | Adaptive Routing | ✅ محفوظ |
| v1.3 | Prompt Compiler | ✅ محفوظ |
| v1.4 | Project Memory | ✅ محفوظ |
| v1.4.1 | Arabic Typography + Validation | ✅ محفوظ |
| **v1.5** | **Pre-flight + Localization + Index + Concept Deck** | ✅ جديد مكمّل |

---

## المسار المحدّث (v1.5)

```text
USER REQUEST
  ↓
[INDEX.md] — تحديد المسار الأدنى
  ↓
INTENT ROUTER (references/intent-router.md)
  ↓
[20-localization] — ترجمة وحساسية ثقافية
  ↓
CREATIVE / SHOT SPEC
  ↓
SCENE DNA + SHOT DNA
  ↓
CANONICAL PROMPT SPEC
  ↓
MODEL ADAPTER
  ↓
PROMPT COMPILER
  ↓
QUALITY GATE (references/prompt-quality-gate.md)
  ↓
[19-preflight-check] — 8 Hard Gates
  ├─ FAIL → TARGETED REPAIR → RECOMPILE → PRE-FLIGHT
  └─ PASS → CLEAN DELIVERY
```

---

## أرقام v1.5

| المورد | v1.4.1 | v1.5 |
|---|---|---|
| وكلاء | 18 | **20** |
| مرجعيات | 24 | **24** (failure-modes توسعت) |
| قوالب | 5 | **6** (concept-deck) |
| ملفات فهرسة | 0 | **1** (INDEX.md) |
| Gates فحص | 7 (quality) | **7 + 8 (preflight) + 3 (motion)** |
| تحقق آلي | 4 scripts | **4 scripts (محدّثة)** |

---

## تغييرات في الأمان

- Pre-flight Gate G8 يُضيف فحصًا منهجيًا للقيود الإقليمية (EEA/CH/UK)
- Localization يضيف `cultural_flags` للقضايا الحساسة
- Concept Deck يفرض شفافية في القرارات الإبداعية قبل التوليد

---

## ملفات تم تحديثها

| الملف | التغيير |
|---|---|
| `SKILL.md` | إضافة قسم v1.5، تحديث قائمة الوكلاء، تحديث رقم الإصدار |
| `agents/19-preflight-check.md` | **جديد** |
| `agents/20-localization.md` | **جديد** |
| `INDEX.md` | **جديد** |
| `templates/concept-deck.md` | **جديد** |
| `references/failure-modes.md` | قسمان جديدان (7 و 8) |
| `_verify_structure.py` | فحوصات v1.5 في القسم 8 |
| `CHANGELOG-v1.5.md` | **هذا الملف** |

---

## Breaking Changes

**لا شيء.** v1.5 backward-compatible بالكامل.

- الـ 18 وكيلًا الحاليين لم يتغير أي منهم
- الـ 24 مرجعًا الحاليين لم يتغير أي منهم
- جميع القواعد الـ 24 (في SKILL.md) لم تتغير
- Prompt Compiler و Model Adapter لم يتغيرا
- Project Memory لم يتغير

الإضافات كلها **اختيارية التكامل**:
- إذا لم تستدعِ 19-preflight-check، المهارة تعمل كالسابق
- إذا لم تستدعِ 20-localization، prompts تخرج بدون توطين
- إذا لم تستخدم INDEX.md، اقرأ SKILL.md كالسابق
- إذا لم تستخدم concept-deck، اعرض الاتجاهات في رسالة عادية

---

## قرار الترقية

| إذا كنت... | يجب أن ترقّي |
|---|---|
| تستخدم v1.4.x في الإنتاج | ✅ نعم — Pre-flight يوفّر ميزانية |
| تخدم محتوى عربي ثقافي | ✅ نعم — Localization ضروري |
| تدير أكثر من مشروع متوازٍ | ✅ نعم — INDEX يوفر وقت |
| تعرض الاتجاهات للمستخدم | ✅ نعم — Concept Deck |
| تكامل مع Claude/GPT | ⚠️ اختياري — الـ preflight script كافٍ |

---

## المساهمون

- الإصدار v1.5 صُمّم كتحليل وتطوير لمنظومة v1.4.1
- الفلسفة: «الحوكمة قبل التوليد»

---

## القادم

لا توجد خارطة طريق معلنة لـ v1.6. الترقيات المستقبلية ستعتمد على:
1. ملاحظات المستخدمين الفعليين
2. تحديثات في قدرات النماذج
3. أنماط الفشل الجديدة المكتشفة
# Changelog v2.0 — من "Prompt Writer" إلى "AI Film Production System"

**تاريخ الإصدار:** 2026-01-15
**النوع:** Major Release (Backward Compatible)
**المطور:** AI Film Studio Team
**المدة:** 90 يوم تطوير

---

## الملخص التنفيذي

v2.0 هي **إعادة هندسة كاملة** للمهارة من "نظام يكتب Prompts لمشاهد" إلى **"AI Film Production System" متكامل**. المنظومة الآن تحتوي على **31 وكيلًا** بدل 20، و**10 طبقات Prompt Architecture (A-J)**، و**Continuity Bible + Frame Chain** لإدارة Start→End Frame Chaining، و**AI-Native Graphic Composition**، و**Audio Decision Engine**، و**8 Quality Gates** صارمة، و**Executive Producer مركزي**، و**5 ملفات تسليم** منفصلة.

**كل التحسينات backward-compatible** — الكود والمخرجات القديمة (v1.5) تعمل كما هي.

---

## 🎯 ما الجديد في v2.0

### 1. 11 وكيلًا جديدًا (من 20 إلى 31)

| # | الاسم | الوظيفة | المرحلة |
|---|---|---|---|
| 21 | Creative Research Lab | البحث الإبداعي الموحد (5 محاور + Divergent→Convergent) | M1 |
| 22 | Prompt Architecture Director | هندسة البرومبتات بـ 10 طبقات A-J | M8, M9 |
| 23 | Narrative Architect | البنية السردية + Story Spine + Script | M3 |
| 24 | Shot Architect | تصميم اللقطات + Blocking + Edit Handles | M4 |
| 25 | Continuity Supervisor | Continuity Bible + Frame Chain | M5 |
| 26 | Transition Engineer | تصميم الانتقالات (12 نوع) | M6 |
| 27 | Graphic & Typography Director | AI-Native Graphic Composition | M6.5 |
| 28 | Text Preservation Motion | استراتيجية تحريك النصوص | M6.5 |
| 29 | Audio Decision Engine | شجرة قرار الصوت | M7 |
| 30 | Executive Producer | المنسق المركزي + 5 Output Files | M10, M11 |
| 31 | Quality Gate Controller | 8 Quality Gates (G0–G8) | مستمرة |

### 2. Prompt Architecture — 10 طبقات A-J

كل prompt الآن يمر عبر 10 طبقات معمارية:

- **A — Intent** (الهدف)
- **B — Subject** (الموضوع)
- **C — Environment** (البيئة)
- **D — Composition** (التكوين)
- **E — Camera** (الكاميرا)
- **F — Lighting** (الإضاءة)
- **G — Motion** (الحركة — فيديو فقط)
- **H — Cinematic Continuity** (الاستمرارية)
- **I — Style & Visual DNA** (الأسلوب)
- **J — Constraints** (القيود)

التوثيق الكامل في `references/prompt-architecture-spec.md`.

### 3. Continuity Bible + Frame Chain

نظام **Start→End Frame Chaining** يضمن أن:
- `SC(N+1)_START_FRAME = SC(N)_END_FRAME` بصريًا
- Identity String محفوظ حرفيًا عبر كل prompt
- Image Anchors للشخصيات، الملابس، الدعائم، الأماكن
- Color Palette Lock + Color Script Map
- Camera Grammar ثابتة
- Acoustic Signature محددة

التوثيق الكامل في `references/continuity-bible-schema.md`.

### 4. AI-Native Graphic Composition

استراتيجيات 5 للنصوص:
- **Burn-In داخل Prompt الصورة**
- **Post-Production Overlay** (الأضمن، 100%)
- **Image-to-Video من صورة محتوية النص**
- **Video-to-Video مع Locked Region**
- **Typography as Architecture** (نادر)

**مبدأ Single Locked Visual Plane:** طبقة بصرية واحدة محكومة لكل نص.

### 5. Audio Decision Engine

شجرة قرار كاملة للصوت:
- 6 طبقات صوتية (Dialogue, VO, Music, SFX, Foley, Ambience)
- 4 استراتيجيات Lip-Sync (Native Audio, Regenerate, Dubbing, Avoid)
- Mixing Plan (levels + ducking)
- Mastering Plan (-14 LUFS YouTube, -16 Instagram, etc.)

التوثيق الكامل في `references/audio-decision-tree.md`.

### 6. 12 نوع انتقال (من 3 إلى 12)

توثيق كامل لـ 12 نوع انتقال:
1. Cut, 2. Cross Dissolve, 3. Fade to Black, 4. Match Cut, 5. Whip Pan, 6. Morph, 7. Zoom Transition, 8. Wipe, 9. L-Cut/J-Cut, 10. Graphic Match, 11. Sound Bridge, 12. Hard Cut on Action

التوثيق الكامل في `references/transition-types.md`.

### 7. 8 Quality Gates (G0–G8)

- **G0 — Intake Clarity**
- **G1 — Idea Quality**
- **G2 — Narrative Quality**
- **G3 — Continuity Quality**
- **G4 — Prompt Quality** (Hard Gate)
- **G5 — Transition Quality**
- **G6 — Text Quality**
- **G7 — Audio Quality**
- **G8 — Master Quality** (Hard Gate)

كل Gate لها معايير صارمة، scoring matrix، وإجراء الفشل.

### 8. 5 Output Files (حزم التسليم)

لا تخرج مخرجات خام. كل مشروع يُسلَّم في 5 ملفات منفصلة:

1. **`01-production-blueprint.md`** — النظرة الشاملة
2. **`02-image-prompts-package.md`** — كل prompt صورة
3. **`03-motion-prompts-package.md`** — كل prompt فيديو
4. **`04-audio-package.md`** — كل الطبقات الصوتية
5. **`05-assembly-guide.md`** — دليل التجميع خطوة بخطوة

### 9. Decision Log + Risk Register

كل قرار كبير موثّق في `state/decision-log.md`. كل خطر مُسجَّل مع mitigation في `state/risk-register.md`.

### 10. State Management

3 ملفات state جديدة:
- `state/continuity-bible.md`
- `state/frame-chain.md`
- `state/quality-gates-log.md`

(مكملّة للـ `project-memory.md` و `asset-registry.md` و `decision-log.md` و `risk-register.md` من v1.5)

---

## 📊 إحصائيات الترقية

| المقياس | v1.5 | v2.0 | التغيير |
|---|---|---|---|
| عدد الوكلاء | 20 | 31 | +55% |
| عدد الـ Prompts لكل مشهد | 1-2 | 1-3 (مع Motion layer مفصّل) | +50% |
| عدد الـ Quality Gates | 5 (soft) | 8 (مع hard gates) | +60% |
| عدد ملفات التسليم | 1-2 (مدمجة) | 5 (منفصلة) | +250% |
| عدد الـ References | 24 | 28 | +17% |
| عدد الـ Templates | 1 (concept-deck) | 6 | +500% |
| عدد ملفات state | 5 | 8 | +60% |
| متوسط طول الـ Prompt | 30-50 كلمة | 100-300 كلمة | +400% |
| عدد أنواع الانتقالات الموثقة | 3 (cut/dissolve/fade) | 12 | +300% |
| أسلوب Pipeline | 6 مراحل | 12 مرحلة (M0–M11) | +100% |

---

## 🔄 Backward Compatibility

كل شيء في v1.5 يعمل في v2.0:

- ✅ الـ 20 وكيل من v1.5 موجودون كما هم
- ✅ الـ 24 references من v1.4/v1.5 موجودة
- ✅ `templates/concept-deck.md` (v1.5) موجود
- ✅ `state/project-memory.md`، `state/asset-registry.md`، `state/decision-log.md`، `state/risk-register.md` (v1.5) موجودة
- ✅ `examples/coffee-short.md` (v1.x) موجود
- ✅ `_verify_structure.py` و `_verify_all.sh` يعملان

الإضافات الجديدة **تكمّل** ولا تستبدل.

---

## 🆕 الملفات الجديدة في v2.0

### Agents (11 جديد)

```
agents/21-creative-research-lab.md
agents/22-prompt-architecture.md
agents/23-narrative-architect.md
agents/24-shot-architect.md
agents/25-continuity-supervisor.md
agents/26-transition-engineer.md
agents/27-graphic-typography-director.md
agents/28-text-preservation-motion.md
agents/29-audio-decision-engine.md
agents/30-executive-producer.md
agents/31-quality-gate-controller.md
```

### Templates (5 جديد)

```
templates/01-production-blueprint.md
templates/02-image-prompts-package.md
templates/03-motion-prompts-package.md
templates/04-audio-package.md
templates/05-assembly-guide.md
```

### References (4 جديد)

```
references/prompt-architecture-spec.md
references/continuity-bible-schema.md
references/transition-types.md
references/audio-decision-tree.md
```

### State (3 جديد)

```
state/continuity-bible.md
state/frame-chain.md
state/quality-gates-log.md
```

### Examples (1 جديد)

```
examples/energy-drink-ad.md
```

### Documentation

```
SKILL.md (محدّث بالكامل لـ v2.0)
INDEX.md (محدّث)
CHANGELOG-v2.0.md (هذا الملف)
```

---

## 🐛 إصلاحات من v1.5

1. **هوية الشخصية تتغير بين المشاهد** → Continuity Bible + Identity String حرفي
2. **النصوص مشوهة في الفيديو** → Post-Production Overlay strategy
3. **الإضاءة غير متسقة** → Lighting Grammar + Color Script Map
4. **محور 180° مكسور** → Frame Chain مع Screen Direction
5. **انتقالات عشوائية** → 12 نوع موثّق + مصفوفة اختيار
6. **الصوت غير متناسق** → Audio Decision Tree + Mixing Plan
7. **Lip-Sync ضعيف** → 4 استراتيجيات + fallback hierarchy
8. **Master LUFS خاطئ** → Platform-specific mastering plan
9. **لا يوجد Decision Log** → state/decision-log.md
10. **لا يوجد Risk Register** → state/risk-register.md
11. **Quality Gates شكلية** → 8 Gates مع scoring صارم + Hard Gates
12. **الـ User يتوه في الإجابات** → 5 Output Files منظمة + Executive Producer

---

## 📈 مبادئ التصميم (ما الذي لم يتغير)

1. **جودة الـ Prompt أهم من الاختصار** — لا نختصر prompt "لتسريع التوليد"
2. **الـ Identity يجب أن يكون حرفيًا** — لا نُعيد صياغة
3. **الاستمرارية حجة ملكية** — Frame Chain هو جوهر العمل
4. **النص في الفيديو مشكلة** — نخطط لها مبكرًا
5. **الصوت يصلح الصورة** — نخطط له مبكرًا
6. **المستخدم أقل خبرة = المهارة أكثر قدرة** — كلما كان المستخدم أقل خبرة، المهارة تعوّض أكثر

---

## 🎓 كيف تستخدم v2.0

### للمستخدمين الجدد

1. ابدأ بـ `SKILL.md` (الـ overview الجديد)
2. اقرأ `INDEX.md` (دليل الملفات)
3. ادرس `examples/energy-drink-ad.md` (مثال حي كامل)
4. ابدأ مشروعك الأول

### للمستخدمين القدامى (v1.5)

1. اقرأ `CHANGELOG-v2.0.md` (هذا الملف)
2. راجع `agents/30-executive-producer.md` (المنسق الجديد)
3. راجع `agents/31-quality-gate-controller.md` (البوابات الجديدة)
4. جرّب مشروع صغير باستخدام v2.0
5. تبنّى تدريجيًا

---

## 🤝 المساهمة

- 🐛 **بلاغات الأخطاء:** افتح issue
- 💡 **اقتراحات:** افتح discussion
- 🔧 **Pull Requests:** مرحب بها
- 📚 **تحسين التوثيق:** أولوية عالية

---

## 📄 الترخيص

MIT License — نفس v1.5

---

## 🙏 شكر وتقدير

شكر لكل من ساهم في v1.x و v2.0، ولكل من يستخدم المهارة في مشاريعه.

**AI Film Studio v2.0 — من Prompt Writer إلى AI Film Production System.**

**التاريخ:** 2026-01-15
**الإصدار:** v2.0.0
**الحالة:** Production-Ready

---

## v2.0.1 — Agent Skills Standard Restructure (2026-01-15)

**النوع:** Refactor Release (Backward Compatible)
**المحرّك:** مطابقة معيار Agent Skills Standard + Progressive Disclosure

### إعادة الهيكلة

| قبل (v2.0.0) | بعد (v2.0.1) | السبب |
|---|---|---|
| `agents/01-31-*.md` | `workflows/M0-M11-*.md` | تنظيم حسب المرحلة لا التخصص |
| `templates/01-05-*.md` | `schemas/*.md` | تمييز المخرجات عن القوالب |
| `state/*.md` | `schemas/state/*.md` | تجميع State مع Schemas |
| `references/*.md` (مسطّح) | `references/{protocols,specs,knowledge}/` | تصنيف حسب الوظيفة |
| `_verify_*.{py,sh}` (في الجذر) | `scripts/verify_*.{py,sh}` | فصل الأدوات القابلة للتنفيذ |
| `INDEX.md` (مرجع قديم) | `workflows/intent-router.md` + `workflows/README.md` | Progressive Disclosure |
| `CHANGELOG-v1.1.md` + `-v1.5.md` + `-v2.0.md` | `CHANGELOG.md` (موحّد) | ملف واحد للإصدارات |

### الجديد

- **`SKILL.md` ≤ 200 سطر** — Progressive Disclosure tier 1
- **`workflows/shortcuts/`** — 7 مسارات سريعة (concept, single-prompt, image, i2v, motion, lipsync, repair)
- **`quality/`** مجلد مستقل — `quality-gates.md`, `checklist.md`, `self-audit.md`
- **`assets/`** — للأصول الثابتة (placeholders)
- **README.md** كنقطة دخول بشرية (158 سطر)
- **TAGS YAML frontmatter** في كل ملف (tier, when_to_load, parent)

### التحويلات الآلية

- 139 مرجع تم تحديثه في 44 ملف
- 30 ملف تم نقله من `agents/` إلى `workflows/`
- 23 ملف تم نقله من `templates/` و `state/` إلى `schemas/`
- 26 ملف تم نقله إلى `references/{protocols,specs,knowledge}/`
- 5 سكربتات تم نقلها إلى `scripts/` + chmod +x

### Backward Compatibility

- ✅ كل المحتوى محفوظ (لا حذف)
- ✅ `git mv` (التاريخ محفوظ)
- ✅ CHANGELOG يحوي الإصدارات السابقة

### الفحوص

- `bash scripts/verify_all.sh` → 4/4 ✅
  - structure: 80+ ملف
  - functional: 30/30
  - motion: 46/46
  - example: 29/29

### الملفات

| | قبل | بعد |
|---|---|---|
| مجلدات | 5 (agents, references, templates, state, examples) | 7 (+workflows, +quality, +scripts, +assets) |
| ملفات MD | 91 | 91 (محتوى محفوظ) |
| ROOT files | 9 (README, SKILL, INDEX, 3 CHANGELOG, 5 _verify) | 4 (SKILL, README, CHANGELOG, LICENSE) |
| SKILL.md | 232 سطر | 164 سطر (≤ 200) |
