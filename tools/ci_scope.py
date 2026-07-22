#!/usr/bin/env python3
"""Classify repository changes for the research-integrity workflow."""

from __future__ import annotations

import argparse
import subprocess
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "tools/research_manifest.toml"
MATH_DIRECTORIES = {"active", "barriers", "results"}
FULL_VERIFIER_INPUTS = {
    ".github/workflows/research-integrity.yml",
    "tools/ci_scope.py",
    "tools/requirements-verifiers.txt",
    "tools/research_index.py",
}


@dataclass(frozen=True)
class Scope:
    run_tool_tests: bool
    verifier_mode: str
    verifier_ids: tuple[str, ...] = ()
    reasons: tuple[str, ...] = ()


def verifier_records(manifest: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {record["id"]: record for record in manifest.get("verifiers", [])}


def classify_changes(
    event: str,
    changed_paths: set[str],
    current_manifest: Mapping[str, Any],
    base_manifest: Mapping[str, Any] | None,
) -> Scope:
    run_tool_tests = any(
        path.startswith("tools/") or path.startswith(".github/workflows/")
        for path in changed_paths
    )

    if event in {"schedule", "workflow_dispatch"}:
        return Scope(run_tool_tests, "full", reasons=(f"{event} full run",))
    if event not in {"pull_request", "push"}:
        return Scope(True, "full", reasons=(f"unknown event {event!r}",))
    if base_manifest is None:
        return Scope(True, "full", reasons=("base manifest unavailable",))

    current = verifier_records(current_manifest)
    base = verifier_records(base_manifest)
    current_paths = {record["path"]: verifier_id for verifier_id, record in current.items()}
    base_paths = {record["path"]: verifier_id for verifier_id, record in base.items()}
    selected: set[str] = set()
    full_reasons: set[str] = set()

    for path in sorted(changed_paths):
        if path in FULL_VERIFIER_INPUTS:
            full_reasons.add(path)
            continue
        if path in current_paths:
            selected.add(current_paths[path])
            continue
        if path in base_paths:
            full_reasons.add(f"removed or renamed verifier path {path}")
            continue
        parts = Path(path).parts
        if parts and parts[0] in MATH_DIRECTORIES and Path(path).suffix.lower() != ".md":
            full_reasons.add(f"unregistered mathematical dependency {path}")

    removed_ids = set(base) - set(current)
    if removed_ids:
        full_reasons.add(
            "removed verifier record(s): " + ", ".join(sorted(removed_ids))
        )
    for verifier_id in set(current) - set(base):
        selected.add(verifier_id)
    for verifier_id in set(current) & set(base):
        if current[verifier_id] != base[verifier_id]:
            selected.add(verifier_id)

    if full_reasons:
        return Scope(
            run_tool_tests,
            "full",
            reasons=tuple(sorted(full_reasons)),
        )
    if selected:
        return Scope(
            run_tool_tests,
            "selected",
            verifier_ids=tuple(sorted(selected)),
            reasons=("changed verifier records or scripts",),
        )
    return Scope(run_tool_tests, "none", reasons=("no verifier inputs changed",))


def run_git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(detail or f"git {' '.join(args)} failed")
    return result.stdout


def read_manifest(root: Path, ref: str | None = None) -> Mapping[str, Any]:
    if ref is None:
        data = (root / MANIFEST).read_bytes()
    else:
        data = run_git(root, "show", f"{ref}:{MANIFEST}")
    return tomllib.loads(data.decode("utf-8"))


def changed_paths(root: Path, event: str, base: str) -> set[str]:
    separator = "..." if event == "pull_request" else ".."
    data = run_git(root, "diff", "--name-only", "-z", f"{base}{separator}HEAD")
    return {
        path.decode("utf-8", errors="strict")
        for path in data.split(b"\0")
        if path
    }


def determine_scope(root: Path, event: str, base: str | None) -> Scope:
    current = read_manifest(root)
    if event in {"schedule", "workflow_dispatch"}:
        return classify_changes(event, set(), current, current)
    if not base or set(base) == {"0"}:
        return classify_changes(event, set(), current, None)
    try:
        run_git(root, "rev-parse", "--verify", f"{base}^{{commit}}")
        base_manifest = read_manifest(root, base)
        paths = changed_paths(root, event, base)
    except (RuntimeError, tomllib.TOMLDecodeError, UnicodeDecodeError):
        return classify_changes(event, set(), current, None)
    return classify_changes(event, paths, current, base_manifest)


def write_selection(path: Path, verifier_ids: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(f"{verifier_id}\n" for verifier_id in verifier_ids)
    path.write_text(content, encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", required=True)
    parser.add_argument("--base")
    parser.add_argument("--selection-file", type=Path, required=True)
    args = parser.parse_args(argv)

    scope = determine_scope(ROOT, args.event, args.base)
    write_selection(args.selection_file, scope.verifier_ids)
    print(f"run_tool_tests={'true' if scope.run_tool_tests else 'false'}")
    print(f"verifier_mode={scope.verifier_mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
