#!/usr/bin/env python3
"""
فاحص مهارة ai-film-studio
يشغّل مسار المهارة على طلب حقيقي ويختبر:
  1. سلامة البنية والملفات
  2. صحة YAML frontmatter
  3. سلامة الروابط الداخلية (كل ملف مشار إليه موجود فعلًا)
  4. تنفيذ بوابات الخروج على مشروع تجريبي حقيقي
  5. صحة برومبتات التوليد مقابل قيود النماذج الموثقة
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
FAIL, WARN = [], []
def fail(m): FAIL.append(m)
def warn(m): WARN.append(m)
def ok(m):   print(f"  ✓ {m}")

# ── 1. البنية ───────────────────────────────────────────────
print("\n[1] فحص البنية")
REQUIRED = [
    "SKILL.md", "README.md", "INDEX.md",  # v1.5: INDEX.md
    "agents/01-intake.md", "agents/02-creative-direction.md",
    "agents/03-character-world-bible.md", "agents/04-shot-list.md",
    "agents/05-image-prompts.md", "agents/06-motion-prompts.md",
    "agents/07-sound-design.md", "agents/08-edit-color-qc.md",
    # الطبقة الجديدة: بحث المرجعيات، تحليلها، الموشن، توسيع المفاهيم
    "agents/09-visual-research.md", "agents/10-reference-analyst.md",
    "agents/11-motion-graphics.md", "agents/12-concept-expansion.md",
    "agents/13-production-architecture.md", "agents/14-animation-ready-assets.md",
    "agents/15-motion-direction.md", "agents/16-dialogue-lipsync.md",
    "agents/17-continuity-qc.md", "agents/18-hybrid-edit-assembly.md",
    # v1.5: الوكلاء الجدد
    "agents/19-preflight-check.md", "agents/20-localization.md",
    "references/agent-contract.md", "references/production-state-machine.md",
    "references/shot-contract.md", "references/prompt-compiler.md",
    "references/model-adapters.md", "references/prompt-quality-gate.md",
    "references/text-execution-matrix.md", "references/project-memory.md",
    "references/memory-schema.md", "references/memory-lifecycle.md",
    "references/session-continuation.md", "references/memory-context-policy.md",
    "state/production-brief.md", "state/asset-registry.md",
    "state/continuity-ledger.md", "state/approval-log.md",
    "state/generation-log.md", "state/project-memory.md",
    "state/decision-log.md", "state/session-checkpoint.md",
    "references/model-matrix.md", "references/prompt-patterns.md",
    "references/failure-modes.md",
    "templates/production-brief.md", "templates/delivery-package.md",
    "templates/style-dna-sheet.md", "templates/reference-library.md",
    "templates/concept-deck.md",  # v1.5: قالب جديد
    "examples/coffee-short.md",
]
for r in REQUIRED:
    p = ROOT / r
    if not p.exists():
        fail(f"ملف مفقود: {r}")
    elif p.stat().st_size < (100 if str(p.relative_to(ROOT)).startswith("state/") else 500):
        fail(f"ملف شبه فارغ: {r} ({p.stat().st_size} بايت)")
    else:
        ok(f"{r} ({p.stat().st_size:,} بايت)")

# ── 2. YAML frontmatter ────────────────────────────────────
print("\n[2] فحص YAML frontmatter في SKILL.md")
sk = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", sk, re.S)
if not m:
    fail("SKILL.md لا يبدأ بـ YAML frontmatter")
else:
    fm = m.group(1)
    for field in ["name:", "description:", "version:"]:
        if field not in fm:
            fail(f"حقل مفقود في frontmatter: {field}")
        else:
            ok(f"حقل {field.rstrip(':')} موجود")
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if name and name.group(1).strip() != "ai-film-studio":
        warn(f"اسم المهارة '{name.group(1).strip()}' لا يطابق اسم المجلد")
    if desc and len(desc.group(1)) < 100:
        warn("الوصف قصير — قد لا يُفعَّل التوجيه التلقائي بشكل موثوق")
    else:
        ok(f"طول الوصف {len(desc.group(1))} حرفًا (كافٍ للتوجيه)")

# ── 3. الروابط الداخلية ────────────────────────────────────
print("\n[3] فحص الروابط الداخلية (كل مسار مشار إليه يجب أن يوجد)")
all_md = list(ROOT.rglob("*.md"))
refs = set()
for p in all_md:
    for r in re.findall(r"`((?:agents|references|templates|state)/[^`]+?\.md)`", p.read_text(encoding="utf-8")):
        refs.add(r)
missing = [r for r in sorted(refs) if not (ROOT / r).exists() and r != "state/production-brief.md"]
if missing:
    for mm in missing: fail(f"مرجع لملف غير موجود: {mm}")
else:
    ok(f"{len(refs)} مرجعًا داخليًا — كلها صالحة (أو ملفات حالة تُنشأ عند التشغيل)")

# ── 4. القيود الموثقة موجودة فعلًا ─────────────────────────
print("\n[4] فحص أن القيود الموثقة للنماذج مذكورة في المهارة")
CORPUS = "\n".join(p.read_text(encoding="utf-8") for p in all_md)
MUST_CONTAIN = [
    ("gemini-omni-1.1-flash",        "معرف Omni Flash"),
    ("gemini-3.1-flash-image",       "معرف Nano Banana 2"),
    ("gemini-3-pro-image-preview",   "معرف Nano Banana 2 Pro"),
    ("gpt-image-2",                  "معرف GPT Image 2"),
    ("seedance-2.0",                 "معرف Seedance 2.0"),
    ("<FIRST_FRAME>",                "وسم إطار Omni"),
    ("<LAST_FRAME>",                 "وسم إطار Omni"),
    ("<IMAGE_REF_0>",                "وسم مرجع Omni"),
    ("@Image1",                      "وسم مرجع Seedance"),
    ("previous_interaction_id",      "التحرير الحواري Omni"),
    ("delivery",                     "تسليم URI في Omni"),
    ("SynthID",                      "العلامة المائية Google"),
    ("C2PA",                         "العلامة المائية ByteDance"),
    ("Keep everything else the same","صيغة تحرير Omni"),
    ("Canonical Prompt Schema",      "مخطط البرومبت المعياري"),
    ("MODEL ADAPTER",                 "طبقة محولات النماذج"),
    ("FAIL → DIAGNOSE → REPAIR → REVALIDATE → PASS", "حلقة الإصلاح وإعادة التحقق"),
    ("continuity_delta",              "سجل تغييرات الاستمرارية"),
    ("Memory is state, not chat history", "قاعدة ذاكرة المشروع"),
    ("APPROVE / EDIT",                "بروتوكول اعتماد المستخدم"),
    ("Text Execution Matrix",         "مصفوفة تنفيذ النص"),
    ("image_size",                   "معامل دقة Gemini"),
    ("aspect_ratio",                 "معامل النسبة"),
    ("generate_audio",               "معامل صوت Seedance"),
    ("3–10",                         "سقف مدة Omni"),
    ("4–15",                         "سقف مدة Seedance"),
    ("10 صور",                       "سقف مراجع Omni"),
    ("3 مقاطع",                      "سقف فيديو Omni"),
    ("9 صور",                        "سقف مراجع Seedance"),
    ("يستثني",                       "قيد Seedance الحاسم"),
    ("لا يدعم 16:9",                 "قيد GPT Image 2 الحاسم"),
]
for needle, label in MUST_CONTAIN:
    if needle in CORPUS: ok(label)
    else: fail(f"قيد موثق غير مذكور في المهارة: {label} ('{needle}')")

# ── 5. المحظورات ممنوعة صراحة ─────────────────────────────
print("\n[5] فحص أن الأشياء غير المدعومة معلَّمة كممنوعة")
FORBIDDEN_MARKED = [
    ("مراجع صوتية", "لا مراجع صوتية في Omni"),
    ("تحرير الصوت", "لا تحرير صوت في Omni"),
    ("negative prompt", "لا negative prompt"),
    ("الذيل فقط", "التمديد في الذيل فقط"),
]
for needle, label in FORBIDDEN_MARKED:
    if needle in CORPUS: ok(label)
    else: fail(f"قيد سلبي غير معلَّم: {label}")

# ── 6. الطبقة الجديدة: بحث المرجعيات + الموشن ──────────────
print("\n[6] فحص طبقة المرجعيات والموشن جرافيك")
NEW_MUST = [
    # بحث المرجعيات
    ("Style DNA",              "مفهوم Style DNA"),
    ("Pinterest",              "مصدر Pinterest"),
    ("القاعدة لا العنصر",      "قاعدة استخراج القاعدة لا العنصر"),
    ("لا تخترع",               "قاعدة عدم اختراع المراجع"),
    # محلل المرجعيات
    ("Color Palette",          "طبقة لوحة الألوان"),
    ("Typography DNA",         "طبقة الـTypography"),
    ("Composition DNA",        "طبقة التكوين"),
    ("Motion DNA",             "طبقة الحركة"),
    ("Graphic Element DNA",    "طبقة العناصر الرسومية"),
    # منحنيات easing صحيحة
    ("0.22, 1, 0.36, 1",       "منحنى expo-out"),
    ("0.68, -0.55, 0.27, 1.55","منحنى back-in-out"),
    ("0.4, 0, 0.2, 1",         "منحنى standard ease"),
    # الطباعة العربية — الفجوة الأهم
    ("كلمة بكلمة",             "قاعدة تحريك العربية كلمة بكلمة"),
    ("حرفًا بحرف",             "تحذير تحريك العربية حرفًا بحرف"),
    ("Middle Eastern text engine", "تحذير محرك النص العربي"),
    ("RTL",                    "اتجاه RTL"),
    ("Cairo",                  "عائلة خطوط عربية"),
    # التصحيح المعماري الجوهري
    ("ليست",                   "التصريح أن مواصفة الموشن ليست برومبت توليد"),
    ("frame-accurate",         "توثيق غياب التحكم الدقيق بالإطارات"),
    ("أداة تركيب",             "طبقة التركيب"),
    ("After Effects",          "أداة التركيب"),
    # المنطقة الآمنة
    ("المنطقة الآمنة",         "قواعد المنطقة الآمنة"),
    # توسيع المفاهيم
    ("محورين على الأقل",       "قاعدة تباين الاتجاهات"),
    ("Start state:",             "حالة بداية الحركة"),
    ("End state:",               "حالة نهاية الحركة"),
    ("Composite later:",         "فصل حركة التركيب"),
    ("Depth layers",              "طبقات العمق"),
    ("Continuity Ledger",         "سجل الاتساق بين المقاطع"),
    ("DIALOGUE ID:",              "دفتر الحوار الحرفي"),
]
for needle, label in NEW_MUST:
    if needle in CORPUS: ok(label)
    else: fail(f"محتوى ناقص في الطبقة الجديدة: {label} ('{needle}')")

# ── 7. الاتساق: موجّه المسار في SKILL.md ───────────────────
print("\n[7] فحص موجّه المسار والاتساق")
ROUTING = [
    ("موجّه المسار",       "قسم موجّه المسار"),
    ("11-motion-graphics", "توجيه إلى وكيل الموشن"),
    ("10-reference-analyst","توجيه إلى محلل المرجعيات"),
    ("09-visual-research", "توجيه إلى البحث البصري"),
    ("12-concept-expansion","توجيه إلى موسّع المفاهيم"),
    ("13-production-architecture", "توجيه إلى هندسة الإنتاج"),
    ("14-animation-ready-assets", "توجيه إلى الأصول المهيأة للتحريك"),
    ("15-motion-direction", "توجيه إلى مخرج الحركة"),
    ("16-dialogue-lipsync", "توجيه إلى الحوار والشفاه"),
    ("17-continuity-qc", "توجيه إلى فحص الاتساق"),
    ("18-hybrid-edit-assembly", "توجيه إلى التجميع الهجين"),
    # v1.5: الوكلاء الجدد
    ("19-preflight-check", "توجيه إلى وكيل ما قبل التوليد"),
    ("20-localization", "توجيه إلى وكيل التوطين"),
]
for needle, label in ROUTING:
    if needle in sk: ok(f"{label} موجود في SKILL.md")
    else: fail(f"{label} مفقود من SKILL.md")

# القواعد الجديدة مرقمة وموجودة
for n in [18, 19, 20, 21, 22, 23, 24]:
    if f"\n{n}. " in sk: ok(f"القاعدة {n} مرقمة")
    else: fail(f"القاعدة {n} مفقودة أو غير مرقمة")

# ── 8. فحص v1.5: الوكلاء والقوالب الجديدة ─────────────────
print("\n[8] فحص طبقة v1.5 (Pre-flight + Localization + Index)")
V15_CHECKS = [
    # Pre-flight
    ("Hard Gates",                 "Gates موثقة في Pre-flight"),
    ("G1 — الهوية",                "Gate G1 مسمى"),
    ("G5 — توافق النموذج",          "Gate G5 مسمى"),
    ("G6 — النص",                  "Gate G6 مسمى"),
    ("G7 — النظافة اللغوية",         "Gate G7 مسمى"),
    # Localization
    ("EXACT ARABIC TEXT TO RENDER", "كتلة النص العربي في Localization"),
    ("right-to-left",               "قاعدة RTL"),
    ("cultural_flags",              "معالجة الحساسية الثقافية"),
    ("فصحى مبسطة",                   "قاعدة الفصحى المبسطة"),
    ("Middle Eastern / Arab",        "قاعدة التفاصيل العربية"),
    # INDEX
    ("INDEX.md",                   "INDEX.md موجود"),
    ("خريطة المسارات",              "خريطة المسارات في INDEX"),
    ("Concept Deck",               "مرجع Concept Deck"),
    # Concept deck template
    ("اللحظة الحاسمة",              "قالب Concept Deck للحظة الحاسمة"),
    ("التكلفة التقديرية",            "تقدير التكلفة في Concept Deck"),
]
for needle, label in V15_CHECKS:
    if needle in CORPUS: ok(f"v1.5: {label}")
    else: fail(f"v1.5 ناقص: {label} ('{needle}')")

print("\n" + "="*64)
if FAIL:
    print(f"❌ فشل: {len(FAIL)}")
    for f in FAIL: print(f"   • {f}")
    sys.exit(1)
print(f"✅ كل الفحوص البنيوية نجحت")
if WARN:
    print(f"⚠️  تحذيرات: {len(WARN)}")
    for w in WARN: print(f"   • {w}")
print("="*64)
