# Model Adapter Layer — AI Film Studio v1.3

## Purpose
يفصل «ماذا نريد إنتاجه» عن «كيف نخاطب النموذج». الـCanonical Shot Spec ثابت؛ الـAdapter يترجمه إلى صيغة النموذج المستهدف.

## Adapter Contract
```yaml
adapter_id: ADAPTER-<MODEL>
input: canonical_prompt_spec
output:
  prompt_syntax: ...
  reference_syntax: ...
  supported_controls: ...
  unsupported_controls: ...
  settings: ...
validation:
  - capability_check
  - reference_check
  - aspect_ratio_check
  - duration_check
  - text_check
```

## Selection Policy
- إذا حدّد المستخدم نموذجًا، استخدمه ما لم يكن غير متوافق مع المتطلبات؛ عندها اشرح التعارض باختصار واقترح البديل.
- إذا لم يحدده، اختر النموذج الأنسب بناءً على المهمة، النسبة، المدة، المراجع، النص، والحاجة إلى الصوت/التحرير.
- لا تغيّر Creative Spec لتناسب النموذج؛ غيّر الصياغة أولًا، وغيّر النموذج فقط إذا كانت القدرة المطلوبة غير مدعومة.

## Capability-Aware Translation
قبل التسليم، افحص:
1. هل النسبة المطلوبة مدعومة؟
2. هل المدة مطلوبة ومدعومة؟
3. هل نوع المراجع المطلوب مدعوم؟
4. هل الصوت/الحوار/الـlipsync مطلوب ومدعوم؟
5. هل النص داخل الصورة/الفيديو يحتاج مسارًا خارجيًا؟
6. هل FIRST/LAST frame أو edit mode متاح؟

## Model Profiles
لا تثق بأي مواصفة رقمية قديمة من الذاكرة. استخدم `specs.md` كمصدر داخلي، واعتبر بيانات Preview قابلة للتغير. عند وجود عدم يقين، لا تخترع capability.

## Adapter Principle
```text
ONE SHOT SPEC
   ├── Adapter A → syntax/settings A
   ├── Adapter B → syntax/settings B
   └── Adapter C → syntax/settings C
```

المستخدم لا يرى طبقة الـAdapter إلا إذا طلب مقارنة النماذج أو سبب اختلاف الصياغة.
