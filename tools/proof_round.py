#!/usr/bin/env python3
"""Run a bounded, provider-blinded 3-1-2 mathematical proof round.

The orchestrator is deliberately non-promotional.  It freezes one theorem
and a small context bundle, launches three read-only laboratories, asks one
fresh selector through a provider-neutral prompt to choose at most one
admissible candidate, and sends that
candidate to two cold referees.  Every generated file lives below
``.cache/research/rounds``; this program never stages, commits, pushes,
merges, or opens a pull request.
"""

from __future__ import annotations

import argparse
import atexit
import concurrent.futures
from contextlib import contextmanager
import fcntl
import functools
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import signal
import subprocess
import sys
import threading
import time
import tomllib
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ROUND_ROOT = REPO_ROOT / ".cache" / "research" / "rounds"
MARKER_NAME = ".proof-round"
FROZEN_NAME = "frozen.json"
STATE_NAME = "state.json"

PROVIDERS = ("codex", "claude", "grok")
LAB_ROLES = ("structural", "colouring", "falsifier")
ROUND_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
ACTIVE_PROCESSES: set[subprocess.Popen[bytes]] = set()
ACTIVE_PROCESSES_LOCK = threading.Lock()

TOP_LEVEL_KEYS = {
    "schema_version",
    "id_prefix",
    "brief_file",
    "context_files",
    "timeout_seconds",
    "max_output_bytes",
    "max_context_bytes",
    "max_repairs",
    "target",
    "providers",
    "labs",
    "selector",
    "review",
}
TARGET_KEYS = {"file", "heading", "sha256"}
PROVIDER_KEYS = {"model", "effort", "claude_max_budget_usd", "grok_max_turns"}
LAB_KEYS = {"provider", "role"}
SELECTOR_KEYS = {"provider"}
REVIEW_KEYS = {"provider_pool", "required", "exclude_selected_author"}

ROLE_INSTRUCTIONS = {
    "structural": (
        "Develop a structural proof.  In particular, test whether absence of "
        "the paired-rooted model forces compatible planar/society structure "
        "or a one-way colour-extension mechanism that actually yields a "
        "four-colouring."
    ),
    "colouring": (
        "Work from a vertex-minimal five-chromatic counterexample.  Use only "
        "proved colouring-extension, Kempe, and minor-model facts, and keep "
        "the two literal root sets distinct from palette colours."
    ),
    "falsifier": (
        "Try to construct a counterexample satisfying every displayed "
        "hypothesis, including five-connectivity and literal two-sided root "
        "contacts.  Weak quotient shadows or lower-connectivity examples do "
        "not count."
    ),
}


