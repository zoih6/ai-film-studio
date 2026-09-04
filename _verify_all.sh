#!/usr/bin/env bash
# فاحص مهارة ai-film-studio — يشغّل كل الاختبارات
set -uo pipefail
cd "$(dirname "$0")"
rc=0
echo "═══════════════════════════════════════════"
echo " 1/4  الفحص البنيوي"
echo "═══════════════════════════════════════════"
python3 _verify_structure.py > /tmp/s.log 2>&1 || rc=1
tail -8 /tmp/s.log
echo
echo "═══════════════════════════════════════════"
echo " 2/4  الفحص الوظيفي — المسار السردي"
echo "═══════════════════════════════════════════"
python3 _verify_functional.py > /tmp/f.log 2>&1 || rc=1
tail -6 /tmp/f.log
echo
echo "═══════════════════════════════════════════"
echo " 3/4  فحص المثال الحي"
echo "═══════════════════════════════════════════"
python3 _verify_example.py || rc=1
echo
echo "═══════════════════════════════════════════"
echo " 4/4  الفحص الوظيفي — مسار الموشن جرافيك"
echo "═══════════════════════════════════════════"
python3 _verify_motion.py > /tmp/m.log 2>&1 || rc=1
tail -7 /tmp/m.log
echo
echo "═══════════════════════════════════════════"
if [ $rc -eq 0 ]; then echo " ✅ كل الاختبارات نجحت"; else echo " ❌ فشل"; fi
echo "═══════════════════════════════════════════"
exit $rc
