# Independent audit: bichromatic support at a non-double-critical edge

**Audited source:** `hc7_adjacent_pair_bichromatic_support_dichotomy.md`
**Frozen proof SHA-256:**
`b8ed27232cfb6a1b7195f6190ec481b999d375198cbb4c58394cd74018776710`
**Promoted theorem SHA-256:**
`cbceda7fd8f6323d7b78a23e47cb7d8a0650b634ddd3decddf7e27367e9d2bcb`
**Verdict:** **GREEN.**

The promoted copy differs from the frozen proof only in its status line,
which now records this audit.  The theorem statement and mathematical proof
are byte-for-byte unchanged.

The support-component dichotomy, both separator constructions, and the
three-common-branch-set consequence are correct under the stated
hypotheses.  The result remains strictly local: a returned separator need
not have order seven, and a concentrated bichromatic component does not
identify its colour contacts with specified branch sets of the `K_6` model.

## 1. The contraction colouring

A six-colouring of `G/zu` expands to a proper colouring of `G-zu` by giving
both ends of `zu` the contracted vertex's colour `alpha`.  Consequently no
`alpha`-coloured vertex of `H` is adjacent to either pole.  The restriction
to `H` must use all six colours because `chi(H)=6`, so its `alpha` class is
nonempty.

Each pole has a neighbour of every colour `beta != alpha`.  If, for
example, `z` missed `beta`, the colouring of `H` would extend to `G` by
giving `z` colour `beta` and `u` colour `alpha`.  This also verifies the
setup independently of the earlier edge-deletion palette lemma.

## 2. Existence of a common component

In the `alpha`--`beta` subgraph of `G-zu`, the two poles must be in the same
component.  Otherwise swapping `alpha` and `beta` on the component
containing `z` gives the poles different colours and remains proper after
restoring `zu`, contrary to `chi(G)=7`.

The poles have colour `alpha` and have no `alpha`-coloured neighbours.
Deleting them from an `alpha`--`beta` path between them therefore leaves a
component of `H[phi^{-1}({alpha,beta})]` containing a `beta`-coloured
neighbour of each pole.  This is precisely a common member of `C_beta`.

The two alternatives in Theorem 2.1 are exhaustive and disjoint: either
this is the only support component, or `C_beta` has another member.

## 3. Concentrated support

If `C_beta={K_beta}`, every `beta`-coloured pole neighbour lies in
`K_beta`.  Swapping the two colours on that component changes all those
neighbours to `alpha`.  No pole acquires a `beta`-coloured neighbour from
the old `alpha` side because the original `alpha` class was anticomplete to
both poles.  The other four pole-neighbour colours are unchanged.  Thus
`beta` is exactly the common missing colour after the swap, while `alpha`
is present at both poles.

For `theta` outside `{alpha,beta}`, suppose no `beta`-coloured vertex of
`K_beta` had a `theta`-coloured neighbour.  Recolouring the entire
`beta` side of `K_beta` with `theta` is proper: that side is independent,
contains no `theta` vertex, and by assumption has no neighbour of the new
colour.  Both poles then miss `alpha` and `beta`; assigning those two
different colours to `z,u` gives a six-colouring of `G`.  This contradiction
proves the asserted external contact for each of the four remaining
colours.  Since `K_beta` contains only `alpha,beta`, every such contact lies
in `H-K_beta`, as stated.

## 4. Diffuse support and separator order

Let `K` be common and let another support component contain a pole neighbour
`w`.  Distinct components of the induced `alpha`--`beta` subgraph are
anticomplete, so

```text
w notin K union N_H(K).
```

Every neighbour of `K` in `H-K` has a colour outside `{alpha,beta}`, and
the only possible neighbours outside `H` are the two poles.  Removing
`N_H(K) union {z,u}` therefore leaves the connected nonempty set `K`
separated from `w`.  This is an actual vertex cut of `G`, not merely a
model-relative separation.  Seven-connectivity yields
`|N_H(K)|+2 >= 7`, hence `|N_H(K)|>=5`; equality gives an order-seven
separation.  The existence of the second support component also proves
that `K` is a proper subset of `H`.

No upper bound follows when `|N_H(K)|>5`.

## 5. One-pole refinement

Suppose a component `L` is met by `z` but not by `u`.  If every
`beta`-coloured neighbour of `z` lay in `L`, swapping `alpha,beta` on `L`
would make `z` miss `beta`, while `u` would continue to miss `alpha`:
`u` has no neighbour in `L`, because a pole can meet an
`alpha`--`beta` component only through its `beta` side.  Assigning `beta`
to `z` and `alpha` to `u` would then six-colour `G`.  Therefore `z` meets a
second support component.

A `beta`-coloured neighbour in that second component lies outside
`L union N_H(L)`.  The other pole has no neighbour in `L`.  Hence
`N_H(L) union {z}` is an actual separator, and seven-connectivity gives
`|N_H(L)|>=6`; equality again means order seven.  This verifies both the
far-side witness and the claimed boundary size, which are the two points
at which the refinement could otherwise fail.

## 6. Three common branch sets

The corollary uses the separately audited singleton-portal normal form in
`hc7_adjacent_pair_palette_linkage.md`.  In that form, each common branch
set contains exactly one pole neighbour, shared by the poles; there is one
`z`-exclusive branch set `F_z`, one `u`-exclusive branch set `F_u`, and one
uncontacted branch set.  The model is spanning.

At most three of the five non-`alpha` colours occur on the three common
portals.  Hence at least two colours are absent there.  For each such
colour `beta`, every `beta`-coloured neighbour of `z` lies in `F_z` and
every one at `u` lies in `F_u`.  Applying Theorem 2.1 is therefore
legitimate.  In the concentrated case its common component meets both
exclusive branch sets and has the four asserted colour contacts.  In the
diffuse case the theorem returns the actual separator.  The argument is
valid independently for each of at least two absent portal colours.

The conclusion does not say that either bichromatic component avoids the
other four branch sets, that two such components are disjoint, or that its
four colour contacts occur in four prescribed model branch sets.

## 7. Adversarial checks and scope

The existing complete-join icosahedron checks were rerun:

```text
python3 barriers/hc7_same_row_split_two_apex_icosahedron_check.py
python3 active/hc7_atomic_two_pole_contact_trichotomy_verify.py
```

Both returned `GREEN`.  These examples realize the separator/terminal
guardrail for downstream model surgery and do not refute the theorem.
More generally, a join construction cannot evade the component argument:
if support is split between two bichromatic components, the displayed
full neighbourhood is literally a vertex cut; if all pole support is in
one component, the Kempe swap and recolouring contradiction apply without
any model hypothesis.  For the universal edge of `K_2 vee J`, moreover,
`chi(G-{z,u})=chi(J)=chi(G)-2`, so it does not satisfy the present
non-double-critical condition `chi(H)=6` when `chi(G)=7`.

The theorem may be cited as proving an exact reversible missing-colour
transition or a genuine separator for every nonbuffer colour.  It may not
be cited as proving a bounded-order separator, a labelled branch-set
rerouting, a `K_7` minor, or a two-vertex `K_5`-minor transversal.
