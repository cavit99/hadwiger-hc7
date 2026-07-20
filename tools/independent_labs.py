#!/usr/bin/env python3
"""Prepare independent, symmetric Codex and Grok research laboratories.

The tool never invokes a provider and never promotes repository changes.  It
freezes one clean commit, then lets either provider independently provision a
standalone writable clone with no remote or shared object store.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import secrets
import shlex
import shutil
import subprocess
import sys
import time
import tomllib
from typing import Any

try:  # `python tools/independent_labs.py`
    import proof_round as proof
except ModuleNotFoundError:  # `python -m tools.independent_labs`
    from tools import proof_round as proof


REPO_ROOT = Path(__file__).resolve().parents[1]
LAB_ROOT = REPO_ROOT / ".cache" / "research" / "labs"
MARKER = ".independent-labs"
MANIFEST = "manifest.json"
PROMPT = ".independent-lab-prompt.md"
GOAL = ".independent-lab-goal.md"
RESULT = ".independent-lab-result.md"
PROVIDERS = ("codex", "grok")
CONFIG_KEYS = {
    "schema_version",
    "id_prefix",
    "brief_file",
    "context_files",
    "max_context_bytes",
    "target",
    "providers",
}
TARGET_KEYS = {"file", "heading", "sha256"}
PROVIDER_KEYS = {"model", "effort"}


class LabError(RuntimeError):
    """A fail-closed independent-lab preparation error."""


def make_lab_id(prefix: str) -> str:
    stamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    return f"{prefix}-independent-{stamp}-{secrets.token_hex(2)}"


def safe_lab_path(lab_id: str) -> Path:
    if not proof.ROUND_ID_RE.fullmatch(lab_id):
        raise LabError("unsafe laboratory id")
    root = LAB_ROOT.resolve()
    path = (LAB_ROOT / lab_id).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise LabError("laboratory path escapes the generated root") from exc
    return path


def load_config(path: Path) -> dict[str, Any]:
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise LabError(f"cannot read independent-lab configuration: {exc}") from exc
    if set(raw) != CONFIG_KEYS:
        raise LabError("independent-lab configuration has missing or unknown top-level keys")
    if raw["schema_version"] != 1:
        raise LabError("unsupported independent-lab schema_version")
    if not isinstance(raw["id_prefix"], str) or not proof.ROUND_ID_RE.fullmatch(
        raw["id_prefix"]
    ):
        raise LabError("id_prefix contains unsafe characters")
    if not isinstance(raw["brief_file"], str):
        raise LabError("brief_file must be a string")
    if type(raw["max_context_bytes"]) is not int or raw["max_context_bytes"] < 1024:
        raise LabError("max_context_bytes must be an integer of at least 1024")
    context = raw["context_files"]
    if not isinstance(context, list) or not context or not all(
        isinstance(item, str) for item in context
    ):
        raise LabError("context_files must be a nonempty string list")
    target = raw["target"]
    if not isinstance(target, dict) or set(target) != TARGET_KEYS or not all(
        isinstance(target[key], str) and target[key] for key in TARGET_KEYS
    ):
        raise LabError("target must contain exactly file, heading, and sha256 strings")
    providers = raw["providers"]
    if not isinstance(providers, dict) or set(providers) != set(PROVIDERS):
        raise LabError("providers must contain exactly codex and grok")
    for provider in PROVIDERS:
        settings = providers[provider]
        if not isinstance(settings, dict) or set(settings) != PROVIDER_KEYS:
            raise LabError(f"providers.{provider} must contain exactly model and effort")
        if not all(isinstance(settings[key], str) and settings[key] for key in PROVIDER_KEYS):
            raise LabError(f"providers.{provider} values must be nonempty strings")
    return raw


def tracked_config(path: Path) -> tuple[str, dict[str, Any]]:
    absolute = path.resolve()
    try:
        relative = absolute.relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise LabError("configuration must be inside the repository") from exc
    proof.resolve_tracked_path(relative)
    return relative, load_config(absolute)


def neutral_prompt(config: dict[str, Any], brief: str, commit: str) -> str:
    context_list = "\n".join(f"- `{path}`" for path in config["context_files"])
    return f"""# Independent primary research task

