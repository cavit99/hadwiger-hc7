# A degree-seven vertex lies in a `K_5` or forces `K_7^-`

**Status:** written proof on an experimental branch; not yet separately audited
or promoted.

Here `K_7^-` is `K_7` with one edge deleted.

## Theorem

Let `G` be a seven-contraction-critical graph with no `K_7^-` minor, and let
`v` be a vertex of degree seven.  Then `G[N(v)]` contains a `K_4`.
Consequently `v` belongs to a literal `K_5` subgraph of `G`.

## Proof

Put

\[
                         H=G[N(v)].
\]

Dirac's neighbourhood inequality for a seven-contraction-critical graph gives

\[
                         \alpha(H)\le2.                       \tag{1}
\]

Suppose for a contradiction that `H` is `K_4`-free.

### 1. An almost-dominating endpoint

We first prove that `H` has a nonuniversal vertex `a` of degree at least four.

Assume initially that `Delta(H)<=3`.  Then `F=overline H` is triangle-free by
(1) and has minimum degree at least three.  The graph `F` is bipartite.  An
elementary proof is as follows.  If `F` has a shortest odd cycle, it has order
five or seven.  An induced seven-cycle has no chord compatible with shortest
oddness, and hence has degree two, a contradiction.  If it has an induced
five-cycle, the two vertices outside the cycle have at most two neighbours
each on it because their cycle-neighbourhoods are independent.  The five
cycle vertices need at least five edges to the two outside vertices in total
to reach degree three, but at most four exist, again a contradiction.

Thus `F` is bipartite.  Its two parts have orders three and four, because
`delta(F)>=3`.  The four-vertex part is a `K_4` in `H`, contrary to our
assumption.  Therefore

\[
                         \Delta(H)\ge4.                       \tag{2}
\]

A universal vertex of `H` would also give a `K_4`: on the other six vertices,
Ramsey's equality `R(3,3)=6` gives either an independent triple, contrary to
(1), or a triangle, which together with the universal vertex is a `K_4`.
Hence a vertex `a` of maximum degree is nonuniversal.  Choose a nonneighbor
`b` of `a` and put

\[
                         U=N(v)-\{a,b\}.                       \tag{3}
\]

By (2), `a` is nonadjacent to at most one member of the five-set `U`.

### 2. The rooted `K_5`

The degree-seven anti-neighbourhood theorem applies: `G-N[v]` is nonempty and
connected.  The exact matching-language and rooted-model theorem can
therefore be applied to the boundary nonedge `ab`.  Since `G` has no
`K_7^-` minor, it has no `K_7` minor.  The theorem consequently gives five
pairwise disjoint connected pairwise adjacent branch sets

\[
                         (B_u:u\in U)                           \tag{4}
\]

in `G-v-\{a,b\}`, with `u\in B_u` for every `u\in U`.

Consider the seven branch sets

\[
                         \{v\},\quad\{a\},\quad(B_u:u\in U).   \tag{5}
\]

They are pairwise disjoint and connected.  The five rooted bags form a clique
model.  The singleton `{v}` is adjacent to `{a}` and to every `B_u`, through
the literal root `u`.  Finally `{a}` is adjacent to every `B_u` except
possibly the one whose root is the unique member of `U` nonadjacent to `a`.
Thus at most one of the twenty-one branch-set adjacencies in (5) is absent.
The sets in (5) form a `K_7^-` minor, a contradiction.

Therefore `H` contains a `K_4`, and adjoining `v` gives the asserted literal
`K_5`.  \(\square\)

## Dependencies and trust boundary

The proof uses:

1. Dirac's contraction-critical neighbourhood inequality;
2. the promoted connected degree-seven anti-neighbourhood theorem; and
3. the promoted uniform rooted-`K_5` theorem for any boundary nonedge.

The finite order-seven census on the same branch independently checks the
local almost-dominating statement on all `1,044` unlabelled seven-vertex
graphs, but it is not a logical dependency.
