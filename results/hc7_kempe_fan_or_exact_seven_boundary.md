# Three Kempe connections give a packing or an exact-seven boundary

**Status:** written proof; separate internal audit.  This is a host-level
consequence of the boundary-edge colouring in the degree-eight branch.  It
produces either three paths which are disjoint away from their prescribed
terminals or an actual order-seven separation carrying one side of that
colouring.  It does not prove that the equality partition on the new
boundary extends through the other closed shore.

## 1. Setup

Let `G` be seven-connected, and let

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |T|=7,                                           \tag{1.1}
\]

where `L` is nonempty.  Write

\[
 T=I\mathbin{\dot\cup}J\mathbin{\dot\cup}\{b,q,r\},
 \qquad |I|=|J|=2,                                      \tag{1.2}
\]

and put

\[
                         F=E_G(\{b\},I).                \tag{1.3}
\]

Let `c` be a proper six-colouring of `G-F` such that

\[
 c(b)=c(i) = \alpha\quad(i\in I),
 \qquad
 c(q)=c(j)=\delta\quad(j\in J),                         \tag{1.4}
\]

where `alpha` and `delta` are distinct.  Suppose that
`beta_1,beta_2,beta_3` are distinct colours absent from `T` and, for each
`k`, there is an `alpha,beta_k` path `P_k` from `b` to `I` in

\[
                         G[R\cup T]-F                    \tag{1.5}
\]

which stops at its first vertex of `I` and whose internal boundary
vertices, if any, belong to `{r}`.

These hypotheses are supplied by the audited boundary-edge Kempe theorem.
In particular, the three paths come from one colouring, rather than from
three separately chosen proper-minor responses.

Put

\[
        H=\bigl(G[R\cup\{b,r\}\cup I]\bigr)-F.          \tag{1.6}
\]

Every `P_k` is a path in `H`.

## 2. The packing-or-separation theorem

### Theorem 2.1

Under the setup of Section 1, at least one of the following holds.

1. The graph `H` contains three `b`--`I` paths which are pairwise
   vertex-disjoint outside the terminal set `\{b\}\cup I`.  Their ends in
   `I` are allowed to coincide.
2. There are a nonempty connected set \(A\subseteq R\) and a two-set
   \(Z=\{z_1,z_2\}\subseteq R\) such that

   \[
              N_G(A)=(T-I)\mathbin{\dot\cup}Z.          \tag{2.1}
   \]

   Thus `N_G(A)` is the boundary of an actual nontrivial order-seven
   separation.  The five literal vertices in `T-I`, including `b`, `r`,
   and \(J\cup\{q\}\), remain on that boundary, while `I` lies on the
   opposite open side.

In outcome 2, every selected path `P_k` meets `Z`.  At least one member of
`Z` lies on two of the three selected paths and has colour `alpha`.
Moreover

\[
                     c\big|_{G[A\cup N_G(A)]}           \tag{2.2}
\]

is a proper six-colouring of this closed side in the original graph `G`.
Its boundary partition contains \(J\cup\{q\}\) in one monochromatic block
and contains `b` together with at least one member of `Z` in an
`alpha`-coloured block.

### Proof

Use the vertex-capacitated form of Menger's theorem in `H`, assigning
capacity one to every vertex outside `\{b\}\cup I` and infinite capacity
to the three terminals.  Equivalently, this is the standard terminal-set
version in which a separator is required to avoid `\{b\}\cup I`, paths
may share `b` and their final vertex in `I`, and all their other vertices
must be disjoint.

If the maximum packing has order at least three, outcome 1 holds.  Suppose
otherwise.  Menger's theorem gives a set

\[
 Z\subseteq V(H)-(\{b\}\cup I),
 \qquad |Z|\le2,                                        \tag{2.3}
\]

which meets every `b`--`I` path in `H`.

