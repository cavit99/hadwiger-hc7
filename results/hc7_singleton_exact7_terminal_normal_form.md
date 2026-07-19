# The singleton exact-seven terminal mode

**Status:** written proof and computer-assisted finite classification;
separate internal audit GREEN in
[`hc7_singleton_exact7_terminal_normal_form_audit.md`](hc7_singleton_exact7_terminal_normal_form_audit.md).
This note does not close the singleton mode or prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Let `a` have degree seven, put

\[
 S=N_G(a),\qquad H=G[S],\qquad F=\overline H,
 \qquad C=G-N_G[a],
\tag{1.2}
\]

and assume that `{a},S,C` is the singleton-shore outcome of a generic
exact-seven selected-response interface.  The promoted degree-seven
anti-neighbourhood theorem says that `C` is nonempty and connected.

A connected subgraph of `C` is **boundary-full** when it has a neighbour at
every literal vertex of `S`.  Write `nu(C)` for the maximum number of
pairwise vertex-disjoint boundary-full connected subgraphs of `C`.

## 2. The opposite exterior has full-subgraph packing number one

### Theorem 2.1

\[
                              \nu(C)=1.                 \tag{2.1}
\]

### Proof

The singleton `{a}` is boundary-full.  Apply the exact-seven full-subgraph
packing theorem to the actual separation with open sides `{a}` and `C`.
It gives `nu(C)<=3`.

The connected graph `C` is also boundary-full: its open neighbourhood is
contained in the seven-set `S`, and missing one member of `S` would give a
separator of order at most six between `C` and `a`.  Hence `nu(C)>=1`.

If `nu(C)=3`, the adaptive `(1,3)` reflection theorem gives an explicit
`K_7`-minor model or a six-colouring of `G`, both impossible.

Suppose `nu(C)=2`.  The adaptive `(1,2)` boundary theorem puts `H` in its
audited 129-type residual.  Dirac's neighbourhood-independence inequality
at the degree-seven vertex `a` gives

\[
                             \alpha(H)\le2.              \tag{2.2}
\]

Inside that residual, the audited finite extraction leaves exactly the
Moser spindle and its specified one-edge extension.  The rich open side
`C` is connected, so the one-anchor connected-rich construction in the
adaptive `(1,2)` theorem gives a `K_7` minor for either boundary.  This is
again impossible.  Hence `nu(C)` is neither two nor three.  Equation (2.1)
follows.
\(\square\)

The Moser classification is used only inside the `(1,2)` contradiction.
It is not a classification of the surviving packing-one boundary.

## 3. A cutvertex or bridge returns an exact order-seven interface

### Theorem 3.1 (cutvertex reduction)

If `z` is a cutvertex of `G[C]`, then some component `D` of `C-z` satisfies

\[
       |N_S(D)|=6,\qquad N_G(D)=N_S(D)\mathbin{\dot\cup}\{z\}.       \tag{3.1}
\]

Consequently `N_G(D)` is an actual order-seven full-neighbourhood
separator.  For every edge `zd` with `d in D`, any six-colouring of
`G-zd` makes this separator a generic exact-seven selected-response
interface with operated connected shore `D`, which is a proper subset of
the old exterior `C`.

### Proof

Every component `D` of `C-z` has

\[
                          N_G(D)\subseteq S\cup\{z\}.    \tag{3.2}
\]

It is separated by this set from `a` and from every other component of
`C-z`.  Seven-connectivity therefore gives `|N_S(D)|>=6`.

If every component were adjacent to all seven vertices of `S`, two of
those components would be disjoint boundary-full connected subgraphs,
contrary to Theorem 2.1.  Thus some component has exactly six boundary
neighbours.  Componenthood gives (3.1), and the existence of another
component makes the separation nontrivial.

Choose an edge `zd` entering `D`.  A six-colouring of the proper minor
`G-zd` makes `z,d` monochromatic; otherwise the edge could be restored.
Its restriction to the closed shore opposite `D` is proper.  Its equality
partition on `N_G(D)` cannot extend through the intact `D`-shore, since
the two shore colourings would align by a palette permutation and
six-colour `G`.  Thus it is a generic exact-seven response.  Finally
`D subsetneq C` because `C-z` has another component. \(\square\)

### Corollary 3.2 (bridge reduction)

If `G[C]` has a bridge, an actual order-seven full-neighbourhood separator
with a proper connected side `D subsetneq C` is obtained in the same way.

### Proof

Deleting a bridge divides `C` into two connected sets.  For either side,
its open neighbourhood consists of the opposite bridge endpoint and at
most seven vertices of `S`; seven-connectivity gives at least six boundary
neighbours.  If both sides were boundary-full they would contradict
Theorem 2.1.  Therefore one side has exactly six boundary neighbours, and
the proof of Theorem 3.1 applies. \(\square\)

Hence a survivor with no returned order-seven interface has a
two-connected, nonbipartite exterior of order at least three.  The
nonbipartiteness is the promoted singleton-shore theorem.

