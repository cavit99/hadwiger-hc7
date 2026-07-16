# Decorated three-model `H`-path composition

**Status:** active global proof attempt with one retracted decoder.  The
packing and obstruction lemmas below are proved.  The boxed decoder in
Section 4 is false; an exact 15-vertex falsifier is recorded in
[`../barriers/hc7_decorated_hwege_genuine_cell_falsifier.md`](../barriers/hc7_decorated_hwege_genuine_cell_falsifier.md).
The stronger minimal-bad quotient condition in Section 5 remains under
test.

This note treats the separated branch of the support-six programme without
selecting portals inside a shore.  Its input is three pairwise disjoint
minor models, and its only intended outputs are a literal `K_7` or an actual
model-preserving separation of order seven.

## 1. Setup and target

Let `G` be seven-connected.  For `i=1,2,3`, let `M_i` be a `K_5` model
with four singleton bags forming a clique `Q_i` and one two-vertex bag
`x_i y_i`.  Assume the three supports are pairwise vertex-disjoint, and
put

\[
 F=\{x_1y_1,x_2y_2,x_3y_3\},\qquad H=G/F.
\]

Write `z_i` for the image of `x_i y_i` and

\[
                         L_i=Q_i\cup\{z_i\}.
\]

The `L_i` are pairwise disjoint literal `K_5` cliques in `H`.  Give each
`z_i` weight two and every other vertex weight one.  If `T` separates
`H`, its expansion separates `G`, and hence

\[
             w(T):=|T|+|T\cap\{z_1,z_2,z_3\}|\ge 7.       \tag{1.1}
\]

The exact target is the following.

> **Decorated three-model decoder.**  Either `G` contains a `K_7` minor,
> or `G` has a separation of order seven with both open shores nonempty
> such that every `M_i` lies in one of its two closed shores.

The second outcome is an accepted ranked handoff once one literal root is
fixed in each open shore and the side of every named model is retained.

## 2. Seven good paths are already a literal minor

Call a path in `H` **good** if its two ends lie in distinct members of
`{L_1,L_2,L_3}`.  Shorten it, if necessary, so that its internal vertices
avoid `L_1\cup L_2\cup L_3`.

### Lemma 2.1 (path-packing decoder)

If `H` contains seven pairwise vertex-disjoint good paths, then `G`
contains a `K_7` minor.

### Proof

Contract each of the seven paths to one connected bag.  Associate to a
path the unordered pair of clique labels containing its ends.  Any two
unordered pairs from the three labels intersect.  At a common label, the
two paths use distinct vertices of the corresponding literal clique,
because the paths are vertex-disjoint.  Those two endpoint vertices are
adjacent, so the two contracted path bags are adjacent.  The seven bags
therefore form a `K_7` model in `H`.  Expanding the three contractions
`x_i y_i -> z_i` gives a `K_7` model in `G`.  \(\square\)

This proof is exactly why the split edge must first be treated as one
indivisible branch bag.  Seven ordinary paths between the six-vertex
supports need not be branch-bag-injective.

## 3. The exact Mader obstruction

Assume henceforth that the first outcome of Lemma 2.1 is absent.  Apply
the `H`-path lemma in the form of Robertson--Seymour--Thomas (equivalently
Lemma 3.2 of Kawarabayashi--Luo--Niu--Zhang) to
`L_1,L_2,L_3` with packing target seven.  It gives a set `W`, a partition

\[
                  Y_1\dot\cup\cdots\dot\cup Y_n=V(H)-W,
\]

and sets `X_j subseteq Y_j` such that

\[
 |W|+\sum_{j=1}^n\left\lfloor\frac{|X_j|}{2}\right\rfloor
       \le 6,                                           \tag{3.1}
\]

every vertex of `Y_j-X_j` has no neighbour outside `W\cup Y_j`, every
vertex of `(L_1\cup L_2\cup L_3)\cap Y_j` belongs to `X_j`, and every
good path in `H-W` has an edge with both ends in some `Y_j`.

Choose such a certificate with `|W|` maximum, deleting empty cells.

### Lemma 3.1 (maximal-certificate arithmetic)

For this choice:

1. equality holds in (3.1);
2. every nonempty `X_j` has odd order; and
3. if `o` is the number of nonempty sets `X_j`, then

   \[
                              o\ge |W|+3.               \tag{3.2}
   \]

### Proof

If `|X_j|` were positive and even, move one vertex of `X_j` into `W`
and replace `Y_j,X_j` by their deletion of that vertex.  The separation
condition remains true, and every good path in the smaller graph was
already a good path in the old graph.  The contribution

\[
  |W|+\left\lfloor |X_j|/2\right\rfloor
\]

is unchanged.  This contradicts maximality of `|W|`.  Thus every
nonempty `X_j` is odd.  No assertion about cells with `X_j=emptyset` is
needed or made.

If (3.1) were strict, moving one vertex from any `X_j` to `W` would raise
the left side by exactly one and preserve the certificate, again
contradicting maximality.  A nonempty `X_j` exists because the fifteen
terminal-clique vertices lie in `W union X_1 union ... union X_n` while
`|W|<=6`.  This proves equality.

