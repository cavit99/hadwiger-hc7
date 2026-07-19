# Completion of the exact two-cut order-eight residue

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_completion_audit.md`](hc7_order8_two_cut_completion_audit.md).
This is an unbounded completion theorem inside the exact three-component
order-eight interface.  It does not by itself prove `HC_7`.

## Theorem

Assume the hypotheses and notation of the audited
[response-orientation theorem](hc7_order8_two_cut_response_orientation.md).
Thus `S` has order eight, `G-S` has the three boundary-full components
`C,Q_0,Q_1`, and

\[
 C=A_d\mathbin{\dot\cup}A_e,
 \qquad S-\{d,e\}=P\mathbin{\dot\cup}R.               \tag{1}
\]

The connected sets `A_d,A_e` are disjoint and adjacent, and their exact
missed boundary vertices are `d,e`, respectively.  The sets `P,R` are
nonempty independent sets with an edge between them; `d,e` are
nonadjacent; and each of `d,e` has a neighbour in both `P` and `R`.
Finally, the closed `C`-side has a proper six-colouring inducing

\[
                    P\mid R\mid\{d\}\mid\{e\}.       \tag{2}
\]

Then `G` is six-colourable.  Consequently, the two-lobe two-cut residue of
the minimum-positive-excess order-eight interface cannot occur in a
hypothetical minor-minimal counterexample to `HC_7`.

## Proof

Fix `i in {0,1}` and put `j=1-i`.  We prove that the individual closed
component-side `G[Q_i union S]` has a proper six-colouring inducing (2).
Regard `Q_i` as one open shore and `C union Q_j` as the other; the two are
anticomplete.

Write

\[
 D_d=N_G(d)\cap V(Q_j),\qquad
 D_e=N_G(e)\cap V(Q_j).                              \tag{3}
\]

Both sets are nonempty because `Q_j` is boundary-full.  There are two
exhaustive cases.

### Case 1: the two portal sets have distinct representatives

Choose distinct `q_d in D_d` and `q_e in D_e`.  Since `Q_j` is connected,
it contains a nontrivial `q_d`--`q_e` path `D`.  The three connected
subgraphs

\[
                         D,\qquad A_d,qquad A_e       \tag{4}
\]

are pairwise vertex-disjoint.  The path has contacts with both roots,
`A_d` meets every vertex of `P`, and `A_e` meets every vertex of `R`.
Split `D` at an arbitrary path edge into adjacent nonempty connected
subgraphs retaining the `d`- and `e`-contacts.  The audited reserved-path
and boundary-block contraction theorem now gives a proper six-colouring of
`G[Q_i union S]` inducing (2).

### Case 2: the two portal sets have no distinct representatives

For two nonempty sets, failure of distinct representatives is equivalent
to

\[
                            D_d=D_e=\{q\}              \tag{5}
\]

for one vertex `q in Q_j`.  In a proper minor of `G`, simultaneously
contract spanning trees of the following three pairwise disjoint connected
sets:

\[
                   \{q,d\},\qquad A_d\cup P,
                   \qquad A_e\cup R.                 \tag{6}
\]

Leave `e` uncontracted.  Every set in (6) contains an edge: `qd` is an
edge, and each lobe has a neighbour at every vertex of its displayed
nonempty boundary class.

The three contraction images together with the vertex `e` form a `K_4`.
Indeed:

* the image of `{q,d}` is adjacent to `e` through the edge `qe`;
* it is adjacent to both block images through the neighbours of `d` in
  `P` and `R` (or through the boundary-full contacts of `q` when present);
* `e` is adjacent to both block images through its neighbours in `P` and
  `R`; and
* the two block images are adjacent through an edge between `P` and `R`.

The minor is proper and hence has a proper six-colouring.  Restrict this
colouring to the untouched vertices `Q_i union S`.  Pull the colour of the
first contraction image back to `d`, and pull the two block-image colours
back to all vertices of `P` and `R`, respectively.  The four displayed
images had distinct colours, the four boundary blocks in (2) are
independent, and every edge from `Q_i` to a contracted boundary block was
represented by an edge to its contraction image.  The expanded colouring
is therefore proper and induces exactly (2).

The two cases prove the claim for each `i`.  Choose the resulting
colourings of `G[Q_0 union S]` and `G[Q_1 union S]`, and choose the
prescribed colouring (2) of the closed `C`-side.  Permute colour names so
that all three colourings agree on the four labelled blocks in (2).  The
three components of `G-S` are pairwise anticomplete, so the aligned
colourings glue to a proper six-colouring of `G`. \(\square\)

## Exact gain and trust boundary

The proof uses literal portal vertices.  It does not identify a palette
colour with a branch-set label.  It covers arbitrary orders and internal
structures of `C,Q_0,Q_1`, and it treats all bipartition sizes uniformly.

The theorem is conditional on the audited response-orientation normal form.
It does not prove that every order-eight interface has a two-cut, make an
unrelated order-seven separation colour-compatible, or close the remaining
three-connected and singleton-selected order-eight residues.

## Dependencies

- the audited response-orientation theorem;
- the audited reserved-path and boundary-block contraction theorem; and
- six-colourability of every proper minor of `G`.
