# Audit: repair terminals and reserved rooted `K_4`

**Audit status:** GREEN.

**Audited source revision SHA-256:**
`ff619bfdba9d25239f484360d0f6899a558f553fa93b2b405748fd8f60a3bf78`

**Audited checker SHA-256:**
`987e7deaf01d75d6e737178edcc396d832c591e7f11fe190ce5c68a9f10af502`

This is a separate internal audit, not external peer review.

## Verdict

**GREEN**, after correcting the negative-branch terminology.  The exact
census, repair invariant, and reserved-model lift are correct.  Failure of
the reserved rooted `K_4` places `(H-r,W)` in one of the six labelled
Fabila-Monroy--Wood obstruction families; three-connectivity alone does
not imply that the literal graph is planar or fill-free.

This result does not close the order-six overlap-three cell.  In
particular, the `153` path-core states with only three good terminals remain
outside Lemma 3.1.

## 1. Independent replay

The command

```text
python3 active/hc7_overlap_three_order_six_repair_verify.py
```

completed successfully and returned

```text
joined=60162 noncommon=7878
(core_edges,good)
  (2,3):153 (2,4):1557 (2,5):1782 (2,6):1458
  (3,4):2592 (3,5):336
P3 (good,repair)
  (3,3):144 (3,4):9
  (4,2):1332 (4,3):225
  (5,1):324 (5,2):1458
  (6,1):1458
```

The checker reads only forced original incidences after joining the nine
support relations.  It does not complete an undecided edge and does not
use a carrier adjacency in a support relation.  Every one of the `4,950`
path-core states has a bad terminal adjacent to both endpoints of the
missing core edge.

## 2. Branch-set audit

Write `I={u,v,c}` with edges `uc,vc` and missing edge `uv`.  Let `r` be a
repair terminal, so `ru,rv` are literal edges, and let
`D_1,...,D_4` be a `W`-rooted `K_4` model in

```text
G-(I union {r}).
```

The seven proposed bags are

```text
{u,r}, {v}, {c}, D_1, D_2, D_3, D_4.
```

They are pairwise disjoint because the four exterior bags were found after
deleting `I union {r}`.  The first three bags form a triangle at bag level:

```text
{u,r}--{v} through rv,
{u,r}--{c} through uc,
{v}--{c} through vc.
```

Each `D_j` contains its good root `w_j`, and every `w_j` is literally
adjacent to all three members of `I`.  Hence all three core bags contact
every `D_j`; the `D_j` are pairwise adjacent by the rooted `K_4` model.
No adjacency from `r` to an exterior bag is used.  The lift is therefore
literal and complete.

## 3. Negative branch

In the intended application `H=G-I` is four-connected, hence `H-r` is
three-connected.  If the reserved rooted `K_4` does not exist, the exact
published rooted-`K_4` characterization places the labelled rooted graph
in one of its six obstruction families.  Those families may contain fill
cliques behind facial triangles.  Neither planarity of the literal graph,
cofaciality in a fill-free embedding, nor any stronger web transition is
available without an additional four-connectivity or fill-elimination
argument.

## 4. Trust boundary

An ordinary rooted `K_4` in `H` is insufficient: a branch bag may absorb
every repair terminal.  The deletion of `r` before finding the rooted model
is essential.  Likewise, a later composition may use an omitted terminal
only after separately proving that it lies outside all four rooted bags.
