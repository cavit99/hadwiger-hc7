# Seven terminals root a cycle or a `K_{3,4}`

## Status and scope

**Status:** proved and independently audited **GREEN** in
[`hc7_seven_terminal_rooted_cycle_or_biclique_audit.md`](hc7_seven_terminal_rooted_cycle_or_biclique_audit.md).

This theorem is independent of `HC_7`.  It strengthens the bounded
terminal-kernel theorem at seven roots.  Its published inputs are Wu's
contractible-edge theorem, already stated and audited in
[`hc7_five_terminal_rooted_fan.md`](hc7_five_terminal_rooted_fan.md), and
Dirac's standard circumference bound that a `k`-connected `n`-vertex graph
has a cycle of order at least `min{2k,n}`.

For a seven-set `T`, a **`T`-rooted carrier** has seven pairwise disjoint
connected bags, one containing each literal member of `T`.  An edge of the
carrier means an actual adjacency between the corresponding bags.  It need
not be an edge between the two terminal vertices themselves.

## 1. The seven-vertex base

### Lemma 1.1

Every simple three-connected graph on seven vertices contains either a
spanning cycle `C_7` or a spanning `K_{3,4}`.

### Proof

The standard circumference theorem for `k`-connected graphs gives a cycle
of order at least

```text
min{2k,n}=6.
```

If the graph is Hamiltonian, the first outcome holds.  Otherwise let

```text
C=c_0c_1...c_5c_0
```

be a six-cycle and let `x` be the remaining vertex.  Minimum degree three
gives at least three neighbours of `x` on `C`.  Two consecutive neighbours
would permit `x` to be inserted into `C`, producing a Hamilton cycle.
Hence the neighbours form the unique independent three-set of `C`, after
renumbering

```text
N(x) cap V(C)={c_0,c_2,c_4}.
```

Each of `c_1,c_3,c_5` has its two cycle neighbours and is nonadjacent to
`x`.  If two of these odd-indexed vertices are adjacent, rotation gives an
edge `c_1c_3`, and

```text
c_0 c_1 c_3 c_2 x c_4 c_5 c_0
```

is a Hamilton cycle.  We may therefore assume that no two odd-indexed
vertices are adjacent.  Minimum degree now forces the three remaining
cross-edges

```text
c_1c_4, c_3c_0, c_5c_2.
```

Together with the six cycle edges and the three edges from `x`, these are
all twelve edges of a spanning `K_{3,4}` with bipartition

```text
{c_0,c_2,c_4} | {x,c_1,c_3,c_5}.
```

This proves the lemma. \(\square\)

## 2. The eight-vertex irreducible base

We first record the elementary contraction criterion used below.

### Lemma 2.1

Let `M` be simple and three-connected, let `v x` be an edge, and put
`H=M-v`.  If `H-x` is two-connected, then `v x` is contractible.

### Proof

Let `z` be the vertex obtained by contracting `v x`, followed by the usual
simplification of parallel edges.  A set of at most two vertices of the
quotient which avoids `z` cannot disconnect it: before contraction the
same deletion leaves the three-connected graph `M` connected, and
contraction preserves connectedness.  Deleting `z`, and possibly one
further vertex `y`, leaves respectively

```text
H-x, or H-{x,y},
```

which is connected because `H-x` is two-connected.  The quotient is
therefore three-connected, so `v x` is contractible. \(\square\)

### Lemma 2.2

Let `M` be a simple three-connected graph on eight vertices and let `v` be
incident with no contractible edge.  Then `M-v` has a Hamilton cycle.

### Proof

Put `H=M-v`.  The graph `H` is two-connected.  Wu's theorem applied to
`v` supplies at least four degree-three neighbours of `v`; after deleting
`v`, each has degree two in `H`.  Thus, with

```text
D={u in V(H): d_H(u)=2},   B=V(H)-D,
```

we have `|D|>=4` and hence `|B|<=3`.  Since `H` is two-connected, every
member of `B` has degree at least three.

Assume for a contradiction that `H` is not Hamiltonian.  The cases
`|B|=0,1` are immediate.  If `B` is empty, `H` is a connected two-regular
graph and hence is `C_7`.  If `B={b}`, then `H-b` is connected and consists
of one path whose ends both attach to `b`; consequently `H` is again a
cycle and `b` has degree two, contrary to `b in B`.

Suppose `|B|` is two or three.  Every component of `H[D]` is a path.  Its
two ends attach to distinct members of `B`: attachment twice to the same
member would make that member a cutvertex of `H`.  Suppress each such path
to one edge, retaining every direct edge within `B`.  This gives a
loopless multigraph `K` on `B`.  Call an edge **long** when it represents a
component of `H[D]`, and give it weight equal to the number of suppressed
vertices.  The long-edge weights sum to `|D|`.  Simplicity of `H` permits
at most one direct edge between a fixed pair of vertices of `B`.

