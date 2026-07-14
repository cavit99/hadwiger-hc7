# Audit: atomic bichromatic-bridge state localization

**Verdict:** GREEN at frozen source SHA-256
`88070e23ca1b0d8d51e8ba34c177a29c6779bd218c77aea71e649cc0128984de`.

The separating-edge localization, the common-state five Kempe locks, the
opposite-shore `B-C` connector, and the final edge-Menger dichotomy are
correct for both permitted edge types:

* `f` has both ends in the rich open shore `R`; or
* `f` has one literal boundary end in `S` and one rich end in `R`.

The conclusion is still a local state-and-connector theorem.  It does not
couple the localized state to the compulsory edge `zu`, turn the connector
into two carriers, or close the atomic cell.

## 1. The two permitted separator-edge types are exhaustive

The boundary blocks `B,C` are individually independent and are assumed
anticomplete to one another.  No edge of the two-colour graph `K` can
therefore have both ends in `S`: its boundary endpoints would lie in `B`,
in `C`, or one in each, and all three possibilities are nonedges.  Hence
every edge of `K` has at least one end in `R`.  A separating edge is either
rich-internal or a boundary--rich incidence edge, exactly as stated.

Orient `f=xy` so that the component of `K-f` containing `x` meets `B` and
the component containing `y` meets `C`.  The hypotheses ensure that these
components are distinct and that neither meets both blocks.  This remains
valid if `x` or `y` itself is the relevant boundary vertex.

## 2. Component swaps give the exact compressed boundary state

Swap the two names `b,c` on every component of `K-f` meeting `B`.
No swapped component meets `C`.  Thus every member of `B` changes from
`b` to `c`, every member of `C` keeps colour `c`, and no other boundary
block is affected because no other block uses either colour.  The resulting
colouring `c'` is proper on `G[R union S]-f` and has exact boundary
partition `Pi/BC`.

The original edge `xy` is bichromatic.  Its `x`-component is swapped and
its `y`-component is not, so its two ends become equal under `c'`.  This
argument is unchanged when one endpoint is a literal member of `B` or
`C`.

## 3. Packet reflection and gluing remain legal at a boundary incidence

The two disjoint `S`-full packets reflect `Pi/BC` onto the untouched
closed shore `G[A union S]` whenever its demand is at most two.  The
reflection operation is performed in the original rich closed shore; it
does not depend on whether `f` lies inside a selected packet, joins a packet
to a boundary block, or joins two different carrier sets.  All such edges
are harmless extra adjacencies in the packet contraction.  The exceptional
reflection outcome is a literal `K_7`, excluded by hypothesis.

After a palette permutation, this opposite-shore colouring agrees with
`c'` on every literal vertex of `S`.  Their union is a proper colouring of
`G-f`: all `A-S` and `A-A` edges are covered on the first side, all
`R-S` and `R-R` edges except the deleted `f` are covered on the second,
and there are no `A-R` edges.

The equality of the ends of `f` makes this colouring descend to `G/f`.
If one end is `s in S`, the contraction identifies `s` only with one rich
vertex.  No two literal members of `S` are identified, so the contracted
image can retain the label `s`; pulling its colour back to the original
copy of `s` gives exactly the same partition `Pi/BC`.  Thus the deletion
and contraction claims of Theorem 2.1 are both literal and valid in the
boundary-incidence case.

## 4. All five `f`-locks coexist in that one colouring

Let the equal endpoint colour be `gamma`.  If, for another colour `delta`,
the `gamma-delta` component containing `x` omitted `y`, swapping that
component would leave a proper colouring of `G-f` in which the ends of
`f` differ.  Restoring `f` would then six-colour `G`.  Therefore the ends
belong to one such component for each of the other five colours.  This
uses neither endpoint being internal to `R`; a boundary endpoint is an
ordinary vertex of the edge-deleted graph for the Kempe argument.

The corollary asserts coexistence in one colouring, not disjointness of the
five paths, and is correct at that scope.

## 5. The old-colour lock necessarily traverses `A`

On `R union S`, the component swaps preserve the vertex set of the
`b,c`-induced graph.  Hence an `x-y` old-colour lock lying wholly in
`R union S` would be an `x-y` path in `K-f`, contradicting separation of
the oriented `B`- and `C`-components.  Every such lock therefore meets
`A`.

After compression, colour `b` is absent from the literal boundary and the
only boundary vertices of the two lock colours are the members of
`B union C`, all coloured `c`.  Delete the vertices of `A` from a lock
path.  Its first remaining segment is in the `B`-component of `x`, and its
last is in the `C`-component of `y`; either segment may be a singleton
boundary endpoint in the incidence-edge case.

Every intermediate segment adjacent to an `A`-excursion contains a literal
boundary vertex, because there is no `A-R` edge.  Such a boundary vertex
lies in `B union C`.  Consequently every segment in the sequence has a
unique type `B` or `C`; a component of `K-f` meeting neither block cannot
occur between two visits to `A`.  At the first change of type, the maximal
intervening subpath has one endpoint in each block and all internal vertices
in `A`.  This proves Theorem 2.3 for both edge types.

## 6. Final-two-duty demand and the exhaustive dichotomy

When `B,C` are the final two equality blocks meeting `J`, their merge is
exactly

```text
I | J
```

or

```text
I | J | K_0,
```

where the optional `K_0` block is one retained singleton.  The respective
packet demands are at most two, so every separating edge of either
permitted type satisfies the localization theorem.

If one edge separates all `B-C` paths, choose it on a surviving
`B-C` connection and orient its two post-deletion components toward the
two blocks.  Section 1 shows that it is rich-internal or boundary--rich, so
Theorems 2.1--2.3 apply.  If no single edge separates the two terminal
sets, the edge form of Menger's theorem supplies two edge-disjoint
`B-C` paths.  This proves the dichotomy in Section 4.  The paths may share
vertices or terminals and may traverse both selected packets; the source
correctly claims only edge-disjointness.

The final-two-duty paragraph now says "separating edge with at least one
rich end", matching the displayed setup and full boundary-incidence scope.

## 7. Exact trust boundary and next lemma

The localized partition has demand at most two, whereas every live state
from deleting the compulsory edge `zu` has demand at least three.  Thus the
new theorem does not establish, or even permit, equality with the old
compulsory-edge state family.

Likewise, a colouring of the common double contraction `G/zu/f` need not
induce the localized partition.  The separate split lemma—every such
colouring locks `z` in all five alternative colours or locks both ends of
`f`—is a geometric saturation input, not a state-identification theorem.

The exact remaining constructive obligation is a rooted connector
composition theorem: enlarge the `A`-internal `B-C` connector, together
with a minimal connection to the unique portal vertex `z`, into two
literal adjacent carriers satisfying the correct frontier list/duty
criterion; or turn failure into a literal `K_7`, a valid fixed pair, a
normalized labelled near-model handoff, or a strict state-carrying
exact-seven descent.  In the Menger branch, the analogous obligation is to
decode the two edge-disjoint rich-side routes.  Neither conclusion follows
from the audited localization alone.
