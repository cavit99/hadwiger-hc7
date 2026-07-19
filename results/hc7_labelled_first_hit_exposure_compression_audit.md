# Independent audit of labelled first-hit exposure compression

**Audit status:** separate internal audit.

**Audited source:**
`results/hc7_labelled_first_hit_exposure_compression.md`

**Audited source SHA-256:**
`9e70ca705870eaf4bba5694dd84825f402f6f97e26d9c5605584685630b53244`

The audited theorem and proof are unchanged; the refreshed hash records the
source status-line update made after the independent GREEN verdict.

## Verdict

**GREEN.**  The matching-cover reduction, the literal order-seven
neighbourhood, the atomic order bound, and the model-preserving critical
edge specialization are correct under the stated unit-capacity first-hit
and spanning labelled-model hypotheses.

The theorem is a structural compression only.  It does not preserve a
selected boundary equality partition, make the forced Kempe components
disjoint, or finish either the repeated-exposure exchange or colour gluing
at the returned separator.

## 1. Imported Rado--Menger data

The source uses the already audited directed-sink construction correctly.
The deficient label set `I` is nonempty, the Menger set has

\[
                         |Z|\le |I|-1,
\]

and at least one source survives because `|P|>=5>|Z|`.  The component `C`
is taken after deleting `T`, `F`, and the nonterminal members of `Z`.
Consequently every host neighbour of `C` belongs to one of exactly three
types:

1. the literal image of a Menger-set member;
2. a vertex of `F`; or
3. a vertex in an unselected terminal class.

This verifies (1.4).  Since `|T_I|>=|I|>|Z|`, a selected terminal sink is
not in `Z`; its literal terminal has no neighbour in `C`.  It lies outside
`C` and outside every containing set for a neighbourhood used later.
Thus the asserted opposite side is genuinely nonempty.

## 2. Placement of the one-vertex cover

Fix an unselected label `j` with `|E_j|>=2` and suppose the matching
outcome fails.  The bipartite exposure graph `B_j` has matching number one,
so Koenig's theorem gives a vertex cover of order one.

That cover cannot be a terminal vertex `t in E_j`.  Every member of `E_j`
belongs to `N_H(C)`, and hence is incident with at least one edge of
`B_j`.  A second member of `E_j-{t}` would have an edge not incident with
`t`, contradicting that `{t}` covers all edges.  Therefore the cover is a
vertex `c_j in C`, and every exposure edge is incident with `c_j`.  In
particular every terminal in `E_j` is adjacent to `c_j`.  This justifies
(2.4), including the word "every" rather than merely the existence of two
contacts.

Repeated labels may choose the same `c_j`; this is correctly handled by
passing from the indexed family to the set

\[
                         X=\{c_j:j\in R\}.
\]

No injectivity of `j mapsto c_j` is assumed.

## 3. The full-neighbourhood separator

Suppose `C-X` is nonempty and let `D` be a component of `H[C-X]`.
The containing set in (2.6) is disjoint from `D`:

* nonterminal members of `bar Z` were deleted before `C` was chosen, and
  terminal members lie outside `C`;
* `F` and every terminal set were deleted from the nonterminal graph;
* `X` was removed in forming `C-X`; and
* distinct components of `C-X` have no edge between them.

There is no omitted neighbour type.  An edge from `D` to a terminal class
with repeated exposure has its `C`-end equal to the corresponding cover
vertex `c_j in X`; hence no such edge can start in `D`.  Exposures of size
one contribute exactly the displayed singleton, and empty exposures
contribute nothing.

The cardinality calculation is also valid without disjointness among the
displayed pieces, since it is an upper bound:

\[
\begin{aligned}
 |\bar Z|+|N_H(C)\cap F|+|X|+|S|
 &\le (|I|-1)+3+|R|+|S|\\
 &\le (|I|-1)+3+(5-|I|)=7.
\end{aligned}
\]

The surviving selected terminal described in Section 1 belongs to none of
these pieces, so it supplies a nonempty opposite open side.  Seven-
connectivity gives `|N_H(D)|>=7`.  Since `N_H(D)` is contained in a set of
order at most seven, both have order seven and are equal.  Thus the source
returns the **full literal neighbourhood** of `D`, not merely an auxiliary
cut, and both open sides are nonempty.

## 4. The atomic alternative

If `C-X` is empty, then `C=X`.  Since `I` is nonempty,

\[
 |C|=|X|\le |R|\le5-|I|\le4.
\]

For every `c in C=X`, at least one repeated label `j` satisfies `c=c_j`.
Choosing such a label gives `|E_j|>=2`, and the cover calculation shows
that `c` is adjacent to every vertex in `E_j`.  Hence it has the required
two literal neighbours in one named terminal class.  The source correctly
does not claim that different vertices of `C` receive different labels.

## 5. Spanning-model specialization

In outcome 2, the two exposure edges have distinct ends on both sides.  In
outcome 3, the two chosen edges share their end in `C` but have distinct
ends in `E_j`.  In either case both join the branch set `D` to the same
different branch set `U_j`.  Deleting either edge leaves the companion
edge, so:

* the old `D-U_j` adjacency remains;
* neither branch set loses an internal edge; and
* all other branch-set adjacencies are unchanged.

The same spanning labelled `K_7`-minus-one-edge model therefore persists
after either deletion.  This conclusion uses the stated containment
`C subseteq D`, `T_j subseteq U_j`; it would not follow from palette labels
alone.

Minor-minimal non-six-colourability gives six-colourings of both proper
minors `G-e` and `G/e`.  Neither can be five-colourable.  From a
five-colouring of `G-e`, recolour one endpoint of `e` with a fresh sixth
colour and restore `e`.  From a five-colouring of `G/e`, expand the
contracted vertex to the two endpoints and again recolour one endpoint
with a fresh sixth colour.  Either construction would six-colour `G`.
Thus

\[
                         \chi(G-e)=\chi(G/e)=6.
\]

Finally, in every six-colouring of `G-e` its ends have the same colour, or
`e` can be restored.  If their two-colour components for that common
colour and another colour were distinct, a Kempe interchange on the
component containing one endpoint would separate the endpoint colours and
again restore `e`.  This verifies all five forced Kempe connections.

## 6. Exact trust boundary

The proof requires:

1. five pairwise disjoint literal terminal classes and five distinct
   unit-capacity sources;
2. at most three fixed literal vertices `F`;
3. seven-connectivity of the host;
4. for Proposition 3.1, a spanning labelled near-complete model with the
   source component and terminal class contained in two different named
   branch sets; and
5. proper-minor six-colourability of the host.

It proves no common boundary colouring at the exact separator.  It also
does not convert an incident edge pair in the atomic outcome into two
vertex-disjoint paths.  Those are the remaining dynamic, label-preserving
obligations.
