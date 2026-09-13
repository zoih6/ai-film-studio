# AI Film Studio

**AI Film Studio** هو Skill/Plugin احترافي لتحويل فكرة فيديو إلى حزمة إنتاج قابلة للتنفيذ: من الـBrief والاتجاه الإبداعي، مرورًا بالسرد والـBeats واللقطات والهوية البصرية، وصولًا إلى برومبتات الصور والحركة والصوت والمونتاج والتسليم.

> **الفكرة أولًا، والبرومبت لاحقًا.** لا تبدأ المهارة بكتابة prompt قبل تثبيت الفكرة، المنتج، السرد، الإيقاع، الاستمرارية، ومتطلبات المنصة.

[![Version](https://img.shields.io/badge/version-3.0.0-111827)](SKILL.md)
[![Skill](https://img.shields.io/badge/format-Agent%20Skill-7c3aed)](SKILL.md)
[![License](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

## التثبيت كرابط Plugin / Skill

ضع الرابط التالي في وكيل يدعم تثبيت Plugins أو Agent Skills:

```text
Install the AI Film Studio skill/plugin from https://github.com/zoih6/ai-film-studio.
Read the repository's AGENTS.md for instructions, use SKILL.md as the canonical behavior, and start at workflows/intent-router.md.
```

- **الرابط الأساسي:** <https://github.com/zoih6/ai-film-studio>
- **ملف التعليمات الأساسي:** [`SKILL.md`](SKILL.md)
- **تعليمات التثبيت للمضيفين:** [`INSTALL.md`](INSTALL.md)
- **تعليمات الوكلاء والمساهمين:** [`AGENTS.md`](AGENTS.md)
- **دليل الـPlugin:** [`plugin.json`](plugin.json)
- **مصفوفة الدعم والقيود:** [`docs/support-matrix.md`](docs/support-matrix.md)

## ماذا تقدم المهارة؟

تتعامل المهارة مع المشاريع التالية:

| نوع المشروع | المخرج الرئيسي |
| --- | --- |
| فيلم قصير أو سردي | Concept، Script، Beat Table، Shot Cards، Prompts، Audio، Edit Sheet |
| إعلان أو Brand Film | Brief، Big Idea، Product Anchor، مصفوفة A/B، End Card، Delivery Pack |
| وثائقي أو Video Essay | بحث وتحقق، سرد، Beats، Prompts TXT، Universal Video Prompt، Thumbnails |
| موشن جرافيك | بنية المشاهد، حركة العناصر، النص، الإيقاع، ومواصفات التصدير |
| سلسلة أو قناة | Series Bible، توقيع بصري، قالب حلقة، واستمرارية بين الحلقات |

## كيف تعمل؟

1. اقرأ `SKILL.md` ثم ابدأ من `workflows/intent-router.md`.
2. حدّد نوع المشروع، المنصة، المدة، اللغة، النبرة، ونموذج التوليد إن كان معروفًا.
3. اختر المسار المناسب: Shortcut، Engine، أو المسار الكامل `M0 → M11`.
4. حمّل فقط المراجع والمخططات المطلوبة للمسار؛ لا تُحمّل المستودع كاملًا في كل طلب.
5. ثبّت الـStyle Lock والـEntity Ledger والـContinuity قبل كتابة prompts النهائية.
6. مرّر الناتج عبر بوابات الجودة المناسبة قبل التسليم.

## خريطة المستودع

| المسار | الاستخدام |
| --- | --- |
| `SKILL.md` | السلوك الأساسي، المحفزات، قواعد العمل، ونقطة الدخول |
| `workflows/` | مراحل الإنتاج، المحركات، والمسارات السريعة |
| `references/` | البروتوكولات والمواصفات والمعرفة وأدوات البحث |
| `schemas/` | عقود ومخططات المخرجات |
| `styles/` | فهرس العوالم البصرية والأقفال النصية |
| `quality/` | بوابات الجودة وقوائم الفحص |
| `examples/` | أمثلة إنتاجية قابلة للقراءة |
| `scripts/` | أدوات التحقق والفحص |
| `schemas/` | عقود النية والحالة والمزودين والمخرجات |
| `references/protocols/agent-protocol.md` | بروتوكول تفاعل الوكيل والتعافي من الأخطاء |
| `workflows/provider-routing.md` | اختيار المزود والبدائل وتسجيل القرار |
| `docs/research/` | ملاحظات البحث ومبررات التطوير |
| `.claude-plugin/` | تعريف Claude Code والـmarketplace |
| `.codex-plugin/` و `.agents/` | تعريف Codex والـmarketplace |
| `skills/` و `.cursor/` | مسارات توافق Agent Skills وCursor |

## نقطة التوجيه

يبدأ كل طلب إنتاج من [`workflows/intent-router.md`](workflows/intent-router.md):

- إعلان أو Brand Film: `workflows/engines/E2-commercial-engine.md`
- وثائقي أو Essay أو Faceless: `workflows/engines/E1-documentary-engine.md`
- إعلان هجين: `workflows/engines/E3-hybrid-commercial.md`
- سلسلة: `workflows/engines/E4-series-engine.md`
- إنتاج بالجملة: `workflows/engines/E5-bulk-production-pipeline.md`
- مهمة صغيرة أو Prompt واحد: `workflows/shortcuts/`
- مشروع كامل: `M0` إلى `M11`

## عقد التشغيل الاحترافي

للمشاريع القابلة للتتبع، ابدأ بإنشاء `generation-intent` ثم اربطه بـ`project-manifest` وسجلات المخرجات. يسجل النظام نوع المشروع، نطاق العمل، الـIDs، التبعيات، الأقفال، المصدر، المزود المختار، والنتيجة (`candidate` أو `qualified` أو `not-yet-verified`).

لا تعتبر المهارة أي قدرة خارجية مثبتة تلقائيًا: يجب أن يكون المزود موثقًا في سجل القدرات، ويجب تسجيل البديل وسبب الاختيار. كما أن نجاح الفحوص البنيوية لا يثبت صلاحية ملف فيديو أو الصوت أو الاستمرارية البصرية ما لم تُنفذ تلك الفحوص فعليًا.

→ البروتوكول الكامل: [`references/protocols/agent-protocol.md`](references/protocols/agent-protocol.md) · [`docs/research/2026-09-14-system-upgrade.md`](docs/research/2026-09-14-system-upgrade.md)

## التحقق

شغّل الفحص الكامل من جذر المستودع:

```bash
bash scripts/verify_all.sh
```

ولفحص تغليف الـSkill والـPlugin فقط:

```bash
python3 scripts/verify_package.py
```

الفحوص تتحقق من البنية، المسارات، الأمثلة، الأقفال البصرية، المحركات، الروابط، والـprompts. التحذيرات المعلوماتية لا تعني فشلًا ما لم يذكر الفحص صراحة وجود أخطاء.

## المساهمة

اقرأ [`CONTRIBUTING.md`](CONTRIBUTING.md) و[`AGENTS.md`](AGENTS.md) قبل تعديل المهارة. لا تعدّل الأقفال الموجودة مباشرة؛ أضف قفلًا جديدًا عند الحاجة، وحافظ على `SKILL.md` كمصدر الحقيقة الوحيد للتعليمات.

## الترخيص

MIT © 2026 [Waseem Alzobiri](https://github.com/zoih6)
