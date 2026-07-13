# Blocker incidence around a minimal sole-exterior connector

## 1. Two different incidence notions

Retain the sole-exterior pure-Moser setting.  Put

\[
 I=\{a,b\}=\{1,3\},\qquad
 U=\{0,5,2,4,6\},
\]

and let `F` be the missing `C5` on `U`.  Let `P` be a minimum-order
`I`-carrier in the exterior `C`.  Minimality makes `P` an induced path

\[
 p_1p_2\cdots p_m,
\]

where only `p_1` sees `a` and only `p_m` sees `b`.

For a component `D` of `C-P`, put

\[
 T_D=N_P(D),\qquad R_D=N_S(D),\qquad S=N(v).
\]

There are two distinct support notions.

* `D` **carries** `xy in E(F)` if `x,y in R_D`.  Since `D` is
  connected, this gives an uncoloured `xy`-carrier.
* `D` **Kempe-supports** `xy` if the fixed `x,y`-bichromatic subgraph
  contains an `x-y` path with interior in `D`.

Kempe support implies carrier contact, but the converse need not hold.
Consequently a failure of fixed-colour support does not by itself imply
that `D` misses either endpoint.  Any incidence proof which replaces the
second notion by the first silently loses colour information.

If all five missing edges remain Kempe-supported in `H-P`, the
Kriesell--Mohr `C5` theorem gives the desired rooted `K5` disjoint from
`P`.  Four supported edges give only `K5-e` and are not a success
condition.

## 2. Exact carrier-blocker incidence

The following is the strongest conclusion obtainable from component
contact rows alone.

### Theorem 2.1 (vertex-cover/portal-surplus lemma)

Let `B subseteq E(F)` be a family of edges for which no component of
`C-P` carries the two ends.  For every component `D` of `C-P`, define

\[
 M_D=S-R_D.
\]

Then:

1. `M_D cap U` is a vertex cover of `B`;
2. either `T_D union R_D` is an exact seven-cut, or

   \[
   |T_D|\ge |M_D|+1\ge \tau(B)+1,                \tag{2.1}
   \]

   where `tau(B)` is the vertex-cover number of `B`.

In particular, outside the exact-adhesion outcome:

* one blocked edge forces at least two distinct `P`-portals in every
  component;
* two vertex-disjoint blocked edges force at least three;
* for two incident blocked edges `ux,uy`, a component missing `u` has
  at least two `P`-portals, while a component containing `u` must miss
  both `x,y` and has at least three `P`-portals.

### Proof

If `xy in B` and both ends belonged to `R_D`, connectedness of `D`
would make `D` an `xy`-carrier, contrary to the definition of `B`.
Thus `M_D cap U` meets every edge of `B`, proving item 1.

Because `D` is a component of `C-P`, and `C` is a component of `G-S`,
its full external neighbourhood is exactly

\[
 N_G(D)=T_D\mathbin{\dot\cup}R_D.                \tag{2.2}
\]

This set separates `D` from the apex shore.  Seven-connectivity gives
`|T_D|+|R_D| >= 7`.  Equality is the displayed exact seven-cut.  If
equality does not hold, integrality gives

\[
 |T_D|+|R_D|\ge8.
\]

Since `|R_D|=7-|M_D|`, this is (2.1).  The listed special cases are the
vertex-cover numbers of one edge and of two disjoint edges.  For two
incident edges, if the common end is present then both other ends must
be absent.  \(\square\)

### Scope warning

Theorem 2.1 applies to **carrier-blocked** edges.  If an edge merely
lacks a fixed bichromatic path in every component, a component may still
contact both roots, and even the vertex-cover conclusion can fail.

## 3. Minimality turns surplus portals into metric locks

The portal lower bounds do not by themselves shorten `P`.  They instead
force an ordered ear geometry.

### Lemma 3.1 (geodesic ear inequalities)

Let `D` be a component of `C-P`.

1. If a path `Q subseteq D` with `q` vertices joins a neighbour of
   `p_i` to a neighbour of `p_j`, where `i<j`, then

   \[
   q\ge j-i-1.                                   \tag{3.1}
   \]

2. If `D` contacts `a` and a `q`-vertex path in `D` runs from an
   `a`-portal to a neighbour of `p_j`, then

   \[
   q\ge j-1.                                     \tag{3.2}
   \]

