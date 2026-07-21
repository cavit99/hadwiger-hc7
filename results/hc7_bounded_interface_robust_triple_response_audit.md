# Independent audit: robust independent-triple concentration

**Verdict:** **GREEN** at the exact revision below, conditional on the
GREEN-audited low-degree alignment and exact-block Kempe reduction used in
the setup.  The audit found one omitted inherited hypothesis in the first
revision: the proof uses the contraction-critical bound
`alpha(G[S])<=4`.  That bound is now stated explicitly as (1.3), together
with `|S-I|>=3` for every independent block under consideration.

## Exact revision audited

```text
821903be3a374ccf69552a4f0209cc82ac7e466f7fcea04b97123c17c8ce94db  audited theorem content before status-only promotion
```

Promotion changed only the status paragraph and audit link.  The promoted
source hash is

```text
42d50b8027bd5acabf986b803cffef9fe5bf402add892d58778d5a2d0bc2d064  results/hc7_bounded_interface_robust_triple_response.md
```

The verdict covers Theorem 2.1, Theorem 3.1, Corollary 4.1, the sentence
following Corollary 4.1, and all stated quantifiers and trust-boundary
limitations.  Any mathematical change to the source invalidates this verdict
until the audit is renewed.

## 1. Setup and the corrected independence bound

The setup retains the exact hypotheses needed from the audited bounded-
interface programme:

- `C` is a component of `G-N[u]`;
- `S=N_G(C) subseteq N(u)` and `7<=|S|<=d_G(u)<=9`;
- every proper minor of `G` is six-colourable;
- every nonempty independent `I subseteq S` occurs as one exact boundary
  colour class on each closed shore; and
- the labelled exact-`I` boundary cylinder is Kempe-connected by moves
  avoiding the colour on `I`.

The contraction-critical neighbourhood bound gives

```text
alpha(G[S]) <= alpha(G[N(u)]) <= d_G(u)-5 <= 4.
```

Consequently every independent `I subseteq S` has
`|S-I|>=7-4=3`.  The original source hash supplied for audit omitted this
display even though the later assertion `f_I in binom(S-I,2)` depends on the
same inherited bound.  Display (1.3) repairs that omission without changing
the argument or strengthening the inherited theorem.

## 2. The star contraction and its expanded colouring

For nonempty independent `I`, the subgraph on `{u} union I` is a connected
star.  Contracting its edges is a genuine proper-minor operation.  In a
six-colouring of the contraction, give `u` and every member of `I` the colour
of the contraction image `w` when expanding.

This expansion is exactly a proper colouring of `G-E_I`:

- the only edges inside `{u} union I` are the deleted star edges `ui`, since
  `I` is independent; and
- every vertex outside the star which is adjacent to one of its vertices is
  adjacent to `w` in the contraction and therefore has a different colour.

Every vertex of `S-I` is adjacent to `u`, so none has the colour `gamma` of
`w`.  Thus `I` is exactly the `gamma`-class on the literal boundary.  No
claim is made that it is the complete `gamma`-class outside `S`, and the
proof does not need such a claim.

## 3. Kempe lifting and the gluing contradiction

Choose an exact-`I` six-colouring of the original closed shore `B` and align
the name of the colour on `I` with `gamma`.  Exact-cylinder connectivity
then supplies a labelled boundary sequence all of whose moves avoid
`gamma`.

Starting from the expanded colouring of `G-E_I`, a requested boundary move
on a two-colour component `W` lifts by swapping the full two-colour
component meeting `W`, unless that full component also meets another
boundary component.  In the latter event, a shortest path inside the full
component between the two boundary components has no internal boundary
vertex.  This is precisely the standard lift-or-interior-path alternative;
no contraction or recolouring is being applied to the path itself.

If every move lifted, restrict the final colouring to `A=G[C union S]`.
This restriction colours the original graph `A`, because every deleted edge
`ui` lies in `B=G-C`, not in `A`.  Its labelled boundary colouring equals
the chosen colouring of the original `B`.  The two colourings therefore
glue on `S`.  Since `S=N_G(C)`, there are no omitted cross-shore edges, and
the colouring on `B` restores all edges `ui`.  The glued colouring would be
a proper six-colouring of `G`, a contradiction.  Hence a failed lift exists.

All moves avoid `gamma`, so throughout the sequence `u` and `I` retain
colour `gamma`.  The failed two-colour path consequently avoids them.  Its
interior avoids `S`; and because there is no edge from `C` to `B-S`, that
interior lies wholly in `C` or wholly in `B-(S union {u})`.  Its two ends
lie in `S-I` and in distinct components of the relevant two-colour graph on
`S`.  An edge between them in `G[S]` would join those components, so their
pair is a literal boundary nonedge.  This verifies every assertion of
Theorem 2.1.

## 4. The robust-family quantifiers

For each root `x`, Theorem 2.1 makes `mathcal E_x` nonempty, and every pair
in that family both avoids `x` and is a boundary nonedge.  Hypothesis (3.2)
is correctly universal only across two *distinct* root indices; no
intersection assertion inside one family is used.

Choose one baseline pair from every family.  The universal cross-family
condition makes the selected two-sets pairwise intersecting.  They cannot
all have one value `{a,b}`, since the selected pair indexed by `a` would
contain its forbidden root.  A pairwise-intersecting family of at least two
distinct two-sets is contained in a star or in the three edges of a
triangle.  A star with centre `q` is impossible because the selected pair
indexed by `q` would contain `q`.  Thus the baseline family lies in
`binom(Q,2)` for a three-set `Q`.

For each `q in Q`, root avoidance leaves exactly the pair `Q-{q}`.  Hence
all three edges of `Q` actually occur, and their nonedge property makes `Q`
independent.

Now replace one baseline pair, at an arbitrary index `x`, by an arbitrary
member of `mathcal E_x`.  The selection is still pairwise intersecting by
(3.2), and it still cannot be one-valued by root avoidance.  It therefore
lies in the edges of a triangle `Q'`.

- If `x notin Q`, the unchanged pairs indexed by the three vertices of `Q`
  are all three edges of `Q`, forcing `Q'=Q`.
- If `x in Q`, the two unchanged pairs indexed by `Q-{x}` have union `Q`,
  so the only triangle containing both is again `Q`.

This proves `mathcal E_x subseteq binom(Q,2)` for every `x`, and for
`q in Q` root avoidance again leaves the singleton family
`{Q-{q}}`.  The arbitrary-witness substitution is legitimate because all
other baseline choices stay fixed; this verifies the full robust
quantifier in Theorem 3.1.

## 5. The exact-triple response

The set `Q` is a nonempty independent set, so Theorem 2.1 applies with
`I=Q` and returns a pair in `binom(S-Q,2)`.  This pair is disjoint from
every singleton-response pair because Theorem 3.1 places all of those
pairs inside `Q`.  Applying Theorem 2.1 with `I=Q-{q}` similarly returns a
pair avoiding the forced pair `Q-{q}`.  These are terminal-pair statements
only; neither application places the paths in one colouring or makes their
interiors disjoint.

## Trust boundary

The source correctly stops at robust concentration and disjoint endpoint
pairs.  It does not infer a common colouring, internally disjoint paths, a
labelled `K_6` boundary model, a common shore partition, or a bounded
same-form restart.  In particular, the universal family condition (3.2)
is a hypothesis, not a consequence of selecting three witnesses with the
triangle pattern.
