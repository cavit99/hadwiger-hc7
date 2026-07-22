# Audit: parallel common-root trace-cycle normalization

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_common_root_parallel_two_cycle_normalization.md`](hc7_common_root_parallel_two_cycle_normalization.md)

Audited source SHA-256:

```text
3717920f83ab38a59ed0a9486795b657cdc872ca7034781fba8f931bdee59d22
```

This is an internal mathematical audit, not external peer review.  I checked
the theorem against the cited audited inputs, with particular attention to
the fixed-extension quantifiers, lexicographic shortcuts, the odd-cycle
parity, and the fact that the conditional incidence test is not automatically
aligned with the parallel connector.

### Correction record

The preceding source revision stated Corollary 3.2 by retaining all
hypotheses of Sections 1--2 of the concentrated-reserve elimination.  That
wording inadvertently imported the earlier connector and disjoint
`T`-carrier whose coexistence is already ruled out by that result's Theorem
2.1.  It made the corollary formally vacuous, despite the intended proof
using only the ambient Section 1 setup, the independence bound, and the
root-to-`T` contacts.  The earlier GREEN audit did not catch this scope
defect and must not be relied upon for that formulation.

The revision audited here states the intended hypotheses explicitly and
expressly excludes any previously supplied connector or carrier.  The proof
below was rechecked under this corrected, nonvacuous formulation.

## 1. Fixed extensions and minimization

For the fixed coordinate `k`, the full two-colour component containing
`W_k` is unique in each of the two fixed shore colourings.  Every parallel
partner `l` therefore lies in those same two components, and connectedness
supplies a trimmed connector on each shore.  The finite lexicographic
minimum in (1.3) is consequently well defined.  Changing the partner in the
proof does not change either fixed colouring or silently select another
shore extension.

If a connector leaves and returns to one boundary trace, the intervening
excursion contains an open-shore vertex: a boundary-only excursion would
join two vertices inside the same component of the boundary two-colour
graph.  Replacing it inside that trace strictly lowers the first coordinate.
This proves the one-interval trace property.

If an incidental trace occurs on both connectors, the two prefixes ending
at its first occurrence are connectors for the new parallel pair consisting
of `k` and that trace.  Each discarded suffix must use an open-shore vertex
to reach the distinct old terminal trace.  The first coordinate again
strictly decreases.  Thus the no-common-incidental-trace conclusion uses
one pair of fixed extensions, not independently reselected colourings.

## 2. Sector count and anticompleteness

After the one-interval property, a connector visiting `s_Q` boundary traces
has exactly `s_Q-1` nonempty open-shore sectors.  The two trace-label sets
intersect exactly in their two endpoint labels, so equation (2.1) is exact
and the total number of sectors is at most `n`.

The strengthened sector assertions are valid under the open-only definition
given in the theorem.

- Opposite-shore sectors are anticomplete because `E,F` are distinct
  components of `G-N[u]`.
- A chord inside one sector shortcuts at least one open-shore vertex and
  lowers the first lexicographic coordinate.
- An edge between nonconsecutive same-shore sectors shortcuts an intervening
  open sector and again lowers the first coordinate.
- An edge between consecutive same-shore sectors either removes an
  open-shore vertex, lowering the first coordinate, or removes only their
  intervening incidental boundary trace, lowering the second coordinate.

Every shortcut remains in the same full two-colour component and preserves
the two endpoint traces.  It is therefore a valid competitor in (1.3).
This proves that each sector is induced and that all distinct sectors are
pairwise anticomplete; the adjacent-sector case has not been omitted.

## 3. The literal odd cycle and low-degree consequences

The two connector interiors lie in different exterior components.  Their
only possible common boundary traces are the two endpoints, because the
incidental trace sets are disjoint.  Trimming makes it possible to join the
two ends within each connected endpoint trace without meeting either
connector elsewhere.  The union contains a simple cycle, including the
cases where one or both joining paths are trivial.

The parity computation is correct.  On the terminal trace `W_l` the two
fixed colourings have the same boundary phase; on `W_k` their phases differ
by exactly one interchange.  The xor contributions from all four endpoints
cancel except for that one phase reversal, so the simple cycle is odd.
Both shore connectors have a nonempty open interior because distinct
boundary two-colour components cannot be joined inside the boundary.

The degree-eight and degree-nine conclusions are explicitly conditional on
the full hypotheses of the audited short-trace classification.  Under that
input, `n<=3` and `n<=4`, respectively.  Since both connectors contribute a
sector, degree eight forces one to have exactly one sector and hence to be
boundary-clean.  An exact two-trace full-component block gives the same
cleanliness directly.  The root-retaining choice correctly imports Theorem
4 of the short-trace classification: setting `k=0` and `W_0={x}` makes the
joined cycle contain the literal vertex `x`.

## 4. Conditional incidence test

For a clean `p`--`q` connector, components of `E-V(P^circ)` and their
contacts with any independent boundary block `B` of order at least two
encode boundary-block carriers exactly.  A carrier projects to a connected
component of the incidence graph containing all of `B`; conversely, the
union of the shore components in such an incidence component becomes
connected after adjoining `B` and contains an edge.  Lemma 3.1 is therefore
an equivalence, including when the carrier itself is disconnected before
`B` is adjoined.

Corollary 3.2 now imports only the Section 1 setup of the audited
concentrated-reserve elimination, together with its independence bound and
the explicit assumption that both roots contact `T`.  In particular it
does **not** import the connector or carrier existence from that result's
Section 2.  Section 1 supplies the full two-component shore structure,
proper-minor six-colourability, the exact partition into independent blocks
`I,T` and roots `p,q`, their prescribed sizes, and the conclusion that
`pq` is a nonedge.

These assumptions recover every remaining hypothesis actually used.  If
there were no `I`--`T` edge, `I` together with one member of `T` would be
an independent set of order `d-4>d-5`.  If either root missed `I`, that
root together with `I` would have the same forbidden order.  Thus there is
an edge between the blocks and both roots contact both blocks.  The
argument is consequently symmetric in `I,T`: if `B` is either block and
`A` is the other, a common incidence component supplies a `B`-carrier `K`
disjoint from the newly assumed connector interior, while `{u}` is an
`A`-carrier.

For the merged response, the three sets

```text
A union {u},   B union K,   V(P)
```

are pairwise disjoint, connected, and nontrivial.  Their contraction images
form a triangle through an edge from `u` to `B`, the edge `up`, and a
root-to-`B` edge.  Pulling their three distinct colours back over
`A,B,{p,q}` gives exactly `I | T | {p,q}` on the closed `F`-shore.  This
works for either choice of `B`; no cardinality equality between `I,T` is
used.

For the split response, the open connector interior, `{u}`, and `K` match
the root connector and two carriers in the audited reflection theorem.  The
imported independence bound and root-contact hypotheses give the required
`I`--`T` edge and both root contacts with each block.  Reflection therefore
gives exactly `I | T | {p} | {q}` on the same shore.  The opposite-response
lemma supplies one of these two types on the retained `E`-shore, so the
matching response glues and six-colours `G`.  Taking the contrapositive for
each choice `B=I,T` proves that both incidence graphs split their named
block in a hypothetical counterexample.

## 5. Seven-connectivity calculation

Let `D` be a component of `G[E-V(P^circ)]`.  If `D` met every vertex of
`I`, its node in `J_I(P)` would put all of `I` in one incidence component;
the same holds for `T`.  Corollary 3.2 therefore makes `D` miss at least one
vertex from each disjoint block and gives `m_D>=2`.

The neighbourhood identity (3.8) is exact.  Outside `D`, its only possible
neighbours are in `S` or `V(P^circ)`: other components of the deletion are
anticomplete to `D`, the exterior components `E,F` are anticomplete, and
`u` has no neighbour in `E`.  These two possible neighbour sets are
disjoint, so

```text
|N(D)| = |S|-m_D+h_D = d-m_D+h_D.
```

The set `N(D)` separates the nonempty set `D` from `u`, which lies outside
both `D` and its neighbourhood.  Seven-connectivity gives `|N(D)|>=7`.
Rearranging yields exactly `h_D>=m_D-1` for `d=8` and
`h_D>=m_D-2` for `d=9`.  These are lower bounds only; they do not bound the
connector length or furnish a bounded separator.

## Unresolved scope

No proof gap was found at the audited hash.  The gain is a genuine but
nonterminal normalization: in degree eight one connector in a parallel
pair is clean, and the two fixed extensions yield one literal odd cycle
with pairwise anticomplete open-shore sectors.  Under the separate response
alignment, both independent boundary blocks must split across the
post-connector component-incidence graphs, with the exact contact lower
bounds recorded in Corollary 3.3.

The theorem does **not** prove that this clean connector has endpoints
`p,q` for which the rest of the boundary admits the independent blocks and
root contacts required by Corollary 3.2.  The incidence test and connectivity
inequalities are expressly conditional on that additional alignment.  The
contact number on the deleted connector is unbounded.  The theorem also
does not synchronize the separately chosen opposite-shore extensions for
two cube coordinates, construct a `K_7`-minor model, produce a common
complete boundary partition, or give a strict same-host
anti-neighbourhood-component descent.

No gap was found in the corrected revision at the hash recorded above.
