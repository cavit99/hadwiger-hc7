# Audit: aligned matching and almost-universal boundary completion

**Verdict:** **GREEN.**  The matching dichotomy, the forced theta
description, the uniform two-reserved-vertex anchoring theorem, the
common-neighbour completion theorem, and the forced-theta mixed-shore
completion are correct under their stated hypotheses.  Every failed
linkage has the advertised sharp separator budget, and every displayed
family of branch sets is pairwise disjoint, connected, and realizes all
edges of the claimed clique minor.

**Audited source:**
[`results/hc7_balanced_aligned_matching_dichotomy.md`](hc7_balanced_aligned_matching_dichotomy.md)

**Audited source SHA-256:**
`d954296e6b5a4016e0894694897a083efe68f4b3085fa1f4d7a3d380799361d7`.

The independently audited mathematical revision had SHA-256
`ddf05e79ae5848c6d07ac7b47d14cc725653d09dff9403f24e6fc96d274a7af5`.
The promoted revision differs only in the opening status paragraph, which
now records this GREEN audit; no theorem statement or proof step changed.

This is an independent internal audit of the conditional results as
stated.  It does not re-audit the upstream derivation of the balanced
order-eight boundary, the cited quotient-support theorem, the cited
shifted-boundary completion theorem, or the existence of support-at-most-six
models after every two-vertex deletion.  Those are explicit inputs.

## 1. Matching dichotomy and theta remainder

After fixing the matching edge `xr`, the two remaining vertices of `R`
cannot be matched to one another because `R` is independent in `F`.
Neither can use `x`, and no matching edge lies inside `A` or inside `B`.
Consequently a perfect matching containing `xr` and an `A`--`B` edge
exists exactly in one of the two cross-neighbourhood cases displayed in
(1.3).

If both cases fail and both remaining clique vertices have an endpoint
neighbour, neither can meet both `A` and `B`; they must meet the same one
of those sets.  The two nonempty disjoint endpoint neighbourhoods for the
other set cannot both lie in the one remaining vertex `r`.  This proves
the alternative in (1.1).  Conversely, a vertex satisfying (1.1) is
isolated after deleting `x,r`, so the alternatives are disjoint.

When `F` is factorizable, such a vertex `p` has no boundary neighbour
except `x`; hence every perfect matching contains `px`.  In the complement
`J`, the two endpoint neighbourhoods of each of `A,B` are then the two
complementary singleton subsets of `{r,q}`.  Each specified edge therefore
forms one length-three `r`--`q` path.  There are no edges between their
internal vertices, and `rq` is present.  This verifies the exact
six-vertex theta graph in Corollary 2.1, not merely a spanning theta
subgraph.

## 2. Uniform two-reserved-vertex anchoring

In Theorem 3.1, let the compact `K_{k-2}` model have support order `m`,
and let `h` branch sets miss

```text
B = S-{p,x}.
```

Every such branch set is wholly outside `S`; because the model avoids
`V`, it lies in `U`.  Retaining one root in each of these branch sets and
deleting the other model vertices together with `p,x` gives

```text
|Z| = m-h+2.
```

At most `m-h` boundary vertices of `B` lie in the deleted model support,
so there are at least

```text
(k-1)-(m-h) >= h
```

unused targets.  If an `h`-linkage fails, set-Menger supplies a separator
`X` of order at most `h-1`; therefore

```text
|Z union X| <= m+1 <= k.
```

Since both terminal sets have order at least `h`, each retains a vertex
after deleting `X`.  Thus `Z union X` genuinely separates two nonempty
sets.  An order below `k` contradicts `k`-connectivity, while equality is
an actual order-`k` separation.

On the successful side, a stopped path cannot enter `V` before its first
boundary visit: it starts in `U`, there is no `U`--`V` edge, `p,x` are
deleted, and every other boundary vertex belongs to `B`.  Its first
boundary vertex lies among the unused targets because every old model
vertex other than its retained root was deleted.  The stopped paths are
mutually disjoint and preserve every old branch-set label and adjacency.

