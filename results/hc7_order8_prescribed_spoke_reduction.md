# Prescribed spokes at a boundary-full order-eight interface

**Status:** written proof; separate internal audit in
[`hc7_order8_prescribed_spoke_reduction_audit.md`](hc7_order8_prescribed_spoke_reduction_audit.md).

This note separates two path-packing facts left by the locked edge-deletion
fan at a boundary-full order-eight separation.  Globally, the five
colour-indexed first edges can always be extended, together with the deleted
edge itself, to six paths with any prescribed six-element target set.  The
paths have distinct ends and share only their base vertex, but they need not
stay in the selected complementary component or avoid other boundary
vertices.

A complementary form retains the target set supplied by the original
bichromatic paths.  It returns either five clean paths or an actual
order-seven separation with a one-sided attained boundary colouring.  The
remaining obstruction is therefore placement of the inherited minor-model
branch sets, not intersection or endpoint concentration of the selected
paths.  Nothing here proves `HC_7`.

## 1. A prescribed-spoke fan lemma

### Theorem 1.1 (prescribed first edges and an arbitrary target set)

Let `k>=1`, let `G` be `(k+1)`-connected, let `v` be a vertex, and let

\[
                         vs_1,\ldots,vs_k                 \tag{1.1}
\]

be distinct edges.  If `Y subseteq V(G)-{v}` and `|Y|>=k`, then there are
`k` paths from `v` to `Y` which

1. have pairwise distinct ends in `Y`;
2. share no vertex other than `v`; and
3. begin with the prescribed edges in (1.1), one path per edge.

When `|Y|=k`, the paths end at every literal vertex of `Y`.

#### Proof

Let

\[
 D=\{s_i:s_i\in Y\},\qquad
 S=\{s_i:s_i\notin Y\},\qquad d=|D|.                 \tag{1.2}
\]

Keep the `d` direct paths `vs_i` for `s_i in D`.  In

\[
                         G'=G-(\{v\}\cup D)             \tag{1.3}
\]

consider paths from the `(k-d)`-set `S` to `Y-D`.  No set `Z` of order less
than `k-d` separates these terminal sets, even when `Z` contains terminals.
Indeed, both terminal sets have order at least `k-d`, so one member of each
survives.  After deleting `Z` together with `v` and `D`, at most `k`
vertices have been deleted from `G`; the surviving terminals remain
connected.

The vertex-set form of Menger's theorem therefore gives `k-d` pairwise
vertex-disjoint `S`--`(Y-D)` paths.  Since there are exactly `k-d` source
vertices, all sources occur and the target vertices are distinct.  Truncate
each path at its first target vertex and prepend its prescribed edge
`vs_i`.  Together with the direct paths, these are the required `k` paths.
\(\square\)

The theorem prescribes the first edges and the target **set**, but not the
pairing between non-direct first edges and target vertices.

## 2. Application to the locked edge-deletion fan

Use the notation of Theorem 5.1 in
[`hc7_order8_full_component_kempe_transition.md`](hc7_order8_full_component_kempe_transition.md).
Thus `X` is an eight-set, `C_i` is a component of `G-X`, `p in X`,
`v in C_i`, `e=pv`, and one colouring of `G-e` produces five distinct
colour-indexed first edges at `v`.

### Corollary 2.1 (a global six-fan to any selected boundary six-set)

Assume additionally that `G` is seven-connected.  For every five-set

\[
                              T\subseteq X-\{p\},       \tag{2.1}
\]

there are six paths from `v` to `T union {p}` such that

1. one path is the edge `vp`;
2. the other five paths begin with the five colour-indexed first edges;
3. their six boundary ends are exactly `T union {p}`; and
4. all six paths share only `v`; in particular, the five non-direct paths
   avoid `p`.

#### Proof

Apply Theorem 1.1 with `k=6`, target set `T union {p}`, and prescribed
edges consisting of `vp` and the five colour-indexed first edges.  These
six edges are distinct because `vp` is absent from the coloured graph
`G-e`.  The path using `vp` is direct by the construction in (1.2).
Pairwise disjointness away from `v` makes every other path avoid `p`.
\(\square\)

The rerouted portions need not remain bichromatic, need not stay in `C_i`,
and may meet vertices of `X-(T union {p})` internally.  What is retained is
the literal identity of each first edge, pairwise disjointness, and complete
freedom to prescribe the six terminal vertices.  This global fan is not a
clean boundary first-hit theorem.

## 3. Retaining the original colour-path targets

The following alternative is weaker as a path-packing statement but retains
the original bichromatic target information and can therefore expose a
coloured order-seven boundary.

### Theorem 3.1 (clean first-edge fan or a coloured order-seven separation)

