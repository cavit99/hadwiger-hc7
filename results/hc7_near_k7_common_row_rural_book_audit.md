# Independent audit: common-row rural book

## Verdict

**GREEN after the two local repairs recorded below.**

* Theorem 1, Lemma 2, and Corollaries 1.1 and 2.1 are **GREEN**.
* The no-private-linkage implication in Theorem 3 yields one common face
  and the corrected labelled order `alpha,P_c,P_b,beta`; the two outcomes
  are now mutually exclusive.
* The first assertion of Theorem 4 is **GREEN**, after choosing each whole
  live component (or augmenting to its `K`-attachment).  Its corrected
  four-way list is mutually exclusive and exhaustive.

The original failures were statement-level and are repaired in the
theorem file.  The useful implication

\[
 \text{no private linkage in a 4-connected connector}
 \Longrightarrow
 \text{one crossed labelled rural page}
\]

survives the audit.

## 1. The literal completion is correct

Theorem 1 is the already-audited common-row promotion construction in a
different order.  Its seven bags are

\[
 X\cup L,\quad W\cup R,\quad F_a\cup K,
 \quad F_i\ (i\ne a).
\]

There are three promoted bags and four unchanged rows.  They are pairwise
disjoint because `X,W,Z,F_1,...,F_5` are pairwise disjoint and
`K,L,R subseteq Z` are pairwise disjoint.  They are connected through the
literal `XL`, `WR`, and `F_aK` edges.

The complete adjacency check is:

* the first two bags meet through the literal `XW` edge;
* they meet the middle bag through `LK` and `RK`;
* `X union L` meets `F_b` through `L` and every other unchanged row
  through `X`;
* `W union R` meets `F_c` through `R` and every other unchanged row
  through `W`;
* `F_a union K` meets every unchanged row through `F_a`; and
* the unchanged rows retain their fixed clique-model edges.

The exact overlap assumption is used correctly:

\[
 D=\{a,b\},\quad E=\{a,c\},\quad a,b,c\text{ distinct},
 \quad D\cap E=\{a\}.
\]

Thus Theorem 1 is **GREEN**.

For Corollary 1.1, `P_a={p}` supplies the literal `p-F_a` contact,
`L,R subseteq Z-p` give disjointness from `K={p}`, and the two `p`
neighbour conditions give `LK,KR`.  Every hypothesis of Theorem 1 is
present.  It is **GREEN**.

## 2. Private-linkage augmentation, including overlapping portals

Lemma 2 remains valid when `P_a` overlaps another portal set.

Choose any `p in P_a`.

* If `p in L`, then `L` already meets `P_a,P_b` and outcome 1 holds.
* If `p in R`, outcome 2 holds.
* Otherwise take a shortest `p-(L union R)` path.  By first-entry
  minimality its internal vertices avoid both carriers, and its terminal
  vertex belongs to exactly one because `L,R` are disjoint.  Add the path
  up to, but not including, that terminal vertex to the carrier it reaches.
  The enlarged carrier is connected, still disjoint from the other, and
  meets `P_a`.

This proof does not require `P_a,P_b,P_c` to be disjoint.  If the selected
`p` lies in an overlap, it is handled by the first two cases or by the same
shortest-path argument.

To invoke the robust exclusion theorem, choose

\[
 \alpha in L\cap N_Z(X),\qquad
 \beta in R\cap N_Z(W).
\]

The two vertices are distinct because the carriers are disjoint, and
they are literal attachment roots.  Outcome 1 covers the two occurrences
`a,b` on the old side and occurrence `c` on the new; outcome 2 covers
occurrence `b` on the old and `a,c` on the new.  Either covers three of
the four occurrences in `D dotcup E`, so the audited robust theorem gives
a `K_7^-` model.  Lemma 2 and Corollary 2.1 are **GREEN**.

## 3. The correct rural order and the exclusivity defect

The quoted four-connected Two Paths alternative has the needed scope:
for four distinct terminals, failure of the prescribed two-linkage gives
a planar embedding in which they alternate on one facial cycle.
Four-connectivity implies three-connectivity, so the spherical rotation
system is unique up to reflection and every facial boundary is a cycle.

Assume outcome 1 fails.  Fix `x_0 in P_b,y_0 in P_c` and let `F` be their
alternating face.  For any `y in P_c`, its alternating face with
`alpha,beta,x_0` shares three distinct vertices with `F`.  In a
three-connected plane graph two distinct faces share at most an edge;
hence it is the same face.  Varying `x` with `y_0` fixed similarly puts
all of `P_b` on `F`.  This common-face argument is **GREEN**.

For the prescribed pairs `(alpha,x)` and `(beta,y)`, alternation places
`x,y` on the same open `alpha-beta` arc.  Fixing `x_0,y_0` forces every
portal onto that same arc.  More is true than the source states.  Orient
the occupied arc from `alpha` to `beta`.  The alternating order is