class RoundError(RuntimeError):
    """A fail-closed proof-round error."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary = path.with_name(f".{path.name}.{secrets.token_hex(4)}.tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RoundError(f"cannot read valid JSON from {path}: {exc}") from exc


def run_git(args: list[str], *, cwd: Path | None = None) -> str:
    cwd = REPO_ROOT if cwd is None else cwd
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        check=False,
    )
    if result.returncode:
        raise RoundError(
            f"git {' '.join(args)} failed ({result.returncode}): {result.stderr.strip()}"
        )
    return result.stdout.strip()


def ensure_clean_repository() -> None:
    status = run_git(["status", "--porcelain=v1", "--untracked-files=all"])
    if status:
        raise RoundError("the source repository is not clean; commit or classify changes first")


def resolve_tracked_path(relative: str, *, commit: str | None = None) -> Path:
    candidate = (REPO_ROOT / relative).resolve()
    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise RoundError(f"path escapes repository: {relative}") from exc
    if not candidate.is_file():
        raise RoundError(f"required file does not exist: {relative}")
    tracked = run_git(["ls-files", "--error-unmatch", "--", relative])
    if tracked != relative:
        raise RoundError(f"required file is not tracked exactly as written: {relative}")
    if commit is not None:
        run_git(["cat-file", "-e", f"{commit}:{relative}"])
    return candidate


def extract_heading_subtree(text: str, heading: str) -> str:
    lines = text.splitlines(keepends=True)
    hits: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*\r?\n?$", line)
        if match and match.group(2) == heading:
            hits.append((index, len(match.group(1))))
    if len(hits) != 1:
        raise RoundError(
            f"target heading must occur exactly once; found {len(hits)} occurrences: {heading}"
        )
    start, level = hits[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6})[ \t]+", lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "".join(lines[start:end])


def closed_keys(record: dict[str, Any], allowed: set[str], where: str) -> None:
    unknown = set(record) - allowed
    if unknown:
        raise RoundError(f"unknown {where} keys: {', '.join(sorted(unknown))}")


def require_type(value: Any, kind: type | tuple[type, ...], where: str) -> None:
    if not isinstance(value, kind):
        raise RoundError(f"{where} has the wrong type")


def load_config(path: Path) -> dict[str, Any]:
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise RoundError(f"cannot read proof-round configuration: {exc}") from exc
    require_type(raw, dict, "configuration")
    closed_keys(raw, TOP_LEVEL_KEYS, "top-level")
    required = TOP_LEVEL_KEYS - {"providers"}
    missing = required - set(raw)
    if missing:
        raise RoundError(f"missing top-level keys: {', '.join(sorted(missing))}")
    if raw["schema_version"] != 1:
        raise RoundError("unsupported proof-round schema_version")
    for key in ("id_prefix", "brief_file"):
        require_type(raw[key], str, key)
    if not ROUND_ID_RE.fullmatch(raw["id_prefix"]):
        raise RoundError("id_prefix contains unsafe characters")
    require_type(raw["context_files"], list, "context_files")
    if not raw["context_files"] or not all(isinstance(item, str) for item in raw["context_files"]):
        raise RoundError("context_files must be a nonempty string list")
    for key in ("timeout_seconds", "max_output_bytes", "max_context_bytes", "max_repairs"):
        if type(raw[key]) is not int:
            raise RoundError(f"{key} must be an integer, not a boolean")
        if raw[key] < 0:
            raise RoundError(f"{key} must be nonnegative")
    if raw["timeout_seconds"] < 60:
        raise RoundError("timeout_seconds must be at least 60")
    if raw["max_repairs"] not in (0, 1):
        raise RoundError("max_repairs must be zero or one")
    if raw["max_output_bytes"] < 65536 or raw["max_context_bytes"] < 1024:
        raise RoundError("byte limits are too small for a proof round")

    require_type(raw["target"], dict, "target")
    closed_keys(raw["target"], TARGET_KEYS, "target")
    if set(raw["target"]) != TARGET_KEYS:
        raise RoundError("target requires file, heading, and sha256")
    if not all(isinstance(raw["target"][key], str) for key in TARGET_KEYS):
        raise RoundError("target fields must be strings")
    if not re.fullmatch(r"[0-9a-f]{64}", raw["target"]["sha256"]):
        raise RoundError("target.sha256 must be a lowercase SHA-256 digest")

    providers = raw.get("providers", {})
    require_type(providers, dict, "providers")
    if set(providers) != set(PROVIDERS):
        raise RoundError("providers must configure codex, claude, and grok explicitly")
    for provider, settings in providers.items():
        require_type(settings, dict, f"providers.{provider}")
        closed_keys(settings, PROVIDER_KEYS, f"providers.{provider}")
        if not isinstance(settings.get("model"), str) or not settings["model"].strip():
            raise RoundError(f"providers.{provider}.model must be a nonempty pinned model")
        if "effort" in settings and settings["effort"] not in {
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
            "ultra",
        }:
            raise RoundError(f"providers.{provider}.effort is unsupported")
        if "claude_max_budget_usd" in settings:
            budget = settings["claude_max_budget_usd"]
            if isinstance(budget, bool) or not isinstance(budget, (int, float)) or budget <= 0:
                raise RoundError("claude_max_budget_usd must be positive and numeric")
        if "grok_max_turns" in settings:
            turns = settings["grok_max_turns"]
            if type(turns) is not int or turns <= 0:
                raise RoundError("grok_max_turns must be a positive integer")

    require_type(raw["labs"], list, "labs")
    if len(raw["labs"]) != 3:
        raise RoundError("exactly three laboratories are required")
    seen_providers: set[str] = set()
    seen_roles: set[str] = set()
    for index, lab in enumerate(raw["labs"]):
        require_type(lab, dict, f"labs[{index}]")
        closed_keys(lab, LAB_KEYS, f"labs[{index}]")
        if set(lab) != LAB_KEYS:
            raise RoundError("each laboratory requires provider and role")
        if lab["provider"] not in PROVIDERS or lab["role"] not in LAB_ROLES:
            raise RoundError("laboratory has an unsupported provider or role")
        seen_providers.add(lab["provider"])
        seen_roles.add(lab["role"])
    if seen_providers != set(PROVIDERS) or seen_roles != set(LAB_ROLES):
        raise RoundError("laboratories must use each provider and each role exactly once")

    require_type(raw["selector"], dict, "selector")
    closed_keys(raw["selector"], SELECTOR_KEYS, "selector")
    if raw["selector"].get("provider") not in PROVIDERS:
        raise RoundError("selector.provider is unsupported")

    require_type(raw["review"], dict, "review")
    closed_keys(raw["review"], REVIEW_KEYS, "review")
    if set(raw["review"]) != REVIEW_KEYS:
        raise RoundError("review requires provider_pool, required, and exclude_selected_author")
    pool = raw["review"]["provider_pool"]
    if not isinstance(pool, list) or set(pool) != set(PROVIDERS) or len(pool) != 3:
        raise RoundError("review.provider_pool must list codex, claude, and grok once")
    if raw["review"]["required"] != 2 or raw["review"]["exclude_selected_author"] is not True:
        raise RoundError("this protocol requires two referees excluding the candidate author")
    return raw


def provider_version(provider: str) -> str:
    executable = shutil.which(provider)
    if not executable:
        raise RoundError(f"provider CLI is not installed: {provider}")
    result = subprocess.run(
        [executable, "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        check=False,
        timeout=20,
    )
    if result.returncode:
        raise RoundError(f"cannot query {provider} version")
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    lines = [line for line in lines if not line.upper().startswith("WARNING")]
    if not lines:
        raise RoundError(f"{provider} returned no usable version string")
    return lines[0]


def check_provider_interface(provider: str) -> None:
    requirements = {
        "codex": (["exec", "--help"], ["--ephemeral", "--ignore-user-config", "--output-schema"]),
        "claude": (["--help"], ["--no-session-persistence", "--json-schema", "--max-budget-usd"]),
        "grok": (["--help"], ["--prompt-file", "--json-schema", "--max-turns"]),
    }
    args, flags = requirements[provider]
    executable = shutil.which(provider)
    if not executable:
        raise RoundError(f"provider CLI is not installed: {provider}")
    result = subprocess.run(
        [executable, *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        check=False,
        timeout=20,
    )
    if result.returncode or any(flag not in result.stdout for flag in flags):
        raise RoundError(f"{provider} CLI lacks a required non-interactive flag; update it")


def sanitized_environment() -> dict[str, str]:
    allowed = {
        "PATH",
        "HOME",
        "TMPDIR",
        "TMP",
        "TEMP",
        "LANG",
        "LC_ALL",
        "LC_CTYPE",
        "TERM",
        "SSL_CERT_FILE",
        "SSL_CERT_DIR",
        "HTTPS_PROXY",
        "HTTP_PROXY",
        "NO_PROXY",
        "CODEX_HOME",
        "CLAUDE_CONFIG_DIR",
        "GROK_HOME",
    }
    environment = {key: value for key, value in os.environ.items() if key in allowed}
    environment.update(
        {
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ASKPASS": "",
            "GH_PROMPT_DISABLED": "1",
            "PYTHONNOUSERSITE": "1",
        }
    )
    return environment


def candidate_schema() -> dict[str, Any]:
    hypothesis = {
        "type": "object",
        "additionalProperties": False,
        "required": ["hypothesis", "justification"],
        "properties": {
            "hypothesis": {"type": "string"},
            "justification": {"type": "string"},
        },
    }
    argument_step = {
        "type": "object",
        "additionalProperties": False,
        "required": ["step", "statement", "uses"],
        "properties": {
            "step": {"type": "integer"},
            "statement": {"type": "string"},
            "uses": {"type": "array", "items": {"type": "string"}},
        },
    }
    dependency = {
        "type": "object",
        "additionalProperties": False,
        "required": ["source", "exact_statement"],
        "properties": {
            "source": {"type": "string"},
            "exact_statement": {"type": "string"},
        },
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "outcome",
            "claim",
            "hypothesis_checklist",
            "numbered_argument",
            "dependencies",
            "target_implication",
            "well_founded_parameter",
            "strict_decrease_proof",
            "first_unresolved_inference",
            "artifacts",
            "trust_boundary",
        ],
        "properties": {
            "outcome": {
                "type": "string",
                "enum": ["proof", "counterexample", "strict_reduction", "no_result"],
            },
            "claim": {"type": "string"},
            "hypothesis_checklist": {"type": "array", "items": hypothesis},
            "numbered_argument": {"type": "array", "items": argument_step},
            "dependencies": {"type": "array", "items": dependency},
            "target_implication": {"type": "string"},
            "well_founded_parameter": {"type": ["string", "null"]},
            "strict_decrease_proof": {"type": ["string", "null"]},
            "first_unresolved_inference": {"type": ["string", "null"]},
            "artifacts": {"type": "array", "maxItems": 0},
            "trust_boundary": {"type": "array", "items": {"type": "string"}},
        },
    }


def selector_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["selected", "classifications", "selection_reason"],
        "properties": {
            "selected": {"type": ["string", "null"]},
            "classifications": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["candidate", "admissible", "reason"],
                    "properties": {
                        "candidate": {"type": "string"},
                        "admissible": {"type": "boolean"},
                        "reason": {"type": "string"},
                    },
                },
            },
            "selection_reason": {"type": "string"},
        },
    }


def referee_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["verdict", "reconstruction", "blocking_findings", "hypothesis_checklist"],
        "properties": {
            "verdict": {"type": "string", "enum": ["GREEN", "RED"]},
            "reconstruction": {"type": "string"},
            "blocking_findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["step", "claim", "counterargument"],
                    "properties": {
                        "step": {"type": "integer"},
                        "claim": {"type": "string"},
                        "counterargument": {"type": "string"},
                    },
                },
            },
            "hypothesis_checklist": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["hypothesis", "verdict", "reason"],
                    "properties": {
                        "hypothesis": {"type": "string"},
                        "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
                        "reason": {"type": "string"},
                    },
                },
            },
        },
    }


def validate_candidate(value: Any) -> tuple[bool, str]:
    if not isinstance(value, dict):
        return False, "candidate is not an object"
    required = set(candidate_schema()["required"])
    if set(value) != required:
        return False, "candidate fields do not exactly match the closed schema"
    if value["outcome"] not in {"proof", "counterexample", "strict_reduction", "no_result"}:
        return False, "unsupported outcome"
    string_fields = ("claim", "target_implication")
    if not all(isinstance(value[key], str) for key in string_fields):
        return False, "claim and target_implication must be strings"
    list_fields = ("hypothesis_checklist", "numbered_argument", "dependencies", "artifacts", "trust_boundary")
    if not all(isinstance(value[key], list) for key in list_fields):
        return False, "candidate list fields have the wrong type"
    for item in value["hypothesis_checklist"]:
        if not isinstance(item, dict) or set(item) != {"hypothesis", "justification"}:
            return False, "hypothesis checklist item is malformed"
        if not all(isinstance(item[key], str) and item[key].strip() for key in item):
            return False, "hypothesis checklist item is empty"
    for expected_step, item in enumerate(value["numbered_argument"], start=1):
        if not isinstance(item, dict) or set(item) != {"step", "statement", "uses"}:
            return False, "numbered argument item is malformed"
        if item["step"] != expected_step or not isinstance(item["statement"], str):
            return False, "numbered argument is not consecutively numbered"
        if not isinstance(item["uses"], list) or not all(isinstance(use, str) for use in item["uses"]):
            return False, "numbered argument dependencies are malformed"
    for item in value["dependencies"]:
        if not isinstance(item, dict) or set(item) != {"source", "exact_statement"}:
            return False, "dependency item is malformed"
        if not all(isinstance(item[key], str) and item[key].strip() for key in item):
            return False, "dependency item is empty"
    if not all(isinstance(item, str) and item.strip() for item in value["trust_boundary"]):
        return False, "trust boundary items must be nonempty strings"
    nullable = ("well_founded_parameter", "strict_decrease_proof", "first_unresolved_inference")
    if not all(value[key] is None or isinstance(value[key], str) for key in nullable):
        return False, "candidate nullable fields have the wrong type"
    if value["outcome"] == "no_result":
        return False, "no_result is recorded but is not selectable"
    if not value["claim"].strip() or not value["numbered_argument"] or not value["target_implication"].strip():
        return False, "candidate lacks a claim, numbered argument, or target implication"
    if value["outcome"] in {"proof", "counterexample"} and value["first_unresolved_inference"]:
        return False, "a proof or counterexample cannot retain an unresolved inference"
    if value["outcome"] == "counterexample" and not value["hypothesis_checklist"]:
        return False, "counterexample does not certify the target hypotheses"
    if value["outcome"] == "strict_reduction":
        if not value["well_founded_parameter"] or not value["strict_decrease_proof"]:
            return False, "strict reduction lacks a well-founded parameter or decrease proof"
        if value["first_unresolved_inference"]:
            return False, "the strict-reduction theorem itself is not complete"
    if value["artifacts"]:
        return False, "v1 requires proofs and certificates inline; external artifacts are disabled"
    return True, "contract-complete; mathematical correctness is not asserted"


def validate_selector(value: Any, admissible: set[str]) -> None:
    if not isinstance(value, dict) or set(value) != set(selector_schema()["required"]):
        raise RoundError("selector returned an object outside its closed schema")
    if not isinstance(value["classifications"], list) or not isinstance(value["selection_reason"], str):
        raise RoundError("selector fields have the wrong type")
    classified: dict[str, bool] = {}
    for item in value["classifications"]:
        if not isinstance(item, dict) or set(item) != {"candidate", "admissible", "reason"}:
            raise RoundError("selector classification is malformed")
        if not isinstance(item["candidate"], str) or not isinstance(item["admissible"], bool):
            raise RoundError("selector classification fields have the wrong type")
        if not isinstance(item["reason"], str) or not item["reason"].strip():
            raise RoundError("selector classification lacks a reason")
        if item["candidate"] in classified:
            raise RoundError("selector classified one candidate more than once")
        classified[item["candidate"]] = item["admissible"]
    if set(classified) != admissible:
        raise RoundError("selector must classify every admissible candidate exactly once")
    selected = value["selected"]
    if selected is not None and (not isinstance(selected, str) or selected not in admissible):
        raise RoundError("selector chose a missing or inadmissible candidate")
    if selected is not None and classified[selected] is not True:
        raise RoundError("selector chose a candidate it classified as inadmissible")


def validate_referee(value: Any) -> None:
    if not isinstance(value, dict) or set(value) != set(referee_schema()["required"]):
        raise RoundError("referee returned an object outside its closed schema")
    if value["verdict"] not in {"GREEN", "RED"}:
        raise RoundError("referee verdict must be GREEN or RED")
    if not isinstance(value["reconstruction"], str):
        raise RoundError("referee reconstruction must be a string")
    if not isinstance(value["blocking_findings"], list) or not isinstance(
        value["hypothesis_checklist"], list
    ):
        raise RoundError("referee list fields have the wrong type")
    if value["verdict"] == "GREEN" and value["blocking_findings"]:
        raise RoundError("GREEN referee cannot retain blocking findings")
    for finding in value["blocking_findings"]:
        if not isinstance(finding, dict) or set(finding) != {"step", "claim", "counterargument"}:
            raise RoundError("referee blocking finding is malformed")
        if not isinstance(finding["step"], int):
            raise RoundError("referee finding step must be an integer")
    if not value["hypothesis_checklist"]:
        raise RoundError("referee must check the target hypotheses")
    for item in value["hypothesis_checklist"]:
        if not isinstance(item, dict) or set(item) != {"hypothesis", "verdict", "reason"}:
            raise RoundError("referee hypothesis item is malformed")
        if item["verdict"] not in {"PASS", "FAIL"}:
            raise RoundError("referee hypothesis verdict is invalid")
    if value["verdict"] == "GREEN" and any(
        item["verdict"] == "FAIL" for item in value["hypothesis_checklist"]
    ):
        raise RoundError("GREEN referee cannot fail a target hypothesis")


def parse_provider_json(provider: str, text: str) -> dict[str, Any]:
    try:
        value: Any = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RoundError(f"{provider} returned malformed JSON") from exc
    for _ in range(4):
        if isinstance(value, dict) and any(key in value for key in ("outcome", "selected", "verdict")):
            return value
        if isinstance(value, dict):
            for key in ("structured_output", "result", "output", "content", "response"):
                nested = value.get(key)
                if isinstance(nested, dict):
                    value = nested
                    break
                if isinstance(nested, str):
                    try:
                        value = json.loads(nested)
                    except json.JSONDecodeError:
                        continue
                    break
            else:
                break
        else:
            break
    raise RoundError(f"{provider} JSON does not contain the structured result")


def safe_round_path(round_id: str) -> Path:
    if not ROUND_ID_RE.fullmatch(round_id):
        raise RoundError("unsafe round id")
    root = ROUND_ROOT.resolve()
    path = (ROUND_ROOT / round_id).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise RoundError("round path escapes the generated round root") from exc
    return path


def build_context(config: dict[str, Any], commit: str) -> tuple[str, list[dict[str, str]]]:
    parts: list[str] = []
    records: list[dict[str, str]] = []
    total = 0
    for relative in config["context_files"]:
        path = resolve_tracked_path(relative, commit=commit)
        data = path.read_bytes()
        total += len(data)
        if total > config["max_context_bytes"]:
            raise RoundError("context bundle exceeds max_context_bytes")
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise RoundError(f"context file is not UTF-8 text: {relative}") from exc
        records.append({"path": relative, "sha256": sha256_bytes(data)})
        parts.append(f"\n\n===== BEGIN {relative} =====\n{content}\n===== END {relative} =====")
    return "".join(parts), records


def clone_at_commit(destination: Path, commit: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["git", "clone", "--quiet", "--no-checkout", "--no-hardlinks", str(REPO_ROOT), str(destination)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        check=False,
    )
    if result.returncode:
        raise RoundError(f"cannot create disposable clone: {result.stderr.strip()}")
    run_git(["checkout", "--quiet", "--detach", commit], cwd=destination)
    run_git(["remote", "remove", "origin"], cwd=destination)
    if run_git(["rev-parse", "HEAD"], cwd=destination) != commit:
        raise RoundError("disposable clone did not resolve to the frozen commit")
    if run_git(["status", "--porcelain=v1", "--untracked-files=all"], cwd=destination):
        raise RoundError("disposable clone is not clean")
    alternates = destination / ".git" / "objects" / "info" / "alternates"
    if alternates.exists():
        raise RoundError("disposable clone unexpectedly shares Git objects")


def make_round_id(prefix: str) -> str:
    stamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    return f"{prefix}-{stamp}-{secrets.token_hex(2)}"


def prepare_round(config_path: Path, requested_id: str | None, *, write: bool = True) -> dict[str, Any]:
    ensure_clean_repository()
    config_path = config_path.resolve()
    try:
        config_relative = config_path.relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise RoundError("configuration must be inside the repository") from exc
    resolve_tracked_path(config_relative)
    config = load_config(config_path)
    commit = run_git(["rev-parse", "--verify", "HEAD^{commit}"])
    if len(commit) != 40:
        raise RoundError("could not freeze a full Git commit id")

    target_path = resolve_tracked_path(config["target"]["file"], commit=commit)
    target_subtree = extract_heading_subtree(
        target_path.read_text(encoding="utf-8"), config["target"]["heading"]
    )
    target_hash = sha256_bytes(target_subtree.encode("utf-8"))
    if target_hash != config["target"]["sha256"]:
        raise RoundError(
            "target heading hash drifted; review the theorem and update the proof-round brief explicitly"
        )
    brief_path = resolve_tracked_path(config["brief_file"], commit=commit)
    brief = brief_path.read_text(encoding="utf-8")
    context, context_records = build_context(config, commit)
    versions = {provider: provider_version(provider) for provider in PROVIDERS}
    round_id = requested_id or make_round_id(config["id_prefix"])
    round_dir = safe_round_path(round_id)
    if round_dir.exists():
        raise RoundError(f"round already exists: {round_id}")

    lab_records: list[dict[str, str]] = []
    for lab in config["labs"]:
        lab_records.append(
            {
                "opaque_id": f"candidate-{secrets.token_hex(4)}",
                "provider": lab["provider"],
                "role": lab["role"],
            }
        )
    frozen = {
        "schema_version": 1,
        "round_id": round_id,
        "base_commit": commit,
        "config_path": config_relative,
        "config_sha256": sha256_file(config_path),
        "brief_path": config["brief_file"],
        "brief_sha256": sha256_file(brief_path),
        "target": {
            "file": config["target"]["file"],
            "heading": config["target"]["heading"],
            "sha256": target_hash,
        },
        "context": context_records,
        "provider_versions": versions,
        "labs": lab_records,
        "selector_provider": config["selector"]["provider"],
        "review": config["review"],
        "limits": {
            "timeout_seconds": config["timeout_seconds"],
            "max_output_bytes": config["max_output_bytes"],
            "max_repairs": config["max_repairs"],
        },
        "provider_settings": config.get("providers", {}),
    }
    if not write:
        return frozen

    round_dir.mkdir(parents=True)
    (round_dir / MARKER_NAME).write_text("proof-round-v1\n", encoding="utf-8")
    (round_dir / "inputs").mkdir()
    (round_dir / "inputs" / "brief.md").write_text(brief, encoding="utf-8")
    (round_dir / "inputs" / "context.md").write_text(context, encoding="utf-8")
    write_json(round_dir / "inputs" / "candidate.schema.json", candidate_schema())
    write_json(round_dir / "inputs" / "selector.schema.json", selector_schema())
    write_json(round_dir / "inputs" / "referee.schema.json", referee_schema())
    write_json(round_dir / FROZEN_NAME, frozen)
    write_json(
        round_dir / STATE_NAME,
        {
            "round_id": round_id,
            "stage": "prepared",
            "repair_count": 0,
            "selected": None,
            "verdict": None,
        },
    )
    clone_at_commit(round_dir / "snapshot", commit)
    for lab in lab_records:
        lab_dir = round_dir / "labs" / lab["opaque_id"]
        lab_dir.mkdir(parents=True)
        prompt = lab_prompt(brief, context, lab["role"])
        (lab_dir / "prompt.md").write_text(prompt, encoding="utf-8")
    for number in (1, 2):
        (round_dir / "referees" / f"referee-{number}").mkdir(parents=True)
    write_summary(round_dir)
    return frozen


def lab_prompt(brief: str, context: str, role: str) -> str:
    return f"""You are one blind laboratory in a bounded mathematical proof round.

