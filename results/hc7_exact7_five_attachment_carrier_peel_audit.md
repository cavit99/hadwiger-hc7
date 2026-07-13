# Independent audit: five-attachment carrier peels

Audited file: `results/hc7_exact7_five_attachment_carrier_peel.md`.

## Audit addendum: corrected Theorem 3.3

**GREEN after a precise hypothesis repair now made in the result.**  The
statement explicitly requires

* `P=N(L) cap K` to have order at least five;
* `L` to be a nonempty connected subgraph of the present open shore; and
* `w` to have a neighbour in `L`, so `W={w} union L` is connected.

Connectedness of `L` alone did not imply the last condition and did not
formally place `L` in the shore.  These are local application hypotheses,
not new structural conclusions.

Assume first that Corollary 3.2 has forced
`E(K-{r},A union B)=empty`.  The traces of `A,B` and the singleton `r`
partition all five vertices of `U`.  Thus deleting
`A union B union {r,w,t}` deletes every boundary neighbour of the present
open shore.  Since `L` lies in that shore, the component `X_0` containing
`L` stays inside it: it cannot reach the opposite shore, the opposite
terminal, or `v`.  At least four members of the five-element attachment
set lie in `K-{r}` and are adjacent to `L`, so `X_0` is nonempty and
contains a non-root vertex of `K`.

If `X_0` missed both `A` and `B`, its whole-graph neighbourhood would be
contained in `{r,w,t}`.  Since `v` lies outside `X_0` and outside those
three vertices, this is a genuine cut of order at most three, contradicting
seven-connectivity.  Hence an `A_0-L` path with internal vertices in `X_0`
exists.

Choose such a path shortest and with its first `L` vertex as its final
vertex.  If it avoids `K`, adjoining all path vertices except the final
`L` vertex to `A_0` preserves connectivity and disjointness from the other
two core blocks and from `L`; all added vertices lie in the open shore, so
the literal trace
of `A_0` is unchanged.  The last edge makes the enlarged block adjacent to
`L`, while `L` was already adjacent to `K`.  Because `w-L` is now an
explicit hypothesis, this is a genuine connected-carrier raw-rank-two
promotion for `W`.

If the path meets `K`, let `q` be its first such vertex.  The deleted root
`r` cannot be `q`.  The prefix excluding `q` is disjoint from all three
core blocks and from `L`; adjoining it to `A_0` preserves connectivity and
trace and creates a literal `A_0-q` edge.  The carrier `K` itself is
unchanged and remains two-connected, while `P` is unchanged.  Theorem 3.1
therefore supplies the labelled peel.  Its three post-peel block
adjacencies and trace preservation are already checked below.

The repaired theorem consequently closes exactly the connected,
`w`-attached, two-connected singleton-trace five-attachment region.  It
does not apply when the five attachments are split among disconnected
regions or when the relevant region has no `w` edge.

## Verdict

**GREEN.**  The line-item verdicts are:

* labelled peel operation (1.4): **GREEN**;
* Lemma 2.1, marked bipolar split: **GREEN**;
* Theorem 3.1, singleton-trace peel: **GREEN**;
* Theorem 3.3, seven-connected singleton-lock promotion: **GREEN after the
  explicit local hypothesis repair above**;
* Theorem 4.1, three-connected pair-trace peel: **GREEN**;
* Corollaries 3.2 and 4.2: **GREEN**.

Theorem 4.1 uses the genuine standard nonseparating-path theorem of Tutte,
not a stronger invented linkage statement.  Its quotient and trace lift are
valid, including the possible two-vertex quotient.  The result is local: it
does not eliminate two-connected pair-trace carriers or the recursive
low-connectivity alternative in Section 5.

## 1. The labelled peel operation

Given a partition `V(K)=X dotcup Y` satisfying the definition, `A union X`
is connected through the specified `X-A` edge, and `Y` is connected.  Since
`K` is connected and both parts are nonempty, there is an `X-Y` edge, so
the two new blocks remain adjacent.  The old `A-B` edge preserves the first
new block's adjacency to `B`.  The whole literal trace of `K` stays in `Y`,
and its stipulated trace edge to the trace of `B` preserves `Y-B`.

Because `X` contains no adhesion vertex, the surgery moves no literal trace.
Both parts meet `P=N(L) cap K`, so `L` contacts both new named blocks.  This
is exactly raw-contact-rank promotion.  The draft correctly keeps
admissibility from `w` as a separate boundary condition.

## 2. Lemma 2.1

