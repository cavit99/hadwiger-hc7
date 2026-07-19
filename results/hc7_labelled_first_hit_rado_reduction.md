# A Rado--gammoid reduction for labelled first-hit paths

**Status:** written proof; separate internal audit GREEN.

This note isolates the exact matroidal content of the current five-label
first-hit problem.  It also records the additional literal-neighbourhood
bound needed to turn a relative linkage obstruction into an order-seven
separation in the host graph.

## 1. Clean labelled linkages

Let `H` be a finite graph.  Let `P` be a set of source vertices, and let

\[
                  T_1,\ldots,T_m\subseteq V(H)
\]

be nonempty pairwise disjoint sets, disjoint from `P`.  Put
`T=\bigcup_i T_i` and assume `|P|>=m`.

A **clean labelled linkage** is a family of pairwise vertex-disjoint paths
`Q_1,...,Q_m` such that, for every `i`,

1. one end of `Q_i` is a distinct vertex of `P`;
2. the other end belongs to `T_i`; and
3. that terminal end is the only vertex of `T` on `Q_i`.

Thus the end in `T_i` is a literal first hit on the whole terminal union.

For `I subseteq [m]`, write `T_I=\bigcup_{i in I}T_i` and let `r_P(T_I)`
be the maximum order of a family of pairwise vertex-disjoint paths from
distinct vertices of `P` to distinct vertices of `T_I`, each meeting `T`
only at its terminal end.

### Theorem 1.1 (Rado--gammoid first-hit alternative)

A clean labelled linkage exists if and only if

\[
                       r_P(T_I)\ge |I|                 \tag{1.1}
\]

for every `I subseteq [m]`.  Consequently, if no clean labelled linkage
exists, there is a nonempty `I subseteq [m]` such that

\[
                       r_P(T_I)<|I|.                   \tag{1.2}
\]

For such an `I`, there is a vertex set `Z` of order `r_P(T_I)` in the
terminal-avoiding directed network defined below which meets every directed
path from `P` to the selected terminal copies.  In particular,

\[
                         |Z|\le |I|-1.                 \tag{1.3}
\]

The separator `Z` is allowed to contain source vertices or selected
terminal copies.

#### Proof

Construct a directed graph `D` as follows.  Its nonterminal vertices are
the vertices of `H-T`.  Replace every edge of `H-T` by its two orientations.
For each `t in T`, introduce one new vertex `hat(t)`.  For every edge `ut`
of `H`, where `u notin T` and `t in T`, add the arc

\[
                            u\longrightarrow \widehat t.
\]

The vertex `hat(t)` has outdegree zero.  Edges with both ends in `T` are
discarded.  Directed paths from `P` to terminal copies in `D` therefore
encode exactly the clean paths in the definition above.  In particular,
no path can pass through an unintended terminal copy.

Reverse all arcs of `D`.  With `P` as the fixed sink set, the subsets of
`hat(T)={hat(t):t in T}` which can be linked vertex-disjointly to `P` are
the independent sets of a gammoid.  Its rank on `hat(T_I)` is exactly
`r_P(T_I)`.  Rado's independent-transversal theorem, applied to the
families `hat(T_1),...,hat(T_m)`, says that an independent transversal
exists exactly when (1.1) holds for every `I`.  Expanding the corresponding
directed paths gives the clean labelled linkage.

If no such linkage exists, the empty index set cannot violate (1.1), so a
nonempty `I` satisfies (1.2).  Directed vertex Menger applied in `D` gives
a set `Z` of order `r_P(T_I)` meeting every directed path from `P` to
`hat(T_I)`.  This proves (1.3).  \(\square\)

### Why the sink orientation is necessary

It is not safe to replace each terminal by an undirected copy adjacent to
all its nonterminal neighbours.  Such a copy need not be a leaf and could
be traversed internally.  For example, on the path

\[
                            u-t-v-s
\]

with `P={u}`, `T_1={s}`, and `T_2={t}`, there is no clean path from `P` to
`T_1`: every such host path uses `t` internally.  An undirected copy
construction nevertheless contains the spurious path

\[
                       u-\widehat t-v-\widehat s.
\]

Making every terminal copy a directed sink removes exactly this error.

## 2. From a relative separator to a host separation

Fix a deficient nonempty index set `I` and a Menger set `Z` supplied by
Theorem 1.1.  Map it back to literal host vertices by

\[
 \overline Z=
 \bigl(Z\cap(V(H)-T)\bigr)
 \mathbin{\dot\cup}
 \{t\in T_I:\widehat t\in Z\}.                         \tag{2.1}
\]

This map is injective, so `|bar(Z)|=|Z|`.  Since `|P|>=m` and
`|Z|<|I|<=m`, choose `p in P-Z`.  Let `C` be the component containing `p`
in

