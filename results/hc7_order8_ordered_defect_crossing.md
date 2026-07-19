# Ordered crossings of the two deficient connected subgraphs

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_ordered_defect_crossing_audit.md`](hc7_order8_ordered_defect_crossing_audit.md).
This is an unbounded branch-set reduction inside the connected order-eight
interface.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
\]

where

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
\]

Assume that `G[S]` contains the two vertex-disjoint triangles

\[
                   d x_d y_d d,
             \qquad e x_e y_e e.                    \tag{1.1}
\]

Assume also that `d,e` are nonadjacent.  Further edges in `G[S]` are
permitted.  Suppose that `G[R]` contains
vertex-disjoint connected subgraphs `P_0,P_1` such that each is adjacent
to every vertex of `S` and there is a `P_0`--`P_1` edge.

Suppose that `G[L]` contains vertex-disjoint connected subgraphs
`A_d,A_e` such that

\[
 S-\{d\}\subseteq N_G(A_d)\cap S,
 \qquad
 S-\{e\}\subseteq N_G(A_e)\cap S,                  \tag{1.2}
\]

and there is an `A_d`--`A_e` edge.  Thus `A_d` may fail to be adjacent
to `d`, while `A_e` may fail to be adjacent to `e`.

A **root connector in `L`** is a nonempty connected subgraph
`D subseteq G[L]` having a neighbour at each of `d,e`.

## 2. Every root connector meets both deficient subgraphs

### Theorem 2.1

If `G` has no `K_7` minor, then every root connector in `L` meets both
`A_d` and `A_e`.

#### Proof

Let `D` be a root connector.

First suppose that `D` is disjoint from `A_e`.  Consider the following
seven vertex sets:

\[
 \begin{split}
 P_0,\quad P_1,\quad
 \{d\},\quad \{x_d\},\quad \{y_d\},\quad
 V(A_e)\cup\{x_e\},\quad
 V(A_d)\cup V(D)\cup\{e\}.                         \tag{2.1}
 \end{split}
\]

They are pairwise disjoint.  The sixth set is connected because `A_e`
is adjacent to `x_e`.  The last set is connected because both `A_d` and
`D` are connected and each is adjacent to `e`; an intersection between
`A_d` and `D` causes no difficulty.

The first two sets are adjacent and each is adjacent to every other set
through the boundary vertex contained in that set.  The three singleton
sets are pairwise adjacent by the first triangle in (1.1).  The sixth set
is adjacent to those singletons because `A_e` is adjacent to
`d,x_d,y_d`.  The last set is adjacent to `\{d\}` through `D`, and to
`\{x_d\},\{y_d\}` through `A_d`.  Finally, the last two sets are adjacent
through the `A_d`--`A_e` edge (and also through `e x_e`).  Hence (2.1) is
an explicit `K_7`-minor model, a contradiction.

Now suppose that `D` is disjoint from `A_d`.  The symmetric seven sets

\[
 P_0,\quad P_1,\quad
 \{e\},\quad \{x_e\},\quad \{y_e\},\quad
 V(A_d)\cup\{x_d\},\quad
 V(A_e)\cup V(D)\cup\{d\}                          \tag{2.2}
\]

are again pairwise disjoint and connected.  Boundary fullness handles
the first two sets, the second triangle in (1.1) handles the three
singletons, `A_d` is adjacent to `e,x_e,y_e`, and `A_e` is adjacent to
`x_e,y_e` while `D` supplies its adjacency to `e`.  The last two sets
are adjacent through the `A_d`--`A_e` edge (and through `d x_d`).  Thus
(2.2) is another explicit `K_7`-minor model.  This contradiction proves
the theorem. \(\square\)

## 3. The forced order of every root-to-root path

### Corollary 3.1

Assume that `G` has no `K_7` minor.

1. Every path in `G[L union {d}]` from `d` to `A_d` meets `A_e`.
2. Every path in `G[L union {e}]` from `e` to `A_e` meets `A_d`.
3. On every `d`--`e` path whose internal vertices lie in `L`, the first
   member of `A_d union A_e` encountered from `d` belongs to `A_e`, and
   the last member encountered before `e` belongs to `A_d`.

#### Proof

If a `d`--`A_d` path avoided `A_e`, unite its vertices other than `d`
with `A_d`.  The resulting connected subgraph of `L` is adjacent to `d`
through the first path edge and to `e` by (1.2).  It is therefore a root
connector disjoint from `A_e`, contrary to Theorem 2.1.  This proves the
first assertion; the second is symmetric.

The internal vertices of a `d`--`e` path form a root connector, so the
path meets both deficient subgraphs.  If its first encounter with their
union were in `A_d`, its initial segment would contradict assertion 1.
Reading the path backwards shows from assertion 2 that its last encounter
must be in `A_d`. \(\square\)

## 4. Application to the three merged-root Kempe paths

Assume additionally that a proper six-colouring of `G[L union S]`
induces the boundary equality partition

\[
                 X\mid Y\mid\{d,e\},
\]

where `S-{d,e}=X dotcup Y`, and that the split-root partition does not
extend through this closed shore.  Let `alpha` be the common colour of
`d,e`, and let `beta_1,beta_2,beta_3` be the three colours absent from
the boundary.  The audited merged-root Kempe-path theorem supplies, for
each `i`, an `alpha`--`beta_i` path `K_i` from `d` to `e` whose internal
vertices lie in `L`.  Distinct such paths can intersect only at vertices
of colour `alpha`.

### Corollary 4.1

Each `K_i` first enters `A_e` and last leaves `A_d`.  If the first
`A_e`-vertices of `K_i,K_j` coincide, or if their last `A_d`-vertices
coincide, then the common vertex has colour `alpha`.

#### Proof

The order assertion is Corollary 3.1.  A coincident first or last vertex
belongs to both paths, and hence has the only colour common to
`{alpha,beta_i}` and `{alpha,beta_j}`, namely `alpha`. \(\square\)

Thus the three colour-indexed paths are not arbitrary root connectors:
in every `K_7`-minor-free survivor they cross the two named connected
subgraphs in the same order.  This conclusion preserves the literal
subgraph labels and does not identify a palette colour with a branch-set
label.

## 5. A barrier to an alpha-only trimmed-path argument

For each `K_i`, one may trim the path from its last vertex in `A_e`
before a subsequent first vertex in `A_d`.  The resulting passage has
one end in each deficient subgraph and has no internal vertex in either.
The following elementary configuration shows that the intersection rule
alone does not finish the argument.

Take distinct vertices

\[
 a_1,a_2,a_3\in A_e,
 \qquad b_1,b_2,b_3\in A_d,
\]

and let the three trimmed passages be the three independent edges

\[
                          a_i b_i\qquad(i=1,2,3).       \tag{5.1}
\]

They satisfy the required pairwise-intersection rule vacuously.  No
passage has an internal vertex, so their union supplies no connected
subgraph disjoint from `A_d union A_e` and adjacent to both.  Moreover,
every vertex set meeting all three passages has order at least three.
Consequently the proposed abstract dichotomy

\[
 \begin{gathered}
 \text{an outside connected subgraph adjacent to both deficient
 subgraphs,}\quad\text{or}\quad
 \text{two common alpha-coloured vertices meeting all three passages}
 \end{gathered}
\]

is false.

This is only a barrier to that path-system inference.  Configuration
(5.1) is not asserted to occur in a seven-connected, contraction-critical,
`K_7`-minor-free host with the complete opposite-response data.  Ruling it
out in the live branch requires a label-preserving split or rerouting of
`A_d,A_e`, or a full-neighbourhood separation obtained from the host; it
cannot be obtained from the alpha-only intersection rule by itself.

## 6. Exact gain and trust boundary

Theorem 2.1 closes every configuration containing a root connector that
avoids either deficient connected subgraph, for arbitrary shore sizes.
Corollary 4.1 then places all three merged-root Kempe paths in a common
ordered form.

The result does not produce a two-vertex transversal of the `X`- and
`Y`-support families in the opposite shore, a compatible order-seven
separation, or a strict selected-response descent.  Those support families
depend on literal incidence in `R`, whereas the theorem constrains paths
inside `L`.  The three-edge configuration in Section 5 identifies the
remaining label-preserving splitting issue exactly.

## 7. Immediate dependencies

- the adjacent connected boundary-full cover on the split-response shore;
- the connected pair `A_d,A_e` with the boundary contacts in (1.2); and
- [three colour-indexed Kempe paths on the merged-response shore](../results/hc7_merged_root_three_kempe_locks.md).
