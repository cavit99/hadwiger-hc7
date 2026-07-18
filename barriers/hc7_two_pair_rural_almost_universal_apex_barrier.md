# An almost-universal two-apex barrier to the rural two-pair shortcut

**Status:** explicit computer-checked barrier to an intermediate claim.  This
is not a counterexample to `HC_7`: the graph is six-colourable and is not
seven-contraction-critical.

## 1. The shortcut refuted

The following implication is false, even when all of its displayed
host-level hypotheses are imposed:

> Let `G` be seven-connected and `K_7`-minor-free, and let
> `V(G)=L dotunion T dotunion R` be an exact separation with `|T|=7`.
> Suppose two disjoint independent pairs `I,J subseteq T` have no disjoint
> `I`- and `J`-connectors through `L`, the rooted graph
> `G[L union I union J]` has a cell-free disk embedding with the four roots
> alternating, and the opposite closed shore contains the five named rows
> with traces `I,J,{s},{t},emptyset`.  Then either `G` has a `K_7` minor or
> two vertices of `T-(I union J)` meet every `K_5`-minor model in `G`.

The construction below satisfies every hypothesis but neither conclusion.
It shows that the rural embedding, the five rows, seven-connectivity, and
`K_7`-minor exclusion do not replace the proper-minor colouring responses
available in a hypothetical minimal counterexample.

## 2. The planar tube

Let `P` have vertices

```text
Top, Bottom, and (r,k) for r in {0,1,2}, k in Z/5Z.
```

Its edges are

```text
(r,k)(r,k+1)                       for r=0,1,2;
Top(0,k), Bottom(2,k)               for every k;
(r,k)(r+1,k), (r,k)(r+1,k-1)       for r=0,1.
```

Thus `P` is the length-two pentagonal triangulated tube.  It is planar and
five-connected.  These two finite facts are checked independently by the
accompanying verifier.

Put

```text
x=(0,0),  u=(1,0),  v=(1,4).
```

Create `G` by adding adjacent vertices `p,q`, joining `p` to every vertex
of `P` except `u`, and joining `q` to every vertex of `P` except `v`.

Define

```text
L = {x},
T = N_G(x),
R = V(G) - (L union T),
I = {p,u},
J = {q,v},
B = T - (I union J) = {Top,(0,1),(0,4)}.
```

There is no `L-R` edge, `R` is connected, and `T=N_G(L)` has order seven.
Both `I` and `J` are independent.

## 3. Seven-connectivity and `K_7`-minor exclusion

### Seven-connectivity

Let `Z` have order at most six.

- If `p,q in Z`, then at most four vertices of the five-connected graph
  `P` have been deleted.
- If exactly one of `p,q` remains, say `q`, then `q` is adjacent to every
  vertex of `P` except `v`.  The vertex `v` has degree six in `P`, so after
  at most five vertices of `P` have been deleted, either `v` is deleted or
  it retains a neighbour adjacent to `q`.
- If both `p,q` remain, every vertex of `P` is adjacent to at least one of
  them, and `pq` is an edge.

In every case `G-Z` is connected.  Since `d_G(x)=7`, it follows that
`kappa(G)=7`.

### No `K_7` minor

Deleting `p,q` leaves the planar graph `P`.  If seven pairwise adjacent
branch sets existed in `G`, at most two of them could contain `p` or `q`.
The other five would be a `K_5`-minor model in `P`, contrary to planarity.
Thus `G` is `K_7`-minor-free.

## 4. The exact rural four-root obstruction

The five neighbours of `x` in `P` induce a cycle.  The vertex `p` is
adjacent to every member of that cycle except `u`, while `q` is adjacent
to every member except `v`.  Consequently

```text
alpha(G[T]) = 2.
```

The graph

```text
H = G[{x} union I union J]
```

is the wheel with rim

```text
p - q - u - v - p
```

and hub `x`.  Hence it has a cell-free disk embedding with the roots in
alternating order.  It has no pair of vertex-disjoint paths joining `p`
to `u` and `q` to `v`: after the other pair of roots is forbidden, each
of those two connections must use the unique hub `x`.

## 5. Five explicit rows

Take the distinguished boundary vertex and the two singleton traces to be

```text
a=Top,  s=(0,1),  t=(0,4).
```

In `G[R union T]-a`, define

```text
Q_I = {p,u,(2,0)},
Q_J = {q,v,(2,4)},
Q_s = {s,(1,1),(1,2)},
Q_t = {t,(1,3),(0,3)},
Q_0 = {(0,2)}.
```

These five sets are pairwise disjoint.  Each induces a connected subgraph,
the five subgraphs are pairwise adjacent, and `a` is adjacent to every one
of them.  Their literal boundary traces are respectively

```text
I, J, {s}, {t}, emptyset.
```

Thus this is exactly the independent-trace rural five-row configuration,
not merely an unlabelled quotient imitation.

## 6. No pair in `B` is a `K_5`-model transversal

After deleting `(0,1),(0,4)`, the five vertices

```text
p, q, Top, (0,2), (0,3)
```

induce a `K_5`.  After deleting either pair

```text
{Top,(0,1)} or {Top,(0,4)},
```

the five vertices

```text
p, q, Bottom, (2,0), (2,1)
```

induce a `K_5`.  Hence no two vertices of `B` meet every `K_5`-minor model.

## 7. Exact scope

The planar graph `P` is four-colourable, and assigning two new colours to
the adjacent vertices `p,q` gives a six-colouring of `G`.  Therefore this
barrier deliberately lacks the hypothesis that `G` is not six-colourable
and that every proper minor is six-colourable.

It does **not** refute a theorem that uses contraction-critical colouring
responses to produce a common boundary partition, an explicit `K_7`-minor
model, or a global two-vertex transversal.  Rather, it proves that such a
theorem must spend those responses: web structure, five-row geometry,
seven-connectivity, and `K_7`-minor exclusion alone are insufficient.

## 8. Verification

Run from the repository root:

```bash
PYTHONPATH=active/runtime/deps python3 \
  barriers/hc7_two_pair_rural_almost_universal_apex_barrier_verify.py
```

Expected output:

```text
tube: planar and 5-connected
host: 7-connected and K7-minor-free by the two-apex argument
boundary: alpha 2; alternating wheel has no required two-linkage
rows: exact traces and all required adjacencies verified
transversal: every pair in B misses an explicit K5 subgraph
colouring: explicit proper 6-colouring verified
```
