# Independent audit: star-Kempe five-core compression

**Audited source:** `hc7_star_kempe_five_core_compression.md`
**SHA-256:** `45e3d2e1a8aab16690c3941e5013c0f5bdc296ab257cea042dab1ceec7cb5557`
**Verdict:** **GREEN.**

The promoted revision differs from the initially audited source only in
changing its status line from “audit pending” to “audit GREEN”; the
mathematical statement and proof are unchanged.

The conditional theorem is correct at the audited revision.  The
star-Kempe hypothesis makes the selected two-colour subgraph a connected
induced bipartite dominating subgraph; its contraction leaves a tight
five-chromatic core.  The two singleton-rooted near-`K_7` models lift
correctly from Martinsson--Steiner's Corollary 1.4.

This verdict is for the theorem as stated, which assumes the full
star-Kempe condition.  Deriving that condition from the earlier rotation
analysis requires both concentration and absence of inactive components,
as recorded precisely in Section 7 below.

## 1. Sets, induced subgraphs, and notation

All six colour classes of `phi` are nonempty because `chi(H)=6`.  Hence
`A` and `B=V_beta` are nonempty independent sets.  Since

\[
                         X=A\cup B,
\]

the graph actually used throughout the proof is

\[
                 G[X]=H[X]=H[A\cup B].
\]

It is induced, bipartite with sides `A,B`, and connected by the
star-Kempe hypothesis.  In particular `|X|>=2`, so contracting a spanning
tree of `G[X]` produces a proper minor of `G`.

The deletion notation is consistent:

\[
  Q=G-X=G[V(R)\cup\{z,u\}],\qquad R=H-X=Q-\{z,u\}.
\]

Thus `Q` is the induced residual graph, not the bipartite subgraph called
`Q` in the separate bipartite-contraction theorem.  Since `B` is outside
`Q`, the source explicitly and correctly uses the relative-neighbourhood
notation

\[
                    N_Q(B)=N_G(B)\cap V(Q).
\]

The same convention gives `N_Q(A)=R`: every vertex of `R` has an
`A`-neighbour by the domination argument below, and `A` is anticomplete to
the two remaining vertices `z,u` of `Q`.

## 2. Connectivity and domination

For `v in R` of colour `gamma`, the full induced graph
`H[A union V_gamma]` is connected and contains both nonempty sides.  Hence
`v` is not isolated there.  Its neighbour in this bipartite graph lies in
`A`, so every vertex of `R` has a neighbour in `X`.  Each pole has a
`beta`-coloured neighbour by the palette hypothesis, and that neighbour
lies in `B subseteq X`.  Therefore `G[X]` is connected and dominates every
vertex of `Q`, exactly as item 1 requires.

No stronger interpretation of domination is used: it means that every
vertex outside `X` has at least one neighbour in `X`.

## 3. Chromatic equalities and the contraction

The four original colour classes outside `A,B` give `chi(R)<=4`.  If
`R` were three-colourable, a disjoint two-colour palette on the induced
bipartite graph `G[X]` would five-colour `H`, contradicting `chi(H)=6`.
Thus `chi(R)=4`.

Contract `G[X]` to a vertex `x`.  Domination makes `x` adjacent to every
vertex of `Q`, while contraction does not alter edges within `Q`.  Hence

\[
                         G/X=K_1\vee Q
\]

as a simple graph and `chi(G/X)=chi(Q)+1`.  The proper-minor hypothesis
gives `chi(Q)<=5`.  A four-colouring of `Q`, together with two new colours
on `G[X]`, would six-colour `G`; therefore `chi(Q)=5` and
`chi(G/X)=6`.

If `Q` had a `K_6`-minor model, the connected branch set `X` would be
adjacent to each of its six branch sets by domination.  This lifts it to a
`K_7`-minor model in `G`, contrary to the setup.  Thus the asserted
`K_6`-minor exclusion is valid.

## 4. Colourful sets and pole deletions

Let `psi` be any proper five-colouring of `Q`.

If a colour `delta` is absent from `R`, colouring `A` with `delta` and
`B` with a new sixth colour is proper.  The only possible neighbours of
`A` outside `X` are in `R` or at the poles; `delta` is absent from the
first and `A` is anticomplete to the second.  The new colour on `B` occurs
nowhere in `Q`, and the two sides of `G[X]` receive different colours.
This would six-colour `G`.

Likewise, if `delta` is absent from `N_Q(B)`, colouring `B` with `delta`
and `A` with a new sixth colour is proper and again six-colours `G`.
Consequently both `R=N_Q(A)` and `N_Q(B)` use all five colours in every
proper five-colouring of the five-chromatic graph `Q`; in the standard
terminology, both are colourful sets in `Q`.

