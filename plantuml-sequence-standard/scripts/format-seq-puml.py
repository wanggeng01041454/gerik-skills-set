#!/usr/bin/env python3
import argparse
import pathlib
import re
import sys


RETURN_RE = re.compile(r"^return(\s|$)")
NOTE_RE = re.compile(r"^note(\s|$)")
GROUP_RE = re.compile(r"^group(\s|$)")
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


def is_outdent(line: str) -> bool:
    return line == "end" or line.startswith("end note") or bool(RETURN_RE.match(line))


def is_indent(line: str) -> bool:
    return bool(GROUP_RE.match(line) or NOTE_RE.match(line) or "->" in line)


def detect_non_sequence(lines: list[str]) -> tuple[int, str] | None:
    note_depth = 0
    for idx, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line or line.startswith("'"):
            continue
        if line.startswith("end note"):
            note_depth = max(0, note_depth - 1)
            continue
        if line.startswith("note"):
            note_depth += 1
            continue
        if note_depth > 0:
            continue
        for pattern, reason in NON_SEQUENCE_RULES:
            if pattern.match(line):
                return idx, reason
    return None


def format_lines(lines: list[str]) -> list[str]:
    level = 0
    out: list[str] = []

    for raw in lines:
        stripped = raw.lstrip().rstrip()
        if stripped == "":
            out.append("")
            continue

        if is_outdent(stripped):
            level = max(0, level - 1)

        out.append(("  " * level) + stripped)

        if is_indent(stripped):
            level += 1

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Format PlantUML sequence file(s) with strict 2-space indentation.")
    parser.add_argument("files", nargs="+", help="Target -seq.puml files")
    args = parser.parse_args()

    exit_code = 0
    for file_name in args.files:
        path = pathlib.Path(file_name)
        if not is_suffix_ok(path):
            print(f"[ERROR] Not a -seq.puml file: {path}", file=sys.stderr)
            exit_code = 2
            continue
        if not path.exists():
            print(f"[ERROR] File not found: {path}", file=sys.stderr)
            exit_code = 2
            continue

        original = path.read_text(encoding="utf-8").splitlines()
        non_seq = detect_non_sequence(original)
        if non_seq is not None:
            line_no, reason = non_seq
            print(
                f"[ERROR] Non-sequence syntax detected at {path}:{line_no} ({reason}); formatter applies only to sequence diagrams",
                file=sys.stderr,
            )
            exit_code = 2
            continue
        formatted = format_lines(original)
        path.write_text("\n".join(formatted) + "\n", encoding="utf-8")
        print(f"[OK] Formatted {path}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
