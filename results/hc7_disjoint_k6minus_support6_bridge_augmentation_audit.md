# Independent audit: bridge augmentation in the exceptional six-path configuration

**Verdict:** GREEN for Theorems 2.1, 3.1, 4.1, 4.2 and their stated
corollaries.  The branch sets are pairwise disjoint, connected, and
pairwise adjacent; the shortest-path and separator arguments use exactly
six deleted vertices; and crossed attachments transpose the two exceptional
right endpoints as claimed.  The two web completions follow from the exact
crossing alternative of Humeau--Pous.  Section 5 is mathematically correct
assuming the standard fan-augmentation theorem of Perfect; the source now
gives its primary bibliographic citation.

**Audited source:**
`results/hc7_disjoint_k6minus_support6_bridge_augmentation.md`.

**Source SHA-256:**
`c1477c493972774cbd0575899d5227c91cd4c6b5f3cedef4770263cdc3c626e4`.

The audited mathematical text had source hash `ef321dbd...`; the current
hash differs only by changing the status line from audit-pending to audited
after promotion.

## 1. Clean augmenting path

The endpoint exclusions guarantee that the neighbours `u^-` toward `y`
and `v^+` toward `b_i` exist, including when a linkage path is a single
edge.  The four pieces in (2.1) have the intended incidences:

- `L_5` and `P_5[u,r]` are disjoint and joined by the omitted edge
  `u^-u`;
- `L_i` and `R_i` are disjoint and joined by `vv^+`; and
- `R-v` contains `u` and the neighbour of `v` on `R`, so its union with
  `P_5[u,r]` is connected and has an edge to `L_i`.

The seven sets in (2.2) are pairwise disjoint.  The interior of `R` avoids
every displayed path and both endpoint supports; deleting `v` from `R`
also removes its sole contact with `L_i`.  Every set is connected, with
`P_4 union L_5` joined by the literal edge `xy`.

The adjacency table is complete.  The only right-side nonedge is `pq`,
and no table entry uses it.  In particular, `P_4 union L_5` meets `P_3`
through `ya_3`, while its adjacency to `R_5` is `u^-u`; `R_5` meets
`L_i` through the last edge of `R` and `R_i` through `rb_i`.  For the two
untouched paths, the left contacts `a_jx,a_kx` exist because
`i,j,k` are exactly `0,1,2`, and all required right contacts to `r,b_i`
exist in `K_6^-`.  Thus (2.2) is an explicit `K_7`-minor model.

## 2. Six-vertex deletion and separator

The set `Z` in (3.1) has exactly six vertices.  Seven-connectivity makes
`H=G-Z` connected.  The sets `U` and `L` used in the proof are nonempty,
connected, and disjoint: `U=P_5-y`, while `L` consists of the other five
paths truncated at their right ends and is joined through the connected
graph `A-y`.

A shortest `U`--`L` path has no internal vertex in either endpoint set.
Every vertex of a displayed linkage path or of `A union B` outside
`U union L` lies in `Z`.  The resulting path therefore has precisely the
avoidance required in Theorem 2.1.  If it returns to one of
`P_0,P_1,P_2`, the clean augmentation gives a `K_7` model; otherwise its
second end is on one of the two exceptional paths.

For the separator conclusion, a shortest `U`--`T` path in `H-X`, trimmed
at its first and last contacts, has interior outside `U union T`, outside
`X`, and outside `Z`.  The identity

\[
 A\cup B\cup\bigcup_{h=0}^5V(P_h)
 \subseteq U\cup T\cup X\cup Z
\]

then makes it another clean augmenting path.  Hence `X` separates `U`
from `T` in a `K_7`-minor-free host.

If a minimum separator `W` has order one, the components of
`G-(Z union W)=H-W` define an actual order-seven separation after putting
all seven boundary vertices on both sides.  Both open sides are nonempty
because they contain `U` and `T`.  If `|W|>=2`, the vertex-set form of
Menger's theorem gives at least two pairwise vertex-disjoint `U`--`T`
paths.  No stronger conclusion about which component of `X` they meet or
their order follows, exactly as the source states.

## 3. Crossed bridge transposition

In Theorem 4.1 the opposite orders make the two paths in (4.2)
vertex-disjoint: the retained segments on each rail are disjoint, and the
two bridges have distinct ends and are pairwise vertex-disjoint.  They
exchange the right endpoints of `P_5` and `P_h`.

