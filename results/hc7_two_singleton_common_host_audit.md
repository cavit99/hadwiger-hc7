# Audit: two nonadjacent singleton roots over a common host

**Verdict:** GREEN.  All five conclusions follow from the stated
hypotheses.  The connectivity calculation, the use of the known case
`HC_6`, the spanning-model absorption, and both opposite colouring
witnesses are valid.

**Audited source:** `results/hc7_two_singleton_common_host.md`.

**Source SHA-256:**
`4abda28600ee5acb22bf56f1946e0ea2499d2bc5b2d90f65ad2ba1dd10b40c75`.

The post-audit change only replaced the draft status with a link to this
audit; the mathematical statement and proof are unchanged.

## 1. Exact chromatic number of the common host

The graph

\[
                         J=G-\{a,b\}
\]

is a proper minor, so the strong contraction-critical hypothesis gives
`chi(J)<=6`.  If `J` had a proper five-colouring, assigning one new sixth
colour to both `a` and `b` would be legal: `ab` is absent, and that colour
does not occur on `J`.  It would six-colour `G`, contrary to `chi(G)=7`.
Thus `chi(J)=6` exactly.

This argument uses nonadjacency of `a,b` essentially.  It does not extend
unchanged to an adjacent prescribed pair.

## 2. Connectivity and the order-seven-separation alternative

Let `X` be a vertex cut of `J`.

* If `|X|<=4`, then deleting `X union {a,b}` disconnects `G`, because the
  distinct components of `J-X` still have no edges between them after
  `a,b` are deleted.  This is a cut of order at most six, contradicting
  seven-connectivity.  Hence `J` is five-connected once the graph-order
  convention is checked.
* If `|X|=5`, the same deletion produces a cut of order seven.  Taking one
  component of `J-X` on one side and all remaining components on the other
  gives a separation whose intersection is exactly
  `X union {a,b}` and whose two open sides are nonempty.  It is therefore
  an actual order-seven separation as defined in the source.  Under the
  additional hypothesis excluding such separations, no cut of `J` has
  order at most five.

It remains to ensure that `J` has enough vertices for the standard
definition of six-connectivity.  A seven-connected graph has at least
eight vertices.  If `|J|<=6`, then necessarily `|G|=8`; seven-connectivity
forces minimum degree at least seven, so `G=K_8`, which has a `K_7` minor.
This contradicts the hypotheses.  Hence `|J|>=7`, and the source correctly
concludes that `J` is five-connected unconditionally and six-connected
when actual order-seven separations are absent.

No minimality of `X` is required for either argument.

## 3. `HC_6` and absorption to a spanning model

The known parameter-six case of Hadwiger's conjecture says that every graph
with no `K_6` minor is five-colourable.  Since `chi(J)=6`, its
contrapositive gives a `K_6`-minor model in `J`.

The absorption step is valid because `J` is connected.  Every component
of the vertices outside the six branch sets has an edge to their union;
otherwise it would be a component of `J` disjoint from the model.  Assign
such a component to a branch set it meets.  The enlargement remains
connected and disjoint from every other branch set and preserves all old
inter-branch-set edges.  Assigning every unused component therefore makes
the model branch sets partition `V(J)`.

The conclusion is only an unlabelled spanning `K_6` model.  Absorption does
not preserve any prescribed attachment of `a` or `b` to named branch sets.

## 4. Universal colour-dominating alternative

Take any proper six-colouring `c` of `J`.  If both `a` and `b` missed a
colour on their respective neighbourhoods in `J`, choose such colours
`alpha` and `beta` and assign them to `a` and `b`.  These choices are legal
against every neighbour in `J`; the only possible additional obstruction
would be `ab`, which is absent.  The colours need not be distinct.  The
extension would six-colour `G`, a contradiction.

Thus in every six-colouring of `J`, at least one of the two literal
neighbourhoods contains all six colours.  This is a disjunction depending
on the colouring; the theorem does not select one vertex that dominates
the palette in every colouring.

## 5. Opposite proper-minor witnesses

The deletion `G-a` is a proper minor and hence has a proper six-colouring
`c_a`.  Its restriction to `J` is proper.  Because `b` is a coloured
vertex, properness gives

\[
                         c_a(b)\notin c_a(N_J(b)).
\]

Consequently `b` does not see all six colours in `J`, so the universal
alternative from Section 4 forces `a` to see all six colours there.
Although `a` is not a vertex of `G-a`, this statement is well-defined: it
only evaluates the colours on the set `N_J(a)`, all of whose vertices lie
in the coloured graph.  Interchanging `a,b` gives the second colouring and
the opposite pair of conditions.

There is no hidden issue if the chosen colouring of `G-a` is initially
described as using "at most" six colours.  Its induced colouring on `J`
must use all six because `chi(J)=6`.

## 6. Exact limitations

The proof establishes a useful common host with:

* chromatic number six;
* connectivity five, or six after excluding actual order-seven
  separations;
* an unlabelled spanning `K_6`-minor model; and
* two opposite colouring witnesses.

It does **not** prove that either colouring is compatible with a chosen
minor model, that `a` or `b` meets every branch set, that the two witnesses
are Kempe-equivalent, or that the host contains a rooted `K_6` model with
prescribed labels.  The final scope paragraph of the source states this
remaining colouring-to-labelled-model problem accurately.
