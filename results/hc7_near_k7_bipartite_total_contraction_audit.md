# Audit: bipartite total-contraction split states

## Verdict

**GREEN in the stated scope.**  This is an independent written re-audit of
`hc7_near_k7_bipartite_total_contraction.md` at SHA-256

```text
69044ccf85ccd3ec32ca118f11ddb1e673dade7fa7f7ac9d980b6b430ee5e228
```

The audit was completed on 2026-07-17.  The source proves the simultaneous
bilateral palette exposure, the resulting two-block state incompatibility,
its localization on the original boundary, the rooted path specialization,
and the stated conditional clique-model completion.  It does not prove
`HC_7`, and it does not align palette colours with arbitrary model bags.

## Revision checked

Theorem 3.1 now explicitly requires every carrier `D_beta` to be contained
in `G-X`.  This repairs the missing cross-disjointness hypothesis in the
previous revision: the `D_beta` are disjoint from both `X^-` and `X^+`, as
well as pairwise disjoint from one another.  No other mathematical change
from the previously audited source was used in reaching this verdict.

The adjacent legacy audit correctly identified the main list-colouring and
state-jump mechanisms, but did not pin a source hash or check the former
cross-disjointness omission.  This audit supersedes it for the exact source
hash above.

## 1. List lemmas

### Lemma 1.1

The common colour `a` makes every list nonempty.  If the total intersection
contained a second colour, alternating the two common colours would colour
the path, so the total intersection is exactly `{a}` and a one-vertex path
is impossible.

The prefix and suffix intersections defining `p` and `q` are well defined.
If `p<q`, any intervening edge has singleton intersection `{a}` on both
sides.  If `p=q`, the two end intervals can be alternated independently
around colour `a`.  If `p>q`, the left and right phases are independently
adjustable; when the secondary colours differ, three colours handle the
middle path with its two boundary exclusions, and when they coincide the
whole overlap alternates in the common two colours.  The empty-interval and
adjacent-end cases are included.  Thus every alternative to `p<q` gives the
forbidden list-colouring.

### Lemma 1.2

For an oriented tree edge, each side intersection contains `a`, so “rich”
really does supply a secondary colour.  If a vertex had no outgoing edge,
each branch of the spanning tree would share such a colour.  Colouring one
global bipartition class with `a` and the other branch-by-branch with the
chosen secondary colours is proper not only on the tree but also on every
extra edge of the bipartite graph: every such edge still crosses the fixed
global bipartition.

Hence every tree vertex has an outgoing edge.  Following outgoing arcs in a
finite tree can close only in a directed two-cycle on one tree edge.  Both
sides of that edge are therefore poor.  The sides are nonempty, connected
in the spanning tree, and adjacent through the deleted tree edge.  The
argument works for every selected spanning tree, not merely for a specially
chosen one.

## 2. Contraction and split results

### Lemma 2.1

Because `|X|>=2`, contraction reduces the vertex count and is a proper
minor, giving the upper bound `chi(G/X)<=q`.  In a hypothetical
`(q-s+1)`-colouring, every external neighbour of the contraction vertex
avoids its colour.  Reusing that colour on one class of an `s`-colouring of
`G[X]` and using at most `s-1` fresh colours on the remaining classes gives
a proper colouring of `G` with at most `q` colours, a contradiction.

For the endpoint `s=q+1`, the asserted lower bound is merely
`chi(G/X)>=1`, immediate because the contraction vertex exists; the lifting
argument is needed only when `q-s+1>=1`.  At `s=2`, the lower and
proper-minor upper bounds coincide, proving `chi(G/X)=q`.

The equality `chi(G/X)=eta(G/X)=q` is explicitly conditional on `HC_q` and
on the host having no `K_{q+1}` minor.  For the application `q=6`, `HC_6`
is established external input; it is not reproved here.

### Theorem 2.2

Fix the palette `Q` of the given `q`-colouring and put `a=c(z)`.  Every
outside neighbour of a vertex of `X` becomes adjacent to `z` after the total
contraction and therefore avoids `a`.  Thus each list

```text
L(x) = Q - c(N_G(x)-X)
```

contains `a`.  An `L`-colouring of `G[X]` would splice directly with
`c|_{G-X}` to give the forbidden `q`-colouring of `G`, so Lemma 1.2 applies
to the arbitrarily selected spanning tree.

For either returned shore, De Morgan's law gives

