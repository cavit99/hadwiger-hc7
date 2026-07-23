#!/usr/bin/env python3
"""Exact Rolek--Song--Mader rooted-K4 completion census at degree eight.

Let v be a degree-eight vertex in a 7-contraction-critical graph, let
H=G[N(v)], and let S be an independent triple. Put R=N(v)-S. The contraction
of S union {v} has a six-colouring in which the five vertices of R receive
five distinct colours. For every missing pair of roots, the Rolek--Song
Kempe-chain lemma supplies a bichromatic path with internal vertices outside
N[v].

Choose four roots T contained in R with alpha(H[T])<=2. For each pair of T,
use its literal edge or its supplied bichromatic path. Partition the union of
these six connections by their four colours. Mader's rooted-K4 theorem then
gives a K4 minor rooted at T. Since all internal vertices avoid N[v], this
proves that G has the augmented closed neighbourhood H+v with T completed to
a K4 as a minor.

The census exhausts every order-eight H with alpha(H)=3 and no K4, every
independent triple S, and every four-set T in H-S with alpha(H[T])<=2. It
completes T to K4, adds universal v, and runs the exact K7-minus branch-set
search.
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
            for T in combinations(R,4):
                if any(independent(H,Q) for Q in combinations(T,3)):
                    continue
                state_count+=1; counts['tested_rooted_k4_states']+=1
                J=H.copy(); J.add_edges_from(combinations(T,2))
                J.add_node(8); J.add_edges_from((8,x) for x in range(8))
                model=k7minus_model(J)
                if model is not None:
                    found={'H':graph6(H),'S':list(S),'roots':list(T),
                           'model':encode_model(model,9)}
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
