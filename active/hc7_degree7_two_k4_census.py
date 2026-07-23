#!/usr/bin/env python3
"""Exact-one-K4 census at a degree-seven vertex.

For H on seven vertices with alpha(H)<=2 and at most one K4, test the
almost-dominating rooted-K5 exit for every nonedge ab.  If it succeeds, the
U-rooted K5 supplied by the promoted degree-seven theorem, together with v
and the almost-dominating endpoint, gives K7-minus.  Thus a survivor would be
the only local obstruction to proving that every degree-seven vertex lies in
at least two literal K5 subgraphs.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_almost_dominating_rooted_k5_census import degree7_exit
from hc7_degree8_alpha3_virtual_edge_census import graph6, independent


def k4s(H: nx.Graph):
    return [Q for Q in combinations(H.nodes(), 4) if all(H.has_edge(x, y) for x, y in combinations(Q, 2))]


def main() -> None:
    counts=Counter(); survivors=[]; certificates=[]
    for raw in sys.stdin:
        raw=raw.strip()
        if not raw or raw.startswith('>>'): continue
        H=nx.from_graph6_bytes(raw.encode())
        H=nx.convert_node_labels_to_integers(H,ordering='sorted')
        if any(independent(H,T) for T in combinations(H.nodes(),3)): continue
        counts['alpha_at_most_two']+=1
        qs=k4s(H)
        if len(qs)>=2:
            counts['two_k4_positive']+=1
            continue
        counts[f'input_k4_{len(qs)}']+=1
        cert=degree7_exit(H)
        if cert is None:
            counts['survivors']+=1
            survivors.append({'H':graph6(H),'k4s':[list(Q) for Q in qs],
                              'edges':H.number_of_edges(),
                              'degree_sequence':sorted(dict(H.degree()).values())})
        else:
            counts['rooted_k5_exit']+=1
            certificates.append({'H':graph6(H),'k4s':[list(Q) for Q in qs],**cert})
    print(json.dumps({'counts':dict(sorted(counts.items())),
                      'survivors':survivors,
                      'certificates':certificates},sort_keys=True))

if __name__=='__main__': main()
