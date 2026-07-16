# Completion when deleting the two clique leaves disconnects their shore

**Status:** written proof with a separate GREEN internal audit in
[`hc7_star_order_eight_disconnected_leaf_side_completion_audit.md`](hc7_star_order_eight_disconnected_leaf_side_completion_audit.md).
This theorem closes an unbounded subfamily of the exact order-eight star
configuration.  It does not close the remaining one-component linkage
obstruction or prove `HC_7`.

## Theorem 1

Let `G` be a seven-connected graph.  Suppose

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\]

and assume:

1. `R` is a clique;
2. `e,f` are vertex-disjoint anticomplete edges, each collectively
   adjacent to every vertex of `R`;
3. `G-S` has distinct connected components `C,D`, each adjacent to every
   vertex of `S`;
4. `C` contains adjacent vertices `ell_e,ell_f`, each adjacent to every
   vertex of `R`;
5. `e` is anticomplete to `ell_e` and has a neighbour at `ell_f`, while
   `f` is anticomplete to `ell_f` and has a neighbour at `ell_e`; and
6. `C-{ell_e,ell_f}` has at least two components.

Then `G` contains a `K_7` minor or has an actual order-seven separation.

The same conclusion holds, without hypothesis 6, if every edge from `x`
to `C` has its end in `{ell_e,ell_f}`.

## Proof

Assume that `G` has no `K_7` minor and no actual order-seven separation.
We derive a contradiction.

### Step 1: contacts of the components after deleting the leaves

Let `A` be a component of `C-{ell_e,ell_f}`, and let `t(A)` be the number
of the two leaves adjacent to `A`.  Since `C` is connected,
`t(A) in {1,2}`.  Moreover,

\[
 N_G(A)=\bigl(N_G(A)\cap S\bigr)
       \mathbin{\dot\cup}
       \bigl(N_G(A)\cap\{\ell_e,\ell_f\}\bigr).       \tag{1.1}
\]

The set in (1.1) separates `A` from the nonempty component `D`.  Its order
is at least eight: an order at most six contradicts seven-connectivity,
and order seven is one of the theorem's conclusions.  Hence

\[
                         |N_G(A)\cap S|\ge 8-t(A).     \tag{1.2}
\]

If `A` were adjacent to every vertex of `R union {x}`, then (1.2) would
make it adjacent to at least one of the two edges `e,f`; call one such
edge `g`, and call the other `h`.  The seven sets

\[
 \{r\}\ (r\in R),\qquad
 V(g),\qquad
 V(h)\cup\{\ell_e,\ell_f\},\qquad
 A\cup\{x\},\qquad D                              \tag{1.3}
\]

would be pairwise disjoint connected branch sets of a `K_7` minor.  Indeed,
the edge `h` is adjacent to the leaf it does not omit, the two leaves are
adjacent, and `A` is adjacent to at least one leaf.  The set `A union {x}`
is adjacent to `g`, every singleton in `R`, the leaf-containing set, and
`D` through `x`.  Fullness of `D` and the stated collective contacts give
all remaining adjacencies.  This is impossible.  Therefore every component
`A` misses at least one vertex of `R union {x}`.

It follows from (1.2) that every component `A` contacts both edge sets
`V(e)` and `V(f)`.  If `t(A)=1`, then (1.2) gives at least seven boundary
neighbours, and the missed vertex in `R union {x}` is its only missed
boundary vertex.  If `t(A)=2`, it has at least six boundary neighbours and
misses at most two boundary vertices, one of them in `R union {x}`; it
therefore cannot miss both endpoints of either `e` or `f`.

### Step 2: a leaf without an interior neighbour gives the separator

Suppose, for example, that `ell_e` has no neighbour in
`C-{ell_e,ell_f}`.  Its neighbours then lie among

\[
             \{\ell_f\}\cup R\cup V(f)\cup\{x\},
\]