Adding `st` preserves two-connectivity and permits an `st`-numbering.  Every
proper initial segment is connected by earlier-neighbour induction, and
every proper terminal segment is connected by later-neighbour induction.
The added edge cannot be used in either induction: the endpoint `t` is
absent from a proper initial segment and `s` is absent from a proper
terminal segment.

The first and last marked positions are distinct because `P_0` is a set of
at least two vertices.  Cutting the ordering anywhere between them places a
marked vertex in each connected side and puts `s,t` on their prescribed
sides.  No hidden adjacency between the two marked vertices is assumed.

## 3. Theorem 3.1

Apply Lemma 2.1 with `s=q,t=r,P_0=P`.  Exact singleton trace means every
vertex other than `r`, in particular `q`, is an open-shore vertex.  The
resulting `Y` retains the only trace vertex, while `q in X` supplies the
edge to `A`; both sides meet `P`.  This is precisely a labelled peel.

The contrapositive in Corollary 3.2 is exact: any edge from a non-root
vertex to either other block would furnish the corresponding `q` and hence
a peel.

## 4. The nonseparating path used in Theorem 4.1

The cited form is valid:

> For distinct vertices `x,y,q` in a three-connected graph `K`, the graph
> `K-q` contains an `x-y` path `Q` such that `K-V(Q)` is connected.

This is the standard nonseparating-path theorem of W. T. Tutte, commonly
cited from *How to draw a graph*, Proc. London Math. Soc. (3) 13 (1963),
743--767.  It gives exactly the two properties used here: `q` is avoided
and deletion of the entire path leaves a connected graph.  Inducedness or
planarity is not required.

## 5. The contraction quotient is two-connected

Contract `Q` to `z`.  The quotient is connected.  Deleting `z` leaves
exactly `K-V(Q)`, which is connected.  If `c ne z`, then `c` represents an
original vertex outside `Q`; the graph `K-c` is connected (indeed
two-connected) because `K` is three-connected, and contracting the still
connected path `Q` preserves connectivity.  Hence deletion of every
quotient vertex leaves a connected graph.

The quotient has at least two vertices because the avoided vertex `q`
survives outside `z`.  If it has at least three vertices, this is the usual
two-connectedness criterion.  If it has exactly two, the draft's special
case is legitimate: its vertices are `q,z`, and the marked split is simply
`{q}|{z}`.

## 6. Marked images and the lift

The image `bar P` has order at least two.  One image is `q`.  Any second
member of the original set `P` maps either to `z` or to a quotient vertex
different from `q`; it cannot be identified with `q` because only `Q` was
contracted and `q` avoids `Q`.

Lemma 2.1 therefore gives connected quotient parts with `q` in `bar X`,
`z` in `bar Y`, and a marked image in each.  Expanding `z` back to the
connected path `Q` preserves connectivity of `Y`: every quotient edge
incident with `z` lifts to an edge incident with some vertex of `Q`, and
`Q` joins all such attachments.  The set `X` is unchanged.

Both literal trace roots `x,y` lie on `Q`, so they lie in `Y`; exact
pair-trace means no adhesion vertex can have moved to `X`.  A marked image
in `X` represents an original member of `P` outside `Q`; a marked image in
`Y` either represents such a member or is `z`, in which case
`P cap V(Q)` is nonempty.  Thus both lifted parts genuinely meet the
original `P`.  Finally `q in X` retains its literal edge to `A`.

All connectivity, portal, and exact-trace conditions of a labelled peel
are therefore satisfied.

## 7. Generalized path clause and Corollary 4.2

The more general clause is also correct.  If a non-root cross-block portal
`q` need not itself lie in `P`, but a nonseparating `x-y` path avoids `q`
and does not contain all of `P`, then contraction still gives at least two
marked images: either two members of `P` remain outside the path, or the
image `z` of the nonempty intersection with the path is accompanied by a
member outside it.  Lemma 2.1 may still use `s=q,t=z`; it never required
`s` to be marked.

Consequently, absence of a peel forces every such path to contain all of
`P`, and any `q in P-{x,y}` adjacent to `A` or `B` is immediately excluded
by Theorem 4.1.  This proves both assertions of Corollary 4.2 without
converting a colour label into a branch-set label.

## Trust boundary

The theorem requires literal three-connectivity of the carrier `K`, not
merely three-connectivity of the ambient graph or terminal shore.  It also
requires exact trace `{x,y}`, a non-root attachment `q in P`, and the
literal `q-A` (or `q-B`) edge.  It makes no assertion when all cross-block
edges are gated at the trace, when the carrier has a 1/2-cut, or when every
allowable nonseparating trace path captures all marked attachments.
