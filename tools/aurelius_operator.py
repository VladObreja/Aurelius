from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "protocol"


def load(name: str) -> Any:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def norm_phase(value: str) -> str:
    value = str(value).strip()
    if value.lower().startswith("phase "):
        value = value.split(" ", 1)[1]
    return value


def phase_aliases(value: str) -> set[str]:
    raw = norm_phase(value)
    aliases = {raw, f"Phase {raw}"}
    try:
        number = float(raw)
    except ValueError:
        return aliases
    aliases.add(str(int(number)) if number.is_integer() else str(number))
    aliases.add(f"{number:.1f}")
    aliases.add(f"Phase {number:.1f}")
    return aliases


def phase_label(value: str) -> str:
    return f"Phase {norm_phase(value)}"


def clean(text: Any) -> str:
    if text is None:
        return ""
    return re.sub(r"\s+", " ", str(text)).strip()


def rows_for_phase(rows: list[dict[str, Any]], phase: str) -> list[dict[str, Any]]:
    aliases = phase_aliases(phase)
    out = []
    for row in rows:
        row_phase = str(row.get("phase", "")).strip()
        if row_phase in aliases:
            out.append(row)
    return out


def cpo_for_phase(phase: str, tiers: set[str] | None = None) -> list[dict[str, Any]]:
    rows = rows_for_phase(load("cpo_entries.json"), phase)
    if tiers:
        rows = [row for row in rows if str(row.get("tier", "")).upper() in tiers]
    return rows


def daily_for_phase(phase: str) -> list[dict[str, Any]]:
    return rows_for_phase(load("daily_schedule.json"), phase)


def command_morning(args: argparse.Namespace) -> None:
    phase = norm_phase(args.phase)
    rows = daily_for_phase(phase)
    print(f"# {phase_label(phase)} Morning / First-Day Operator Plan\n")
    print("Assumption: use this as the default start if no current phase or destabilization context was provided.\n")

    wanted = {
        "On waking",
        "Binder window (fasted, mid-morning)",
        "Binder window (after psyllium)",
        "Post-binder meal (first meal)",
        "Lunch (with food)",
        "Dinner (with food)",
        "Bedtime (PM)",
        "Practices (today)",
        "Watch-for / STOP-ADJUST",
        "Advance when",
    }
    current = None
    for row in rows:
        block = clean(row.get("time_block"))
        if block not in wanted:
            continue
        if block != current:
            current = block
            print(f"## {block}\n")
        optional = " (optional)" if clean(row.get("optional")) else ""
        item = clean(row.get("what_to_do_take"))
        if item:
            print(f"- {item}{optional}")
        notes = clean(row.get("notes"))
        continuation = clean(row.get("continuation_maintenance"))
        if notes:
            print(f"  - Notes: {notes}")
        if continuation:
            print(f"  - Continuation: {continuation}")
        source = clean(row.get("source_ids"))
        if source:
            print(f"  - Source IDs: {source}")
        print()

    print("## Track Today\n")
    print("- sleep, energy, libido, EQ, mood, smell, digestion, skin/fungal signs, adverse effects")
    print("- Energy is primary: significant energy worsening should trigger review/rollback.\n")


def command_shopping(args: argparse.Namespace) -> None:
    phase = norm_phase(args.phase)
    tiers = {tier.upper() for tier in args.tiers}
    cpo = cpo_for_phase(phase, tiers)
    compounds = {row.get("canonical_id"): row for row in load("compounds.json")}

    print(f"# Shopping List - {phase_label(phase)} ({', '.join(sorted(tiers))})\n")
    print("Use this as a protocol-derived shopping aid, not as medical advice or a mandate to start everything at once.\n")

    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in cpo:
        cid = row.get("id") or row.get("canonical_id")
        meta = compounds.get(cid, {})
        category = clean(meta.get("category")) or "Uncategorized"
        grouped.setdefault(category, []).append(row)

    for category in sorted(grouped):
        print(f"## {category}\n")
        for row in grouped[category]:
            name = clean(row.get("compound"))
            cid = clean(row.get("id"))
            dose = clean(row.get("dosage"))
            timing = clean(row.get("timing"))
            freq = clean(row.get("frequency"))
            notes = clean(row.get("notes"))
            tier = clean(row.get("tier"))
            line = f"- {name}"
            if cid:
                line += f" [{cid}]"
            if dose:
                line += f" - {dose}"
            print(line)
            details = []
            if timing:
                details.append(f"Timing: {timing}")
            if freq:
                details.append(f"Frequency: {freq}")
            if tier:
                details.append(f"Tier: {tier}")
            if details:
                print(f"  - {' | '.join(details)}")
            if notes:
                print(f"  - Notes: {notes}")
        print()

    print("## Non-Supplement Prep\n")
    if phase == "1.0":
        print("- Carrot salad ingredients if using CAS-FOOD-01.")
        print("- Large glass / water bottle for hydration and psyllium.")
        print("- Calendar/reminder slots for binder separation and evening practices.")
    print("- Do not treat the research archive as a shopping list; gated or experimental items need HIRA/review first.\n")


def command_phase(args: argparse.Namespace) -> None:
    phase = norm_phase(args.phase)
    cpo = cpo_for_phase(phase)
    print(f"# {phase_label(phase)} Summary\n")
    for tier in ("CORE", "SUPPORT", "EXPERIMENT"):
        rows = [row for row in cpo if clean(row.get("tier")).upper() == tier]
        if not rows:
            continue
        print(f"## {tier}\n")
        for row in rows:
            name = clean(row.get("compound"))
            cid = clean(row.get("id"))
            dose = clean(row.get("dosage"))
            stop = clean(row.get("stop_taper_trigger"))
            line = f"- {name}"
            if cid:
                line += f" [{cid}]"
            if dose:
                line += f" - {dose}"
            print(line)
            if stop:
                print(f"  - Exit: {stop}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Aurelius protocol operator helper")
    sub = parser.add_subparsers(dest="command", required=True)

    morning = sub.add_parser("morning", help="Print an operator morning/first-day plan")
    morning.add_argument("--phase", default="1.0")
    morning.set_defaults(func=command_morning)

    shopping = sub.add_parser("shopping", help="Print a protocol-derived shopping list")
    shopping.add_argument("--phase", default="1.0")
    shopping.add_argument("--tiers", nargs="+", default=["CORE"])
    shopping.set_defaults(func=command_shopping)

    phase = sub.add_parser("phase", help="Summarize phase CPO entries by tier")
    phase.add_argument("--phase", default="1.0")
    phase.set_defaults(func=command_phase)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
