# Palette-to-label alignment in a spanning bipartite singleton shell

## Status

This note proves a parameter-uniform labelled alignment theorem.  It does
not prove Hadwiger's conjecture.  Its point is that the full-palette split
from `hc7_near_k7_bipartite_total_contraction.md` becomes a
literal all-but-one **model-label** split when all other model bags are
singletons.  With two or more deficient singleton labels, failure of the
target minor forces an actual small separator or an entire portal class
into one independent transversal of the complex bag.

The conclusion is operation-sensitive: it uses a different proper-minor
colouring for each apex non-neighbour.  It is stronger than merely saying
that the two shores see all palette colours.

## 1. Spanning singleton shell

Let `k>=4`.  Suppose that

\[
 V(G)=\{v\}\mathbin{\dot\cup}V(B)
       \mathbin{\dot\cup}\{b_1,\ldots,b_{k-2}\},            \tag{1.1}
\]

where:

1. `G` is not `(k-1)`-colourable;
2. the induced graph `G[B]` is connected, bipartite, and has at least two
   vertices;
3. the vertices `b_1,...,b_{k-2}` form a clique; and
4. `(B,{b_1},...,{b_{k-2}})` is a spanning `K_{k-1}`-model in
   `G-v`.

Thus every `b_i` has a nonempty portal set

\[
                         P_i=N_B(b_i).                       \tag{1.2}
\]

Put

\[
              J=\{i\in[k-2]:vb_i\notin E(G)\}.              \tag{1.3}
\]

No assumption is made about the edges from `v` to `B`.

### Theorem 1.1 (literal defect-one split)

For every `j in J`, there is an edge of a spanning tree of `B` whose two
tree components have vertex sets

\[
                        B=B_j^-\mathbin{\dot\cup}B_j^+       \tag{1.4}
\]

such that:

1. `B_j^-` and `B_j^+` are nonempty, connected and adjacent;
2. every singleton `b_i` with `i!=j` has a neighbour in each shore; and
3. each shore has a neighbour in the two-vertex set `{v,b_j}`.

If `G` has no `K_k` minor, then `b_j` misses at least one of the two
shores.  Every shore missed by `b_j` has a neighbour at `v`.

#### Proof

Contract `B` to a vertex `z`.  On `G/B`, use the colour set

\[
                         \{a,p_1,\ldots,p_{k-2}\}
\]

and assign

\[
                   c(z)=a,\qquad c(b_i)=p_i,qquad c(v)=p_j. \tag{1.5}
\]

This is a proper `(k-1)`-colouring.  The singleton vertices form a
clique and have distinct colours.  The model edge `Bb_i` makes `zb_i`
an edge, so its ends have the distinct colours `a,p_i`.  Finally all
edges at `v` are proper: the only other vertex of colour `p_j` is
`b_j`, and `vb_j` is absent by the choice of `j`.

Apply Theorem 2.2 of
`hc7_near_k7_bipartite_total_contraction.md` to the connected
bipartite set `B`, the colouring (1.5), and any spanning tree of `B`.
It returns (1.4), and both shores see every colour other than `a`.
For `i!=j`, the only outside vertex of colour `p_i` is `b_i`; hence
`b_i` sees both shores.  The outside vertices of colour `p_j` are exactly
`v,b_j`, proving item 3.

If `b_j` saw both shores, then

\[
                 B_j^-,\ B_j^+,\ \{b_1\},\ldots,\{b_{k-2}\}
                                                                    \tag{1.6}
\]

would be `k` disjoint connected pairwise adjacent branch sets.  They
would form a `K_k`-model.  Thus in the target-free branch `b_j` misses a
shore, and item 3 forces `v` to see that shore.  \(\square\)

The theorem is already a literal palette-to-label conversion: only the
one colour shared by `v` and `b_j` remains ambiguous.

## 2. Simultaneous deficient-label witnesses

