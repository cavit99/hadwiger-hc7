# Audit of the augmented path-span exchange

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_augmented_path_span_exchange.md`

**Audited SHA-256:**
`2e0802c286a1fdca7ed60b0b7708ef0f5c2c08641ba37e05f6bda19d1df3aaa6`

**Promoted source SHA-256:**
`515380046e7a02f163e78ccbd711c502a8a7a017712854632f1cfd2630063915`

The promoted revision changes only the status line and adds this audit link;
the theorem statements, proofs, dependencies, and trust boundary audited
below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Lemma 2.1: the four contracted sets

Consider the representative `Pi_A` case in which `K` meets every vertex of
`Q_r(D)`.  The four sets

```text
K union D,   P_2 union E,   V(P'_z),   {r}
```

are pairwise disjoint.  The first is connected because `K` is connected and
has a neighbour at every member of the nonempty independent set `D`; the
second is connected because the boundary-full connected subgraph `P_2`
has a neighbour at every member of `E`; and the third is the path `P'`
after its first endpoint `r` is deleted.

All six clique adjacencies are literal:

1. `K union D`--`V(P'_z)` is the assumed edge from `K` to the internal
   part of `P'`;
2. `P_2 union E`--`V(P'_z)` is a `P_2`--`z` edge;
3. `K union D`--`P_2 union E` is a `P_2`--`D` edge;
4. `{r}`--`V(P'_z)` is the first edge of `P'`;
5. `{r}`--`P_2 union E` is a `P_2`--`r` edge; and
6. `{r}`--`K union D` is either an `r`--`D` edge or, precisely when none
   exists, the required `K`--`r` edge encoded by `r in Q_r(D)`.

Each nonsingleton set contains an edge, so simultaneous contraction gives a
proper minor with a `K_4` on the four images.  The other three required
contact sets follow by interchanging `D,E` and/or `r,z`; the same six-edge
check is invariant under those symmetries.

## Pullback and exactness for `Pi_A`

The four contraction images contain, respectively, the complete boundary
blocks `D,E,{z},{r}`.  Their `K_4` forces four distinct colours.  On
restricting a six-colouring of the minor to the untouched closed `B`-shore,
expand only the boundary vertices of each image.  Every edge from `B` to a
contracted boundary block was represented by an edge to its image, and all
four boundary blocks are independent under the selected exact partition.
The pullback is therefore proper and induces exactly `Pi_A`, not merely a
coarsening.  It aligns with the selected colouring on the closed `A`-shore.

## The three contracted sets for `Pi_B`

In the representative case where `K` meets all of `D`, the sets

```text
K union D,   P_2 union E,   V(P')
```

are disjoint, connected, and pairwise adjacent.  Their three literal edges
are supplied by the assumed `K`--path edge, a `P_2`--`r` (or `z`) edge, and
a `P_2`--`D` edge.  Their images form a triangle and contain the independent
blocks `D,E,{r,z}`.  The same restriction-and-pullback argument produces
the exact partition `Pi_B`.  The case in which `K` meets all of `E` is
symmetric.

## Theorem 3.1: whole-shore off-path components

The open path segment `I` is nonempty and connected.  Every off-path
component included in `K` has an edge to `I`, so their union with `I`
induces a connected subgraph.  Because these are components of the whole
induced graph `G[A-(V(P) union V(P_2))]`, an ambient connector joining
several pieces formerly lying in `P_1-V(P)` is automatically contained in
one such component; the proof does not assume that all connectors lie in
`P_1`.

Rerouting through `R_0` removes every vertex of `I` from the path.  The
detour interior lies entirely in `R_0`, which is excluded from `K`; every
other included off-path component is vertex-disjoint from `R_0`.  Hence the
rerouted path `P'` and `K` are vertex-disjoint.

Both remain disjoint from `P_2` by construction: the original path avoids
`P_2`, and every off-path component—including `R_0`—is a component of a
graph from which `V(P_2)` was deleted.  Finally, the path edges
`p_i p_{i+1}` and `p_{j-1}p_j` give literal edges from `K` to internal
vertices of `P'`.  Thus every hypothesis of Lemma 2.1 holds.  A chord
detour is the same argument with empty detour interior and no consumed
off-path component.

## Trust boundary

The result may combine arbitrarily many off-path components and ambient
connectors, and so is unbounded.  It does not prove existence of a
qualifying detour or that any augmented span attains a required contact
set.  Failure of all displayed exchanges is not promoted to a separator or
descent.  No palette colour is identified with a literal boundary label.

Within this scope, no gap was found.
