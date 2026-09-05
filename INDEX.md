# INDEX — AI Film Studio v2.0

> **خريطة قراءة سريعة.** عند تشغيل المهارة، اقرأ هذا الملف أولًا لتحديد ما تحتاج قراءته، ثم ادخل على القسم المطلوب فقط. هذا يحمي السياق من الإغراق.

---

## 0. نقطة الدخول

| الملف | متى تقرأه |
|---|---|
| **`SKILL.md`** | مرة واحدة لفهم البنية الكاملة. لا تُقرأ في كل دورة. |
| **`INDEX.md`** (هذا الملف) | عند بداية أي مشروع لتحديد المسار. |
| **`CHANGELOG-v2.0.md`** | إذا كنت قادمًا من v1.5 لفهم الجديد. |
| **`examples/energy-drink-ad.md`** | مثال حي كامل لفهم v2.0 في مشروع واقعي. |

---

## 1. المسارات السريعة (Quick Paths)

| النية | المسار الأدنى | الوكلاء |
|---|---|---|
| **فكرة فقط** | CONCEPT | 01 → 21 → 23 |
| **«اكتب برومبت واحد»** | PROMPT_ONLY | 22 → `references/prompt-patterns.md` |
| **صورة/فريم ثابت** | IMAGE_GENERATION | 22 → 19 → 31 (G4) |
| **تحريك صورة موجودة** | IMAGE_TO_VIDEO | 22 → 25 (Frame Chain) → 19 → 31 (G4) |
| **موشن جرافيك/تايبوجرافي** | MOTION_GRAPHICS | 27 → 28 → 22 |
| **حوار/مزامنة شفاه** | DIALOGUE_LIPSYNC | 29 → 22 |
| **لقطة من مشروع قائم** | SHOT_BUILD | State → 25 → 22 → 19 → 31 |
| **مشهد متعدد اللقطات** | SCENE_BUILD | 23 → 24 → 25 → 22 |
| **فيلم/إعلان كامل** | FULL_PRODUCTION | M0–M11 (12 مرحلة) |
| **إصلاح جزء** | REPAIR | تشخيص → الوكيل المتضرر → Quality Gate |

---

## 2. الـ 12 مرحلة الكاملة (M0–M11)

| المرحلة | الوصف | الوكلاء | الجودة |
|---|---|---|---|
| **M0** | الاستقبال (Intake) | 01 | G0 |
| **M1** | البحث الإبداعي | 21 | G1 |
| **M2** | تثبيت المفهوم | 30 (Concept Deck) | G1.5 |
| **M3** | البنية السردية | 23 | G2 |
| **M4** | هندسة اللقطات | 24 | G3 (1/2) |
| **M5** | الاستمرارية | 25 | G3 (2/2) |
| **M6** | الانتقالات | 26 | G5 |
| **M6.5** | الجرافيكس والنصوص | 27 + 28 | G6 |
| **M7** | تصميم الصوت | 29 | G7 |
| **M8** | برومبتات الصور | 22 | G4 (Hard) |
| **M9** | برومبتات الفيديو | 22 | G4 (Hard) |
| **M10** | مراجعة ما قبل الإنتاج | 30 + 31 | G8 (Hard) |
| **M11** | التسليم النهائي | 30 | - |

---

## 3. الـ 31 وكيلًا

### v1.0 (v1.5) — الوكلاء الأساسيون (20)

| # | الوكيل | الملف | المسؤولية | المرحلة |
|---|---|---|---|---|
| 1 | محلل الطلبات | `01-intake.md` | تفكيك الطلب | M0 |
| 2 | المخرج الإبداعي | `02-creative-direction.md` | لوجلاين + هوية | M1 |
| 3 | مشرف الشخصيات | `03-character-world-bible.md` | ثبات الهوية | M2 |
| 4 | مساعد المخرج | `04-shot-list.md` | تقطيع اللقطات | M3 |
| 5 | مدير التصوير | `05-image-prompts.md` | برومبتات الصور | M4 |
| 6 | مشرف التحريك | `06-motion-prompts.md` | برومبتات الفيديو | M5 |
| 7 | مصمم الصوت | `07-sound-design.md` | الصوت | M6 |
| 8 | مونتير و QC | `08-edit-color-qc.md` | المونتاج | M7 |
| 9 | باحث بصري | `09-visual-research.md` | بحث مرئي | - |
| 10 | محلل المراجع | `10-reference-analyst.md` | تحليل المراجع | - |
| 11 | موشن جرافيكس | `11-motion-graphics.md` | تايبوجرافي | - |
| 12 | توسيع المفهوم | `12-concept-expansion.md` | brainstroming | M1 |
| 13 | معماري الإنتاج | `13-production-architecture.md` | بنية الإنتاج | - |
| 14 | أصول جاهزة للتحريك | `14-animation-ready-assets.md` | تحضير الصور | M5 |
| 15 | مخرج الحركة | `15-motion-direction.md` | تصميم الحركة | M5 |
| 16 | حوار و lip-sync | `16-dialogue-lipsync.md` | تزامن الحوار | M6 |
| 17 | QC الاستمرارية | `17-continuity-qc.md` | فحص الاستمرارية | - |
| 18 | مونتاج هجين | `18-hybrid-edit-assembly.md` | تجميع | M7 |
| 19 | Preflight Check | `19-preflight-check.md` | فحص ما قبل التوليد | قبل كل توليد |
| 20 | التوطين | `20-localization.md` | تكييف ثقافي | - |

