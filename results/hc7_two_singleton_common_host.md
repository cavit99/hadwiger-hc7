# Two nonadjacent singleton roots over a common host

**Status:** written proof with a separate GREEN internal audit in
[`hc7_two_singleton_common_host_audit.md`](hc7_two_singleton_common_host_audit.md).

Throughout this note, a graph `G` is **strongly
seven-contraction-critical** if

\[
 \chi(G)=7
 \quad\text{and every proper minor of }G\text{ is six-colourable}.
\]

An **actual order-seven separation** is a separation `(A,B)` such that
both `A-B` and `B-A` are nonempty and `|A\cap B|=7`.

## Theorem 1 (two-singleton common-host lemma)

Let `G` be a seven-connected, strongly seven-contraction-critical graph
with no `K_7` minor.  Let `a,b` be distinct nonadjacent vertices, and put

\[
                         J=G-\{a,b\}.
\]

Then all of the following hold.

1. \(\chi(J)=6\).
2. `J` is five-connected.  If `G` has no actual order-seven separation,
   then `J` is six-connected.
3. `J` has a `K_6` minor.  Moreover, its branch sets may be chosen to
   partition `V(J)`.
4. In every proper six-colouring `c` of `J`, at least one of `a,b` sees
   all six colours in its neighbourhood in `J`:

   \[
      c(N_J(a))=\{1,\ldots,6\}
      \quad\text{or}\quad
      c(N_J(b))=\{1,\ldots,6\}.
   \]

5. There are six-colourings `c_a` of `G-a` and `c_b` of `G-b` such that
   their restrictions to `J` satisfy the opposite conditions

   \[
   \begin{array}{c|cc}
      &\text{deleted vertex sees all six colours in }J
      &\text{retained vertex misses its own colour in }J\\ \hline
   c_a&a&c_a(b)\notin c_a(N_J(b))\\
   c_b&b&c_b(a)\notin c_b(N_J(a)).
   \end{array}
   \]

   More explicitly,
   `c_a(N_J(a))={1,...,6}` and
   `c_b(N_J(b))={1,...,6}`.

### Proof

Because `J` is a proper minor of `G`, it is six-colourable.  If it were
five-colourable, then assigning a sixth colour to both `a` and `b` would
give a proper six-colouring of `G`: the two vertices are nonadjacent and
their new colour does not occur on `J`.  This contradicts `chi(G)=7`.
Hence

\[
                              \chi(J)=6.                 \tag{1}
\]

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  For completeness, if a set `X\subseteq V(J)` of
order at most four disconnected `J`, then `X\cup\{a,b\}` would be a
vertex cut of `G` of order at most six.  If `X` has order five, then
`X\cup\{a,b\}` is the separator of an actual order-seven separation of
`G`.  Thus, when the latter separations are excluded, `J` has no vertex
cut of order at most five.  Also `|V(J)|\ge 7`.  Indeed, a
seven-connected graph has at least eight vertices; if `|V(J)|\le6`,
then `|V(G)|=8` and minimum degree at least seven forces `G=K_8`,
contrary to the absence of a `K_7` minor.  Consequently `J` is
six-connected under the additional hypothesis.

Hadwiger's conjecture is known for parameter six.  Its contrapositive,
together with (1), gives a `K_6` minor in `J`.  Let
`B_1,...,B_6` be its branch sets.  For every component `C` of

\[
                  J-\bigcup_{i=1}^6 B_i,
\]

connectedness of `J` gives an edge from `C` to at least one branch set.
Assign `C` to one such branch set.  After all components are assigned,
the enlarged branch sets remain pairwise disjoint, connected and
pairwise adjacent, and they partition `V(J)`.  This proves item 3.

Now let `c` be any proper six-colouring of `J`.  If neither `a` nor `b`
sees all six colours, choose a colour `alpha` absent from `c(N_J(a))`
and a colour `beta` absent from `c(N_J(b))`.  Extending `c` by

\[
                         c(a)=\alpha,\qquad c(b)=\beta
\]

is proper; there is no edge `ab`, so `alpha` and `beta` need not be
distinct.  This would six-colour `G`, a contradiction.  Item 4 follows.

Finally, strong contraction-criticality supplies a six-colouring `c_a`
of the proper minor `G-a`.  Its restriction to `J` is proper, and

\[
                         c_a(b)\notin c_a(N_J(b))          \tag{2}
\]

because `b` is present in that colouring.  Thus `b` does not see all six
colours in `J`; item 4 applied to `c_a|_J` forces

\[
                         c_a(N_J(a))=\{1,\ldots,6\}.       \tag{3}
\]

Interchanging `a` and `b` gives a six-colouring `c_b` of `G-b` with

\[
 c_b(a)\notin c_b(N_J(a)),\qquad
 c_b(N_J(b))=\{1,\ldots,6\}.
\]

This proves item 5.  \(\square\)

## Scope

The theorem supplies a common six-chromatic, and in the no-order-seven
branch six-connected, host for two opposite colouring witnesses and a
spanning `K_6`-minor model.  It does **not** assert that the same branch-set
model is compatible with either colouring, nor that one can prescribe a
branch set containing a neighbour of each of `a,b`.  That
colouring-to-labelled-model compatibility is the remaining rooted-model
problem.
