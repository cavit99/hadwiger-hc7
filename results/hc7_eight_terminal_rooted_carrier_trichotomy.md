# Eight terminals root a cycle or one of two bipartite carriers

## Status and scope

**Status:** proved and independently audited **GREEN** in
[`hc7_eight_terminal_rooted_carrier_trichotomy_audit.md`](hc7_eight_terminal_rooted_carrier_trichotomy_audit.md).

This is a standard rooted-minor theorem for eight prescribed vertices in a
simple three-connected graph.  It is independent of `HC_7`.  Its published
inputs are:

* Wu's contractible-edge theorem, through the audited terminal-kernel theorem
  in [`hc7_five_terminal_rooted_fan.md`](hc7_five_terminal_rooted_fan.md);
* the Chvatal--Erdos Hamiltonicity theorem; and
* the Moon--Moser bipartite degree-sum theorem.

The theorem gives a small label-faithful carrier family.  It deliberately
forgets some contacts of the one- and two-nonterminal kernels.  In particular,
a bare rooted `C_8` does **not** by itself close the active order-six-arm,
overlap-one composition cell.  Any use there must either verify all three
carrier families against the exact support state or retain the stronger exact
kernel contacts.

## 1. The three carriers

Let `F_8` be the following eight-vertex graph.  Start with the complete
bipartite graph with parts

```text
L={a_0,a_1,a_2,a_3,a_4},       R={b_0,b_1,b_2},
```

delete the two independent edges `a_0b_0,a_1b_1`, and add the edge
`a_0a_1`.  Thus

```text
F_8 = K_{5,3}-{a_0b_0,a_1b_1}+a_0a_1.                 (1.1)
```

### Theorem 1.1 (eight-terminal carrier trichotomy)

Let `G` be a simple three-connected graph and let `T` be any eight distinct
labelled vertices.  Then `G` contains a `T`-rooted model of at least one of

```text
C_8,       K_{3,5},       F_8.                         (1.2)
```

The bijection between the eight terminal labels and the carrier vertices is
not prescribed.  Every bag contains exactly one member of `T`.

The complete labelled decoder family in (1.2) has

```text
8!/16 + binom(8,3) + 8!/12 = 2520+56+3360 = 5936       (1.3)
```

distinct edge masks.

## 2. The order-eight base

We use two standard Hamiltonicity theorems.

> **Chvatal--Erdos.**  If a graph `H` satisfies
> `kappa(H)>=alpha(H)`, then `H` is Hamiltonian.

> **Moon--Moser.**  Let `H` be balanced bipartite with parts of order `n`.
> If `d(x)+d(y)>=n+1` for every nonedge `xy` with ends in opposite parts,
> then `H` is Hamiltonian.

### Lemma 2.1

Every simple three-connected graph on eight vertices contains a spanning
copy of `C_8`, `K_{3,5}`, or `F_8`.

### Proof

Let `H` be such a graph.  If it is Hamiltonian, there is nothing to prove.
Otherwise Chvatal--Erdos gives `alpha(H)>=4`.  Minimum degree three rules out
an independent set of order at least six.

Suppose first that `H` has an independent five-set `I`.  Each member of `I`
has all its neighbours in the other three vertices, and minimum degree makes
it adjacent to all three.  These fifteen edges give a spanning `K_{3,5}`.

It remains that `alpha(H)=4`.  Fix an independent four-set `I` and put
`B=V(H)-I`.  Let `J` be the spanning bipartite graph consisting of the
`I`--`B` edges of `H`.  Every member of `I` has degree at least three in
`J`.  If every member of `B` has degree at least two in `J`, then every
opposite nonedge `ib` satisfies

```text
d_J(i)+d_J(b)>=3+2=5=|I|+1.
```

Moon--Moser gives a spanning `C_8` in `J`, a contradiction.  Hence some
`b_0 in B` has at most one neighbour in `I`.

If `b_0` has no neighbour in `I`, minimum degree makes it adjacent to all
three vertices of `R=B-{b_0}`.  Each member of `I` misses at most one member
of `B`, namely `b_0`, and therefore sees all of `R`.  The bipartition

```text
R | (I union {b_0})
```

gives a spanning `K_{3,5}`.

Suppose finally that `N_I(b_0)={i_0}`.  The other three members of `I` see
all of `R=B-{b_0}`.  Since `i_0b_0` is an edge and both endpoints have
degree at least three, each of `i_0,b_0` misses at most one member of `R`.
They cannot both miss the same `r in R`: deleting the other two members of
`R` would isolate the edge `i_0b_0` from the rest of `H`, contradicting
three-connectivity.

Consequently, across the bipartition

```text
L=I union {b_0},       R=B-{b_0},
```

all cross-edges are present except possibly two independent edges, one at
`i_0` and one at `b_0`, while `i_0b_0` is present inside `L`.  If fewer than
two cross-edges are absent, delete suitable extra cross-edges with distinct
ends in `R`.  The resulting spanning subgraph is exactly `F_8`.  \(\square\)