Your role is **{role}**. {ROLE_INSTRUCTIONS[role]}

Provider identity and other laboratory outputs are intentionally unavailable.
Work only on the frozen target. Return exactly one JSON object satisfying the
supplied candidate schema. A strict reduction must include a proved
well-founded host-level parameter and an explicit implication back to the
target. If you cannot meet an allowed outcome, return `no_result` and identify
the first unresolved inference. Do not claim that an internal audit is peer
review.

===== FROZEN BRIEF =====
{brief}

===== FROZEN CONTEXT =====
{context}
"""


def selector_prompt(brief: str, candidates: dict[str, dict[str, Any]]) -> str:
    neutral = json.dumps(candidates, indent=2, sort_keys=True, ensure_ascii=False)
    return f"""You are the fresh, provider-blinded selector in a bounded proof round.

Choose at most one candidate, and choose none when no candidate is proof-quality.
The deterministic filter checked only contract completeness, not mathematics.
Reject unstated hypotheses, quotient-only models, finite-only evidence, missing
literal root contacts, selected colourings presented as universal extension,
or an unproved theorem-strength lemma. Return exactly the selector schema.

===== FROZEN BRIEF =====
{brief}

===== OPAQUE CANDIDATES =====
{neutral}
"""


def referee_prompt(
    brief: str,
    context: str,
    candidate_id: str,
    candidate: dict[str, Any],
    audit_role: str,
    prior_findings: list[dict[str, Any]] | None = None,
) -> str:
    prior = ""
    if prior_findings:
        prior = "\nPrior blocking findings to recheck after repair:\n" + json.dumps(
            prior_findings, indent=2, ensure_ascii=False
        )
    role_text = (
        "Audit every inference, theorem dependency, literal A/B contact, "
        "connectivity assertion, separator order, and claimed implication."
        if audit_role == "inference"
        else "Independently reconstruct the minor/colouring/counterexample and rerun or inspect every certificate."
    )
    return f"""You are a cold mathematical referee. {role_text}

