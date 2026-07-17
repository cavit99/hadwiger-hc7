# Repair terminals in the order-six overlap-three cell

**Status:** computer-assisted local theorem plus an elementary composition
lemma; independently audited **GREEN** in
[`hc7_overlap_three_repair_reserved_k4_audit.md`](hc7_overlap_three_repair_reserved_k4_audit.md).
This does not close the normalized order-six overlap-three cell or `HC_7`.

The proof-producing checker is
[`../active/hc7_overlap_three_order_six_repair_verify.py`](../active/hc7_overlap_three_order_six_repair_verify.py).
It uses no generic `K_7`-partition enumeration.

## 1. Normalized relation

Use the labels

```text
A={0,1,2,3,4,5},       I=A cap X={0,1,2},
X=I union {6,7},        p=8, q=9,
T={3,4,5,6,7,8,9}.
```

Assume that each of the nine six-sets

```text
A, X+p, X+q,
(A-{i})+p, (A-{i})+q  for i in I
```

is an irredundant support of a spanning `K_5` model.  As in the audited
overlap-three decoder, each local six-set has one of the 375 exact labelled
relations consisting of a spanning `K_5` minor but no literal `K_5`.
Join the nine relations on their common literal edges and nonedges.

Call a joined state **common** when it has the already-audited common
three-rooted small-`K_4` outcome.  For a noncommon state, call a terminal
`t in T` **good** when it is adjacent to all three members of `I`.

## 2. Exact repair invariant

### Theorem 2.1

There are 60,162 joined partial states and 7,878 noncommon states.  In every
noncommon state the literal graph on `I` is either `K_3` or `P_3`.  Their
exact profile is

```text
(number of I-edges, number of good terminals) : states
(3,4):2592, (3,5):336,
(2,3):153,  (2,4):1557, (2,5):1782, (2,6):1458.
```

Suppose `G[I]=P_3`, and write `uv` for its missing edge.  Then at least one
bad terminal `r` is adjacent to both `u` and `v`.  Call such an `r` a
**repair terminal**.  More precisely, the pair

```text
(number of good terminals, number of repair terminals)
```

has the following distribution:

```text
(3,3):144, (3,4):9,
(4,2):1332, (4,3):225,
(5,1):324, (5,2):1458,
(6,1):1458.
```

### Certificate

The checker enumerates the 375 exact local relations, joins all nine
copies, removes the common outcome, and reads only forced literal
`I-I` and `I-T` incidences.  It neither completes the seven unknown edges
nor enumerates `K_7` branch partitions.  The assertion that the repair set
is nonempty is checked in every one of the 4,950 noncommon `P_3` states.

## 3. Reserved-rooted-`K_4` composition

### Lemma 3.1

Let `G` contain a three-set `I={u,v,c}` inducing the path `u-c-v`.  Let
`W={w_1,w_2,w_3,w_4}` be disjoint from `I`, with every `w_j` adjacent to
all of `I`.  Let `r` be a further vertex adjacent to both `u` and `v`.
If `G-(I union {r})` contains a `W`-rooted `K_4` model, then `G` contains a
`K_7` minor.

### Proof

Let `D_1,...,D_4` be the four rooted bags, indexed so that `w_j in D_j`.
They are disjoint from `I union {r}`.  The seven bags

```text
{u,r}, {v}, {c}, D_1, D_2, D_3, D_4
```

are connected and pairwise disjoint.  The first bag meets `{v}` through
`rv` and meets `{c}` through `uc`; `{v}` meets `{c}` through `vc`.  Every
member of `I` meets every `D_j` through the literal edge to `w_j`, and the
four `D_j` are pairwise adjacent.  These are all adjacencies of a `K_7`
model.  `square`

### Corollary 3.2 (the exact negative object)

Put `H=G-I` in the normalized cell.  In every noncommon `P_3` state with
at least four good terminals, either `G` has a `K_7` minor, or for every
repair terminal `r` and every four-set `W` of good terminals, `H-r` has no
`W`-rooted `K_4` minor.

In the hypothetical counterexample setting, `H` is four-connected and
`H-r` is three-connected.  Hence Fabila-Monroy--Wood's rooted-`K_4`
classification places the negative branch in one of their six labelled
rooted-obstruction families.  No assertion is made here that a fill clique
is absent or that the literal graph is planar.  An ordinary rooted `K_4`
in `H` is insufficient because it may absorb every repair terminal.

## 4. Relation to the planar carrier decoder

If `G[I]=K_3`, four good roots that form a rooted `K_4` in `H` close
immediately with the three singleton core bags.  The audited
clique-or-cofacial argument can then enter the planar facial carrier
decoder.

For `G[I]=P_3`, the same ordinary rooted `K_4` gives only `K_7` minus the
edge `uv`; it is terminal only when a repair terminal is reserved as in
Lemma 3.1.  Therefore the all-cofacial/off-face carrier computation is a
valid conditional composition theorem, but it cannot by itself be used to
claim closure of the entire order-six overlap-three cell.

## 5. Exact scope

The result exposes a uniform repair resource in every path-core state and
identifies the correct labelled obstruction: a rooted `K_4` must be found
while reserving one repair terminal, or the corresponding three-connected
deletion belongs to one of the six rooted-obstruction families.  It does
not yet decode those families, prove that the repair terminal can be kept
outside a model, or close the 153 three-good states without an additional
direct certificate.
