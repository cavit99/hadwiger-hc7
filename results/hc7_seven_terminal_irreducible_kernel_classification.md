# Exact seven-terminal irreducible kernels

## Status and scope

**Status:** proved and independently audited **GREEN** in
[`hc7_seven_terminal_irreducible_kernel_classification_audit.md`](hc7_seven_terminal_irreducible_kernel_classification_audit.md).

This is a standard rooted-minor theorem for seven prescribed vertices in a
simple three-connected graph.  It is independent of `HC_7`.  Its only
non-elementary input is Wu's contractible-edge theorem, through the audited
terminal-kernel theorem in
[`hc7_five_terminal_rooted_fan.md`](hc7_five_terminal_rooted_fan.md).

The point of the exact statement is its quantifier.  An order-eight kernel
does not merely give an unspecified rooted cycle.  It gives one of three
explicit terminal graphs, its exact extra-vertex neighbourhood, and a bundle
of legal owner absorptions.  This is the information a labelled composition
argument may use.

## 1. Definitions and contraction criterion

Let `T` be a set of seven labelled vertices.  An edge is **`T`-legal** if it
does not have two ends in `T`.  A simple three-connected graph containing `T`
is **`T`-irreducible** if it has no `T`-legal contractible edge.

We use the following exact version of the elementary contraction criterion.

### Lemma 1.1

Let `M` be simple and three-connected, let `xv` be an edge, and put
`H=M-x`.  Then `xv` is contractible if and only if `H-v` is two-connected.

### Proof

For the forward implication, contract `xv` to `z`.  If the simplified
quotient is three-connected, deleting `z` leaves the two-connected graph
`M-{x,v}=H-v`.

Conversely suppose that `H-v` is two-connected.  A deletion of at most two
vertices of `M/xv` which avoids `z` lifts to the same deletion in `M`, and
therefore leaves a connected graph.  Deleting `z`, and possibly one further
vertex `w`, leaves `H-v` or `H-{v,w}`, which is connected.  Thus `M/xv` is
three-connected.  \(\square\)

## 2. Exact order-eight classification

### Theorem 2.1

Let `M` be a `T`-irreducible simple three-connected graph with

```text
V(M)=T union {x}.
```

There is a cyclic labelling `t_0,t_1,...,t_6` of `T` for which exactly one of
the following descriptions applies.  In each display, `C` is the cycle

```text
t_0 t_1 t_2 t_3 t_4 t_5 t_6 t_0.
```

1. **Wheel type.**

   ```text
   M[T]=C,
   N_M(x)=T.
   ```

2. **One-chord type.**  For some `U subseteq {t_0,t_3}`,

   ```text
   M[T]=C+t_0t_3,
   N_M(x)={t_1,t_2,t_4,t_5,t_6} union U.
   ```

3. **Two-chord type.**  For some `U subseteq {t_0,t_1,t_4}`,

   ```text
   M[T]=C+t_0t_4+t_1t_4,
   N_M(x)={t_2,t_3,t_5,t_6} union U.
   ```

Conversely, every graph in these three displayed families is simple,
three-connected, and `T`-irreducible.

Up to unlabelled rooted isomorphism these are ten types: one wheel, three
one-chord types according as `U` has size zero, one, or two, and six
two-chord types according to `U` up to interchange of `t_0,t_1`.

### Proof

Put `H=M-x`.  The graph `H` is two-connected.  The Hamilton-remainder lemma
proved in
[`hc7_seven_terminal_rooted_cycle_or_biclique.md`](hc7_seven_terminal_rooted_cycle_or_biclique.md)
shows that `H` has a Hamilton cycle `C`.

Let

```text
A={a in T : xa is an edge and d_M(a)=3}.
```

Wu's theorem and terminal irreducibility give `|A|>=4`.  Moreover every
member of `A` has degree two in `H`.  Hence no chord of `C` is incident with
a member of `A`.  Write `B=T-A`, so `|B|<=3`, and let `R` be the graph on `B`
whose edges are the chords of `C` in `H`.

Every vertex of `B` has degree at least one in `R`.  Indeed, if `b in B` had
degree two in `H`, minimum degree three in `M` would force `xb` to be an
edge, making `d_M(b)=3` and hence `b in A`, a contradiction.

If `B` is empty, `H=C`; minimum degree forces `x` to see every terminal.
This is the wheel type.  The case `|B|=1` is impossible because `R` has
minimum degree at least one.

Suppose `|B|=2`.  Then `R` is its single possible edge, so `H` is `C` plus
one chord.  Its ends cannot be at cyclic distance two.  Otherwise the
intervening vertex `a` belongs to `A`, and `H-a` contains the six-cycle made
from the chord and the other rim arc.  Lemma 1.1 would make `xa`
contractible.  Thus the chord ends have cyclic distance three.  Relabel them
`t_0,t_3`.  The five other terminals are in `A`, while `x` may independently
see either chord end.  This is the one-chord type.

