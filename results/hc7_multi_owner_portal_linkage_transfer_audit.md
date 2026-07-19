# Independent audit: labelled portal-linkage branch-set transfer

**Verdict:** **GREEN** for the exact source revision below.

This is a separate internal mathematical audit, not external peer review.
It checks the spanning branch-set reassignment, every retained adjacency,
the relaxed first-hit rank, the Rado criterion with overlapping portal
sets, the minimal Menger certificate, the two-owner host-exposure fork, and
the bounded host outcome for a general minimal owner circuit.

## Audited revision

The audited source is
`results/hc7_multi_owner_portal_linkage_transfer.md`.

**Source SHA-256:**

```text
4cd27295dc89c172d4246c67a529b87318d9e4343e5185dc5233f37d04f7109b
```

## 1. Partitioning the transferred piece

The owner and retained-side portal sets are nonempty for exactly the reasons
given in the source.  Trivial paths are consistently allowed when the two
sets intersect.  Once the disjoint paths are fixed, every component of the
remaining vertices of `W` has an edge to their union because `G[W]` is
connected.  Assigning it to one incident path gives pairwise disjoint
connected sets `L_i` which cover all of `W`.

Each enlarged owner `R_i union L_i` is connected through the `A_i` end of
its path.  Its `B` end gives an edge to `U'=U-W`.  Hence the new sets are
nonempty, connected, pairwise disjoint and spanning together with the
unchanged branch sets.

## 2. Model adjacencies and literal data

For an owner, the new path repairs the adjacency which would otherwise be
lost when `U` is reduced.  For a nonowner, an old edge from `U'` survives by
the definition of the owner set.  The fixed edge `c_1u_1` preserves the
`D-U'` adjacency.  Enlarging an owner preserves all of its old adjacencies,
and no other pair changes.  Thus `X-Y` is the only pair which can remain
nonadjacent; if it is repaired, the result is explicitly a `K_7` model.

The root of `U` lies in `U'`, every owner root remains in its old owner, and
the fixed partition and response subgraph are unchanged literal objects of
the same host.  The transfer therefore belongs to the exact compatibility
class claimed in the theorem.

## 3. Relaxed first-hit rank

Every old response path whose terminal label is not `U` avoided all of old
`U`, including every transferred `L_i`.  It remains a valid first-hit path
even when its ranked owner is enlarged.  A path ending in `U'` also remains
valid.  If the old `U`-path ended in `W`, connectedness of `Z` and the fixed
edge `c_1u_1` replace it by a path from the same designated port through
`Z` and then directly to `u_1`.

The replacement has only `u_1` outside `Z`.  Other paths avoided old `U`,
so outside-`Z` disjointness is preserved; overlap inside `Z` is expressly
permitted.  Thus the relaxed rank cannot fall.  Maximizing it and then
minimizing `|U|` is a well-founded extremal choice in the fixed finite host.

## 4. Rado and Menger certificate

The sets `A_i` need not be disjoint, but Rado's independent-transversal
theorem does not require disjoint presentation sets.  The strict gammoid on
literal vertices of `W` enforces distinct representatives and pairwise
vertex-disjoint paths to distinct vertices of `B`.  Its rank on `A_I` is
exactly the path-packing number in the source, so the displayed inequalities
are necessary and sufficient.

Choose a deficient set `I` inclusion-minimal.  A singleton is not deficient
because `G[W]` is connected and its two endpoint sets are nonempty.  For
each `i in I`, nondeficiency of `I-{i}` gives rank at least `|I|-1`;
monotonicity and deficiency make the rank on `A_I` exactly `|I|-1`.
Every proper subfamily satisfies all of its Rado inequalities and therefore
has a full labelled portal linkage.  Vertex Menger with endpoints permitted
in the separator gives the stated transversal of order `|I|-1`; this also
handles zero-edge paths when a portal lies in `A_I cap B`.  Since there are
at most five possible owners, its order is at most four.

## 5. Two-owner host fork

Let `s` be the one-vertex transversal from Corollary 3.2.  If both owner
portal sets are contained in `{s}`, their nonemptiness makes both equal to
`{s}`, giving the concentrated two-label incident pair in outcome 1.

