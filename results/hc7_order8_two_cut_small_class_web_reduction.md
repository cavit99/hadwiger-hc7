# Unbalanced bipartitions at the two-cut response interface

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_small_class_web_reduction_audit.md`](hc7_order8_two_cut_small_class_web_reduction_audit.md).
This is an unbounded structural reduction, not a proof of `HC_7`.  An
order-seven separation returned below is not asserted to carry a common
equality partition on both closed shores.

## 1. Setting

Assume the hypotheses and notation of the audited
[two-cut response orientation theorem](hc7_order8_two_cut_response_orientation.md).
Thus `S` has order eight, `G-S` has the three boundary-full components
`C,Q_0,Q_1`, and

\[
 C=L_d\mathbin{\dot\cup}L_e\mathbin{\dot\cup}\{x,y\}.
 \tag{1.1}
\]

The two lobes `L_d,L_e` miss exactly `d,e`, respectively; neither cut
vertex is adjacent to `d` or `e`; and

\[
 S-\{d,e\}=P\mathbin{\dot\cup}R                    \tag{1.2}
\]

is a bipartition into nonempty independent sets.  The closed `C`-side
realizes only

\[
                 P\mid R\mid\{d\}\mid\{e\},        \tag{1.3}
\]

while each individual closed `Q_i`-side realizes

\[
                 P\mid R\mid\{d,e\}.                \tag{1.4}
\]

Every colouring in the prescribed response family (1.3) contains a
bichromatic `d`--`e` path with all internal vertices in `C`.

For `s in S`, write

\[
                         Z_s=N_G(s)\cap C.            \tag{1.5}
\]

for its literal portal set in `C`.

## 2. A reserved connector realizes both response types

### Lemma 2.1

Let `B` be one of the two classes `P,R`, and let `B'` be the other.  Suppose
that `C` contains pairwise vertex-disjoint connected subgraphs `D,K` such
that

1. `D` has a neighbour at both `d` and `e` and has at least two vertices;
2. `K` has a neighbour at every literal vertex of `B`.

Then `G` is six-colourable.

### Proof

Fix `i in {0,1}` and put `j=1-i`.  Regard `Q_i` as one open shore and
`C union Q_j` as the other.  In the latter shore use

\[
                         D,\qquad K,\qquad Q_j.       \tag{2.1}
\]

The first set is adjacent to both roots, the second meets every member of
`B`, and the third meets every member of `B'`.  The three sets are pairwise
disjoint.  The two classes in (1.2) have an edge between them, as proved in
the response-orientation theorem.

The audited reserved-path and boundary-block contraction theorem therefore
realizes (1.4) on the closed `Q_i`-side.  Choose a `d`-portal and an
`e`-portal in `D`.  They are distinct: every `d`-portal in `C` lies in
`L_e`, every `e`-portal lies in `L_d`, and the lobes are disjoint.  Split a
spanning tree of `D` across an edge on the unique tree path between those
portals.  Its two nonempty components are connected, adjacent, and retain
one root contact each.  The same theorem then realizes (1.3) on that closed
side.

Apply the construction for both `i=0,1`.  The two resulting colourings of
the individual `Q_i` sides inducing (1.3) can be aligned with the prescribed
colouring (1.3) of the closed `C`-side.  The three open components are
pairwise anticomplete, so the colourings glue to a proper six-colouring of
`G`. \(\square\)

## 3. A singleton bipartition class

### Theorem 3.1

If one class of (1.2) is a singleton, then at least one of the following
holds.

1. `G` is six-colourable.
2. `G` has an actual separation of order seven.
3. There is a nonempty connected proper set $C'\subsetneq C$ such that,
   with `T=N_G(C')`, one has `|T|=8`, the graph `G-T` has exactly two or
   three components, and every component of `G-T` is adjacent to every
   literal vertex of `T`.

In outcome 3, the selected unequal-response colouring of the closed
`C`-side restricts to a proper colouring of `G[C' union T]`, and
`|C'|<|C|`.

### Proof

Let the singleton class be `{p}` and choose `w in Z_p`, which is nonempty
because `C` is boundary-full.  If some `d`--`e` path with interior in `C`
avoids `w`, take its internal vertex set as `D` and take `K={w}` in
Lemma 2.1.  The set `D` has at least two vertices: a neighbour of `d` lies
in `L_e`, a neighbour of `e` lies in the disjoint lobe `L_d`, and the cut
vertices miss both roots.  Lemma 2.1 gives outcome 1.

