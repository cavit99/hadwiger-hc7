# Audit of the unbalanced two-cut response reduction

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_two_cut_small_class_web_reduction.md`

**Audited SHA-256:**
`b61163b0541acf822b31e2ad46481cdf35f14010ffa71a9bf7c5d1e159b56036`

**Promoted source SHA-256:**
`ea617eeaa4be6210e2321c1b4ee6589425245c2ced01c17bd6d5e01b57582abf`

The promoted revision changes only the status line and adds this audit link;
the theorem statements, proofs, dependencies, and trust boundary audited
below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Imported normal form

The audited response-orientation theorem supplies all data used in Section
1: the two lobes and cut vertices, the exact defects, the nonedge `de`, the
bipartition `S-{d,e}=P dotcup R`, the physical orientation of the two
response types, and the forced bichromatic `d`--`e` path internal to `C`.
It also proves that both classes are nonempty, each root has a neighbour in
both classes, and an actual `P`--`R` edge exists.  No colour is identified
with a branch-set label.

## Lemma 2.1: reserved connected subgraphs

For fixed `i` and `j=1-i`, use `Q_i` as one open shore and `C union Q_j`
as the other.  These shores are anticomplete.  The three connected
subgraphs `D,K,Q_j` in the latter shore are pairwise disjoint.  They have,
respectively, both root contacts, every contact in the selected boundary
class `B`, and every contact in the complementary class `B'`.

These are exactly the hypotheses of the audited three-block linkage and
reflection theorem.  They first produce the equality partition

```text
B | B' | {d,e}.
```

A `d`-portal of `D` lies in `L_e`, while an `e`-portal lies in the disjoint
lobe `L_d`, so the two selected portals are distinct.  In a spanning tree
of `D`, deleting any edge on their unique connecting path partitions all of
`D` into two nonempty connected adjacent subgraphs retaining the respective
root contacts.  The four-block part of the same theorem therefore produces

```text
B | B' | {d} | {e}.
```

Repeating this construction with `i=0,1` yields the unequal partition on
both individual `Q_i` component-sides.  Those colourings and the prescribed
unequal colouring on the closed `C`-side can be aligned on the four labelled
blocks and glued because the three open components are pairwise
anticomplete.  Lemma 2.1 is valid.

## Theorem 3.1: singleton class

Let the singleton class be `{p}` and choose a portal `w` in `C`.  If one of
the forced `d`--`e` paths avoids `w`, its internal vertex set and `{w}` are
the disjoint connected subgraphs required by Lemma 2.1.  The root-path
interior has at least two vertices: its first and last internal vertices lie
in the disjoint lobes `L_e` and `L_d`.

Otherwise every such path contains `w`.  Two-connectivity makes `C-w`
connected.  If both roots retained neighbours there, a path in `C-w`
between a `d`-neighbour in `L_e` and an `e`-neighbour in `L_d`, together
with the two root edges, would avoid `w`.  Thus `w` is the unique `C`-portal
of one root.

For `C'=C-{w}`, two-connectivity also ensures that `w` has a neighbour in
`C'`, so `N_{G[C]}(C')={w}`.  The missing root bounds the number of boundary
neighbours by seven.  Hence

```text
|N_{G[C]}(C')| + |N_G(C') intersect S| <= 8.
```

The hypotheses of the audited small-boundary lobe descent hold: `C'` is
nonempty, connected, proper, and another component of `G-S` lies outside
it.  Its conclusions are exactly outcomes 2 and 3.  The one-sided colouring
claim is only a restriction of the already selected closed-`C` colouring;
it does not assert response preservation on the other shore.

## Theorem 4.1: two-vertex class

For `B={p,q}`, both nominated pairs `(d,e)` and `(p,q)` are nonedges.  The
graph `H=G[C union {d,e,p,q}]` is connected because `C` is connected and
boundary-full.  Lemma 2 of Fabila-Monroy and Wood, *Rooted K4-Minors*,
Electronic Journal of Combinatorics 20(2) (2013), #P64, states that for
distinct `s_1,t_1,s_2,t_2`, either there is an
`(s_1t_1,s_2t_2)`-linkage or the graph is a spanning subgraph of an
`(s_1,s_2,t_1,t_2)`-web.  Substituting

```text
(s_1,t_1,s_2,t_2)=(d,e,p,q)
```

gives exactly the outer order `(d,p,e,q)` used in the theorem.

In the linkage outcome, vertex-disjointness prevents either path from using
a terminal of the other.  All internal vertices therefore lie in `C`.  The
`d`--`e` path has at least two internal vertices in the two distinct lobes,
and the `p`--`q` path has a nonempty connected interior.  Their interiors
satisfy Lemma 2.1 and give outcome 1.

In the web outcome, let `F` be the planar skeleton and `X_T` an attachment
clique behind a facial triangle `T`.  Each attachment vertex belongs to
`C`, since the four nominated boundary vertices belong to the skeleton.
For a component `A` of `G[X_T]`, the spanning-subgraph relation to the web
completion excludes every neighbour in `H` outside `T union X_T`, and
componenthood excludes neighbours in `X_T-A`.  Because `C` is a component
of `G-S`, the only additional possible neighbours are the four omitted
boundary vertices.  Consequently

```text
N_G(A) subseteq T union (S-{d,e,p,q}),
```

a set of order seven.  The set is genuinely separating: `A` is nonempty
and `Q_0` is anticomplete to `C`, hence lies outside `A union N_G(A)`.
Seven-connectivity forces equality and produces an actual order-seven
separation with connected shore `A`.

If every attachment set is empty, the web completion is its planar
skeleton, and the exact conclusion in outcome 3 follows.  The proof does
not treat virtual completion edges as host edges.

## Trust boundary

The singleton result terminates only in six-colourability, an unqualified
order-seven separation, or a strict one-sided order-eight restart.  It does
not preserve a complete common equality partition or the five inherited
minor-model labels.  The two-vertex result leaves an attachment-free planar
web; it does not allocate the other four boundary contacts or close that
web.  The balanced `3+3` bipartition is outside the theorem.  These limits
are stated accurately.

Within this scope, no gap or source-number error was found.
