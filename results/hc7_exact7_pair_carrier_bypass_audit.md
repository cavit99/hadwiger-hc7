# Independent audit: pair-carrier outside bypass

Audited file: `results/hc7_exact7_pair_carrier_bypass.md`.

## Verdict

The required local hypotheses are now explicit in Section 1.  Accordingly,
Theorem 2.1 is **GREEN**, including its universal vital-rail conclusion.
Theorem 4.1 is also **GREEN in its current endpoint-omitting form**.
Theorem 5.1 is also **GREEN in its current nonroot-qualified wording**.
The required local hypotheses are

\[
 L\subseteq D_t,\qquad L\ne\varnothing,\qquad G[L]\text{ connected},
 \qquad E(w,L)\ne\varnothing,
\]

where `D_t` is the present open shore.  The last condition makes
`W={w}\cup L` connected.  Merely saying that `L` is connected and
disjoint from the core and side terminal does not place it in the open
shore, does not prevent it from containing other adhesion vertices, and
does not make `W` connected.  Without these conditions, the claimed
whole-graph neighbourhood containment and raw-carrier promotion would not
follow.

## 1. Exact-cell containment after the repair

The traces of `K,A,B` partition `U`, with `K\cap T={x,y}`.  Therefore

\[
                         A\cup B\cup\{x,y,w,t\}
\]

contains every boundary neighbour of the present open shore.  Because `L`
lies in that shore, the component `X_0` containing it after deleting this
set remains wholly inside the present open shore.  It cannot reach the
opposite shore, either terminal, or `v`.

At most two of the at least five vertices of `P=N(L)\cap K` are `x,y`.
Each other member survives the deletion and is adjacent to `L`, so `X_0`
contains at least three vertices of `K-{x,y}`.  If it has no neighbour in
`A\cup B`, then, simply because it is a component of the deleted graph,

\[
                         N_G(X_0)\subseteq\{x,y,w,t\}.
\]

The set on the right has order four, while nonempty `X_0` and `v` lie on
opposite sides.  This contradicts seven-connectivity.  Thus the required
outside `A_0-L` path exists.

## 2. The path avoiding `K`

Choose the path with internal vertices in `X_0` and first entry into `L`
at its final vertex.  If it avoids `K`, adjoin every path vertex except the
final `L` vertex to `A_0`.  The internal vertices lie in the open shore and
outside all three core blocks.  Hence the enlarged block is connected,
remains disjoint from the other two blocks and `L`, and has exactly its old
adhesion trace.  Its old adjacency to the third block survives, and its
last path edge gives adjacency to `L`.

The set `L` already sees `K` through nonempty `P`; the repaired hypothesis
`E(w,L)\ne\varnothing` makes `W` connected.  Therefore this is a genuine direct
raw-contact-rank promotion, not merely an edge to a disconnected set.

## 3. First hit of `K`

If the path meets `K`, its first such vertex `q` is not `x` or `y`, because
both roots were deleted before `X_0` was chosen.  The prefix before `q` is
disjoint from `K`, the other core block, and `L`.  Absorbing it into `A_0`
preserves the target block's connectedness and exact trace and creates a
literal `q-A_0` edge.  The carrier `K`, the attachment set `P`, and all
trace edges to the third block remain unchanged.

Consequently the generalized clause following the audited pair-trace peel
theorem applies to every nonseparating `x-y` path in `K-q` which omits at
least one member of `P`.

## 4. Universal rail quantifier

Tutte's theorem guarantees at least one `x-y` path in `K-q` whose vertex
deletion leaves `K` connected.  If any such path omits a member of `P`, the
audited generalized peel gives outcome 2.  Hence failure of outcomes 1 and
2 implies

\[
 \text{every nonseparating `x-y` path in `K-q` contains all of `P`.}
\]

This is the correct universal quantifier: the portal `q` is fixed by the
first outside-path hit, while the quantifier ranges over all
nonseparating trace paths avoiding that fixed `q`.

Moreover `q\notin P`.  Otherwise every path in `K-q` omits the member `q`
of `P` and immediately invokes the peel alternative.  Thus
`q\in K-(\{x,y\}\cup P)`, exactly as outcome 3 states.

## 5. Theorem 4.1: three-bypass amplification

**GREEN.**  The current proof explicitly absorbs each target-side prefix
with its endpoint `q_i` omitted.  Thus every `q_i` remains in `K`, exactly
as required by the statement's subsequent rail conclusion.  This repairs
the only defect found in the first audit pass.

### Menger fan and separator vertices in the target

After contracting connected `L` to a source `s`, the vertex-fan form of
Menger gives either three paths from `s` to distinct vertices of
`A\cup B`, disjoint outside `s`, or a set `Z` of order at most two,
disjoint from `s`, meeting every source-to-target path.  Endpoints in
`A\cup B` are allowed to lie in `Z`; equivalently, in the graph minus
`Z`, the source component contains no target vertex outside `Z`.

On expanding `L`, let `C` be its component in `G-(F\cup Z)`, where
`F={x,y,w,t}`.  The separator conclusion means that `C` contains no target
vertex and has no edge to a target vertex outside `Z`.  Since the remaining
root traces are contained in the target blocks `A,B`, exact-cell
containment prevents `C` from escaping the present open shore.  Therefore

\[
                         N_G(C)\subseteq F\cup Z,
                         \qquad |F\cup Z|\le6.
\]

