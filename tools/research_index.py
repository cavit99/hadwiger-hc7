#!/usr/bin/env python3
"""Build and validate the disposable HC7 research index.

The Markdown repository remains authoritative.  This program indexes only
Git-tracked documents and uses a small curated manifest for the live proof
spine.  It deliberately does not infer mathematical dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import time
import tomllib
import urllib.parse
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "tools" / "research_manifest.toml"
DEFAULT_DATABASE = ROOT / ".cache" / "research" / "index.sqlite"
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".sh",
    ".bash",
    ".zsh",
    ".fish",
    ".ps1",
    ".toml",
    ".yml",
    ".yaml",
    ".json",
    ".txt",
    ".tex",
    ".rst",
    ".ini",
    ".cfg",
}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "ftp", "data"}
PROOF_RELATIONS = {"uses"}
ALLOWED_RELATIONS = PROOF_RELATIONS | {
    "strengthens",
    "specializes",
    "subproblem_of",
    "supersedes",
    "contradicts",
    "refuted_by",
    "sharpness_witness",
    "external_input",
    "related_to",
    "guarded_by",
}
ALLOWED_KINDS = {"theorem", "lemma", "target", "barrier", "laboratory"}
ALLOWED_STATUSES = {
    "audited-green",
    "active-target",
    "written-unaudited",
    "barrier",
    "frozen",
    "superseded",
    "refuted",
}
CLAIM_KEYS = {
    "id",
    "title",
    "kind",
    "status",
    "source",
    "source_heading",
    "active",
    "scope",
    "label_fidelity",
    "separator_order",
    "colour_compatibility",
    "strict_parameter",
    "audit",
    "expected_source_sha256",
    "hypotheses",
    "conclusions",
    "preserves",
    "does_not_prove",
    "allowed_exits",
    "keywords",
    "satisfies",
    "lacks",
    "refutes",
}
LIST_ATTRIBUTES = {
    "hypotheses",
    "conclusions",
    "preserves",
    "does_not_prove",
    "allowed_exits",
    "keywords",
    "satisfies",
    "lacks",
    "refutes",
}
DEVICE_PATH_PATTERNS = (
    re.compile(r"(?<![\w.])/" + r"Users/[A-Za-z0-9._-]+/"),
    re.compile(r"(?<![\w.])/" + r"home/[A-Za-z0-9._-]+/"),
    re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+\\"),
    re.compile(r"(?i)\bfile:" + r"//"),
)
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\((<[^>]+>|[^)\s]+(?:\s+['\"][^'\"]*['\"])?)[)]")
REFERENCE_LINK_RE = re.compile(
    r"(?m)^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)(?:\s+['\"(].*)?$"
)
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
AUTHORED_ROOTS = {"active", "results", "barriers", "archive", "tools"}
AUTHORED_SUFFIXES = {
    ".md",
    ".py",
    ".sh",
    ".bash",
    ".zsh",
    ".fish",
    ".ps1",
    ".toml",
    ".yml",
    ".yaml",
    ".json",
    ".txt",
    ".tex",
    ".rst",
    ".ini",
    ".cfg",
}
AUTHORED_PATH_RE = re.compile(
    r"(?<![\w./-])"
    r"(?P<path>(?:(?:\.\.?/)+)?(?:active|results|barriers|archive|tools)/"
    r"[A-Za-z0-9_.@+%/-]+?"
    r"(?:\.md|\.py|\.sh|\.bash|\.zsh|\.fish|\.ps1|\.toml|\.ya?ml|"
    r"\.json|\.txt|\.tex|\.rst|\.ini|\.cfg))"
    r"(?:#[A-Za-z0-9_.%-]+)?"
)
INLINE_MATH_RE = re.compile(
    r"(?<!\\)\$\$.*?(?<!\\)\$\$|"
    r"\\\[.*?\\\]|"
    r"(?<!\\)\$(?!\$).*?(?<!\\)\$|"
    r"\\\(.*?\\\)"
)
MATH_FENCE_RE = re.compile(r"^\s*(\$\$|\\\[|\\\])\s*$")


class IntegrityError(RuntimeError):
    """Raised when repository metadata or proof-spine integrity fails."""


@dataclass(frozen=True)
class Section:
    ordinal: int
    level: int
    heading: str
    slug: str
    start_line: int
    end_line: int
    body: str


@dataclass(frozen=True)
class MarkdownLink:
    line: int
    label: str
    raw_target: str
    resolved_path: str | None
    fragment: str
    kind: str
    valid: bool
    error: str


@dataclass(frozen=True)
class AuthoredArtifactReference:
    line: int
    raw_target: str
    resolved_path: str | None
    valid: bool
    error: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, capture_output=True
    )
    if result.returncode:
        raise IntegrityError(
            f"git {' '.join(args)} failed: {result.stderr.decode(errors='replace').strip()}"
        )
    return result.stdout


def tracked_paths(root: Path) -> tuple[str, ...]:
    raw = run_git(root, "ls-files", "-z")
    return tuple(sorted(item.decode() for item in raw.split(b"\0") if item))


def git_head(root: Path) -> str:
    return run_git(root, "rev-parse", "HEAD").decode().strip()


def corpus_signature(root: Path, manifest_path: Path, tracked: Sequence[str] | None = None) -> str:
    """Hash the exact tracked Markdown corpus plus the curated manifest."""
    paths = tracked if tracked is not None else tracked_paths(root)
    digest = hashlib.sha256()
    digest.update(b"research-index-schema-1\0")
    digest.update(manifest_path.read_bytes())
    digest.update(b"\0")
    for relative in paths:
        if not relative.endswith(".md"):
            continue
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update((root / relative).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    with path.open("rb") as stream:
        return tomllib.load(stream)


def mask_fences(text: str) -> list[str]:
    masked: list[str] = []
    active: str | None = None
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)[0]
            if active is None:
                active = marker
            elif marker == active:
                active = None
            masked.append("")
        elif active is None:
            masked.append(line)
        else:
            masked.append("")
    return masked


def mask_fences_and_math(text: str) -> list[str]:
    """Mask fenced code and TeX-style math while preserving line numbers.

    Inline code is deliberately retained because repository paths written in
    backticks are authored-artifact references.  Conventional Markdown links
    are retained for the same reason.
    """
    masked: list[str] = []
    code_fence: str | None = None
    math_fence: str | None = None
    for line in text.splitlines():
        code_match = FENCE_RE.match(line)
        if code_match and math_fence is None:
            marker = code_match.group(1)[0]
            if code_fence is None:
                code_fence = marker
            elif marker == code_fence:
                code_fence = None
            masked.append("")
            continue
        if code_fence is not None:
            masked.append("")
            continue

        math_match = MATH_FENCE_RE.match(line)
        if math_match:
            marker = math_match.group(1)
            if math_fence is None and marker in {"$$", r"\["}:
                math_fence = marker
            elif math_fence == "$$" and marker == "$$":
                math_fence = None
            elif math_fence == r"\[" and marker == r"\]":
                math_fence = None
            masked.append("")
            continue
        if math_fence is not None:
            masked.append("")
            continue

        masked.append(INLINE_MATH_RE.sub("", line))
    return masked


def github_slug(heading: str) -> str:
    value = re.sub(r"<[^>]*>", "", html.unescape(heading)).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def extract_sections(text: str) -> list[Section]:
    lines = text.splitlines()
    masked = mask_fences(text)
    headings: list[tuple[int, int, str, str]] = []
    slug_counts: defaultdict[str, int] = defaultdict(int)
    for index, line in enumerate(masked, start=1):
        match = HEADING_RE.match(line)
        if not match:
            continue
        heading = match.group(2).strip()
        base = github_slug(heading)
        count = slug_counts[base]
        slug_counts[base] += 1
        slug = base if count == 0 else f"{base}-{count}"
        headings.append((index, len(match.group(1)), heading, slug))

    starts = [(1, 0, "", "")] if not headings or headings[0][0] > 1 else []
    starts.extend(headings)
    sections: list[Section] = []
    for ordinal, (start, level, heading, slug) in enumerate(starts):
        end = (starts[ordinal + 1][0] - 1) if ordinal + 1 < len(starts) else len(lines)
        body = "\n".join(lines[start - 1 : end])
        sections.append(Section(ordinal, level, heading, slug, start, end, body))
    return sections


def _clean_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    else:
        target = re.sub(r"\s+(['\"]).*\1$", "", target)
    return urllib.parse.unquote(target)


def _inside_repo(root: Path, path: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def extract_links(
    root: Path,
    source_relative: str,
    text: str,
    tracked: set[str],
    anchors: dict[str, set[str]],
) -> list[MarkdownLink]:
    links: list[MarkdownLink] = []
    masked_text = "\n".join(mask_fences(text))
    for match in LINK_RE.finditer(masked_text):
        line_number = masked_text.count("\n", 0, match.start()) + 1
        label, raw = re.sub(r"\s+", " ", match.group(1)).strip(), match.group(2)
        target = _clean_link_target(raw)
        parsed = urllib.parse.urlsplit(target)
        if parsed.scheme.lower() in EXTERNAL_SCHEMES or target.startswith("//"):
            links.append(MarkdownLink(line_number, label, target, None, "", "external", True, ""))
            continue
        if parsed.scheme:
            links.append(MarkdownLink(line_number, label, target, None, parsed.fragment, "external", True, ""))
            continue
        path_part = parsed.path
        fragment = parsed.fragment
        if not path_part:
            resolved = source_relative
        else:
            candidate = (root / Path(source_relative).parent / path_part).resolve()
            if not _inside_repo(root, candidate):
                links.append(MarkdownLink(line_number, label, target, None, fragment, "local", False, "target escapes repository"))
                continue
            resolved = candidate.relative_to(root.resolve()).as_posix()
        candidate_path = root / resolved
        if resolved in tracked:
            valid = True
            error = ""
        elif candidate_path.is_dir() and any(p.startswith(resolved.rstrip("/") + "/") for p in tracked):
            valid = True
            error = ""
        else:
            valid = False
            error = "target is missing or untracked"
        if valid and fragment and resolved.endswith(".md"):
            if github_slug(fragment) not in anchors.get(resolved, set()) and fragment not in anchors.get(resolved, set()):
                valid = False
                error = f"unknown fragment #{fragment}"
        links.append(MarkdownLink(line_number, label, target, resolved, fragment, "local", valid, error))
    return links


def _resolve_authored_artifact(
    root: Path,
    source_relative: str,
    raw_target: str,
    tracked: set[str],
) -> AuthoredArtifactReference | None:
    """Resolve a path which names one of the repository's authored areas."""
    target = urllib.parse.unquote(raw_target).split("#", 1)[0]
    path = PurePosixPath(target)
    if not path.parts:
        return None

    if path.parts[0] in AUTHORED_ROOTS:
        candidate = root / path
    else:
        candidate = root / PurePosixPath(source_relative).parent / path
    if not _inside_repo(root, candidate):
        return AuthoredArtifactReference(
            0, raw_target, None, False, "target escapes repository"
        )

    resolved = candidate.resolve().relative_to(root.resolve()).as_posix()
    resolved_parts = PurePosixPath(resolved).parts
    if not resolved_parts or resolved_parts[0] not in AUTHORED_ROOTS:
        return None
    if PurePosixPath(resolved).suffix.lower() not in AUTHORED_SUFFIXES:
        return None
    if resolved in tracked:
        return AuthoredArtifactReference(0, raw_target, resolved, True, "")
    return AuthoredArtifactReference(
        0,
        raw_target,
        resolved,
        False,
        "authored artifact is missing or untracked",
    )


