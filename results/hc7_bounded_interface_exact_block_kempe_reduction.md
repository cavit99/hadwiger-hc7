# Exact-block Kempe reduction at a bounded anti-neighbourhood boundary

**Status:** written proof; separate internal audit GREEN.  This is a conditional structural
reduction inside the bounded-interface programme.  It does not prove
`HC_7`, does not synchronize the two closed shores, and does not identify
colour classes with clique-minor branch sets.

## 1. Setup

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`, and use
the notation supplied by the low-degree adjacent-pair theorem.  Thus `u`
has degree between seven and nine, `C` is a component of `G-N[u]`,

\[
 S=N_G(C),\qquad A=G[C\cup S],\qquad B=G-C,
\]

and

\[
 7\le |S|\le d_G(u)\le9,\qquad S\subseteq N(u).
\]

Both closed shores are six-colourable, their boundary extension languages
are disjoint, and, for every nonempty independent set `I` of `G[S]`, both
closed shores admit a six-colouring in which `I` is exactly one boundary
colour class.

Write `T=N(u)-S`; then

\[
                              |T|\le2.                 \tag{1.1}
\]

## 2. Boundary sparsity after fixing one exact block

### Lemma 2.1

For every nonempty set `I\subseteq S`, the graph `G[S-I]` is
four-degenerate.

### Proof

Suppose that a subgraph `H` of `G[S-I]`, on `h` vertices, has minimum
degree at least five.  Since `I` is nonempty and `|S|\le9`, one has
`h\le8`, and

\[
                         |E(H)|\ge \frac52h.           \tag{2.1}
\]

Contracting `C` gives two nonadjacent vertices, namely the image of `C`
and `u`, each complete to `S`.  Hence

\[
                         \overline K_2\vee H
\]

is a `K_7`-minor-free minor of `G`.  It has `h+2` vertices and at least

\[
                         2h+\frac52h=\frac92h          \tag{2.2}
\]

edges.  Mader's exact `K_7` extremal bound gives at most

\[
                         5(h+2)-15=5h-5               \tag{2.3}
\]

edges.  But `9h/2>5h-5` for `h<10`, a contradiction.  Thus every
nonempty subgraph of `G[S-I]` has a vertex of degree at most four.  \(\square\)

### Corollary 2.2 (connected exact-block cylinder)

Fix a nonempty independent set `I` of `G[S]`.  Any two labelled proper
six-colourings of `G[S]` in which `I` is exactly one colour class are
joined by a sequence of boundary Kempe interchanges that never changes
the colour on `I` and never assigns that colour to `S-I`.

### Proof

Rename the common colour on `I` to colour six in both colourings.  Their
restrictions to `S-I` are proper colourings with the other five colours.
By Lemma 2.1, `G[S-I]` is four-degenerate.  The Las Vergnas--Meyniel
degeneracy theorem says that all `k`-colourings of a `(k-1)`-degenerate
graph are Kempe equivalent.  Apply it with `k=5`.  Each interchange is on
colours different from six and is therefore also a Kempe interchange of
`G[S]` leaving the exact block `I` fixed.  \(\square\)

The cited theorem is the standard result of Las Vergnas and Meyniel,
*Kempe classes and the Hadwiger Conjecture*, J. Combin. Theory Ser. B 31
(1981), 95--104.

## 3. The exact shore obstruction to one boundary interchange

The next elementary lemma records the literal information lost by looking
only at a boundary equality partition.

### Lemma 3.1 (Kempe lift or an interior bridge)

Let `Y` be either closed shore, let `c` be a six-colouring of `Y`, and let
`W` be one component of the subgraph of `G[S]` induced by two colours
`alpha,beta`.  Interchange `alpha,beta` on `W` in the boundary colouring.
Then either the new boundary colouring extends to `Y`, or
`Y[alpha,beta]` contains a path joining `W` to `S-W` whose internal
vertices lie in `Y-S`.

### Proof

Consider all `alpha`--`beta` components of `Y` that meet `W`.  If none
meets `S-W`, interchange the two colours on their union.  The resulting
colouring of `Y` induces exactly the desired boundary interchange.

Otherwise one such component meets both `W` and `S-W`.  A shortest path
inside it between those two boundary sets has no internal vertex in `S`:
an internal boundary vertex would give an earlier hit in one of the two
sets.  This is the asserted path.  \(\square\)

## 4. A canonical two-ended transition

### Theorem 4.1 (exact-block boundary transition)

For every nonempty independent set `I` of `G[S]`, there are:

1. an exact-`I` boundary colouring extending to `A`;
2. an exact-`I` boundary colouring extending to `B`; and
3. a shortest Kempe sequence between such choices, entirely within the
   exact-`I` cylinder of Corollary 2.2,

with the following properties.

At the first interchange, the old boundary colouring extends to `A` and
the new one does not.  Consequently every extension of the old colouring
to `A` contains a bichromatic path through `C` joining the interchanged
boundary component to another boundary component.

At the last interchange, the new boundary colouring extends to `B` and
the old one does not.  Fix an extension to `B`, and let `delta` be the
colour of `u`.  Exactly one of the following occurs.

1. **Pole-free bridge.**  The last interchange uses two colours different
   from `delta`.  There is a bichromatic path joining two distinct
   boundary components whose internal vertices lie in
   `B-(S\cup\{u\})`.
2. **Single-vertex pole move.**  The last interchange uses `delta`.  Since
   `u` is complete to `S`, colour `delta` is absent from `S`; hence the
   interchange recolours one boundary vertex `x` and no other boundary
   vertex.  In the reverse direction it assigns `x` the colour of `u`.

In the pole-free-bridge outcome, choose the returned path shortest between
its two boundary components.  Its interior meets at most three components
of `G-N[u]` other than `C`.  Every such component `D` satisfies

\[
                  |N_G(D)\cap S|\ge |S|-2\ge5.        \tag{4.1}
\]

### Proof

The exact-block trace theorem supplies the two endpoint colourings.  After
renaming the exact block to colour six, Corollary 2.2 supplies a Kempe
sequence.  Minimize its length over all endpoint choices.  The two shore
extension sets are disjoint, so its length is positive.  Minimality says
that only the first vertex of the sequence extends to `A` and only the
last extends to `B`; otherwise a shorter pair of endpoints could be used.
Lemma 3.1 at the first and last interchanges gives the two interior paths.
The first path has all internal vertices in `A-S=C`.

In a colouring of `B`, the colour `delta` of `u` is absent from `S`, since
`u` is adjacent to every boundary vertex.  If the last two interchange
colours avoid `delta`, the path from Lemma 3.1 avoids `u`.  If one colour
is `delta`, then `G[S]` has no vertex of that colour.  A two-colour
component on `S` involving `delta` is therefore a singleton (vertices of
the other one colour form an independent set).  This proves the displayed
dichotomy.

It remains to localize a pole-free path `P`.  The vertices outside
`N[u]` split into pairwise anticomplete components, one of which is `C`.
After removing `S`, `C`, and `u`, a path can move from one other such
component to another only through a vertex of `T=N(u)-S`.  A simple path
uses each member of `T` at most once.  By (1.1), `P` therefore meets at
most `|T|+1\le3` other components of `G-N[u]`.

For each such component `D`, seven-connectivity gives
`|N_G(D)|\ge7`, while `N_G(D)\subseteq N(u)` and `|N(u)|=d_G(u)\le9`.
Thus

\[
 |N_G(D)\cap S|
 \ge |N_G(D)|+|S|-d_G(u)
 \ge 7+|S|-9=|S|-2,
\]

which proves (4.1).  \(\square\)

## 5. Canonical use of an edge-deletion response

The preceding transition can be anchored at a colouring of one proper
minor.  This removes the single-vertex pole move from the first geometric
obstruction.

### Theorem 5.1 (pole-edge response gives a pole-free bridge)

For every `x\in S`, some six-colouring of `G-ux` arising during the
construction below and some pair of its colours give a bichromatic path with ends in
distinct two-colour components of `G[S]`, internal vertices outside `S`,
and all internal vertices contained either in `C` or in
`B-(S\cup\{u\})`.  In the latter case its interior meets at most three
components `D` of `G-N[u]` other than `C`, and every such `D` satisfies
(4.1).

### Proof

Delete the edge `ux`.  A six-colouring `phi` of the proper minor `G-ux`
gives `u,x` the same colour: otherwise it would already colour `G`.
Because `u` is adjacent to every member of `S-x`, the singleton `{x}` is
an exact boundary colour class under `phi`.

The exact-block trace on `B` supplies a six-colouring of `B` in which
`{x}` is also an exact boundary colour class.  Rename colours so that the
two boundary colourings agree on the colour of `x`.  Corollary 2.2 gives a
boundary Kempe sequence between them which never uses that colour.

Starting with `phi`, try to lift the sequence inside the whole graph
`G-ux`.  At each step, interchange the two colours on the union of all
full two-colour components meeting the chosen boundary component.  This
realizes the requested boundary step unless one of those full components
also meets another boundary component.  If every step were realized, the
final colouring of `G-ux`, restricted to `A`, would have the same boundary
colouring as the chosen colouring of the original closed shore `B`.
Gluing those two restrictions would six-colour `G`, a contradiction.

At the first failed step, a shortest path in the obstructing two-colour
component between the two boundary components has all internal vertices
outside `S`.  Neither `u` nor `x` lies on it, since both retain the fixed
colour excluded from every interchange.  The separation has no edge from
`C` to `B-S`, so the path interior lies wholly in `C` or wholly in
`B-(S\cup\{u\})`.  In the second case, the localization proof at the end
of Theorem 4.1 applies verbatim and gives the final assertions.  \(\square\)

## 6. Consequence and exact remaining gate

Theorems 4.1 and 5.1 eliminate arbitrary boundary-state drift inside any fixed
exact independent block.  The two shore languages cannot merely occupy
unrelated regions of the boundary recolouring space: a shortest transition
has a literal path through `C` at one end and, at the other end, either a
path avoiding the universal pole and supported by at most three
almost-full anti-neighbourhood components, or one critical pole edge
`ux`.

More sharply, anchoring the transition at the actual colouring of `G-ux`
forces a pole-free path for every `x\in S`; its interior lies in one
literal open shore and has the localization stated in Theorem 5.1.

This does **not** yet prove a common boundary partition.  Full
contraction-criticality still selects an uncontrolled colouring after a
proper-minor operation.  In particular, contracting a returned path need
not preserve its endpoint boundary colouring.  The next positive lemma
must convert one of the two outcomes in Theorem 4.1 into an explicit
`K_7`-minor model, a smaller bounded anti-neighbourhood interface, or a
common shore partition.  Treating the returned path as an extra edge while
simultaneously retaining the same shore as a full branch set is not valid
without an explicit split.
