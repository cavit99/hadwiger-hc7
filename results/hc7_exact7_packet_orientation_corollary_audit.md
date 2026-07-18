# Independent audit: exact-seven orientation by full connected subgraphs

## Verdict

**GREEN** at the exact source revision

```text
4f857d8cdecc7b885610fc9f528d8ca4e71c0b42a20f89a45d20d3a667db2ee8  results/hc7_exact7_packet_orientation_corollary.md
```

Corollary 2.1 correctly reduces to the two-full-subgraph Kempe-compression
theorem; no edge between the two open-shore subgraphs is required because
their boundary-block enlargements are automatically adjacent.  The
high-demand partition classification and both Kempe orientations are
exhaustive.  Theorem 3.1 correctly removes the
former three-connectivity hypothesis: a cutvertex gives one of the first two
outcomes, while two-connectivity is exactly enough for the remaining
single-vertex deletion arguments and the unrestricted Two Paths theorem.
No unresolved mathematical assumption remains in these conditional results.

## 1. Setup and terminology

The displayed decomposition has two nonempty open sides and no edge between
them.  Consequently, once `G[A]` is shown connected in Theorem 3.1, it is a
literal component of `G-S`, and the nonempty set `B` supplies the opposite
side required by every separation argument.

The demand definition agrees with the exact packet-reflection lemma: a
maximum clique among singleton boundary blocks may remain literal, and one
boundary-full connected subgraph is used for each remaining block.  Every
partition considered below is induced by a proper colouring and therefore
has independent blocks.

## 2. Why adjacency of the two open-shore subgraphs is unnecessary

Start with disjoint connected subgraphs `C_D,C_E` in `A`, each adjacent to
every vertex of `S`.  The compression proof uses the enlarged connected sets

```text
K_D=C_D union D,    K_E=C_E union E.
```

They are disjoint because `C_D,C_E` are disjoint and lie outside `S`, while
`D,E` are disjoint subsets of `S`.  They are connected by boundary fullness.
They are automatically adjacent even if `C_D,C_E` themselves are not:
`C_D` has a literal edge to every vertex of the nonempty set `E`, and
`E subseteq K_E`.  Therefore the adjacency-free canonical compression
theorem applies at source hash

```text
f1b25b93fefdd1775d0a105ea6cdd67bfcecfe3416642550405aed85f0fd7cc3.
```

This also shows that connectedness of the whole open side `G[A]` is irrelevant
to Corollary 2.1.  The two initially chosen subgraphs retain their literal
identities throughout.

## 3. Complete partition-demand classification

Let `Pi` be the complete equality partition induced by `c` on `S`.  The
monochromatic sets `D,E` belong to distinct blocks.  Since only `r,z` remain,
there are at most four blocks.

If either `r` or `z` joins the `D`- or `E`-block, then there are at most three
blocks.  In the only potentially tight three-block case, the other displayed
vertex is a singleton, so

```text
d_{G[S]}(Pi) <= 3-1 = 2.
```

Exact packet reflection through the two named connected subgraphs therefore
returns the same complete partition on the opposite closed side, and the two
colourings glue after a permutation of the six colours.

If neither displayed vertex joins the first two blocks, exactly two
partitions remain:

```text
Pi_A = D | E | {r} | {z},
Pi_B = D | E | {r,z}.
```

For `Pi_A`, the singleton graph is the graph induced by `r,z`; hence its
demand is three exactly when `rz` is absent, and is two when `rz` is present.
For `Pi_B`, there are three blocks and no singleton block, so its demand is
three.  This proves that the two displayed exceptional partitions are the
complete high-demand list.

## 4. Four-block Kempe orientation

Assume the original partition is `Pi_A` and `rz` is absent.  Contracting
spanning trees in

```text
C_D union D,    C_E union E
```

produces adjacent representatives, each adjacent to `r,z`.  Any six-colouring
of this proper minor therefore returns exactly `Pi_A` or `Pi_B` on the
untouched closed side.  A returned `Pi_A` glues immediately.

If `Pi_B` is returned, let `gamma=c(r)` and `eta=c(z)`.  These colours occur
on the original boundary only at `r,z`.  If the `gamma,eta` Kempe component
containing `r` omitted `z`, a switch on that component would change only `r`
on the boundary, create `Pi_B`, and glue.  Thus the component contains an
`r-z` path, and all internal vertices of that path lie in `A`.

If such a path avoided both named full connected subgraphs, splitting it at
one edge would give two adjacent connected path parts containing `r,z`.
Together with `C_D union D` and `C_E union E`, these are four disjoint,
pairwise adjacent connected sets.  Their contraction forces exact partition
`Pi_A` on the opposite closed side, again giving a gluing contradiction.
Hence every such path meets the named pair, as asserted.

## 5. Three-block Kempe orientation

Assume the original partition is `Pi_B`, and write
`kappa=c(r)=c(z)`.  A returned `Pi_B` glues immediately, so the only surviving
return is `Pi_A`.  The original boundary uses exactly three colours, leaving
three palette colours absent.  Choose one such colour `theta`.  The returned
four block colours can be permuted so that its `D`- and `E`-colours match the
original ones, `z` receives `kappa`, and `r` receives `theta`; these four
target colours are distinct.

