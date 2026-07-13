"""Record and merge independently rerun kappa-only order-seven shards.

This file imports the frozen worker from k34_c7_kappaonly_parallel.py,
records every graph/status result in JSON, verifies the frozen shard
digests, and then merges the six certificates.
"""

import argparse
import hashlib
import json
import platform
from collections import Counter
from pathlib import Path

import networkx as nx
import z3

import k34_c7_kappaonly_parallel as frozen


SHARD_COUNT = 6
EXPECTED_SOLVER_SHA256 = (
    "aea1de233d30568694208458ea44a415c64f6c7637531c4438299f69b572a5fb"
)
EXPECTED_RUNNER_SHA256 = (
    "36231bad721c4f2ab66c1e92cfbcafc771ffabad66875fdee160dfa0088f0e0a"
)
EXPECTED_GLOBAL_DIGEST = (
    "fe854344e1c75336fa01d6bab426e1456e28a2f59ad46c9315dc82c11e72a946"
)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_paths() -> tuple[Path, Path]:
    runner = Path(frozen.__file__).resolve()
    solver = runner.with_name("k34_c7_sparse_fixed.py")
    assert file_sha256(runner) == EXPECTED_RUNNER_SHA256
    assert file_sha256(solver) == EXPECTED_SOLVER_SHA256
    return runner, solver


def atlas_items() -> list[tuple[int, str]]:
    graphs = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and nx.is_connected(graph)
    ]
    assert len(graphs) == 853
    return [
        (index, nx.to_graph6_bytes(graph, header=False).decode().strip())
        for index, graph in enumerate(graphs)
    ]


def record_digest(records: list[dict]) -> str:
    lines = [f"{record['graph6']}:{record['status']}" for record in records]
    return hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def run_shard(index: int, output: Path) -> None:
    assert 0 <= index < SHARD_COUNT
    runner, solver = frozen_paths()
    items = [item for item in atlas_items() if item[0] % SHARD_COUNT == index]
    records = []
    for position, item in enumerate(items, start=1):
        graph_index, graph6, status, model = frozen.worker(item)
        record = {
            "index": graph_index,
            "graph6": graph6,
            "status": status,
        }
        if status == "sat":
            record["model"] = model
        records.append(record)
        if position % 20 == 0 or position == len(items):
            print(
                "shard",
                index,
                "progress",
                position,
                "/",
                len(items),
                Counter(record["status"] for record in records),
                flush=True,
            )

    counts = Counter(record["status"] for record in records)
    digest = record_digest(records)
    expected_count = frozen.EXPECTED_SHARD_COUNTS[index]
    assert len(records) == expected_count
    assert counts == Counter({"unsat": expected_count})
    assert digest == frozen.EXPECTED_SHARD_DIGESTS[index]

    payload = {
        "format": "k34-c7-kappaonly-shard-v1",
        "certified": True,
        "shard_index": index,
        "shard_count": SHARD_COUNT,
        "atlas_connected_order7_count": 853,
        "record_count": len(records),
        "counts": dict(counts),
        "graph_id_status_sha256": digest,
        "expected_graph_id_status_sha256": frozen.EXPECTED_SHARD_DIGESTS[index],
        "frozen_runner": str(runner),
        "frozen_runner_sha256": file_sha256(runner),
        "frozen_solver": str(solver),
        "frozen_solver_sha256": file_sha256(solver),
        "python": platform.python_version(),
        "networkx": nx.__version__,
        "z3": z3.get_version_string(),
        "records": records,
    }
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("wrote certified shard", index, output, digest, flush=True)


def merge(inputs: list[Path], output: Path) -> None:
    runner, solver = frozen_paths()
    assert len(inputs) == SHARD_COUNT
    payloads = [json.loads(path.read_text(encoding="utf-8")) for path in inputs]
    assert {payload["shard_index"] for payload in payloads} == set(range(SHARD_COUNT))

    records = []
    shard_files = []
    for path, payload in zip(inputs, payloads, strict=True):
        shard = payload["shard_index"]
        assert payload["format"] == "k34-c7-kappaonly-shard-v1"
        assert payload["certified"] is True
        assert payload["shard_count"] == SHARD_COUNT
        assert payload["frozen_runner_sha256"] == EXPECTED_RUNNER_SHA256
        assert payload["frozen_solver_sha256"] == EXPECTED_SOLVER_SHA256
        assert payload["record_count"] == frozen.EXPECTED_SHARD_COUNTS[shard]
        assert payload["counts"] == {"unsat": payload["record_count"]}
        assert record_digest(payload["records"]) == frozen.EXPECTED_SHARD_DIGESTS[shard]
        records.extend(payload["records"])
        shard_files.append(
            {
                "path": str(path),
                "sha256": file_sha256(path),
                "shard_index": shard,
            }
        )

    records.sort(key=lambda record: record["index"])
    assert len(records) == 853
    assert [record["index"] for record in records] == list(range(853))
    expected_items = atlas_items()
    assert [
        (record["index"], record["graph6"]) for record in records
    ] == expected_items
    assert all(record["status"] == "unsat" for record in records)
    digest = record_digest(records)
    assert digest == EXPECTED_GLOBAL_DIGEST

    merged = {
        "format": "k34-c7-kappaonly-merged-v1",
        "certified": True,
        "atlas_connected_order7_count": 853,
        "record_count": len(records),
        "counts": {"unsat": 853},
        "graph_id_status_sha256": digest,
        "expected_graph_id_status_sha256": EXPECTED_GLOBAL_DIGEST,
        "frozen_runner": str(runner),
        "frozen_runner_sha256": file_sha256(runner),
        "frozen_solver": str(solver),
        "frozen_solver_sha256": file_sha256(solver),
        "shard_files": sorted(
            shard_files, key=lambda item: item["shard_index"]
        ),
        "records": records,
    }
    output.write_text(
        json.dumps(merged, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("wrote merged certificate", output, digest, flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    shard_parser = subparsers.add_parser("shard")
    shard_parser.add_argument("--index", type=int, required=True)
    shard_parser.add_argument("--output", type=Path, required=True)
    merge_parser = subparsers.add_parser("merge")
    merge_parser.add_argument("--inputs", type=Path, nargs=SHARD_COUNT, required=True)
    merge_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "shard":
        run_shard(args.index, args.output)
    else:
        merge(args.inputs, args.output)


if __name__ == "__main__":
    main()