## 3. One nonterminal: the theta exception

The next lemma is the only new kernel calculation needed for eight roots.

### Lemma 3.1 (Hamilton remainder or `Theta_{3,3,3}`)

Let `M` be a simple three-connected graph on nine vertices and let `x` be
incident with no contractible edge.  Put `H=M-x`.  Then exactly one of the
following is available.

1. `H` has a Hamilton cycle.
2. There are distinct terminals `p,q` and six other terminals
   `u_i,w_i` (`i=1,2,3`) such that

   ```text
   H-{pq if present}
   = (p-u_1-w_1-q) union (p-u_2-w_2-q) union (p-u_3-w_3-q),   (3.1)
   ```

   the three displayed paths are internally disjoint, `pq` is optional,
   and

   ```text
   {u_1,w_1,u_2,w_2,u_3,w_3} subseteq N_M(x) subseteq V(H).  (3.2)
   ```

In outcome 2, absorbing `x` into **any** one of the six internal terminals
gives a terminal-rooted `C_8`.

### Proof

The graph `H` is two-connected.  Let

```text
D={z in V(H):d_H(z)=2},       B=V(H)-D.
```

Wu's theorem gives at least four degree-three neighbours of `x`; all lie in
`D`.  Thus `|D|>=4` and `|B|<=4`.

If `|B|=0`, then `H` is a cycle.  The case `|B|=1` is impossible: deleting
the sole member of `B` leaves one path through all vertices of `D`, whose
two ends both return to that member, forcing it also to have degree two.
Thus assume `|B|>=2`.  Every component of `H[D]` is then a path whose two
ends attach to distinct members of `B`.  Suppress each such path to a **long**
edge and give it weight equal to its number of internal vertices.  Retain
each literal edge inside `B` as a weight-zero edge.  The result is a loopless
two-connected multigraph `K` on `B` with minimum degree at least three.
There is at most one zero edge on each pair, and the positive weights sum to

```text
|D|=8-|B|.                                               (3.3)
```

The graph `H` is Hamiltonian exactly when `K` has a spanning cycle containing
every positive edge.

We first record the contraction escape used below.  We use the exact
criterion that, for `xz in E(M)`, contraction of `xz` preserves
three-connectivity if and only if `M-{x,z}=H-z` is two-connected.  Suppose a positive edge
`e=ab` has weight one, with unique internal vertex `z`, and `K-e` is
two-connected.  Then `H-z` is two-connected.  Moreover `M-{a,b}` is
connected, while both `H`-neighbours of `z` have been deleted, so `xz` must
be an edge.  The exact contraction criterion says that `xz` is contractible,
a contradiction.  Hence

```text
no weight-one positive edge e has K-e two-connected.       (3.4)
```

Let `|B|=2`.  Then `K` consists of parallel edges, and a cycle of this
two-vertex multigraph means two distinct parallel routes.  If at most two
routes are positive, two routes give a Hamilton cycle of `H`.  Otherwise deleting any positive
edge leaves at least two routes, so (3.4) makes every positive weight at
least two.  Their weights sum to six.  The only non-Hamiltonian possibility
is therefore three positive edges of weight two, with one optional zero
edge.  This is (3.1).

Let `|B|=3`.  The underlying simple graph of `K` is a triangle.  Failure of
a positive-spanning triangle requires two positive edges on the same pair.
Each is removable while preserving two-connectivity, so each has weight at
least two by (3.4).  If their common ends are `a,b`, the third branch vertex
`c` has only the two underlying pairs `ca,cb`.  Its degree is at least three,
so one of those pairs has a second route.  At most one route on a pair is a
zero edge; hence that parallel class contains a positive edge.  By (3.3),
the two repeated `ab` edges have weight two and this extra positive edge has
weight one.  It has a parallel route, so its deletion leaves `K`
two-connected, contrary to (3.4).

It remains that `|B|=4` and the positive weights sum to four.  The underlying
simple graph of `K` is `C_4`, `K_4-e`, or `K_4`.

* For `C_4`, every vertex must be incident with a parallel class, because
  its simple degree is two but its degree in `K` is at least three.  Every
  parallel class contains a positive route, and deleting such a route keeps
  the underlying `C_4`; it is therefore removable.  Select positive routes
  from parallel classes so that their ends cover all four vertices.  By
  (3.4) each has weight at least two, and by (3.3) there are exactly two,
  both of weight two, on a matching.  No other positive route remains.  The
  four-cycle using those two routes contains every positive edge.
* For `K_4-e`, each of the two nonadjacent degree-two tips must be incident
  with a parallel class.  Choose a positive route from each class.  These
  two routes are removable, lie on distinct pairs, and hence have weight at
  least two.  They exhaust (3.3), so there are no other positive routes.  A
  spanning four-cycle can be chosen through both selected pairs (whether
  they meet the same or different degree-three vertex).
