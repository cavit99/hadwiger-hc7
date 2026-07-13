# Audit of the state-forcing column gammoid theorem

## Verdict

**GREEN AS PATCHED.**  The Rado/Perfect quantifiers, the protected-carrier
lift, and the `K_4`-join-independent-seven counterexample are correct.
Two wording defects were patched in the main note:

* the artificial vertex adjacent to a target family is a protected
  terminal, not generally a degree-one leaf; and
* the two clauses in Theorem 2.1 are equivalent, so they apply together
  rather than “exactly one” applying.

## 1. Rado and Perfect quantifiers

The source sets may overlap.  Rado's theorem is being applied to a
matroid on their union, so an independent transversal automatically
chooses distinct source vertices.  The strict-gammoid rank of a set `X`
is exactly the maximum number of vertex-disjoint paths from distinct
members of `X` to distinct vertices of `T`.  Therefore the condition

\[
 r\left(\bigcup_{i\in I}S_i\right)\ge |I|
 \quad\hbox{for every }I\subseteq[m]
\]

is precisely Rado's necessary and sufficient condition.  Failure gives
a nonempty deficient `I`; vertex Menger then gives a transversal of all
`(union_{i in I}S_i)`--`T` paths of order equal to the displayed rank,
hence below `|I|`.

Menger separators here are allowed to contain source or target vertices.
This causes no error in Corollary 1.2.  Since the source union has order
at least `|I|>|Z|` and `|T|=4>|Z|`, a source and a target both survive.
Their absence of a connecting path makes `H-Z` disconnected, contradicting
four-connectivity because `|Z|<=3`.

For target families, the artificial protected terminals correctly encode
an arbitrary bijection.  In a full `m`-linkage to `m` terminals every
terminal is an endpoint of one path, so no terminal can occur internally
on another disjoint path.  Deleting the final artificial edges leaves
distinct original endpoints in the named target families.  A separator
using an artificial terminal does not automatically lift; the main note
records this qualification.

## 2. Protected carriers

After contracting the pairwise disjoint connected sets `C_i`, an
`m`-linkage from the `m` contracted vertices to the `m` targets uses every
source and every target exactly once.  Lifting its `i`th path together
with all of `C_i` produces disjoint connected protected bags.  Conversely,
a path chosen inside each protected bag contracts to such a linkage.

If a Menger set contains a contracted source `c_i`, its inverse image is
the whole `C_i`, which may be large.  Formula (2.2) is therefore the exact
lift.  Four-connectivity rules out a Menger set of at most three only when
it avoids all contracted carrier vertices; it does not rule out a
capacity-one warehouse.  This is the correct logical boundary.

## 3. Warehouse counterexample

For

\[
                       H=K_4\vee\overline{K_7},
\]

deleting at most three vertices leaves a vertex of the `K_4`, which joins
all remaining vertices, so `H` is four-connected.  The graph is chordal
with maximal cliques of order five, hence has treewidth four.  Since
`tw(K_6)=5`, it is `K_6`-minor-free and therefore certainly
`K_7`-minor-free.

The four displayed ordinary paths are disjoint.  But a protected bag for
`C_4=W=K_4` consumes all of `W`, while every path from any `a_i` to a
target uses `W`; hence no other protected bag can reach a target.  After
contracting `W`, the one-vertex separator is its image.  Its inverse image
has order four, exactly the minimum cut of `H`, so no order-three cut was
hidden in the construction.

## 4. Interface with the exact seven-adhesion task

The warehouse alternative is precisely capable of producing the residue

\[
                     Q\cup Z_D\cup Z_E
\]

from the two-carrier gate theorem: a small Menger certificate in the
contracted state graph may contain two capacity-one carrier images whose
inverse images are the two gate pairs.  Adding the neutral triangle then
gives an order-seven, rather than an order-at-most-six, separator.

The boundary-threshold theorem in
`hadwiger_exact_seven_two_gate_boundary_threshold.md` supplies an
independent restriction on this case: in a seven-connected
`K_7`-minor-free host the induced seven-boundary has at least four
nonedges, has missing-edge vertex-cover number at least three, and cannot
have missing graph `3K_2 dotunion K_1`.  Thus the warehouse cannot be
resolved by a dense two-pair boundary completion.

Critical anti-domination correctly removes the literal false-twin
warehouse and forces private distinguishing contacts.  Nothing in Rado,
Perfect, or four-connectivity proves those contacts bypass the protected
carrier images or are mutually disjoint.  A further contraction-critical
transition is genuinely required to turn them into state-forcing columns,
a common boundary state, or the coherent rural alternative.

