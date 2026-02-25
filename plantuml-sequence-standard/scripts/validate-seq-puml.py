#!/usr/bin/env python3
import argparse
import pathlib
import re
import sys


RETURN_RE = re.compile(r"^return(\s|$)")
GROUP_RE = re.compile(r'^group\s+#[A-Za-z0-9]+\s+"[^"]+"\s*$')
NOTE_RE = re.compile(r"^note(\s|$)")
PARTICIPANT_RE = re.compile(r"^(participant|actor|boundary|control|entity|database|queue|collections)\b")
NON_SEQUENCE_RULES = [
    (re.compile(r"^state\b"), "state diagram keyword 'state'"),
    (re.compile(r"^\[\*\]"), "state diagram marker '[*]'"),
    (re.compile(r"^partition\b"), "activity/swimlane keyword 'partition'"),
    (re.compile(r"^start$"), "activity keyword 'start'"),
    (re.compile(r"^stop$"), "activity keyword 'stop'"),
    (re.compile(r"^fork\b"), "activity keyword 'fork'"),
    (re.compile(r"^end\s+fork\b"), "activity keyword 'end fork'"),
    (re.compile(r"^\|.*\|$"), "swimlane syntax '|lane|'"),
]


def is_suffix_ok(path: pathlib.Path) -> bool:
    return path.name.endswith("-seq.puml")


def validate_file(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    has_start = False
    has_end = False
    has_participant = False
    arrow_count = 0
    return_count = 0

    group_stack: list[int] = []
    note_stack: list[int] = []

    for idx, raw in enumerate(lines, start=1):
        line = raw.strip()
        if line == "":
            continue
        if line.startswith("'"):
            continue

        if line.startswith("@startuml"):
            has_start = True
        if line == "@enduml":
            has_end = True

        if PARTICIPANT_RE.match(line):
            has_participant = True

        if line.startswith("group "):
            if not GROUP_RE.match(line):
                errors.append(
                    f"{path}:{idx}: group syntax must be: group #<color> \"标题\""
                )
            group_stack.append(idx)
            continue

        if line.startswith("end note"):
            if not note_stack:
                errors.append(f"{path}:{idx}: unexpected 'end note' without matching note")
            else:
                note_stack.pop()
            continue

        if line == "end":
            if not group_stack:
                errors.append(f"{path}:{idx}: unexpected 'end' without matching group")
            else:
                group_stack.pop()
            continue

        if NOTE_RE.match(line):
            note_stack.append(idx)
            continue

        if note_stack:
            continue

        for pattern, reason in NON_SEQUENCE_RULES:
            if pattern.match(line):
                errors.append(
                    f"{path}:{idx}: detected non-sequence syntax ({reason}); this skill applies only to sequence diagrams"
                )
                break

        if RETURN_RE.match(line):
            return_count += 1
            continue

        if "->" in line:
            arrow_count += line.count("->")

    if not has_start:
        errors.append(f"{path}: missing @startuml")
    if not has_end:
        errors.append(f"{path}: missing @enduml")
    if not has_participant:
        errors.append(f"{path}: no participant/actor declaration found")

    if group_stack:
        errors.append(f"{path}: unclosed group starting at line {group_stack[-1]}")
    if note_stack:
        errors.append(f"{path}: unclosed note starting at line {note_stack[-1]}")
    if arrow_count != return_count:
        errors.append(
            f"{path}: '->' count ({arrow_count}) does not match 'return' count ({return_count})"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PlantUML sequence diagram standards.")
    parser.add_argument("files", nargs="+", help="Target -seq.puml files")
    args = parser.parse_args()

    all_errors: list[str] = []
    for file_name in args.files:
        path = pathlib.Path(file_name)
        if not is_suffix_ok(path):
            all_errors.append(f"{path}: filename must end with -seq.puml")
            continue
        if not path.exists():
            all_errors.append(f"{path}: file does not exist")
            continue
        all_errors.extend(validate_file(path))

    if all_errors:
        for err in all_errors:
            print(f"[ERROR] {err}", file=sys.stderr)
        return 1

    for file_name in args.files:
        print(f"[OK] {file_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
