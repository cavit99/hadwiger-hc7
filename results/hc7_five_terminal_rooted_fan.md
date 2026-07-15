# Five terminals in a three-connected graph root a triangulated pentagon

## Status

Proved and independently audited in
[`hc7_five_terminal_rooted_fan_audit.md`](hc7_five_terminal_rooted_fan_audit.md),
using one published theorem of Wu on contractible edges in three-connected
graphs.  The overlap-four corollary also uses the already audited
five-terminal cycle decoder and its three-rooted composition outcome.

The theorem is independent of the `HC_7` criticality hypotheses.  In
particular, it does not assume that the five terminals lie on a common cycle
and does not first choose a rooted `K_4`.

## 1. Definitions and published input

Write

```text
F_5 = K_1 join P_4.
```

Equivalently, `F_5` is the unique maximal outerplanar graph on five vertices:
it consists of a five-cycle together with two noncrossing chords having a
common end.

For a five-set `T` in a graph `G`, a **`T`-rooted `F_5` model** is a family of
five pairwise disjoint connected bags, one containing each member of `T`,
whose bag-adjacency graph contains a copy of `F_5`.  The bijection between the
terminals and the vertices of `F_5` is not prescribed.

An edge of a simple three-connected graph is **contractible** if contracting
it and simplifying parallel edges leaves a simple three-connected graph.  An
edge is **`T`-legal** if it does not have two ends in `T`; contracting such an
edge does not identify two terminals.

A simple three-connected graph containing `T` is **`T`-irreducible** if it
has no `T`-legal contractible edge.

We use the following result.

> **Wu's contractible-edge theorem.**  Let `G` be a simple three-connected
> graph on at least five vertices.  If a vertex `v` is incident with no
> contractible edge, then `v` has at least four neighbours of degree three,
> each of which is incident with exactly two contractible edges.

