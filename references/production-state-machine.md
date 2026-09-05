# Production State Machine — AI Film Studio v1.1

## الحالة الرئيسية
```text
M0 → M1 → M2 → M3 → M4 → M5 → APPROVAL → M6 → M7 → M8 → M9 → M10 → M11 → M12 → M13
                                      │
                                      └─ REJECT → M1/M2/M3/M4/M5 حسب سبب الرفض

M6–M12: أي FAIL → DIAGNOSE → REPAIR → REVALIDATE → PASS
```

## Gates
| Gate | شرط PASS | إذا فشل |
|---|---|---|
| G0 Intake | brief complete | M0 |
| G1 Concept | concept + visual DNA locked | M1 |
| G2 Identity/World | character/world bible approved | M2 |
| G3 Script | script/dialogue/performance locked | M3 |
| G4 Architecture | production plan, risks, versions defined | M4 |
| G5 Shot Plan | every shot has purpose, start/end, dependencies | M5 |
| G-APPROVAL | user explicitly approves M0–M5 | return to relevant stage |
| G6 Assets | approved frames/assets + identity lock | M6 repair |
| G7 Motion | choreography + fallback validated | M7 repair |
| G8 Video | generated clips linked to source assets | M8 repair |
| G9 Dialogue | script/audio/timing/lipsync validated | M9 repair |
| G10 Composite | external text/VFX layers editable and timed | M10 repair |
| G11 QC | all shots PASS, no unresolved HOLD | M11 repair |
| G12 Master | picture/sound/color locked | M12 repair |
| G13 Delivery | delivery manifest complete | M13 |

## Approval rule
The only mandatory human production approval before expensive generation is after M5. Additional approvals may be requested for brand/legal/high-risk decisions.

## Transition record
Every transition records: `from`, `to`, `timestamp`, `reason`, `operator`, `artifacts`, `approval_id`, `state_version`.
