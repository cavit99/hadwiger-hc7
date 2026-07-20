# Independent audit: three-portal connectivity barrier

**Audit status:** separate internal mathematical and computational audit;
**GREEN**.

**Audited source:**
[`hc7_three_portal_connectivity_barrier.md`](hc7_three_portal_connectivity_barrier.md)

**Audited source SHA-256:**
`ee1de236ec4ec439916b6c67111b7d1aea922551081b4bfff74d0a93c92016de`

After this audit, the source status was changed only to record the GREEN
verdict and link to this file.  No construction, refuted statement, proof,
scope, verifier invocation, or trust boundary changed.  The resulting
promoted source SHA-256 is
`0688fa076c81a10f7c52d9f837e0bb5e6dccd01e791e1184ed71741f2bd6ec1e`.

**Audited verifier:**
[`hc7_three_portal_connectivity_barrier_verify.py`](hc7_three_portal_connectivity_barrier_verify.py)

**Audited verifier SHA-256:**
`3bf307e2015be084e53e39d83ea9fce2eda54f26e4eee1b803add53218355556`

The verifier changed only by removal of a trailing blank line; its executable
content is unchanged.

This is an internal audit, not external peer review.  The example is a
barrier to a connectivity-only intermediate assertion, not a counterexample
to `HC_7`.

## Verdict

The construction and the claimed scope are correct.  It is an exact
order-eight separation of an eight-connected graph, the selected component
is three-connected and full to the boundary, and the required disjoint
path/three-portal-tree packing does not exist.

The example deliberately fails the central `HC_7` hypotheses.  In fact, an
explicit `K_8`-minor model is recorded below.  Thus the barrier proves that
connectivity and portal fullness alone cannot replace `K_7`-minor exclusion
and the operation-specific proper-minor colouring response.

## 1. Construction and boundary data

The verifier constructs exactly 15 vertices and 70 edges.  The induced
boundary is the complete tripartite graph with parts `{d,e}`, `X`, and `Y`.
Consequently `d,e` are nonadjacent, `X` and `Y` are independent, both roots
meet both classes, and every `X`--`Y` edge is present.

Deleting `S` leaves precisely two components:

- the wheel `Q=q_4\vee(q_0q_1q_2q_3q_0)`; and
- the edge `R=r_0r_1`.

There are no `Q`--`R` edges.  The displayed portal table is reproduced
exactly by the adjacency construction, and both components have a neighbour
at every literal boundary vertex.  NetworkX independently reports
`kappa(Q)=3`.

## 2. Exact connectivity

The verifier enumerates every vertex-deletion set of order zero through
seven.  There are

\[
                         \sum_{i=0}^{7}\binom{15}{i}=16384
\]

such sets, and every resulting graph is connected.  Deleting the eight-set
`S` leaves the two components `Q,R`.  Hence `kappa(G)=8`, and in particular
the graph has no actual separation of order seven.

There is also a short structural check behind the enumeration.  The four
boundary vertices `x_3,y_1,y_2,y_3` are complete to `Q`.  For every nonempty
`A subseteq V(Q)`, those four vertices, the distinct private labels of the
rim vertices in `A`, and `N_Q(A)-A` give at least eight distinct neighbours
of `A`.  The edge `R` joins all surviving boundary vertices unless both its
ends are deleted; in that exceptional case at least three boundary vertices
survive, and either the complete tripartite boundary or the intact wheel
joins them.  Thus the exhaustive connectivity value is consistent with the
literal construction rather than an artefact of a quotient encoding.

## 3. Exact absence of the packing

The root portal sets are the distinct singletons `{q_0}` and `{q_2}`.  Any
connected subgraph meeting the three `X`-portal sets contains `q_1,q_3`.
If it is disjoint from a root path, it avoids `q_0,q_2`; the only remaining
way to connect `q_1` to `q_3` in the wheel uses the hub `q_4`.  Removing
`q_1,q_3,q_4` leaves `q_0,q_2` isolated and nonadjacent, so no root path can
remain.

The verifier checks the equivalent finite condition independently: it
enumerates every connected vertex set in `Q` containing the two root
portals and every disjoint connected vertex set meeting all three `X`
portal sets.  No pair exists.  Using connected root supports is exact,
because every connected support containing the two distinct root portals
contains a nontrivial path between them.

The audited command was

```text
PYTHONPATH=active/runtime/deps python3 barriers/hc7_three_portal_connectivity_barrier_verify.py
```

and produced exactly

```text
GREEN portal path/three-set-tree connectivity barrier
G: vertices=15 edges=70 connectivity=8 cuts_tested=16384
G-S: two connected S-full components of orders 5 and 2
Q: W5 connectivity=3; exhaustive packing witness: none
connected-support pairs checked=12
scope: no K7-minor-free or contraction-critical claim
```

## 4. Minor-exclusion trust boundary

The host is not merely unverified for `K_7`-minor exclusion; it contains the
following explicit `K_8`-minor model:

\[
\begin{array}{llll}
 \{q_1,x_3\},&\{x_1\},&\{d,r_1\},&\{q_4,y_2\},\\
 \{q_2,y_3\},&\{e\},&\{y_1\},&\{q_0,q_3,r_0,x_2\}.
\end{array}
\]

These eight sets are pairwise disjoint and connected; direct inspection of
the construction gives an edge between every pair.  This model was also
checked mechanically during the audit.

Therefore the barrier refutes only the assertion stated in its source.  It
does not refute a theorem using any of:

- global `K_7`-minor exclusion;
- seven-chromaticity or six-colourability of every proper minor;
- an operation-specific boundary equality response; or
- the inherited five labelled branch sets of the active `HC_7` reduction.

Within this exact scope, no mathematical or computational gap was found.
