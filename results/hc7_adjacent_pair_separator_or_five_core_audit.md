# Independent audit: adjacent-pair separation or five-chromatic core

**Audited file:**
[`hc7_adjacent_pair_separator_or_five_core.md`](hc7_adjacent_pair_separator_or_five_core.md)

**Audited source SHA-256:**
`e8ac71370bbefbd9bd7bd717b335a8e9179499fdbbe554a1c61d37a4e0701f93`

**Verdict:** **GREEN.**

The case exhaustion, all three literal separator constructions, the passage
to the five connected star-Kempe instances, and the rooted-`K_4` lift to an
explicit `K_7`-minor model are correct.  No repair is required.  The theorem
may be promoted unchanged, with this audit moved beside it and the usual
status-line-only promotion update.

This is a deductive audit.  No finite search is used as evidence for the
verdict.

The independent audit was performed on source hash
`ba22eb3d521f4d867e6fd19a90b83735cb7bf3bb2c3c0a3b60e7ed3d9324768c`.
The only subsequent source change was the status-only promotion from
“separate internal audit pending” to “separate internal audit GREEN,” plus
a grammatical shortening of the adjacent descriptive sentence.  The
theorem statement, proof, consequences, and scope are unchanged.

## 1. Hypotheses and promoted inputs

The source's hypotheses make `G` a `7`-contraction-critical graph.  Mader's
connectivity theorem therefore makes `G` seven-connected.  This justifies
both the applicability of the separator inputs and every lower bound
`|N_G(L)| >= 7`.  The primary source is W. Mader,
[*Über trennende Eckenmengen in homomorphiekritischen Graphen*](https://eudml.org/doc/161665),
Mathematische Annalen 175 (1968), 243--252.  Thus seven-connectivity is a
consequence of the displayed hypotheses, not a missing additional
assumption.

The four promoted inputs were checked at these exact GREEN-audited
revisions:

- `hc7_global_adjacent_pair_palette_frame.md`, SHA-256
  `e4f99a43d6f45d3c1e7d93bbf854185e0009ecdc143c733d25449c2956aead98`;
- `hc7_adjacent_pair_bichromatic_support_dichotomy.md`, SHA-256
  `cbceda7fd8f6323d7b78a23e47cb7d8a0650b634ddd3decddf7e27367e9d2bcb`;
- `hc7_concentrated_rotation_normalization.md`, SHA-256
  `c60dd0c95f38bb39cf6922987861be83c66e6f85dc9cbf7a452df307d2eef37f`;
  and
- `hc7_star_kempe_five_core_compression.md`, SHA-256
  `45e3d2e1a8aab16690c3941e5013c0f5bdc296ab257cea042dab1ceec7cb5557`.

The palette setup is internally consistent for the selected edge.  A
six-colouring of the proper minor `G/zu` restricts to a six-colouring of
`H`.  Its contracted colour `alpha` must occur in `H`, since otherwise
`chi(H)<=5`.  Properness at the contracted vertex makes this colour class
anticomplete to both poles.  If either pole missed another colour, that
colour and `alpha` could be assigned to the two poles to six-colour `G`.
Hence both poles see all five other colours exactly as stated.

## 2. Exhaustion for a fixed colour

Fix `beta != alpha`.  Let `C_beta` be the support family from the promoted
bichromatic-support theorem: its members are the components of
`H[A union V_beta]` containing a `beta`-coloured neighbour of at least one
pole.  That theorem supplies a common member `K_beta`, met by both poles.

There are then only the following possibilities.

1. **Diffuse support.**  If `C_beta` has another member, the common member
   from the diffuse alternative has a literal separator as its full
   neighbourhood.
2. **One-sided support.**  If a support component is met by only one pole,
   the one-sided refinement forces that pole to meet a second support
   component and makes the first component's full neighbourhood a literal
   separator.  This case can overlap the diffuse case; treating it
   separately gives a sharper one-pole boundary and creates no gap.
3. **Concentrated support with an inactive component.**  If
   `C_beta={K_beta}` but `H[A union V_beta]` is disconnected, every other
   component contains no `beta`-neighbour of either pole.  It also contains
   no `alpha`-neighbour of a pole, because the whole `alpha` class is
   anticomplete to the poles.  It is therefore inactive in precisely the
   sense required by the normalization theorem, whose separator corollary
   applies.
4. **Concentrated support with no inactive component.**  The common
   component is then the whole graph `H[A union V_beta]`, which is connected.

Thus every disconnected two-colour graph gives outcome 1.  If outcome 1
never occurs, case 4 holds for each of the five choices of `beta`, proving
all five full connectivity assertions.  No diffuse or one-sided support is
lost inside the word “concentrated,” and no unsupported component is omitted
from the inactive case.

## 3. Literal separators and their colour structure

Each separator in the proof is the full open neighbourhood of the displayed
component, not merely a subset of a model boundary.

In the diffuse case, take the common component `K`.  Both poles meet it, so

\[
                  N_G(K)=N_H(K)\mathbin{\dot\cup}\{z,u\}.
\]

A pole-neighbour in a second support component is outside
`K union N_G(K)`: distinct components of the induced two-colour graph are
anticomplete.  Hence `K` and that vertex lie on the two nonempty open sides
of the separation defined by `N_G(K)`.

For a one-sided component `L`, if `p` is its unique adjacent pole, then

\[
                     N_G(L)=N_H(L)\mathbin{\dot\cup}\{p\}.
\]

The refinement supplies a neighbour of `p` in a second two-colour
component.  This vertex lies outside `L union N_G(L)` and gives the nonempty
opposite open side.  The other pole is not silently included in the
boundary because it is anticomplete to `L`.

For an inactive component `L`, both poles are anticomplete to it, so

\[
                            N_G(L)=N_H(L).
\]

The adjacent poles remain together outside `L union N_G(L)`, furnishing a
nonempty opposite side.  This is again an actual graph separation.

In all three cases, an `H`-neighbour of `L` or `K` cannot have colour
`alpha` or `beta`; an edge to such a vertex would put it in the same
component of the induced `alpha,beta` graph.  Therefore the boundary part
inside `H` uses only the other four colours, exactly as outcome 1 states.
Mader's seven-connectivity consequence gives `|N_G(L)|>=7` for every one
of these literal separators.  It gives no upper bound, and the source does
not claim one.

## 4. Five connected dominating cores

If no separator case occurs, then

\[
                 H[A\cup V_\gamma]\text{ is connected}
                 \qquad(\gamma\ne\alpha)
\]

for all five other colours in the single fixed six-colouring.  This is
exactly the full star-Kempe hypothesis of the promoted compression theorem,
not merely connectivity of five selected support subgraphs.

For each choice of `beta`, the set `X=A union V_beta` is consequently the
connected induced bipartite graph used by that theorem.  The same five
connectivity conditions make it dominate `Q=G-X`: a vertex in any other
colour class has an `A`-neighbour, and each pole has a `V_beta`-neighbour.
The compression theorem therefore applies for every `beta` and gives all
five instances of the claimed core data:

- `chi(R)=4`, `chi(Q)=5`, and `Q` is `K_6`-minor-free;
- `chi(Q-z)=chi(Q-u)=5`;
- `R` and the relative neighbourhood
  `N_Q(V_beta)=N_G(V_beta) cap V(Q)` are colourful in every five-colouring
  of `Q`; and
- the two oppositely singleton-rooted near-`K_7` models exist.

The five cores need not coincide or be mutually compatible.  Outcome 2
correctly asserts one core for every choice of `beta`, not one common core
carrying all five choices simultaneously.

## 5. Rooted-`K_4` consequence

Fix one core and put `S=N_R(z)`, `T=N_R(u)`.  Since

\[
               R+z=Q-u,\qquad R+u=Q-z
\]

are five-chromatic while `R` is four-chromatic, both `S` and `T` are
colourful in `R`.  Indeed, if a four-colouring of `R` omitted a colour from
`S`, assigning that colour to `z` would four-colour `R+z`; the argument for
`T,u` is identical.

Suppose `B_1,...,B_4` is a `K_4`-minor model in `R` and each `B_i` meets
both `S` and `T`.  The seven proposed branch sets

\[
                    \{z\},\ \{u\},\ X,\ B_1,\ldots,B_4
\]

are pairwise disjoint and connected.  All 21 required adjacencies are
accounted for as follows:

- the six pairs among `B_1,...,B_4` are adjacent by the `K_4` model;
- `X` is adjacent to each `B_i` because it dominates `Q`;
- `{z}` is adjacent to every `B_i` because `B_i cap S` is nonempty;
- `{u}` is adjacent to every `B_i` because `B_i cap T` is nonempty; and
- among `{z},{u},X`, the edge `zu` gives the first adjacency, while the
  `V_beta`-neighbours of the two poles give the other two.

The counts are `6+4+4+4+3=21`.  Hence these are genuinely seven branch sets
of an explicit `K_7`-minor model in `G`.

## 6. Scope and limitations

The theorem does not bound a returned separator from above or say that it
has order exactly seven.  A diffuse and a one-sided description may apply
to the same support configuration; this redundancy strengthens the
available boundary description and does not affect exhaustion.  The five
core decompositions and their opposite near-`K_7` models need not be
label-compatible.  Finally, colourfulness of `S,T` does not itself supply a
single `K_4` model rooted at both sets: that model is the explicit additional
hypothesis in Section 3.  The theorem therefore reduces to, but does not
solve, the paired colourful-set frontier and does not prove `HC_7`.
