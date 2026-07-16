# Independent audit: a connector between the unmatched `2+2` paths

## Audit identity

- theorem file:
  `results/hc7_disjoint_k6minus_support6_two_two_connector.md`
- audited theorem SHA-256:
  `767781e0b27d73d6a8d353cf08a032c4a46006c92c3a96fd193752816c221588`

## Verdict

**GREEN.**  Theorem 2.1 gives seven nonempty, connected, pairwise disjoint
branch sets and all twenty-one required adjacencies under exactly the
normalized `2+2` hypotheses stated in the theorem.  The construction also
works when the added path has one edge, or when either of its ends is an end
of the corresponding linkage path.  No unlisted support edge or hidden
path-disjointness assumption is used.

This is a separate internal mathematical audit, not external peer review.
No mathematical source content was changed during the audit.  After the
audit, only the theorem's status line and repository-relative source link
were updated for promotion from `active/` to `results/`; the hash above is
the resulting promoted revision.

The companion extraction barrier was checked separately and is GREEN at the
corrected revision recorded in Section 4.  The connector theorem does not
depend on that barrier.

## 1. Disjointness and connectivity

Write

```text
L = V(P_0) union V(R-v),
M = V(P_5),
W = {a_1,a_2,a_3,x}
    union V(P_1-b_0) union V(P_2-b_1)
    union V(P_3-b_2) union V(P_4-r).
```

All three sets are nonempty.  The path `R-v` meets `P_0` exactly at its end
`u`, so `L` is connected.  The set `M` is a path.  The vertices
`a_1,a_2,a_3` lie in the clique `Q`, the edge `a_1x` joins `x` to that
clique, and each truncated path in `W` contains its displayed left end.
Thus `W` is connected.

The six linkage paths are pairwise vertex-disjoint.  Every internal vertex
of `R` avoids all six paths and `A union B`; its only contacts with the
linkage skeleton are the prescribed ends `u` and `v`.  Deleting `v` from
`R` therefore leaves `L` disjoint from `M`.  The left ends used in `L`,
`M`, and `W` are respectively `a_0`, `y`, and
`a_1,a_2,a_3,x`, so these three sets are pairwise disjoint.  Truncating the
four paths in `W` deletes `b_0,b_1,b_2,r`, and neither `L` nor `M` contains
those vertices.  Hence

```text
L, M, W, {b_0}, {b_1}, {b_2}, {r}
```

are seven nonempty, connected, pairwise disjoint sets.

## 2. The twenty-one adjacencies

The three adjacencies among `L,M,W` are:

| pair | witnessing edge |
|---|---|
| `L,M` | the last edge of `R` incident with `v` |
| `L,W` | `a_0a_1` |
| `M,W` | `yx` |

The first witness remains valid when `R=uv`: then `R-v={u}` and the edge
`uv` joins `L` to `M`.  It is also valid when `u` or `v` is an end of its
linkage path.

The set `L` contains `p`, while `M` contains `q`.  Since `B` is complete
except possibly for `pq`, both sets are adjacent to every singleton among
`b_0,b_1,b_2,r`; the possibly absent edge is never needed.  The final
edges of `P_1,P_2,P_3,P_4` join `W` respectively to
`b_0,b_1,b_2,r`.  Finally those four singleton vertices form a clique in
`B`.  These witnesses account for all eighteen remaining pairs, so the
displayed sets form a `K_7`-minor model.

## 3. Exact scope

The proof assumes an additional path whose internal vertices avoid
`A union B` **and all six linkage paths**.  It does not show that every
six-terminal crossing contains such a path.  It also does not prove either
the six-terminal crossing theorem, the support-six transversal theorem, or
`HC_7`.

## 4. Companion-barrier audit

The file
`barriers/hc7_two_two_three_pattern_extraction_barrier.md`, at SHA-256
`c6af8ab0f97df11cea0cc25f0f7c4efae0955193cba4309b003b9b9f6db39dd7`,
is **GREEN** as a counterexample to the corrected extraction claim.  Here
the optional edge `pq` is absent, as required by and implicit in the
displayed assertion that there is no linkage-clean `P_0`--`P_5` edge.

The paths `a_0-u-y` and `a_1-v-q` are vertex-disjoint `T`-paths with
endpoint positions `(0,2)` and `(1,3)`, hence form a genuine `T`-crossing.
Every vertex of the completed graph belongs to `A union B` or to one of the
six linkage paths.  Since a linkage-clean path has no internal vertex in
that union, every such path in this graph is a single edge.  The relevant
edges are exactly

```text
P_0--P_1: a_0a_1, a_0u, pb_0;
P_1--P_5: uy, vq, b_0q;
P_0--P_5: none.
```

Among the first two rows, every pair with four distinct ends has the same
attachment order on the two oriented paths.  Thus none of the connector or
two opposite-order alternatives occurs.  In particular, the formerly
problematic path

```text
a_0 -- a_2 -- P_2 -- b_1 -- q
```

is correctly excluded: its internal vertices use both support vertices and
another linkage path, so it is not linkage-clean.

Finally, the seven sets in (3.1) are nonempty, connected, and pairwise
disjoint.  The five singleton sets form a clique in `B-p`; the two large
sets are connected respectively by `a_0p,a_0u,uy` and by
`a_1v` together with the clique `Q` and `a_1x`, and they are adjacent along
`uv`.  The first large set reaches the five singletons through the edges
from `p` to `b_0,b_1,b_2,r` and through `yq`; the second reaches them through
`vb_0,a_2b_1,a_3b_2,xr,vq`.  Hence (3.1) is a valid explicit `K_7`-minor
model.  The example therefore refutes only the three-pattern extraction,
not the desired six-terminal minor conclusion.
