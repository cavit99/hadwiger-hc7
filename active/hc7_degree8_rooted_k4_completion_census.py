#!/usr/bin/env python3
"""Exact Rolek--Song rooted-K4 completion census at degree eight.

Let v be a degree-eight vertex in a 7-contraction-critical graph, let
H=G[N(v)], and let S be an independent triple.  Put R=N(v)-S.

Rolek--Song Lemma 2.5 (in the formulation recalled by Lafferty--Song) says
that if x1x2 and y1y2 are two vertex-disjoint literal edges of H[R], then all
four cross edges between {x1,x2} and {y1,y2} may be added simultaneously as a
rooted K4 minor, even though the four Kempe paths need not be pairwise
disjoint.  Thus any K7-minus model in the augmented closed neighbourhood
lifts to the original host.

This script exhausts every order-eight H with alpha(H)=3 and no K4, every
independent triple S, and every pair of disjoint edges in H-S.  It completes
their four endpoints to K4, adds the universal vertex v, and runs the exact
K7-minus branch-set search.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
import sys

import networkx as nx

from hc7_almost_dominating_rooted_k5_census import degree8_exit
from hc7_degree8_alpha3_virtual_edge_census import (
    encode_model,
    graph6,
    has_k4,
    independent,
    k7minus_model,
)


def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument('--survivor-limit',type=int,default=3000); args=parser.parse_args()
    counts=Counter(); survivors=[]; certificates=[]

    for raw in sys.stdin:
        raw=raw.strip()
        if not raw or raw.startswith('>>'): continue
        H=nx.from_graph6_bytes(raw.encode()); H=nx.convert_node_labels_to_integers(H,ordering='sorted')
        if H.number_of_nodes()!=8: raise ValueError('expected order-eight catalogue')
        counts['graphs']+=1
        triples=[S for S in combinations(range(8),3) if independent(H,S)]
        if not triples or any(independent(H,Q) for Q in combinations(range(8),4)): continue
        counts['alpha_three']+=1
        if has_k4(H): counts['k4_positive']+=1; continue
        counts['k4_free']+=1
        if degree8_exit(H) is not None:
            counts['rooted_k5_positive']+=1
            continue
        counts['rooted_k5_survivors']+=1

        found=None; state_count=0
        for S in triples:
            R=sorted(set(range(8))-set(S))
            edges=[tuple(sorted(e)) for e in H.subgraph(R).edges()]
            for e,f in combinations(edges,2):
                if set(e)&set(f): continue
                state_count+=1; counts['tested_rooted_k4_states']+=1
                endpoints=tuple(sorted(set(e)|set(f)))
                J=H.copy(); J.add_edges_from(combinations(endpoints,2))
                J.add_node(8); J.add_edges_from((8,x) for x in range(8))
                model=k7minus_model(J)
                if model is not None:
                    found={'H':graph6(H),'S':list(S),'edges':[list(e),list(f)],
                           'completed':list(endpoints),'model':encode_model(model,9)}
                    break
            if found is not None: break

        if found is None:
            counts['survivors']+=1
            if len(survivors)<args.survivor_limit:
                survivors.append({'H':graph6(H),'edges':H.number_of_edges(),
                                  'degree_sequence':sorted(dict(H.degree()).values()),
                                  'independent_triples':[list(S) for S in triples],
                                  'tested_states':state_count})
        else:
            counts['rooted_k4_positive']+=1
            if len(certificates)<50: certificates.append(found)

    print(json.dumps({'counts':dict(sorted(counts.items())),
                      'survivors_truncated':counts['survivors']>len(survivors),
                      'survivors':survivors,'sample_certificates':certificates},sort_keys=True))

if __name__=='__main__': main()
