# A surviving two-cut has a singleton full component

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_singleton_reduction_audit.md`](hc7_order8_two_cut_singleton_reduction_audit.md).
This is an unbounded reduction inside the exact three-component order-eight
interface.  It does not prove `HC_7`, and the order-seven separation
returned below is not asserted to carry compatible boundary colourings.

## Theorem

Assume the hypotheses and notation of the audited
[response-orientation theorem](hc7_order8_two_cut_response_orientation.md).
Thus `S` has order eight, `G-S` has the three components `C,Q_0,Q_1`, each
adjacent to every vertex of `S`, and

\[
 C=A_d\mathbin{\dot\cup}A_e,
 \qquad S-\{d,e\}=P\mathbin{\dot\cup}R.              \tag{1}
\]

The connected sets `A_d,A_e` are adjacent and miss exactly `d,e`,
respectively.  The classes `P,R` are nonempty independent sets with an
edge between them, `d,e` are nonadjacent, and the closed `C`-side realizes
the boundary partition

\[
                    P\mid R\mid\{d\}\mid\{e\}.       \tag{2}
\]

Then at least one of the following holds.

1. `G` is six-colourable.
2. `G` has an actual separation of order seven.
3. Exactly one of `Q_0,Q_1` is a singleton.

Consequently, every unresolved two-cut residue with neither terminal
outcome 1 nor 2 belongs to the previously isolated singleton-component
order-eight interface.

## Proof

For `i in {0,1}`, call `Q_i` **root-splittable** if it contains distinct
vertices `q_d,q_e` adjacent to `d,e`, respectively.  Since `Q_i` is
connected, a shortest `q_d`--`q_e` path is nontrivial.  Splitting that path
at any edge gives adjacent nonempty connected sets retaining the two root
contacts.

Suppose first that both `Q_0,Q_1` are root-splittable.  Fix
`i in {0,1}` and put `j=1-i`.  Regard `Q_i` as one open shore and
`C union Q_j` as the other.  Inside the latter shore take

* a nontrivial `d`--`e` portal path in `Q_j`;
* `A_d` as the connected subgraph meeting every vertex of `P`; and
* `A_e` as the connected subgraph meeting every vertex of `R`.

These three subgraphs are pairwise disjoint.  The reserved-path and
boundary-block contraction theorem applies.  Splitting the root path at an
edge gives a proper six-colouring of the closed `Q_i`-side inducing (2).
Do this for both values of `i`.  Align those two colourings with the
prescribed colouring (2) of the closed `C`-side.  The components of `G-S`
are pairwise anticomplete, so the three colourings glue to a proper
six-colouring of `G`.  This is outcome 1.

We may therefore assume that some `Q_i` is not root-splittable.  Both
portal sets

\[
 N_G(d)\cap Q_i,\qquad N_G(e)\cap Q_i                \tag{3}
\]

are nonempty because `Q_i` is boundary-full.  If their union contained
two distinct vertices, choosing one vertex from each set (interchanging a
choice when the two sets overlap) would give distinct representatives.
Thus failure of root-splittability says that both sets in (3) are the same
singleton, say `{q}`.

If `Q_i-{q}` is nonempty, let `W` be a component of that graph.  No vertex
of `W` is adjacent to `d` or `e`, and every neighbour of `W` in `Q_i-W`
is `q`.  Hence

\[
                    N_G(W)\subseteq
                    (S-\{d,e\})\cup\{q\}.            \tag{4}
\]

The right side has order seven.  The set `W` is nonempty, while `d,e` and
the other two components of `G-S` lie outside `W` and its neighbourhood.
Thus (4) gives an actual separation of order at most seven.  Seven-
connectivity makes its order exactly seven, giving outcome 2.  If outcome
2 is absent, `Q_i={q}` is a singleton.

Finally, both `Q_0,Q_1` cannot be singletons.  Give the four independent
blocks in (2) four distinct colours.  Give the two singleton components a
fifth common colour; they are nonadjacent and each has all its neighbours
in `S`.  Align this boundary colouring with the prescribed closed-`C`
colouring from (2).  This six-colours `G`, giving outcome 1.  Therefore,
when outcomes 1 and 2 are absent, exactly one full component is a
singleton. \(\square\)

## Exact gain and trust boundary

The theorem eliminates, without any size bound, every two-cut residue in
which both components opposite `C` have two distinct literal portals for
the defect pair.  The only nonterminal residue has one singleton full
component and one non-singleton full component.

The theorem does not colour the remaining non-singleton component with the
partition (2), allocate a boundary-class connector disjoint from the
forced `d`--`e` path in `C`, or make an order-seven separation
colour-compatible.  It does not identify colours with branch-set labels.

## Dependencies

- the audited response-orientation theorem;
- the audited reserved-path and boundary-block contraction theorem; and
- seven-connectivity.
