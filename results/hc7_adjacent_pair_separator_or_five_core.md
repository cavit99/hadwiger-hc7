# Adjacent-pair two-colour separation or five-chromatic core

**Status:** written proof; separate internal audit GREEN.  This theorem
combines promoted colouring lemmas into the current top-level dichotomy.
It does not prove `HC_7`.

## 1. Statement

Let `G` be a seven-chromatic graph with no `K_7` minor such that every
proper minor of `G` is six-colourable.  Let `zu` be an edge for which

\[
                         \chi(G-\{z,u\})=6,            \tag{1.1}
\]

put `H=G-{z,u}`, and fix the six-colouring of `G-zu` supplied by the
global adjacent-pair palette theorem.  Thus `z,u` have one common colour
`alpha`; the nonempty `alpha`-class `A` in `H` is anticomplete to
`{z,u}`; and both poles have a neighbour of every other colour.

For a colour `beta != alpha`, let `V_beta` be its colour class in `H` and
put

\[
                         X_\beta=A\cup V_\beta.        \tag{1.2}
\]

### Theorem 1.1

At least one of the following holds.

1. **Two-colour separation.**  For some `beta != alpha`, a component `L`
   of `H[X_beta]` has `N_G(L)` as the boundary of an actual separation
   with two nonempty open sides.  The part

   \[
                         N_G(L)\cap V(H)               \tag{1.3}
   \]

   uses only the four colours outside `{alpha,beta}`.  Consequently
   `|N_G(L)|>=7`.

2. **Connected-dominating five-core.**  For every `beta != alpha`, the
   graph `H[X_beta]` is connected.  For each such `beta`, on putting

   \[
      X=X_\beta,\qquad Q=G-X,\qquad R=H-X,             \tag{1.4}
   \]

   all of the following hold:

   - `X` is a connected induced bipartite subgraph dominating `Q`;
   - `chi(R)=4`, `chi(Q)=5`, and `Q` has no `K_6` minor;
   - `chi(Q-z)=chi(Q-u)=5`;
   - both `R` and `N_Q(V_beta)` are colourful in every five-colouring of
     `Q`; and
   - `G` has the two oppositely rooted seven-branch near-`K_7` models
     described in the connected two-colour compression theorem.

The two-colour separation alternative does not assert that the separator
has order exactly seven.  The connected-dominating alternative does not
assert that either near-`K_7` model can be completed.

## 2. Proof

Fix `beta != alpha`.  The adjacent-pair bichromatic-support theorem gives
at least one component of `H[X_beta]` containing a `beta`-coloured
neighbour of both poles.

If pole support occurs in more than one component, the diffuse-support
alternative of that theorem gives a component `L` for which `N_G(L)` is
an actual separator.  If there is a component which contains a pole
neighbour on only one side, its one-sided refinement gives the same
conclusion.  In either case, every neighbour of `L` inside `H` has a
colour outside `{alpha,beta}`: a neighbour of either displayed colour
would belong to the same component of the induced two-colour graph.

It remains to consider the case in which all pole support is concentrated
in one common component `K_beta`.  If `H[X_beta]` has another component
`L`, then `L` is inactive: it contains no `beta`-coloured neighbour of
either pole.  The concentrated-rotation normalization theorem proves that
`L` is anticomplete to both poles and that

\[
                         N_G(L)=N_H(L),                \tag{2.1}
\]

which again uses only the four colours outside `{alpha,beta}` and is the
boundary of an actual separation.  Since `G` is seven-connected, every
separator obtained in these cases has order at least seven.

Therefore, if outcome 1 never occurs, `H[X_beta]` is connected for every
`beta != alpha`.  These five connectivity assertions are exactly the
star-Kempe hypothesis of the connected two-colour compression theorem.
Applying that theorem separately for every `beta` gives all assertions in
outcome 2. \(\square\)

## 3. Immediate rooted-minor consequence

Fix `beta` in outcome 2 and retain the notation (1.4).  Put

\[
                         S=N_R(z),\qquad T=N_R(u).
\]

Both `S,T` are colourful in the four-chromatic graph `R`, because
`R+z=Q-u` and `R+u=Q-z` are five-chromatic.  If `R` has a `K_4` model each
of whose branch sets meets both `S` and `T`, then

\[
                       \{z\},\ \{u\},\ X
\]

together with those four branch sets is an explicit `K_7`-minor model.
This reduces outcome 2 to the paired colourful-set frontier; it does not
solve that frontier.

## 4. Promoted inputs

- [global adjacent-pair palette frame](../results/hc7_global_adjacent_pair_palette_frame.md)
- [bichromatic support and exact missing-colour rotation](../results/hc7_adjacent_pair_bichromatic_support_dichotomy.md)
- [concentrated-rotation normalization and separator](../results/hc7_concentrated_rotation_normalization.md)
- [connected two-colour compression to a five-chromatic core](../results/hc7_star_kempe_five_core_compression.md)
