# Independent audit: cycle completion from two connected shores

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollary 3.2,
Lemmas 3.3--3.4, and Corollary 3.5 at the exact revision below.  This is a
separate internal mathematical audit, not external peer review.  The result
does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_adjacent_full_pair_cycle_completion.md`](hc7_adjacent_full_pair_cycle_completion.md)
at promoted SHA-256

```text
832fff95b699aa73b1f1b10cc52e1f562d6e108dad059962b3563a799bc3f875
```

The mathematical text is identical to the independently audited revision
`730469b2736a4ea6f947cd24e91decc2fa88de233c911d447235319fa4034208`;
the promoted revision changes only the status line to link this audit.

The source materially strengthens the previously audited revision.  It no
longer assumes that the two boundary-full subgraphs are adjacent, that the
two one-defect subgraphs are adjacent, or that their boundary defects are
exact.  The new connected-shore reductions and every displayed minor model
were checked independently below.  No unresolved mathematical assumption or
gap remains within the stated trust boundary.

## 1. The adjacent connected normal form

The first half of Lemma 2.1 invokes Lemma 1.1 of the GREEN-audited
[`hc7_exact7_connected_rich_width2_frontier.md`](hc7_exact7_connected_rich_width2_frontier.md).
That dependency is present at its promoted SHA-256

```text
943808c3b7aa2e53d299d500b2ea2ff0f8fe03bf09d1d70e573a656bc4b33225
```

and its adjacent audit verifies Sections 1--6, including Lemma 1.1.  After
contracting the two prescribed disjoint connected subgraphs, deleting an
edge on the root-to-root path in a spanning tree divides the connected shore
into two connected vertex sets, one containing each prescribed subgraph.
Expanding the contractions gives a genuine partition

```text
R = P_0 disjoint-union P_1
```

with a literal cross-edge.  Since each part contains one of `Q_0,Q_1`, both
parts remain adjacent to every boundary vertex.

For the second half, take a shortest path

```text
v_0 v_1 ... v_k
```

from `V(A_d)` to `V(A_e)` in the connected graph `G[L]`, with its endpoints
in the two prescribed sets.  Since those sets are disjoint, `k>=1`.  No
internal path vertex belongs to either original subgraph: such a vertex
would give a strictly shorter path between the two vertex sets.  Therefore
adjoining `v_1,...,v_{k-1}` and the path edges up to `v_{k-1}` to `A_d`
preserves disjointness from `A_e`, preserves connectivity, and leaves the
last edge `v_{k-1}v_k` as an edge between the enlarged subgraphs.  The same
argument covers `k=1`, when no vertex is absorbed.  Enlargement cannot
remove any boundary contact, so both inclusions in (1.1) persist.

Thus Lemma 2.1 is valid and uses connectedness of each shore exactly as the
source states.

## 2. Theorem 3.1: the seven branch sets

Let `C` be a cycle in `G[S-{d,e}]`.  Dividing its cyclic order into three
nonempty consecutive intervals gives pairwise disjoint connected vertex
sets `M_1,M_2,M_3`.  The three transition edges of the cycle give one edge
between every pair of interval sets, including when `C` is a triangle.

The seven displayed sets

```text
P_0,
P_1,
V(Ahat_d) union {e},
V(Ahat_e) union {d},
M_1,
M_2,
M_3
```

are pairwise disjoint: the first two lie in `R`, the next two use disjoint
off-boundary subgraphs in `L` and the distinct roots, and the last three lie
in `S-{d,e}`.  They are connected because `Ahat_d` is adjacent to `e` and
`Ahat_e` is adjacent to `d`; these contacts follow from the lower bounds
`S-{d} subseteq N(Ahat_d)` and
`S-{e} subseteq N(Ahat_e)`.

All twenty-one branch-set adjacencies are supplied as follows.

| Branch-set pairs | Count | Supplying fact |
|---|---:|---|
| `P_0,P_1` | 1 | the cross-edge from Lemma 2.1 |
| one `P_j` and one enlarged off-boundary set | 4 | the `P_j` contact at `e` or `d` |
| one `P_j` and one cycle interval | 6 | boundary fullness of `P_j` |
| the two enlarged off-boundary sets | 1 | the cross-edge from Lemma 2.1 |
| one enlarged off-boundary set and one interval | 6 | every cycle vertex avoids both `d,e` |
| two distinct interval sets | 3 | the cycle transition edges |

The total is `1+4+6+1+6+3=21`.  Hence the seven sets form an explicit
`K_7`-minor model.  Corollary 3.2 is its immediate contrapositive.

## 3. Lemma 3.3: the `(3,5)` type

Assume for contradiction that `G` has no `K_7` minor.  Forest normalization
forces each of the two disjoint odd cycles to contain a root.  If one
contained both roots, the other would avoid both, so the roots occur one per
cycle.  Relabeling the roots if necessary, let the five-cycle `C` contain
`d` and the disjoint triangle contain `e`.  A non-root triangle vertex `t`
is distinct from every vertex of `C`.

The five-cycle can be partitioned into three nonempty consecutive intervals
so that the interval `M_1` containing `d` has at least two vertices.  The
seven sets in (3.2) are disjoint.  Connectivity of the two enlarged
off-boundary sets follows from the contacts `e--Ahat_d` and `t--Ahat_e`.

Their twenty-one adjacencies have the same count as in Theorem 3.1.  The only
changed checks are these:

- `Ahat_e` is adjacent to every interval because the five-cycle avoids `e`;
- `Ahat_d` is adjacent to the two intervals avoiding `d` and to `M_1`
  through any non-`d` vertex of `M_1`;
- each `P_j` is adjacent to the two enlarged off-boundary sets through its
  boundary contacts at `e` and `t`.

All other adjacencies come from the two shore cross-edges, boundary
fullness, and the cycle transition edges.  Thus (3.2) is an explicit
`K_7`-minor model, and Lemma 3.3 is correct.

## 4. Lemma 3.4: an extra rooted-triangle neighbour

Let `dxy` be the displayed boundary triangle and let `e` lie outside it.

### Case `w != e`

The five vertices `d,e,w,x,y` are distinct, so an eight-vertex boundary
contains a vertex `t` outside that set.  In (3.3):

- `Ahat_d union {e}` and `Ahat_e union {t}` are connected;
- `{d,w}` is connected by the assumed edge `dw`;
- `{d,w}`, `{x}`, and `{y}` are pairwise adjacent through `dx,dy,xy`;
- `Ahat_d` meets the first boundary set through `w`, while `Ahat_e` meets it
  through `d`; both meet `x` and `y`;
- the two off-boundary sets meet one another through their cross-edge;
- each `P_j` meets the enlarged off-boundary sets through `e,t` and meets
  each of the final three sets by boundary fullness.

The seven sets are disjoint, so these checks exhaust all branch-set pairs.

### Case `w = e`

Here `de` is an edge.  The set `S-{d,e,x,y}` has four vertices, so distinct
`a,b` can be chosen as in (3.4).  The sets

```text
Ahat_d union {a},   Ahat_e union {b},   {d,e},   {x},   {y}
```

are connected and mutually disjoint.  The first two meet `P_0,P_1` through
`a,b`; they meet one another through the off-boundary cross-edge; each meets
all three final boundary sets because `Ahat_d` sees `e,x,y` and `Ahat_e`
sees `d,x,y`; and the final three sets are pairwise adjacent through
`de,dx,dy,xy`.  Boundary fullness supplies their contacts with `P_0,P_1`.
Thus (3.4) also gives an explicit `K_7`-minor model.

Interchanging `d,e` preserves every hypothesis, so the symmetric assertion
is valid.

## 5. Corollary 3.5

In a `K_7`-minor-free graph, Corollary 3.2 forces each of two
vertex-disjoint odd cycles to meet `{d,e}`.  Disjointness forces one root in
each cycle.  Two disjoint simple odd cycles on an eight-vertex set have
orders only `(3,3)` or `(3,5)`.  Lemma 3.3 excludes `(3,5)`, so both are
triangles.  Each root already has its two triangle neighbours, and any
additional boundary neighbour is excluded by Lemma 3.4.  Therefore both
root degrees in `G[S]` are exactly two.

After deleting the roots, the two opposite triangle edges remain in the
forest from Corollary 3.2.  Other edges among the six non-root vertices are
allowed only insofar as the residual graph remains a forest.  This is
exactly the normalized `(3,3)` description in the source.

## 6. Applicability and trust boundary

The live connected two-component opposite-response branch recorded in
[`active/hc7_degree7_model_separator_frontier.md`](../active/hc7_degree7_model_separator_frontier.md)
has exactly the data used here:

- its two open shores are connected components and hence are anticomplete;
- the merged-response shore contains the two disjoint connected one-defect
  subgraphs `A_d,A_e`, which satisfy the weaker contact inclusions (1.1);
- the connected split-response shore contains two disjoint connected
  boundary-full subgraphs.

Thus Lemma 2.1 supplies both cross-edges and Theorem 3.1 applies directly;
the colouring-response orientation is not used in the construction.  The
result eliminates every cycle in `G[S-{d,e}]` for arbitrary shore orders.
It does **not** eliminate rooted triangles in `G[S]`: Corollary 3.5 leaves
the explicit two-rooted-triangle forest configuration.

The audit does not infer a common boundary equality partition, an
order-seven separation, a label-preserving recursive descent, or a proof of
`HC_7`.  Those limitations are stated accurately in the source.
