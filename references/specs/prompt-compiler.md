# Prompt Compiler — AI Film Studio v1.3

## Purpose
حوّل مواصفة إنتاج منظمة إلى Prompt نهائي قابل للتنفيذ. لا يكتب الـPrompt من الصفر اعتمادًا على البلاغة؛ بل يركّبه من حقول إنتاجية ثابتة ثم يزيل التعارض والتكرار.

## Compilation Chain
```text
USER INTENT
→ CREATIVE SPEC
→ SCENE DNA
→ SHOT DNA
→ MODEL ADAPTER
→ PROMPT COMPILER
→ QUALITY GATE
→ COPY-READY PROMPT
```

## Canonical Prompt Schema
```yaml
prompt_id: SC01_SH01_VIDEO_v001
output_type: image | image_to_video | text_to_video | edit | motion_graphics | dialogue
model_target: auto | named_model
references:
  - role: CHARACTER | STYLE | WORLD | PROP | FIRST_FRAME | LAST_FRAME | MOTION | AUDIO | TEXT
    source: ...
creative_intent: ...
subject: ...
action: ...
framing: ...
camera: ...
lighting: ...
environment: ...
style: ...
timeline: ...
audio: ...
continuity: ...
text: ...
constraints: ...
output_settings: ...
```

## Compilation Rules
1. Preserve user-provided exact text verbatim when text fidelity is required.
2. Inherit approved Scene DNA before adding shot-specific details.
3. Keep one dominant subject action and one dominant camera movement per shot unless the target model explicitly supports more.
4. Convert vague adjectives into observable production instructions.
5. Remove duplicate constraints.
6. Resolve contradictions before delivery; never knowingly emit contradictory instructions.
7. Put high-priority instructions early.
8. Keep model-specific syntax in the adapter layer, not in the canonical spec.
9. Do not invent missing facts. Infer only low-risk production details; mark high-impact assumptions internally.
10. Output one canonical prompt unless the user explicitly requests variants.

## Priority Order
`identity/reference locks > user constraints > composition > primary action > camera > lighting > environment > style > secondary detail > optional aesthetics`

## Prompt Budget
Use the shortest prompt that preserves all production-critical variables. Delete decorative prose that does not affect generation.

## Final Form
The compiler emits only the model-ready prompt plus essential settings. Internal schema, routing, scoring, and diagnostics remain hidden unless requested.