def extract_authored_artifact_references(
    root: Path,
    source_relative: str,
    text: str,
    tracked: set[str],
) -> list[AuthoredArtifactReference]:
    """Extract authored-artifact paths from links, inline code, and prose.

    Conventional Markdown links may use same-directory paths.  Plain prose
    and inline-code references must name an authored root explicitly (for
    example ``barriers/example.md`` or ``../results/theorem.md``).
    Fenced code and TeX-style math are excluded from both scans.
    """
    masked_text = "\n".join(mask_fences_and_math(text))
    found: dict[tuple[int, str], AuthoredArtifactReference] = {}

    if source_relative.endswith(".md"):
        for pattern, target_group in ((LINK_RE, 2), (REFERENCE_LINK_RE, 1)):
            for match in pattern.finditer(masked_text):
                target = _clean_link_target(match.group(target_group))
                parsed = urllib.parse.urlsplit(target)
                if parsed.scheme or target.startswith("//") or not parsed.path:
                    continue
                reference = _resolve_authored_artifact(
                    root, source_relative, parsed.path, tracked
                )
                if reference is None:
                    continue
                line = masked_text.count("\n", 0, match.start()) + 1
                found[(line, reference.resolved_path or reference.raw_target)] = (
                    AuthoredArtifactReference(
                        line,
                        target,
                        reference.resolved_path,
                        reference.valid,
                        reference.error,
                    )
                )

    for match in AUTHORED_PATH_RE.finditer(masked_text):
        raw_target = match.group("path")
        reference = _resolve_authored_artifact(
            root, source_relative, raw_target, tracked
        )
        if reference is None:
            continue
        line = masked_text.count("\n", 0, match.start()) + 1
        key = (line, reference.resolved_path or reference.raw_target)
        found.setdefault(
            key,
            AuthoredArtifactReference(
                line,
                raw_target,
                reference.resolved_path,
                reference.valid,
                reference.error,
            ),
        )

    return sorted(found.values(), key=lambda item: (item.line, item.raw_target))