Let `G` be seven-connected, let `X` be an eight-set, and let `C` be a
component of `G-X`.  Assume that `G-X` has another component.  Let `p in X`,
`v in C`, and `e=pv`.  Let `d` be a proper six-colouring of `G-e` with

\[
                              d(p)=d(v)=\alpha.          \tag{3.1}
\]

For each colour `beta ne alpha`, suppose `P_beta` is an
`alpha`--`beta` path from `v` to `X`, stopped at its first boundary vertex,
with all internal vertices in `C`.  Suppose the five paths are pairwise
edge-disjoint and paths of different colour pairs meet only at
`alpha`-coloured vertices.

Then one of the following holds.

1. There are five `v`--`X` paths, preserving the five first edges of the
   `P_beta`, which are pairwise vertex-disjoint outside `{v} union X`.
   Common boundary ends are permitted.
2. For some `ell in {2,3,4,5}` there are sets

   \[
      I\subseteq X,\quad |I|=\ell+1,\quad p\in I,
      \qquad Z\subseteq C-\{v\},\quad |Z|=\ell-1,       \tag{3.2}
   \]

   and a nonempty connected set `A subseteq C-({v} union Z)` such that

   \[
        N_G(A)=(X-I)\mathbin{\dot\cup}\{v\}
                     \mathbin{\dot\cup}Z.              \tag{3.3}
   \]

   This is an actual order-seven separation.  The restriction of `d` to
   `G[A union N_G(A)]` is a proper colouring in the original graph `G`, and
   its boundary `alpha`-class contains `v` and some vertex of `Z`.

#### Proof

Call `P_beta` direct when it is one edge.  Let `h` be the number of direct
paths and put `ell=5-h`.  Direct ends are distinct because they have the
distinct colours `beta`.  No direct end is `p`, because `pv` is absent from
`G-e`, and no direct end is the end of a non-direct path belonging to a
different colour pair.

If `ell<=1`, the original five paths already satisfy outcome 1.  Assume
`ell>=2`.  For every non-direct `P_beta`, write `vs_beta` for its first edge,
`x_beta in X` for its end, and `Q_beta=P_beta-v`.  The `ell` sources

\[
                         S=\{s_\beta:P_\beta
                                  \text{ is non-direct}\}            \tag{3.4}
\]

are distinct.  Choose `I subseteq X`, of order `ell+1`, containing `p` and
every `x_beta` from a non-direct path, and avoiding all direct ends.  This is
possible: after removing the `h=5-ell` direct ends, `X` still has `ell+3`
vertices, while at most `ell+1` vertices are prescribed.

In

\[
                            K=G[(C-\{v\})\cup I]          \tag{3.5}
\]

apply vertex-capacitated Menger from `S` to `I`, with unit capacity on
`C-{v}` and unlimited capacity on the targets in `I`.  Equivalently, split
the internal vertices, join a supersource to each member of `S` by a unit
arc, and use integral max flow.  Either there are `ell` paths, using every
source and pairwise disjoint outside `I`, or there is a set

\[
                         Z\subseteq C-\{v\},qquad
                         |Z|\le\ell-1,                  \tag{3.6}
\]

possibly containing sources, which meets every `S`--`I` path.

In the packing outcome, truncate each path at its first member of `I`,
prepend its prescribed edge `vs_beta`, and retain the direct paths.  The
set `I` avoids the direct ends, so the five paths are disjoint outside
`{v} union X` and preserve every first edge.  This is outcome 1.

In the cut outcome, some source lies outside `Z`.  Let `A` be its component
in `G[C-({v} union Z)]`.  It has no neighbour in `I`, since such an edge
would give an `S`--`I` path avoiding `Z`.  Componenthood and the fact that
`C` is a component of `G-X` give

\[
                   N_G(A)\subseteq (X-I)\cup\{v\}\cup Z. \tag{3.7}
\]

The right side has order at most

\[
                (8-(\ell+1))+1+(\ell-1)=7.             \tag{3.8}
\]

Another component of `G-X` lies outside `A union N_G(A)`, so the separation
is nontrivial.  Seven-connectivity forces equality throughout (3.6)--(3.8),
which proves (3.2)--(3.3).

Every original tail `Q_beta` is an `S`--`I` path and hence meets `Z`.  There
are `ell` tails and only `ell-1` vertices in `Z`; some `z in Z` belongs to
two tails, say those for `beta,gamma`.  Therefore

\[
 d(z)\in\{\alpha,\beta\}\cap\{\alpha,\gamma\}
                         =\{\alpha\}.                  \tag{3.9}
\]

Finally `p in I`, so the sole deleted edge `pv` is absent from the closed
graph `G[A union N_G(A)]`.  The restriction of `d` is consequently proper
there in the original graph. \(\square\)

