# Bichromatic support at a non-double-critical edge

**Status:** written proof; separate internal audit GREEN.  This note gives a
model-independent colouring-space dichotomy for an adjacent pair whose
two-vertex deletion is six-chromatic.  It does not prove `HC_7`: a separator
returned below can have order greater than seven, and the concentrated
alternative still has to be composed with a labelled `K_6`-minor model.

## 1. Setup

Let `G` be a seven-connected, seven-chromatic graph such that every proper
minor is six-colourable.  Let `zu` be an edge and put

\[
                         H=G-\{z,u\}.
\]

Assume `chi(H)=6`.  Colour the contraction `G/zu` with six colours and
restrict the colouring to `H`.  If `alpha` is the colour of the contracted
vertex, this gives a proper six-colouring `phi` of `H` such that

* the `alpha`-colour class is nonempty and anticomplete to both `z,u`; and
* each of `z,u` has a neighbour of every colour `beta ne alpha`.

Fix one such colour `beta`.  Let `C_beta` be the set of components of

\[
                  H[\phi^{-1}(\{\alpha,\beta\})]
\]

which contain a `beta`-coloured neighbour of at least one of `z,u`.  A
member of `C_beta` is **common** if it contains a neighbour of both poles.
This terminology concerns literal pole neighbourhoods, not branch sets of
a minor model.

## 2. Support-component dichotomy

### Theorem 2.1

For every colour `beta ne alpha`, at least one common component exists.
Moreover exactly one of the following two alternatives holds.

1. **Concentrated support.**  The set `C_beta` consists of one common
   component `K_beta`.  Interchanging `alpha,beta` on `K_beta` gives another
   proper six-colouring of `H` in which `beta`, rather than `alpha`, is the
   unique colour absent from both pole neighbourhoods.  In addition, for
   every colour

   \[
                         theta notin \{alpha,beta\},
   \]

   some `beta`-coloured vertex of `K_beta` has a
   `theta`-coloured neighbour in `H-K_beta`.

2. **Diffuse support.**  There is a common component `K` and another member
   of `C_beta`.  Then

   \[
                         S=N_H(K)\cup\{z,u\}             \tag{2.1}
   \]

   is an actual vertex separator of `G`.  Every member of `N_H(K)` has a
   colour outside `\{alpha,beta\}`, and

   \[
                         |N_H(K)|\ge5.                  \tag{2.2}
   \]

   In particular, equality in (2.2) gives an actual order-seven
   separation.  The open side `K` is a proper nonempty connected subset of
   `H`.

#### Proof

First give both `z,u` the colour `alpha` in the edge-deleted graph `G-zu`.
For the fixed colour `beta`, the vertices `z,u` must lie in the same
`alpha`--`beta` component.  Otherwise interchange the two colours on the
component containing `z`.  The pole `z` changes to `beta`, the pole `u`
remains `alpha`, and restoring the edge `zu` gives a proper six-colouring
of `G`, a contradiction.

The only way in which the two poles can be joined in that bichromatic
subgraph is through a component of
`H[phi^{-1}({alpha,beta})]` which contains a neighbour of each.  Thus a
common component exists.

Suppose first that `C_beta={K_beta}`.  Every `beta`-coloured pole neighbour
lies in `K_beta`, while neither pole has an `alpha`-coloured neighbour.
After interchanging `alpha,beta` on `K_beta`, both poles see `alpha` and
neither sees `beta`.  Contacts in the other four colours are unchanged.
Thus `beta` is the common missing colour in the new colouring.

Fix `theta` outside `{alpha,beta}`.  If the `beta`-coloured side of
`K_beta` had no `theta`-coloured neighbour, recolour every
`beta`-coloured vertex of `K_beta` with `theta`.  This is proper: those
vertices are independent and, by assumption, none has a neighbour of the
new colour.  Since `K_beta` contains every `beta`-coloured pole neighbour,
both poles now miss both `alpha` and `beta`.  Giving `z` colour `alpha` and
`u` colour `beta` would then six-colour `G`, a contradiction.  Hence the
asserted `theta`-contact exists for each of the four untouched colours.

