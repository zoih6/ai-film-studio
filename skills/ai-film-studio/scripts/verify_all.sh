#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════
#  AI Film Studio v3.0.0 — الفاحص الشامل
#  يشغّل 9 فحوص: البنية · الوظيفي · الأمثلة · الموشن · الأنماط
#                 المحركات · الروابط · البرومبتات
#  الاستخدام:  bash scripts/verify_all.sh
# ══════════════════════════════════════════════════════════════════
cd "$(dirname "$0")" || exit 1

rc=0
passed=0
failed=0
TOTAL=9
n=0

run_check () {
    local title="$1"; local script="$2"; shift 2
    n=$((n+1))
    echo
    echo "═══════════════════════════════════════════"
    echo " $n/$TOTAL  $title"
    echo "═══════════════════════════════════════════"
    if python3 "$script" "$@" > "/tmp/afs_$n.log" 2>&1; then
        tail -6 "/tmp/afs_$n.log"
        passed=$((passed+1))
    else
        cat "/tmp/afs_$n.log"
        failed=$((failed+1))
        rc=1
    fi
}

run_check "فحص حزمة المهارة والـ Plugin"          verify_package.py

echo
echo "╔═══════════════════════════════════════════╗"
echo "║  AI Film Studio v3.0.0 — الفاحص الشامل    ║"
echo "║  Designed & Built by Waseem Alzobiri      ║"
echo "╚═══════════════════════════════════════════╝"

run_check "الفحص البنيوي (structure + YAML)"   verify_structure.py
run_check "الفحص الوظيفي (المسار السردي)"      verify_functional.py
run_check "فحص المثال الحي"                    verify_example.py
run_check "الفحص الوظيفي (مسار الموشن جرافيك)"  verify_motion.py
run_check "مكتبة الأنماط (LOCK A–J + Closers)" verify_styles.py
run_check "المحركات والتكامل (E1–E5)"          verify_vox.py
run_check "سلامة الروابط الداخلية"             verify_links.py
run_check "فاحص البرومبتات (اختبار ذاتي)"      prompt_lint.py --selftest

echo
echo "═══════════════════════════════════════════"
if [ $rc -eq 0 ]; then
    echo " ✅ كل الاختبارات نجحت ($passed/$TOTAL)"
else
    echo " ❌ فشل: $failed من $TOTAL"
fi
echo "═══════════════════════════════════════════"
echo
exit $rc