### v2.0 — الوكلاء الجدد (11)

| # | الوكيل | الملف | المسؤولية | المرحلة |
|---|---|---|---|---|
| **21** | مختبر البحث الإبداعي | `21-creative-research-lab.md` | بحث + عصف ذهني + Concept Deck | M1 |
| **22** | مهندس هندسة البرومبتات | `22-prompt-architecture.md` | 10 طبقات A-J | M8, M9 |
| **23** | مهندس البنية السردية | `23-narrative-architect.md` | Story Spine + Scenes + Script | M3 |
| **24** | مهندس هندسة اللقطات | `24-shot-architect.md` | Shot Cards + Blocking + Edit Handles | M4 |
| **25** | مشرف الاستمرارية | `25-continuity-supervisor.md` | Continuity Bible + Frame Chain | M5 |
| **26** | مهندس الانتقالات | `26-transition-engineer.md` | تصميم الانتقالات (12 نوع) | M6 |
| **27** | مدير الجرافيكس | `27-graphic-typography-director.md` | AI-Native Graphic Composition | M6.5 |
| **28** | استراتيجية تحريك النصوص | `28-text-preservation-motion.md` | 5 استراتيجيات للنصوص | M6.5 |
| **29** | محرك قرار الصوت | `29-audio-decision-engine.md` | شجرة قرار الصوت | M7 |
| **30** | المنتج التنفيذي | `30-executive-producer.md` | المنسق المركزي + 5 Output Files | M10, M11 |
| **31** | مدير بوابات الجودة | `31-quality-gate-controller.md` | 8 Quality Gates (G0–G8) | مستمرة |

---

## 4. الـ 28 Reference (مرجعيات)

### v1.4–v1.5 (24 references)

```
references/agent-contract.md
references/context-assembly.md
references/copywriting-and-text-in-images.md
references/decision-policy.md
references/failure-modes.md
references/intent-router.md
references/interaction-flow.md
references/memory-context-policy.md
references/memory-lifecycle.md
references/memory-schema.md
references/model-adapters.md
references/model-matrix.md
references/output-protocol.md
references/production-state-machine.md
references/project-memory.md
references/prompt-compiler.md
references/prompt-patterns.md
references/prompt-quality-gate.md
references/scene-shot-dna.md
references/session-continuation.md
references/shot-contract.md
references/text-execution-matrix.md
references/version-lineage.md
```

### v2.0 — المرجعيات الجديدة (4)

```
references/prompt-architecture-spec.md    # 10 طبقات A-J
references/continuity-bible-schema.md     # مخطط Bible الكامل
references/transition-types.md            # 12 نوع انتقال
references/audio-decision-tree.md         # شجرة قرار الصوت
```

---

## 5. الـ 11 Template (قوالب)

### v1.5 (5)

```
templates/concept-deck.md
templates/delivery-package.md
templates/production-brief.md
templates/project-memory.md
templates/reference-library.md
templates/style-dna-sheet.md
```

### v2.0 — الحزم الخمس (5)

```
templates/01-production-blueprint.md     # النظرة الشاملة
templates/02-image-prompts-package.md    # برومبتات الصور
templates/03-motion-prompts-package.md   # برومبتات الفيديو
templates/04-audio-package.md            # الحزمة الصوتية
templates/05-assembly-guide.md           # دليل التجميع
```

---

## 6. ملفات State (12 ملف)

### v1.5 (5)

```
state/project-memory.md
state/asset-registry.md
state/decision-log.md
state/risk-register.md
state/reference-library.md
```

### v2.0 (7 جديد)

```
state/continuity-bible.md       # قاموس الهوية البصرية
state/frame-chain.md            # Start/End Frame Registry
state/quality-gates-log.md      # G0–G8 log
state/approval-log.md           # من v1.0
state/continuity-ledger.md      # من v1.0
state/generation-log.md         # من v1.0
state/production-brief.md       # من v1.0
state/session-checkpoint.md     # من v1.0
```

