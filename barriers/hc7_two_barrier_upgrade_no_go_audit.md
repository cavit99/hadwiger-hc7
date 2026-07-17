# Independent audit: limitations of the two sharp barrier families

**Verdict:** **GREEN — separate internal audit.**

This audit checked the barrier revision with SHA-256

```text
5bdd1aae69210a0273e3dcd27d5ccc6c416a48349ce38dc0615588483e3bb1c3
```

for
[`hc7_two_barrier_upgrade_no_go.md`](hc7_two_barrier_upgrade_no_go.md).
This is an internal mathematical audit, not external peer review.

The promoted source has SHA-256
`0206c365fbd761648080e758c60a75bd8188d1f1f07d3a632f9cad9052e4e1cd`.
It differs from the audited revision only in the opening status line, which
records this GREEN verdict; no mathematical or scope claim changed.

## Checks performed

### 1. The complete-join barrier

1. If deleting a set `P` of at most two vertices leaves no `K_5` minor,
   the established `t=5` case of Hadwiger gives a four-colouring of
   `G-P`; two fresh colours extend it to a six-colouring of `G`.
2. In the capped-antiprism construction `G_n=K_2\vee H_n`, deleting the
   complete factor leaves the planar graph `H_n`.  Planarity is
   minor-closed and `K_5` is nonplanar, so those two vertices meet every
   `K_5`-minor model.
3. The cited and audited identity

   \[
             \eta(K_2\vee H)=2+\eta(H)
   \]

   also gives the stated general conclusion: if the join is
   `K_7`-minor-free, then `H` is `K_5`-minor-free and the join is
   six-colourable.  Hence retaining the two-vertex transversal is already
   incompatible with seven-chromaticity.

### 2. The false-twin amplification

1. The displayed branch sets in `K_{m,m}` number `(m-1)+2=m+1`, are
   disjoint and connected, and every two are adjacent.  The proof remains
   valid for `m=1`, when the two singleton branch sets form `K_2`.
   Therefore `K_{m,m}` contains a `K_{m+1}` minor.
2. If nonadjacent vertices `u,v` have the same open neighbourhood, every
   colouring of `G-u` extends to `u` by giving it the colour of `v`.
   Consequently a vertex-critical graph has no such false-twin pair.
3. The cited connected-full realization contains an open-shore edge, and
   the order-seven false-twin amplification replaces its endpoints by two
   independent classes complete to one another.  It therefore contains a
   fixed `K_{7,7}`, hence a `K_8` minor and, after discarding one branch
   set, a `K_7` minor.
4. If the amplified graph has chromatic number seven and `u,v` are two
   members of one false-twin class, then `chi(G-u)=7`: a six-colouring of
   `G-u` would extend to `u` with the colour of `v`.  Thus the named vertex
   deletion directly contradicts the requirement that every proper minor
   be six-colourable.

### 3. Full minor-criticality

A seven-connected graph has at least eight vertices and is therefore not
`K_7`.  If such a graph contained a `K_7` minor, the resulting `K_7` would
be a proper minor with chromatic number seven.  Hence the simultaneous
hypotheses `chi(G)=7` and “every proper minor is six-colourable” correctly
imply global `K_7`-minor exclusion in the stated seven-connected setting.

## Dependency and scope checks

The capped-antiprism facts used here are confined to its audited complete-
join and separator-excess results.  The amplified boundary-state facts are
confined to the separately audited `K_{3,5}` realization: seven-
connectivity, seven-chromaticity, the specified proper-minor responses,
the fixed `K_{7,7}`, and the absence of a two-vertex `K_5`-model
transversal.

The strategic conclusion has the correct scope.  Neither construction is
a counterexample to `HC_7`, and the note does not claim that arbitrary
boundary-state realizers must use false twins or contain a large complete
bipartite graph.  It proves only that these two particular architectures
cannot be upgraded while retaining, respectively, the two-vertex
transversal or the false-twin amplification.
