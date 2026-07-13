# Relative shore contraction and tight seven-separator witnesses

## 1. Relative expansion

Let `D` and `L` be disjoint vertex sets in a graph, where `D` is
connected and every neighbour of a vertex of `D` lies in `D union L`.
For a nonempty set `X subsetneq D`, put

\[
 \partial_D(X)=N_D(X)-X,
 \qquad A_L(X)=N_L(X),
 \qquad \phi(X)=|\partial_D(X)|+|A_L(X)|.
\]

In each order-six reserved-connector shore derived from a hypothetical
counterexample to `HC_7`, seven-connectivity gives

\[
 \phi(X)\ge 7                                      \tag{1.1}
\]

for every nonempty proper `X subsetneq D`, and the whole shore is full:
`N_L(D)=L`, where `|L|=7`.

The following elementary lemma isolates exactly why an internal edge may
fail to be safely contractible for this relative expansion.

## 2. Tight-witness lemma

### Lemma 2.1

Assume (1.1), and let `xy` be an edge of `G[D]`.  Contract `xy` to a new
vertex `z`, retaining the natural union of their `L`-neighbourhoods, and
call the resulting shore `D'`.

If `D'` fails (1.1), then there is a nonempty proper set

\[
 Y\subseteq D-\{x,y\}
\]

such that

\[
 \phi(Y)=7,
 \qquad x,y\in N_D(Y),                              \tag{2.1}
\]

and the corresponding boundary in the contracted shore has order six.

Conversely, every violation created by the contraction has this form.

### Proof

Let `Y'` be a nonempty proper subset of `D'` with contracted boundary
order at most six.

If `z in Y'`, replace `z` by both `x,y` and call the preimage `X`.  Every
external neighbour of `X` in `D union L` corresponds bijectively to an
external neighbour of `Y'` in `D' union L`; contraction changes only
vertices internal to the set.  Hence the two boundary orders are equal,
contradicting `phi(X)>=7`.

Thus `z notin Y'`, and we identify `Y'=Y subseteq D-{x,y}`.  All boundary
vertices other than `x,y` are unchanged.  If `Y` sees neither or exactly
one of `x,y`, its boundary order is unchanged.  If it sees both, the two
distinct boundary vertices `x,y` become the single boundary vertex `z`,
so the order drops by exactly one.  Since the original order is at least
seven and the new one at most six, equality holds throughout: the
original order is seven, the new order is six, and `Y` sees both ends of
the contracted edge.  This proves (2.1), as well as the converse
description. \(\square\)

### Corollary 2.2 (minimal-shore protection)

Consider a class of relative shores satisfying (1.1) and full attachment
to `L`, with a target minor model that always lifts through an internal
edge contraction.  In a minimum-order member of the class having no target
model, every internal edge `xy` has a tight witness `Y` as in (2.1), unless
some additional side constraint is destroyed by contracting `xy`.

For the pure-Moser reserved-connector shore, the only additional numerical
constraint used in the finite quotient theorem is the terminal degree

\[
 \epsilon+|N_D(a)|\ge3.                             \tag{2.2}
\]

Here `epsilon` records the optional edge from the terminal to the sixth
portal.  Contraction can destroy (2.2) only when equality holds in (2.2)
and both `x,y` are neighbours of `a`.  Consequently every edge in a
minimum no-model shore is of one of two explicit types:

1. it joins two neighbours of a terminal whose degree inequality is
   tight; or
2. it is protected by a relative minimum seven-separator `Y` satisfying
   (2.1).

### Proof

Full attachment is preserved because the contracted vertex inherits the
union of the two attachment rows.  If the contracted shore still satisfies
(1.1) and (2.2), minimality gives the target model there; expanding `z`
back to the connected pair `{x,y}` lifts every branch set and therefore
gives the same target model before contraction.  This is impossible.
Lemma 2.1 supplies the only possible failure of (1.1).  The count in
(2.2) drops precisely when `a` saw both endpoints, and it can cross the
threshold only from equality. \(\square\)

## 3. How a tight witness returns to the global graph

If (1.1) comes from a seven-connected ambient graph and `Y` is a tight
witness, then

\[
 T=(N_D(Y)-Y)\mathbin{\dot\cup}N_L(Y)
\]

is an order-seven vertex cut.  Taking any component `K` of `G[Y]`, its
external neighbourhood is contained in `T`; seven-connectivity forces it
to be all of `T`.  Hence every component of `G[Y]` is itself a connected
full shore for the new adhesion `T`.

This observation converts failure of local contraction into another exact
full-shore separator, where the boundary-state and minor-augmentation
theorems apply.  It is not by itself a contradiction: the induced graph on
`T` can be one of the nonsplit sharp cores.  The remaining closing task is
to uncross these tight witnesses until either a safely contractible edge is
obtained or the resulting laminar family supplies enough disjoint full
shores for a `K_7` model.