## 4. A list-critical separator from a boundary matching

The exact boundary language also gives an unbounded reduction which is
independent of the finite census below.  Fix a matching

\[
                        M=\{e_1,e_2,e_3\}              \tag{4.1}
\]

of order three in `F`.  Colour the ends of each `e_i` alike, use different
colours on the three matching edges, and give the unmatched vertex of `S`
a fourth colour.  For `v in C`, put

\[
 t_M(v)=|\{e\in M:V(e)\subseteq N_S(v)\}|,
 \qquad
 L_M(v)=[6]\setminus c_M(N_S(v)).                      \tag{4.2}
\]

Thus `t_M(v)` records how many repeated boundary colours are counted twice
inside the literal boundary neighbourhood of `v`.

### Theorem 4.1 (matching-list separator)

The graph `C` is not `L_M`-colourable.  Let `K` be an
inclusion-minimal induced subgraph of `C` which is not `L_M`-colourable.
Then `K` is connected and

\[
 d_K(v)\ge |L_M(v)|
          =6-|N_S(v)|+t_M(v)                           \tag{4.3}
\]

for every `v in K`.  Consequently,

\[
        v\in K\quad\Longrightarrow\quad
        t_M(v)\le d_G(v)-6.                            \tag{4.4}
\]

In particular, if some `v in C` satisfies

\[
                         t_M(v)>d_G(v)-6,               \tag{4.5}
\]

then `K` is a proper connected subgraph of `C` and `N_G(K)` is an actual
separator of order at least seven.  If `|N_G(K)|=7`, deleting any edge
from `K` to `N_G(K)` supplies a generic exact-seven selected response with
operated shore `K subsetneq C`.  If `|N_G(K)|>=8`, it supplies an actual
separator with positive excess over seven.

### Proof

The displayed four-colouring of `S` leaves two colours unused on `S`.
If `C` had a proper `L_M`-colouring, it would combine with `c_M` on `S`,
because every colour forbidden at `v in C` is precisely a colour used on
a boundary neighbour of `v`.  The vertex `a` could then receive either
colour unused on `S`; it has no neighbour in `C`.  This would six-colour
`G`, a contradiction.  Hence `C` is not `L_M`-colourable.

Choose `K` inclusion-minimal by its vertex set.  If `K` were disconnected,
one of its components would already be non-`L_M`-colourable, contrary to
minimality.  For `v in K`, minimality gives an `L_M`-colouring of `K-v`.
If `d_K(v)<|L_M(v)|`, one available colour at `v` would extend that
colouring, again a contradiction.  This proves the inequality in (4.3).

Write `k=|N_S(v)|`.  The boundary neighbours of `v` use exactly
`k-t_M(v)` colours: each matching edge counted by `t_M(v)` is the sole
duplication.  This proves the equality in (4.3).  Moreover, `v` has no
neighbour at `a`, so

\[
 d_K(v)\le d_C(v)=d_G(v)-k.
\]

Combining this with (4.3) gives

\[
 d_G(v)-k\ge6-k+t_M(v),
\]

which is (4.4).

If (4.5) holds, that vertex `v` does not belong to `K`, so `K subsetneq C`.
The full open neighbourhood `N_G(K)` separates the nonempty connected set
`K` from `a`; seven-connectivity gives `|N_G(K)|>=7`.

Suppose equality holds and choose an edge `xy` with `x in K` and
`y in N_G(K)`.  Every six-colouring of the proper graph `G-xy` makes
`x,y` monochromatic, since otherwise the edge could be restored.  Its
restriction to the closed shore opposite `K` is proper.  The resulting
equality partition on `N_G(K)` cannot also be induced by a colouring of
the intact `K`-shore: aligning the two palettes would six-colour `G`.
This is the asserted generic exact-seven selected response.  The
positive-excess alternative is immediate when the neighbourhood has order
at least eight. \(\square\)

### Corollary 4.2 (low-degree contact restriction)

Unless the separator outcome of Theorem 4.1 occurs, every order-three
matching `M` of `F` satisfies

\[
 \begin{array}{ll}
 d_G(v)=7 &\Longrightarrow\quad t_M(v)\le1,\\[2mm]
 d_G(v)=8 &\Longrightarrow\quad t_M(v)\le2
 \end{array}                                             \tag{4.6}
\]

for every `v in C`.  Equivalently, no degree-seven exterior vertex sees
both ends of two edges of one order-three complement matching, and no
degree-eight exterior vertex sees all six ends of such a matching.

This is a necessary literal-contact restriction, not a claim that every
pair of disjoint complement edges extends to an order-three matching.

### Proposition 4.3 (the genuine Gallai equality cell)

Use the minimal non-`L_M`-colourable core `K` from Theorem 4.1.  If

\[
                         d_G(v)=6+t_M(v)                \tag{4.7}
\]