* For `K_4`, every positive route is removable: deleting a sole route leaves
  `K_4-e`, while deleting a parallel route leaves the same underlying
  `K_4`.  Hence there are at most two positive edges.  Two on distinct pairs
  lie on a common spanning four-cycle.  The sole non-Hamiltonian residue is
  two parallel edges of weight two on one pair `p,q`, with the other five
  pairs represented by zero edges and `pq` itself optionally represented by
  a zero edge.

In that last residue all four members of `D` are Wu neighbours of `x`, so
`x` sees all of them.  Deleting `p,q` separates `x` and the two subdivided
`p`--`q` paths from the other two branch vertices unless `x` sees one of
those branch vertices, say `r`.  But `H-r` is a subdivision of a theta graph
and is two-connected.  The edge `xr` is therefore contractible, a final
contradiction.

We have proved that the only non-Hamiltonian remainder is (3.1).  On one
path `p-u_i-w_i-q`, deletion of `{p,w_i}` forces `xu_i`, and deletion of
`{u_i,q}` forces `xw_i`, by three-connectivity.  This proves (3.2).

For the owner `u_1`, put `Z={x,u_1}`.  The cycle of rooted bags

```text
Z,w_1,q,w_2,u_2,p,u_3,w_3,Z                         (3.5)
```

is a `C_8`.  For the owner `w_1`, use

```text
Z,u_1,p,u_2,w_2,q,w_3,u_3,Z.                         (3.6)
```

Relabelling the three paths proves the assertion for every internal owner.
\(\square\)

## 4. Two nonterminals

### Lemma 4.1

Let `T` be eight terminals in a `T`-irreducible simple three-connected graph
`M` of order ten.  Then `M[T]` is a spanning `C_8`.

### Proof

Let the two nonterminals be `x,y`.  The disjoint Wu charge sets at `x,y`
each have order at least four and lie in `T`; hence they partition `T` into
two four-sets.  Every terminal has degree three in `M`, with one incident
edge to its charging nonterminal and two incident terminal--terminal edges.
Therefore `M[T]` is two-regular.  Three-connectivity says that
`M-{x,y}=M[T]` is connected.  It is consequently `C_8`.  \(\square\)

The stronger exact residue is a cycle coloured `AABB AABB`, with `x,y`
joined to the complementary colour classes and not to each other, but that
extra classification is not needed for Theorem 1.1.

## 5. Proof of the carrier trichotomy and safe quantifiers

Apply the audited terminal-legal contraction theorem to `G,T`.  It returns a
`T`-irreducible simple three-connected rooted minor `M` with

```text
8 <= |M| <= 8+floor(8/4)=10.                            (5.1)
```

If `|M|=8`, Lemma 2.1 supplies one of the three spanning carriers.  If
`|M|=9`, Lemma 3.1 supplies a terminal cycle directly or after merging the
unique nonterminal bag into any one of six literal internal owners.  If
`|M|=10`, Lemma 4.1 supplies the terminal cycle and both nonterminals are
unused.

Expanding every terminal-legal contraction preserves the eight literal
labels, disjointness, bag connectivity, and all carrier adjacencies.  In the
theta branch, the nonterminal bag is merged into exactly one adjacent
terminal bag before expansion.  Thus every final bag contains exactly one
literal terminal.

For a labelled composition decoder the safe quantifier is simply

```text
for every one of the 5936 labelled carrier masks.                (5.2)
```

No owner quantifier survives in (5.2), because every exceptional owner
already produces one of the labelled `C_8` masks.  This is weaker than an
exact-kernel decoder: if a support state fails on a bare `C_8`, the discarded
contacts of the nonterminal bag may still be essential and must be restored
from the exact kernel.

## 6. Published inputs and verification boundary

The Hamiltonicity inputs are:

* V. Chvatal and P. Erdos, *A note on Hamiltonian circuits*, Discrete
  Mathematics **2** (1972), 111--113,
  [doi:10.1016/0012-365X(72)90079-9](https://doi.org/10.1016/0012-365X(72)90079-9);
* J. Moon and L. Moser, *On Hamiltonian bipartite graphs*, Israel Journal of
  Mathematics **1** (1963), 163--165,
  [doi:10.1007/BF02759704](https://doi.org/10.1007/BF02759704).

Wu's theorem and the terminal-kernel induction are stated and audited in
[`hc7_five_terminal_rooted_fan.md`](hc7_five_terminal_rooted_fan.md) and its
audit.

The deterministic falsifier
[`../active/hc7_eight_terminal_rooted_carrier_verify.py`](../active/hc7_eight_terminal_rooted_carrier_verify.py)
checks all `5936` labelled carriers, every simple three-connected graph on
eight vertices generated by `geng`, and every rooted order-nine irreducible
kernel.  It is evidence for the hand proof, not a premise of it.
