# Normal form for concentrated missing-colour rotations

**Status:** written proof; separate internal audit GREEN.  This note identifies
exactly what a concentrated missing-colour rotation changes after the buffer
colour is normalized.  It also records a limitation: the rotations alone
cannot improve a fixed uncoloured `K_6` model or a fixed linkage.

## 1. Setup

Let `G` be a seven-connected, seven-chromatic graph such that every proper
minor is six-colourable.  Let `zu` be an edge for which

\[
                         H=G-\{z,u\}
\]

has chromatic number six.  Fix a proper six-colouring `phi` of `H` with a
colour `alpha` absent from both pole neighbourhoods, while each pole has a
neighbour of every colour different from `alpha`.

Fix `beta != alpha`.  Assume that the `alpha`--`beta` pole support is
concentrated in the sense of the audited bichromatic-support dichotomy:
there is exactly one component `K_beta` of

\[
             H[\phi^{-1}(\{\alpha,\beta\})]
\]

which contains a neighbour of either pole, and it contains neighbours of
both poles.  Call every other component of this two-colour subgraph
**inactive**.  Thus an inactive component has no neighbour in `\{z,u\}`.

Interchanging `alpha,beta` on `K_beta` produces a colouring in which
`beta` is absent from both pole neighbourhoods.  We call this the direct
missing-colour transition from `alpha` to `beta`.

## 2. Exact normalization

### Theorem 2.1 (normalized rotation identity)

Perform the direct transition from `alpha` to `beta`, and then globally
interchange the names `alpha,beta` so that the common missing colour is
again called `alpha`.  The resulting colouring is obtained from `phi`
by interchanging `alpha,beta` on every inactive component and nowhere
else.

In particular:

1. every vertex of `K_beta` retains its original colour;
2. every pole neighbour retains its original colour; and
3. the normalized transition fixes `phi` if and only if `K_beta` is the
   whole subgraph induced by the two colour classes `alpha,beta`.

#### Proof

On `K_beta`, the direct transition interchanges `alpha,beta`, and the
subsequent global renaming interchanges them a second time.  Hence the
original colours are restored there.

On every other `alpha`--`beta` component, the direct transition does
nothing and the global renaming interchanges the two colours once.  Every
vertex of any other colour is untouched by both operations.  This proves
the identity.

Neither pole has an `alpha`-coloured neighbour, and concentration places
every `beta`-coloured pole neighbour in `K_beta`.  The inactive components
are therefore anticomplete to both poles.  The identity consequently fixes
the colour of every pole neighbour.  Its fixed-point statement follows
because every component under discussion is nonempty. \(\square\)

### Corollary 2.2 (inactive-component separator)

Let `L` be an inactive `alpha`--`beta` component.  Then

\[
                         N_G(L)=N_H(L)
\]

is an actual vertex separator of `G`.  Its vertices use only the four
colours outside `\{alpha,beta\}`, and

\[
                         |N_H(L)|\ge 7.                \tag{2.1}
\]

Equality in (2.1) gives an actual order-seven separation with `L` on one
open side and both poles on the other.

#### Proof

Inactivity says that `L` is anticomplete to the poles.  Since `L` is a
component of the subgraph induced by the `alpha,beta` classes, no vertex
of either colour outside `L` is adjacent to `L`.  Thus every neighbour of
`L` lies in `H` and has one of the other four colours.

After deleting `N_H(L)`, the nonempty set `L` has no edge to its
complement.  The adjacent vertices `z,u` remain outside `L`, so the
complement is nonempty as well.  Hence `N_H(L)` is an actual separator of
`G`.  Seven-connectivity proves (2.1), and the equality case is immediate.
\(\square\)

The separator in Corollary 2.2 is different from the separator in the
diffuse-support alternative.  Diffuse support puts one or two poles into
the separator; an inactive component is anticomplete to both poles and
therefore has a separator entirely inside `H`.

## 3. Collapse of a separator-free transition orbit

Consider the orbit obtained by repeatedly applying direct missing-colour
transitions, retaining the actual colour names.  At a colouring whose
common missing colour is `m`, the five possible moves interchange `m`
with one of the other colours on the corresponding pole-support component.

### Corollary 3.1 (global-relabel orbit)

Suppose that, at every colouring in this orbit and for every available
transition, the pole-support component is the entire subgraph induced by
the two colours involved.  Then every transition is a global interchange
of those two colour names.  Consequently the orbit contains no colouring
information beyond global permutations of the original six colour
classes.

Conversely, if some concentrated transition is not a global colour
interchange, its normalized form changes at least one inactive component,
and Corollary 2.2 exposes a four-coloured-boundary separator.

#### Proof

If the pole-support component is the whole two-colour subgraph, the direct
transition interchanges the two colours at every vertex having either
colour.  It is exactly their global transposition.  Repeating such moves
only globally permutes the six original colour classes.  Transpositions
between the current missing colour and any other colour generate all
permutations, although only the absence of new internal data is needed.

The converse is Theorem 2.1 and Corollary 2.2. \(\square\)

## 4. Consequence for a fixed minor model and linkage

Fix a spanning `K_6`-minor model of `H`, fixed selected neighbours of the
two poles, and fixed paths between those selected neighbours.  A normalized
concentrated rotation preserves

* every branch set and every pole--branch-set contact;
* every selected pole-neighbour and its colour; and
* every path, its branch-set interval sequence, and its length.

Hence it preserves each coordinate of the current joint score

\[
  (\text{number of common-contact branch sets},
    \text{number of contacted branch sets},
    -\text{path--branch-set interval changes},
    -\text{total path length}).
\]

This is not merely an example of cycling: it follows from the exact
identity in Theorem 2.1.  A strict model improvement cannot come from the
colour rotation alone.  It must use an additional rule which regenerates
or reroutes the model or paths using the changed inactive components.  But
those components already have the separator described in Corollary 2.2.
If there are no inactive components anywhere in the orbit, the rotations
are only global colour relabellings and supply no regeneration data at all.

Thus a minimal-transition-component argument has the following precise
fork:

1. a nontrivial normalized rotation exposes a separator whose boundary is
   four-coloured in the current proper-minor colouring; or
2. all rotations are global relabellings, and the next theorem must use
   information beyond the rotation orbit--for example a genuinely rooted
   model theorem or proper-minor colouring compatibility across a
   separator.

The first outcome does not yet give a colour-gluable separation: its order
can exceed seven, and the displayed four-colour boundary pattern need not
be induced by compatible proper-minor colourings on both closed sides.
The second outcome does not imply that every pair of nonbuffer colour
classes induces a connected graph, so Kriesell's theorem on
Kempe-colourings cannot be invoked from this star of two-colour connections
alone.

## 5. Guardrail

Complete-join planar examples remain sharp for the conclusion.  In a
graph of the form `K_2` joined to a five-connected planar graph, the added
pair is a coherent two-vertex obstruction and minimum-degree vertices give
order-seven separators.  Such examples can realize concentrated initial
pole support and nontrivial inactive components.  They confirm that the
separator/fixed-pair alternatives cannot be discarded.  They are not
hypothetical `HC_7` counterexamples because they are six-colourable; the
missing input is precisely the compulsory response supplied by
seven-chromatic minor-criticality.
