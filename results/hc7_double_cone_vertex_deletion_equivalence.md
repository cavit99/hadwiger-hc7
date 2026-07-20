# Double-cone vertex-deletion equivalence

**Status:** written proof; separate internal audit GREEN in
[`hc7_double_cone_vertex_deletion_equivalence_audit.md`](hc7_double_cone_vertex_deletion_equivalence_audit.md).

## 1. Exact equivalence

For a graph `J`, let `I_2 \vee J` denote the graph obtained by adding two
nonadjacent vertices `a,b`, each adjacent to every vertex of `J`.

### Theorem 1 (double-cone equivalence)

For every nonempty finite graph `J`, the following are equivalent.

1. `I_2 \vee J` contains a `K_7` minor.
2. There is a vertex `v \in V(J)` such that `J-v` contains a `K_5` minor.

#### Proof

Suppose first that `J-v` has a `K_5`-minor model with branch sets
`M_1,\ldots,M_5`.  Then

\[
\{a\},\qquad \{b,v\},\qquad M_1,\ldots,M_5
\]

are seven pairwise disjoint connected sets.  The first set is adjacent to the
second through the edge `av`; both are adjacent to every `M_i`; and the five
sets `M_i` are pairwise adjacent.  They are therefore a `K_7`-minor model in
`I_2 \vee J`.

Conversely, let `\mathcal M` be a `K_7`-minor model in `I_2 \vee J`.  At most
two branch sets of `\mathcal M` meet `\{a,b\}`.

- If no branch set meets `\{a,b\}`, all seven branch sets lie in `J`.  Choose
  five of them and choose `v` in a sixth.
- If exactly one branch set meets `\{a,b\}`, at least six branch sets lie in
  `J`.  Choose five of them and choose `v` in the sixth.
- If two branch sets meet `\{a,b\}`, the remaining five branch sets lie in
  `J`.  The two exceptional branch sets cannot both be the singletons
  `\{a\}` and `\{b\}`, since those sets are not adjacent.  Hence at least one
  exceptional branch set contains a vertex `v` of `J`.

In every case, the five selected branch sets lie in `J-v` and form a
`K_5`-minor model there.  This proves the reverse implication.  ∎

## 2. Two full shores

Call a connected subgraph `Q` **full to** a set `B` if every vertex of `B`
has a neighbour in `Q`.

### Corollary 2 (boundary deletion condition)

Let `G` contain disjoint connected subgraphs `Q_0,Q_1` and a vertex set `B`
disjoint from both, such that `Q_0,Q_1` are anticomplete and each is full to
`B`.  If `G` has no `K_7` minor, then

\[
G[B]-v\text{ has no }K_5\text{ minor for every }v\in B.
\]

Consequently, `\chi(G[B]-v)\le 4` for every `v\in B`.  In particular, if
`\chi(G[B])=5`, then `G[B]` is vertex-5-critical.

#### Proof

Contract `Q_0` and `Q_1` separately.  Keeping only their edges to `B` and the
edges of `G[B]` produces `I_2\vee G[B]` as a minor of `G`.  The first conclusion
now follows from Theorem 1.  The inequality `\chi(G[B]-v)\le4` is Hadwiger's
theorem for `t=5`: a graph of chromatic number at least five contains a `K_5`
minor.  The final assertion is immediate.  ∎

## 3. A simplicial boundary vertex

### Corollary 3 (four-colourability from one simplicial vertex)

Under the hypotheses of Corollary 2, suppose that `d\in B` has exactly two
neighbours `x_d,y_d` in `G[B]`, and that `x_dy_d\in E(G)`.  Then `G[B]` has no
`K_5` minor and hence

\[
\chi(G[B])\le4.
\]

#### Proof

Assume that `G[B]` has a `K_5`-minor model
`M_1,\ldots,M_5`.  We first modify it to avoid `d`.

If `d` is unused, there is nothing to do.  Otherwise let `d\in M_1`.  The set
`M_1` cannot equal `\{d\}`: a singleton branch set of degree two cannot be
adjacent to the other four branch sets.  Removing `d` leaves `M_1` connected.
Indeed, if only one of `x_d,y_d` lies in `M_1`, then `d` is a leaf of
`G[M_1]`; if both lie in `M_1`, the edge `x_dy_d` replaces any use of the
two-edge path `x_d d y_d`.

No branch-set adjacency is lost.  The only possible lost edge from `M_1` to
another branch set is `dx_d` or `dy_d`.  If, say, `x_d\in M_1` and
`y_d\in M_j`, then the edge `x_dy_d` retains the adjacency between `M_1-d`
and `M_j`; the other cases are immediate.  Thus

\[
M_1-d,M_2,\ldots,M_5
\]

is a `K_5`-minor model in `G[B]-d`, contradicting Corollary 2.

For completeness, the corresponding seven branch sets in `G` are explicit:
after orienting the two full shores as `Q_0,Q_1`, they are

\[
Q_0,\qquad Q_1\cup\{d\},\qquad M_1-d,M_2,\ldots,M_5.
\]

They are connected and pairwise adjacent: both shores are full to `B`, while
`d` supplies the missing adjacency between the two shore-derived branch sets.
Hence a `K_5` model in `G[B]` would give a `K_7` model in `G`.

Finally, Hadwiger's theorem for `t=5` gives `\chi(G[B])\le4`.  ∎

## 4. Trust boundary and conjectural classification

Theorem 1 does **not** classify the graphs `J` satisfying its second
condition.  The natural remaining conjecture is:

> If `J` is vertex-5-critical and `J-v` is `K_5`-minor-free for every
> `v\in V(J)`, then `J\cong K_2\vee C_{2r+1}` for some `r\ge1`.

This classification is not used in Corollary 3 and is not proved here.
An exact exploratory census of the authoritative edge-5-critical graph
catalogues through order eleven found only the displayed family (including
`K_5=K_2\vee C_3`).  That finite evidence is not an unbounded proof.
