# Cold audit of the five-terminal rooted-fan theorem

## Verdict

**GREEN.**  The bounded terminal-kernel theorem, its universal five-root fan
corollary, and the normalized overlap-four consequence are all valid.
Specifically, every `k>=4` prescribed terminals in a simple three-connected
graph admit a terminal-irreducible rooted minor with at most `floor(k/4)`
nonterminals, and every five prescribed vertices root a minor isomorphic to

\[
                         F_5=K_1\vee P_4.
\]

The contractible-edge induction is valid, Wu's published theorem is used
at exactly its stated strength, and all six-vertex residues are covered.
In the overlap-four crossed order, the two fan chords necessarily contain
one of the decoder's four fixed gate repairs, so the branch-set lift gives
a literal `K_7`.

The independently written finite checker is
[`../active/hc7_universal_rooted_f5_audit.py`](../active/hc7_universal_rooted_f5_audit.py).
It is evidence for the finite bases, not a dependency of the proof.

## 1. Primary-source verification

The source is H. Wu, *Contractible Elements in Graphs and Matroids*,
Combinatorics, Probability and Computing **12** (2003), 457--465,
[doi:10.1017/S0963548302005497](https://doi.org/10.1017/S0963548302005497).

The paper's published abstract states both facts used in the proof:

1. `G` is a **simple** three-connected graph with at least five vertices;
2. if a vertex `v` is incident with no contractible edge, then `v` has at
   least four neighbours of degree three, and every such neighbour is
   incident with exactly two contractible edges.

Here a contractible edge is one whose contraction, followed by
simplification of parallel edges, remains simple and three-connected.
The proof does not use the separate extremal bound saying that at most
`|V(G)|/5` vertices miss all contractible edges.

Thus no stronger prescribed-edge splitter theorem has been silently
attributed to Wu.

## 2. Bounded terminal-kernel theorem

Repeatedly contracting a contractible edge with at most one terminal end is
legitimate: the simplified graph remains simple and three-connected, while
the terminal labels remain distinct.  The process terminates because every
contraction reduces the vertex count.  In the terminal-irreducible graph
`M`, every contractible edge therefore has both ends in `T`.

For any nonterminal `v`, no incident edge is contractible.  Wu supplies at
least four degree-three neighbours `A_v`, each incident with exactly two
contractible edges.  Each such neighbour `x` must itself lie in `T`, because
an incident contractible edge has both ends in `T`.  Its three incident
edges are precisely `xv` and its two contractible terminal-terminal edges.

If distinct nonterminals `v,w` shared `x`, then the four distinct edges
from `x` to `v,w` and along its two terminal-terminal contractible edges
would contradict `d_M(x)=3`.  The sets `A_v` are consequently pairwise
disjoint subsets of `T`, each of size at least four.  Hence

```text
4 |V(M)-T| <= sum_v |A_v| <= |T|=k,
```

which proves `|V(M)-T|<=floor(k/4)` and the stronger charge-set statement.
Wu's order-at-least-five hypothesis is respected: for `k>=5` it is
automatic whenever a nonterminal survives; for `k=4`, a surviving
nonterminal gives order at least five, while an empty residue needs no Wu
application.  The stated `k=3` counterexample (`K_4` with three terminals)
correctly shows that the numerical bound cannot be extended unchanged.

## 3. Five-vertex base

When `V(G)=T`, three-connectivity gives `delta(G)>=3`.  Hence every vertex
has complement degree at most one and `complement(G)` is a matching.  On
five vertices that matching misses some vertex `z`, so `z` is universal
in `G`.

The other four vertices induce `K_4` with at most a matching deleted.
Such a graph has a spanning `P_4`: this is immediate for `K_4` and
`K_4-e`, while deleting a two-edge matching leaves `C_4`.  The universal
vertex and this path form a spanning `K_1 join P_4`, with the five
singleton bags rooted at `T`.

## 4. Legal contraction and fan lifting

Call a contractible edge legal when it does not join two members of `T`.
If `e` is legal, contraction leaves five distinct root images:

* when neither end is a root, the roots are unchanged;
* when exactly one end is a root, its contracted image represents that
  root.

Wu's definition makes the simplified graph `G/e` simple and
three-connected.  Induction supplies five rooted fan bags in `G/e`.
Expanding the contracted image to both ends of `e` within its one branch
bag preserves connectivity, disjointness, every root, and all quotient
adjacencies.  The lift is therefore legitimate.

It remains only when every contractible edge has both ends in `T`.

## 5. Reduction to six vertices

Let `v` be a nonterminal.  It is incident with no contractible edge, so
Wu gives at least four degree-three neighbours `A_v`.  For each
`x in A_v`, the two contractible edges at `x` have both ends in `T`.
Consequently `x itself belongs to T`.  Neither contractible edge is `xv`,
because `v` is not a terminal.  Since `d_G(x)=3`, its incident edges are
exactly

```text
xv and two contractible x--T edges.
```

If `v,w` were two distinct nonterminals and some `x` belonged to both
`A_v,A_w`, then `x` would have the two distinct edges `xv,xw` in addition
to its two distinct contractible edges, contradicting degree three.
Thus `A_v` and `A_w` are disjoint.  They would be disjoint subsets of the
five-set `T`, each of order at least four, which is impossible.

There is therefore exactly one nonterminal and `|V(G)|=6`.  This argument
also proves that every Wu neighbour lies in `T`; it does not merely count
four unnamed neighbours.

## 6. Complete six-vertex residue

Let `A` be the Wu neighbours of the unique nonterminal `v`.  Then
`A subseteq T`, `|A|` is four or five, and

\[
                         d_{G[T]}(x)=2\quad(x\in A).       \tag{5.1}
\]

If `A=T`, the graph `G[T]` is a simple two-regular graph on five
vertices, hence `C_5`, and `v` is adjacent to every root.

Suppose `A=T-{y}` and put `epsilon=1` when `vy` is present.  Minimum degree
three gives

\[
                         d_{G[T]}(y)\ge3-\epsilon.
\]

The degree sum of `G[T]` is `8+d_{G[T]}(y)`, so the last degree is even.
It is at most four.  Therefore the exhaustive alternatives are:

```text
epsilon=1 and d_T(y)=2, or d_T(y)=4.
```

In the first alternative all five root degrees inside `T` are two, so
again `G[T]=C_5` and `v` is adjacent to all five roots.  In either
five-cycle case, for any `x in A`, the bag `{v,x}` is universal to the
other four singleton root bags, while deleting `x` from the root cycle
leaves a `P_4`.

In the remaining alternative, `y` is adjacent to every vertex of `A`.
Equation (5.1) says that every vertex of `A` has exactly one further
neighbour in `A`; hence `G[A]` is a perfect matching, say `xa,bc`.  The
bag `{v,x}` is adjacent to each of

```text
{a}, {y}, {b}, {c}:
```

use `xa`, `xy`, `vb`, and `vc`, respectively.  The four singleton bags
contain the path `a-y-b-c`.  This is the final rooted `F_5` model.

No parity or adjacency case is omitted.  In particular, the case
`vy notin E(G)` necessarily lies in the `d_T(y)=4` alternative and is
covered by the same construction.

## 7. Independent finite replay

The checker generated every unlabeled simple three-connected graph of
orders five, six, and seven and enumerated every five-set of roots.  It
used an independent branch-set search over all mappings of nonroots to
the five bags or to deletion.  It reported

```text
n=5 graphs=3   root_sets=3    counterexamples=0
n=6 graphs=17  root_sets=102  counterexamples=0
n=7 graphs=136 root_sets=2856 counterexamples=0
```

At order six, exactly one rooted instance had its nonterminal incident
with no contractible edge.  It is the wheel consisting of a universal
nonterminal and a five-cycle on `T`; the checker returned the bag made
from the hub and one rim root, exactly matching the proof's first residue.

## 8. Overlap-four decoder implication

Let the outer cycle of the rooted fan have one of the decoder's crossed
orders

```text
l_1,l_2,r,6,s.
```

The fixed gate defects are

```text
l_1 6, l_1 r, l_2 6, l_2 s.                            (7.1)
```

In a pentagon triangulated as `K_1 join P_4`, the two chords have the same
universal end.  Their exact values at each possible universal position
are:

| universal bag | two chords | fixed repair supplied |
|---|---|---|
| `l_1` | `l_1 r`, `l_1 6` | both |
| `l_2` | `l_2 6`, `l_2 s` | both |
| `r` | `r s`, `r l_1` | `r l_1` |
| `6` | `6 l_1`, `6 l_2` | both |
| `s` | `s l_2`, `s r` | `s l_2` |

Thus at least one fan chord realizes one of (7.1) for every placement of
the universal bag.  It is an actual adjacency between two connected
rooted exterior bags.  It is not asserted to be a literal edge between
the terminal vertices and is not fed into any original support relation.

The independently audited cycle decoder tests gate maximality in exactly
this final virtual edge layer: adding any one fixed repair gives a `K_7`
model in all 27 crossed states.  Replacing the terminal labels by the five
rooted fan bags preserves connectivity, disjointness, and the chord
adjacency, so the quotient certificate lifts to a literal `K_7` model in
`G`.

For the ten noncrossed orders the same decoder already gives `K_7`, either
directly or through its audited common three-rooted small-`K_4` outcome.
The overlap-four corollary is therefore complete under the eleven
irredundant support hypotheses.

## 9. Trust boundary

The universal rooted-fan theorem requires simple three-connectivity and
five **distinct** roots.  It does not prescribe which terminal is the
universal fan vertex.  The overlap-four argument needs no such
prescription because the table in Section 7 covers all five possibilities.

The corollary closes only the normalized overlap-four cell governed by the
eleven irredundant support constraints.  It does not prove the entire
support-six transversal theorem or `HC_7`.