3. Symmetrically, if `D` contacts `b` and such a path ends next to
   `p_j`, then

   \[
   q\ge m-j.                                     \tag{3.3}
   \]

### Proof

For item 1, replace the internal subpath
`p_{i+1},...,p_{j-1}` by `Q`.  The resulting `I`-carrier has

\[
 i+q+(m-j+1)
\]

vertices.  Minimum-order choice of `P` says this is at least `m`, which
is (3.1).  For item 2, use `Q` followed by
`p_j,...,p_m`; its order is `q+m-j+1`.  Minimality gives (3.2).
Item 3 is the reversed argument.  \(\square\)

Thus a strict-surplus blocker is not automatically a packet-deficient
shore.  It may be a long multi-portal ear whose internal distances exactly
match the order of its attachments on `P`.  Eliminating this possibility
requires an ear exchange or an internal minor transition; counting portal
incidences is insufficient.

## 4. Why the proposed packet reduction cannot target the original shore

The palette-wall axiom has a consequence in the opposite direction.
By the cross-trace two-linkage theorem in
`hadwiger_sole_exterior_cross_trace_linkage.md`, every two
vertex-disjoint Moser nonedges have disjoint carriers in the original
shore `C`.  Hence for every matching mode

\[
 A\mid B\mid K\mid\{r\},qquad |A|=|B|=|K|=2,
\]

the shore `C` has two-block capacity (indeed for every selected pair of
the three blocks).  Therefore `C` is never packet-deficient for such a
mode.

The arbitrary-shore packet-or-exact-adhesion theorem can enter only after
one of two additional operations:

1. Theorem 2.1 already gives `|T_D|+|R_D|=7`, producing a new full shore
   behind an exact adhesion; or
2. an internal deletion/contraction of the connector creates a genuinely
   new accepting shore/state relation.

There is no direct implication

\[
 \text{component blocker incidence}
 \Longrightarrow
 \text{packet-deficiency of the original full shore}.
\]

This is not merely an unproved step: it contradicts the palette-wall
cross-trace linkage theorem.

## 5. Correct next exchange statement

The incidence programme reduces rigorously to the following operation-level
lemma.

> **Multi-portal ear exchange.**  Let `P` be a minimum `13`-connector.
> Suppose a carrier-blocked edge family `B` gives no exact cut in
> Theorem 2.1.  Thus every blocker component has at least
> `tau(B)+1` attachments to `P`, satisfying the geodesic inequalities
> (3.1)--(3.3).  Then an internal deletion or contraction on one interval
> of `P`, together with the palette-wall transition state, either reroutes
> `P` past one blocked support, produces a rooted model using a different
> exact trace, or exposes an exact seven-adhesion.

This statement uses precisely the information absent from an incidence
table: the order of the portals on `P` and the new boundary state created
by an operation between consecutive portals.

Finally, the earlier protected-support concentration theorem still closes
the short case `|P|<=2`.  It must not be applied to an arbitrary long
minimum connector: cross-trace linkage supplies, for each demand edge, a
possibly different `13`-connector avoiding it, and minimality alone does
not transfer that avoidance to the chosen `P`.

## 6. Sharp incidence-only counterarchitecture

The dependency-assisted verifier
`moser_long_connector_incidence_probe.py` constructs a graph showing that
the operation-level qualification above is necessary.  It has:

* the pure-Moser boundary and sole exterior;
* connectivity seven, with the original boundary as its only minimum cut;
* a minimum `13`-connector of order three;
* exactly one carrier-blocked missing-cycle edge after deleting that
  connector;
* two blocker components, each with eight external neighbours, so neither
  gives an exact seven-cut; and
* two-block capacity in the original shore for every pair of disjoint
  Moser nonedges.

The graph deliberately does **not** satisfy the six-colour exact-state
axiom (its dense blocker modules have larger chromatic number).  It is
therefore not a counterexample to the palette-wall synchronization lemma.
It is a counterexample to the purely incidence-theoretic inference from a
blocked support to either a nested exact cut or a packet-deficient original
shore.  The missing palette-wall transition must be used as an operation,
not merely listed among the hypotheses.

