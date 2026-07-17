# Selected Kempe fans do not repair the exact order-eight near-clique model

**Status:** explicit counterexample to an intermediate claim, with a
deterministic verifier in
[`hc7_order_eight_selected_kempe_fan_barrier_verify.py`](hc7_order_eight_selected_kempe_fan_barrier_verify.py).
This note does **not** refute the universal colour-saturation theorem, a
statement using every six-colouring of the common host, or Hadwiger's
conjecture for parameter seven.

## 1. The false strengthening

The following collection of local data does not force a `K_7` minor, even
when it occurs at the literal exceptional order-eight separation:

1. two nonadjacent singleton roots over a spanning five-branch-set
   `K_5` model;
2. a six-chromatic common host obtained by deleting the roots;
3. a six-colouring after deleting either root in which the deleted root
   sees every colour and the retained root misses its own colour; and
4. for each of the five other colours, an internally disjoint
   bichromatic path between the two roots.

The example below also shows that these selected paths need not give an
order-seven boundary, and that the two nominated roots need not meet every
`K_5` minor.  Its purpose is to isolate the hypothesis which is still
capable of doing work: **every** six-colouring of the common host must make
at least one root see all six colours.  Merely selecting the two opposite
deletion colourings, even with their complete path systems, loses that
global condition.

## 2. The graph and its ambient properties

Let `I` be the icosahedral graph.  Use vertices

\[
 t,d,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and, with subscripts modulo five, edges

\[
 tu_i,\quad dw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.                         \tag{2.1}
\]

Add adjacent vertices `p,q`, each complete to `I`, and put

\[
                              G=K_2\vee I.               \tag{2.2}
\]

### Proposition 2.1

The graph `G` is seven-connected and has no `K_7` minor.  The pair
`{p,q}` meets every `K_5`-minor model.

### Proof

The icosahedral graph is planar and five-connected.  If at most six
vertices are deleted from `G` and one of `p,q` remains, that remaining
vertex joins all other surviving vertices.  If both are deleted, at most
four vertices of `I` were also deleted, and the remainder is connected.
Thus `G` is seven-connected.

Suppose `G` had a `K_7`-minor model.  At most two of its branch sets
contain `p` or `q`.  Removing those branch sets leaves at least five
pairwise adjacent connected branch sets in `I`, a `K_5` minor in the
planar graph `I`, which is impossible.  The same planarity observation
shows directly that deleting `p,q` destroys every `K_5`-minor model.
\(\square\)

The verifier checks a combinatorial spherical triangulation of `I`, as
well as five-connectivity of `I` and seven-connectivity of `G` by exhaustive
vertex-deletion tests.

## 3. A literal exceptional order-eight separation

Put

\[
\begin{aligned}
 R&=\{p,q,t\},& e&=u_0w_0,& f&=u_2w_2,& x&=d,\\
 C&=\{u_3,u_4,w_3,w_4\},&&
 D&=\{u_1,w_1\}.
\end{aligned}                                             \tag{3.1}
\]

Then

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
      \mathbin{\dot\cup}\{x\}                           \tag{3.2}
\]

has order eight.  The set `R` is a clique, `e,f` are edges and are
anticomplete to one another, and each of `e,f` is collectively adjacent
to every member of `R`.  The two components of `G-S` are exactly `C,D`,
and each is adjacent to every literal vertex of `S`.

Choose

\[
                              a=u_0,\qquad b=u_2.          \tag{3.3}
\]

The following five connected sets form a spanning `K_5`-minor model in
`J=G-\{a,b\}` and are each adjacent to both roots:

\[
 C,\quad D\cup\{d,w_0,w_2\},\quad \{p\},\quad\{q\},
 \quad\{t\}.                                              \tag{3.4}
\]

Together with the singleton roots `{a},{b}`, they form a spanning
`K_7`-minus-one-edge model whose sole absent branch-set adjacency is
`ab`.  Thus the construction has the exact normalization used in the
order-eight branch; it is not merely an abstract near-clique model.

The graph `J` is exactly six-chromatic.  It is six-colourable by the
colouring in Section 5.  For the lower bound, `J` contains the odd wheel
on `d,w_0,\ldots,w_4`, which is four-chromatic, and the adjacent universal
vertices `p,q` require two further colours.

