#!/usr/bin/env python3
"""Exact local census for degree-eight neighbourhoods with alpha<=2.

For every order-eight H with alpha(H)<=2 and no K4, add a universal vertex v
and test exactly for a K7-minus minor.  The known Rolek--Song--Thomas
classification says every edge-minimal such H contains the exceptional H8;
this census checks whether K7-minus exclusion already eliminates the regime
without any outside Kempe paths.
"""

from __future__ import annotations
from collections import Counter
from itertools import combinations
import json,sys
import networkx as nx
from hc7_degree8_alpha3_virtual_edge_census import graph6,has_k4,independent,k7minus_model,encode_model

def main():
    c=Counter(); survivors=[]; certs=[]
    for raw in sys.stdin:
        raw=raw.strip()
        if not raw or raw.startswith('>>'): continue
        H=nx.from_graph6_bytes(raw.encode()); H=nx.convert_node_labels_to_integers(H,ordering='sorted')
        c['graphs']+=1
        if any(independent(H,T) for T in combinations(range(8),3)): continue
        c['alpha_at_most_two']+=1
        if has_k4(H): c['k4_positive']+=1; continue
        c['k4_free']+=1
        J=H.copy(); J.add_node(8); J.add_edges_from((8,x) for x in range(8))
        model=k7minus_model(J)
        if model is None:
            c['survivors']+=1
            survivors.append({'H':graph6(H),'edges':H.number_of_edges(),
                              'degree_sequence':sorted(dict(H.degree()).values()),
                              'complement_edges':nx.complement(H).number_of_edges()})
        else:
            c['local_positive']+=1
            if len(certs)<30: certs.append({'H':graph6(H),'model':encode_model(model,9)})
    print(json.dumps({'counts':dict(sorted(c.items())),'survivors':survivors,'sample_certificates':certs},sort_keys=True))
if __name__=='__main__': main()
