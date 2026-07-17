# Independent audit: palette-permutation linkage at an adjacent pair

**Audited source:** `hc7_adjacent_pair_palette_linkage.md`
**SHA-256:** `8fe432cff08f5bf638f908b382bf75548be379f1a3fcee8ee7858149064ac801`
**Verdict:** **GREEN.**

**Promoted source SHA-256:**
`2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2`.
The only change is the status-line update recorded in the revision note.

The colouring arguments, the five-path application of Menger's theorem,
the contact-profile deductions, and the invocation of the audited rooted
branch-set split are correct.  The theorem is strictly local: the five
paths preserve the two endpoint palettes only up to a permutation, and
the separator produced by the branch-set split has no proved upper bound
or compatible boundary colouring.

## 1. Hypotheses and the edge-deletion colouring

Because edge deletion is a minor operation, `G-zu` has a proper
six-colouring.  Its ends must receive the same colour: otherwise restoring
`zu` would give a six-colouring of `G`.  Properness excludes that colour
from both pole neighbourhoods.  If either pole missed one of the other
five colours, recolouring that pole and restoring `zu` would again
six-colour `G`.  Thus Lemma 2.1 correctly obtains five saturated neighbour
colours at both poles.

The assertion that the common pole colour occurs in `H` also follows:
otherwise the restriction to `H` would use at most five colours, contrary
to `chi(H)=6`.  This remains valid if the initial colouring was presented
with an unused colour label, since the saturation argument itself forces
all five non-pole colours to occur.

## 2. Kempe-component argument

Lemma 2.2 is valid, including its formulation for a set `T` of several
colours.  Let `K` be the component containing `z` in the subgraph induced
by `T` together with the common pole colour.  If `u` is outside `K`, then
interchanging the common colour with any fixed colour in `T`, only on
`K`, preserves properness:

- within `K` this is an ordinary transposition of two colour names; and
- no vertex outside `K` with any colour in the induced palette is
  adjacent to `K`, by the definition of an induced component.

The poles then have different colours, so restoring `zu` contradicts
`chi(G)=7`.  Taking `T` to be a singleton gives each asserted
two-colour pole-to-pole path.  Paths for two different non-pole colours
can share an internal vertex only when that vertex has the common pole
colour, exactly as stated.  The lemma does not assert that the five such
paths can be chosen simultaneously disjoint.

## 3. Audit of the five-path linkage

The selected sets `A` and `B` each have order five because their members
have pairwise distinct colours.  A vertex in `A cap B` necessarily has
the same colour role on both sides.  Assigning every such vertex a trivial
path is therefore legitimate.

If `I=A cap B`, then deletion of `I` from the five-connected graph `H`
leaves a `(5-|I|)`-connected graph.  The residual terminal sets are
disjoint and each has order `5-|I|`.  The set form of Menger's theorem
therefore gives that many vertex-disjoint paths between them.  More
explicitly, a separator of smaller order would leave a terminal from each
set outside the separator; if the remaining graph were connected, those
two terminals would still be joined, so such a separator would contradict
`(5-|I|)`-connectivity.  The zero-path case `|I|=5` is already covered by
the five trivial paths.

The Menger paths may be truncated at their first and last selected
terminals.  Together with the trivial paths they cover each selected
terminal exactly once.  Adding the incident pole edges therefore gives
five pairwise internally vertex-disjoint `z`--`u` paths.  Their pairing
may permute the five colours; no same-colour pairing is claimed.  Thus the
word “palette” records the two complete endpoint palettes, not colours on
the interiors of the linkage paths.

## 4. Four common branch sets

Suppose the contact intersection has order four.  If each pole has an
exclusive branch set, the union of one exclusive branch set from each
side is connected because all branch sets of the `K_6` model are pairwise
adjacent.  That union, the four common branch sets, and the two singleton
poles form seven pairwise adjacent connected branch sets.  Consequently,
in a `K_7`-minor-free host the contact set of one pole is contained in the
other.  After orienting the poles, `u` contacts exactly the four common
branch sets.

The five saturated neighbour colours of `u` are distributed among those
four branch sets, so one contains two distinct neighbours of `u`.  Any
neighbour of `z` in that same common branch set differs from at least one
of them.  This supplies the two distinct rooted vertices required by
Lemma 4.1 of the audited two-pole contact trichotomy.

