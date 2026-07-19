# Independent audit of the clique-star Kempe-separation dichotomy

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete contents of
[`hc7_clique_star_kempe_separation.md`](hc7_clique_star_kempe_separation.md) at
the following exact revision:

```text
c64df3af9619df6aa6408c11c223041557cda26b1009e4a80d65f26070b71e73  results/hc7_clique_star_kempe_separation.md
```

The GREEN audit was performed on the source revision
`8a186a2ab4007d2a7527173197e9a795b9c4c8b3e08f70a60bebf85fd1398ca5`.
The source was then moved from `active/` to `results/` and only its status
line was changed to link this audit.  Its theorem statement and proof are
unchanged; the displayed hash pins the promoted source.

The uniform theorem is valid for every `2 <= m <= q`, including `m=2`
and `m=q`.  The separator corollary and both dense degree-eight
specializations are also valid under their stated hypotheses.  The audit
does not promote the separate dense-alternative input or claim that either
residue completes `HC_7`.

## 1. Response classes and the normalized Kempe transition

Because `A` is a clique, its `m` vertices have pairwise distinct colours
in every proper colouring of `H`.  Hypothesis (1) therefore makes the
classes `C_i` disjoint and exhaustive.  Since `H` is `q`-colourable, at
least one class is nonempty.  The proof does not require every class to be
nonempty.

Suppose that one Kempe interchange takes `c in C_i` to `c' in C_j`, with
`i != j`, and let `Q` be the switched two-colour component.  There are two
cases.

1. If `v in Q`, the colour of `v` changes.  The new matching vertex `a_j`
   cannot belong to `Q`: if it did, its old colour would be the second
   switched colour and it would change in the opposite direction from
   `v`.  Thus the two switched colours are
   `gamma_i=c(v)=c(a_i)` and `gamma_j=c(a_j)`.  The edge `a_i a_j` puts
   `a_i` in the same two-colour component as `a_j`, so neither is in `Q`.
   Here the normalized component `K` is `Q`.
2. If `v notin Q`, its colour remains `gamma_i`.  Moving the unique match
   from `a_i` to `a_j` forces both `a_i` and `a_j` to be switched, and the
   edge between them puts them in the same component `Q`.  Again the two
   colours are exactly `gamma_i,gamma_j`.  The component `K` containing
   `v` is distinct from `Q`; switching `K` instead fixes all of `A` and
   changes `v` from `gamma_i` to `gamma_j`.

In either case, `a_i,a_j` lie in the other two-colour component, while
every `a_r` with `r notin {i,j}` has a colour outside the switched pair.
Thus `K` avoids all of `A`.  This also checks the edge cases `m=2` and
`m=q`: no unused palette colour is being assumed.

The only edges deleted in passing from `G` to `H` are the edges `va_r`.
They do not affect the validity of the Kempe interchange in `H`.  The
presence of all of them in `G`, together with `v in K` and `K cap A` empty,
gives `A subseteq N_G(K)`, including the vertices whose colours are not in
the switched pair.  Since the two colourings differ only on `K`, they agree
pointwise on the open neighbourhood `N_G(K)`.  No additional deleted star
edge creates an omitted transition case.

## 2. The Kempe-separated component

Fix `c in C_i` and suppose that no two response classes are Kempe-adjacent.
For each `j != i`, the edge `a_i a_j` puts those two vertices in one
`gamma_i,gamma_j` component.  If the component containing `v` were
different, switching it would fix `A`, change `v` from `gamma_i` to
`gamma_j`, and hence give a colouring in `C_j`.  That is precisely a
forbidden response adjacency.  Therefore `v,a_i,a_j` lie in one
two-colour component for every `j`.

All these two-colour components lie in the component `D` containing `v` of
the subgraph induced by `Gamma=c(A)`.  Hence **every** clique vertex lies
in `D`; the argument does not assume in advance that its response class is
nonempty.  The classes remain exhaustive because every proper colouring
belongs to its unique response class, so this proves the claimed statement
for every proper colouring of `H`.

The exact chromatic conclusion is also sound.  The graph `H[D]` is
connected by definition, so `G[D]` is connected.  Restoring the star gives
the clique `A union {v}` of order `m+1`, proving the lower bound.  On
`D-v`, the colouring `c` uses only the `m` colours in `Gamma`, and `G[D-v]`
has no edge absent from `H[D-v]`.  Giving `v` one fresh colour proves the
upper bound.  Thus

```text
chi(G[D]) = m+1
```

also when `m=q`; the fresh colour is used only for this chromatic upper
bound and need not belong to the original `q`-colour palette.

