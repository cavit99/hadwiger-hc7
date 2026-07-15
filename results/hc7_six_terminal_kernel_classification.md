# Six-terminal irreducible-kernel classification

## Status and scope

**Status:** proved and independently audited **GREEN** in
[`hc7_six_terminal_kernel_classification_audit.md`](hc7_six_terminal_kernel_classification_audit.md).
The only published inputs are Wu's contractible-edge theorem and Dirac's
standard circumference bound, both already used in the audited
terminal-kernel work.

This is a label-faithful rooted-minor theorem for any simple
three-connected graph.  It does not use `HC_7` criticality.

## 1. Statement

Let `T` be six prescribed vertices of a simple three-connected graph `G`.
Then `G` has a `T`-rooted `C_6` model.

More precisely, reduce `G` by terminal-legal contractible edges to a
`T`-irreducible three-connected rooted minor `M`.  The audited terminal
kernel theorem gives

```text
6 <= |V(M)| <= 6+floor(6/4)=7.
```

The irreducible kernel has the following exact form.

1. If `|M|=6`, then `V(M)=T`; the graph `M` is an arbitrary simple
   three-connected graph on the six terminals and has a spanning cycle.
2. If `|M|=7`, let `v` be its unique nonterminal.  There is a cyclic order

   ```text
   t_0,t_1,t_2,t_3,t_4,t_5
   ```

   of `T` such that either:

   * `M[T]` is that `C_6` and `v` is adjacent to all six terminals; or
   * `M[T]` is that `C_6` plus the opposite chord `t_0t_3`, while `v` is
     adjacent to each of `t_1,t_2,t_4,t_5` and to an arbitrary subset of
     `{t_0,t_3}`.

Thus the order-seven possibilities are a six-wheel, or one of the three
rooted types obtained from an oppositely chorded six-cycle according as the
hub sees neither, one, or both chord ends.  The terminal cycle itself avoids
the nonterminal.

## 2. Contraction criterion

We use the following elementary lemma.

### Lemma 2.1

Let `M` be simple and three-connected, let `vx` be an edge, and put
`H=M-v`.  If `H-x` is two-connected, then `vx` is contractible.

### Proof

Contract `vx` to `z` and simplify parallel edges.  Deleting at most two
vertices which avoid `z` cannot disconnect the quotient, because the same
deletion leaves `M` connected.  Deleting `z`, and possibly one other vertex
`y`, leaves `H-x` or `H-{x,y}`, which is connected because `H-x` is
two-connected.  The quotient is therefore three-connected.  \(\square\)

## 3. Hamilton cycle in the one-nonterminal kernel

### Lemma 3.1

Let `M` be a simple three-connected graph on seven vertices and suppose
that `v` is incident with no contractible edge.  Then `M-v` is Hamiltonian.

### Proof

Put `H=M-v`.  The graph `H` is two-connected.  Wu's theorem supplies at
least four degree-three neighbours of `v`; each has degree two in `H`.  Set

```text
D={x in V(H): d_H(x)=2},       B=V(H)-D.
```

Then `|D|>=4`, so `|B|<=2`.  If `B` is empty, `H` is a connected
two-regular graph and hence is `C_6`.  If `B={b}`, then `H-b` is connected
and has maximum degree two.  Every neighbour of `b` has degree at most one
in `H-b`, so `H-b` is a path whose ends attach to `b`.  This makes `H` a
cycle and gives `d_H(b)=2`, contrary to `b in B`.

It remains that `B={a,b}` and `|D|=4`.  Every component of `H[D]` is a path
with one end attached to `a` and the other to `b`: attachment twice to the
same branch vertex would make it a cutvertex.  Suppress each such path to
an `ab` edge, assigning it the positive weight equal to its number of
internal vertices; retain a possible literal edge `ab` as a weight-zero
route.  Since `a,b` have degree at least three, there are at least three
parallel routes.

If at most two routes have positive weight, their union, or the unique long
route together with the direct edge, lifts to a Hamilton cycle of `H`.
Thus non-Hamiltonicity requires at least three long routes.  Their positive
weights sum to four, so one is the path

```text
a-x-b.
```

After deleting `x`, at least two `a-b` routes remain, and their expansions
show that `H-x` is two-connected.  Since `M-{a,b}` is connected and `x` has
only `a,b` as neighbours in `H`, the edge `vx` must exist.  Lemma 2.1 then
makes `vx` contractible, contrary to the hypothesis.  Hence `H` is
Hamiltonian.  \(\square\)

## 4. Exact order-seven classification

Let `M` be a `T`-irreducible kernel of order seven and let `v` be its sole
nonterminal.  Every edge at `v` is terminal-legal and hence
noncontractible.  Lemma 3.1 gives a Hamilton cycle `C` in `H=M-v`.

Wu's theorem supplies a set `A subseteq T` of at least four neighbours of
`v`, each having degree two in `H`.  Every member of `A` therefore has only
its two cycle edges.  Consequently every chord of `C` has both ends in
`T-A`.  There are at most two such vertices, so `H` has at most one chord.

If there is no chord, `H=C_6`.  If `v` missed a terminal, take a maximal
nonempty interval of missed vertices on the rim.  Its two boundary rim
vertices are distinct because `v` has at least four neighbours.  Deleting
those boundary vertices separates the interval from `v` and the rest of
the rim, contrary to three-connectivity.  Thus `v` is universal and `M` is
the six-wheel.

Suppose instead that the unique chord has ends `u,w`.  Then necessarily

```text
A=T-{u,w},
```

so `v` sees the other four terminals and may or may not see each of `u,w`.
The chord is not a rim edge.  If its ends were at cyclic distance two, let
`x in A` be the intervening rim vertex.  The graph `H-x` would be the
five-cycle consisting of the chord and the other rim arc.  Since `vx` is an
edge, Lemma 2.1 would make it contractible.  The chord ends must therefore
be opposite on `C_6`.  This proves the classification.

For `|M|=6`, Dirac's circumference theorem gives a cycle of length
`min{2*3,6}=6`.  In both kernel orders the terminal singleton bags therefore
contain a rooted `C_6`.  Expanding the terminal-legal contractions lifts it
to the asserted rooted model in `G`.  \(\square\)

## 5. Exhaustive cross-check

The independent falsifier
[`../active/hc7_six_terminal_kernel_probe.py`](../active/hc7_six_terminal_kernel_probe.py)
enumerates every simple three-connected graph of orders six and seven.  It
finds:

```text
17 three-connected order-six graphs, all Hamiltonian;
4 rooted order-seven irreducible isomorphism types;
0 exceptions to the classification.
```

The computation is not a dependency of the proof.