def _relative_path(value: str, field: str) -> None:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise IntegrityError(f"{field} must be a repository-relative path: {value}")


def _opening_verdict(audit_text: str) -> str:
    lines = audit_text.splitlines()[:80]
    candidates = [line for line in lines if re.search(r"\bverdict\b", line, re.I)]
    if not candidates:
        return ""
    first = lines.index(candidates[0])
    return "\n".join(lines[first : min(len(lines), first + 8)]).upper()


def _proof_cycle(claims: dict[str, dict], relations: Sequence[dict]) -> list[str] | None:
    edges: defaultdict[str, list[str]] = defaultdict(list)
    indegree = {claim_id: 0 for claim_id in claims}
    for relation in relations:
        if relation["kind"] not in PROOF_RELATIONS:
            continue
        source, target = relation["source"], relation["target"]
        edges[target].append(source)  # dependency -> consumer
        indegree[source] += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    seen: list[str] = []
    while queue:
        node = queue.popleft()
        seen.append(node)
        for neighbour in sorted(edges[node]):
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    if len(seen) == len(claims):
        return None
    return sorted(node for node, degree in indegree.items() if degree > 0)


def validate_repository(root: Path = ROOT, manifest_path: Path = MANIFEST_PATH) -> list[str]:
    errors: list[str] = []
    manifest = load_manifest(manifest_path)
    tracked_tuple = tracked_paths(root)
    tracked = set(tracked_tuple)
    required_top = {"schema_version", "project", "required_text", "claims", "relations", "verifiers"}
    unknown_top = set(manifest) - required_top
    if unknown_top:
        errors.append(f"manifest has unknown top-level keys: {sorted(unknown_top)}")
    if manifest.get("schema_version") != 1:
        errors.append("manifest schema_version must be 1")

    project = manifest.get("project", {})
    for key in ("status_authority", "navigation_root", "public_overview", "database"):
        if key not in project:
            errors.append(f"manifest project.{key} is required")
    if project.get("status_authority") != "RESEARCH_LEDGER.md":
        errors.append("manifest project.status_authority must remain RESEARCH_LEDGER.md")
    if project.get("navigation_root") != "active/INDEX.md":
        errors.append("manifest project.navigation_root must remain active/INDEX.md")
    if project.get("public_overview") != "README.md":
        errors.append("manifest project.public_overview must remain README.md")

    claims: dict[str, dict] = {}
    for claim in manifest.get("claims", []):
        unknown = set(claim) - CLAIM_KEYS
        if unknown:
            errors.append(f"claim {claim.get('id', '<missing>')} has unknown keys: {sorted(unknown)}")
        missing = {"id", "title", "kind", "status", "source", "active"} - set(claim)
        if missing:
            errors.append(f"claim {claim.get('id', '<missing>')} lacks {sorted(missing)}")
            continue
        claim_id = claim["id"]
        if claim_id in claims:
            errors.append(f"duplicate claim id: {claim_id}")
            continue
        claims[claim_id] = claim
        if claim["kind"] not in ALLOWED_KINDS:
            errors.append(f"claim {claim_id} has invalid kind {claim['kind']!r}")
        if claim["status"] not in ALLOWED_STATUSES:
            errors.append(f"claim {claim_id} has invalid status {claim['status']!r}")
        for key in LIST_ATTRIBUTES:
            if key in claim and not isinstance(claim[key], list):
                errors.append(f"claim {claim_id}.{key} must be a list")
        for key in ("source", "audit"):
            if key not in claim:
                continue
            value = claim[key]
            try:
                _relative_path(value, f"claim {claim_id}.{key}")
            except IntegrityError as exc:
                errors.append(str(exc))
                continue
            if value not in tracked:
                errors.append(f"claim {claim_id}.{key} is missing or untracked: {value}")
        source = claim["source"]
        if source in tracked and claim.get("source_heading"):
            source_text = (root / source).read_text(encoding="utf-8", errors="replace")
            headings = {section.heading for section in extract_sections(source_text) if section.heading}
            if claim["source_heading"] not in headings:
                errors.append(
                    f"claim {claim_id} source_heading is absent from {source}: {claim['source_heading']!r}"
                )
        if source in tracked and claim.get("expected_source_sha256"):
            actual = sha256_file(root / source)
            if actual != claim["expected_source_sha256"]:
                errors.append(f"claim {claim_id} source hash drift: expected {claim['expected_source_sha256']}, got {actual}")
        if claim["status"] == "audited-green":
            audit = claim.get("audit")
            expected = claim.get("expected_source_sha256")
            if not audit or not expected:
                errors.append(f"audited-green claim {claim_id} requires audit and expected_source_sha256")
            elif audit in tracked:
                audit_text = (root / audit).read_text(encoding="utf-8")
                if expected not in audit_text:
                    errors.append(f"audit {audit} does not contain exact source hash for {claim_id}")
                verdict = _opening_verdict(audit_text)
                if "GREEN" not in verdict or re.search(r"\bRED\b", verdict):
                    errors.append(f"audit {audit} lacks an unambiguous opening GREEN verdict")

    relations = manifest.get("relations", [])
    for relation in relations:
        unknown = set(relation) - {"source", "target", "kind", "note"}
        if unknown:
            errors.append(f"relation has unknown keys: {sorted(unknown)}")
        if not {"source", "target", "kind"} <= set(relation):
            errors.append(f"relation lacks required fields: {relation}")
            continue
        source, target, kind = relation["source"], relation["target"], relation["kind"]
        if source not in claims or target not in claims:
            errors.append(f"relation {source} -[{kind}]-> {target} has unknown endpoint")
            continue
        if source == target:
            errors.append(f"self relation is not allowed: {source} -[{kind}]-> itself")
        if kind not in ALLOWED_RELATIONS:
            errors.append(f"relation {source}->{target} has invalid kind {kind!r}")
        if kind == "uses" and claims[target]["status"] != "audited-green":
            errors.append(
                f"proved dependency {target} must be audited-green, not {claims[target]['status']}"
            )
    cycle = _proof_cycle(claims, relations)
    if cycle:
        errors.append(f"proof-dependency cycle among: {', '.join(cycle)}")

    markdown = [path for path in tracked_tuple if path.endswith(".md")]
    anchors: dict[str, set[str]] = {}
    for path in markdown:
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        anchors[path] = {section.slug for section in extract_sections(text) if section.slug}

    strict_documents = {
        project.get("public_overview", "README.md"),
        project.get("status_authority", "RESEARCH_LEDGER.md"),
        project.get("navigation_root", "active/INDEX.md"),
    }
    for claim in claims.values():
        strict_documents.add(claim["source"])
        if claim.get("audit"):
            strict_documents.add(claim["audit"])
    for path in sorted(strict_documents):
        if path not in tracked or not path.endswith(".md"):
            continue
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        for link in extract_links(root, path, text, tracked, anchors):
            if not link.valid:
                errors.append(f"{path}:{link.line}: broken link {link.raw_target!r}: {link.error}")

    navigation = project.get("navigation_root", "active/INDEX.md")
    if navigation in tracked:
        navigation_text = (root / navigation).read_text(encoding="utf-8")
        navigation_links = extract_links(root, navigation, navigation_text, tracked, anchors)
        linked = {link.resolved_path for link in navigation_links if link.valid and link.resolved_path}
        for claim_id, claim in claims.items():
            if claim["active"] and claim["source"] not in linked and claim["source"] != navigation:
                errors.append(f"active claim {claim_id} is not directly reachable from {navigation}")
        for link in navigation_links:
            source = link.resolved_path
            if not source or not source.startswith("results/") or source.endswith("_audit.md"):
                continue
            theorem = root / source
            audit_relative = theorem.with_name(theorem.stem + "_audit.md").relative_to(root).as_posix()
            if audit_relative not in tracked:
                errors.append(f"active proved input {source} lacks tracked adjacent audit {audit_relative}")
                continue
            actual_hash = sha256_file(theorem)
            audit_text = (root / audit_relative).read_text(encoding="utf-8")
            if actual_hash not in audit_text:
                errors.append(f"active proved input audit {audit_relative} lacks current source hash {actual_hash}")
            verdict = _opening_verdict(audit_text)
            if "GREEN" not in verdict or re.search(r"\bRED\b", verdict):
                errors.append(f"active proved input audit {audit_relative} lacks an unambiguous opening GREEN verdict")

    for required in manifest.get("required_text", []):
        if set(required) != {"file", "pattern"}:
            errors.append(f"required_text entry must contain only file and pattern: {required}")
            continue
        path = required["file"]
        if path not in tracked:
            errors.append(f"required_text file is missing or untracked: {path}")
            continue
        text = (root / path).read_text(encoding="utf-8")
        if not re.search(required["pattern"], text, re.I | re.S):
            errors.append(f"{path} does not retain required status phrase /{required['pattern']}/")

    for path in tracked_tuple:
        if (root / path).suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        if path.endswith(".md"):
            for reference in extract_authored_artifact_references(
                root, path, text, tracked
            ):
                if not reference.valid:
                    errors.append(
                        f"{path}:{reference.line}: authored artifact reference "
                        f"{reference.raw_target!r}: {reference.error}"
                    )
        for pattern in DEVICE_PATH_PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path}:{line}: device-specific path {match.group(0)!r}")

    for verifier in manifest.get("verifiers", []):
        unknown = set(verifier) - {"id", "path", "sha256", "timeout", "expected_stdout", "requires"}
        if unknown:
            errors.append(f"verifier {verifier.get('id', '<missing>')} has unknown keys: {sorted(unknown)}")
        missing = {"id", "path", "sha256", "timeout", "expected_stdout"} - set(verifier)
        if missing:
            errors.append(f"verifier {verifier.get('id', '<missing>')} lacks {sorted(missing)}")
            continue
        path = verifier["path"]
        try:
            _relative_path(path, f"verifier {verifier['id']}.path")
        except IntegrityError as exc:
            errors.append(str(exc))
            continue
        if path not in tracked:
            errors.append(f"verifier {verifier['id']} is missing or untracked: {path}")
        elif sha256_file(root / path) != verifier["sha256"]:
            errors.append(f"verifier {verifier['id']} hash drift")
        if not isinstance(verifier["timeout"], int) or verifier["timeout"] <= 0:
            errors.append(f"verifier {verifier['id']} timeout must be a positive integer")
        if not isinstance(verifier["expected_stdout"], list):
            errors.append(f"verifier {verifier['id']} expected_stdout must be a list")
    return errors


