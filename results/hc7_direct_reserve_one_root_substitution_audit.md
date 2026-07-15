# Independent audit: direct-reserve one-root substitution

**Verdict:** GREEN.

**Audited source:** `results/hc7_direct_reserve_one_root_substitution.md`

**Source SHA-256:**
`d5d12fd1003504ce55928d4ed704fcb0cc24980bd730f21e80765e03320e406d`

## 1. Direct-edge mask parity

The ends of a bad path belong to the two opposite demand sets, so their
orientation demands differ. For a forced endpoint `v`, the demand is

\[
\theta(v)=c(v)\mathbin{\mathsf{xor}}p(v).
\]

If `xy` is a literal edge of the bipartite boundary, then
`p(x) xor p(y)=1`. Consequently

\[
\theta(x)\ne\theta(y)
\quad\Longleftrightarrow\quad
c(x)=c(y).
\]

Both endpoints are forced because the bad-path terminal sets consist of
singleton-list vertices. The canonical lists contain only one vertex with
singleton `{0}`, namely `u`, so two distinct forced endpoints with the same
label cannot both have label zero. Thus both have singleton `{1}`. They
belong to `W`, and the equivalence

\[
0\in\Lambda(w)\Longleftrightarrow zw\in E(G)
\]

then gives `zx,zy notin E(G)`. Lemma 1 is exact.

The companion mask probe was rerun independently and reported

```text
DIRECT_RESERVE_MASKS pairs 2636 violations 0
```

This agrees with, but is not needed for, the uniform parity proof.

## 2. Existence of the retained root

The endpoint set `Q` has four distinct vertices. At most one boundary
vertex is `u`, while `x,y` are already distinct vertices of `W`. Of the two
remaining members of `Q`, at least one therefore lies in `W`. Hence a choice

\[
r\in (Q\cap W)-\{x,y\}
\]

always exists and is distinct from `x,y`.

## 3. Reoriented literal seven-separation

With

\[
A'=A-\{z\},\qquad S'=W\cup\{z\},\qquad R'=R\cup\{u\},
\]

the three sets are pairwise disjoint and partition `V(G)`. The boundary has
order seven because `|W|=6` and `z` was an open-shore vertex. Both open
shores are nonempty: `|A'|>=2`, and the original `R` is nonempty.

There is no `A'-R'` edge. Old `A-R` edges are absent, and the hypothesis
that `zu` is the unique `A-u` edge excludes every `A'-u` edge. The edge
`zu` now runs from the boundary to the right shore and causes no problem.

Thus this is an actual seven-separation to which the audited closed-shore
rooted-connectivity theorem applies.

## 4. Rooted-diamond theorem

The set

\[
Q'=\{z,x,y,r\}
\]

has four distinct vertices and is contained in `S'`. Closed-shore rooted
connectivity makes

\[
\bigl(G[A'\cup Q'],Q'\bigr)
\]

internally four-connected. Since `|A'|>=2`, its host graph has at least six
vertices. These are precisely the relevant hypotheses of Jorgensen's
rooted-diamond theorem as recorded in Norin--Totschnig Lemma 10. Hence the
host contains the asserted `Q'`-rooted `K_4^-` model.

## 5. Avoidance and exact scope

The host vertex set is

\[
(A-\{z\})\cup\{z,x,y,r\}.
\]

It excludes `u`, because `x,y,r` lie in `W`, and it excludes the unique
fourth original root in `Q-\{x,y,r\}`. Every regenerated branch set is a
subgraph of this host, so the avoidance is literal, not merely a choice of
labels. If the omitted original root happens to be `u`, the two avoidance
descriptions refer to the same vertex, which is harmless.

The result regenerates a labelled rooted diamond after replacing one
original root by `z`. It does not identify the diamond's missing pair,
repair it, or compose two regenerated models. Those limitations are stated
correctly in the source.