## 4. The exact-seven output retains a dynamic colouring constraint

### Corollary 4.1 (common exact block and a connected boundary cylinder)

Assume, in addition to the hypotheses of Theorem 3.1, that every proper
minor of `G` is six-colourable.

In outcome 2 of Theorem 3.1, put

\[
             Y=N_G(A),\qquad
             J=d^{-1}(\alpha)\cap Y.                   \tag{4.1}
\]

Then:

1. every component of `G-Y` is adjacent to every literal vertex of `Y`;
2. `J` is an exact boundary colour class on the `A`-side and is an exact
   boundary colour class in some colouring of the opposite closed shore;
3. all labelled boundary colourings having `J` as one fixed exact class lie
   in one Kempe class; and
4. if `G[Y-J]` is a clique, the two shores have a common equality partition
   and six-colour `G`.

Thus every live separator output has a nonedge in `G[Y-J]`.

#### Proof

If a component of `G-Y` missed a vertex of the seven-set `Y`, its full
neighbourhood would have order at most six and would separate it from
another component, contrary to seven-connectivity.  This proves item 1.

The colouring `d` makes `J` exact on the `A`-side by definition.  Contract
a spanning tree of the connected set `A union J`, six-colour the resulting
proper minor, and restrict to the opposite closed shore.  Since `A` is
`Y`-full, pulling back the contraction colour over the independent set `J`
makes `J` an exact boundary class.  This proves item 2.

The graph `G[Y-J]` has at most five vertices because `|J|>=2`; it is
therefore four-degenerate.  The Las Vergnas--Meyniel theorem connects all
its labelled five-colourings by Kempe interchanges.  Holding the sixth colour
fixed exactly on `J` proves item 3.

If `G[Y-J]` is a clique, every exact-`J` boundary colouring has the same
equality partition

\[
                         J\mid\{y\}\quad(y\in Y-J).     \tag{4.2}
\]

After a palette permutation the two closed-shore colourings agree literally
on `Y` and glue, contradicting that `G` is not six-colourable. \(\square\)

## 5. The exact label-allocation condition

Neither fan normalization identifies colour names with minor-model branch
sets.  The following elementary decoder records precisely what still has to
be aligned.

### Lemma 5.1 (clean donor split)

Let `D,B_1,...,B_5` be the branch sets of a `K_6`-minor model.  Suppose

\[
                         D=A\mathbin{\dot\cup}W          \tag{5.1}
\]

where `A,W` are nonempty connected adjacent sets and `A` is adjacent to
every `B_i`.  Let

\[
                  M=\{i:E_G(W,B_i)=\varnothing\}.       \tag{5.2}
\]

If there is a connected set `R`, disjoint from
`A union W union B_1 union ... union B_5`, such that `W union R` is
connected and `R` is adjacent to every `B_i` with `i in M`, then `G`
contains a `K_7` minor.

#### Proof

The seven sets

\[
                      A,\quad W\cup R,\quad
                      B_1,\ldots,B_5                   \tag{5.3}
\]

are disjoint and connected.  The old `K_6` model supplies every adjacency
except possibly those from `W union R` to a member of `M`; those are supplied
by `R`.  Thus (5.3) is a `K_7`-minor model. \(\square\)

In particular, a clean connected subgraph assembled from suitable fan
prefixes suffices once it meets every label in `M`.  Corollary 2.1 alone
does not provide such prefixes, because its paths can cross unselected
boundary vertices or old model branch sets.  No injective colour-to-label
matching is required.  What remains unproved is the model-alignment
statement that places `p,v` in a splittable branch set with the `p`-side
retaining the five old contacts, and either gives the other five branch sets
clean traces or turns failure into a compatible order-seven separation.

## 6. Exact scope

The two fan theorems are host-level and unbounded.  The global fan removes
shared internal vertices and repeated terminal concentration only when
paths may traverse the whole host.  The target-retaining theorem either
gives a component-internal clean fan (common boundary ends permitted) or an
exact order-seven separator.  The possible obstruction has been compressed
to three label-sensitive events:

1. the locally chosen edge `pv` need not lie in a branch set of the inherited
   near-clique model whose `p`-side retains the five named contacts; and
2. an inherited branch set can cross the order-eight separator, so its clean
   target trace need not be available independently of the fan interior;
   and
3. the arbitrary-target global fan may cross other boundary vertices or
   protected branch sets before reaching its prescribed ends.

The exact-seven alternative retains a one-sided boundary colouring and a
common exact block, but not a common full equality partition.  These are the
remaining label-preserving model-alignment or colour-gluing obligations.

## 7. Dependencies

- [order-eight full-component Kempe transition](hc7_order8_full_component_kempe_transition.md)
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B 31 (1981), 95--104.
