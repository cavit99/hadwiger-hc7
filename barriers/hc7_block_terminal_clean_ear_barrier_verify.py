"""Verify the exact block-terminal clean-ear guardrail.

Run with:
  PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_block_terminal_clean_ear_barrier_verify.py
"""

from __future__ import annotations

import networkx as nx


def glued_icosahedral_tube() -> nx.Graph:
    left = nx.icosahedral_graph()
    right = nx.relabel_nodes(nx.icosahedral_graph(), lambda v: v + 100)
    _, emb_left = nx.check_planarity(left)
    _, emb_right = nx.check_planarity(right)
    left_ring = list(emb_left.neighbors_cw_order(0))
    right_ring = list(emb_right.neighbors_cw_order(100))
    left.remove_node(0)
    right.remove_node(100)
    identification = {
        right_ring[i]: left_ring[(-i) % 5] for i in range(5)
    }
    right = nx.relabel_nodes(right, identification)
    return nx.compose(left, right)


def faces(graph: nx.Graph) -> list[list[object]]:
    planar, embedding = nx.check_planarity(graph)
    assert planar
    seen: set[tuple[object, object]] = set()
    answer: list[list[object]] = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            answer.append(embedding.traverse_face(u, v, seen))
    return answer


def cyclic_equal(left: list[object], right: list[object]) -> bool:
    if len(left) != len(right):
        return False
    doubled = left + left
    return any(doubled[i : i + len(right)] == right for i in range(len(left))) or any(
        doubled[i : i + len(right)] == list(reversed(right))
        for i in range(len(left))
    )


def linked(
    graph: nx.Graph, x: object, y: object, q: object, p: object
) -> bool:
    for path in nx.all_simple_paths(graph, x, y):
        if q in path or p in path:
            continue
        remainder = graph.copy()
        remainder.remove_nodes_from(path)
        if q in remainder and p in remainder and nx.has_path(remainder, q, p):
            return True
    return False


tube = glued_icosahedral_tube()
assert nx.check_planarity(tube)[0]
assert nx.node_connectivity(tube) == 5

host = tube.copy()
host.add_edge("a", "b")
for apex in ("a", "b"):
    for vertex in tube:
        host.add_edge(apex, vertex)
assert nx.node_connectivity(host) == 7

carrier = tube.subgraph(set(tube) - {1, 2, 9, 102}).copy()
assert nx.node_connectivity(carrier) == 3
cell = {6}
gate = {3, 4, 5}
assert set(carrier.neighbors(6)) == gate
remainder = carrier.copy()
remainder.remove_nodes_from(gate)
assert cell in [set(component) for component in nx.connected_components(remainder)]

rib = carrier.copy()
rib.remove_node(6)
rib.add_edge(3, 5)  # the sole virtual edge of the facial gate
outer = [3, 10, 7, 8, 106, 103, 109, 5]
assert any(cyclic_equal(face, outer) for face in faces(rib))
assert any(set(face) == gate for face in faces(rib))

x, y = 3, 106
q_block = {10, 7, 8}
p_block = {103, 109, 5}
assert all(
    not linked(carrier, x, y, q, p) for q in q_block for p in p_block
)

# Exhibit the same-vertex web completion explicitly.
web_rib = rib.copy()
for terminal in ("alpha", "beta"):
    web_rib.add_node(terminal)
web_rib.add_edges_from(("alpha", q) for q in q_block)
web_rib.add_edges_from(("beta", p) for p in p_block)
web_rib.add_edges_from(
    [(x, "alpha"), ("alpha", y), (y, "beta"), ("beta", x)]
)
assert nx.check_planarity(web_rib)[0]
assert any(set(face) == gate for face in faces(web_rib))

web = web_rib.copy()
web.add_node(6)
web.add_edges_from((6, vertex) for vertex in gate)
augmented_edges = set(carrier.edges()) | {
    ("alpha", q) for q in q_block
} | {("beta", p) for p in p_block}
assert all(web.has_edge(u, v) for u, v in augmented_edges)

reserved = {1, 2, "a", "b"}
assert set(host.neighbors(6)) == gate | reserved
assert nx.node_connectivity(host) == 7
assert nx.check_planarity(host.subgraph(tube))[0]

print("tube: planar and 5-connected")
print("host: 7-connected; deleting apices a,b leaves the planar tube")
print("carrier: induced, 3-connected, with exact full gate", sorted(gate))
print("all nine block-terminal crosses absent")
print("cell outside-neighbour set:", reserved)
print("no clean gate bypass can avoid the four reserved first neighbours")