\[
                 H-T-\bigl(Z\cap(V(H)-T)\bigr).        \tag{2.2}
\]

### Theorem 2.1 (exact exposure criterion)

With the notation above,

\[
 N_H(C)\subseteq
 \overline Z\ \cup\ \bigl(N_H(C)\cap(T-T_I)\bigr).    \tag{2.3}
\]

There is a vertex of `T_I-bar(Z)` outside `C` and outside the right-hand
side of (2.3).  Hence the right-hand side separates the nonempty connected
set `C` from a nonempty part of the host graph.

If `H` is seven-connected and

\[
              e_C:=|N_H(C)\cap(T-T_I)|\le 7-|Z|,       \tag{2.4}
\]

then equality holds in (2.4), the right-hand side of (2.3) is exactly
`N_H(C)`, and it is the boundary of an actual order-seven separation.
Equivalently, in a seven-connected host every deficient label set has one
of the two outcomes

\[
 \begin{array}{ll}
 e_C=7-|Z|, &\text{an actual order-seven separation};\\
 e_C\ge 8-|Z|, &\text{excess exposure to unselected terminal classes}.
 \end{array}                                             \tag{2.5}
\]

#### Proof

Every neighbour of `C` outside `T` belongs to
`Z cap (V(H)-T)` by the definition of the component in (2.2).  If a
selected terminal `t in T_I` has a neighbour in `C`, the arc from that
neighbour to `hat(t)` is a directed `P`--`hat(T_I)` path unless
`hat(t) in Z`.  These are exactly the first two parts of the right-hand
side of (2.3).  The only remaining host neighbours of `C` lie in `T-T_I`.

Moreover,

\[
                      |T_I|\ge |I|>|Z|.
\]

Thus some selected terminal `t` has `hat(t) notin Z`.  The preceding
argument shows that `t` has no neighbour in `C`; it belongs neither to
`C` nor to the right-hand side of (2.3).  The displayed set is therefore
a genuine host separator.

Under (2.4), that separator has order at most seven.  Seven-connectivity
forces `|N_H(C)|>=7`.  Since `N_H(C)` is contained in a set of order at
most seven, all inclusions and inequalities are equalities.  This proves
the first line of (2.5); integrality gives the second line when (2.4)
fails.  \(\square\)

### Corollary 2.2 (three fixed vertices and one portal per unused label)

Suppose the clean-linkage network is formed after additionally deleting a
fixed literal set `F`, disjoint from `P union T`, of order at most three.
Use `H-(T union F)` as the nonterminal part of `D`.  For the component `C`
returned above, assume

\[
             |N_H(C)\cap T_j|\le1
             \quad\text{for every }j\notin I.          \tag{2.6}
\]

Then

\[
 \left|\overline Z\cup(N_H(C)\cap F)
                 \cup(N_H(C)\cap(T-T_I))\right|
 \le (|I|-1)+3+(m-|I|).
\]

For `m=5` the right-hand side is seven.  Thus, in a seven-connected host,
this set is the boundary of an actual order-seven separation.

#### Proof

The proof of Theorem 2.1 is unchanged after adding
`N_H(C) cap F` to the exposed host vertices.  Condition (2.6) bounds the
unselected-terminal contribution by `m-|I|`; now use (1.3).  \(\square\)

## 3. Trust boundary for the `HC_7` application

The theorem is a complete Hall--Rado reduction, but it does not by itself
close the labelled first-hit problem.

1. The sources are distinct unit-capacity vertices.  If several paths may
   share one connected source branch set, or if both source and target
   labels prescribe a pairing, the resulting problem is not this gammoid
   transversal problem.
2. A contracted connected branch set is not one literal separator vertex.
   Corollary 2.2 applies to three actual vertices.  It applies to a
   contracted branch set only after proving that every relevant attachment
   to `C` is covered by the stated number of literal portal vertices.
3. A rank defect controls selected terminal copies but says nothing about
   how many vertices in the unused terminal classes meet `C`.  The exposure
   bound (2.4), or a host theorem implying it, is indispensable.
4. Even an actual order-seven separation is not yet a colouring-gluing
   conclusion.  To use it terminally in a hypothetical minimal
   counterexample, one still needs proper colourings of the two closed
   shores which induce the same equality partition on these seven literal
   boundary vertices.  Rado's theorem carries no boundary-colouring data.

Accordingly, the remaining host theorem has a precise form: use
`K_7`-minor exclusion and the proper-minor colouring responses to bound the
unused-label exposure in (2.5), concentrate it at one literal portal per
label as in Corollary 2.2, or directly produce the common boundary equality
partition.
