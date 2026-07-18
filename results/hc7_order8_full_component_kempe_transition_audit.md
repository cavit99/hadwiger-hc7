# Internal audit of the order-eight full-component Kempe transition

**Verdict:** GREEN for the complete written theorem, with the limitations
stated in Sections 5 and 6 of the source.

**Audited source:**
`hc7_order8_full_component_kempe_transition.md`, SHA-256

```text
2ee9a566e57e27983d8c17c54621768fd228c02a1f0f533db7c727010fc60575
```

This is a separate internal mathematical audit, not external peer review.
The boundary-degeneracy and transition-tree argument and the specialised
edge-deletion fan were checked independently by different agents.

## 1. Setup and gluing convention

The source uses labelled boundary colourings in Sections 1--4.  This is the
right level of precision: component-side extensions with the same labelled
boundary colouring glue directly because distinct components of `G-X` are
anticomplete.  If only the equality partition is specified, a palette
permutation on each component-side first makes the labelled restrictions
agree.  Consequently (1.4) is exact.

Every component deletion or contraction used in the proof is a proper minor
operation.  In particular, each `C_i` is nonempty, and `C_i union I` contains
an edge whenever `I` is nonempty because `C_i` is `X`-full.

## 2. The two degeneracy bounds

Both density calculations are correct.

If `F subseteq H` has minimum degree at least six, then its order `h` is
seven or eight.  Contracting two distinct full components gives the minor
`̅K_2 vee F`, with at least `5h` edges on `h+2` vertices.  Mader's exact
`K_7`-minor bound is `5(h+2)-15=5h-5`, a contradiction.

If `I` is nonempty and `F subseteq H-I` has minimum degree at least five,
then `h` is six or seven.  The same minor has at least 27 or 32 edges,
whereas Mader permits at most 25 or 30.  Thus `H` is five-degenerate and
`H-I` is four-degenerate.

The graphs to which Mader is applied have at least eight vertices and are
`K_7`-minor-free because they are minors of `G`.

The Las Vergnas--Meyniel theorem therefore applies with six colours to `H`
and with five colours to `H-I`.  It includes labelled colourings with unused
palette colours.  In the exact-block cylinder every move avoids the fixed
sixth colour, so it preserves `I` exactly.

## 3. Exact traces and pullback

The trace orientation is correct.  To colour the intact `C_i`-side, the
proof contracts a different full component together with `I`, and pulls
back only over the literal independent set `I`; it never expands the
contracted component.  Fullness makes the contraction image adjacent to
every vertex of `X-I`, which proves exactness.

The exact-pair assertion is correctly restricted to `m=3`.  The two other
components fund the two disjoint independent blocks while the selected
component remains untouched.  Their representatives are adjacent and have
distinct colours.  When `|I union J|>=4`, at most four boundary vertices
remain, so the four-colour exact-pair cylinder is connected by the same
degeneracy theorem.

## 4. Signature-change paths

Lemma 3.1 is a standard but correctly literal Kempe-lifting argument.  If a
boundary interchange could be performed on every full two-colour component
meeting the operated boundary component without reaching another boundary
component, it would extend the new boundary colouring through the same
shore.  Failure therefore gives a shortest two-colour path between distinct
boundary components.  Shortestness puts every internal vertex in the named
literal component `C_i`.

For `m=2`, minimal distance between the two disjoint extension sets makes
the first and last transition edges genuine membership changes.  The two
paths need not use the same colour pair unless the distance is one; the
source states this restriction.

For `m=3`, contracting `C_i union I` gives a colouring whose signature is
exactly `[3]-{i}`.  It cannot also extend through `C_i`, since the three
extensions would glue.  A finite connected union of Kempe paths contains
the three anchors; taking a spanning tree is legitimate.  Along a tree path
from the anchor omitting `i` to one containing `i`, that signature bit must
change.  The three resulting paths may come from different transitions and
are not asserted simultaneous.

The version without a fixed block is also correct: deleting `C_i` is a
proper minor, and Theorem 2.1 connects all labelled six-colourings of the
boundary.

## 5. Three-component lock and edge-deletion fan

The 82-type hypothesis is used exactly where needed.  Since these boundary
graphs are three-colourable and have no clique odd-cycle transversal, no
colour class of a three-colouring is a singleton; hence one class has order
two.  The two fixed contractions in (5.2) force the other two colour classes
exactly.  Their only possible returned equality partitions are therefore
`Theta` and `Omega`.

The glue-or-lock quantifier is correct for one fixed orientation of (5.2).
If each intact component-side has one `Theta` response, the three responses
glue.  Otherwise one fixed minor has no `Theta` response, and every colouring
of that fixed minor returns `Omega`.  The theorem does not claim the same
for the swapped assignment of the two other components.

In a locked colouring, a Kempe swap would merge `r,z` unless their two-colour
component contains an `r`--`z` path.  The two contraction representatives
and `A union B` use the other two boundary colours, so the path interior is
in the intact component.  The nonedge `rz` makes its first edge `rv` a
literal boundary-to-component edge.

For any colouring of `G-rv`, the endpoints have one common colour `alpha`;
otherwise restoring the edge colours `G`.  Its boundary partition cannot
extend through the intact component.  It is not `Omega`, because `Omega`
already extends there and the deletion colouring extends through the other
two components.  Packet demand is at least three by the no-clique-odd-cycle-
transversal identity proved in the cited classification.

For every other colour `beta`, the `alpha`--`beta` component containing `v`
must also contain `r`; otherwise swapping it permits restoration of `rv`.
Stopping a `v`--`r` path at its first boundary hit gives item c.  Paths for
different colours can share only `alpha`-coloured vertices and cannot share
an edge.  A repeated boundary endpoint is likewise `alpha`-coloured.

## 6. Explicit non-conclusions

The audit rejects the following stronger inferences, none of which appears
in the source:

- the five paths are vertex-disjoint (they all contain `v`);
- their first boundary endpoints are distinct or different from `r`;
- the paths simultaneously add five boundary edges;
- the three transition-tree paths use one common boundary colouring; or
- palette colours identify the inherited clique-minor branch sets.

Thus the promoted result is a dynamic host-level compression, not a closure
of the two- or three-component order-eight interfaces.  Its remaining gate
is exactly the label-preserving first-hit allocation or compatible-separator
step stated by the source.
