"""Parallel discovery run for the |C|=7 actual-helper lemma.

This reuses solve_graph from the frozen sparse checker but disables the sparse
edge-count and Dirac-neighbourhood constraints.  What remains is weaker than
full seven-connectivity: only the 127 necessary inequalities |N_G(X)| >= 7
for nonempty X subset C are imposed.  Therefore all-UNSAT would prove the
actual helper lemma under kappa(G)>=7.  Any SAT model must still be checked
for full host connectivity before it is a counterexample.
"""

import argparse
import hashlib

import networkx as nx

from k34_c7_sparse_fixed import solve_graph


EXPECTED_SHARD_COUNTS = (143, 142, 142, 142, 142, 142)
EXPECTED_SHARD_DIGESTS = (
    "88bd85f9d81e547408ee9ccb5a18eb1c3ad9705e183ae2bdc81c3999e07cb136",
    "fe51bf49c4239069592a28b04edbc2c88d96500cfbd200d3fbd12088be9fac68",
    "c2190fb67ce2035a602128e028690a75c39d6bf24d67b26a28e699f059a8c8b5",
    "01ea845a80461d583d95bf23213fb0b8d8344c2832c3092587191b7d4ec834b4",
    "6aef5ce8017afb1120a0bad7c7a67ec334753430b7d11b961d8ec3397b41764c",
    "26383fc75f1e08e833a28eb6da083ec08555e9856a45b9084bbd550f2054e452",
)


def worker(item):
    index, code = item
    graph = nx.from_graph6_bytes(code.encode())
    status, model = solve_graph(
        graph,
        timeout_ms=120_000,
        enforce_sparse=False,
        enforce_dirac=False,
    )
    return index, code, str(status), model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()
    graphs = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and nx.is_connected(graph)
    ]
    items = [
        (i, nx.to_graph6_bytes(graph, header=False).decode().strip())
        for i, graph in enumerate(graphs)
    ]
    shard_items = [item for item in items if item[0] % args.shard_count == args.shard_index]
    results = {}
    for item in shard_items:
        index, code, status, model = worker(item)
        results[index] = (code, status, model)
        counts = {
            key: sum(result[1] == key for result in results.values())
            for key in ("sat", "unsat", "unknown")
        }
        print(index, code, status, len(results), counts, flush=True)
        if status == "sat":
            print("SAT A/B rows", model, flush=True)

    records = [f"{results[i][0]}:{results[i][1]}" for i, _ in shard_items]
    digest = hashlib.sha256(("\n".join(records) + "\n").encode()).hexdigest()
    counts = {
        key: sum(result[1] == key for result in results.values())
        for key in ("sat", "unsat", "unknown")
    }
    print("shard", args.shard_index, "of", args.shard_count, "final counts", counts)
    print("graph-id/status sha256", digest)
    if args.shard_count == 6:
        expected_count = EXPECTED_SHARD_COUNTS[args.shard_index]
        assert len(records) == expected_count
        assert counts == {"sat": 0, "unsat": expected_count, "unknown": 0}
        assert digest == EXPECTED_SHARD_DIGESTS[args.shard_index]
        print("shard certificate verified")


if __name__ == "__main__":
    main()