Any concrete gap requires RED. GREEN means no blocking finding after an
independent reconstruction; it remains an internal audit, not peer review.
Return exactly the referee schema.{prior}

===== FROZEN BRIEF =====
{brief}

===== FROZEN CONTEXT =====
{context}

===== SELECTED CANDIDATE {candidate_id} =====
{json.dumps(candidate, indent=2, sort_keys=True, ensure_ascii=False)}
"""


def provider_command(
    provider: str,
    clone: Path,
    prompt_path: Path,
    schema_path: Path,
    result_path: Path,
    settings: dict[str, Any],
) -> tuple[list[str], bytes | None]:
    model = settings.get("model", "")
    if provider == "codex":
        command = [
            "codex",
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--sandbox",
            "read-only",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(result_path),
            "--color",
            "never",
            "-C",
            str(clone),
        ]
        if model:
            command.extend(["--model", model])
        if settings.get("effort"):
            command.extend(["--config", f'model_reasoning_effort="{settings["effort"]}"'])
        command.append("-")
        return command, prompt_path.read_bytes()
    if provider == "claude":
        command = [
            "claude",
            "--print",
            "--no-session-persistence",
            "--disable-slash-commands",
            "--no-chrome",
            "--strict-mcp-config",
            "--mcp-config",
            '{"mcpServers":{}}',
            "--tools",
            "",
            "--permission-mode",
            "dontAsk",
            "--output-format",
            "json",
            "--json-schema",
            json.dumps(read_json(schema_path), separators=(",", ":")),
        ]
        if model:
            command.extend(["--model", model])
        if settings.get("effort"):
            command.extend(["--effort", settings["effort"]])
        budget = settings.get("claude_max_budget_usd")
        if budget is not None:
            command.extend(["--max-budget-usd", str(budget)])
        return command, prompt_path.read_bytes()
    if provider == "grok":
        command = [
            "grok",
            "--prompt-file",
            str(prompt_path),
            "--no-memory",
            "--no-subagents",
            "--disable-web-search",
            "--permission-mode",
            "dontAsk",
            "--tools",
            "",
            "--output-format",
            "json",
            "--json-schema",
            json.dumps(read_json(schema_path), separators=(",", ":")),
            "--cwd",
            str(clone),
        ]
        if model:
            command.extend(["--model", model])
        if settings.get("effort"):
            command.extend(["--reasoning-effort", settings["effort"]])
        turns = settings.get("grok_max_turns")
        if turns is not None:
            command.extend(["--max-turns", str(turns)])
        return command, None
    raise RoundError(f"unsupported provider: {provider}")


def terminate_process_group(process: subprocess.Popen[bytes]) -> None:
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass


def terminate_active_processes() -> None:
    with ACTIVE_PROCESSES_LOCK:
        processes = list(ACTIVE_PROCESSES)
    for process in processes:
        terminate_process_group(process)


atexit.register(terminate_active_processes)


def invoke_provider(
    provider: str,
    clone: Path,
    prompt_path: Path,
    schema_path: Path,
    stage_dir: Path,
    settings: dict[str, Any],
    timeout_seconds: int,
    max_output_bytes: int,
) -> dict[str, Any]:
    stage_dir.mkdir(parents=True, exist_ok=True)
    result_path = stage_dir / "result.raw.json"
    command, standard_input = provider_command(
        provider, clone, prompt_path, schema_path, result_path, settings
    )
    command_record = [Path(item).name if index == 0 else item for index, item in enumerate(command)]
    write_json(stage_dir / "invocation.json", {"argv": command_record, "provider": provider})
    started = time.monotonic()
    stdout_path = stage_dir / "stdout.log"
    stderr_path = stage_dir / "stderr.log"
    with stdout_path.open("wb") as stdout_file, stderr_path.open("wb") as stderr_file:
        process = subprocess.Popen(
            command,
            cwd=clone,
            stdin=subprocess.PIPE if standard_input is not None else subprocess.DEVNULL,
            stdout=stdout_file,
            stderr=stderr_file,
            env=sanitized_environment(),
            shell=False,
            start_new_session=True,
        )
        with ACTIVE_PROCESSES_LOCK:
            ACTIVE_PROCESSES.add(process)
        def feed_standard_input() -> None:
            if standard_input is None or process.stdin is None:
                return
            try:
                process.stdin.write(standard_input)
                process.stdin.close()
            except (BrokenPipeError, OSError):
                pass

        feeder = threading.Thread(target=feed_standard_input, daemon=True)
        feeder.start()
        deadline = started + timeout_seconds
        failure: str | None = None
        try:
            while process.poll() is None:
                if time.monotonic() >= deadline:
                    failure = f"{provider} timed out after {timeout_seconds} seconds"
                    terminate_process_group(process)
                    break
                watched = (stdout_path, stderr_path, result_path)
                if any(path.exists() and path.stat().st_size > max_output_bytes for path in watched):
                    failure = f"{provider} output exceeded max_output_bytes"
                    terminate_process_group(process)
                    break
                time.sleep(0.2)
            feeder.join(timeout=2)
        except BaseException:
            terminate_process_group(process)
            raise
        finally:
            with ACTIVE_PROCESSES_LOCK:
                ACTIVE_PROCESSES.discard(process)
        if failure:
            raise RoundError(failure)
    elapsed = round(time.monotonic() - started, 3)
    for path in (stdout_path, stderr_path, result_path):
        if path.exists() and path.stat().st_size > max_output_bytes:
            raise RoundError(f"{provider} output exceeded max_output_bytes")
    write_json(
        stage_dir / "exit.json",
        {"returncode": process.returncode, "elapsed_seconds": elapsed},
    )
    if process.returncode:
        raise RoundError(f"{provider} exited with status {process.returncode}")
    raw = (
        result_path.read_text(encoding="utf-8")
        if result_path.exists()
        else stdout_path.read_text(encoding="utf-8")
    )
    value = parse_provider_json(provider, raw)
    if run_git(["status", "--porcelain=v1", "--untracked-files=all"], cwd=clone):
        raise RoundError(f"{provider} modified its frozen clone")
    write_json(stage_dir / "result.json", value)
    return value


def load_round(round_id: str) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    round_dir = safe_round_path(round_id)
    if not round_dir.is_dir() or (round_dir / MARKER_NAME).read_text(encoding="utf-8") != "proof-round-v1\n":
        raise RoundError("round is missing its generated marker")
    frozen = read_json(round_dir / FROZEN_NAME)
    state = read_json(round_dir / STATE_NAME)
    if frozen.get("round_id") != round_id or state.get("round_id") != round_id:
        raise RoundError("round metadata does not match the requested id")
    return round_dir, frozen, state


@contextmanager
def round_lock(round_dir: Path):
    lock_path = round_dir / ".run.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RoundError("another process is already operating on this round") from exc
        try:
            yield
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def locked_round(operation):
    @functools.wraps(operation)
    def wrapper(round_id: str):
        round_dir = safe_round_path(round_id)
        if not round_dir.is_dir():
            raise RoundError("proof round does not exist")
        with round_lock(round_dir):
            return operation(round_id)

    return wrapper


def run_laboratory(round_dir: Path, frozen: dict[str, Any], lab: dict[str, str]) -> tuple[str, dict[str, Any]]:
    lab_dir = round_dir / "labs" / lab["opaque_id"]
    result = invoke_provider(
        lab["provider"],
        round_dir / "snapshot",
        lab_dir / "prompt.md",
        round_dir / "inputs" / "candidate.schema.json",
        lab_dir,
        frozen["provider_settings"].get(lab["provider"], {}),
        frozen["limits"]["timeout_seconds"],
        frozen["limits"]["max_output_bytes"],
    )
    return lab["opaque_id"], result


@locked_round
def run_round(round_id: str) -> None:
    ensure_clean_repository()
    round_dir, frozen, state = load_round(round_id)
    if state["stage"] != "prepared":
        raise RoundError(f"round cannot run from stage {state['stage']}")
    state["stage"] = "labs_running"
    write_json(round_dir / STATE_NAME, state)
    candidates: dict[str, dict[str, Any]] = {}
    failures: dict[str, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(run_laboratory, round_dir, frozen, lab): lab["opaque_id"]
            for lab in frozen["labs"]
        }
        for future in concurrent.futures.as_completed(futures):
            opaque = futures[future]
            try:
                candidate_id, candidate = future.result()
                candidates[candidate_id] = candidate
            except Exception as exc:  # preserve all three diagnostics
                failures[opaque] = str(exc)
    write_json(round_dir / "labs" / "failures.json", failures)
    if failures:
        state.update({"stage": "complete_infrastructure_failure", "verdict": "NONE"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise RoundError("one or more laboratories failed; inspect the generated diagnostics")

    admissibility: dict[str, dict[str, Any]] = {}
    admissible: dict[str, dict[str, Any]] = {}
    for candidate_id, candidate in candidates.items():
        ok, reason = validate_candidate(candidate)
        admissibility[candidate_id] = {"admissible": ok, "reason": reason}
        if ok:
            admissible[candidate_id] = candidate
    write_json(round_dir / "labs" / "admissibility.json", admissibility)
    if not admissible:
        state.update({"stage": "complete_no_candidate", "selected": None, "verdict": "NONE"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        return

    brief = (round_dir / "inputs" / "brief.md").read_text(encoding="utf-8")
    selector_dir = round_dir / "selector"
    selector_dir.mkdir(parents=True, exist_ok=True)
    (selector_dir / "prompt.md").write_text(selector_prompt(brief, admissible), encoding="utf-8")
    try:
        selector = invoke_provider(
            frozen["selector_provider"],
            round_dir / "snapshot",
            selector_dir / "prompt.md",
            round_dir / "inputs" / "selector.schema.json",
            selector_dir,
            frozen["provider_settings"].get(frozen["selector_provider"], {}),
            frozen["limits"]["timeout_seconds"],
            frozen["limits"]["max_output_bytes"],
        )
        validate_selector(selector, set(admissible))
    except Exception:
        state.update({"stage": "complete_infrastructure_failure", "verdict": "NONE"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise
    selected = selector["selected"]
    if selected is None:
        state.update({"stage": "complete_no_selection", "selected": None, "verdict": "NONE"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        return

    state["selected"] = selected
    state["stage"] = "reviewing"
    write_json(round_dir / STATE_NAME, state)
    try:
        run_referees(round_dir, frozen, state, admissible[selected], repair=False)
    except Exception:
        state.update({"stage": "complete_review_failure", "verdict": "NONE"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise


def run_referees(
    round_dir: Path,
    frozen: dict[str, Any],
    state: dict[str, Any],
    candidate: dict[str, Any],
    *,
    repair: bool,
    prior_findings: list[dict[str, Any]] | None = None,
) -> None:
    selected = state["selected"]
    author = next(lab["provider"] for lab in frozen["labs"] if lab["opaque_id"] == selected)
    reviewer_providers = [provider for provider in frozen["review"]["provider_pool"] if provider != author]
    if len(reviewer_providers) != 2:
        raise RoundError("cannot assign two distinct cold referees")
    brief = (round_dir / "inputs" / "brief.md").read_text(encoding="utf-8")
    context = (round_dir / "inputs" / "context.md").read_text(encoding="utf-8")
    base = round_dir / ("repair" if repair else "referees")
    audit_roles = ("inference", "reconstruction")
    jobs: list[tuple[str, str, Path]] = []
    for number, (provider, audit_role) in enumerate(zip(reviewer_providers, audit_roles), start=1):
        referee_dir = base / f"referee-{number}"
        referee_dir.mkdir(parents=True, exist_ok=True)
        prompt = referee_prompt(
            brief, context, selected, candidate, audit_role, prior_findings=prior_findings
        )
        (referee_dir / "prompt.md").write_text(prompt, encoding="utf-8")
        jobs.append((provider, audit_role, referee_dir))

    def invoke(job: tuple[str, str, Path]) -> tuple[str, dict[str, Any]]:
        provider, audit_role, referee_dir = job
        result = invoke_provider(
            provider,
            round_dir / "snapshot",
            referee_dir / "prompt.md",
            round_dir / "inputs" / "referee.schema.json",
            referee_dir,
            frozen["provider_settings"].get(provider, {}),
            frozen["limits"]["timeout_seconds"],
            frozen["limits"]["max_output_bytes"],
        )
        validate_referee(result)
        return audit_role, result

    reviews: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(invoke, job) for job in jobs]
        for future in concurrent.futures.as_completed(futures):
            role, review = future.result()
            reviews[role] = review
    verdict = "GREEN" if all(review["verdict"] == "GREEN" for review in reviews.values()) else "RED"
    write_json(base / "reviews.json", reviews)
    state["stage"] = "complete_green" if verdict == "GREEN" else "complete_vetoed"
    state["verdict"] = verdict
    write_json(round_dir / STATE_NAME, state)
    write_summary(round_dir)


@locked_round
def repair_round(round_id: str) -> None:
    ensure_clean_repository()
    round_dir, frozen, state = load_round(round_id)
    if state["stage"] != "complete_vetoed" or not state.get("selected"):
        raise RoundError("repair is available only after a selected candidate is vetoed")
    if state["repair_count"] >= frozen["limits"]["max_repairs"]:
        raise RoundError("the one-repair ceiling has been reached")
    state["repair_count"] += 1
    state["stage"] = "repairing"
    write_json(round_dir / STATE_NAME, state)
    selected = state["selected"]
    author_record = next(lab for lab in frozen["labs"] if lab["opaque_id"] == selected)
    original = read_json(round_dir / "labs" / selected / "result.json")
    reviews = read_json(round_dir / "referees" / "reviews.json")
    findings = [
        finding
        for review in reviews.values()
        for finding in review.get("blocking_findings", [])
    ]
    repair_dir = round_dir / "repair" / "author"
    repair_dir.mkdir(parents=True, exist_ok=True)
    prompt = f"""Repair the selected candidate once. Address every blocking finding.
