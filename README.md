<div align="center">

# 🎬 AI Film Studio

**استوديو إنتاج مرئي متكامل بالذكاء الاصطناعي — يعمل داخل أي وكيل ذكي**

*فيلم · إعلان · وثائقي · موشن جرافيك · سلسلة*

<p>
<img alt="Version" src="https://img.shields.io/badge/version-3.0.0-111827">
<img alt="Skill" src="https://img.shields.io/badge/agent-skill-7c3aed">
<img alt="Stages" src="https://img.shields.io/badge/stages-12%20%2B%205%20engines-059669">
<img alt="Workflows" src="https://img.shields.io/badge/workflows-31-2563eb">
<img alt="Style Locks" src="https://img.shields.io/badge/style%20locks-10-d97706">
<img alt="Quality Gates" src="https://img.shields.io/badge/quality%20gates-12-db2777">
<img alt="Verify" src="https://img.shields.io/badge/verify-9%2F9%20passing-16a34a">
<img alt="License" src="https://img.shields.io/badge/license-MIT-059669">
</p>

**صُمّم وبُني بواسطة [Waseem Alzobiri](https://github.com/zoih6)**

</div>

---

## ✨ ما هذه المهارة؟

**AI Film Studio** مهارة وكيل (Agent Skill) تحوّل فكرة بسيطة إلى **حزمة إنتاج كاملة**:
مفهوم، سرد، جدول Beats، بطاقات لقطات، برومبتات صور وفيديو، صوت، وورقة مونتاج —
جاهزة للتنفيذ على نماذج التوليد دون أن يسأل المنفّذ سؤالًا واحدًا.

**ليست مولّد برومبتات.** هي **استوديو كامل**: 31 تخصصًا عبر 12 مرحلة، **5 محركات**،
**10 عوالم بصرية بأقفال نصية حرفية**، و **12 بوابة جودة**.

> **"البرومبت هو الخطوة رقم 10، وليس رقم 1."**

---

## 🆕 ما الجديد في v3.0.0؟

دمج كامل لأربعة مستودعات سابقة في نظام واحد، مع **17 إضافة جديدة كليًا**.

| الإضافة | الوصف |
|---|---|
| 🎨 **10 عوالم بصرية مقفولة** | `LOCK A–J` بأقفال نصية حرفية — تُنص ولا تُعاد صياغتها |
| 🎬 **5 محركات متخصصة** | وثائقي · إعلان · هجين · سلسلة · تنفيذ بالجملة |
| 🔍 **حزمة أدوات بحث** | بحث، تعدين مراجع، تحقق حقائق، ترند، مكتبة استعلامات |
| 🛡️ **مرجع الدقة والأمان** | تدريج الثقة، ضبط المآسي، الحساسية الثقافية، الحقوق |
| 📐 **10 مخططات إخراج جديدة** | Brief · Beat Table · Shot Card · Product Sheet · Edit Sheet · End Card · Thumbnail Pack · Delivery Pack · Series Bible · Prompts TXT |
| ✅ **بوابات G9–G13** | سلامة السكربت · الـ Beats · أمانة المنتج · المنصة · السلسلة |
| 🧪 **4 سكربتات فحص جديدة** | الأقفال · المحركات · الروابط · فاحص البرومبتات |
| 📚 **مثالان حيان كاملان** | حلقة وثائقية + إعلان 15 ثانية |

→ التفاصيل: [`docs/gap-analysis-v3.md`](docs/gap-analysis-v3.md) · [`docs/migration-v2-to-v3.md`](docs/migration-v2-to-v3.md)

---

## 🏗️ المعمارية

```
tier 1 — يُحمَّل دائمًا (≤ 8KB)
  ├─ SKILL.md · README.md · CHANGELOG.md

tier 2 — يُحمَّل عند بدء مشروع
  ├─ workflows/intent-router.md      ← نقطة التوجيه
  ├─ workflows/M0–M11/               ← 12 مرحلة / 31 workflow
  ├─ workflows/engines/E1–E5/        ← 5 محركات متخصصة
  └─ workflows/shortcuts/            ← 11 مسارًا سريعًا

tier 3 — يُحمَّل عند الحاجة المتخصصة
  ├─ styles/          ← 10 عوالم + أقفال حرفية + خواتيم + UVP
  ├─ references/      ← protocols (10) · specs (~21) · knowledge (~10) · research (5)
  ├─ schemas/         ← 23 مخطط إخراج
  ├─ quality/         ← 12 بوابة + قوائم فحص
  └─ examples/        ← 4 أمثلة حية

scripts/               ← 9 أدوات فحص قابلة للتنفيذ
```

→ التفاصيل: [`docs/architecture.md`](docs/architecture.md)

---

## 🎯 التوجيه السريع

| إذا كان طلبك... | المسار |
|---|---|
| برومبت واحد / صورة / تحريك صورة | `workflows/shortcuts/` |
| ثامبنيل لفيديو | `workflows/shortcuts/thumbnail.md` |
| **وثائقي / essay / قناة بدون وجه** | `workflows/engines/E1-documentary-engine.md` |
| **إعلان منتج / حملة / brand film** | `workflows/engines/E2-commercial-engine.md` |
| **إعلان بسرد وثائقي** | `workflows/engines/E3-hybrid-commercial.md` |
| **سلسلة أو قناة كاملة** | `workflows/engines/E4-series-engine.md` |
| **تنفيذ بالجملة** | `workflows/engines/E5-bulk-production-pipeline.md` |
| مشهد متعدد اللقطات | `M0` → `M3` |
| فيلم قصير كامل | `M0` → `M11` |

---

## 🎨 العوالم البصرية العشرة

كل عالم = **قفل نصي يُنسخ حرفيًا** في كل برومبت. إعادة الصياغة تكسر الثبات بين 20 لقطة.

| القفل | العالم | الاستخدام |
|---|---|---|
| **A** | Documentary Archive Collage | توقيع VOX — وثائقي، essay |
| **B** | Commercial Craft Collage | **الافتراضي للمنتجات** |
| **C** | Paper Noir Luxury | عطور، ساعات، فخامة |
| **D** | Pop Cutout Playground | سناكس، مشروبات، شباب |
| **E** | Miniature Tabletop Cinematic | تقنية، أجهزة، سيارات |
| **F** | Photoreal Studio | واقعية كاملة بلا ورق |
| **G** | Mixed Media Editorial | مجلات، أزياء، ثقافة |
| **H** | Tactile Clay Diorama | طين/صلصال، سناكس، أطفال |
| **I** | Flat Vector Explainer | **نمط VOX المسطح** — شروح، بيانات |
| **J** | Arabic Calligraphic | هوية عربية معاصرة |

→ `styles/index.md` لشجرة القرار · `styles/locks/` للأقفال الحرفية

---

## 👥 المحركات الخمسة

| المحرك | العقد | المخرج |
|---|---|---|
| **E1** Documentary | آلة حالات 9 خطوات، توقف بعد كل حالة | سكربت + Beats + prompts.txt + UVP + 3 ثامبنيل |
| **E2** Commercial | 10 مراحل، طاقم 9 أدوار | حزمة إعلان كاملة (Brief → Edit Sheet) |
| **E3** Hybrid | دمج VOX + Commercial | إعلان بسرد وثائقي وكولاج |
| **E4** Series | خطة سلسلة + توقيع قناة مقفول | سلسلة متسقة |
| **E5** Bulk | ملف txt + UVP + مونتاج | إرشاد تنفيذ |

---

## 🔬 أدوات البحث (جديد)

| الأداة | الوظيفة |
|---|---|
| `references/research/search-playbook.md` | منهجية البحث وقرار «ابحث أم افترض» |
| `references/research/reference-mining.md` | تعدين المراجع البصرية وحقوقها |
| `references/research/fact-verification.md` | التحقق من الحقائق وتدريج الثقة |
| `references/research/trend-research.md` | الترند والموسمية والمنافسون |
| `references/research/query-library.md` | مكتبة استعلامات جاهزة |

---

## ✅ الجودة

12 بوابة جودة · **بوابتان صلبتان (G4, G8)** تمنعان التسليم عند الفشل.

| المجموعة | البوابات |
|---|---|
| **G0–G8** | الأساسية (العمود الفقري) — G4 و G8 Hard |
| **G9–G13** | السكربت · الـ Beats · المنتج · المنصة · السلسلة |

---

## 🧪 التحقق

```bash
bash scripts/verify_all.sh
```

| # | الفحص | يفحص |
|---|---|---|
| 1 | `verify_structure.py` | البنية + YAML frontmatter |
| 2 | `verify_functional.py` | 95 حالة وظيفية (4 fixtures) |
| 3 | `verify_example.py` | 29 حالة أمثلة |
| 4 | `verify_motion.py` | 46 حالة موشن جرافيك |
| 5 | `verify_styles.py` | الأقفال العشرة + الخواتيم + UVP |
| 6 | `verify_vox.py` | المحركات الخمسة + مراجع v3 |
| 7 | `verify_links.py` | سلامة الروابط الداخلية |
| 8 | `prompt_lint.py` | فحص أي برومبت قبل التسليم |

**الحالة:** ✅ 9/9 ناجحة

فحص برومبت واحد:
```bash
python3 scripts/prompt_lint.py path/to/prompt.txt
```

---

## 📦 التثبيت

### Claude Code / Claude.ai
```bash
cp -r ai-film-studio ~/.claude/skills/
```

### أي وكيل يدعم Agent Skills Standard
انسخ المجلد إلى مجلد المهارات، ثم ابدأ بطلب طبيعي:
> «أريد إعلانًا لمنتج قهوة مختصة، 15 ثانية، Reels»

---

## 🌐 التوافق

| | |
|---|---|
| **الوكلاء** | Claude (Sonnet/Opus) · GPT-4+ · Gemini Pro/Ultra — أي وكيل يدعم Agent Skills Standard |
| **نماذج الصور** | Midjourney · Flux · Nano Banana · GPT Image · Ideogram · Imagen · Seedream |
| **نماذج الفيديو** | Veo · Kling · Runway · Sora · Hailuo · Luma · Wan · Seedance |
| **الصوت** | ElevenLabs (أو أي مولّد) |
| **اللغات** | الشرح بلغة المستخدم · البرومبتات بالإنجليزية |

---

## 📖 الوثائق

| الوثيقة | المحتوى |
|---|---|
| [`docs/architecture.md`](docs/architecture.md) | المعمارية الكاملة |
| [`docs/gap-analysis-v3.md`](docs/gap-analysis-v3.md) | تحليل الفجوات بين النسخ السابقة و v3.0.0 |
| [`docs/migration-v2-to-v3.md`](docs/migration-v2-to-v3.md) | دليل الترقية من v2.x |
| [`docs/m8b-m8c-audit.md`](docs/m8b-m8c-audit.md) | تدقيق مرحلتي M8b و M8c |
| [`CREDITS.md`](CREDITS.md) | الإسناد ونسب النظام |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | دليل المساهمة |

---

## 🧬 نسب النظام

هذا المستودع هو النسخة النهائية الموحّدة لأربعة أنظمة سابقة من نفس المنشئ:

| المستودع | ما أُخذ منه |
|---|---|
| **AI Film Studio v2.1.0** | العمود الفقري M0–M11 · 10-Layer Prompt Architecture · Quality Gates · Memory System |
| **VOX Paper Engine** | محرك الوثائقيات · DNA الكتابة السردية · حساب الـ Beats · نظام الصوت · حمض الثامبنيل |
| **VOX Commercial Director** | طاقم 9 أدوار · Big Idea · 8 عوالم بصرية · Product Reference · بوابات الجودة |
| **VOX Commercial Director Skill v3.0.0** | Brief بـ 12 حقلًا · T1–T4 · منحنى الطاقة · End Card · مصفوفة A/B · Edit Sheet |

---

## 👤 الاعتماد

<div align="center">

**Designed & Built by**

### Waseem Alzobiri

*هندسة الأنظمة · هندسة التوجيهات · معمارية الـ Workflows*

[![GitHub](https://img.shields.io/badge/GitHub-zoih6-181717?logo=github)](https://github.com/zoih6)

</div>

---

## 📜 الترخيص

**MIT** © 2026 Waseem Alzobiri

عند إعادة النشر أو التفرّع، يُرجى الإبقاء على الإسناد.
الأقفال النصية في `styles/locks/` **لا تُعدّل** — أنشئ قفلًا جديدًا بدل تعديل الموجود.

---

<div align="center">

**AI Film Studio v3.0.0** · 9/9 verifications passing · MIT License

*صُمّم وبُني بواسطة **Waseem Alzobiri***

</div>
