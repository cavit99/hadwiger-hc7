# An icosahedral barrier to combining contraction models

## Status

This note gives a uniform counterexample to a broad class of
multi-contraction arguments.  It does **not** contradict Hadwiger's
conjecture: the constructed graph is `(t-1)`-colourable.  Its point is
that all of the following data can hold simultaneously without producing
a `K_t` minor:

* connectivity at least `t` and minimum degree at least `t`;
* Hadwiger number exactly `t-1`; and
* many proper edge contractions, each having both chromatic and Hadwiger
  number exactly `t-1`.

For `t=5`, the equality holds after **every** edge contraction.  Thus the
family of unrooted `K_{t-1}` models supplied by contractions cannot be
combined by a minor-theoretic invariant alone.  A successful use of all
contractions in a hypothetical counterexample must exploit the extra
fact `chi(G)=t` (and its colouring/Kempe consequences), not only the
existence or abundance of the contraction models.

## 1. The construction

Let `I` be the icosahedral graph.  Thus `I` is planar, five-connected,
five-regular, and edge-transitive.  It contains an odd wheel: in the
standard labelling

```text
t,b,u_0,...,u_4,w_0,...,w_4,
```

the vertices `w_0,...,w_4` induce a five-cycle and `b` is adjacent to all
of them.  Consequently

```text
chi(I)=4,       eta(I)=4,       kappa(I)=delta(I)=5.       (1.1)
```

Here `eta` denotes the Hadwiger number.  The upper bound on `eta(I)` is
planarity, and a three-connected graph has a `K_4` minor.

For an integer `k>=0`, put

```text
J_k = K_k join I,              t=k+5.                      (1.2)
```

The empty join is allowed when `k=0`.

### Theorem 1.1 (multi-contraction barrier)

For every `k>=0`, the graph `J_k` satisfies

```text
chi(J_k)=eta(J_k)=t-1,
kappa(J_k)=t,
delta(J_k)>=t,
J_k has no K_t minor.                                      (1.3)
```

Moreover, for every edge `e` whose two ends lie in the icosahedral part,

```text
chi(J_k/e)=eta(J_k/e)=t-1.                                 (1.4)
```

In particular, the thirty distinct contractions of the icosahedral edges
all supply tight `K_{t-1}` models, but no selection of those models can
force a `K_t` minor in `J_k`.

For `k=0` (so `t=5`), every edge of the graph is an icosahedral edge.
Thus (1.4) holds for **every** edge contraction while `I` remains
`K_5`-minor-free, five-connected, and of minimum degree five.

### Proof

For every graph `H` and integer `k>=0`,

```text
chi(K_k join H)=k+chi(H),
eta(K_k join H)=k+eta(H).                                 (1.5)
```

The chromatic equality is immediate.  For the second equality, the
`k` universal clique vertices together with a maximum clique model in
`H` give the lower bound.  Conversely, remove from an arbitrary clique
model every branch bag meeting the `K_k`.  At most `k` bags are removed,
and the remaining bags form a clique model wholly in `H`, so their number
is at most `eta(H)`.

Equation (1.1) and (1.5) give

```text
chi(J_k)=eta(J_k)=k+4=t-1,
```

and in particular exclude a `K_t` minor.

Every vertex of the icosahedral part has degree `k+5=t` in `J_k`, while
each clique vertex is universal.  Hence `delta(J_k)>=t`.  Any vertex cut
of `J_k` must contain all `k` universal clique vertices; after their
deletion at least five more vertices are needed to disconnect the
icosahedron.  Conversely the universal clique together with a minimum
five-cut of `I` disconnects the join.  Therefore

```text
kappa(J_k)=k+5=t.                                          (1.6)
```

It remains to prove (1.4).  By edge-transitivity it is enough to contract
the edge `tu_0`.  Edge contraction preserves planarity.  It also lowers
vertex-connectivity by at most one, so `I/tu_0` is four-connected; in
particular it has a `K_4` minor.  Hence

```text
eta(I/tu_0)=4.                                             (1.7)
```

The odd wheel on `b,w_0,...,w_4` is disjoint from the contracted edge and
survives literally.  Thus `I/tu_0` is not three-colourable; the Four
Colour Theorem gives

```text
chi(I/tu_0)=4.                                             (1.8)
```

Since contraction inside the second join factor commutes with the join,

```text
J_k/e = K_k join (I/e).
```

Equations (1.5), (1.7), and (1.8) now give (1.4).  QED.

## 2. Exact implication for a contraction-critical proof

Let `G` be a least-parameter, minor-minimal counterexample at parameter
`t`.  Then the genuinely stronger facts are

```text
chi(G)=t,
chi(G/e)=eta(G/e)=t-1       for every edge e.              (2.1)
```

Theorem 1.1 shows that the second line, even when combined with the
counterexample-level degree/connectivity scale and with `eta(G)=t-1`,
does not by itself contain a branch-set exchange forcing `K_t`.  At
`t=5` it fails with every contraction tight.

Accordingly, any uniform multi-contraction lemma must include a
colour-sensitive compatibility condition which fails in the icosahedron.
Examples of legitimate extra data are:

1. a common literal `(t-2)`-clique boundary whose colours canonically
   label the external bags;
2. a boundary-faithful equality state shared by operations on opposite
   shores, allowing colour gluing; or
3. a Kempe exchange which turns a palette colour into a prescribed model
   contact while avoiding the other branch bags.

Merely choosing more contraction models, maximizing their overlap, or
assuming stronger ordinary connectivity cannot supply that missing
alignment.  The existing audited uniform warehouse theorem is therefore
at the correct frontier: it reduces a contracted root bag to charged
warehouses and ordered owner corridors, but the final step must use the
`chi(G)=t` state incompatibility rather than another unrooted model count.