Return a complete candidate-schema object, not a response letter. If the proof
cannot be repaired, return no_result. No second repair is permitted.

ORIGINAL CANDIDATE:\n{json.dumps(original, indent=2, ensure_ascii=False)}

BLOCKING FINDINGS:\n{json.dumps(findings, indent=2, ensure_ascii=False)}

FROZEN BRIEF:\n{(round_dir / 'inputs' / 'brief.md').read_text(encoding='utf-8')}

FROZEN CONTEXT:\n{(round_dir / 'inputs' / 'context.md').read_text(encoding='utf-8')}
"""
    (repair_dir / "prompt.md").write_text(prompt, encoding="utf-8")
    try:
        repaired = invoke_provider(
            author_record["provider"],
            round_dir / "snapshot",
            repair_dir / "prompt.md",
            round_dir / "inputs" / "candidate.schema.json",
            repair_dir,
            frozen["provider_settings"].get(author_record["provider"], {}),
            frozen["limits"]["timeout_seconds"],
            frozen["limits"]["max_output_bytes"],
        )
    except Exception:
        state.update({"stage": "complete_repair_failed", "verdict": "RED"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise
    ok, reason = validate_candidate(repaired)
    if not ok:
        state.update({"stage": "complete_repair_failed", "verdict": "RED"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise RoundError(f"repaired candidate is inadmissible: {reason}")
    state["stage"] = "reviewing_repair"
    state["verdict"] = None
    write_json(round_dir / STATE_NAME, state)
    try:
        run_referees(round_dir, frozen, state, repaired, repair=True, prior_findings=findings)
    except Exception:
        state.update({"stage": "complete_repair_review_failure", "verdict": "RED"})
        write_json(round_dir / STATE_NAME, state)
        write_summary(round_dir)
        raise


def write_summary(round_dir: Path) -> None:
    frozen = read_json(round_dir / FROZEN_NAME)
    state = read_json(round_dir / STATE_NAME)
    lines = [
        f"# Proof round `{frozen['round_id']}`",
        "",
        f"- Frozen commit: `{frozen['base_commit']}`",
        f"- Target: `{frozen['target']['file']}` — {frozen['target']['heading']}",
        f"- Target hash: `{frozen['target']['sha256']}`",
        f"- Stage: `{state['stage']}`",
        f"- Selected candidate: `{state.get('selected') or 'none'}`",
        f"- Internal referee verdict: `{state.get('verdict') or 'pending'}`",
        f"- Repair count: `{state.get('repair_count', 0)}`",
        "",
        "Generated artifacts are non-authoritative and ignored by Git. A GREEN",
        "result is an internal audit only and must be promoted manually through",
        "the repository theorem-and-audit workflow.",
        "",
    ]
    (round_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def status_round(round_id: str) -> None:
    round_dir, frozen, state = load_round(round_id)
    print((round_dir / "summary.md").read_text(encoding="utf-8"))
    print("Provider versions:")
    for provider, version in frozen["provider_versions"].items():
        print(f"  {provider}: {version}")
    if (round_dir / "labs" / "admissibility.json").exists():
        print("Admissibility:")
        for candidate, record in read_json(round_dir / "labs" / "admissibility.json").items():
            print(f"  {candidate}: {record['admissible']} — {record['reason']}")
    if state["stage"] == "complete_infrastructure_failure":
        print("Laboratory failures:")
        for candidate, reason in read_json(round_dir / "labs" / "failures.json").items():
            print(f"  {candidate}: {reason}")


@locked_round
def cleanup_round(round_id: str) -> None:
    round_dir, _, _ = load_round(round_id)
    root = ROUND_ROOT.resolve()
    if round_dir.parent != root:
        raise RoundError("refusing cleanup outside the generated round root")
    shutil.rmtree(round_dir)
    print(f"Removed generated proof round {round_id}")


def doctor(config_path: Path | None) -> None:
    ensure_clean_repository()
    print(f"Repository: clean at {run_git(['rev-parse', 'HEAD'])}")
    print(f"Python: {sys.version.split()[0]}")
    if sys.version_info < (3, 11):
        raise RoundError("Python 3.11 or newer is required")
    for provider in PROVIDERS:
        version = provider_version(provider)
        check_provider_interface(provider)
        print(f"{provider}: {version} (required interface present)")
    if config_path:
        frozen = prepare_round(config_path, "doctor-check", write=False)
        print(f"Target hash: {frozen['target']['sha256']} (verified)")
        print(f"Context files: {len(frozen['context'])} (verified and tracked)")
    print("Authentication is not probed to avoid network calls; run each provider's auth status command.")


def dry_run(config_path: Path) -> None:
    frozen = prepare_round(config_path, "dry-run-check", write=False)
    public = dict(frozen)
    public["labs"] = [
        {"opaque_id": lab["opaque_id"], "role": lab["role"], "provider": "<blinded>"}
        for lab in frozen["labs"]
    ]
    public["selector_provider"] = "<configured fresh session>"
    print(json.dumps(public, indent=2, sort_keys=True, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    doctor_parser = subparsers.add_parser("doctor", help="check repository, CLIs, and optional config")
    doctor_parser.add_argument("config", nargs="?", type=Path)
    dry_parser = subparsers.add_parser("dry-run", help="validate and display a frozen plan without writing")
    dry_parser.add_argument("config", type=Path)
    prepare_parser = subparsers.add_parser("prepare", help="freeze inputs and create isolated clones")
    prepare_parser.add_argument("config", type=Path)
    prepare_parser.add_argument("--round-id")
    run_parser = subparsers.add_parser("run", help="run labs, selector, and cold referees")
    run_parser.add_argument("round_id")
    repair_parser = subparsers.add_parser("repair", help="permit the selected author one repair")
    repair_parser.add_argument("round_id")
    status_parser = subparsers.add_parser("status", help="show a generated round summary")
    status_parser.add_argument("round_id")
    cleanup_parser = subparsers.add_parser("cleanup", help="remove one marked generated round")
    cleanup_parser.add_argument("round_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "doctor":
            doctor(args.config)
        elif args.command == "dry-run":
            dry_run(args.config)
        elif args.command == "prepare":
            frozen = prepare_round(args.config, args.round_id)
            print(frozen["round_id"])
        elif args.command == "run":
            run_round(args.round_id)
            status_round(args.round_id)
        elif args.command == "repair":
            repair_round(args.round_id)
            status_round(args.round_id)
        elif args.command == "status":
            status_round(args.round_id)
        elif args.command == "cleanup":
            cleanup_round(args.round_id)
        else:  # pragma: no cover
            raise RoundError("unknown command")
    except RoundError as exc:
        print(f"proof-round error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