The first vertex after `b` on `P_k` has colour `beta_k`.  It belongs to
`R`: the colour `beta_k` is absent from `T`, and the only permitted
internal boundary vertex is `r`.  These three first vertices are distinct
because their colours are distinct.  Since \(|Z|\le2\), one of them, say
`x`, is not in `Z`.

Let `U` be the set of vertices reachable from `b` in `H-Z`, and let `A`
be the component of \(G[R\cap U]\) containing `x`.  The set `A` is nonempty
and connected, and \(b\in N_G(A)\) because `bx` is the first edge of the
corresponding selected path.

We claim that

\[
                         N_G(A)\subseteq Z\cup(T-I).     \tag{2.4}
\]

There is no edge from `A` to `L` by (1.1).  If a vertex of `R-A` is
adjacent to `A` and is not in `Z`, it is reachable from `b` in `H-Z` and
belongs to the same component of \(G[R\cap U]\), a contradiction.  Finally,
if `A` has a neighbour in `I`, a path in `H-Z` from `b` to `x`, followed
by a path in `A` and that last edge, is a `b`--`I` path avoiding `Z`, also
a contradiction.  This proves (2.4).  Restoring the edges of `F` does not
affect this calculation: every such edge has one end at `b` and the other
in `I`, and neither end lies in `A`.

The nonempty set `L` lies outside \(A\cup N_G(A)\), so `N_G(A)` is the
boundary of a genuine nontrivial separation.  Seven-connectivity and
(2.4) give

\[
 7\le |N_G(A)|
    \le |Z\cup(T-I)|
    \le 2+5=7.                                         \tag{2.5}
\]

All inequalities are equalities.  In particular, `|Z|=2` and `Z` is
disjoint from `T-I`.  The only boundary vertex of `H` outside
`\{b\}\cup I` is `r`; hence \(Z\subseteq R\).  Equality in (2.4) now gives
exactly (2.1).

Every `P_k` is a `b`--`I` path in `H`, so every one meets `Z`.  Three
nonempty subsets of a two-set cannot be pairwise disjoint; some
\(z\in Z\) lies on two selected paths.  Away from their ends, an
\(\alpha,\beta_k\) path and an \(\alpha,\beta_l\) path with \(k\ne l\)
can meet only at an `alpha`-coloured vertex.  Therefore `c(z)=alpha`.

It remains to verify the one-sided colouring assertion.  The colouring
`c` is proper on `G-F`.  No edge of `F` belongs to the closed graph
\(G[A\cup N_G(A)]\): its `b`-end lies on the boundary (2.1), while its
`I`-end lies on the opposite side.  Hence the restriction in (2.2) is
proper in the original graph.  The two stated monochromatic boundary
blocks follow from (1.4) and from `c(z)=c(b)=alpha`.  This completes the
proof.  \(\square\)

## 3. Exact scope

Outcome 2 is not yet terminal for `HC_7`.  The theorem proves a concrete
six-colouring on the `A`-side, but it does not prove that the same equality
partition extends through the opposite closed shore.  It also does not
prove that the five named far-side connected subgraphs survive as whole
subgraphs on specified sides of the new separation.

The theorem avoids two invalid shortcuts:

- it applies Menger's theorem in the whole literal graph `H`, not merely
  in the union of three selected Kempe paths; and
- it does not infer a host separator from a common vertex of selected
  two-colour paths.  The separator in outcome 2 is the full neighbourhood
  of the literal connected set `A`.

The unresolved branch is outcome 1: the three-path packing must be used to
peel a label-preserving connector while retaining a disjoint connected
subgraph with all seven required boundary contacts, or else to produce a
compatible order-seven separation or a strict labelled separator descent.

## 4. Dependencies

- [boundary-edge deletion and three Kempe connections](../results/hc7_degree8_blocker_edge_kempe_fork.md)
- [three selected paths need not have a common host bottleneck](../barriers/hc7_three_kempe_paths_common_bottleneck_barrier.md)
