# Completion of the two-vertex fixed-boundary critical core

**Status:** written proof, independently audited in
[`hc7_two_vertex_fixed_boundary_core_completion_audit.md`](hc7_two_vertex_fixed_boundary_core_completion_audit.md).
This theorem
eliminates the two-vertex zero-slack outcome of the planar fixed-boundary
critical-core argument in the balanced order-eight configuration.  It does
not eliminate the triangular or positive-slack cores and does not prove
`HC_7`.

## 1. A boundary-endpoint selection lemma

### Lemma 1.1

Let `R` be a three-element set, and let `e,f` be disjoint two-element
sets.  Suppose that every member of `R` is adjacent to at least one member
of `e` and to at least one member of `f`.  Let `A` be a connected subgraph
which

1. has a neighbour in each of `e` and `f`;
2. has a neighbour at all but at most two vertices of
   `R union e union f`; and
3. misses at least one vertex of `R`.

Then there is a set `Z subseteq e union f` such that

1. `|Z cap e|<=1` and `|Z cap f|<=1`;
2. every member of `Z` has a neighbour in `A`; and
3. for every `r in R` missed by `A`, some member of `Z` is adjacent to
   `r`.

### Proof

Put

\[
             M=\{r\in R:N(r)\cap V(A)=\varnothing\}.
\]

By hypothesis, `1<=|M|<=2`.

If `|M|=2`, then the only two vertices of `R union e union f` missed by
`A` are the two members of `M`.  Hence `A` has a neighbour at all four
vertices of `e union f`.  Assign one member of `M` to `e` and the other
to `f`.  Collective adjacency supplies an endpoint of each assigned edge
adjacent to its assigned member of `M`; take those two endpoints for `Z`.

Suppose `M={r}`.  Since `A` misses at most two vertices of
`R union e union f`, at most one endpoint in `e union f` has no neighbour
in `A`.  Each of the two disjoint edges has an endpoint adjacent to `r`.
Those two candidate endpoints are distinct, so at least one of them has a
neighbour in `A`.  Taking that one endpoint for `Z` proves the lemma.
\(\square\)

## 2. Explicit seven-branch-set completion

### Theorem 2.1

Let `G` contain an eight-vertex separator

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\]

and suppose the following hold.

1. `R` is a clique.
2. `e` and `f` are vertex-disjoint anticomplete edges, each collectively
   adjacent to every member of `R`.
3. `G-S` has two connected components `C,D`, and `D` is adjacent to every
   literal vertex of `S`.
4. The component `C` contains adjacent vertices `ell_e,ell_f`.  Put

   \[
                         A=C-\{\ell_e,\ell_f\}.
   \]

   The graph `A` is connected, both displayed vertices have a neighbour
   in `A`, and `A` has a neighbour at `x`.
5. Both `ell_e,ell_f` are adjacent to every member of `R`;
   `ell_e` is adjacent to both endpoints of `f`; and `ell_f` is adjacent
   to both endpoints of `e`.
6. Among the eight literal vertices of `S`, the connected graph `A`
   misses one or two, at least one of which belongs to `R`.  It has a
   neighbour in each of `e` and `f`.

Then `G` contains a `K_7` minor.

### Proof

Apply Lemma 1.1 to `A`, using the collective adjacencies in item 2.  Its
hypothesis on the number of missed vertices follows from item 6 together
with the fact that `A` meets `x`: among `R union V(e) union V(f)`, it
still misses at most two vertices.  Obtain a set

\[
                         Z\subseteq V(e)\cup V(f)       \tag{2.1}
\]

with the three conclusions of the lemma.

Consider the following seven vertex sets:

\[
 \{\ell_e\},\quad \{\ell_f\},\quad
 V(A)\cup Z,\quad
 V(D)\cup\bigl((S-R)-Z\bigr),\quad
 \{r\}\quad(r\in R).                                 \tag{2.2}
\]

They are pairwise disjoint.  The `A`-set is connected because every
vertex of `Z` has a neighbour in the connected graph `A`.  The `D`-set
is connected because `D` is connected and adjacent to every boundary
vertex added to it.  The other sets are singletons.

We verify all adjacencies.  The two leaf singletons are adjacent to one
another, to the `A`-set, and to each singleton from `R`.  Since (2.1)
uses at most one endpoint of each of `e,f`, the `D`-set retains at least
one endpoint of each edge.  Item 5 therefore joins `ell_e` to the
`D`-set through the retained endpoint of `f`, and joins `ell_f` to it
through the retained endpoint of `e`.

The vertex `x` belongs to the `D`-set, while `A` has a neighbour at `x`,
so the two nonsingleton sets are adjacent.  The `D`-set is adjacent to
every singleton from `R` because the component `D` is boundary-full.  If
`A` meets a vertex `r in R`, then the `A`-set is directly adjacent to
`{r}`.  Otherwise Lemma 1.1 supplies a vertex of `Z` adjacent to `r`.
Finally, the three singleton sets from `R` are pairwise adjacent.

Thus the seven sets in (2.2) are pairwise adjacent connected branch sets,
and they form a `K_7`-minor model in `G`.  \(\square\)

## 3. Consequence for the balanced order-eight branch

### Corollary 3.1

In the balanced order-eight configuration with no `K_7` minor and no
earlier order-seven-separation outcome, the nonrepairable leaf-side
fixed-boundary critical core cannot consist only of the edge
`ell_e ell_f`.

### Proof

The promoted fixed-boundary theorem says that a two-vertex core gives
identical singleton lists at the two leaves.  Consequently each leaf sees
all five alternate boundary colours.  Since the distinguished boundary
vertex `x` misses both leaves and each leaf is anticomplete to its
same-index defect edge, the two colours absent from the original
five-clique occur on the two endpoints of the opposite defect edge.
Hence `ell_e` is adjacent to both endpoints of `f` and `ell_f` to both
endpoints of `e`.

All other hypotheses of Theorem 2.1 are exactly the promoted connected
leaf-side conclusions: `A` is connected, both leaves and `x` meet it, it
contacts both defect edges, and it misses one or two boundary vertices
including a member of `R`.  The theorem gives a `K_7` minor, contrary to
the surviving branch.  \(\square\)

## 4. Exact remaining zero-slack case

This closes the two-vertex critical core for hosts of arbitrary order.  In
the zero-slack branch the only uneliminated core is therefore the triangle
on `ell_e ell_f` and the third vertex of the bounded face incident with
that outer web edge.  The argument above uses complete cross-index
endpoint contact, which is special to the singleton-list core; it does not
apply when the common lists have order two.
