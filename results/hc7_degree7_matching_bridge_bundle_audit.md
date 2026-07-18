# Independent audit: exact matching languages and disjoint Kempe bridges

Audited file: `results/hc7_degree7_matching_bridge_bundle.md`.

Audited SHA-256:

```text
7fda58a909aabf5a49c32be513ebc598695c448855a4a8bede3ae1efdc63314a
```

**Verdict:** **GREEN** for the theorem as written at the hash above.

The audit checked the exact two closed-shore extension languages, the use of
one fixed colouring for all bichromatic paths, the five-colour restriction
needed for Kriesell--Mohr's Theorem 7, the rooted-`K_5`
connector-or-separator dependency, Corollary 3.6, and every asserted
separator/fullness conclusion.

## 1. Exact matching languages

Because `alpha(H)<=2`, every colour block on the seven-vertex boundary is
either a singleton or an edge of `F=overline H`; hence its two-vertex blocks
form a matching and the number of boundary blocks is `7-|M|`.

On `B=G[N[u]]`, the colour of `u` is absent from `S`, so precisely the
matchings of order at least two occur: every such matching has at most five
blocks and extends by giving `u` a sixth colour.

On `A=G-u`, every six-colouring has at most six boundary blocks and therefore
a nonempty matching.  A matching of order at least two would also extend to
`B`; after a palette permutation the two colourings would agree on `S` and
glue, contradicting `chi(G)=7`.  Conversely, contracting the star on
`{u,a,b}` for any `ab in E(F)` forces `{a,b}` to be an exact block, and the
preceding exclusion prevents any second pair.  Thus both equalities in
Theorem 2.1 are exact.

## 2. One-colouring disjoint path bundle

Fixing the one-edge boundary matching `{e_0}` fixes one six-colouring `c` of
`A`.  Every endpoint of an edge disjoint from `e_0` is a singleton boundary
block and these endpoints consequently have pairwise distinct colours.

For `e_i=p_iq_i`, if `p_i` and `q_i` lay in different components of their
two-colour graph, a Kempe swap on the component containing `p_i` would create
the forbidden boundary matching `{e_0,e_i}`.  Hence a shortest path between
them exists in that same two-colour graph.  No internal boundary vertex can
occur because `p_i,q_i` are the only boundary vertices with those two
colours.  Distinct matching edges use disjoint pairs of colour classes, so
their entire bichromatic induced subgraphs, not just selected paths, are
vertex-disjoint.  This validates the simultaneous and same-colouring claims
in Theorem 3.1 and Corollaries 3.2--3.4.

The complement is triangle-free because a triangle in `F` would be an
independent triple in `H`.  The star-versus-disjoint-pair conclusion is
therefore the standard classification of a pairwise-intersecting family of
two-element sets, with the triangular family excluded.

## 3. Kriesell--Mohr application

The primary source defines property `(*)` for a graph `K` using a colouring
with exactly `|V(K)|` colour classes and a transversal of those classes.
Its Theorem 7 states that every five-vertex graph with at most six edges has
property `(*)`.

The proof now makes the necessary restriction explicitly: `A'` is induced
by the five colour classes meeting `U`, while the sixth class containing
`a,b` is deleted.  Each required bichromatic path uses two of those five
classes and therefore remains in `A'`.  Since `F[U]` is triangle-free,
Mantel gives `|E(F[U])|<=6`, so Theorem 7 yields an `F[U]`-rooted certificate
in `A'`.  For every complementary pair the two roots are adjacent by a
literal edge of `H[U]`; because each root lies in its named bag, these edges
complete the certificate to a `U`-rooted `K_5` model.  No vertex of the
sixth colour class is used, so the model lies in `A-{a,b}` as required.

Primary source: M. Kriesell and S. Mohr, *Kempe Chains and Rooted Minors*,
arXiv:1911.09998, definition of property `(*)` and Theorem 7.

## 4. Connector-or-separator dependency

The dependency's hypotheses are all present:

* `u` has degree seven and `ab` is a nonedge;
* the star contraction gives the exact trace with five distinct root
  colours;
* the preceding step gives the rooted `K_5` in `A-{a,b}`; and
* `{a,b}` jointly dominates `U`, since otherwise `a,b` and a missed root
  form an independent triple in `H`.

The connector outcome gives six pairwise adjacent branch sets in `G-u`, and
`{u}` completes them to a `K_7` model.  In the other outcome, an
inclusion-minimal `a-b` separator `Z` contained in the five rooted bags has
order at least six because `A=G-u` is six-connected.  Minimality makes both
distinguished components of `A-Z` adjacent to every vertex of `Z`.  Adding
`u` to the boundary produces an actual separation of `G`: the two components
contain `a` and `b`, respectively, so each is also adjacent to `u`.  Hence
their full neighbourhood is `Z union {u}`.  Six vertices distributed among
five disjoint bags also force the asserted double hit.

The dependency theorem itself was rechecked in this audit.  Its adjacent
legacy audit is mathematically GREEN but predates the repository's current
hash-pinning convention; before this bundle is put on the active proof
spine, that older audit should record the dependency source hash
`2ee51a2af500d8d208964e130ac3008e937b2c05dcc1231e7f13cf7ce340dda8`.
This is a provenance repair, not a mathematical gap in the bundle.

## 5. Corollary 3.6 and separator accounting

Since `A` is six-connected and `a,b` are nonadjacent, their minimum vertex
separator has order at least six.  If the minimum is six, an
inclusion-minimal separator `Q` is full to the two distinguished components;
`Q union {u}` is therefore an actual full order-seven boundary in `G`.  If
the minimum is at least seven, Menger gives seven internally vertex-disjoint
`a-b` paths.  In the non-`K_7` branch the rooted-model union separates
`a,b`, so every one of those paths meets it.

The audited source uses only the valid pigeonhole consequence: at least one
of five rooted bags meets at least two of the seven paths.  More precisely,
after assigning one met bag to each path, either one bag receives at least
three paths or two bags receive at least two each.  The stronger unqualified
claim that two bags must receive multiple hits was removed before this hash
was taken.

For Proposition 7.1, every component `R` of `C-Z` has

```text
N_G(R) = N_S(R) disjoint-union N_Z(R),
```

because `C` is a component of `G-N[u]`.  If `R` is not `S`-full, `u` lies on
the opposite side of this neighbourhood, so seven-connectivity gives
`(7-d(R))+a(R)>=7`.  Equality is exactly an order-seven separation, while
strict inequality is the stated attachment surplus.  These conclusions do
not assume that `Z` is a tree or that a reserved component exists.

## 6. Remaining scope

The bundle does not prove `HC_7`.  It gives a simultaneous colour-indexed
path system, a rooted-`K_5`/full-separator dichotomy, and exact proper-minor
boundary responses.  It does not show that the seven-fold linkage can be
split label-faithfully, that a separator has order seven in every case, or
that the attachment-surplus alternative yields a strict descent.  Those
limitations are stated correctly in the source.
