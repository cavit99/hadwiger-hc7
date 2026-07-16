# Small boundary models lift through two full shores

**Status:** proved and independently audited.

This note isolates the part of an exact-seven handoff that is genuinely
state-free.  It gives a literal shore anchor for every preserved small
`K_5` model and explains why a coherent `K_2 join C_5` boundary frame
cannot drift between two full shores.

## 1. Uniform lifting lemma

### Theorem 1.1 (proper-boundary model lift)

Let `r>=1`.  Let `G` contain pairwise disjoint vertex sets `A,S,B` such
that

1. `A` and `B` are nonempty and connected;
2. there is no edge between `A` and `B`; and
3. every vertex of `S` has a neighbour in each of `A` and `B`.

If `G[S]` contains a `K_r` model whose support is a proper subset of `S`,
then `G` contains a `K_{r+2}` minor.

### Proof

Let `D_1,...,D_r` be the branch sets of the model and put

\[
                         W=\bigcup_{i=1}^r V(D_i).
\]

Choose `s in S-W`.  The following `r+2` sets are pairwise disjoint:

\[
                       D_1,\ldots,D_r,\quad A\cup\{s\},\quad B.       \tag{1.1}
\]

They are connected: this is part of the model for the first `r` sets,
it is assumed for `B`, and `s` has a neighbour in `A`, so `A union {s}`
is connected.  The first `r` sets are pairwise adjacent.  Each `D_i`
contains a literal vertex of `S`; fullness makes both `A` and `B`
adjacent to `D_i`.  Finally `s` has a neighbour in `B`, giving an edge
between the last two sets in (1.1).  Thus (1.1) is a literal
`K_{r+2}` model.  \(\square\)

## 2. The exact-seven consequence

### Corollary 2.1 (no small model in the boundary)

Let `G` be `K_7`-minor-free, and let `S` be a seven-set separating two
nonempty connected `S`-full shores.  Then `G[S]` contains no `K_5` model
supported on at most six vertices.

In particular, if a support-at-most-six `K_5` model is contained in one
closed shore of this separation, then its support meets that open shore.
Consequently the model chooses that shore uniquely; it cannot be assigned
to the opposite closed shore merely by relabelling the separation.

### Proof

The first assertion is Theorem 1.1 with `r=5`, because a support of order
at most six is a proper subset of the seven-set `S`.  For the second,
write the closed shores as `A union S` and `B union S`.  If the model is
contained in `A union S` but not in `S`, its support meets `A`.  Since `A`
is disjoint from `B union S`, it is not contained in the opposite closed
shore.  The other orientation is symmetric.
\(\square\)

This is an orientation theorem, not yet a recursive theorem.  It does not
say that the oriented shore is smaller than a previously selected shore,
nor that a colouring state survives the handoff.

## 3. Rigidity of the cyclic two-apex frame

### Corollary 3.1 (`K_2 join C_5` is edge-maximal on a full boundary)

Under the hypotheses of Corollary 2.1, suppose `G[S]` contains a spanning
subgraph

\[
                              H_0\cong K_2\mathbin\vee C_5.
\]

Then `G[S]=H_0`.  In particular the two vertices of the `K_2` are the
unique spanning-frame apex pair.  Two `K_2 join C_5` frames supported on
the same literal boundary therefore have exactly the same edge set and
the same apex pair.

### Proof

The only nonedges of `H_0` join nonconsecutive vertices of its five-cycle.
Adding any one of them creates a triangle on three cycle vertices.  Those
three vertices together with the two universal adjacent vertices induce
a literal `K_5` on five vertices.  Corollary 2.1 forbids this.  Hence no
edge can be added to `H_0` inside `S`, proving `G[S]=H_0`.

Any second spanning `K_2 join C_5` subgraph has sixteen edges and is a
subgraph of the sixteen-edge graph `G[S]=H_0`; hence it has the same edge
set.  Its apices are the two degree-six vertices, so the apex pair is
intrinsic.  \(\square\)

## 4. Trust boundary

Theorem 1.1 is uniform in `r` and uses only literal branch sets and two
full connected shores.  No colouring, criticality or planarity is used.

The theorem does **not** prove that two small models anchored in opposite
shores force `K_7`, and it does not make an unranked exact-seven handoff
recursive.  Its exact contribution is narrower and indispensable:

* a named support-at-most-six `K_5` model already known to lie in one
  closed shore cannot disappear into the adhesion;
* an unordered support-count rank is unnecessary for orienting the cell;
  an actual named model supplies the orientation; and
* the standard cyclic two-apex obstruction has one coherent literal apex
  pair rather than independently drifting local pairs.