Now suppose that `C_beta` has at least two members and choose a common
member `K`.  Since distinct bichromatic components are anticomplete, a
pole neighbour in another member of `C_beta` lies outside
`K union N_H(K)`.  The set `K` is nonempty and connected.  Its only
neighbours outside `H` are the two poles, both of which meet `K`, and every
neighbour in `H-K` has a colour outside `{alpha,beta}`.  Consequently
`S` in (2.1) separates `K` from the displayed pole neighbour in the other
component.  It is therefore an actual separator of `G`.

Seven-connectivity gives `|S|>=7`.  The two poles are outside `H`, so
`|N_H(K)|>=5`.  All remaining assertions follow directly. \(\square\)

### Remark 2.2 (one-pole refinement)

If the two poles do not meet exactly the same members of `C_beta`, choose a
component `L` met by only one pole.  Criticality forces that pole to meet a
second bichromatic component: if all its `beta`-neighbours lay in `L`,
interchanging `alpha,beta` on `L` would make the two poles miss the distinct
colours `beta` and `alpha`, and those colours could be assigned to the
poles.  Hence

\[
              N_H(L)\cup\{\hbox{the pole meeting }L\}
\]

is an actual separator.  Seven-connectivity now gives
`|N_H(L)|>=6`; equality again gives an order-seven separation.  This
refinement has one literal pole in its boundary rather than two.

## 3. Exact consequence for three common model branch sets

Let `F_1,...,F_6` be a spanning `K_6`-minor model in `H`.  Suppose it is in
the three-common-branch-set normal form from the palette-permutation
linkage theorem:

* three branch sets contain one common pole portal each;
* `F_z` is contacted only by `z` and `F_u` only by `u`;
* the sixth branch set is contacted by neither pole; and
* at least two non-`alpha` colours are absent from the three common portal
  vertices.

For every such absent portal colour `beta`, all `beta`-coloured pole
neighbours lie in `F_z` and `F_u`.  Theorem 2.1 therefore gives a uniform
fork:

1. an actual separator of the form (2.1), with an order-seven separation
   at equality; or
2. one connected `alpha`--`beta` subgraph which contains every
   `beta`-coloured pole neighbour, joins the two exclusive branch sets, and
   whose `beta` side has a neighbour in every other non-`alpha`,
   non-`beta` colour class.

There are at least two distinct colours for which this fork is available.
Thus the unresolved three-common-branch-set profile cannot have diffuse
bichromatic pole support without exposing a genuine graph separator.  Its
separator-free residue consists of two or more concentrated, reversible
colour transitions, not merely two unstructured paths between the
exclusive branch sets.

#### Proof

The normal-form statement places every pole neighbour of an absent portal
colour in the appropriate exclusive branch set.  Apply Theorem 2.1 to each
of the at least two such colours.  In the concentrated alternative the
common component contains a pole neighbour in each of `F_z,F_u`, and is
therefore a connected subgraph joining those two branch sets.  The
four-colour contact assertion is the final assertion of Theorem 2.1.
\(\square\)

## 4. Trust boundary

Theorem 2.1 is a strict structural fork in the full colouring space of the
adjacent pair.  It improves the five arbitrary pole-to-pole paths to either
an actual graph separator or an exact reversible missing-colour transition
whose root-facing colour side meets every untouched colour class.

It does **not** identify a colour class with a branch set of the uncoloured
`K_6` model.  In particular, four colour contacts need not preserve four
specified branch-set adjacencies.  Nor does seven-connectivity bound the
separator in (2.1) from above: if its order exceeds seven, a separate
state-preserving composition theorem is still needed.  The complete-join
icosahedron family is consistent with the concentrated alternative and
remains the required guardrail against inferring a `K_7` model from the
colour transitions alone.