\[
                  \alpha,quad P_c,quad P_b,quad \beta, \tag{3.1}
\]

where every `P_c` occurrence precedes every `P_b` occurrence.  If some
`P_b` preceded some `P_c`, that pair would have nonalternating order and
the two boundary subarcs would give the forbidden linkage.

The source records only "two noninterleaving blocks ... or conversely".
That property does not imply alternation and does not exclude outcome 1.
Here is a literal counterexample using its own square-antiprism test graph.
In graph6 `GQyurg`, take

\[
 \alpha=0,\quad\beta=5,\quad P_b=\{6\},\quad P_c=\{3\}.
\]

The facial quadrilateral is `(6,0,5,3)`.  Both portals lie on the open
`0-5` arc `0,6,3,5` and form two noninterleaving singleton blocks, so
outcome 2 as written holds.  But the literal edges `0-6` and `5-3` are
disjoint paths, so outcome 1 also holds.  The graph is four-connected and
all four terminals are distinct.  Therefore "exactly one" is **RED**.

### Exact repair to Theorem 3

Replace the block sentence in outcome 2 by

> Orient the occupied open facial arc from `alpha` to `beta`.  Every
> occurrence of `P_c` precedes every occurrence of `P_b`; equivalently,
> every quadruple `alpha,x,beta,y`, with `x in P_b,y in P_c`, has the
> alternating cyclic order for the prescribed pairs.

One may reverse the entire facial orientation, but one may not say "or
conversely" while keeping the four labels and the direction
`alpha -> beta` fixed.  With (3.1), outcomes 1 and 2 are mutually
exclusive and exhaustive, and Theorem 3 becomes **GREEN**.

The phrase "unique plane embedding" should also be read as "unique
spherical/combinatorial embedding up to reflection"; choosing a different
outer face does not change the common facial cycle but literally gives a
different drawing in the plane.

## 4. The nine-vertex double-book check

For graph6 `HCZTfP}` with roots `alpha=0,beta=7`, the two facial pages

\[
 (5,0,7,1),\qquad(7,0,6,2)
\]

block the matched singleton pairs `(1,5)` and `(2,6)`.  With
`P_b={1},P_c={5}`, Theorem 3 returns the first crossed page; with
`P_b={2},P_c={6}`, it returns the second.

If instead `P_b={1,2}` and `P_c={5,6}`, outcome 1 correctly occurs:
there are disjoint `0-1` and `7-6` carriers, and also disjoint `0-2` and
`7-5` carriers (the exact vertex sets are machine-verified by the robust
barrier search).  No single face contains all four portals.  Thus the
double-book does not falsify the corrected set-terminal statement; it
illustrates why the theorem quantifies over *every* private pair before
returning one page.

## 5. Component exchange

Let `C` be a component of `Z-K`.  Since `Z` is connected and `K` is
nonempty, `C` has an edge to `K`: a path from `C` to `K` leaves the
component directly into `K`.

If distinct components `C_L,C_R` are respectively left-live and
right-live, use the whole components as `L,R`.  They are disjoint,
connected, meet the required endpoint/root and private-row portal sets,
and each has an edge to `K`.  Together with the assumed `K-F_a` edge,
they satisfy Theorem 1.  This proves the first assertion of Theorem 4.

The source proof says merely to take a connected subgraph inside each
component meeting its two portal sets.  Such a smaller subgraph need not
contain a `K`-attachment.  This is a proof-writing gap, not a false
statement: take the entire component, or adjoin a path from the smaller
subgraph to a vertex with a `K` neighbour.

If a `K_7` is excluded and both live families are nonempty, every
left-live component must equal every right-live component.  Fixing one of
each proves there is exactly one member of each family and they coincide.
That substantive concentration statement is **GREEN**.

However, the displayed alternatives are not "exactly one" as written.
If there is neither a left-live nor a right-live component, both bullets
1 and 2 hold.  The most immediate example is permitted by the statement:
take `K=Z`, so `Z-K` has no components at all.

### Exact repair to Theorem 4

Either replace "exactly one" by "at least one", followed by the already
proved assertion that if both live families are nonempty then bullet 3
holds, or use the mutually exclusive list

1. there is no left-live component;
2. there is a left-live component but no right-live component; or
3. both kinds exist, and one unique component is the sole member of both
   families.

With that wording and the whole-component choice above, Theorem 4 is
**GREEN**.

## Trust boundary

After the two local repairs, this note proves three exact implications:

* three disjoint promoted carriers give `K_7`;
* a private linkage gives `K_7^-`; and
* failure of all private linkages in a four-connected connector gives one
  crossed, label-oriented rural page.

It does not compose different pages into a global two-apex embedding,
force a page through a cutvertex or 2-adhesion, or match a proper-minor
equality state.  Those remain the proof-spine gap.
