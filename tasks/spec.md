# Spec: AI Film Studio v2.0.2 — Stage Model Unification

## Objective

إزالة التضاربات البنيوية في تعريف مراحل الإنتاج (M0–M13 vs M0–M11) وتحقيق
**Source of Truth واحد** للـ pipeline. لا ميزات جديدة، فقط ترميم ادعاءات v2.0.0
التي لم تكن متسقة مع الواقع.

**User Story:** قارئ المستودع (LLM أو مهندس) يجب أن يحصل على نفس التعريف
للمراحل بغض النظر عن الملف الذي يفتحه. لا M0–M13 و M0–M11 في نفس المستودع.

**Success Criteria:**

1. لا توجد إشارات إلى `M12` أو `M13` أو `M14` في أي ملف في المستودع (ماعدا CHANGELOG التاريخي).
2. `references/protocols/production-state-machine.md` هو المرجع **الوحيد** لتعريف المراحل والـ gates.
3. كل من `M9a-executive-producer.md` و `SKILL.md` و `README.md` و `intent-router.md` يستخدم نفس تعريف M2/M3/M11.
4. وجود ملف `references/protocols/orchestration-runtime.md` صريح وقابل للتنفيذ، يغطي 9 مسارات.
5. `M4c-continuity-qc.md` إلزامي في كل مسار `SCENE_BUILD` و `FULL_PRODUCTION`، اختياري في `IMAGE_GENERATION` و `SINGLE_PROMPT`.

## Tech Stack

- Markdown files (لا code).
- YAML frontmatter (tier 3 references).
- Python 3.x (verify scripts).
- Git (commits).

## Commands

```bash
# Phase: اصلاحات
# (لا build ولا test ولا lint في هذا الإصدار — فقط markdown)

# فحص بعد التعديل:
bash scripts/verify_all.sh
grep -rn "M12\|M13\|M14" --include="*.md" workflows/ references/ schemas/ examples/ quality/ scripts/ 2>/dev/null

# commit
git add -A && git commit -m "v2.0.2: unify stage model + orchestration runtime" && git push origin main
```

## Project Structure (الملفات المتأثرة)

### ملفات معدّلة (4)

| المسار | السبب |
|---|---|
| `references/protocols/production-state-machine.md` | تحويله من v1.1 (M0–M13) إلى v2.0.2 (M0–M11 + substage). المرجع الرسمي الوحيد. |
| `workflows/M9a-executive-producer.md` | تصحيح M3=Narrative → M2=Narrative، M3=Shot Architecture، M11=Final Assembly. محاذاة pipeline الكامل (YAML، 5 Output Files، Decision Log، Risk Register) مع workflow filesystem. |
| `SKILL.md` | قسم "12 stages / 31 workflows" واضح. جدول المراحل الـ12 يطابق الواقع. |
| `README.md` | نفس الشيء + قسم "12 stages / 31 workflows" في Repository Structure. |
| `quality/quality-gates.md` | تحديد رسمي: `production-state-machine.md` هو authoritative للـ stages، `M9b-quality-gates.md` للتفاصيل. شرح اختلاف عدد الـ gates (8 vs 14) كـ "8 gates للـ end-to-end، 14 gates للـ per-stage". |
| `workflows/intent-router.md` | تحديث M3 (M3a-shot-design.md)، M11 (M11a/M11b). إضافة M4c required في SCENE/FULL routes. |
| `workflows/README.md` | خريطة substage → stage (31 → 12). |
| `references/protocols/interaction-flow.md` | M0–M13 → M0–M11 في المخططين النصيين. |
| `workflows/M9d-localization.md` | M13 → M11 (السطر 26). |
| `CHANGELOG.md` | إضافة بند v2.0.2. |

### ملفات جديدة (1)

| المسار | المحتوى |
|---|---|
| `references/protocols/orchestration-runtime.md` | executable spec لـ 9 مسارات (REPAIR، IMAGE_TO_VIDEO، IMAGE_GENERATION، MOTION_GRAPHICS، DIALOGUE_LIPSYNC، SHOT_BUILD، SCENE_BUILD، FULL_PRODUCTION، PROMPT_ONLY، CONCEPT). |

## Code Style

- YAML في code blocks: indentation بمسافتين، لا tabs.
- Stage references تستخدم `M0–M11` (en-dash) في النصوص، `M0..M11` في الـ code.
- substage references: `M1a`، `M1b`، ... بصيغة ثابتة (لا توجد M1d أو M0b).

## Testing Strategy

- 4 سكربتات verify الحالية (`verify_structure.py`, `verify_functional.py`, `verify_motion.py`, `verify_example.py`) يجب أن تنجح كلها 4/4.
- `bash scripts/verify_all.sh` = نقطة الفحص الإلزامية.
- grep يدوي للتأكد من عدم وجود `M12`/`M13` بعد التعديل (باستثناء CHANGELOG التاريخي).

## Boundaries

**Always do:**
- اتبع workflow filesystem كـ source of truth عند أي تضارب.
- أضف `## v2.0.2` بند في CHANGELOG.md.
- حافظ على backward compatibility (v1.x يبقى يعمل).

**Ask first:**
- لا تغيير في أي workflow file فردي إلا إذا كان التصحيح منطقياً.
- لا تحذف أي ملف.

**Never do:**
- لا تخترع workflow جديد (لا M0b، لا M1d، لا M13-bis).
- لا تضيف Memory Conflict Resolution.
- لا تضيف Story/Editorial QC.
- لا تعيد كتابة `verify_functional.py`.
- لا تحدث `M8b` أو `M8c`.
- لا تحدث `prompt-compiler.md` أو `model-adapters.md`.

## Open Questions

- لا شيء. النطاق محدد بوضوح في طلب المستخدم.
