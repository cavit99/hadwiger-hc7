# Independent audit: two-apex exclusion for disjoint small models

**Verdict:** **GREEN.**  The connectivity reduction, apex-allocation
argument, `K_6^-` case split, path contraction, and Wagner consequence are
all correct.  The theorem excludes a two-apex outcome under its disjoint
support hypothesis; it neither produces the two-apex set nor proves a
`K_7` minor.

**Audited source:**
[`hc7_disjoint_k6minus_k5model_two_apex_exclusion.md`](hc7_disjoint_k6minus_k5model_two_apex_exclusion.md).

**Source SHA-256:**
`5247b6eafa6be34e5fb9f514c98c9b7bf7cd8018e08a4dc5ced38879bad50ee5`.

## 1. Connectivity after deleting the apex pair

Let `Z` have order two and put `P=G-Z`.  If a set of at most four vertices
separated `P`, adjoining `Z` would give a separator of `G` of order at most
six.  Seven-connectivity therefore gives `kappa(P)>=5`.  The order
convention causes no exception: a seven-connected graph has at least eight
vertices, so `P` has at least six vertices.

## 2. Allocation of the two apex vertices

The support of the `K_5` model must meet `Z`, because otherwise it would
be a `K_5` minor in the planar graph `P`.  The displayed `K_6^-` must also
meet `Z`: deleting either endpoint of its unique missing edge leaves a
literal `K_5`, so `K_6^-` is nonplanar.

The two supports are vertex-disjoint and `Z` has only two vertices.  Since
each support contains at least one of them, each support contains exactly
one.  This justifies the unique vertex

\[
                       r\in V(K)\cap Z.
\]

No assumption about which branch set of the separate `K_5` model contains
the other vertex of `Z` is required later.

## 3. The three locations of the apex in `K_6^-`

Write `V(K)=X dotcup {p,q}`, where `X` is a four-clique, both `p,q` are
complete to `X`, and `pq` is absent.

If `r=p`, then `X union {q}` is a literal `K_5` wholly contained in `P`,
contradicting planarity.  The case `r=q` is symmetric.

Suppose `r in X` and put `T=X-{r}`.  The graph `P` contains the triangle
`T` and both `p,q` are complete to it.  Since `P` is five-connected,
`P-T` is connected and contains a `p`--`q` path
`R=p=v_0,v_1,...,v_k=q`.  Take the three vertices of `T` as singleton
branch sets, take `{v_0,...,v_{k-1}}` as a fourth branch set, and take
`{q}` as the fifth.  The fourth bag is connected and meets the fifth
through `v_{k-1}q`; it meets every vertex of `T` through the edges from
`p`, while `{q}` meets every vertex of `T` through the edges from `q`.
Equivalently, contract the initial segment of `R` into `p` and retain its
last edge.

This is a `K_5` minor in the planar graph `P`, a contradiction.  The proof
therefore exhausts every possible location of `r`.

## 4. Fixed-pair corollary and Wagner input

If `G-Z` is `K_5`-minor-free, the same separator count makes it
five-connected and hence four-connected.  Wagner's four-connected form
states that every four-connected `K_5`-minor-free graph is planar.  Theorem
1.1 then applies and gives the claimed contradiction.

This exact Wagner consequence has already been checked in the audit of
[`../results/hc7_global_topological_k5_pair_height.md`](../results/hc7_global_topological_k5_pair_height.md):
for a five-connected remainder, `K_5`-minor-freeness and planarity are
equivalent.

## 5. Exact trust boundary

The theorem uses only seven-connectivity, a two-vertex planarizing set,
and the two vertex-disjoint supports.  It does not use contraction
criticality or `K_7`-minor-freeness.  Its special six-vertex-model sentence
is immediate because that configuration is one instance of a `K_5` model
with support disjoint from the `K_6^-` support.

The corollary proves that no fixed pair whose deletion is `K_5`-minor-free
can coexist with the two disjoint supports.  It does not prove that such
a fixed pair exists, nor does it transform the supports into a `K_7`
minor.  The source records this limitation correctly.