It remains that `|B|=3`.  A simple three-vertex graph of minimum degree one
is a path or a triangle.  The triangle is impossible.  In that case `B` is
independent on `C`, and the four vertices of `A` occupy three nonempty cyclic
gaps between consecutive members of `B`.  One gap has size one.  Its unique
vertex `a` is in `A`, the two ends of the gap are joined by a chord, and
again `H-a` contains a spanning cycle, contradicting Lemma 1.1.

Consequently `R` is a path.  Call its centre `b` and its leaves `u,w`.  Each
of the chords `bu,bw` has cyclic distance three.  It cannot have distance
two with an intervening member of `A`, by the same contraction argument.  If
the intervening vertex were the other leaf, then that leaf would be a rim
neighbour of `b`; its required edge to `b` would be a rim edge rather than a
chord of `R`, again impossible.  On a seven-cycle the two vertices at cyclic
distance three from `b` are adjacent.  Relabel

```text
b=t_4,  {u,w}={t_0,t_1}.
```

This gives the two-chord terminal graph.  Its other four vertices form `A`,
and `x` may independently see any subset of `B`, proving necessity.

For completeness, consider the converse.  It suffices first to omit the
optional edges from `x` to `U`, since adding them cannot destroy
three-connectivity.  In every family, deleting `x` and at most one terminal
leaves a connected graph because `H` is two-connected.  If `x` remains and
at most two terminals are deleted, the rim breaks into at most two paths.
Every path containing a displayed mandatory neighbour of `x` attaches to
`x`.  In the one-chord family, a remaining path containing only a chord end
is joined by the chord to the other end; isolating both ends would require a
third deletion.  In the two-chord family, the only rim intervals without a
mandatory neighbour of `x` lie in `{t_0,t_1}` or in `{t_4}`.  The two chords
join either such interval to the other one, and deleting both rim boundary
vertices already uses the two allowed deletions.  Thus the graph remains
connected after every deletion of at most two vertices, and is
three-connected.

Only edges at `x` are `T`-legal.  Lemma 1.1 reduces their noncontractibility
to checking that `H-v` is not two-connected.  In the wheel type it is a
path.  In the one-chord type, deleting a chord end removes the chord, while
deleting any other terminal leaves a path whose endpoints are not joined by
the distance-three chord.  In the two-chord type, deleting `t_4` leaves a
path; deleting `t_0` or `t_1` leaves a path with one chord and a degree-one
endpoint; and deleting one of `t_2,t_3,t_5,t_6` again leaves a degree-one
endpoint.  These statements are unaffected by which optional edges `xU`
are present.  Every edge at `x` is therefore noncontractible.  This proves
the converse and the classification.  \(\square\)

## 3. Exact finite owner catalogue

Let `K` be one of the order-eight templates in Theorem 2.1, put

```text
H=K[T],   W=N_K(x),
```

and choose any **owner** `w in W`.  The seven bags

```text
{w,x},  and {t} for t in T-{w}
```

have an adjacency graph containing

```text
Q(K,w)=H + {wv : v in W-{w}}.                         (3.1)
```

Thus every owner in `W` is legal.  Notice that (3.1) retains every terminal
chord and every actual contact of `x`; replacing it by an arbitrary
four-charge star loses valid kernel information.

For the order-seven branch, let `E_7` be the finite set of all labelled
edge-minimal simple three-connected graphs on `T`.  There are five
unlabelled and `5,495` labelled members.  Every simple three-connected graph
on `T` contains a member of `E_7` as a spanning subgraph.

Combining this observation with the audited terminal-kernel bound gives the
following exact decoder rule.

### Corollary 3.1 (complete seven-terminal carrier catalogue)

Let `G` be simple and three-connected and let `T` be seven prescribed
vertices.  Apply terminal-legal contractions to a `T`-irreducible kernel.
Exactly one of the following finite alternatives is available after lifting
the rooted bags back to `G`.

1. One labelled carrier in `E_7` occurs on seven terminal-rooted bags.
2. One exact template `K` from Theorem 2.1 occurs, and for **every**
   `w in N_K(x)` the owner quotient `Q(K,w)` occurs on seven terminal-rooted
   bags.

Consequently a labelled composition test is complete precisely when it
checks

```text
every F in E_7,
```

and, for each order-eight template `K`, verifies that

```text
some w in N_K(x) closes Q(K,w).
```

This is a finite universal/existential catalogue, not a claim that one fixed
owner works for all kernels.  There are `30,600` labelled exact order-eight
templates.

## 4. Exhaustive falsification

The independent script
[`../active/hc7_seven_terminal_kernel_bundle_probe.py`](../active/hc7_seven_terminal_kernel_bundle_probe.py)
enumerates all simple three-connected graphs of orders seven and eight.  It
finds

```text
5       unlabelled edge-minimal order-seven carriers,
5,495   labelled edge-minimal order-seven carriers,
10      rooted order-eight irreducible isomorphism types,
30,600  labelled exact order-eight templates,
0       exceptions to the owner-bundle classification.
```

It also generates the three abstract families directly from a fixed
seven-cycle and recovers exactly the same ten rooted isomorphism types.  The
computation is a falsifier and cross-check, not a dependency of the proof.
