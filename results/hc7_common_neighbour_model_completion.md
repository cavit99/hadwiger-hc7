# Completing a small clique-minor model at an adjacent pair

**Status:** written proof with a separate GREEN internal audit in
[`hc7_common_neighbour_model_completion_audit.md`](hc7_common_neighbour_model_completion_audit.md).
The theorem is a uniform rooted-model completion result.  Its `k=7`
corollary eliminates the case where the opposite open shore in the
mixed-shore support-six configuration consists of one vertex.  It does not
prove `HC_7`.

## 1. Common-neighbour completion

### Theorem 1.1 (uniform common-neighbour completion)

Let `k\ge3` be an integer.  Let `G` be a `k`-connected graph, let `a,b`
be adjacent vertices, and
let

\[
                 W\subseteq N_G(a)\cap N_G(b),
                 \qquad |W|\ge k.                    \tag{1.1}
\]

Suppose `G-{a,b}` contains a `K_{k-2}`-minor model whose support has order
at most `k-1`.  Then at least one of the following holds.

1. `G` contains a `K_k` minor.
2. `G` has an actual separation of order `k`.

Here an **actual separation** means a vertex separator whose deletion leaves
at least two nonempty components.

### Proof

Let the `k-2` branch sets of the `K_{k-2}`-minor model be

\[
                         M_1,\ldots,M_{k-2},
\]

and put

\[
                         m=\left|\bigcup_iM_i\right|\le k-1.   \tag{1.2}
\]

If every branch set meets `W`, then

\[
                         M_1,\ldots,M_{k-2},\{a\},\{b\}         \tag{1.3}
\]

are `k` pairwise adjacent connected branch sets.  Indeed, `a` and `b`
are adjacent, and each is adjacent to every `M_i` through a vertex of
`M_i\cap W`.  Thus (1.3) is a `K_k`-minor model.

Assume that some branch set does not meet `W`, and define

\[
       \mathcal I=\{i:M_i\cap W=\varnothing\},
       \qquad h=|\mathcal I|.                            \tag{1.4}
\]

Choose one vertex `c_i\in M_i` for every `i\in\mathcal I`, and put

\[
       A=\{c_i:i\in\mathcal I\},\qquad
       Z=\left(\bigcup_iM_i-A\right)\cup\{a,b\},\qquad
       T=W-\bigcup_iM_i.                                \tag{1.5}
\]

The sets `A,T,Z` are pairwise disjoint.  Moreover,

\[
                         |Z|=m-h+2.                     \tag{1.6}
\]

Every model vertex in `W` belongs to `\bigcup_iM_i-A`, because the selected
vertices in `A` lie in branch sets disjoint from `W`.  Hence

\[
                  |T|\ge |W|-(m-h)
                       \ge k-m+h
                       \ge h+1.                         \tag{1.7}
\]

We apply the set form of Menger's theorem in `G-Z`.  If there are not `h`
pairwise vertex-disjoint `A`--`T` paths, there is a set
`X\subseteq V(G)-Z` of order at most `h-1` separating `A` from `T` in
`G-Z`.  Since `|A|=h` and `|T|\ge h+1`, both `A-X` and `T-X` are nonempty.
Consequently `Z\cup X` is an actual vertex separator of `G`, and

\[
                  |Z\cup X|\le(m-h+2)+(h-1)=m+1\le k. \tag{1.8}
\]

`k`-connectivity excludes order less than `k`.  Thus equality holds in
(1.8), and `Z\cup X` is an actual separator of order `k`, giving
outcome 2.

It remains that `G-Z` contains `h` pairwise vertex-disjoint `A`--`T`
paths.  Since `|A|=h`, these paths start at the distinct selected vertices
`c_i`; their ends in `T` are also distinct.  Stop every path on its first
visit to `W`.  Its first vertex in `W` belongs to `T`, because every vertex
of `W` already used by the model lies in `Z`.  The resulting paths

\[
                         P_i:c_i\longrightarrow t_i
                         \quad(i\in\mathcal I)          \tag{1.9}
\]

are pairwise disjoint, meet the old model only at their initial vertices,
and have distinct ends `t_i\in T`.

For each `i\in\mathcal I`, enlarge `M_i` to `M_i\cup P_i`.  The `k-2`
enlarged branch sets remain connected, pairwise disjoint, and pairwise
adjacent.  Every one now meets `W`: the branch sets indexed outside
`\mathcal I` did so already, and the others contain their respective
vertices `t_i`.  Adding the two singleton branch sets `\{a\},\{b\}` now
gives the explicit `K_k`-minor model (1.3).  This is outcome 1. \(\square\)

### Remark 1.2 (sharp separator budget)

The proof is label-preserving: it only enlarges a branch set from the
given `K_{k-2}` model.  The possible order-`k` separator is not an artefact
of a loose estimate.  The two reserved adjacent vertices contribute two
vertices to `Z`, while failure of the `h`-path linkage contributes at most
`h-1`; for a support-`(k-1)` model the total budget is exactly `k`.

## 2. Elimination of a singleton opposite shore

### Corollary 2.1

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two components `U,V`, every vertex of `S` has
a neighbour in each component, and `s\in S` is adjacent to every vertex
of `S-\{s\}`.  Suppose additionally that

\[
       \text{for every two-vertex set }P,
       \quad G-P\text{ contains a `K_5`-minor model of support order at
       most six}.                                      \tag{2.1}
\]

If `V` consists of one vertex, then `G` has a `K_7` minor or an actual
separation of order seven.

### Proof

Write `V=\{v\}`.  Boundary fullness says that `v` is adjacent to every
vertex of `S`.  Therefore `vs\in E(G)` and

\[
                         S-\{s\}\subseteq N_G(v)\cap N_G(s),
                         \qquad |S-\{s\}|=7.           \tag{2.2}
\]

Apply (2.1) to the pair `\{v,s\}`.  The resulting support-at-most-six
`K_5`-minor model in `G-\{v,s\}`, together with (2.2), satisfies all
hypotheses of Theorem 1.1.  Its conclusion is exactly the asserted
alternative. \(\square\)

## 3. Application to the active endpoint-rigid configuration

The mixed-shore normalization in
[`hc7_boundary_anchored_model_completion.md`](hc7_boundary_anchored_model_completion.md)
assumes the global support-height-six bound (2.1).  Its endpoint-rigid
eight-vertex boundary has the required universal vertex `s`, and both open
shores are full to the boundary.  Consequently, in a `K_7`-minor-free host
with no actual order-seven separation, the opposite shore `V` in that
normalization is not a singleton.

This conclusion is independent of the three complementary-defect patterns
of the particular mixed-shore model.  The remaining problem begins only
when `V-v` is nonempty: one must then use the components of `V-v`, whose
boundary contacts are constrained by the companion component-contact
theorem.