Work as an independent primary mathematical researcher.  No method, role, or
relationship to another researcher is assigned.  Choose and develop whichever
proof strategy you judge strongest, and use native tools and subagents as
useful.

Use this workspace as the only local research corpus.  Do not seek, inspect, or
infer output from any other research process.  Public web research is permitted
for ordinary mathematical background and primary literature, but not to search
for a solution to this exact target or benchmark.  Record exact sources and
theorem numbers.  Preserve every literal graph-theoretic hypothesis, branch-set
label, colouring condition, and separation order.

The research objective is persistent across turns.  Read and maintain
`{GOAL}` as the live objective and evidence log.  An unresolved inference is a
checkpoint, not by itself a reason to stop.  Use native web tools, subagents,
retained verifiers, and Python experiments when they can test a concrete
mechanism.  Use `.venv/bin/python` when the laboratory runtime has been
prepared.  Keep every nontrivial new experiment script and record its command,
output, and exact finite scope.

Before returning `no_result`, complete every evidence gate in `{GOAL}` with
specific references.  In particular, read the full frozen context, investigate
relevant primary literature, test at least two materially different proof
mechanisms, perform a targeted computational or adversarial test (or prove why
no such test can distinguish the live inference), and cold-audit the strongest
candidate.  Do not mark a gate complete with a generic summary.  A complete
proof, a full-hypothesis counterexample, or a proved unbounded strict reduction
is substantive; an unproved intermediate lemma or another finite residue is not.

First read `AGENTS.md`, `RESEARCH_LEDGER.md`, `active/INDEX.md`, the frozen
brief below, and every listed context file.  Work from frozen commit `{commit}`.
You may edit and commit inside this disposable clone, which has no remote.  At
the end, write a self-contained account of the result, exact proof status, and
first unresolved inference (if any) to `{RESULT}`.  Do not alter authoritative
status documents unless a claim is genuinely proved and separately audited.

## Frozen brief

{brief.rstrip()}

## Frozen context files

{context_list}
"""


def persistent_goal(config: dict[str, Any], commit: str) -> str:
    target = config["target"]
    return f"""# Persistent independent research goal

**Status:** active
**Frozen commit:** `{commit}`
**Target:** `{target["file"]}` — `{target["heading"]}`

## Objective

Resolve the exact frozen target by a complete proof, a full-hypothesis
counterexample, or a proved unbounded strict reduction with a well-founded
host-level parameter and an explicit induction back to the target.

## Evidence gates required before `no_result`

- [ ] Read `AGENTS.md`, the authoritative status/navigation documents, the
      frozen brief, and every frozen context file completely.
- [ ] Search relevant primary literature and record exact citations and what
      each result does or does not supply. Do not search for a solution to the
      exact target or benchmark.
- [ ] Develop and test at least two materially different proof mechanisms.
- [ ] Run a targeted Python/computational or adversarial experiment, retaining
      every nontrivial new script and its invocation/output; or give a rigorous
      reason computation cannot distinguish the live inference.
- [ ] Cold-audit the strongest candidate against every literal hypothesis,
      branch-set label, colouring condition, and separation order.
- [ ] State the first unresolved inference and explain, with concrete evidence,
      why another research cycle would repeat rather than advance the work.

## Research log