After augmentation, each old row contains a distinct vertex of `B`.
The final two branch sets are `V union {x}` and `{p}`.  Boundary fullness
makes the first connected and adjacent to every old row, (3.1) makes
`p` adjacent to every old row, and the `V`--`p` contact joins the final
two sets.  This verifies the `K_k` model in (3.6).  The case `h=0` is the
same construction without linkage.

## 3. Compact-model mixed-shore normal form

Under the hypotheses of Corollary 3.2, Theorem 3.1 in both orientations
forces every support-at-most-six `K_5` model in `G-{p,x}` to meet both
open components.  If each component met only one branch-set label,
contracting each entire component is label-safe and gives a support-at-most-six
model in the two-apex quotient.  The cited quotient-support theorem rules
this out, so one component meets at least two labels.

A support-five model consists of five singleton branch sets and cannot
meet two anticomplete open components.  Thus a minimum compact model has
support six: four singleton rows and one edge row.  Orient the components
so that one contains at least two labels.  One of those labels is a
singleton.  The label meeting the opposite component must then be the
edge row; its second vertex is a boundary vertex, giving `{v,t}`.  The
remaining labels in the first component are singleton rows.  This yields
(3.7) with initially `2<=h<=4`.

If `h=4`, the vertex `t` together with the four `u_i` is a support-five
`K_5`, because the old model forces `t` adjacent to every `u_i`.  If `t`
also met every `w_j`, then `t` together with all four singleton rows would
again be a support-five `K_5`.  These observations give `h<=3` and the
required missing `t`--`w_j` edge.

This corollary depends essentially on the **support-at-most-six** response.
An arbitrary unbounded `K_5` model need not have one edge row, need not
survive the component contractions with the same support bound, and does
not yield (3.7).

## 4. Common-neighbour completion

For Lemma 4.1, let `h` old branch sets miss `W`.  Retain one root in each,
delete the other `m-h` support vertices together with `a,b`, and use the
vertices of `W` outside the old support as targets.  There are at least

```text
(k-1)-(m-h) >= h
```

targets.  Failure gives a separator of order at most

```text
(m-h)+2+(h-1) = m+1 <= k.
```

The same terminal-count argument makes equality an actual order-`k`
separation.  Success puts a distinct common neighbour of `a,b` in every
old branch set, so adjoining `{a}` and `{b}` realizes a `K_k` model.  No
shore-location assertion is needed in this lemma.

## 5. Component contacts in the forced-theta completion

For a component `C` of `V-v`, connectedness of `V` and the fact that
`U,V` are distinct components of `G-S` give exactly

```text
N_G(C) = {v} union N_S(C).
```

Seven-connectivity gives `|N_S(C)|>=6`; equality is an actual order-seven
separation because `C` and `U` remain on opposite nonempty sides.  Hence,
away from the terminal conclusion, every such component sees at least
seven boundary vertices.

### Full contact with `F_0`

If `C` sees all of

```text
F_0={p,t,w_1,...,w_{4-h}},
```

then at least `h+1` of its boundary contacts lie outside `F_0`.  At most
one is the reserved vertex `x`, leaving at least `h` targets in (4.4).
Here

```text
|Z|=8-h,
```

so a failed `h`-linkage gives an actual order-seven separation.  A stopped
successful path cannot enter `C`: every non-target entrance is in `Z`.
The old five model rows, `C`, and `{p}` then form a `K_7` model.  Therefore
every surviving component sees exactly seven boundary vertices and misses
one member of `F_0`.

### Excluding a missed `t`