First let `B={a,b}`.  All edges of `K` are parallel `a b` edges, and there
are at least three because `a,b` have degree at least three.  If there were
at most two long edges, the two long paths (or one long path and a direct
edge) would form a Hamilton cycle of `H`.  Thus there are at least three
long edges.  Their positive weights sum to five, so one has weight one;
write its unique internal vertex as `x`.  Deleting `x` leaves at least two
internally disjoint `a-b` routes, so `H-x` is two-connected.

The graph `M-{a,b}` is connected.  Since `x` has only `a,b` as neighbours
in `H`, this forces the literal edge `v x`.  Lemma 2.1 makes `v x`
contractible, a contradiction.

Now let `B={a,b,c}`.  Suppression preserves cutvertices, so the underlying
simple graph of `K` is the triangle on `a,b,c`.  Here `|D|=4`.  If there is
at most one long edge between each pair of vertices of `B`, choose that
long edge when it exists and otherwise choose the available direct edge.
The resulting triangle in `K` contains every long edge and lifts to a
Hamilton cycle of `H`.  Non-Hamiltonicity therefore forces two long edges
with the same ends, say `a,b`.

At least one of these two long edges has weight one.  Otherwise their
weights use all four vertices of `D`, so the only `a-c` and `b-c` edges are
the two possible direct edges.  This would give `d_K(c)=d_H(c)=2`, contrary
to `c in B`.  Let `x` be the sole internal vertex of a weight-one repeated
`a-b` edge.  Deleting it leaves the other `a-b` edge and leaves the
underlying triangle of `K` intact, so `H-x` is two-connected.  Connectivity
of `M-{a,b}` again forces `v x`, and Lemma 2.1 again says that this edge is
contractible.

Both remaining cases contradict the hypothesis at `v`.  Hence `H` is
Hamiltonian. \(\square\)

### Corollary 2.3

Let `T` be seven terminals in a `T`-irreducible simple three-connected
graph `M` of order eight.  Then the seven singleton terminal bags contain
a rooted `C_7`; the unique nonterminal is unused.

### Proof

Let `v` be the unique nonterminal.  Every edge incident with `v` is
`T`-legal, so terminal irreducibility says that none is contractible.
Lemma 2.2 gives a Hamilton cycle in `M-v=M[T]`. \(\square\)

## 3. Universal seven-root carrier theorem

### Theorem 3.1

Let `G` be a simple three-connected graph and let `T` be any seven
distinct vertices.  Then `G` contains either

1. a `T`-rooted `C_7` model; or
2. a `T`-rooted `K_{3,4}` model.

The bijection from the seven terminal labels to the carrier vertices is
not prescribed.

### Proof

Apply the audited terminal-legal contraction theorem to obtain a
three-connected `T`-irreducible rooted minor `M`.  Its kernel bound gives

```text
7 <= |V(M)| <= 7+floor(7/4)=8.
```

If `|V(M)|=7`, every vertex is a terminal and Lemma 1.1 supplies the
spanning carrier.  If `|V(M)|=8`, Corollary 2.3 supplies the terminal
cycle.  Expanding the terminal-legal contractions within their unique
rooted bags preserves terminal labels, bag disjointness, connectivity, and
every carrier adjacency.  The resulting bags give the asserted rooted
model in `G`. \(\square\)

## 4. Label-faithful use in the overlap-three cell

In the normalized arm-order-six, overlap-three rigid cell, write

```text
I={0,1,2},
T={3,4,5,6,7,p,q},
H=G-I.
```

Seven-connectivity of `G` makes `H` four-connected, so Theorem 3.1 applies
to the seven **literal** terminal labels.  A finite decoder may therefore
test all cyclic orders of `C_7` and all `3+4` bipartitions of `K_{3,4}`.
The lift must keep two edge layers separate:

* original edges among `I union T` enforce the nine irredundant six-support
  relations and any literal common-model test;
* carrier edges are added only in the final branch-set composition layer.

For a finite quotient certificate, replace every terminal label `t` by its
rooted carrier bag `B_t` and retain each member of `I` as a singleton bag.
An original edge incident with `t` remains available through the literal
root `t in B_t`; a carrier edge is available through an actual edge between
the two corresponding rooted bags.  The carrier bags lie in `G-I`, are
pairwise disjoint, and contain exactly one prescribed terminal each.
Consequently every connected quotient bag and every quotient adjacency
lifts literally.

It is **not** legitimate to feed a carrier edge back into an irredundant
support relation, to treat it as an edge between the two terminal vertices,
or to assume a prescribed cyclic order or prescribed `K_{3,4}` side.  The
theorem supplies the bounded carrier list; whether every labelled carrier
placement closes the order-six overlap-three decoder is a separate finite
composition theorem.

## 5. Computational falsification

The dependency-free probe
[`../active/hc7_seven_terminal_kernel_dichotomy_probe.py`](../active/hc7_seven_terminal_kernel_dichotomy_probe.py)
checks the stronger carrier dichotomy for every three-connected graph of
orders seven and eight and every choice of seven terminals.  It reports no
counterexample.  Among the ten eight-vertex terminal-irreducible rooted
instances, every one has a Hamilton cycle on the seven terminal vertices,
as Lemma 2.2 proves.  The computation is evidence only and is not used in
the proof.