In the original colouring, `theta` is absent from all of `S`, while `kappa`
occurs there exactly at `r,z`.  If the `kappa,theta` component containing `r`
omitted `z`, switching it would change only `r` on the boundary and make the
two shore colourings agree vertex by vertex.  Therefore it contains `z`, and
every connecting path has all internal vertices in `A`.

If one such path avoided the named pair, the three connected sets

```text
C_D union D,    C_E union E,    V(P)
```

would be disjoint and pairwise adjacent.  Contracting them forces the exact
three-block partition `Pi_B` on the untouched side, which glues.  Thus every
such path meets the same named union.  This is the required boundary-absent
Kempe orientation; no path in the opposite shore is inferred.

## 6. Connectedness and the cutvertex reduction in Theorem 3.1

Every component `K` of `G[A]` has neighbourhood contained in the seven-set
`S`.  That neighbourhood separates `K` from the nonempty opposite side `B`,
so seven-connectivity forces `N_G(K)=S`.  Hence every component is
boundary-full.  Full-subgraph packing number one then forces `G[A]` to be
connected.

If `|A|<=2`, this connected nonempty set is itself boundary-full, so
`N_G(A)=S`; the nonempty opposite side makes `S` an actual nontrivial
order-seven separation.  The proof therefore reaches outcome 1 before using
the convention that a connected graph of order at least three with no
cutvertex is two-connected.

If `G[A]` has a cutvertex, the separately audited cutvertex theorem at source
hash

```text
b6205cae0d5ee6fe25a7258b3b8e3aa1894ce97d0fa348cef2c06935f5c24d87
```

gives either a literal order-seven separation or the required repair support
and disjoint residual boundary-full connected subgraph.  Thus the remaining
argument may validly assume only that `G[A]` is two-connected.

## 7. Contact transversals in the two-connected remainder

If a one-vertex transversal `{p}` exists, then `{p}` itself is a connected
boundary-full subgraph.  When `p` is a unique portal for some boundary vertex
`s`, two-connectivity makes `A-p` connected and its neighbourhood is contained
in the seven-set `{p} union (S-{s})`; seven-connectivity forces equality.
Otherwise every boundary vertex has a portal outside `p`.  Connectedness of
`A-p` gives a path from a `b`-portal to an `I`-portal, disjoint from the
boundary-full singleton `{p}`.

Now let `W={p,q}` be inclusion-minimal.  A unique portal again yields the
same order-seven separation after deleting that portal.  If one vertex of
`A` sees both `b` and a member of `I`, that singleton is a repair support;
two-connectivity and the absence of unique portals make its complement
connected and boundary-full.

After excluding those cases, exactly one of `p,q` sees `b`; orient it as
`p`.  No member of `I` sees `p`, while every member of `I` sees `q`.  The
sets

```text
X_b = N_A(b)-W,
X_I = (union_{i in I} N_A(i))-W
```

are nonempty because otherwise `p` or `q` would be a unique portal, and they
are disjoint because an intersection vertex would itself be a repair support.

For fixed `x in X_b`, `y in X_I`, disjoint paths joining `x` to `y` and `p`
to `q` give outcome 2: the first path is a repair support and the second
contains the whole contact transversal, so it is boundary-full.  If outcome
2 is absent, this linkage fails for every choice of `x,y`.  Fabila-Monroy and
Wood's Two Paths theorem, applied with

```text
(s_1,t_1,s_2,t_2)=(x,y,p,q),
```

then says that the literal graph `G[A]` is a spanning subgraph of an
`(x,p,y,q)`-web.  The terminal order is correct, and the theorem requires no
three-connectivity hypothesis.  The source does not use any edge belonging
only to a web completion.

## 8. Orientation of the actual Kempe-fan separation

In the separation outcome of the cited Kempe-fan theorem, the new literal
boundary is

```text
(T-I) union {z_1,z_2}
  = J union {b,q,r,z_1,z_2}.
```

The theorem supplies a proper six-colouring on the closed connected side in
which `J union {q}` is monochromatic, while `b` and at least one member of
`{z_1,z_2}` share a second, distinct colour.  Naming that member `z_1` gives

```text
D=J union {q},    E={b,z_1},    S-(D union E)={r,z_2},
```

so all colour hypotheses of Corollary 2.1 hold literally.  If the coloured
shore has packing number at least two, its two disjoint boundary-full
connected subgraphs therefore give one of the two audited first-entry paths.

If its packing number is one and it has a boundary-contact transversal of
order at most two, the hypotheses of Theorem 3.1 hold on that same oriented
shore and give exactly its three alternatives.  The nonempty original shore
on the far side of the Kempe-fan separation supplies the required opposite
side.  The additional strong-criticality and `K_7`-minor-free hypotheses are
also exactly those under which the exact-seven packing theorem guarantees
that at least one of the two shores has packing number one.  As the source
correctly notes, that theorem does not say that the packet-thin shore is the
coloured shore.

## 9. Trust boundary

The GREEN verdict is confined to the exact conditional conclusions.  The
source does not:

- produce the two disjoint boundary-full connected subgraphs when the
  packing number is one;
- act at the first entry returned by Corollary 2.1;
- preserve a previously selected labelled minor model in the repair outcome;
- synchronize a boundary colouring in the exact-separation outcome;
- break the alternating web without further contraction-critical colouring
  input; or
- prove `HC_7`.

These are stated remaining obligations, not gaps in the two conditional
results.
