# A double-forced rural state localizes to one facial edge

## Status

This note continues the two-heavy harmonica dichotomy.  In a
four-connected fully rural carrier, the harmonica outcome is impossible,
so an uncolourable exactly-two-heavy total-contraction state has two
vertices with the singleton list consisting of the contraction colour.
When those two vertices are adjacent on the active face, the state is
already realized by contracting that one literal facial edge.  Thus the
proper-minor state jump need not contract the rest of the carrier.

This is a strict localization, not yet a contradiction: a matching
equality partition from an operation in the opposite open shore is still
needed for the crossed splice.

## Setting

Let `K` be a four-connected plane graph with outer facial cycle `F`, and
let `S` be an actual external adhesion such that every vertex of `K`
having a neighbour in `S` lies on `F`.  Contract `K` to `z` and fix a
proper six-colouring `c` of the resulting minor.  Put

\[
 \alpha=c(z),\qquad
 L(w)=\{1,\ldots,6\}-c(N_G(w)\cap S)\quad(w\in K).
\tag{1.1}
\]

Every list contains `alpha`.  Every vertex strictly inside `F` has the
full six-element list.

## Theorem 1 (single-edge localization)

Suppose `|F|>=4` and `x,y` are adjacent vertices of `F`,

\[
                         L(x)=L(y)=\{\alpha\},             \tag{1.2}
\]

and every other vertex of `F` has a list of order at least three.  Then
the restriction of `c` to `G-K` extends to both

\[
                             G/xy\quad\hbox{and}\quad G-xy. \tag{1.3}
\]

In the deletion extension, `x` and `y` both receive `alpha`.  Hence the
labelled equality partition of the full actual adhesion `S` produced by
the total contraction `G/K` is already produced by the single internal
edge operation `xy`.

### Proof

Contract the outer-cycle edge `xy` inside the plane graph `K`, and call
its image `p`.  Delete loops and suppress parallel copies of edges.  The
resulting plane graph `K'=K/xy` has outer facial cycle `F/xy`: because
`|F|>=4` in the locked application, this is a cycle of order at least
three.  Give `p` the singleton list `{alpha}` and retain every other
vertex's list from (1.1).

Choose either neighbour `q` of `p` on `F/xy`.  It is the image of a
vertex of `F-{x,y}` and therefore has a list of order at least three.
Since every list contains `alpha`, choose

\[
                         \beta\in L(q)-\{\alpha\}.
\]

Temporarily replace the lists at the outer edge `pq` by `{alpha}` and
`{beta}`.  Every other outer vertex has a list of order at least three,
and every interior vertex has its full six-element list, hence a list of
order at least five.  Thomassen's outer-face list-extension theorem
therefore gives an `L`-colouring of `K'` with

\[
                              p=\alpha,qquad q=\beta.
\]

By the definition of the lists, this colouring has no conflict with the
fixed colouring `c` across an edge from `K` to `S`.  It consequently
glues to `c` on `G-K`, giving a six-colouring of `G/xy`.

Alternatively split the contracted vertex `p` back into the two
vertices `x,y`, give both of them colour `alpha`, and omit their mutual
edge.  All other internal and external edges remain proper, so this is a
six-colouring of `G-xy`.  The colouring on `S` was never changed, proving
the final boundary-state assertion. \(\square\)

## Corollary 2 (exact two-heavy reduction)

Under the hypotheses of the audited harmonica gate, suppose the carrier
is four-connected, the active face contains four distinct literal portal
representatives, and the total-contraction state has exactly two heavy
vertices.  If the host is not six-colourable, then either

1. the two heavy vertices are nonadjacent; or
2. their common forced state is realized by one facial-edge contraction
   and deletion as in Theorem 1.

### Proof

The harmonica gate excludes the one-singleton/one-two-list obstruction
in this carrier.  Its two-heavy dichotomy therefore leaves only two
singleton lists `{alpha}`.  Apply Theorem 1 when their vertices are
adjacent. \(\square\)

## Exact remaining gap

Theorem 1 replaces a whole-carrier operation by one named facial edge,
which is the smallest possible support for an internal proper-minor
state.  It does not show that the same labelled equality partition occurs
after an operation in the opposite shore.  Nor does it handle a
nonadjacent double-forced pair.  Closing the gate still requires one of:

* an opposite-shore operation with the same partition, giving the
  audited crossed splice;
* a literal protected linkage forced by the two singleton portals; or
* a coherent recursion proving that every localized forced edge belongs
  to the boundary of one global rural strip with one fixed apex pair.