---

## 7. الـ 8 Quality Gates (G0–G8)

| Gate | الاسم | بعد المرحلة | المسؤولية | النوع |
|---|---|---|---|---|
| **G0** | وضوح الاستقبال | M0 | 30-EP | Soft |
| **G1** | جودة الفكرة | M1 | 21-CRL | Soft |
| **G2** | جودة السرد | M3 | 23-NA | Soft |
| **G3** | جودة الاستمرارية | M5 | 25-CS | Soft |
| **G4** | جودة البرومبتات | M8, M9 | 22-PA + 31-QG | **HARD** |
| **G5** | جودة الانتقالات | M6 | 26-TE | Soft |
| **G6** | جودة النصوص | M6.5 | 27-GTD + 28-TPM | Soft (critical on G6.4) |
| **G7** | جودة الصوت | M7 | 29-ADE | Soft |
| **G8** | الجودة الشاملة | M10 | 30-EP + 31-QG | **HARD** |

التوثيق الكامل في `agents/31-quality-gate-controller.md`.

---

## 8. Prompt Architecture — 10 طبقات A-J

| الطبقة | الاسم | الغرض |
|---|---|---|
| **A** | Intent | لماذا هذا المشهد؟ |
| **B** | Subject | من/ما الموضوع؟ |
| **C** | Environment | أين ومتى؟ |
| **D** | Composition | كيف يُبنى الكادر؟ |
| **E** | Camera | بمَ نرى؟ |
| **F** | Lighting | كيف يُضاء؟ |
| **G** | Motion | ما الذي يتحرك؟ (video) |
| **H** | Cinematic Continuity | كيف يرتبط بما قبله/بعده؟ |
| **I** | Style & Visual DNA | ما اللغة البصرية؟ |
| **J** | Constraints | ما الذي يجب الحفاظ عليه؟ |

التوثيق الكامل في `references/prompt-architecture-spec.md`.

---

## 9. الـ 5 Output Files (مخرجات v2.0)

| # | الملف | يحوي | يُنتَج من |
|---|---|---|---|
| **01** | `01-production-blueprint.md` | النظرة الشاملة | 30-EP بعد M0–M9 |
| **02** | `02-image-prompts-package.md` | كل prompt صورة | 22-PA + 30-EP |
| **03** | `03-motion-prompts-package.md` | كل prompt فيديو | 22-PA + 30-EP |
| **04** | `04-audio-package.md` | كل الطبقات الصوتية | 29-ADE + 30-EP |
| **05** | `05-assembly-guide.md` | دليل التجميع خطوة بخطوة | 30-EP |

---

## 10. الأمثلة (Examples)

| المثال | النوع | المدة | يُظهر |
|---|---|---|---|
| `examples/coffee-short.md` | قصة قصيرة | 60s | v1.5 نمط |
| `examples/energy-drink-ad.md` | إعلان منتج | 30s | **v2.0 كامل** (كل المنظومة) |

---

## 11. أدوات الفحص (Verification)

```
_verify_structure.py    # يفحص بنية الملفات
_verify_all.sh          # يفحص كل شيء (هيكل + وظيفي + أمثلة)
```

---

## 12. كيف تقرأ v2.0 (للمستخدمين الجدد)

### قراءة سريعة (5 دقائق)

1. `SKILL.md` (الـ overview)
2. `INDEX.md` (هذا الملف)
3. `CHANGELOG-v2.0.md` (ما الجديد)

### قراءة متوسطة (30 دقيقة)

+ `examples/energy-drink-ad.md` (مثال حي)
+ `agents/30-executive-producer.md` (المنسق)

### قراءة كاملة (3 ساعات)

+ كل الـ 31 وكيل
+ كل الـ 5 templates
+ الـ 4 references الجديدة

### بدء مشروع

1. افتح `SKILL.md` → اتبع المراحل M0–M11
2. في كل مرحلة، شغّل الوكيل المناسب
3. في النهاية، استلم الـ 5 Output Files

---

## 13. التوثيق الإضافي

| الملف | الوصف |
|---|---|
| `SKILL.md` | الـ overview الرئيسي |
| `CHANGELOG-v1.5.md` | تغييرات v1.5 |
| `CHANGELOG-v2.0.md` | تغييرات v2.0 (هذا الإصدار) |
| `INDEX.md` | هذا الملف |
| `README.md` | مقدمة عامة (إن وُجد) |

---

**AI Film Studio v2.0 — من Prompt Writer إلى AI Film Production System.**

**31 وكيلًا • 10 طبقات • 12 مرحلة • 8 Quality Gates • 5 Output Files**
