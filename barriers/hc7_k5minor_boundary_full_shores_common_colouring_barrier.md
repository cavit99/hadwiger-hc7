# A `K_5`-minor-free boundary and two full shores need not have a common colouring

**Status:** written counterexample; separate internal audit GREEN in
[`hc7_k5minor_boundary_full_shores_common_colouring_barrier_audit.md`](hc7_k5minor_boundary_full_shores_common_colouring_barrier_audit.md).

This construction refutes the following state-free intermediate claim.

> If a boundary graph is `K_5`-minor-free and has a simplicial vertex whose
> two neighbours are adjacent, then any two anticomplete connected subgraphs
> full to the boundary admit six-colourings with a common labelled boundary
> colouring.

The example deliberately does not satisfy the full hypotheses of a
hypothetical `HC_7` counterexample.

## 1. Construction

Let

\[
 B=\{d,a,b,x,y,z,t_1,t_2,t_3\}
\]

and put

\[
                         E(G[B])=\{da,db,ab,xz\}.       \tag{1.1}
\]

Thus `d` has exactly the two adjacent boundary neighbours `a,b`.
The graph `G[B]` is the disjoint union of a triangle, an edge and three
isolated vertices, so it has no `K_5` minor.

Take two disjoint anticomplete five-cliques

\[
 L=\{l_1,\ldots,l_5\},\qquad
 R=\{r_1,\ldots,r_5\}.                                \tag{1.2}
\]

Add the following boundary-to-shore edges.

- Make `x` and `y` adjacent to every vertex of `L`, and join each of
  `d,a,b,z,t_1,t_2,t_3` to `l_1`.
- Make `y` and `z` adjacent to every vertex of `R`, and join each of
  `d,a,b,x,t_1,t_2,t_3` to `r_1`.

Both shores are connected and full to every literal vertex of `B`.

## 2. Each closed shore is six-colourable

For the `L`-side, give `l_i` colour `i`, give `x,y` colour six, and use

\[
 d=2,\qquad a=3,\qquad b=4,\qquad
 z=t_1=t_2=t_3=2.                                    \tag{2.1}
\]

This is proper: all boundary vertices joined only to `l_1` avoid colour
one, the triangle has three colours, and the edge `xz` has colours six and
two.

For the `R`-side, give `r_i` colour `i`, give `y,z` colour six, and use

\[
 d=2,\qquad a=3,\qquad b=4,\qquad
 x=t_1=t_2=t_3=2.                                    \tag{2.2}
\]

The same check proves that this is proper.

## 3. No common boundary colouring exists

In every proper six-colouring of the `L`-side, the clique `L` uses five
distinct colours.  Since `x` and `y` are each complete to `L`, both must
receive the unique sixth colour.  Hence

\[
                              c(x)=c(y).                \tag{3.1}
\]

Similarly, every proper six-colouring of the `R`-side satisfies

\[
                              c(y)=c(z).                \tag{3.2}
\]

A common boundary colouring would therefore give `c(x)=c(z)`, contrary to
the boundary edge `xz`.  Thus the two nonempty extension languages are
disjoint.

For clarity, the union graph is not a counterexample to Hadwiger's
conjecture.  It contains the explicit `K_7`-minor model

\[
 \{l_1\},\ldots,\{l_5\},\qquad
 \{x,z\},\qquad \{y,r_1\}.                           \tag{3.3}
\]

The last two sets are adjacent through `zr_1`; each is adjacent to every
`l_i` through `x` or `y` respectively.

## 4. Exact scope

The example has:

- a nine-vertex `K_5`-minor-free boundary;
- a simplicial boundary vertex on a triangle;
- two nonempty anticomplete connected boundary-full shores; and
- a proper six-colouring of each closed shore.

It lacks seven-connectivity, `K_7`-minor exclusion and the proper-minor
criticality of the live `HC_7` setting.  It therefore refutes only an
inference from the boundary structure and shore fullness alone.  In
particular it does not refute the operation-specific
[exact-block Kempe-transition theorem](../results/hc7_two_full_shore_exact_block_kempe_transition.md).