This is proved in H. Wu, *Contractible Elements in Graphs and Matroids*,
Combinatorics, Probability and Computing **12** (2003), 457--465,
[doi:10.1017/S0963548302005497](https://doi.org/10.1017/S0963548302005497).

## 2. Bounded terminal kernel and the five-root fan

### Theorem 2.1

Let `G` be a simple three-connected graph, let `T` be a set of `k>=4`
vertices, and keep every vertex of `T` labelled.  Then `G` has a
three-connected `T`-rooted minor `M`, obtained using only `T`-legal edge
contractions, with the following properties:

1. `M` is `T`-irreducible;
2. `|V(M)-T| <= floor(k/4)`; and hence
3. `|V(M)| <= k+floor(k/4)`.

More precisely, for every `v in V(M)-T` there is a set `A_v subseteq T` of
at least four neighbours of `v` such that:

* every `x in A_v` has degree three in `M`;
* the other two edges incident with `x` are contractible edges with both
  ends in `T`; and
* the sets `A_v`, over all `v in V(M)-T`, are pairwise disjoint.

### Proof

Starting with `G`, repeatedly contract a `T`-legal contractible edge, keeping
the label of a terminal when the edge has one end in `T`.  Every intermediate
graph is simple and three-connected, the vertices of `T` remain distinct,
and the process terminates at a `T`-irreducible graph `M`.  Thus

```text
every contractible edge of M has both ends in T.                 (2.1)
```

If `M-T` is empty, all conclusions hold.  Otherwise `|V(M)|>=k+1>=5`, so
Wu's theorem applies.  Let `v` be a vertex outside `T`.  By (2.1), `v` is
incident with no contractible edge.  Wu's theorem supplies a set `A_v` of at
least four degree-three neighbours of `v`, each incident with exactly two
contractible edges.

Every member `x` of `A_v` belongs to `T`: each of the two contractible edges
incident with `x` has both ends in `T` by (2.1).  Moreover, the three edges
incident with `x` consist exactly of

```text
xv and two edges from x to T.                                  (2.2)
```

If `v,w` were two distinct nonterminals, then `A_v` and `A_w` would be
disjoint.  Indeed, a vertex in their intersection would have the two edges
to `v,w` in addition to its two incident contractible edges, contrary to its
degree being three.  The sets `A_v` are therefore pairwise disjoint subsets
of `T`, each of order at least four.  It follows that

```text
4|V(M)-T| <= sum_v |A_v| <= |T|=k.
```

This proves the bound and all the stated structural properties.  \(\square\)

The restriction `k>=4` is real.  For `k=3`, take `K_4` with three terminals:
it is terminal-irreducible with one nonterminal, whereas `floor(3/4)=0`.
For `k=4`, Wu is needed only when a nonterminal survives, in which case the
kernel has at least five vertices and the published hypothesis is satisfied.

### Corollary 2.2 (universal five-root fan)

Let `G` be a simple three-connected graph and let `T` be any five distinct
vertices of `G`.  Then `G` contains a `T`-rooted `F_5` model.

### Proof

Apply Theorem 2.1 with `k=5`.  It gives a three-connected `T`-rooted minor
`M` with at most one nonterminal.  It suffices to find the rooted fan in `M`,
because every branch model in `M` lifts through the legal contractions to
`G`.

If `V(M)=T`, then three-connectivity gives `delta(M)>=3`, so every vertex has
degree at most one in the complement of `M`.  The complement is therefore a
matching.  Since `|T|=5` is odd, some vertex `z` is incident with no
complementary edge and hence is universal in `M`.  The other four vertices
contain a spanning path: their induced graph is `K_4` with at most a matching
deleted.  The universal vertex `z` together with that path is a spanning
`F_5`.

Suppose now that `M-T={v}`.  Let `A` be the set of all neighbours `x` of `v`
which have the properties supplied by Wu's theorem.  By Theorem 2.1, `A` is
a subset of `T`, `|A|` is four or five, and (2.2) gives

```text
d_{M[T]}(x)=2 for every x in A.                                (2.3)
```

If `A=T`, then (2.3) says that `M[T]` is a simple two-regular graph on five
vertices.  It is therefore a five-cycle.  Also `v` is adjacent to every
member of `T`.

Now suppose `A=T-{y}`.  Put `epsilon=1` when `vy` is an edge and
`epsilon=0` otherwise.  Since `M` is three-connected,

```text
d_{M[T]}(y) >= 3-epsilon.
```

The degree sum in `M[T]`, together with (2.3), shows that
`8+d_{M[T]}(y)` is even.  Hence exactly one of the following occurs:

1. `epsilon=1` and `d_{M[T]}(y)=2`; or
2. `d_{M[T]}(y)=4`.

In the first case all five vertices have degree two in `M[T]`, so `M[T]` is
a five-cycle, and `v` is again adjacent to all of `T`.

Thus, in both five-cycle cases, choose any `x in A`.  The five bags

```text
{v,x}, and {t} for t in T-{x}
```

form a rooted `F_5`: the bag `{v,x}` is universal to the other four bags,
while deleting `x` from the five-cycle `M[T]` leaves a spanning four-vertex
path.

It remains to handle `d_{M[T]}(y)=4`.  Then `y` is adjacent to all four
vertices of `A`.  By (2.3), every vertex of `A` has exactly one further
neighbour in `A`; consequently `M[A]` is a perfect matching.  Label its two
edges

```text
xa and bc.
```

The bag `{v,x}` is adjacent to each of the singleton bags
`{a},{y},{b},{c}`: use `v` for `a,b,c` and the edge `xy` for `y`.  Those four
singleton bags contain the path

```text
a-y-b-c.
```

They and the universal bag `{v,x}` again form a rooted `F_5`.  This disposes
of the last residue.  \(\square\)

## 3. Overlap-four consequence

Use the normalized overlap-four cross-arm setup of
[`hc7_cross_arm_overlap_four_cycle_decoder.md`](hc7_cross_arm_overlap_four_cycle_decoder.md):

```text
I={0,1,2,3},       T={4,5,6,p,q},       H=G-I,
```

with the eleven irredundant support-six hypotheses used by that decoder.
Seven-connectivity of `G` implies that `H` is three-connected, since a cut
of order at most two in `H` would combine with `I` to give a cut of order at
most six in `G`.

### Corollary 3.1

Every seven-connected graph satisfying the normalized overlap-four
cross-arm hypotheses contains a literal `K_7` minor.

### Proof

Apply Corollary 2.2 to `H` and `T`.  Let the outer five-cycle of the resulting
rooted `F_5` model have cyclic order `pi`.  Feed those five rooted cycle bags
to the audited five-terminal cycle decoder.

For ten of the twelve cyclic orders, the decoder gives a literal `K_7` or
its common rooted-`K_4` outcome; the latter gives `K_7` by the audited
three-rooted composition theorem.

It remains to consider a crossed order.  Up to orientation and exchanging
`p,q`, write it as

```text
l_1, l_2, r, 6, s.
```

The crossed-frame certificate has the four fixed gate defects

```text
l_1 6,   l_1 r,   l_2 6,   l_2 s.                              (3.1)
```

The two chords of a triangulated pentagon have a common end, namely its
universal vertex.  Whichever of the five cyclic positions is universal, at
least one chord is a pair from (3.1):

| universal position | a chord in (3.1) |
|---|---|
| `l_1` | `l_1 r` (also `l_1 6`) |
| `l_2` | `l_2 6` (also `l_2 s`) |
| `r` | `r l_1` |
| `6` | `6 l_1` (also `6 l_2`) |
| `s` | `s l_2` |

That chord is a literal adjacency between two rooted exterior bags, not a
completion edge.  The crossed-frame decoder was exhaustively proved to be
edge-maximal at each of the four defects (3.1): supplying any one of them
produces a `K_7` model in every residual state.  Its branch-set lift replaces
terminal labels by the present rooted bags and therefore yields a literal
`K_7` model in `G`.  \(\square\)

## 4. Computational evidence (not a dependency)

Before the proof above was found, a dependency-free branch-set census tested
all simple unlabeled graphs through order nine.  At order nine it checked all
`80,890` three-connected graphs and all `10,192,140` choices of five
terminals; no counterexample occurred.  A separate scan for the induction
obstruction through order eight found only the six-vertex wheel with its five
rim vertices as terminals, which is exactly the five-cycle residue handled in
the proof.

These computations motivated the contractible-edge induction but are not
used in Theorem 2.1 or Corollary 3.1.
