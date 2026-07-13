# Adversarial audit: uniform three-demand exchange

## Verdict

**GREEN AS PATCHED for the fixed-linkage trichotomy, separator lemmas,
and operation-state statements.  AMBER as an exchange theorem or packet-
triangle closure.**

Theorem 2.1 correctly reduces one fixed two-demand linkage to:

1. a disjoint third carrier;
2. capture of an omitted portal class by the two enlarged rails; or
3. a crossless alternating four-terminal graph with a same-vertex web
   completion.

Seven-connectivity gives the stated strict separator load once nested
order-seven cuts are excluded, and proper-minor criticality gives the
stated boundary-state rigidity for operations supported faithfully in
opposite open shores.

What is **not** proved is an exchange between two different certificates
sharing a demand.  The packet pigeonhole leaves three live combinations:
web--web, capture--web, and capture--capture.  The original application
silently retained only the first.  Section 6 and the status statement now
record all three, so the note no longer claims a packet-triangle closure.

This is an internal proof audit, not external peer review or a novelty
determination.

## 1. Fixed-linkage rail enlargement

Start with two disjoint connected carriers.  A shortest path between them
has no internal vertex in either carrier.  Partition its internal
vertices into an initial and a terminal segment and absorb those segments
into the corresponding carriers.  The edge between the segments—or the
first/last path edge if a segment is empty—makes the enlarged carriers
adjacent.  Connectivity, disjointness, and all original portal contacts
are preserved.

The manuscript's former phrase “split the interior at an edge” did not
literally cover a path with zero or one internal vertex.  The proof now
uses an indexed path and includes those cases explicitly.

The subsequent alternatives are exhaustive for these **fixed enlarged
rails**:

* if the two residual portal sets intersect, a common vertex is a
  singleton third carrier;
* if either residual set is empty, this is portal capture;
* otherwise, a residual path between them is a third carrier, and absence
  of such a path gives the crossless outcome.

The theorem is existential in the choice of rail enlargement and does not
say that capture or web type is invariant under rerouting the original
two-linkage.

## 2. Exact generalized Two Paths mapping

After contracting the two disjoint rails and suppressing loops and
parallel edges, add new terminals `alpha,beta` adjacent respectively to
the two nonempty disjoint residual portal sets.  The four terminals

```text
alpha, ell_i, beta, ell_j
```

are pairwise distinct.  In that cyclic order the alternating pairs are
exactly `alpha-beta` and `ell_i-ell_j`.

Any crossing would contain an `alpha-beta` path vertex-disjoint from an
`ell_i-ell_j` path.  The first path avoids both contracted rail vertices;
after deleting its artificial ends and lifting the contraction, it gives
a residual portal-to-portal path outside the rails.  This is precisely
the third carrier already excluded.  The direct rail edge supplies an
`ell_i-ell_j` path but is not needed for the converse.