for every `v in K`, then `K=C`, every inequality in (4.3) is an equality,
and `C` is a Gallai tree.  In the two-connected survivor of Section 3,
`C` is therefore either a complete graph or an odd cycle.

### Proof

For `v in K`, writing again `k=|N_S(v)|`, hypothesis (4.7) gives

\[
 d_C(v)=d_G(v)-k=6-k+t_M(v)=|L_M(v)|.
\]

Together with

\[
 |L_M(v)|\le d_K(v)\le d_C(v),
\]

this forces equality throughout.  In particular every neighbour of `v`
in `C` belongs to `K`.  Since `K` is nonempty and `C` is connected, this
implies `K=C`.

The connected graph `C` is not colourable from a list assignment whose
list order at every vertex equals its degree.  The
Borodin--Erdos--Rubin--Taylor degree-choosability theorem therefore makes
`C` a Gallai tree: every block is complete or an odd cycle.  If `C` is
two-connected, it has one block, giving the final alternative. \(\square\)

Proposition 4.3 is the precise scope in which Gallai tightness is
available.  Minimal list-criticality alone gives (4.3), not equality and
not a Gallai-tree conclusion.

## 5. Exact finite boundary census

The following classification is deliberately separated from the preceding
unbounded proofs.

### Proposition 5.1 (computer-assisted boundary census)

Up to isomorphism, exactly twenty seven-vertex graphs satisfy the following
four necessary boundary conditions supplied by the promoted degree-seven
boundary reduction:

1. `alpha(H)<=2`;
2. `F=overline(H)` has a matching of order three;
3. `overline(K_2) join H` has no `K_7` minor; and
4. the subgraph of `F` induced by its nonisolated vertices is connected,
   two-connected, has at least six vertices and minimum degree at least two.

Their graph6 certificates, in NetworkX-atlas order, are

```text
FKdbG Fms`G Fm{`G FhNHo F{cZG
FhffG FQT|o FpLYw FL~Cg Ffwhg
F`urg FK|ko FN^Sg FJe~O Floxw
Fb]lg Feg~w F{e}o FzM]W FtTnw
```

Eighteen have a degree-two vertex in the nonisolated complement core and
therefore enter the promoted boundary-labelled `K_7^-` construction.  The
two exceptions are

\[
            F\cong K_{3,4},\qquad
            F\cong K_{3,3}\mathbin{\dot\cup}K_1,        \tag{5.1}
\]

which enter the promoted two-adjacent-missing-edge construction.  The Moser
spindle and its one-edge extension are two of the twenty types, not the
whole residual.

The deterministic verifier is
[`hc7_singleton_exact7_boundary_census.py`](hc7_singleton_exact7_boundary_census.py).
It enumerates the complete seven-vertex graph atlas and tests the displayed
conditions, including exact branch-set detection for the `K_7`-minor
exclusion.  This finite proposition does not assert that any listed type is
realizable by a hypothetical counterexample.

## 6. Exact remaining singleton obstruction

After the reductions above, any unresolved singleton terminal has:

1. one of the twenty boundary types in Proposition 5.1;
2. a connected, nonbipartite, boundary-full exterior `C` with `nu(C)=1`;
3. no cutvertex or bridge unless the argument accepts the proper-side
   exact-seven restart from Section 3;
4. for every nonedge `xy` of `H`, an exact one-pair colouring and the
   associated rooted `K_5` model on `S-{x,y}`; and
5. either an order-seven separator or seven internally disjoint `x-y`
   paths through the five named rooted bags, by the promoted
   connector-or-separator theorem; and
6. the low-degree literal-contact restrictions in Corollary 4.2, unless
   the matching-list kernel has already returned a proper-side separator.

The missing step remains label-sensitive: the seven paths need not split
the rooted bags, and an order-seven separator is not terminal without one
complete equality partition realized on both closed shores.  Neither the
Moser census nor another unlabelled `K_7^-` model supplies that step.

## Dependencies

- [degree-seven anti-neighbourhood connectivity](../results/hc7_degree7_anti_neighbourhood_connectivity.md)
- [exact matching languages and rooted `K_5` models](../results/hc7_degree7_matching_bridge_bundle.md)
- [boundary-labelled near-`K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
- [exact-seven full-subgraph packing](../results/hc7_exact_seven_packet_packing.md)
- [adaptive `(1,3)` reflection](../results/hc7_exact7_adaptive_packet_reflection.md)
- [adaptive `(1,2)` boundary closure](../results/hc7_exact7_adaptive_12_boundary_closure.md)
- [singleton-shore nonbipartiteness](../results/hc7_singleton_shore_nonbipartite.md)

The degree-choosability input in Proposition 4.3 is the classical theorem
of Borodin and, independently, Erdos--Rubin--Taylor; see P. Erdos,
A. L. Rubin and H. Taylor, *Choosability in graphs*, Congressus
Numerantium **26** (1979), 125--157.
