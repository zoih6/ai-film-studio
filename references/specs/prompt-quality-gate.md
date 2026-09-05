# Prompt Quality Gate — AI Film Studio v1.3

## Purpose
فحص الـPrompt بعد تركيبه وقبل تسليمه. الهدف منع Prompt يبدو احترافيًا لغويًا لكنه غير قابل للتنفيذ أو متناقض مع الأصول/النموذج.

## Hard Gates
### G1 — Identity
- كل شخصية لها Identity ID أو مرجع واضح عند الحاجة.
- لا يوجد تعارض في العمر/الوجه/الشعر/الملابس/الهوية.

### G2 — Reference Roles
- كل مرجع له وظيفة واضحة.
- لا يُستخدم مرجع Style كمرجع Identity أو العكس.
- FIRST_FRAME وLAST_FRAME يحافظان على أدوارهما.

### G3 — Motion
- فعل رئيسي واحد قابل للرصد.
- حركة كاميرا مهيمنة واحدة.
- بداية → تطور → نهاية واضحة عند الحاجة.
- لا توجد تعليمات متعارضة مثل static + orbit.

### G4 — Continuity
- Scene DNA موروث.
- لا يوجد تغيير غير مبرر في المكان/الضوء/الملابس/الاتجاه/الدعائم.

### G5 — Model Compatibility
- النسبة، المدة، المراجع، الدقة، الصوت، والنمط المطلوب ضمن قدرات الـAdapter.

### G6 — Text Integrity
- النص الحرفي محفوظ.
- يحدد مكان تنفيذ النص: image model / video model / compositing.
- لا يُطلب من مولد الفيديو تنفيذ typography دقيقة إذا كان المسار الصحيح هو compositing.

### G7 — Prompt Hygiene
- لا تكرار جوهري.
- لا حشو إنشائي.
- لا تعليمات متعارضة.
- لا افتراضات عالية التأثير غير معتمدة.

## Soft Score
يمكن حساب درجة داخلية من 0–100، لكن لا تُعرض للمستخدم افتراضيًا. أي Hard Gate فاشل يعني `FAIL` مهما كانت الدرجة.

## Repair Logic
```text
FAIL
→ classify failed gate
→ change the smallest responsible variable
→ recompile
→ revalidate
→ PASS
```

لا تعالج فشل الهوية بإضافة أوصاف إضاءة. أصلح المتغير المسؤول فقط.
