---
name: schema-storyboard
description: "عقد الـStoryboard المرئي: مشاهد وفريمات مرتبة قبل Prompts الصور."
tier: 3
when_to_load: "بعد اعتماد الرؤية وقبل توليد Prompts الصور"
---

# Storyboard Contract

الـStoryboard هو طبقة العرض الأولى قبل البرومبتات. هدفه أن يفهم المستخدم تسلسل العمل دون إغراقه في تفاصيل التنفيذ.

## الحقول الإلزامية

```yaml
storyboard:
  project_id: "..."
  aspect_ratio: "16:9"
  total_duration_seconds: 15
  scenes:
    - scene_id: "SC01"
      title: "..."
      purpose: "وظيفة المشهد"
      frames:
        - frame_id: "FR01"
          shot_id: "SC01_SH01"
          role: "opening"
          visual_description: "وصف بصري مختصر"
          duration_seconds: 2
          start_state: "..."
          end_state: "..."
          image_prompt_status: "pending"
```

## قواعد العرض

- اعرض المشاهد بالترتيب الزمني.
- اجعل الوصف البصري مختصرًا وقابلًا للتخيل.
- لا تعرض Prompt الصورة في جدول الـStoryboard.
- اربط كل فريم بـ`frame_id` ثابت سيظهر لاحقًا في Prompt الصورة والتحريك.
- لا تنشئ فريمات إضافية لمجرد تغطية طبقات Prompt.
- عدد الفريمات يخدم القصة والانتقال، لا حجم النظام.

## بوابة الانتقال

لا تبدأ Prompts الصور حتى يعتمد المستخدم الـStoryboard في مشروع متعدد المشاهد. إذا طلب المستخدم التنفيذ المباشر، اعتبر الـStoryboard معتمدًا ضمنيًا بعد عرض ملخصه المختصر.
