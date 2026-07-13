# Coherent spanning transport from a nonspanning near model

## Status

This is a proved partial `P1` transport lemma.  It does not turn the
deficient bag into the singleton/bipartite shell, but it removes one
quantifier problem: all unused components which meet the deficient bag
select the same missing twin.  They can therefore be absorbed without
creating incompatible local deficient pairs.

The proof is not special to seven labels.  The parameter-uniform form is
recorded first.

## Theorem 1 (uniform missing-star transport)

Let `t>=3`.  Let `G` be connected and `K_t`-minor-free, and let
`A,V_1,...,V_{t-1}` be a labelled, not necessarily spanning model in
which the foreign bags `V_1,...,V_{t-1}` form a `K_{t-1}` model.  Let
`D` be the set of foreign labels not required to be adjacent to `A`, and
assume `A` is adjacent to every foreign label outside `D`.

Union `A` with every component outside the model union which has a
neighbour in `A`, obtaining `A^+`.  Then `A^+` is anticomplete to at
least one bag in `D`.  All remaining exterior components can be absorbed
into foreign bags while preserving one such globally missing spoke.

### Proof

The union `A^+` is connected.  If it met every foreign bag in `D`, it
would meet all `t-1` foreign bags, and those bags together with `A^+`
would be a `K_t` model.  Thus one spoke remains absent.  Distinct
components outside the old model union are anticomplete.  Hence every
remaining exterior component is anticomplete to `A^+`; connectedness of
`G` gives it a neighbour in a foreign bag, into which it may be absorbed
without creating the selected missing spoke.  QED.

For a two-spoke deficiency this selects one fixed missing twin.  With a
larger missing star it guarantees at least one surviving spoke but does
not canonically identify all other contacts.

## Theorem 2 (`K_7^vee` coherent transport)

Let `G` be connected and `K_7`-minor-free, and let

\[
                 A,B,C,U_1,U_2,U_3,U_4
\]

be a labelled, not necessarily spanning, `K_7^vee` model whose only
unprescribed pairs are `AB,AC`.  Let `R` be the union of all components
of

\[
 G-\bigl(A\cup B\cup C\cup U_1\cup\cdots\cup U_4\bigr)
\]

which have a neighbour in `A`.  Then:

1. `A^+=A\cup R` is connected;
2. one of `B,C` is anticomplete to `A^+`;
3. the model can be made spanning by replacing `A` with `A^+` and
   absorbing every remaining unused component into a foreign bag, while
   preserving that same missing pair.

### Proof

The six foreign bags

\[
                         B,C,U_1,U_2,U_3,U_4
\]

are connected, pairwise disjoint and pairwise adjacent, so they form a
`K_6` model.  Every component included in `R` is connected and has an
edge to the connected bag `A`.  Hence their union with `A` is connected.

The old bag `A` is adjacent to all four `U_i`.  If `A^+` were also
adjacent to both `B` and `C`, then

\[
                  A^+,B,C,U_1,U_2,U_3,U_4
\]

would be seven connected, disjoint and pairwise adjacent branch sets,
contrary to `K_7`-minor-freeness.  Thus `A^+` is anticomplete to at least
one fixed member `D` of `{B,C}`.

It remains to span the model.  A component not included in `R` has no
edge to `A`.  It also has no edge to a component included in `R`, since
both are distinct components of the graph outside the old model union.
Consequently it has no edge to `A^+`.  Since `G` is connected, it has an
edge to at least one foreign bag.  Absorb it into any such bag.
The enlarged bag is connected and retains all of its old model
adjacencies.  Repeating this for every remaining component gives a
spanning model.  No absorption creates an edge between `A^+` and `D`,
because every absorbed component was anticomplete to `A^+`.  The same
fixed pair `A^+D` therefore remains absent.  \(\square\)

## Corollary (transport of the normalized path core)

Apply the theorem to the deficient-first model in
`../results/hc7_near_k7_deficient_path_normalization.md`.  The resulting
spanning deficient bag has an induced path core whose four original
neutral portal classes are singleton `2+2` endpoint classes.  Every
added piece is an entire old exterior component meeting that core, and
the union of the core and all added pieces is anticomplete to one fixed
twin `B` or `C`.

This is strictly weaker than `P1`: absorbing the exterior components can
destroy bipartiteness and can add new neutral portals.  Its content is
that these pieces cannot choose different deficient twins.  Any further
normalization may therefore work relative to one fixed missing label.

If the host is seven-connected, each old exterior component `K` absorbed
into `A^+` has

\[
 |N_G(K)|\ge 7,
 \qquad
 N_G(K)\subseteq A\cup
       \bigl(\{B,C,U_1,U_2,U_3,U_4\}\setminus\{D\}\bigr),
\]

where a bag name in the containment denotes its vertex set.  Distinct
old exterior components have no edges between them, and coherence gives
no edge from `K` to the fixed missing twin `D`.  Thus every added lobe
comes with an actual order-at-least-seven adhesion on the same five-label
side.  This is the precise interface at which the rigid-boundary splice
or a labelled rerouting theorem must act.

In a seven-connected, non-six-colourable, `K_7`-minor-free target, the
audited exact-seven boundary theorem sharpens this further.  If
`|N_G(K)|=7`, every component of `G-N_G(K)` is full to that cut.  Hence
the missing-edge graph of `G[N_G(K)]` must have at least six edges;
otherwise the exact-seven crossing/web closure gives a `K_7` minor or a
six-colouring.  Thus a surviving transported lobe has either adhesion at
least eight or an exact-seven boundary with at least six defects.

## Scope caution

Connectedness of `G` is used only to ensure that an unused component not
meeting `A^+` has a foreign bag into which it can be absorbed.  In a
disconnected host, apply the statement to the component containing the
model; other components are irrelevant to both the model and chromatic
number reduction.
