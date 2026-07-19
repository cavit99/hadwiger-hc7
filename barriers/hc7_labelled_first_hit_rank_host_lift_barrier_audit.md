# Independent audit of the first-hit rank host-lift barrier

**Audit status:** separate internal audit.

**Audited source:**
`barriers/hc7_labelled_first_hit_rank_host_lift_barrier.md`

**Audited source SHA-256:**
`407b24ef9ed70479b6668f6474107a1d550c910e2f67494fd1e06fe7bcbf9ad0`

## Verdict

**GREEN.**  The displayed graph is seven-connected, the two selected
terminal labels have clean-linkage rank one with minimum directed Menger
set `{z}`, and the source-side component has literal host boundary of order
eight.  It therefore refutes the claimed inference from a small relative
Rado--Menger certificate to a host separator of order at most seven when no
unused-label exposure bound is assumed.

The construction contains a large clique.  It is not `K_7`-minor-free and
is not contraction-critical, exactly as the source records.

## 1. Construction and connectivity

The sets `P` and `U` have orders eight and seven.  The graph contains the
clique on `P union U`, the clique on `U union {a,b}`, and a vertex `z`
complete to `P union {a,b}` and anticomplete to `U`.  No edge joins `P`
directly to `{a,b}`.

After deleting at most six vertices, at least one vertex of each of `P`
and `U` remains.  The surviving part of `P union U` is a connected clique.
Every surviving one of `a,b` meets every surviving vertex of `U`, and a
surviving `z` meets every surviving vertex of `P`.  Thus the remaining
graph is connected.  This proves seven-connectivity, including deletions
which contain some or all of `{a,b,z}`.

## 2. Clean-linkage rank

The terminal union is `U union {a,b}`.  After it is excluded from path
interiors, the nonterminal host is induced by `P union {z}`.  The only
nonterminal neighbour of either selected terminal `a` or `b` is `z`.
Accordingly, in the correctly sink-oriented network, every directed path
from `P` to `hat(a)` or `hat(b)` contains `z`.  At least one such path
exists, for example `p_1,z,hat(a)`.  Hence

\[
                    r_P(T_1\cup T_2)=1,
\]

and `{z}` is a minimum Menger set.  Two disjoint paths cannot serve the
two selected labels.

## 3. Failure of the host lift

Deleting `z` does not separate the original graph: every vertex of `P`
is adjacent to every vertex of `U`, and every vertex of `U` is adjacent to
both `a` and `b`.  The relevant source component in the terminal-avoiding
network has nonterminal vertex set `P`, but in the host

\[
                         N_H(P)=U\cup\{z\}.
\]

This boundary has order eight.  The seven vertices in `U`, belonging to
the three unused terminal labels, are exactly the exposure discarded by
the relative routing network.  Thus the example directly realizes the
high-exposure outcome `e_C=7=8-|Z|` of the audited Rado reduction.

## 4. Scope

The clique `P union U` has order fifteen, so the host contains `K_7` as a
subgraph.  The example consequently does not challenge any theorem which
uses `K_7`-minor exclusion or the proper-minor colourings of a hypothetical
counterexample to bound unused-label exposure.  It does establish that
seven-connectivity, labelled terminal families, and the Rado--Menger rank
defect alone are insufficient.
