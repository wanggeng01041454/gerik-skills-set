---
name: plantuml-sequence-standard
description: Create, edit, and validate PlantUML sequence diagrams with strict standards. Applies only to files ending in -seq.puml; enforce 2-space indentation rules, colored groups, and one return for every -> message.
---

# PlantUML Sequence Standard

Use this skill when the task is about PlantUML **sequence diagrams**.

## Scope Guard (Hard Rule)

- This skill applies only to files ending with `-seq.puml`.
- Do not edit non-suffix `.puml` files with this workflow.
- If the requested file does not end with `-seq.puml`, create/rename to a compliant filename first.
- This skill is **not applicable** to non-sequence PlantUML diagrams:
  - swimlane/activity diagrams
  - state transition diagrams
  - other non-sequence diagram families
- If content indicates non-sequence syntax, stop this workflow and switch to a diagram-specific skill/process.

## Required Conventions

- Must be valid PlantUML sequence diagram text.
- Every `->` message must have one corresponding `return` line.
- Use details in `note` blocks.
- Group coloring syntax:
  - `group #<color> "标题"`
  - `end`
- Indentation is 2 spaces per level.

## Indentation Rules

- Indent keywords (increase for next line):
  - `group`
  - `note`, `note over`, `note left`
  - any line containing `->`
- Outdent keywords (decrease on current line):
  - `end` (paired with `group`)
  - `end note`
  - `return`

## Workflow

1. Confirm target file path ends with `-seq.puml`.
2. Create or edit the sequence diagram content.
3. Format the file:
   - `python3 scripts/format-seq-puml.py <file-seq.puml>`
4. Validate conventions:
   - `python3 scripts/validate-seq-puml.py <file-seq.puml>`
   - Validation rejects files that look like activity/swimlane/state diagrams.
5. Optional syntax check if PlantUML exists:
   - `plantuml -checkonly <file-seq.puml>`

## Scripts

- Formatter: `scripts/format-seq-puml.py`
- Validator: `scripts/validate-seq-puml.py`