Otherwise a component `C` of `G[W-s]` contains an owner portal other than
`s`.  It cannot contain a vertex of `B`: connectedness inside `C` would
then give a `B`--owner-portal path avoiding the transversal.  Since
`B=N_G(U') cap W`, this also makes `C` anticomplete to `U'`.  Connectedness
of `G[W]` and the fact that `C` is a component after deleting `s` give

```text
N_{G[W]}(C)={s}.
```

The full host neighbourhood is a genuine separator, not merely an internal
one.  The set `C` is nonempty, `U'` is nonempty, no vertex of `U'` belongs
to `N_G(C)`, and deleting `N_G(C)` leaves `C` and `U'` on distinct nonempty
sides.  Seven-connectivity therefore gives `|N_G(C)|>=7`.

Every neighbour other than `s` belongs to one of the six branch sets other
than `U`.  If each contributes at most one vertex, there are at most seven
boundary vertices in total; equality with the connectivity lower bound
then forces exactly `s` and one literal vertex from every other branch set.
This verifies the label-transversal order-seven outcome.

Otherwise one outside branch set contains two distinct boundary vertices
`x,y`.  Choosing incident edges from `C` to `x,y` gives two distinct cross
edges, even if their ends in `C` coincide.  Deleting either cross edge does
not alter the internal connectivity of a branch set, while the companion
edge retains the same `U`--outside-branch-set adjacency.  Thus outcome 2b
has exactly the claimed edge-by-edge model persistence.

## 6. Critical-host interpretation

Corollary 4.2 explicitly assumes both that `G` is not six-colourable and
that every edge-deleted proper subgraph is six-colourable.  Hence every
displayed edge is deletion-critical.  Indeed `G-e` is six-colourable by
hypothesis, and it cannot be five-colourable: giving one end of `e` a fresh
sixth colour would then six-colour `G`.

Only outcome 2b has the companion-edge argument needed to preserve the
same labelled near-complete model after either deletion.  The source does
not assert this for the differently labelled incident edges in outcome 1.
In outcome 2a an edge from `s` to `C` crosses the actual order-seven
boundary and its deletion supplies a proper-subgraph colouring response;
the source correctly does not claim that this response already extends
through the intact `C`-side.  No contraction-critical conclusion is used
or asserted in Section 4.

## 7. General minimal-owner-circuit fork

Let `I` be inclusion-minimal deficient and let `K` be its Menger
transversal.  If `A_I` is contained in `K`, choose one portal occurrence
from every nonempty `A_i`.  There are `|I|` occurrences but only
`|K|=|I|-1` possible vertices, so two differently labelled owners share
one portal vertex.  The portal definition supplies one edge from that
vertex to each of the two distinct owner branch sets, proving the incident
differently labelled contact pair in outcome 1.

If `A_I` is not contained in `K`, a component `C` of
`G[W-K]` contains a portal in `A_I-K`.  It cannot also contain a vertex of
`B`: a path inside the connected component between those two vertices
would be a `B`--`A_I` path disjoint from `K`, including the zero-length
case if the two endpoint sets overlap.  Since `B=N_G(U') cap W`, this
proves that `C` is anticomplete to `U'`.

As `C` is a component after deleting `K`, all of its neighbours within
`W` lie in `K`.  There are no neighbours in `U'`, so

```text
N_G(C) cap U subseteq K.
```

The set `N_G(C)` is an actual host separator: `C` and the nonempty retained
donor `U'` survive its deletion on distinct nonempty sides.  Thus
seven-connectivity supplies the lower bound seven.

All remaining neighbours lie in the six branch sets other than `U`.  If
each such set contributes at most one literal vertex, then

```text
|N_G(C)| <= |K|+6 = (|I|-1)+6 = |I|+5 <= 10.
```

This verifies the complete separator count and the stated distribution of
its vertices.  If the one-per-branch-set condition fails, two distinct
outside vertices in one branch set give two distinct cross edges from
`C`.  Deleting either cross edge leaves the branch sets internally
connected and the other edge retains exactly the same model adjacency.
Hence the repeated-contact alternative is model-preserving as claimed.

## 8. Trust boundary

The Menger set lies inside the old branch set.  It is not a host separator:
components behind it may have arbitrarily many neighbours in other branch
sets.  The result neither bounds that exposure nor transports a legal
boundary colouring.  It proves a strict model-and-rank descent when the
full labelled portal linkage exists and isolates a minimal internal
bottleneck otherwise; it does not prove `HC_7`.

No mathematical error was found.
