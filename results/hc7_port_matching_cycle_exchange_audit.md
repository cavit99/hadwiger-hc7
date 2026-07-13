# Independent audit: port-matching cycle exchange

## Verdict

**GREEN after a proof-local repair.**  The stated dichotomy, the
three-row `K_7` lift, and the four-block labelled corollary are correct.
The present proof's instruction to contract **all** matching edges and
then invoke the earlier two-shore theorem is unnecessarily unsafe as
written: in the simple quotient the two cycle images can have a common
edge, whereas that theorem assumes edge-disjoint shores.  It also refers
to “the four minor branch sets” although the cited theorem first returns
a subdivision.

Neither issue changes the result.  Apply the crossing-chord lemma directly
to the two cyclic orders and use only the four matching edges selected by
the crossing.  The construction below gives four literal rooted branch
sets and is unaffected by arbitrarily many extra matching endpoints.

Audited source: `results/hc7_port_matching_cycle_exchange.md`.

## 1. The formal defect in the all-edge contraction proof

After every `ell_i r_i` is contracted to `s_i`, the images of `C_L` and
`C_R` are cycles through the common set `S`.  If `i,j` are consecutive in
both port orders, however, an `s_i-s_j` cycle edge can occur in both cycle
images after simplification.  Thus the quoted hypothesis

\[
                      E(H_1)\cap E(H_2)=\varnothing
\]

of the earlier rural cycle-order theorem is not literally established.
One can retain two coloured parallel copies in a multigraph, but that
convention is not stated.

There is a second expository gap.  The earlier theorem returns a rooted
`K_4` subdivision.  Before lifting contractions, one must either convert
that subdivision into four disjoint minor branch sets or directly lift
its six internally disjoint paths.  The desired lift is valid, but the
current sentence skips this construction.

## 2. Direct repaired proof of the mismatched-order outcome

Suppress on each of `C_L,C_R` every maximal subpath whose internal
vertices are not matching endpoints.  This records two abstract cycles
on the index set `I`.  If their cyclic orders differ up to reversal, the
crossing-chord lemma gives two independent edges

\[
                         ab,\quad cd                       \tag{2.1}
\]

of the suppressed `R`-cycle whose four ends alternate on the suppressed
`L`-cycle.  Say their `L`-order is

\[
                         a,c,b,d.                          \tag{2.2}
\]

Lift `ab,cd` to the two corresponding arcs of `C_R`.  Because they are
edges of the cycle suppressed on **all** port indices, their interiors
contain no `r_i`, and the two arcs are internally disjoint.  In `C_L`,
take the four arcs between consecutive members of (2.2).  Their interiors
are pairwise disjoint; they may contain additional `ell_i`, which causes
no difficulty.

For each `x in {a,b,c,d}`, take the literal matching edge

\[
                         Q_x=\{\ell_x,r_x\}               \tag{2.3}
\]

as the initial rooted branch gadget.  The four `L`-arcs and the two
`R`-arcs are six connections between these four gadgets in the pattern of
all six edges of `K_4`.  The shore vertex sets are disjoint, so an
`L`-arc cannot meet an `R`-arc.  Within either shore the chosen arcs are
internally disjoint, and their only selected port endpoints are their
advertised ends.

Choose one cut edge on each of the six connecting paths and assign the
two remaining path segments to the rooted gadgets at its ends.  Equivalently,
contract each connection down to one edge without contracting a gadget.
The resulting four branch sets are connected, disjoint and pairwise
adjacent, and the branch set rooted at `x` still contains the whole
literal edge `ell_x r_x`.

This proves the mismatch conclusion without contracting any unselected
matching edge.

### Extra-endpoint falsification check

Additional matching endpoints can occur internally on the four selected
`L`-arcs.  Their `R`-endpoints cannot occur internally on either selected
`R`-arc, because (2.1) consists of edges of the cycle on the full index
set.  In any event, the unused matching edges are simply omitted from the
minor subgraph.  Their presence in the host only adds adjacencies and
cannot merge branch sets.  Thus extra matching endpoints do not furnish a
counterexample.

This check also explains why distinct matching endpoints are essential.
If two selected port edges shared an endpoint, the four gadgets (2.3)
would not be disjoint.

## 3. Compatible-order annulus gluing

Assume the cyclic orders agree up to reversal and each disk embedding has
the displayed cycle as its exposed boundary cycle.  Reflect one disk if
needed.  Put one drawing in the disk bounded by the inner circle of an
annulus and put the other, after inversion if desired, in the exterior of
the outer circle.  Match equally labelled boundary points by pairwise
disjoint arcs across the annulus.  Such arcs exist precisely because their
orders agree on the two boundary components after accounting for the
opposite boundary orientations.

The graphs `L,R` are vertex-disjoint and the port edges form a matching,
so no other identifications or shared endpoints have to be accommodated.
The interiors of the two disk drawings and of the annular arcs are
pairwise disjoint.  Hence the claimed plane embedding is valid.

As in the earlier rural theorem, “exactly one” refers to equality versus
inequality of the two cyclic orders.  The compatible planar graph is not
claimed to contain no unrelated rooted `K_4` minor.

## 4. Three-row `K_7` lift

The repaired mismatch proof returns four branch sets `Q_a,Q_b,Q_c,Q_d`,
each containing both endpoints of its selected literal port edge.  The
hypothesis on a port edge says that, for every fixed row `F_j`, at least
one of those two endpoints has a neighbour in `F_j`.  Therefore every
`Q_x` is adjacent to every `F_j`.

The four `Q_x` are connected, disjoint and pairwise adjacent.  The three
`F_j` are connected, mutually disjoint and pairwise adjacent, and are
disjoint from both shores.  Thus

\[
                  Q_a,Q_b,Q_c,Q_d,F_1,F_2,F_3
\]

are seven literal minor branch sets.  Corollary 2 is GREEN.  Merely asking
each `F_j` to meet the matching somewhere would not suffice; the stated
pointwise-per-port-edge condition is what makes the conclusion independent
of which crossing is returned.

## 5. Four contiguous label blocks

Choose one edge from each labelled class and discard every other matching
edge for purposes of applying Theorem 1.  Contiguity implies that the
cyclic order of the four selected endpoints on either cycle is exactly the
induced cyclic order of the four class labels.  If the two label orders
differ up to reversal, the selected four-edge submatching therefore has
mismatched endpoint orders.

Applying the repaired theorem to that submatching gives four branch sets,
one containing each of the four chosen edges.  Since the edges were chosen
from distinct classes, the four branch sets carry four distinct literal
labels.  Extra edges of the same classes and unlabelled matching edges are
unused and harmless.  Corollary 3 is GREEN.

## Required repair to the active source

Replace the mismatched-order paragraph beginning “Contract every edge of
`M`” by the direct construction in Section 2 above, or explicitly work in
an edge-coloured multigraph and then construct the rooted minor branch
sets before lifting.  The direct construction is preferable: it proves
label preservation transparently and resolves the extra-endpoint issue at
the same time.

No strengthening beyond the stated trust boundary is justified.  In
particular, shared port endpoints, boundary paths instead of cycles, or
distributed three-row contacts remain outside the theorem.