For `h=3`, the first set in (4.3) is connected by `a_0a_3` and reaches
the singleton sets through the final edges into `b_0` and `r`.  Its four
other contacts are `a_0a_1,a_0a_2,a_0x,a_3y`.  The middle right endpoints
are `b_1,b_2,q,p`; their sole possible missing adjacency `pq` is replaced
by the left edge `xy`.  Both `b_0` and `r` are adjacent to every middle
right endpoint and to each other.

For `h=4`, the corresponding first set in (4.4) is connected by `a_0x`.
Its four middle contacts are `a_0a_1,a_0a_2,a_0a_3,xy`; the middle right
endpoints are `b_1,b_2,p,q`, and the missing `pq` contact is replaced by
`a_3y`.  These checks establish all 21 adjacencies in each seven-bag
model without identifying or overlapping branch sets.

Corollary 4.2 is a valid application of Menger after deleting `D_h`.
Trimming between consecutive last/first rail contacts converts every
set-to-set path into exactly the restricted external path family, and the
converse is immediate.  If the packing number exceeds two, any pair in a
pairwise vertex-disjoint family has four distinct ends; Theorem 4.1
forbids opposite attachment order.  The resulting order-at-most-two set
is only a transversal of this restricted path family, not necessarily a
cut of `G`, as the note correctly emphasizes.

## 4. Web-completion certificates

For the ordered terminal tuple

\[
                         (y,r,t_h,s_h),
\]

a crossing in the sense of Humeau--Pous is exactly a pair of disjoint
paths from `y` to `t_h` and from `r` to `s_h`.  The definition of `H_h`
deletes every vertex of `A union B` and every other displayed linkage path
except these four endpoints and the two rails `P_5,P_h`.  Hence such a
crossing gives two transposed paths of the exact kind used in (4.3) or
(4.4), and the already checked branch sets produce a `K_7` minor.

If no `K_7` minor exists, the tuple is therefore crossless in each `H_h`.
Humeau--Pous define a web completion for any tuple of at least three
distinct vertices as a set of edges `F` for which `H_h+F` is a web with
that tuple as frame.  Their Generalised Two Paths Theorem (Theorem 1.3),
together with the equivalent web-completion formulation in Section 5,
says exactly that a tuple is crossless if and only if it has such a
completion.  It applies to arbitrary simple graphs; no unproved
connectivity or pre-existing-frame-cycle hypothesis is hidden here.

The theorem correctly treats `F_3,F_4` as completion edges only.  They need
not be host edges and the two completions need not agree on their common
vertices, so no branch-set adjacency or simultaneous embedding is inferred
from them.

## 5. Perfect augmentation paragraph

Deleting `Z'={b_0,b_1,b_2,y}` from a seven-connected graph leaves a
three-connected graph.  The Fan Lemma gives a three-fan from `r` to
`S={p,q} union T`.  Perfect's augmentation theorem in its standard form
says that a smaller fan with prescribed feet can be extended to the size
of an existing larger fan while preserving those feet.  Applying it to
the two literal arms `rp,rq` therefore gives a three-fan whose third foot
is in `T`.  Replacing the other two arms by the literal edges makes the
third arm avoid `p,q`.

The third arm begins at `r in U` and ends in `T`.  Trimming from its last
contact with `U` to its first later contact with `T` leaves no internal
vertex in `U union T`.  Its construction avoids `p,q`, while `Z'` was
deleted; hence, if it also avoids `X`, it avoids every vertex of `A`, `B`,
and the six linkage paths except its two allowed ends.  Theorem 2.1 then
applies.  This logic is sound.

The source cites Hazel Perfect, *Applications of Menger's graph theorem*,
Journal of Mathematical Analysis and Applications 22 (1968), 96--111.
For maximum reproducibility, a future promoted version should also state
the fan-augmentation lemma explicitly or add its theorem number.  This is
a citation-granularity recommendation, not a mathematical gap.

## 6. Exact remaining gap

The audited results force an exceptional return, an order-seven
separation when the induced minimum separator has order one, and a
`K_7` model from two crossed bridges on the same exceptional path.  They
do not prove that the two Menger paths meet different exceptional paths,
produce crossed attachment order, or compose several order-preserving
bridges.  Thus they identify but do not close the labelled two-crossing
problem.