We may therefore assume that every `d`--`e` path through `C` contains `w`.
The graph `G[C]-w` is connected because `G[C]` is two-connected.  If both
`d` and `e` had neighbours in `C-w`, a path between such neighbours in
`C-w`, together with its two root edges, would be a `d`--`e` path avoiding
`w`.  Consequently `w` is the unique neighbour in `C` of one of `d,e`.

Put `C'=C-{w}`.  It is nonempty, connected and proper.  Its neighbourhood
inside `C` is exactly `{w}`, while it misses from `S` the root whose unique
portal was `w`.  Hence

\[
 |N_{G[C]}(C')|+|N_G(C')\cap S|\le1+7=8.             \tag{3.1}
\]

The audited small-boundary lobe descent applies.  It gives outcome 2 or
outcome 3, including the strict inequality `|C'|<|C|`.  Finally, all
vertices of `C' union T` belong to `C union S`; restricting the selected
closed-`C` response colouring therefore gives the asserted proper
one-sided colouring at the descended interface. \(\square\)

## 4. A two-vertex bipartition class

### Theorem 4.1

Suppose one class of (1.2) is `B={p,q}`.  Then at least one of the following
holds.

1. `G` is six-colourable.
2. `G` has an actual separation of order seven whose connected shore lies
   in `C`.
3. The graph

   \[
                    H=G[C\cup\{d,e,p,q\}]            \tag{4.1}
   \]

   is a spanning subgraph of a planar `(d,p,e,q)`-web having no nonempty
   attachment set behind a facial triangle.  In particular, the four
   displayed boundary vertices occur in this cyclic order on the outer
   face of the web skeleton.

### Proof

The vertices `p,q` are nonadjacent because they lie in one bipartition
class, and `d,e` are nonadjacent by the response normal form.  Apply the
Two Paths theorem to the terminal pairs `(d,e)` and `(p,q)` in `H`.

If the required two vertex-disjoint paths exist, neither can use a terminal
of the other path.  Their internal vertices therefore lie in `C`.  The
internal vertices of the `d`--`e` path form a connected set `D` of order at
least two, for its first and last vertices lie in the two distinct lobes.
The internal vertices of the `p`--`q` path form a nonempty connected set
`K` adjacent to both `p,q`.  These two sets are disjoint, so Lemma 2.1 gives
outcome 1.

Assume that the linkage does not exist.  The Two Paths theorem says that
`H` is a spanning subgraph of a `(d,p,e,q)`-web.  Let `F` be its planar
skeleton.  For every facial triangle `T_0` of `F`, let `X_{T_0}` denote the
possibly empty attachment set allowed behind that triangle in the web
completion.

Suppose some `X_{T_0}` is nonempty.  Choose a nonempty component `A` of
`G[X_{T_0}]`.  In the web completion no vertex of `X_{T_0}` has a neighbour
outside `T_0 union X_{T_0}`.  Componenthood then gives

\[
 N_G(A)\subseteq T_0\mathbin{\dot\cup}
              \bigl(S-\{d,e,p,q\}\bigr).             \tag{4.2}
\]

The right-hand side has order seven.  This is a genuine separation: `A`
is nonempty, while `Q_0` lies outside `A union N_G(A)`.  Seven-connectivity
forces equality in (4.2), giving outcome 2.

We may therefore assume every attachment set is empty.  The web completion
is then its planar skeleton, and `H` is a spanning subgraph of that skeleton
with `d,p,e,q` in the displayed cyclic order on its outer face.  This is
outcome 3. \(\square\)

## 5. Exact gain and trust boundary

The theorem eliminates the entire singleton-class case up to the already
audited order-seven/strict-order-eight restart, and reduces every
two-vertex-class case to an attachment-free planar web.  It is independent
of the orders of the two lobes and of the full components.

The order-seven outcome is not proved colour-compatible.  The strict
order-eight outcome preserves the selected colouring only on its descended
closed shore, not a complete equality partition on both shores or the five
inherited minor-model labels.  The planar web in Theorem 4.1 is not itself
terminal: completion edges are virtual, and the contacts of the other four
boundary vertices have not been allocated.  The balanced `3+3`
bipartition remains outside the theorem.

## Dependencies

- the audited two-cut response orientation;
- the audited reserved path and boundary-block contraction theorem;
- the audited small-boundary lobe descent; and
- the classical Two Paths theorem in the form of Lemma 2 of R. Fabila-Monroy
  and D. R. Wood, *Rooted K4-Minors*, Electronic Journal of Combinatorics
  **20** (2013), #P64.