Fix a bipartition `(A,D)` of `B`.  Call a vertex of `B` **universal** if
it is adjacent to all `b_1,...,b_{k-2}`.

### Lemma 2.1 (one saturated vertex in each bipartition class)

For every `j in J`, each of `A,D` contains a vertex `x` satisfying

\[
 x\sim b_i\quad(i\ne j),qquad
 x\sim v\ \hbox{ or }\ x\sim b_j.                          \tag{2.1}
\]

#### Proof

Use the quotient colouring (1.5).  For `x in B`, let

\[
 L_j(x)=\{a,p_1,\ldots,p_{k-2}\}
              -c(N_G(x)-B).                                \tag{2.2}
\]

Every list contains `a`.  The graph `B` has no `L_j`-colouring, since
such a colouring together with (1.5) outside `B` would be a
`(k-1)`-colouring of `G`.

If every vertex of `A` had a secondary colour in its list, colour the
vertices of `D` with `a`, and choose independently for every vertex of
`A` any colour in `L_j(x)-{a}`.  This is a proper list-colouring because
both bipartition classes are independent.  Therefore some `x in A` has
`L_j(x)={a}`.  The same argument with `A,D` interchanged gives such a
vertex in `D`.

For `i!=j`, the sole outside vertex of colour `p_i` is `b_i`, so
`L_j(x)={a}` forces `x~b_i`.  The colour `p_j` occurs outside `B`
exactly at `v,b_j`, so it forces at least one of `x~v,x~b_j`.  This is
(2.1).  \(\square\)

### Lemma 2.2 (opposite universal vertices close)

If both `A` and `D` contain a universal vertex, then `G` contains a
`K_k` minor.

#### Proof

Choose universal vertices `x in A`, `y in D` and a shortest `x-y` path
in `B`.  Delete any edge of that path and take its two path intervals.
They are disjoint, connected and adjacent, and each contains a vertex
adjacent to every `b_i`.  Together with the `k-2` singleton bags they
form a `K_k`-model.  \(\square\)

### Theorem 2.3 (deficient-label transversal or target minor)

Assume `|J|=d>=2` and `G` has no `K_k` minor.  One of the two
bipartition classes of `B`, say `A_0`, contains distinct vertices

\[
                              X=\{x_j:j\in J\}              \tag{2.3}
\]

such that, for every `j in J`,

\[
 x_j\sim v,qquad x_j\not\sim b_j,qquad
 x_j\sim b_i\quad(i\ne j).                                 \tag{2.4}
\]

Consequently

\[
                             C=\{v\}\cup X                  \tag{2.5}
\]

is connected and is adjacent to every singleton bag `{b_i}`.

Moreover at least one of the following two literal obstructions occurs:

1. `B-X` is disconnected; or
2. `P_i subseteq X` for some `i in[k-2]`.

#### Proof

By Lemma 2.2, at least one bipartition class `A_0` contains no universal
vertex.  For each `j in J`, choose in `A_0` the vertex supplied by
Lemma 2.1.  It is adjacent to every `b_i` except possibly `b_j`.  Since
it is not universal, it misses `b_j`, and (2.1) therefore forces its edge
to `v`.  This proves (2.4).

The vertices are distinct.  Indeed, if `x_j=x_h` for distinct `j,h`,
then the conditions for `j` and `h` together make this common vertex
adjacent to every `b_i`, contrary to the choice of `A_0`.

The set `C` is a star at `v`.  If `i notin J`, every `x_j` sees `b_i`.
If `i in J`, choose `h in J-{i}`; then `x_h` sees `b_i`.  Thus `C`
sees every singleton bag.

Suppose neither displayed obstruction occurs.  Then

\[
                              R=B-X                           \tag{2.6}
\]

is connected, and every `P_i` contains a vertex of `R`; hence `R` sees
every singleton bag.  Since `X` lies in one bipartition class, it is
independent.  The connected graph `B` has at least two vertices, and
every `x_j` has a neighbour in the opposite bipartition class, necessarily
in `R`.  Therefore `C` and `R` are adjacent.  The `k` sets