If a component misses `t`, the deletion set again has order `8-h`, while
the target set has order `h+1`.  The stopped paths avoid the component for
the same entrance reason.  In (4.5), the old rows retain their clique
adjacencies, the component sees the boundary anchor of every row, and
`p` meets every row through `B`; the contacts with `{v,t}` and between
the two new sets are also forced.  Thus a missed contact belongs to
`{p,w_1,...,w_{4-h}}`.

## 6. Aligning the missed contact

For `h=3`, the deletion set in Step 4 has order five.  Failure of the
three-linkage therefore gives a separator of order at most seven.  The
four non-row branch sets in (4.7) are connected, disjoint, and pairwise
adjacent through

```text
C_p-t, C_p-v, wp, tv, tp, C_w-p.
```

Each augmented row meets both component sets through its terminal and
meets `{t}` and `{p}` through its old `u_i-t` edge and its boundary
terminal, respectively.

For `h=2`, the deletion set has order six; failure of the two-linkage is
again an actual order-seven separation.  The endpoint sets

```text
L(b)={e in {v,t}: eb is an edge}
```

are nonempty.  If the two missed contacts have distinct representatives,
the branch sets in (4.11) give a `K_7`: each component supplies its two
unmissed boundary contacts, its assigned endpoint supplies the missed
one, and the two assigned endpoints are `v,t`.

If no distinct representatives exist, both endpoint sets are the same
singleton.  In the common-`v` case the missed contacts must be `w_1,w_2`,
and the ten pairs among the last five sets of (4.12) are exactly the ten
listed witnesses.  In the common-`t` case the explicit missing
`t`--`w_j` edge forces one missed contact to be `p`; after relabelling,
the ten listed witnesses for (4.13) are all available.  In both displays,
the two augmented rows retain their mutual edge and meet each of the
other five sets through old model edges or their distinct boundary
terminals.  No edge `px` is used anywhere.

It follows that all components of `V-v` have one common missed boundary
vertex `y`.

## 7. Shifted boundary and final anchoring

If `V-v` had two components, then with

```text
S'={v} union (S-{y})
```

they are two actual components of `G-S'`, each full to the order-eight
boundary `S'`.  The support-six model avoids them.  The cited uniform
two-full-component theorem therefore gives a `K_7`.  Thus the residue
`X=V-v` is connected.

If `y!=p`, then `y` is one of the singleton rows `w_j`.  The `h+1`
unanchored rows relative to `W=B-{y}` are exactly the `h` rows in `U`
and `{y}`.  The deletion set has order `7-h`, and there are exactly
`h+1` unused targets.  Failed linkage plus a separator of order at most
`h` has total order seven.  On success the stopped paths avoid `X`, since
`X` misses `y`, `v,p,x` are deleted, and every other entrance is deleted
or is a target.  All five rows then meet distinct vertices of `W`; they,
`X`, and `{p}` form the claimed `K_7` model.

If `y=p`, the deletion set has order `8-h`, there are `h+1` unused
vertices of `B`, and only an `h`-linkage is needed.  Failure again has
total order seven.  Success anchors the five old rows at five distinct
vertices of `B`; with `z` the unused sixth vertex, the last two branch
sets are `X union {z}` and `{p}`.  Boundary fullness connects `X` to all
rows and to `z`, while (3.1) supplies every edge from `p` to the five rows
and to `z`.

These cases prove Theorem 4.2 and Corollary 4.3.

## 8. Trust boundary and exact surviving gap

The argument is conditional on all of the following inputs:

- the balanced order-eight boundary and its perfect matching in the
  complement;
- the independently audited shared missed-contact vertex `r`;
- a support-at-most-six `K_5` model after every two-vertex deletion;
- the cited quotient-support theorem; and
- the cited shifted-boundary completion theorem.

Within those hypotheses, the Hall obstruction is eliminated.  The proof
does **not** turn the resulting aligned perfect matching into compatible
six-colourings or a labelled `K_7` model.  That palette-to-model step is
the exact remaining host-level gap described in Section 5 of the audited
source, and this audit does not enlarge the conclusion beyond it.