The source set is nonempty, and the far side is nonempty even if `v` happens
to belong to `Z`: the traces of `A,B` contain the three vertices of
`U-{x,y}`, whereas `|Z|<=2`, so at least one target vertex survives outside
`F\cup Z`.  This is a genuine cut contradicting seven-connectivity.
Thus the claimed three-fan exists even when a minimum `Z` uses one or two
target vertices.

### Expansion, trimming, and simultaneous absorption

Expanding the contracted source may make the three paths share vertices of
`L`, but they remain disjoint outside `L`, exactly as stated.  Trimming from
the source side at the first target occurrence and at the first `L`
occurrence gives distinct target endpoints and removes all other
`A\cup B` and `L` vertices from their interiors.

Moreover, each pre-target segment stays in the present closed terminal
shore.  Its only possible exits are through `x,y,w,t`, which are deleted,
or through a remaining root of `U-{x,y}`, and every such root already lies
in the target `A\cup B`.  Hence a trimmed prefix cannot silently run
through `v` or the opposite shore before its first target hit.

If one trimmed path avoids `K`, its non-`L` prefix can be absorbed into its
target block exactly as in Theorem 2.1, giving direct promotion.  Otherwise
the first `K` hits `q_1,q_2,q_3` are distinct because `K` is disjoint from
`L` and the paths are disjoint outside `L`.  They avoid `F`, hence are
non-root vertices.

Under the current endpoint-omitting wording, each absorbed prefix is disjoint
from `K`, from `L`, and from the other target block; different prefixes are
mutually disjoint.  Several prefixes ending in the same target block cause
no problem: their union with that already connected block is connected.
The two target blocks stay disjoint, retain their exact traces, and retain
their old mutual adjacency.  Each `q_i` stays in the unchanged carrier `K`
and gains a literal edge to its enlarged target block.  Hence `K` and
`P=N(L)\cap K` really are common and unchanged for all three indices.

### Applying the generalized peel for all three portals

Fix `i`.  Tutte supplies a nonseparating `x-y` path in `K-q_i`.  If any
such path omits a member of the unchanged `P`, the already audited
generalized pair peel applies to the simultaneously enlarged core and
gives outcome 2.  If no peel occurs, every such path contains all of `P`,
which forces `q_i\notin P` because every path avoids `q_i`.

This reasoning may be repeated for each `i` without performing a peel or
altering `K`: under the standing assumption that outcome 2 never occurs,
it merely records the universal path property.  It therefore yields three
distinct vertices of `K-(\{x,y\}\cup P)` referring to the same carrier and
the same marked set, as claimed.

## 6. Theorem 5.1: two-rail segregation

The formal theorem is **GREEN**.

### Exact Tutte input

Tutte's second nonseparating-path theorem states that, for any distinct
`x,y` in a three-connected graph, there are two independent `x-y` paths
`R_1,R_2` such that `K-V(R_i)` is connected for each `i`.  In the standard
terminology, independent paths have no internal vertex of one on the other.
For paths with the same two endpoints this is exactly internal
vertex-disjointness.  Thus the cited theorem supplies precisely the two
rails and the two individual connected-complement assertions used here.

It does **not** assert that `K-V(R_1\cup R_2)` is connected, and Theorem
5.1 should not be read that way.  “Both rail complements are connected”
means separately

\[
                         K-V(R_P)\text{ is connected},
                         \qquad K-V(R_Q)\text{ is connected}.
\]

### Pigeonhole argument

Every `q_i` is different from `x,y`, so internal disjointness puts it on at
most one rail.  If some `q_i` were on neither rail, both rails would avoid
it.  The universal property from Theorem 4.1 would then put all of `P` on
both rails.  This is impossible even when `x,y in P`: since `|P|>=5`, the
set `P-{x,y}` has at least three vertices, all of which would be common
internal vertices.

If `q_i` lies on one rail and `q_j` on the other, the first rail avoids
`q_j` and the second avoids `q_i`; again both would contain all of `P`, the
same contradiction.  Since no `q_i` is off both rails and no two occupy
different rails, all three lie internally on one rail `R_Q`.  The other
rail `R_P` avoids every `q_i`, so the universal property puts all of `P` on
`R_P`.

Internal disjointness now gives

\[
 (P-\{x,y\})\cap V(R_Q)=\varnothing,
\]

while the nonroot `q_i` all lie in `V(R_Q)-{x,y}`.  These are exactly
(5.1)--(5.2).

### Applied prose qualification

The current source says “all nonroot marked attachments occur on one
rail.”  This is the exact qualification needed if `x` or `y` belongs to
`P`, because both rails contain their common endpoints.  The proved
statement is:

> all **nonroot** marked attachments occur only on `R_P`, while all three
> movable foreign portals occur only on `R_Q`.

This applied wording repair does not alter the displayed theorem or its
proof.

## Trust boundary

The repaired theorem requires the carrier `K` itself to be
three-connected, a single connected and `w`-attached region `L` in the
present exact-cell open shore, and the literal exact trace partition by
`K,A,B`.  It does not handle disconnected attachment regions, a region
without a `w` edge, or pair carriers with a 1/2-cut.  The phrase “vital
rail” remains local and does not assert a standard vital linkage.  The
current Theorem 4.1 already includes the necessary endpoint omission.
Theorem 5.1 gives two individually nonseparating rails; it gives no
connectivity assertion after deleting their union, and it segregates only
the nonroot part of `P`.