\[
                       C,\ R,\ \{b_1\},\ldots,\{b_{k-2}\}  \tag{2.7}
\]

are now disjoint, connected and pairwise adjacent.  They form a
`K_k`-model, the required contradiction.  \(\square\)

### Corollary 2.4 (connectivity--portal threshold)

In the setting of Theorem 2.3, if

\[
                 \kappa(B)\ge d+1
        \quad\hbox{and}\quad |P_i|\ge d+1\quad(1\le i\le k-2), \tag{2.8}
\]

then `G` contains a `K_k` minor.

#### Proof

The set `X` has order `d`.  The first inequality makes `B-X` connected,
and the second prevents any nonempty portal set `P_i` from lying in `X`.
Theorem 2.3 finishes.  \(\square\)

### Corollary 2.5 (the exact two-defect residue)

Assume `J={s,t}` and every portal set has order at least two.  If `G`
has no `K_k` minor, then either `B-{x_s,x_t}` is disconnected, or

\[
               P_i=\{x_s,x_t\}\quad\hbox{for some }i\notin\{s,t\}.
                                                                    \tag{2.9}
\]

#### Proof

Apply Theorem 2.3.  In its second outcome, `P_i` is a subset of the
two-vertex set `X={x_s,x_t}`.  Its assumed order is at least two, so
`P_i=X`.  But `x_s` misses `b_s` and `x_t` misses `b_t`; hence neither
`P_s` nor `P_t` can equal `X`.  Thus `i notin{s,t}`.  \(\square\)

For the near-`K_7` shell, when `k=7` and `|J|=2`, a three-connected
bipartite complex bag in which every singleton label has three portals is
already impossible in the target-free branch.  Under the
two-portal multiplicity already supplied by the spanning-singleton core
theorem, the exact residue is not an unlabelled palette collision: it is a
two-vertex separator of the complex bag, or an ordinary singleton label
whose portal set is exactly the two independent deficient-label
witnesses.

## 3. Why the strong colouring hypothesis is used

The two literal defect-one split patterns alone do not encode the strong
colouring hypothesis.
For every `k>=6`, let `O` be a clique of order `k-4`; add vertices
`s,t,v,l,m,r`; make `{s,t} union O` a clique, and add

\[
 lm,mr,\quad sl,sm,\quad tm,tr,\quad vl,vr,               \tag{3.1}
\]

together with all edges from every vertex of `O` to `l,r,v`.  Put
`B=lmr`, `b_s=s`, `b_t=t`, and use `O` as the other singleton bags.
The cuts `lm` and `mr` have exactly the all-but-one labelled split
patterns for `t` and `s`, respectively.  Nevertheless the graph is
`(k-1)`-colourable: colour the six-vertex remainder with three colours and
use fresh colours on `O`.  Thus it has no static reason to be a minimal
Hadwiger counterexample.

Thus Theorem 2.3 genuinely spends the non-`(k-1)`-colourability through
the two bipartite singleton-list obstructions.  It is not a consequence
of portal incidence alone.

## 4. Interface with the general model-meeting problem

The argument isolates a reusable conversion principle:

\[
\boxed{
 \begin{array}{c}
 \text{one complex bipartite carrier + singleton clique}\cr
 \text{+ all proper-minor apex colour choices}
 \end{array}
 \Longrightarrow
 \begin{array}{c}
 \text{literal all-but-one labelled splits}\cr
 \text{and a same-side deficient-label transversal.}
 \end{array}}
\]

In a general clique model the colour `p_i` may occur at vertices outside
the labelled bag `B_i`, so the uniqueness step in Theorem 1.1 fails.
The correct extension target is therefore precise: replace each singleton
`b_i` by a connected carrier which is the unique exterior occurrence of
its quotient colour, or prove that nonuniqueness yields a colour-gluable
adhesion.  No assertion that an arbitrary colour class is a connected
model carrier is used here.