```text
intersection L(x) = Q - c(N_G(shores)-X) = {a}.
```

Taking the palette complement yields exposure to every colour other than
`a` on both shores in the same fixed exterior colouring.  The shores are
nonempty and connected in the tree and are adjacent through its selected
edge.  No connectivity of the ambient graph is needed beyond the explicit
connectedness of `G[X]`.

### Corollary 2.3

Minor-minimality supplies a `q`-colouring of every total contraction, and
Lemma 2.1 shows that every such colouring uses all `q` colours.  Hence
Theorem 2.2 applies without selecting a lower-palette or edge-dependent
state.  The statement about owner bags is a separate application of
Theorem 2.1 in the cited archived corridor note; it is not an input to the
abstract bilateral theorem.

### Corollary 2.4

The condition `|X|>=3` ensures that at least one of the two nonempty shores
has at least two vertices, so separately contracting the connected shores
produces a proper minor `G_2`.  Under the fixed exterior colouring, the
available palette for each contracted shore is its list intersection,
namely `{a}`.  The two contracted shore vertices are adjacent, so that
exterior state cannot extend.

Minor-minimality nevertheless supplies some `q`-colouring of `G_2`.  Exact
agreement with the old exterior is impossible; agreement up to a global
palette permutation is equally impossible because applying the inverse
permutation would give exact agreement.  Thus the claimed pair of
incompatible proper-minor states is genuine.

### Corollary 2.5

The boundary `S=N_G(X)` consists entirely of uncontracted original
vertices.  Equality of the two marked colour partitions on `S` induces a
bijection between the colours used there, and this bijection extends to a
global permutation of the `q`-colour palette.  After applying it, the
putative colouring of `G_2` agrees with `c` on `S`.

Use that colouring on the two contracted shore vertices together with `S`,
and use `c` on `G-X`.  There is no edge from either contracted shore to
`(G-X)-S`, by the definition of `S`, and the colourings agree on their
overlap.  They therefore splice to a colouring of `G_2` agreeing with `c`
on all of `G-X`, contradicting Corollary 2.4.  The later order-seven/eight
interpretation additionally uses the seven-connectivity and owner-bag
separation hypotheses of the cited corridor setting.

### Corollary 2.6

Nonadjacent roots have a shortest path of at least two edges in `G[D]`.
Any chord of that path would also lie in `G[D]` and shorten it, so the path
is induced in `G`.  It is connected and bipartite; Lemma 2.1 gives
`chi(G/P)=k-1`, and Theorem 2.2 applies to every `(k-1)`-colouring of the
total contraction.  Removing the returned path edge separates the two path
ends, so the shores contain the prescribed roots on opposite sides.  The
Hadwiger-number equality is again exactly conditional on `HC_{k-1}` and the
absence of a `K_k` minor in the host.

## 3. Clique-model completion

### Theorem 3.1

The repaired hypothesis `D_beta subseteq G-X` makes every carrier disjoint
from both shores.  Pairwise disjointness in the statement separates the
carriers from one another.  Theorem 2.2 supplies two nonempty, disjoint,
connected, adjacent shores; the hypotheses supply connected carriers, all
shore-to-carrier adjacencies, and all carrier-to-carrier adjacencies.
Consequently the displayed `2+(q-1)=q+1` sets are pairwise disjoint,
connected branch sets with an edge between every pair, hence an explicit
`K_{q+1}`-minor model.

The theorem remains conditional on already having the pairwise adjacent
exterior carriers.  The note expressly leaves their palette-to-label
construction open and does not infer connected carriers merely from colour
classes or individual palette witnesses.

## 4. Trust boundaries and residual scope

- `HC_q` is used only in the explicitly conditional Hadwiger-number
  equalities.  The `q=6` application uses the established `HC_6` theorem.
- The owner-bag exclusions and separator-order commentary depend on the
  cited archived constant-owner corridor result and its seven-connected
  host; they are not hidden hypotheses of Theorem 2.2.
- All state comparisons occur on original exterior vertices.  No quotient
  vertex is treated as an original boundary vertex.
- No finite computation is offered or needed for these written arguments.
- The palette-to-label exchange in Section 4 is clearly marked unproved.
  No unbounded theorem, `K_7` model, or `HC_7` conclusion is claimed from
  the bilateral palette exposure alone.

There are no unresolved mathematical assumptions or gaps within the stated
results at the pinned source revision.
