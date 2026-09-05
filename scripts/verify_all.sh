#!/usr/bin/env bash
# فاحص مهارة ai-film-studio — يشغّل كل الاختبارات
cd "$(dirname "$0")"
rc=0
echo "═══════════════════════════════════════════"
echo " 1/4  الفحص البنيوي"
echo "═══════════════════════════════════════════"
if python3 verify_structure.py > /tmp/s.log 2>&1; then
    tail -8 /tmp/s.log
else
    cat /tmp/s.log
    rc=1
fi
echo
echo "═══════════════════════════════════════════"
echo " 2/4  الفحص الوظيفي — المسار السردي"
echo "═══════════════════════════════════════════"
if python3 verify_functional.py > /tmp/f.log 2>&1; then
    tail -6 /tmp/f.log
else
    cat /tmp/f.log
    rc=1
fi
echo
echo "═══════════════════════════════════════════"
echo " 3/4  فحص المثال الحي"
echo "═══════════════════════════════════════════"
if python3 verify_example.py > /tmp/e.log 2>&1; then
    tail -5 /tmp/e.log
else
    cat /tmp/e.log
    rc=1
fi
echo
echo "═══════════════════════════════════════════"
echo " 4/4  الفحص الوظيفي — مسار الموشن جرافيك"
echo "═══════════════════════════════════════════"
if python3 verify_motion.py > /tmp/m.log 2>&1; then
    tail -7 /tmp/m.log
else
    cat /tmp/m.log
    rc=1
fi
echo
echo "═══════════════════════════════════════════"
if [ $rc -eq 0 ]; then echo " ✅ كل الاختبارات نجحت"; else echo " ❌ فشل"; fi
echo "═══════════════════════════════════════════"
exit $rc