The invoked external statement is exactly Humeau--Pous, Theorem 1.5:
maximally crossless graphs for a tuple are webs with that frame, and hence
any crossless input embeds by adding edges on the same vertex set into
such a web.  The paper explicitly states the arbitrary-tuple version and
the same-vertex web completion consequence.  See the
[primary arXiv text](https://arxiv.org/abs/2505.16431).

Thus no hidden 3-connectivity, fixed representative, or planar-embedding
hypothesis is being inserted at this step.  The completion may contain
formal edges absent from the host; later arguments correctly use only its
cell-neighbour confinement, not those formal edges as host paths.

## 3. Boundary classes and strict separator load

The seven-connectivity section originally started with arbitrary portal
sets, but then referred to their “corresponding boundary labels.”  It now
states the needed hypothesis explicitly:

```text
A_i=N_C(a_i),  B_i=N_C(b_i),  with a_i,b_i in S.
```

For a nonempty proper set `Y` in the shore `C`, its complete ambient open
neighbourhood is

```text
(N_C(Y)-Y) disjoint-union N_S(Y),
```

because the two components of `G-S` are anticomplete.  It separates `Y`
from the opposite full shore.  Seven-connectivity gives order at least
seven; if equality held, it would be a nested minimum seven-cut.  Under
the no-descent hypothesis its order is therefore at least eight.  Any
order-seven cut is minimum, and the standard six-vertex deletion argument
makes every component behind it full.

If a boundary label had a unique portal `z` and `|C|>=2`, take
`Y=C-{z}`.  It has at most one internal neighbour outside and sees at most
the other six boundary labels, contradicting the order-eight inequality.
Hence each actual boundary class has at least two portals.  The singleton
shore was a genuine exception to the former unqualified lemma; the source
now states `|C|>=2`.  Packet ownership of a two-linkage automatically
places the application outside that exception.

Capture consequently places at least two vertices of the captured
boundary class in the union of the two rails.  It does not place them in
different rails and does not identify either rail with a rail from another
packet.

## 4. Off-rail web cells

The cell statement is valid for the vertices inserted behind one facial
triangle, excluding the support triangle itself.  It is now worded that
way explicitly.

If the supporting triangle avoids both contracted rail vertices, its
ordinary vertices lift to at most three actual vertices of `C`.  An
artificial terminal in the triangle may be conservatively replaced by its
boundary label.  Because the original contracted graph is a subgraph of
the web completion, every actual neighbour of the inserted cell outside
the cell lies either in those lifted triangle positions or in its actual
boundary-contact set `P`.  Therefore

```text
N_G(K) subseteq hat(T) union P,  |hat(T)|<=3.
```

The opposite shore lies beyond this neighbourhood.  If `|P|<=3`, a cut
of order at most six results.  If `|P|=4`, the cut has order at most seven;
order below seven contradicts connectivity, while order seven is a nested
minimum cut and its components are full.  Thus, in the seven-connected
no-descent row, every off-rail cell has at least five boundary contacts.

The restriction that the support triangle avoid the rail vertices is
essential.  A rail vertex lifts to an unbounded connected carrier, not to
one separator vertex.  The source explicitly retains rail-incident cells
as the unresolved geometry.

## 5. Operation-state rigidity

For an interface edge `e` of a connected covering split, every
six-colouring of `G-e` induces a state on `S` which is realizable both by
the operated shore and by the unchanged opposite shore.  If that same
state extended across the unoperated original shore, a palette permutation
would align the boundary blocks and six-colour `G`.  This proves the two
memberships and the strict nonmembership in (4.2).

The endpoint common-colour assertion and the detour-or-two-boundary-
anchors dichotomy are exactly the already proved interface-edge theorem:
switching an unanchored bichromatic endpoint component would separate the
endpoint colours and restore `e`.

For opposite-operation splicing, “faithful” must be literal.  The source
now defines it to mean a nontrivial proper-minor operation supported
wholly in one open shore, disjoint from the boundary, leaving the opposite
closed shore unchanged.  If opposite faithful operations had a common
boundary equality state, retain from each colouring the shore on which
the other operation occurred, align the boundary palettes, and splice a
six-colouring of `G`.

No claim is made for boundary contractions, boundary deletions, or an
operation which alters both shores.  Nor does abstract novelty of states
force two independently generated state sets to intersect.

## 6. Counterexample suite

The command

```text
.venv/bin/python three_demand_exchange_counterexamples.py
```

passes all assertions.

The carrier search is exhaustive for the linkage questions: every
connected carrier contains a simple path between one left and one right
portal, so shrinking disjoint carriers to simple paths cannot destroy a
linkage.

The three examples establish distinct sharp limitations.

1. The 14-vertex two-hub graph has six portal classes of order two and
   every pair of demands linkable, but every carrier uses one of the two
   hubs, so no triple exists.  Its minimum separator is exactly the two
   hubs.  Portal multiplicity alone is insufficient.
2. The triangular prism is 3-connected and pairwise linkable but not
   triple-linkable.  The displayed packets using demand `13` consume a
   singleton portal of the omitted demand and therefore genuinely return
   capture.  The middle packet is a clean crossless row.  Thus
   3-connectivity does not remove capture.
3. The eight-vertex graph in Example 5.3 is 3-connected, all three
   displayed packet linkages avoid the omitted terminals, their rails are
   already adjacent, and the two omitted terminals are disconnected after
   rail deletion.  Exhaustive search finds no triple.  Thus even clean
   pairwise packets in a 3-connected shore do not remove the web outcome.

The script now asserts the stated capture and clean-web properties, not
only pairwise linkability and absence of a triple.

## 7. Packet-triangle pigeonhole

For a fully positive packet triangle, each of its three packet edges has
at least one shore owner.  Choose one owner for each edge.  Two colours on
the three edges force one shore to own two edges, and two edges of a
triangle share one demand.  This pigeonhole inference is exact.

Full positivity forbids a simultaneous triple in either shore.  Applying
Theorem 2.1 to the two owned packets therefore produces two certificates,
but each certificate can independently be capture or web.  The complete
residue is:

* web--web: a common-rail exchange is missing;
* capture--web: a captured-rail transfer is missing; and
* capture--capture: a double-capture exchange is missing.

Lemma 3.1 only says that a captured class contains at least two portal
vertices.  It does not put them on opposite rails, identify the shared-
demand carriers, convert capture into web, or create a triple linkage.
Consequently none of these three comparison problems has been solved.

## 8. Exact frontier consequence

The proved advance is a useful, label-free **one-packet normal form**:

```text
fixed pair linkage + no triple
    => captured omitted portal class
       or alternating same-vertex web.
```

With seven-connectivity and minor-criticality, capture has multiplicity,
off-rail web cells are high-contact or descend, and faithful opposite
operations carry disjoint states.  This is genuine uniform machinery and
rules out an unclassified third geometry for one fixed packet.

It does not close a fully positive packet triangle, the seven-edge layer,
or `HC_7`.  The exact next theorem must solve at least the three certificate
comparison problems above.  Calling the current result a complete
“three-demand exchange” without that qualification would be misleading;
as a static trichotomy it is GREEN, while its intended dynamic exchange
programme remains AMBER.