## 4. Two opposite deletion colourings and ten disjoint connectors

Colour labels are `1,...,6`.  A first proper six-colouring `c_a` of
`G-a` has colour classes

\[
\begin{array}{c|l}
1&d,u_1,u_3\\
2&w_0,w_3,b\\
3&u_4,w_1\\
4&t,w_2,w_4\\
5&p\\
6&q.
\end{array}                                               \tag{4.1}
\]

The retained root `b` has colour two and no neighbour of colour two,
while the deleted root `a` has a neighbour in every colour class.  For
the five colours other than two, respectively, the paths

\[
 a u_1 b,\quad
 a w_0 w_1 b,\quad
 a t b,\quad
 a p b,\quad
 a q b                                                   \tag{4.2}
\]

use internally only colours `{2,beta}` for
`beta=1,3,4,5,6`.  Their interiors are pairwise vertex-disjoint.

Symmetrically, a proper six-colouring `c_b` of `G-b` has classes

\[
\begin{array}{c|l}
1&d,u_3,a\\
2&w_0,w_3,t\\
3&u_4,w_1\\
4&u_1,w_2,w_4\\
5&p\\
6&q.
\end{array}                                               \tag{4.3}
\]

Now `a` has colour one and no neighbour of colour one, while `b` sees all
six colours.  For `beta=2,3,4,5,6`, the five paths are

\[
 b t a,\quad
 b u_3u_4 a,\quad
 b u_1a,\quad
 b p a,\quad
 b q a.                                                   \tag{4.4}
\]

Again their interiors are pairwise disjoint, and after the deleted root
is omitted each path uses only colours `{1,beta}`.

Consequently even the strengthening “all five alternatives are
root-to-root paths, pairwise internally disjoint within each deletion
witness” does not produce a labelled split of (3.4): `G` has no `K_7`
minor by Proposition 2.1.

Nor does a selected bichromatic component automatically return an exact
order-seven separation.  In `c_a`, the `{2,3}`-component of `G-a`
containing `b` is

\[
                             K=\{u_2,w_0,w_1\}.           \tag{4.5}
\]

Its open neighbourhood in `G` is

\[
 N_G(K)=\{d,p,q,t,u_0,u_1,u_3,w_2,w_4\},                \tag{4.6}
\]

of order nine.  Deleting it leaves `K` and the nonempty connected set
`{u_4,w_3}`, so (4.6) is an actual order-nine separator.

## 5. The indispensable hypothesis which the example fails

The common host `J` has the proper six-colouring

\[
\begin{array}{c|l}
1&d,u_3\\
2&w_0,w_3\\
3&u_1,u_4,w_2\\
4&t,w_1,w_4\\
5&p\\
6&q.
\end{array}                                               \tag{5.1}
\]

In (5.1), the root `a` misses colour one on its neighbourhood and `b`
misses colour two.  It therefore extends to a six-colouring of `G` by
assigning those two colours to `a,b`.  This is exactly why the example is
not a hypothetical `HC_7` counterexample.

Thus the universal condition

> every six-colouring of `J` makes at least one of `a,b` adjacent to all
> six colour classes

is not a consequence of the exact order-eight geometry, six-chromaticity
of `J`, the two exclusive deletion witnesses, or their ten bichromatic
paths.  Any valid continuation must use that universal quantifier, rather
than treat the two selected fan systems as a substitute for it.

Two final checks locate the permitted global outcomes.  The nominated
roots are not a `K_5`-minor transversal, because

\[
                         \{p,q,t,u_3,u_4\}               \tag{5.2}
\]

induces a `K_5` in `G-\{a,b\}`.  On the other hand, the unrelated pair
`{p,q}` is a valid global transversal, and

\[
                         \{p,q,u_0,u_1,u_2,u_3,u_4\}     \tag{5.3}
\]

is an actual order-seven separator: after its deletion, `t` is isolated
from the connected lower wheel.  Hence the example does not refute the
full conclusion “`K_7`, an actual order-seven separation, or some
two-vertex `K_5`-minor transversal.”  It shows precisely that the selected
Kempe fans alone cannot prove that conclusion.
