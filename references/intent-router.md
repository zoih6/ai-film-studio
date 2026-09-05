# Intent Router — AI Film Studio v1.2

## Purpose
حوّل طلب المستخدم إلى **أصغر مسار إنتاجي كافٍ** بدل تشغيل M0–M13 دائمًا.

## Routing Contract
قبل أي تنفيذ، استخرج داخليًا:
- `intent`: ما الذي يريد المستخدم الحصول عليه الآن؟
- `scope`: مفرد / لقطة / مشهد / مشروع كامل.
- `inputs`: صور، فيديو، صوت، نص، مراجع، ملفات.
- `state`: مشروع جديد أم استمرار لمشروع قائم.
- `output`: prompt / plan / assets / production package / repair.
- `constraints`: مدة، نسبة، منصة، نموذج، هوية، لغة، نص حرفي.

## Priority
طبّق القواعد بالترتيب:
1. طلب إصلاح واضح → `REPAIR` للمخرج المتضرر فقط.
2. طلب تحريك صورة/فريم موجود → `IMAGE_TO_VIDEO`.
3. طلب صورة/فريم ثابت → `IMAGE_GENERATION`.
4. طلب موشن جرافيك/kinetic typography → `MOTION_GRAPHICS`.
5. طلب حوار/لِبسِنك → `DIALOGUE_LIPSYNC`.
6. طلب لقطة واحدة من مشروع قائم → `SHOT_BUILD` مع وراثة الحالة.
7. طلب مشهد متعدد اللقطات → `SCENE_BUILD`.
8. طلب فيلم/إعلان متعدد المشاهد → `FULL_PRODUCTION`.
9. طلب «اكتب برومبت» دون نطاق واضح → `PROMPT_ONLY`.
10. طلب فكرة فقط → `CONCEPT`.

## Minimum Sufficient Pipeline
| Intent | Minimum internal path |
|---|---|
| CONCEPT | 01 → 02 → 12 عند الحاجة |
| PROMPT_ONLY | context → prompt-patterns → model adaptation |
| IMAGE_GENERATION | reference analysis عند وجود مراجع → 05 |
| IMAGE_TO_VIDEO | reference analysis → 14 → 15 → 06 |
| MOTION_GRAPHICS | 11 → text execution matrix → delivery |
| DIALOGUE_LIPSYNC | 16 → 06/07 حسب الحاجة |
| SHOT_BUILD | continuity → 05/14 → 15 → 06 → 07 عند الحاجة |
| SCENE_BUILD | 02/03 → 04 → shot pipeline |
| FULL_PRODUCTION | M0–M13 |
| REPAIR | diagnose → affected specialist → revalidate |

## Escalation
المسار يبدأ صغيرًا ويُوسّع فقط إذا ظهر اعتماد حقيقي على مرحلة إضافية. لا تُشغّل مرحلة لمجرد أنها موجودة.

## No-Ask Rule
لا تسأل المستخدم عن قرار يستطيع الاستوديو حسمه مهنيًا، مثل العدسة أو نوع الحركة أو توزيع الإضاءة، إلا إذا كان هناك أكثر من خيار متعارض وله أثر جوهري على النتيجة.

## Router Output (Internal)
```yaml
intent: IMAGE_TO_VIDEO
scope: shot
state: existing_project
inputs: [reference_image]
required_agents: [10, 14, 15, 6]
optional_agents: [16, 7, 17]
user_questions_needed: 0-3
output_mode: DELIVER
```