That cited split does give the exact conclusion used here.  Deleting an
edge on the root-to-root path of a spanning tree partitions the branch
set into two nonempty connected adjacent parts.  If both parts meet every
other model branch set, adjoining the appropriate pole to each part gives
an explicit `K_7`-minor model.  Otherwise a part `Y` is anticomplete to a
foreign branch set, and its full external neighbourhood `N_G(Y)` separates
`Y` from that foreign branch set.  Seven-connectivity proves only
`|N_G(Y)| >= 7`; it does not prove equality.  The source preserves this
trust boundary.

## 5. Three common branch sets

Under the no-separator hypothesis of Corollary 5.1, a common branch set
cannot have distinct pole neighbours: in a `K_7`-minor-free host the
audited split would otherwise return the excluded separator.  Therefore
the two nonempty pole-neighbourhoods in each common branch set coincide
in one vertex.

Those three portal vertices account for at most three of the five
saturated neighbour colours, so each pole must contact an exclusive
branch set.  A union of contacts of order six would let the connected
set `{z,u}` meet all six model branch sets and would form a `K_7` minor.
Hence the union has order at most five.  Starting with three common branch
sets leaves exactly one exclusive branch set for each pole and one branch
set contacted by neither pole.  At least two saturated colours at each
pole are absent from the three common portal vertices, so the associated
exclusive branch set contains neighbours in at least two distinct
colours.  All four claims in Corollary 5.1 follow.

For every colour absent from the common portals, all pole neighbours of
that colour lie in the appropriate exclusive branch set.  Lemma 2.2 then
places the first and last internal vertices of the corresponding
two-colour pole path in the two exclusive branch sets.  Finally, two
chosen, differently coloured neighbours on each side form disjoint
two-element terminal sets; five-connectivity and Menger yield two
vertex-disjoint paths between them.  Their pairing may interchange the
two colours, as Corollary 5.2 explicitly allows.

## 6. Adversarial guardrails

The two available `K_2`-join icosahedron checks were rerun.

- `barriers/hc7_same_row_split_two_apex_icosahedron_check.py` confirms a
  seven-connected, `K_7`-minor-free host with exactly four common-contact
  branch sets and distinct pole roots in one common branch set.  Each of
  the two possible rooted pieces misses a foreign branch set, and the
  resulting external neighbourhood has order seven.  Thus it realizes,
  rather than refutes, the separator alternative of Theorem 4.1.
- `active/hc7_atomic_two_pole_contact_trichotomy_verify.py` confirms the
  separate contact-five rotation guardrail.  It does not satisfy the
  seven-chromatic/minor-critical hypotheses, and so cannot refute the
  palette lemmas; it correctly warns that contact geometry alone cannot
  orient the model.

The same-row icosahedral graph is six-colourable and has the two universal
vertices as a coherent two-vertex terminal.  It therefore establishes
the sharp scope of the theorem: seven-connectivity, a spanning contact-
maximal model, and rooted branch-set geometry do not eliminate the
separator outcome.  The proper-minor colouring response or a global
two-vertex terminal remains indispensable.

## 7. Promotion boundary

The audited source may be used for the following claims:

1. every adjacent pair with six-chromatic two-vertex deletion has a
   common-colour edge-deletion colouring saturating five neighbour colours
   at each end;
2. those endpoints admit five internally disjoint paths whose endpoint
   colours form the two complete five-colour palettes, paired by a
   permutation;
3. four common-contact branch sets reduce to an explicit `K_7`-minor
   model or an actual separator; and
4. after excluding that separator mechanism, three common-contact branch
   sets have the exact profile in Corollary 5.1 and the two-linkage in
   Corollary 5.2.

It may not be cited as proving an order-seven separation, a common
boundary colouring, a colour-preserving five-linkage, a fixed two-vertex
`K_5`-minor transversal, or `HC_7`.

## Revision note

The audited source had SHA-256
`8fe432cff08f5bf638f908b382bf75548be379f1a3fcee8ee7858149064ac801`.
Promotion changed only its status line from “independent audit pending” to
“separately audited”; every mathematical statement and proof is otherwise
unchanged from the audited revision.
