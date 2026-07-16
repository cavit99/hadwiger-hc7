# A two-vertex transversal of `K_5`-minor models yields an order-seven separation

**Status:** written proof; separately internally audited in
[`hc7_k5_transversal_order_seven_separation_audit.md`](hc7_k5_transversal_order_seven_separation_audit.md).

A **separation** of a graph `G` is a pair `(A,B)` of vertex sets such
that

\[
 A\cup B=V(G)
 \quad\text{and}\quad
 E_G(A-B,B-A)=\varnothing.
\]

Its order is `|A\cap B|`.  It is **actual** when both `A-B` and `B-A`
are nonempty.

## Theorem (two-vertex `K_5`-minor transversal)

Let `G` be a finite simple seven-connected graph and let
`P={p,q}\subseteq V(G)`.  Suppose that `P` meets the vertex-union of
every `K_5`-minor model in `G`.  Equivalently, suppose that `G-P` has no
`K_5` minor.

Then `G` has an actual separation `(A,B)` of order seven such that

\[
                         P\subseteq A\cap B.
\]

### Proof

Put `H=G-P`.  First, `H` is five-connected.  Indeed, if
`X\subseteq V(H)` with `|X|\le 4` disconnected `H`, then

\[
                         G-(X\cup P)=H-X
\]

would be disconnected.  Thus `X\cup P` would be a vertex cut of `G`
of order at most six, contrary to seven-connectivity.

We also have `|V(H)|\ge 7`.  Seven-connectivity gives
`|V(G)|\ge 8`, so `|V(H)|\ge 6`.  If equality held, the
five-connected graph `H` would be `K_6`, and hence would contain a
`K_5` minor, contrary to the hypothesis.

Suppose for a contradiction that `H` is six-connected.  Then `H` is,
in particular, four-connected.  The four-connected consequence of
Wagner's characterization of `K_5`-minor-free graphs says that every
four-connected `K_5`-minor-free graph is planar.  Hence `H` is planar.

On the other hand, six-connectivity implies

\[
                              \delta(H)\ge 6.
\]

Every finite simple planar graph on `n\ge3` vertices has at most
`3n-6` edges, and therefore has average degree strictly less than six.
It has a vertex of degree at most five.  This contradicts the displayed
inequality.  Consequently `H` is not six-connected.

Because `H` is five-connected and has at least seven vertices, there is
a vertex cut `X\subseteq V(H)` of order exactly five.  Choose one
component `C` of `H-X`, and put

\[
 D=V(H)-(X\cup C),\qquad
 A=C\cup X\cup P,\qquad
 B=D\cup X\cup P.
\]

Both `C` and `D` are nonempty.  Since `C` is a component of `H-X`,
there is no edge of `G` from `C` to `D`: all vertices of `P` have been
placed in the common separator.  Thus `(A,B)` is an actual separation
of `G`, and

\[
                 A\cap B=X\cup P,
                 \qquad |A\cap B|=5+2=7.
\]

In particular, `P\subseteq A\cap B`, as required.  \(\square\)

## External input

The only structural input is Wagner's characterization:

> A graph has no `K_5` minor if and only if it can be obtained by
> `0`-, `1`-, `2`-, and `3`-clique-sums from planar graphs and the
> eight-vertex Wagner graph `V_8`.

A modern exact statement is Theorem 1.2 of Sergey Norin,
“New tools and results in graph minor structure theory,” in *Surveys in
Combinatorics 2015*, pp. 221–260,
[doi:10.1017/CBO9781316106853.008](https://doi.org/10.1017/CBO9781316106853.008).
The original source is Klaus Wagner, “Über eine Eigenschaft der ebenen
Komplexe,” *Mathematische Annalen* **114** (1937), 570–590,
[doi:10.1007/BF01594196](https://doi.org/10.1007/BF01594196).

For a four-connected graph, every nontrivial clique-sum in that
description would display a vertex cut of order at most three, while
`V_8` is only three-connected.  The four-connected graph must therefore
be planar.  This is the precise consequence used above.

## Scope

The theorem converts a global two-vertex transversal of `K_5`-minor
models into an actual order-seven separation containing the same two
vertices.  It does not preserve any prescribed colouring partition,
minor-model branch sets, or labels across that separation.