because `ell_e` is anticomplete to `e` and there are no edges from `C` to
any other component of `G-S`.  Thus `d_G(ell_e)<=7`.  Seven-connectivity
forces equality, and `N_G(ell_e)` separates the singleton vertex `ell_e`
from `D`.  It is an actual order-seven separation, contrary to our standing
assumption.  The same argument applies to `ell_f`.  Hence each leaf has a
neighbour in `C-{ell_e,ell_f}`.

### Step 3: an interior `x`-contact supplies the two paths

Suppose `x` has a neighbour in a component `A` of
`C-{ell_e,ell_f}`.  We use the audited
[split-edge completion](../results/hc7_star_order_eight_split_edge_completion.md).

If `A` is adjacent to `ell_f` but not `ell_e`, choose inside
`A union {ell_f}` a connected subgraph `P` containing `ell_f` and a
neighbour of `x`.  By Step 2 some component `B` is adjacent to `ell_e`;
it is different from `A`.  Step 1 says that `B` contacts `V(e)`, so choose
inside `B union {ell_e}` a connected subgraph `Q` containing `ell_e` and
a vertex adjacent to `V(e)`.  The subgraphs `P,Q` are vertex-disjoint, and
the split-edge completion gives a `K_7` minor.

The case in which `A` is adjacent to `ell_e` but not `ell_f` is symmetric,
using `f` in place of `e`.  Finally suppose `A` is adjacent to both leaves.
Choose any other component `B`, which exists by hypothesis 6.  If `B` is
adjacent to `ell_e`, use `A` for the `ell_f`--`x` subgraph and `B` for the
`ell_e`--`e` subgraph.  If not, then `B` is adjacent to `ell_f`; use the
symmetric pair, with `A` for `ell_e`--`x` and `B` for `ell_f`--`f`.
Again the two subgraphs are disjoint and the promoted completion gives a
`K_7` minor.

This contradiction proves that, under hypothesis 6, `x` has no neighbour
in `C-{ell_e,ell_f}`.

### Step 4: contacts of `x` only at the leaves also complete the model

The boundary-fullness of `C` at `x` now makes `x` adjacent to at least one
leaf.  Suppose `x ell_f` is an edge.  Take `P={ell_f}`.  By Step 2, choose
a component `B` adjacent to `ell_e`; by Step 1 it contacts `V(e)`, so a
connected subgraph `Q` in `B union {ell_e}` joins `ell_e` to such a
contact.  The two subgraphs `P,Q` are disjoint and satisfy the split-edge
completion.  Hence `G` contains a `K_7` minor.  If instead `x` is adjacent
to `ell_e`, use the symmetric construction.

This contradiction completes the proof under hypothesis 6.  The same
Step 4 proves the final assertion directly when all `x`--`C` edges end at
the two leaves: hypothesis 6 was not used there. \(\square\)

## Corollary 2 (exact remaining clique-side obstruction)

In a `K_7`-minor-free exact order-eight configuration with no actual
order-seven separation,

1. `C-{ell_e,ell_f}` is connected;
2. `x` has a neighbour in this connected graph;
3. both leaves have a neighbour in it;
4. it contacts both `V(e)` and `V(f)`; and
5. it misses one or two boundary vertices, including at least one vertex
   of `R`.

The only remaining local obstruction on the clique side is therefore the
failure, inside this one connected near-full graph, of both labelled
two-path linkages from the split-edge completion.

### Proof

Items 1--3 are Theorem 1 and Step 2.  Apply (1.2) to the unique component,
which is adjacent to both leaves: it has at least six boundary neighbours.
The branch-set construction (1.3) says that it misses a vertex of
`R union {x}`; item 2 excludes `x`, so it misses a vertex of `R`.  It
therefore has at most seven boundary neighbours and misses one or two
vertices.  Step 1 gives item 4.  The final statement is precisely the
contrapositive of the promoted split-edge completion and its symmetric
version. \(\square\)