If `Q-z` were four-colourable, assigning a new fifth colour to `z` would
give a five-colouring of `Q` in which `R subseteq Q-z` uses at most four
colours, contradicting the preceding conclusion.  Hence `chi(Q-z)=5`;
the upper bound follows from `Q-z subseteq Q`.  The argument for `Q-u` is
identical.

The colourful-set conclusions do not themselves invoke Strong Hadwiger at
chromatic number five.  In particular, the source does not infer a `K_5`
model simultaneously rooted at `R` and `N_Q(B)`.

## 5. Martinsson--Steiner and the two minor lifts

A five-chromatic graph contains a five-vertex-critical subgraph, so choose
`C_u subseteq Q-z`.  Because

\[
                         Q-z=R\cup\{u\}
\]

and `R` is four-colourable, `u` must belong to `C_u`.  Martinsson and
Steiner's Corollary 1.4 states exactly that, for every vertex `v` of a
five-vertex-critical graph, there is a `K_5`-minor model having `{v}` as a
singleton branch set.  Applying it with `v=u` gives

\[
                         \{u\},M_1,\ldots,M_4
\]

inside `Q-z`.  The citation, theorem number, and prescribed-vertex
quantifier are correct:

A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
Corollary 1.4.

The lift to (2.1) preserves all branch-set requirements.  The sets are
pairwise disjoint because the five model sets lie in `Q-z`, `X` is
disjoint from `Q`, and `{z}` is the omitted pole.  They are connected.
The old five sets are pairwise adjacent; domination makes `X` adjacent to
all five; and `z` is adjacent to `{u}` through `zu` and to `X` through a
`B`-neighbour.  The only unproved adjacencies are therefore precisely
`({z},M_i)`.  Interchanging the poles gives (2.2).  If the outside pole has
the four missing contacts, all seven branch sets are pairwise adjacent and
form the claimed explicit `K_7`-minor model.

## 6. The four-colour Strong Hadwiger remark

Martinsson--Steiner's Theorem 1.3 roots a `K_4`-minor at one colourful set
in a four-chromatic graph.  It does not synchronize two colourful sets.
The source's two-`K_4` bridge example correctly shows why such
synchronization is not formal: each copy of `K_4` is colourful in the
four-chromatic graph, but every connected set meeting both copies must use
the unique bridge and its endpoints, so disjoint branch sets cannot all
meet both copies.

## 7. Exact bridge from the no-inactive residue

Fix a nonbuffer colour `gamma`.  The promoted bichromatic-support theorem
first guarantees at least one common component of

\[
                         H[A\cup V_\gamma].
\]

To derive the star-Kempe hypothesis from the earlier residue analysis, the
following two exclusions are both necessary:

1. the diffuse-support alternative is excluded, so the pole-support set
   consists of one common component `K_gamma`; and
2. there is no inactive `alpha`--`gamma` component in the chosen
   colouring.

Under the first condition, every component other than `K_gamma` is
inactive by definition.  The second condition therefore says that no such
other component exists, and hence

\[
                         H[A\cup V_\gamma]=K_\gamma
\]

is connected.  Doing this for all five nonbuffer colours gives exactly
the star-Kempe condition (1.1).  Conversely, (1.1) immediately implies
concentrated support and no inactive component for every nonbuffer colour.

Thus, at a fixed colouring,

\[
\text{star-Kempe}
\quad\Longleftrightarrow\quad
\text{all five supports are concentrated and have no inactive component}.
\]

The orbit-wide absence of inactive components from the rotation-normal-form
theorem is stronger than needed once every support is concentrated, but it
does **not** by itself rule out a diffuse colour: a diffuse candidate is not
an available direct transition.  Nor does merely excluding order-seven
separators suffice, because the diffuse and inactive-component separators
can have larger order.  Any downstream application of the present theorem
from a "no-inactive residue" must retain these quantifiers and first dispose
of every diffuse-support alternative.

## 8. Assumptions and limitations

- The proof uses the standard finite-simple-graph convention.  Finiteness
  is needed when selecting a five-vertex-critical subgraph and when invoking
  Martinsson--Steiner.
- The theorem is conditional on one six-colouring satisfying all five full
  two-colour connectivity conditions.  The global adjacent-pair theorem
  supplies the palette setup, but not the star-Kempe condition by itself.
- Returned separators in the preceding support analysis may have order
  greater than seven.  This theorem does not close or colour-glue them.
- The two colourful sets in `Q` do not yield a simultaneous two-root model,
  and the two opposite near-`K_7` models need not be label-compatible.
- The result gives no `K_7` minor unless one outside pole contacts all four
  remaining branch sets in one of the displayed models.  It therefore does
  not prove `HC_7`.

No mathematical correction to the audited source is required.
