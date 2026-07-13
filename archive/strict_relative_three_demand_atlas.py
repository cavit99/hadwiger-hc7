#!/usr/bin/env python3
"""Run the strict-relative three-demand SAT probe on small 3-connected shores."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

import networkx as nx


def main() -> None:
    max_order = int(os.environ.get("MAX_ORDER", "6"))
    script = Path(__file__).with_name("strict_relative_three_demand_search.py")
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if 4 <= len(graph) <= max_order and nx.node_connectivity(graph) >= 3
    ]
    print("three-connected atlas shores", len(graphs), "through order", max_order)
    for index, graph in enumerate(graphs, start=1):
        code = nx.to_graph6_bytes(graph, header=False).strip().decode("ascii")
        environment = dict(os.environ, SHORE_GRAPH6=code)
        result = subprocess.run(
            [sys.executable, str(script)],
            check=True,
            capture_output=True,
            text=True,
            env=environment,
        )
        if "result sat" in result.stdout:
            print("SAT", len(graph), code)
            print(result.stdout)
            return
        if index % 10 == 0:
            print("checked", index)
    print("NO_COUNTEREXAMPLE", len(graphs))


if __name__ == "__main__":
    main()