def _document_area(path: str) -> str:
    first = PurePosixPath(path).parts[0]
    return first if first in {"active", "results", "barriers", "archive"} else "root"


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE documents(
  id INTEGER PRIMARY KEY, path TEXT UNIQUE NOT NULL, area TEXT NOT NULL,
  title TEXT, sha256 TEXT NOT NULL, line_count INTEGER NOT NULL,
  byte_count INTEGER NOT NULL
);
CREATE TABLE sections(
  id INTEGER PRIMARY KEY, document_id INTEGER NOT NULL REFERENCES documents(id),
  ordinal INTEGER NOT NULL, level INTEGER NOT NULL, heading TEXT,
  slug TEXT, start_line INTEGER NOT NULL, end_line INTEGER NOT NULL, body TEXT NOT NULL
);
CREATE VIRTUAL TABLE sections_fts USING fts5(
  section_id UNINDEXED, path UNINDEXED, heading, body, tokenize='unicode61'
);
CREATE TABLE links(
  id INTEGER PRIMARY KEY, document_id INTEGER NOT NULL REFERENCES documents(id),
  line INTEGER NOT NULL, label TEXT, raw_target TEXT NOT NULL, kind TEXT NOT NULL,
  resolved_path TEXT, fragment TEXT, valid INTEGER NOT NULL, error TEXT
);
CREATE TABLE claims(
  id TEXT PRIMARY KEY, title TEXT NOT NULL, kind TEXT NOT NULL, status TEXT NOT NULL,
  source_path TEXT NOT NULL, source_heading TEXT, active INTEGER NOT NULL,
  scope TEXT, label_fidelity TEXT, separator_order TEXT, colour_compatibility TEXT,
  strict_parameter TEXT, audit_path TEXT, expected_source_sha256 TEXT
);
CREATE TABLE claim_attributes(
  claim_id TEXT NOT NULL REFERENCES claims(id), category TEXT NOT NULL, value TEXT NOT NULL
);
CREATE TABLE relations(
  source_id TEXT NOT NULL REFERENCES claims(id), target_id TEXT NOT NULL REFERENCES claims(id),
  kind TEXT NOT NULL, note TEXT
);
CREATE TABLE verifiers(
  id TEXT PRIMARY KEY, path TEXT NOT NULL, expected_sha256 TEXT NOT NULL,
  timeout_seconds INTEGER NOT NULL
);
"""


def build_index(
    root: Path = ROOT,
    manifest_path: Path = MANIFEST_PATH,
    output: Path = DEFAULT_DATABASE,
) -> Path:
    errors = validate_repository(root, manifest_path)
    if errors:
        raise IntegrityError("cannot build invalid index:\n- " + "\n- ".join(errors))
    manifest = load_manifest(manifest_path)
    tracked_tuple = tracked_paths(root)
    tracked = set(tracked_tuple)
    markdown = [path for path in tracked_tuple if path.endswith(".md")]
    anchors = {
        path: {section.slug for section in extract_sections((root / path).read_text(encoding="utf-8", errors="replace")) if section.slug}
        for path in markdown
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    connection = sqlite3.connect(temporary)
    try:
        connection.executescript(SCHEMA)
        connection.executemany(
            "INSERT INTO meta(key,value) VALUES(?,?)",
            [
                ("schema_version", "1"),
                ("git_head", git_head(root)),
                ("corpus_signature", corpus_signature(root, manifest_path, tracked_tuple)),
                ("status_authority", manifest["project"]["status_authority"]),
            ],
        )
        for path in markdown:
            raw = (root / path).read_bytes()
            text = raw.decode("utf-8", errors="replace")
            sections = extract_sections(text)
            title = next((section.heading for section in sections if section.level == 1), "")
            cursor = connection.execute(
                "INSERT INTO documents(path,area,title,sha256,line_count,byte_count) VALUES(?,?,?,?,?,?)",
                (path, _document_area(path), title, hashlib.sha256(raw).hexdigest(), len(text.splitlines()), len(raw)),
            )
            document_id = cursor.lastrowid
            for section in sections:
                section_cursor = connection.execute(
                    "INSERT INTO sections(document_id,ordinal,level,heading,slug,start_line,end_line,body) VALUES(?,?,?,?,?,?,?,?)",
                    (document_id, section.ordinal, section.level, section.heading, section.slug, section.start_line, section.end_line, section.body),
                )
                section_id = section_cursor.lastrowid
                connection.execute(
                    "INSERT INTO sections_fts(section_id,path,heading,body) VALUES(?,?,?,?)",
                    (section_id, path, section.heading, section.body),
                )
            for link in extract_links(root, path, text, tracked, anchors):
                connection.execute(
                    "INSERT INTO links(document_id,line,label,raw_target,kind,resolved_path,fragment,valid,error) VALUES(?,?,?,?,?,?,?,?,?)",
                    (document_id, link.line, link.label, link.raw_target, link.kind, link.resolved_path, link.fragment, int(link.valid), link.error),
                )
        for claim in manifest["claims"]:
            connection.execute(
                "INSERT INTO claims VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    claim["id"], claim["title"], claim["kind"], claim["status"], claim["source"],
                    claim.get("source_heading"), int(claim["active"]), claim.get("scope"),
                    claim.get("label_fidelity"), claim.get("separator_order"),
                    claim.get("colour_compatibility"), claim.get("strict_parameter"),
                    claim.get("audit"), claim.get("expected_source_sha256"),
                ),
            )
            for category in sorted(LIST_ATTRIBUTES):
                for value in claim.get(category, []):
                    connection.execute("INSERT INTO claim_attributes VALUES(?,?,?)", (claim["id"], category, value))
        for relation in manifest["relations"]:
            connection.execute(
                "INSERT INTO relations VALUES(?,?,?,?)",
                (relation["source"], relation["target"], relation["kind"], relation.get("note")),
            )
        for verifier in manifest["verifiers"]:
            connection.execute(
                "INSERT INTO verifiers VALUES(?,?,?,?)",
                (verifier["id"], verifier["path"], verifier["sha256"], verifier["timeout"]),
            )
        connection.commit()
    except sqlite3.OperationalError as exc:
        connection.close()
        temporary.unlink(missing_ok=True)
        if "fts5" in str(exc).lower():
            raise IntegrityError("this Python SQLite build does not provide FTS5") from exc
        raise
    finally:
        if connection:
            connection.close()
    os.replace(temporary, output)
    return output


def ensure_fresh_index(
    database: Path,
    root: Path = ROOT,
    manifest_path: Path = MANIFEST_PATH,
) -> Path:
    expected = corpus_signature(root, manifest_path)
    try:
        with sqlite3.connect(database) as connection:
            metadata = dict(connection.execute("SELECT key,value FROM meta"))
        if metadata.get("schema_version") == "1" and metadata.get("corpus_signature") == expected:
            return database
    except (sqlite3.Error, OSError):
        pass
    return build_index(root, manifest_path, database)


def search_index(database: Path, query: str, area: str | None, limit: int) -> list[tuple]:
    with sqlite3.connect(database) as connection:
        sql = """
          SELECT f.path, s.heading, s.start_line, s.end_line,
                 snippet(sections_fts, 3, '[', ']', ' … ', 18)
          FROM sections_fts AS f
          JOIN sections AS s ON s.id = f.section_id
          JOIN documents AS d ON d.id = s.document_id
          WHERE sections_fts MATCH ?
        """
        params: list[object] = [query]
        if area:
            sql += " AND d.area = ?"
            params.append(area)
        sql += " ORDER BY bm25(sections_fts), f.path, s.start_line LIMIT ?"
        params.append(limit)
        return connection.execute(sql, params).fetchall()


def _claim_map(manifest: dict) -> dict[str, dict]:
    return {claim["id"]: claim for claim in manifest["claims"]}


def _relation_groups(manifest: dict) -> tuple[dict[str, list[dict]], dict[str, list[dict]]]:
    outgoing: defaultdict[str, list[dict]] = defaultdict(list)
    incoming: defaultdict[str, list[dict]] = defaultdict(list)
    for relation in manifest["relations"]:
        outgoing[relation["source"]].append(relation)
        incoming[relation["target"]].append(relation)
    return outgoing, incoming


def proof_dag(manifest: dict) -> str:
    claims = _claim_map(manifest)
    lines = ["# Generated current proof graph", "", "> Non-authoritative; generated from `tools/research_manifest.toml`.", "", "```mermaid", "graph TD"]
    for claim_id in sorted(claims):
        claim = claims[claim_id]
        style = "target" if claim["kind"] == "target" else claim["kind"]
        label = claim["title"].replace('"', "'")
        lines.append(f'  {re.sub(r"[^A-Za-z0-9_]", "_", claim_id)}["{label}"]:::{style}')
    for relation in sorted(manifest["relations"], key=lambda item: (item["kind"], item["target"], item["source"])):
        if relation["kind"] not in PROOF_RELATIONS:
            continue
        dependency = re.sub(r"[^A-Za-z0-9_]", "_", relation["target"])
        consumer = re.sub(r"[^A-Za-z0-9_]", "_", relation["source"])
        lines.append(f'  {consumer} -->|"{relation["kind"]}"| {dependency}')
    lines.extend(["  classDef theorem fill:#d8f3dc,stroke:#2d6a4f", "  classDef lemma fill:#d8f3dc,stroke:#2d6a4f", "  classDef target fill:#fff3bf,stroke:#d9480f", "  classDef barrier fill:#ffe3e3,stroke:#c92a2a", "  classDef laboratory fill:#e7f5ff,stroke:#1971c2", "```", ""])
    return "\n".join(lines)


def trust_boundaries(manifest: dict) -> str:
    lines = ["# Generated trust boundaries", "", "> Non-authoritative; generated from `tools/research_manifest.toml`.", "", "| Claim | Status | Conclusions | Does not prove |", "|---|---|---|---|"]
    for claim in sorted((item for item in manifest["claims"] if item["active"]), key=lambda item: item["id"]):
        conclusions = "; ".join(claim.get("conclusions", [])) or "—"
        gaps = "; ".join(claim.get("does_not_prove", [])) or "—"
        lines.append(f"| `{claim['id']}` | {claim['status']} | {conclusions} | {gaps} |")
    lines.append("")
    return "\n".join(lines)


def barrier_matrix(manifest: dict) -> str:
    lines = ["# Generated barrier matrix", "", "> Non-authoritative; generated from `tools/research_manifest.toml`.", "", "| Barrier | Refutes | Satisfies | Lacks |", "|---|---|---|---|"]
    for claim in sorted((item for item in manifest["claims"] if item["kind"] == "barrier"), key=lambda item: item["id"]):
        lines.append(
            f"| `{claim['id']}` | {'; '.join(claim.get('refutes', [])) or '—'} | {'; '.join(claim.get('satisfies', [])) or '—'} | {'; '.join(claim.get('lacks', [])) or '—'} |"
        )
    lines.append("")
    return "\n".join(lines)


def context_pack(manifest: dict, claim_id: str, database: Path | None = None) -> str:
    claims = _claim_map(manifest)
    if claim_id not in claims:
        raise IntegrityError(f"unknown claim id: {claim_id}")
    claim = claims[claim_id]
    outgoing, incoming = _relation_groups(manifest)
    lines = [f"# Context: {claim['title']}", "", "> Non-authoritative; generated from the curated manifest.", "", f"- **Claim ID:** `{claim_id}`", f"- **Status:** {claim['status']}", f"- **Source:** `{claim['source']}`"]
    if claim.get("strict_parameter"):
        lines.append(f"- **Declared strict parameter:** {claim['strict_parameter']}")
    for heading, key in (("Hypotheses", "hypotheses"), ("Allowed exits", "allowed_exits"), ("Trust boundary", "does_not_prove")):
        values = claim.get(key, [])
        if values:
            lines.extend(["", f"## {heading}", ""] + [f"- {value}" for value in values])
    dependencies = [relation for relation in outgoing.get(claim_id, []) if relation["kind"] in PROOF_RELATIONS]
    if dependencies:
        lines.extend(["", "## Direct prerequisites", ""])
        for relation in sorted(dependencies, key=lambda item: item["target"]):
            dependency = claims[relation["target"]]
            lines.append(f"- `{dependency['id']}` — {dependency['title']} ({dependency['status']})")
    parents = [relation for relation in outgoing.get(claim_id, []) if relation["kind"] == "subproblem_of"]
    if parents:
        lines.extend(["", "## Programme scope", ""])
        for relation in sorted(parents, key=lambda item: item["target"]):
            parent = claims[relation["target"]]
            lines.append(f"- Subproblem of `{parent['id']}` — {parent['title']} ({parent['status']})")
    barriers = [relation for relation in outgoing.get(claim_id, []) if relation["kind"] in {"refuted_by", "sharpness_witness", "related_to", "guarded_by"} and claims[relation["target"]]["kind"] == "barrier"]
    barriers.extend(relation for relation in incoming.get(claim_id, []) if claims[relation["source"]]["kind"] == "barrier")
    if barriers:
        lines.extend(["", "## Directly relevant barriers", ""])
        seen: set[str] = set()
        for relation in sorted(barriers, key=lambda item: (item["source"], item["target"])):
            barrier_id = relation["target"] if claims[relation["target"]]["kind"] == "barrier" else relation["source"]
            if barrier_id in seen:
                continue
            seen.add(barrier_id)
            lines.append(f"- `{barrier_id}` — {claims[barrier_id]['title']}")
    if database and database.exists() and claim.get("keywords"):
        query = " OR ".join(f'"{keyword}"' for keyword in claim["keywords"][:4])
        leads = search_index(database, query, None, 10)
        if leads:
            lines.extend(["", "## Full-text discovery leads", "", "These lexical matches are search hints, not proof dependencies.", ""])
            for path, heading, start, end, _snippet in leads:
                lines.append(f"- `{path}:{start}` — {heading or '(preamble)'} (lines {start}–{end})")
    lines.append("")
    return "\n".join(lines)


def generate_reports(root: Path, manifest: dict, database: Path) -> list[Path]:
    output = database.parent
    output.mkdir(parents=True, exist_ok=True)
    reports = {
        "proof_dag.md": proof_dag(manifest),
        "trust_boundaries.md": trust_boundaries(manifest),
        "barrier_matrix.md": barrier_matrix(manifest),
    }
    paths: list[Path] = []
    for name, content in reports.items():
        path = output / name
        path.write_text(content, encoding="utf-8")
        paths.append(path)
    for claim in sorted((item for item in manifest["claims"] if item["kind"] == "target" and item["active"]), key=lambda item: item["id"]):
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", claim["id"])
        path = output / f"context_{safe}.md"
        path.write_text(context_pack(manifest, claim["id"], database), encoding="utf-8")
        paths.append(path)
    return paths


def run_verifiers(root: Path, manifest: dict, selected: set[str] | None = None) -> None:
    known = {verifier["id"] for verifier in manifest["verifiers"]}
    unknown = (selected or set()) - known
    if unknown:
        raise IntegrityError(f"unknown verifier id(s): {', '.join(sorted(unknown))}")
    for verifier in manifest["verifiers"]:
        if selected and verifier["id"] not in selected:
            continue
        command = [sys.executable, verifier["path"]]
        start = time.monotonic()
        try:
            result = subprocess.run(command, cwd=root, check=False, capture_output=True, text=True, timeout=verifier["timeout"], shell=False)
        except subprocess.TimeoutExpired as exc:
            raise IntegrityError(f"verifier {verifier['id']} timed out after {verifier['timeout']}s") from exc
        elapsed = time.monotonic() - start
        if result.returncode:
            raise IntegrityError(f"verifier {verifier['id']} failed with exit {result.returncode}: {result.stderr.strip()}")
        actual = result.stdout.splitlines()
        if actual != verifier["expected_stdout"]:
            raise IntegrityError(f"verifier {verifier['id']} output mismatch:\nexpected {verifier['expected_stdout']!r}\nactual   {actual!r}")
        if result.stderr.strip():
            raise IntegrityError(f"verifier {verifier['id']} wrote to stderr: {result.stderr.strip()}")
        print(f"PASS {verifier['id']} ({elapsed:.2f}s)")


def print_errors(errors: Sequence[str]) -> int:
    if not errors:
        print("Research integrity check: PASS")
        return 0
    print("Research integrity check: FAIL", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("check", help="validate the curated spine and tracked corpus")
    build_parser = subparsers.add_parser("build", help="rebuild the disposable SQLite/FTS index")
    build_parser.add_argument("--output", type=Path, default=DEFAULT_DATABASE)
    search_parser = subparsers.add_parser("search", help="search indexed Markdown sections")
    search_parser.add_argument("query")
    search_parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    search_parser.add_argument("--area", choices=("root", "active", "results", "barriers", "archive"))
    search_parser.add_argument("--limit", type=int, default=10)
    report_parser = subparsers.add_parser("report", help="generate non-authoritative proof-spine reports")
    report_parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    context_parser = subparsers.add_parser("context", help="generate one target context pack")
    context_parser.add_argument("claim_id")
    context_parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    verifier_parser = subparsers.add_parser("verify", help="run the small deterministic verifier whitelist")
    verifier_parser.add_argument("--id", action="append", dest="ids")
    ci_parser = subparsers.add_parser("ci", help="run check, temporary index/report build, and verifiers")
    ci_parser.add_argument("--skip-verifiers", action="store_true")
    args = parser.parse_args(argv)

    try:
        manifest = load_manifest()
        if args.command == "check":
            return print_errors(validate_repository())
        if args.command == "build":
            path = build_index(output=args.output)
            print(path)
            return 0
        if args.command == "search":
            ensure_fresh_index(args.database)
            for path, heading, start, end, snippet in search_index(args.database, args.query, args.area, args.limit):
                print(f"{path}:{start}-{end}\t{heading or '(preamble)'}\t{snippet.replace(chr(10), ' ')}")
            return 0
        if args.command == "report":
            ensure_fresh_index(args.database)
            for path in generate_reports(ROOT, manifest, args.database):
                print(path)
            return 0
        if args.command == "context":
            ensure_fresh_index(args.database)
            print(context_pack(manifest, args.claim_id, args.database), end="")
            return 0
        if args.command == "verify":
            errors = validate_repository()
            if errors:
                return print_errors(errors)
            run_verifiers(ROOT, manifest, set(args.ids) if args.ids else None)
            return 0
        if args.command == "ci":
            errors = validate_repository()
            if errors:
                return print_errors(errors)
            with tempfile.TemporaryDirectory(prefix="hc7-research-index-") as directory:
                database = Path(directory) / "index.sqlite"
                build_index(output=database)
                generate_reports(ROOT, manifest, database)
                if not search_index(database, '"component defect"', None, 3):
                    raise IntegrityError("FTS smoke query returned no component-defect document")
            if not args.skip_verifiers:
                run_verifiers(ROOT, manifest)
            print("Research integrity CI: PASS")
            return 0
    except (IntegrityError, OSError, sqlite3.Error, tomllib.TOMLDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