The transition and Kempe-separated alternatives are mutually exclusive and
exhaustive: some pair of response classes is Kempe-adjacent, or none is.

## 3. Literal separation statements

For either connected set `Y=K` or `Y=D`, the sets `Y` and
`G-N_G[Y]` are anticomplete.  When the latter is nonempty, they are the two
nonempty open sides of a separation with boundary exactly `N_G(Y)`.  In
the transition branch, both colourings are unchanged off `K`, so their
restrictions to that literal boundary are identical.  A `k`-connected
host therefore makes either boundary have order at least `k`.

The source correctly does not infer that the boundary has order exactly
seven or that separately obtained closed-shore colourings glue.

## 4. Entry into the dense degree-eight specialization

The specialization uses the separately promoted deficient-singleton
joint-persistence theorem at the following current audited revision:

```text
2f413fa679fc7366920b9adbd1cdc9c419e7f2ff26c871ba8757ce2d8510c409  results/hc7_deficient_singleton_joint_persistence.md
8accece292df8c27a3d2a5e3086e01e499ffe47669d7fd9edb56926cb0b471fc  results/hc7_deficient_singleton_joint_persistence_audit.md
```

For `t=7` and `d_G(x)=8`, its exact capacity formula gives a maximum
simultaneously model-preserving incident-edge deletion of order
`8-(7-2)=3`.  Every pair contained in that triple also preserves the same
model.  Under the dense alternative, the three distinct outer endpoints
are consequently pairwise adjacent, so they induce the required triangle.

The graph `H` obtained by deleting the three star edges is a proper minor
and is six-colourable.  In any such colouring, the three outer vertices
have distinct colours.  The colour of `x` can therefore match at most one
of them.  If it matched none, restoring all three edges would six-colour
`G`; hence it matches exactly one.

Every one of the three response classes is nonempty.  Colour the proper
minor `G/xa_i` with six colours and expand the contracted vertex.  This
gives a colouring of `G-xa_i` in which `x` and `a_i` agree.  The other two
star edges remain present, so `x` disagrees with their outer endpoints.
Restricting to `H` gives exactly the `i`-th response.  This verifies all
hypotheses of Theorem 1 with `q=6` and `m=3`.

## 5. Dominating and non-dominating conclusions

In the transition branch, `K` avoids all three outer endpoints.  Therefore
none of the restored star edges has both ends in `K`, and
`G[K]=H[K]`.  It is a connected bipartite graph.  If `K` is not dominating,
Section 3 gives an actual separator of order at least seven and the common
boundary colouring.

If `K` is dominating and `G-K` had a `K_6`-minor model, the connected set
`K` would be disjoint from its six branch sets and adjacent to every one of
them, producing a `K_7`-minor model in `G`.  Thus `G-K` is `K_6`-minor-free
and is five-colourable by the established `t=6` case of Hadwiger's
conjecture.  A four-colouring of `G-K`, together with a disjoint two-colour
palette on `K`, would six-colour `G`.  Hence `chi(G-K)=5` exactly.

In the Kempe-separated branch, the uniform theorem gives a connected
four-chromatic `G[D]`.  The non-dominating separator conclusion is the same.
If `D` is dominating, a `K_6` minor in `G-D` would again combine with `D` to
give a `K_7` minor.  Hence `G-D` is five-colourable.  If it were
two-colourable (including the cases of chromatic number zero or one),
disjoint palettes of orders four and two would six-colour `G`.  Consequently
`3 <= chi(G-D) <= 5`.

All branch sets used in these complement arguments are disjoint, and
domination supplies an edge from the new connected branch set to each old
minor branch set.  No stronger connectivity than the stated
seven-connectivity is used.

## 6. Editorial revision and trust boundary

The current revision makes explicit that Corollary 3 assumes a spanning
labelled `K_7^-`-minor model.  It also replaces the former project shorthand
“lock” by the standard-language description “Kempe-separated component.”
These edits change neither a hypothesis nor a conclusion.  The seven branch
sets still have every required pair adjacent except one, and the
deficient-singleton hypothesis identifies one endpoint of that missing
adjacency as `{x}`.  The complete proof was replayed after these edits; all
arguments audited in Sections 1--5 are unchanged.

No unresolved mathematical gap was found in Theorem 1, Corollary 2, or the
dense degree-eight implication under that standard reading.  In particular,
the source does not claim colour-to-branch-set label identification, an
exact order-seven separator, a common colouring of independently coloured
closed shores, or a proof of `HC_7`.
