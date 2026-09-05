# Schemas

> **Tier 3 — هياكل البيانات (Data Structures).** تُحمَّل عند إنتاج المخرجات.

كل ملف هنا هو **قالب فارغ** أو **مثيل حي** لمخرج معيّن. الـ schemas ليست برومبتات — هي **هياكل بيانات** تُملأ ثم تُسلّم.

## التصنيف

### مخرجات الإنتاج (Production Outputs)

| الملف | متى يُستخدم | يُنتَج من |
|---|---|---|
| `production-blueprint.md` | نهاية M0–M9 | Executive Producer |
| `image-prompts-package.md` | M7 | Prompt Architecture |
| `motion-prompts-package.md` | M8 | Prompt Architecture |
| `audio-package.md` | M6 | Audio Decision Engine |
| `assembly-guide.md` | M10 | Executive Producer |
| `concept-deck.md` | M1 (Concept) | Research Lab |
| `style-dna-sheet.md` | M4b | Character-World |
| `delivery-package.md` | M10 | EP (قديم) |
| `production-brief.md` | M0 | Intake (قديم) |

### State Files (Runtime State)

في `state/`:
- `project-memory.md` — ذاكرة المشروع الدائمة
- `continuity-bible.md` — قاموس الهوية البصرية
- `frame-chain.md` — Start/End Frame Registry
- `asset-registry.md` — كل الأصول المُنتجة
- `decision-log.md` — كل القرارات المهمة
- `risk-register.md` — المخاطر + mitigation
- `quality-gates-log.md` — G0–G8 log
- `production-brief.md` — موجز المشروع
- `production-blueprint.md` — نسخة state من blueprint
- `reference-library.md` — مرجعيات بصرية
- `continuity-ledger.md` — سجل اتساق
- `approval-log.md` — الموافقات
- `generation-log.md` — محاولات التوليد
- `session-checkpoint.md` — checkpoint للجلسات

## كيف تستخدم

1. **انسخ** الـ schema المناسب إلى مشروعك
2. **املأ** كل قسم (لا تترك حقول فارغة)
3. **اربط** cross-references بين الـ schemas
4. **سلّم** عبر EP
