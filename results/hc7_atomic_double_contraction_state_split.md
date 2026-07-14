# Atomic double-contraction state split

**Status:** proved, awaiting independent audit.

This note replaces a comparison of unrelated deletion-state families by
one canonical colouring of a double contraction.  It couples the compulsory
thin edge to a literal rich-shore edge, but it does not yet convert the
resulting colour saturation into labelled carriers.

## 1. Setup and boundary convention

Let `G` be a graph with chromatic number seven such that every proper minor
is six-colourable.  Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

be a separation with no `A-R` edge.  Let

\[
 e=zu,\qquad z\in A,\quad u\in S,
 \qquad\hbox{and}\qquad
 f=xy,\qquad x,y\in R                                      \tag{1.1}
\]

be disjoint literal edges.

When an edge with one end in `S` is contracted, its contracted image retains
the label of the boundary end.  Thus a colouring of `G/e` still has a
well-defined equality partition on the literal label set `S`.

For a six-colouring `c` of a graph in which an edge `vw` is absent and
`c(v)=c(w)`, call `v` **free relative to `w`** if some colour other than
`c(v)` is absent from `N(v)-{w}`.  Recolouring `v` with such a colour makes
the missing edge `vw` proper.

## 2. Critical-edge state chambers

### Lemma 2.1 (deletion-contraction correspondence)

For every edge `h=vw` of `G`, every six-colouring of `G-h` gives `v,w` the
same colour.  Consequently lifting and collapsing the ends gives a
bijection

\[
              \operatorname{Col}_6(G-h)
              \longleftrightarrow
              \operatorname{Col}_6(G/h).              \tag{2.1}
\]

The bijection preserves the equality partition on every labelled set
disjoint from the interior end of the contraction, with the boundary
convention above.

#### Proof

If a six-colouring of `G-h` gave the ends of `h` different colours, restoring
`h` would six-colour `G`.  Thus the ends have the same colour, and such a
colouring collapses to `G/h`.  Conversely every colouring of `G/h` lifts by
giving both ends the colour of the contracted vertex.  These operations are
inverse.  \(\square\)

### Lemma 2.2 (the three nonempty chambers)

The six-colourings of `G-{e,f}` occupy exactly the following equality
chambers at the two missing edges:

\[
\begin{array}{c|c|c}
 c(z)=c(u)&c(x)\ne c(y)&\operatorname{Col}_6(G-e),\\
 c(z)\ne c(u)&c(x)=c(y)&\operatorname{Col}_6(G-f),\\
 c(z)=c(u)&c(x)=c(y)&\operatorname{Col}_6(G/e/f).
\end{array}                                               \tag{2.2}
\]

All three chambers are nonempty.  The fourth chamber, in which both pairs
are different, is empty.

#### Proof

A colouring in the first chamber restores `f` and hence is a colouring of
`G-e`; Lemma 2.1 gives the reverse inclusion.  The second chamber is
symmetric.  The third chamber is precisely the lift of a colouring of the
proper minor `G/e/f`, which exists.  A colouring in the fourth chamber
would restore both edges and six-colour `G`.  \(\square\)

The third chamber is the canonical shared object missing from a comparison
of independently selected colourings of `G-e` and `G-f`.

## 3. The split theorem

### Theorem 3.1 (boundary-preserving double-contraction split)

Let `c` be any six-colouring of `G/e/f`, lifted to `G-{e,f}`.  If `z` is
free relative to `u` and at least one of `x,y` is free relative to the other,
then `G` is six-colourable.

Equivalently, in a hypothetical counterexample every such `c` satisfies

\[
 \boxed{
 z\text{ sees all five colours other than }c(z)
 \quad\text{or}\quad
 x\text{ and }y\text{ both see all five colours other than }c(x).}
                                                               \tag{3.1}
\]

Here the neighbours witnessing an alternative colour are taken outside the
mate across the corresponding missing edge.

#### Proof

The lifted colouring has

\[
                         c(z)=c(u),\qquad c(x)=c(y).     \tag{3.2}
\]

If `z` is free, recolour only `z` with a missing alternative colour and
restore `e`.  This gives a six-colouring of `G-f`.  Since `z` is not a
boundary vertex, its equality partition on `S` is unchanged from that of
`c`.

