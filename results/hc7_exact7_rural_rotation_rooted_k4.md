# Rural pole rotation failure gives a rooted `K_4` or a literal collision

**Status:** proved and independently audited as a conditional composition
of the rural-page and tree-pole theorems.  This is a partial labelled
model, not yet a `K_7` model.

## 1. Exact setting

Let `K` be the three-connected planar carrier in the planar-rib outcome of
the block-terminal theorem.  It has no set-terminal cross between `Q` and
`P`.

### Lemma 1.1 (common carrier face)

The unique plane embedding of `K` has one facial cycle `C` containing the
roots `x,y`, the portal set `Q`, and the attachment set `P`, with `Q` on
one open `x-y` arc and `P` on the other.

#### Proof

Use the **one selected cell-free block-terminal web**, not separately
chosen pairwise web completions.  In its plane completion

\[
                         K^+=K+\alpha Q+\beta P
\]

is a literal subgraph and `(x,alpha,y,beta)` is the outer frame.  Delete
both bookkeeping vertices and every completion-only edge.  Deleting this
material only merges faces.  Since both bookkeeping vertices lie on the
outer frame, every face incident with either of them merges with the outer
face.  Every literal augmentation edge is incident with its bookkeeping
endpoint, so the resulting embedding of `K` has one face incident with
all of

\[
                         \{x,y\}\cup Q\cup P.
\]

The graph `K` is three-connected, so this facial boundary is a simple
cycle `C`.  The inherited nonedge `xy` is retained explicitly, although
the fixed-rib argument does not need to add it.

Finally fix `q in Q,p in P`.  If they lay on the same open `x-y` arc of
`C`, the `q-p` subpath of that arc and the other `x-y` arc would be
vertex-disjoint, a forbidden set-terminal cross.  Thus every `q` lies on
one open `x-y` arc and every `p` on the other. \(\square\)

Let `X` be one of the two connected poles in a spanning planar quotient,
and let `z` be its contracted vertex.  Every literal `X-K` edge is retained
as an attachment occurrence at `z`; parallel occurrences are not
suppressed for this purpose.  The simple carrier end of an occurrence
`omega` is denoted `u(omega) in V(C)`.  Occurrences with one carrier end
may be ordered arbitrarily within the thin band around their common simple
quotient edge; fix one such order.

Choose an edge-minimal connector tree in `X` spanning all literal
attachment bases.  Suppose its occurrence society fails the circular-split
criterion in the selected pole rotation.  The audited tree-pole theorem
then returns occurrences

\[
                         a,b,c,d                              \tag{1.1}
\]

in cyclic pole order and two vertex-disjoint literal paths in `X`, joining
the bases of `a,c` and of `b,d`, respectively.

## 2. Rooted model certificate

### Theorem 2.1 (rotation failure certificate)

In the setting above, one of the following occurs.

1. **Rooted `K_4` subdivision.**  The four carrier ends

   \[
                     u(a),u(b),u(c),u(d)                       \tag{2.1}
   \]

   are distinct, and `G[K union X]` contains a subdivision of `K_4`
   rooted at these four literal vertices.
2. **Repeated-end collision.**  Two of the four alternating attachment
   occurrences have the same literal carrier end.  The two corresponding
   pole edges and their distinct occurrence data are retained as a
   literal collision certificate.

#### Proof

If the four ends are not distinct, outcome 2 is exactly their repeated
incidence; no contraction or completion edge is asserted.

Assume they are distinct.  Around the contracted pole, their incident
edges occur in the cyclic order (1.1).  Since all simple neighbours of
this pole lie on the same facial cycle `C`, their order on `C` is (1.1) up
to reversal.  Reversal preserves alternation.

Let `D_ac` be the path in `X` between the attachment bases of `a,c`,
together with the two literal attachment edges to `u(a),u(c)`.  Define
`D_bd` analogously.  The two paths are vertex-disjoint because the
tree-pole theorem returns paths in different components of one deleted
tree edge; their four carrier ends are distinct, and `X` is disjoint from
`K`.  Hence `D_ac,D_bd` are internally disjoint from each other and from
`C`.

The union

\[
                         C\cup D_{ac}\cup D_{bd}                 \tag{2.2}
\]

is a cycle with two internally disjoint chords joining alternating pairs
of four distinct vertices.  It is therefore a subdivision of `K_4` with
branch vertices (2.1).  Every edge in (2.2) is a literal host edge; the
web completion is used only to certify the plane order of `C`. \(\square\)

## 3. Exact scope

The theorem applies separately to the `A union B` pole (whose simple ends
lie in `Q`, together with any root incidences) and to the locked pole `L`
(ends in `P`, together with any root incidences).  In the distinct-end
branch, a failed rotation is no longer just two paths: it supplies a
rooted `K_4` duty object on the named carrier cycle.  In the collision
branch the output is deliberately weaker; parallel occurrences at one
carrier vertex cannot be promoted to four distinct rooted branch vertices.

The remaining HC7 conversion is now exact:

> combine the rooted `K_4` duty object with the two untouched frame traces
> and the opposite pole, or use the repeated-end collision to perform a
> label-faithful pole split.  The conclusion must be a literal `K_7`, an
> admissible-rank promotion, or a boundary state reproducible on the other
> shore.

No claim is made that every such rooted `K_4` already forces `K_7`.