Record each mechanism, experiment, literature connection, failure certificate,
and pivot here while working. Update `Status` to `complete` only for a proved
allowed outcome, or to `exhausted` only after every evidence gate above is
honestly complete.
"""


def add_local_excludes(workspace: Path) -> None:
    exclude = workspace / ".git" / "info" / "exclude"
    existing = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    additions = [
        name for name in (PROMPT, GOAL, RESULT) if name not in existing.splitlines()
    ]
    if additions:
        with exclude.open("a", encoding="utf-8") as handle:
            if existing and not existing.endswith("\n"):
                handle.write("\n")
            handle.write("\n".join(additions) + "\n")


def verify_clone(workspace: Path, commit: str, branch: str) -> None:
    if not (workspace / ".git").is_dir():
        raise LabError("laboratory workspace is not a standalone clone")
    if proof.run_git(["rev-parse", "HEAD"], cwd=workspace) != commit:
        raise LabError("laboratory workspace is not at the frozen commit")
    if proof.run_git(["branch", "--show-current"], cwd=workspace) != branch:
        raise LabError("laboratory workspace is on the wrong local branch")
    if proof.run_git(["remote"], cwd=workspace):
        raise LabError("laboratory workspace unexpectedly has a Git remote")
    alternates = workspace / ".git" / "objects" / "info" / "alternates"
    if alternates.exists():
        raise LabError("laboratory workspace unexpectedly shares Git objects")
    git_file = workspace / ".git"
    if git_file.is_file():
        raise LabError("laboratory workspace unexpectedly uses shared worktree metadata")
    if proof.run_git(["status", "--porcelain=v1", "--untracked-files=all"], cwd=workspace):
        raise LabError("prepared laboratory workspace is not clean")


def prepare(config_path: Path, requested_id: str | None) -> str:
    proof.ensure_clean_repository()
    config_relative, config = tracked_config(config_path)
    commit = proof.run_git(["rev-parse", "--verify", "HEAD^{commit}"])
    if len(commit) != 40:
        raise LabError("could not freeze a full Git commit id")

    target = proof.resolve_tracked_path(config["target"]["file"], commit=commit)
    subtree = proof.extract_heading_subtree(
        target.read_text(encoding="utf-8"), config["target"]["heading"]
    )
    target_hash = proof.sha256_bytes(subtree.encode("utf-8"))
    if target_hash != config["target"]["sha256"]:
        raise LabError("target heading hash drifted")
    brief_path = proof.resolve_tracked_path(config["brief_file"], commit=commit)
    brief = brief_path.read_text(encoding="utf-8")
    _, context_records = proof.build_context(config, commit)
    prompt = neutral_prompt(config, brief, commit)
    prompt_hash = proof.sha256_bytes(prompt.encode("utf-8"))
    goal = persistent_goal(config, commit)
    goal_hash = proof.sha256_bytes(goal.encode("utf-8"))

    lab_id = requested_id or make_lab_id(config["id_prefix"])
    root = safe_lab_path(lab_id)
    if root.exists():
        raise LabError(f"laboratory pair already exists: {lab_id}")
    root.mkdir(parents=True)
    (root / MARKER).write_text("independent-labs-v1\n", encoding="utf-8")
    (root / "prompt.md").write_text(prompt, encoding="utf-8")
    (root / "goal.md").write_text(goal, encoding="utf-8")
    proof.write_json(
        root / MANIFEST,
        {
            "schema_version": 1,
            "lab_id": lab_id,
            "base_commit": commit,
            "config_path": config_relative,
            "config_sha256": proof.sha256_file(config_path.resolve()),
            "brief_path": config["brief_file"],
            "brief_sha256": proof.sha256_file(brief_path),
            "target": {
                "file": config["target"]["file"],
                "heading": config["target"]["heading"],
                "sha256": target_hash,
            },
            "context": context_records,
            "prompt_sha256": prompt_hash,
            "goal_sha256": goal_hash,
            "provider_settings": config["providers"],
            "lanes": {},
        },
    )
    return lab_id


def provision(lab_id: str, provider: str) -> None:
    if provider not in PROVIDERS:
        raise LabError(f"unsupported provider: {provider}")
    root = safe_lab_path(lab_id)
    with proof.round_lock(root):
        root, manifest = load_lab(lab_id)
        if provider in manifest["lanes"]:
            raise LabError(f"{provider} laboratory is already provisioned")
        lane = root / provider
        if lane.exists():
            raise LabError(f"unclassified path already occupies the {provider} laboratory")
        workspace = lane / "workspace"
        try:
            proof.clone_at_commit(workspace, manifest["base_commit"])
            branch = f"experiment/{lab_id}-{provider}"
            proof.run_git(["switch", "--quiet", "-c", branch], cwd=workspace)
            add_local_excludes(workspace)
            prompt = (root / "prompt.md").read_bytes()
            if proof.sha256_bytes(prompt) != manifest["prompt_sha256"]:
                raise LabError("frozen neutral prompt has drifted")
            (workspace / PROMPT).write_bytes(prompt)
            goal_path = root / "goal.md"
            if goal_path.exists():
                goal = goal_path.read_bytes()
                if proof.sha256_bytes(goal) != manifest.get("goal_sha256"):
                    raise LabError("frozen persistent goal has drifted")
                (workspace / GOAL).write_bytes(goal)
            verify_clone(workspace, manifest["base_commit"], branch)
            manifest["lanes"][provider] = {
                "branch": branch,
                "prompt_sha256": proof.sha256_file(workspace / PROMPT),
                "workspace": f"{provider}/workspace",
            }
            proof.write_json(root / MANIFEST, manifest)
        except Exception:
            shutil.rmtree(lane, ignore_errors=True)
            raise


def load_lab(lab_id: str) -> tuple[Path, dict[str, Any]]:
    root = safe_lab_path(lab_id)
    marker = root / MARKER
    if not root.is_dir() or not marker.is_file():
        raise LabError("independent laboratory pair is missing its marker")
    if marker.read_text(encoding="utf-8") != "independent-labs-v1\n":
        raise LabError("independent laboratory marker is invalid")
    try:
        manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LabError("independent laboratory manifest is invalid") from exc
    if manifest.get("lab_id") != lab_id:
        raise LabError("independent laboratory manifest has the wrong id")
    return root, manifest


def provider_command(
    provider: str,
    workspace: Path,
    settings: dict[str, Any],
    *,
    goal_enabled: bool = True,
) -> list[str]:
    if goal_enabled:
        instruction = (
            f"Read {PROMPT} and {GOAL} completely. Pursue the persistent goal and "
            "carry out the evidence-gated research protocol."
        )
    else:
        instruction = f"Read {PROMPT} completely and carry out the research task."
    model = settings.get("model", "")
    if provider == "codex":
        command = ["codex", "-C", str(workspace), "--sandbox", "workspace-write"]
        if model:
            command.extend(["--model", model])
        if settings.get("effort"):
            command.extend(
                ["--config", f'model_reasoning_effort="{settings["effort"]}"']
            )
        command.append(instruction)
        return command
    if provider == "grok":
        command = [
            "grok",
            "--cwd",
            str(workspace),
            "--no-memory",
            "--sandbox",
            "strict",
        ]
        if model:
            command.extend(["--model", model])
        if settings.get("effort"):
            command.extend(["--reasoning-effort", settings["effort"]])
        command.append(instruction)
        return command
    raise LabError(f"unsupported provider: {provider}")


def selected_providers(provider: str | None) -> tuple[str, ...]:
    if provider is None:
        return PROVIDERS
    if provider not in PROVIDERS:
        raise LabError(f"unsupported provider: {provider}")
    return (provider,)


def show_commands(lab_id: str, provider: str | None) -> None:
    root, manifest = load_lab(lab_id)
    for name in selected_providers(provider):
        if name not in manifest["lanes"]:
            print(f"{name}: not provisioned")
            continue
        workspace = root / manifest["lanes"][name]["workspace"]
        command = provider_command(
            name,
            workspace,
            manifest["provider_settings"].get(name, {}),
            goal_enabled=(workspace / GOAL).exists(),
        )
        print(f"{name.upper()}\n  {shlex.join(command)}\n")


def show_status(lab_id: str) -> None:
    root, manifest = load_lab(lab_id)
    print(f"Laboratory pair: {lab_id}")
    print(f"Frozen commit: {manifest['base_commit']}")
    print(f"Prompt SHA-256: {manifest['prompt_sha256']}")
    for provider in PROVIDERS:
        if provider not in manifest["lanes"]:
            print(f"{provider}: not provisioned")
            continue
        lane = manifest["lanes"][provider]
        workspace = root / lane["workspace"]
        head = proof.run_git(["rev-parse", "HEAD"], cwd=workspace)
        branch = proof.run_git(["branch", "--show-current"], cwd=workspace)
        status = proof.run_git(
            ["status", "--porcelain=v1", "--untracked-files=all"], cwd=workspace
        )
        result = workspace / RESULT
        goal = workspace / GOAL
        goal_status = "legacy"
        completed = 0
        total = 0
        print(f"{provider}: branch={branch} head={head}")
        print(f"  workspace: {workspace}")
        print(f"  status: {'modified' if status else 'clean'}")
        if goal.exists():
            goal_text = goal.read_text(encoding="utf-8")
            completed = goal_text.count("- [x]") + goal_text.count("- [X]")
            total = completed + goal_text.count("- [ ]")
            goal_status = next(
                (
                    line.removeprefix("**Status:**").strip()
                    for line in goal_text.splitlines()
                    if line.startswith("**Status:**")
                ),
                "unknown",
            )
            print(f"  goal: {goal_status} ({completed}/{total} evidence gates)")
        else:
            print("  goal: legacy laboratory without a persistent goal")
        result_status = str(result) if result.exists() else "not written"
        if result.exists() and goal.exists():
            result_text = result.read_text(encoding="utf-8")
            if "`no_result`" in result_text[:2000] and (
                goal_status != "exhausted" or completed != total
            ):
                result_status += " (premature no_result: evidence gates incomplete)"
        print(f"  result: {result_status}")


def show_goal(lab_id: str, provider: str) -> None:
    root, manifest = load_lab(lab_id)
    if provider not in manifest["lanes"]:
        raise LabError(f"{provider} laboratory is not provisioned")
    goal = root / manifest["lanes"][provider]["workspace"] / GOAL
    if not goal.exists():
        raise LabError("laboratory has no persistent goal file")
    print(goal.read_text(encoding="utf-8"), end="")


def setup_runtime(lab_id: str, provider: str) -> None:
    root, manifest = load_lab(lab_id)
    if provider not in manifest["lanes"]:
        raise LabError(f"{provider} laboratory is not provisioned")
    workspace = root / manifest["lanes"][provider]["workspace"]
    runtime = workspace / ".venv"
    requirements = workspace / "tools" / "requirements-verifiers.txt"
    try:
        subprocess.run(
            [sys.executable, "-m", "venv", str(runtime)],
            cwd=workspace,
            check=True,
        )
        subprocess.run(
            [
                str(runtime / "bin" / "python"),
                "-m",
                "pip",
                "install",
                "-r",
                str(requirements),
            ],
            cwd=workspace,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise LabError(f"could not prepare {provider} Python runtime") from exc
    print(runtime)


def cleanup(lab_id: str) -> None:
    root, _ = load_lab(lab_id)
    if root.parent != LAB_ROOT.resolve():
        raise LabError("refusing cleanup outside the generated laboratory root")
    shutil.rmtree(root)
    print(f"Removed independent laboratory pair {lab_id}")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    prepare_parser = commands.add_parser("prepare", help="freeze the shared independent task")
    prepare_parser.add_argument("config", type=Path)
    prepare_parser.add_argument("--lab-id")
    provision_parser = commands.add_parser("provision", help="create one independent workspace")
    provision_parser.add_argument("lab_id")
    provision_parser.add_argument("provider", choices=PROVIDERS)
    commands_parser = commands.add_parser("commands", help="print native provider launch commands")
    commands_parser.add_argument("lab_id")
    commands_parser.add_argument("provider", nargs="?", choices=PROVIDERS)
    status_parser = commands.add_parser("status", help="inspect both independent workspaces")
    status_parser.add_argument("lab_id")
    goal_parser = commands.add_parser("goal", help="show one provider's persistent goal")
    goal_parser.add_argument("lab_id")
    goal_parser.add_argument("provider", choices=PROVIDERS)
    runtime_parser = commands.add_parser(
        "runtime", help="prepare one provider's isolated Python environment"
    )
    runtime_parser.add_argument("lab_id")
    runtime_parser.add_argument("provider", choices=PROVIDERS)
    cleanup_parser = commands.add_parser("cleanup", help="remove one marked laboratory pair")
    cleanup_parser.add_argument("lab_id")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "prepare":
            print(prepare(args.config, args.lab_id))
        elif args.command == "provision":
            provision(args.lab_id, args.provider)
        elif args.command == "commands":
            show_commands(args.lab_id, args.provider)
        elif args.command == "status":
            show_status(args.lab_id)
        elif args.command == "goal":
            show_goal(args.lab_id, args.provider)
        elif args.command == "runtime":
            setup_runtime(args.lab_id, args.provider)
        elif args.command == "cleanup":
            cleanup(args.lab_id)
    except (LabError, proof.RoundError) as exc:
        print(f"independent-labs error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