If, say, `x` is free relative to `y`, recolour only `x` and restore `f`.
This gives a six-colouring of `G-e`, again with exactly the boundary
partition induced by `c`, because `x` lies in the open rich shore.

Restrict the first colouring to the intact thin closed shore `G[A union S]`
and the second to the intact rich closed shore `G[R union S]`.  They induce
the same equality partition on `S`; after a permutation of the six colour
names they agree literally on `S`.  There is no `A-R` edge, so the two
restrictions glue to a six-colouring of `G`, a contradiction.

Thus `z` cannot be free simultaneously with either rich endpoint.  Taking
the logical negation gives (3.1).  \(\square\)

### Corollary 3.2 (the double contraction is exactly six-chromatic)

\[
                             \chi(G/e/f)=6.             \tag{3.3}
\]

#### Proof

The proper minor is six-colourable.  If it had a colouring using at most
five colours, a sixth globally unused colour would make `z`, `x`, and `y`
free in its lift.  Theorem 3.1 would six-colour `G`.  \(\square\)

## 4. A literal leaf consequence

Let `B` be a selected path-or-`Y` carrier core in the rich shore and let
`f=xy` be an edge incident with a leaf `x` of that selected core.  The word
"selected" is essential: `G[V(B)]` may have chords and components of
`R-B` may attach back to several vertices of `B`.

### Corollary 4.1 (support five or a genuine off-core attachment)

If the rich alternative of (3.1) holds, then for the leaf `x` at least one
of the following is true:

1. `x` has neighbours in at least five distinct literal boundary vertices;
2. `x` has a chord to `V(B)-{x,y}`; or
3. `x` has a neighbour in `R-V(B)`, hence lies on a literal `B`-bridge.

#### Proof

The mate `y` has colour `c(x)`, so it witnesses none of the five alternative
colours.  Rich saturation supplies five distinct neighbours of `x`, one in
each alternative colour.  There is no `A-R` edge.  If none is a chord or an
off-core rich neighbour, all five lie in `S`, where they are distinct.
\(\square\)

This is a genuine geometric signal but not yet a branch-set theorem.  In
particular, neither colour saturation nor five boundary contacts by itself
supplies the disjoint labelled carriers required by the active composition.

## 5. Edgewise chromatic fork and the literature input

For every rich edge `f=xy`,

\[
                        5\le\chi(G-\{x,y\})\le6.       \tag{5.1}
\]

The upper bound follows by deleting one vertex from the seven-critical
graph and then deleting the second.  If the graph on the left were
four-colourable, two fresh colours on the adjacent vertices `x,y` would
six-colour `G`, proving the lower bound.

If equality is five, `xy` is a double-critical edge of the seven-chromatic
graph.  The proof of Proposition 3.3 and Corollary 3.1 of Kawarabayashi,
Pedersen and Toft is edge-local: in every five-colouring of `G-{x,y}`,
the common neighbourhood of `x,y` contains every one of the five colours,
and every prescribed sequence of distinct colours occurs internally on an
`x-y` generalized Kempe path.  This is a potentially label-faithful source
of extra routes for the rich-saturation branch.

If equality is six, known `HC_6` regenerates an unrooted `K_6` minor in
`G-{x,y}`.  That does not ensure that its six bags meet prescribed boundary
labels or both ends of `f`; it is therefore only a near-model regeneration
input, not a terminal outcome.

Primary source:
[Kawarabayashi--Pedersen--Toft, *Double-critical graphs and complete
minors*](https://doi.org/10.37236/359), Proposition 3.3 and Corollary 3.1.

## 6. Exact remaining step

The active atomic milestone should now be phrased around the shared
double-contraction colourings, not an unexplained intersection of two
independently chosen state languages:

* in the thin-saturation branch, convert the five coloured neighbours of
  `z` and the compulsory bridge fan into two legal adjacent thin carriers,
  or a strict state-carrying descent;
* in the rich-saturation branch, use Corollary 4.1 and the edgewise fork to
  obtain the required carrier reassignment, a literal terminal model, or a
  strict descent.

A proof must recompute literal carrier contacts and preserve the attained
boundary state.  Merely producing an unrooted `K_6` or five Kempe paths does
not discharge this step.
