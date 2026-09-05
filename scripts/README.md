# Scripts — أدوات فحص قابلة للتنفيذ

> **فاحصات آلية** تتأكد من سلامة المهارة. شغّلها قبل أي commit.

## المتاح

| السكربت | الوظيفة | المدة |
|---|---|---|
| `verify_structure.py` | يفحص البنية + الروابط + YAML | ~5s |
| `verify_functional.py` | يفحص المسار الوظيفي (M0–M7) | ~10s |
| `verify_motion.py` | يفحص مسار الموشن جرافيك | ~5s |
| `verify_example.py` | يفحص الأمثلة الحية | ~5s |
| `verify_all.sh` | يشغّل الكل | ~30s |

## الاستخدام

```bash
# فحص بنية فقط
python3 scripts/verify_structure.py

# فحص شامل
bash scripts/verify_all.sh

# فحص مسار محدد
python3 scripts/verify_motion.py
```

## آخر نتيجة

```
✅ 4/4 فحوص نجحت
   ✓ Structure: 75+ ملف
   ✓ Functional: 30/30
   ✓ Motion: 46/46
   ✓ Example: 29/29
```
