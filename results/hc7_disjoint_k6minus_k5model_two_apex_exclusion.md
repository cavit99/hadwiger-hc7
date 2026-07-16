# Two-apex exclusion for disjoint `K_6^-` and `K_5` models

**Status:** written proof; independently audited in
[`hc7_disjoint_k6minus_k5model_two_apex_exclusion_audit.md`](hc7_disjoint_k6minus_k5model_two_apex_exclusion_audit.md).

This note eliminates the standard two-apex family from the current
support-six configuration.  It does not prove that every seven-connected
`K_7`-minor-free graph is two-apex.

## 1. Statement

### Theorem 1.1

Let `G` be a seven-connected graph.  Suppose that a two-vertex set `Z`
makes `G-Z` planar.  Then `G` cannot contain both of the following with
vertex-disjoint supports:

1. six vertices inducing a subgraph `K` isomorphic to `K_6^-`; and
2. a `K_5`-minor model `M`.

In particular, this excludes the case in which `M` has six support
vertices, four singleton branch sets forming a `K_4`, and one two-vertex
edge branch set.

### Proof

Put `P=G-Z`.  Deleting two vertices lowers vertex connectivity by at most
two, so

\[
                              \kappa(P)\ge5.          \tag{1.1}
\]

The support of `M` meets `Z`, since otherwise the planar graph `P` would
contain a `K_5` minor.  The subgraph `K` also meets `Z`, since `K_6^-` is
nonplanar.  The two supports are disjoint and `|Z|=2`; consequently each
support contains exactly one vertex of `Z`.

Write

\[
             V(K)=X\mathbin{\dot\cup}\{p,q\},
             \qquad |X|=4,
\]

where `X` is a clique, both `p` and `q` are complete to `X`, and `pq` is
the unique missing edge.  Let `r` be the unique vertex of
\(V(K)\cap Z\).

If `r=p`, then \(X\cup\{q\}\) is a `K_5` subgraph of `P`, a
contradiction.  The case `r=q` is symmetric.

It remains that \(r\in X\).  Put \(T=X-\{r\}\).  Then `T` is a triangle in `P`,
and both `p` and `q` are complete to `T`.  By (1.1), the graph `P-T` is
connected, so it has a `p`--`q` path `R` avoiding `T`.  Contracting all
but one edge of `R` produces the missing adjacency `pq`; together with
the triangle `T` and the six edges from `{p,q}` to `T`, this gives a
`K_5` minor in `P`.  This again contradicts planarity.

All possible locations of `r` are impossible, proving the theorem.
\(\square\)

## 2. Fixed-pair consequence

### Corollary 2.1

Let `G` be seven-connected and contain vertex-disjoint supports of a
`K_6^-` subgraph and a `K_5`-minor model.  There is no two-set `Z` for
which `G-Z` is `K_5`-minor-free.

### Proof

As above, `G-Z` is five-connected.  The standard four-connected
consequence of Wagner's characterization says that every
four-connected `K_5`-minor-free graph is planar.  Theorem 1.1 now gives a
contradiction.  \(\square\)

Thus, in the current rigid literal-arm configuration, either of the two
usual terminal conclusions already closes the case:

- an explicit `K_7`-minor model; or
- a fixed pair `Z` such that `G-Z` is `K_5`-minor-free.

The theorem does not supply either conclusion.  It only proves that the
second conclusion is incompatible with the two disjoint supports already
present in this configuration.