The fifteen vertices of the three disjoint cliques all lie in
`W union X_1 union ... union X_n`.  Since the nonempty `X_j` are odd and
(3.1) is an equality,

\[
\begin{aligned}
15
 &\le |W|+\sum_j|X_j|\\
 &=|W|+2\sum_j\left\lfloor |X_j|/2\right\rfloor+o\\
 &=12-|W|+o.
\end{aligned}
\]

This is (3.2).  \(\square\)

### Lemma 3.2 (every genuine cell gives a model-preserving cut)

Suppose `Y_j-X_j` is nonempty and there is a vertex outside
`W\cup Y_j`.  Then `T_j=W\cup X_j` is a separator of `H`.  Its expanded
separator has order

\[
             w(T_j)=|W|+|X_j|+
                      |(W\cup X_j)\cap\{z_1,z_2,z_3\}|. \tag{3.3}
\]

Every one of the three named models lies in the closed shore opposite
`Y_j-X_j`.  In particular, if (3.3) equals seven, this is the required
actual model-preserving exact-seven handoff in `G`.

### Proof

The first assertion follows from the defining absence of edges from
`Y_j-X_j` to vertices outside `W\cup Y_j`.  No vertex of any `L_i` lies
in `Y_j-X_j`, because all clique vertices in `Y_j` belong to `X_j`.
Thus every literal quotient clique `L_i` lies in the other closed shore.
Expanding a boundary vertex `z_i` to `x_i,y_i`, or expanding it within
the other shore, restores the whole support of `M_i` in that same closed
shore.  Formula (3.3) is the size of the expanded boundary.  Equation
(1.1) makes a value at most seven equal to seven.  \(\square\)

## 4. Retracted genuine-cell decoder

The following standard-language statement would have been sufficient to
finish the proposed theorem, but it is false.

\[
\boxed{
\begin{minipage}{0.88\linewidth}
In a `K_7`-minor-free host satisfying (1.1), every maximal Mader
certificate (3.1) has a genuine cell whose expanded boundary (3.3) is at
most seven.
\end{minipage}}
                                                               \tag{4.1}
\]

A direct `K_7` decoder for every maximal certificate in which all genuine
cells have expanded boundary at least eight would likewise have sufficed.
However, the barrier cited above consists of three disjoint marked
`K_5`s covering all fifteen vertices.  It has weighted separator order
seven and no `K_7` minor.  Since every vertex is a named terminal, every
Mader cell has `Y_j=X_j`; no genuine cell exists at all.  Thus (4.1) is
retracted, not merely open.

The falsifier has ordinary connectivity five.  Its seven minimum
five-cuts each contain exactly two marks.  It therefore does **not**
refute the six-connected marked theorem in Section 5, nor the actual
minimal-three-contraction setting in which every proper predecessor is
seven-connected.  Exact search also finds that every minimum two-edge
augmentation repairing those five-cuts already has a `K_7` minor.  This
is evidence only, not a proof of the stronger theorem.

The proof attempt must therefore retain ordinary six-connectivity and the
all-three-marks property of six-cuts, or the still stronger literal
split-predecessor data.  Weighted separator order alone is exhausted.

## 5. Stronger minimal-triple formulation

For the global application one may first choose an inclusion-minimal
nonempty subset of the three split edges whose contraction is not
seven-connected.  The one-edge case is already an actual exact-seven
handoff.  If all three edges are needed, the quotient `H` has the stronger
property

\[
 \kappa(H)\ge6,
 \qquad
 T\text{ a six-separator }\Longrightarrow
 \{z_1,z_2,z_3\}\subseteq T.                         \tag{5.1}
\]

Indeed, splitting back any marked vertex omitted by a separator would
leave an order-at-most-six separator in the corresponding seven-connected
proper predecessor quotient.  Moreover, if a separator had order at most
five, it contains every marked vertex by the preceding observation, and
splitting back any one of them expands it by only one vertex.  This would
again give a separator of order at most six in a seven-connected proper
predecessor.  Hence `H` is six-connected, while the omitted-mark argument
gives the stated property of its six-separators.

This gives the cleaner theorem now under test.

> **Marked three-clique theorem.**  Let `H` be six-connected and contain
> three pairwise disjoint literal `K_5` cliques `L_i`, with prescribed
> `z_i in L_i`.  If every six-separator contains all three `z_i`, then
> `H` contains a `K_7` minor.

This statement is tailored to the minimal three-contraction branch, but
no longer mentions split-bag defects, colouring states, or portals.  The
terminal `5+5+5` equality cell of the published three-clique proof is
already excluded: each of its canonical six-cuts contains only one or two
marked vertices.  The missing work is an adaptation of the earlier
fan-and-cell steps, not the terminal matrix calculation.

The two-edge minimal-bad branch is not covered by this theorem and remains
the independent two-clique/common-deletion composition obligation.
