# Independent adversarial audit: fixed-root holonomy

## Verdict after the recorded repairs

**GREEN in the stated fixed-connector, fixed-root, disjoint-portal scope.**

This audit also cross-checks the common-row rural-book input used by the
holonomy theorem.  That input has its own audit beside its result file.

The branch-set and augmentation core is sound.  In particular, the common-row
three-carrier construction really gives a literal `K_7`, and the use of the
robust four-demand theorem is valid after choosing the attachment roots inside
the two carriers.

The two statement-level defects initially found in the ordering layer have
now been repaired in the theorem files.

1. The alternatives in common-row Theorem 3 are **not exclusive as written**,
   because the rural alternative forgets which private block comes first on
   the oriented facial arc.  The proof establishes the stronger, correctly
   oriented statement.
2. Fixed-root Theorem 1 needs a nonvacuous loopless constraint graph.  As
   written it includes the one-label, no-arc case, in which its planarity
   conclusion is false.  Its basis-exchange lemma also needs to say explicitly
   that every contextual comparison is a total antisymmetric tournament
   comparison.

With those exact repairs applied, all intended implications below are
**GREEN**.  Neither note transports the roots or the facial order between
different connectors.

## A. `hc7_near_k7_common_row_rural_book.md`

### Theorem 1 (common-row third-bag completion): **GREEN**

The seven proposed branch sets are

\[
 X\cup L,\quad W\cup R,\quad F_a\cup K,\quad F_i\ (i\ne a).
\]

They are disjoint because `X,W,Z,F_1,...,F_5` are disjoint and `K,L,R`
are disjoint subsets of `Z`.  Their connectivity uses exactly the three
rooting edges in (1.1).  Every adjacency is literal:

* `(X union L)(W union R)` uses the old `XW` edge;
* the first two bags meet `F_a union K` through `LK` and `RK`;
* `X union L` meets `F_b` through `L` and all other unchanged rows through
  `X`;
* `W union R` meets `F_c` through `R` and all other unchanged rows through
  `W`;
* `F_a union K` meets every unchanged row through the old fixed-row clique
  model.

No centre--`F_a` spoke is being silently assumed.  This is a literal
`K_7` model, not merely a `K_7^-` or quotient model.

### Corollary 1.1: **GREEN**

Taking `K={p}` is legitimate.  The hypotheses in (1.3) give both required
edges from `K`, and `L,R subseteq Z-p` give disjointness.

### Lemma 2 (private-linkage augmentation): **GREEN**

The shortest `p`--`(L union R)` path may be stopped immediately before its
first carrier vertex.  Its added vertices avoid both old carriers; adding
them to the first carrier met preserves connectedness and disjointness and
adds a `P_a` occurrence.

The local note defines “`X`-rooted” as meeting `N_Z(X)`, whereas rotation-edge
Theorem 5 fixes a particular root `alpha`.  This does not invalidate the
application: after `L,R` have been found, choose

\[
 \alpha\in L\cap N_Z(X),\qquad
 \beta\in R\cap N_Z(W),
\]

and instantiate rotation-edge Theorem 5 with those roots.  The proof should
say this explicitly to avoid a false impression that one previously fixed
root is automatically present.

### Corollary 2.1: **GREEN** (conditional on the audited rotation datum)

For `D={a,b}` and `E={a,c}`, outcome 1 of Lemma 2 takes
`D_0=D,E_0={c}`; outcome 2 takes `D_0={b},E_0=E`.  In either case exactly
one **occurrence** in the multiset `D dotcup E` remains uncovered.  Hence
rotation-edge Theorem 5 gives `K_7^-`.  The fact that `a` occurs in both
sets causes no collision: the theorem counts the two centre--row spokes,
not distinct row labels.

### Theorem 3 (private linkage or coherent rural page): **YELLOW**

The implication proved in the text is correct:

> if no pair `x in P_b,y in P_c` admits disjoint `alpha-x` and `beta-y`
> paths, then the unique planar embedding has one common face, all portals
> lie on one open `alpha-beta` arc, and, on that arc directed from `beta`
> to `alpha`, **every `P_b` occurrence precedes every `P_c` occurrence**.

The Two Paths hypotheses are used correctly: `G[Z]` is 4-connected and the
four terminals are distinct because the two portal sets are disjoint from
each other and from `{alpha,beta}`.  One failed instance forces planarity;
Whitney uniqueness applies because 4-connectivity implies 3-connectivity.
The three-common-vertices face propagation is also valid in a 3-connected
plane graph.

However, alternatives 1 and 2 are not exclusive as presently stated.
Alternative 2 merely asks for two noninterleaving blocks “up to reversing
the arc and interchanging the two classes”; it does not retain the prescribed
order forced by the terminal pairing.

An explicit counterexample to “exactly one” is the square-antiprism graph.
It is planar and 4-connected.  On one square face in cyclic order
`alpha,beta,y,x`, take `P_b={x}` and `P_c={y}`.  Alternative 2 as written
holds: both singleton blocks lie on the open `beta`--`alpha` arc.  But
alternative 1 also holds, using the two disjoint boundary edges
`alpha-x` and `beta-y`.

**Exact repair.**  Replace outcome 2 by the oriented assertion

> on the portal-containing boundary arc directed from `beta` to `alpha`,
> every occurrence of `P_b` precedes every occurrence of `P_c`.

Then say either outcome 1 holds, or, if it fails, this oriented outcome 2
holds.  With the oriented order the alternatives are exclusive: the two
terminal pairs alternate on the face, so planar Jordan separation forbids
the private linkage.  The proof already establishes precisely this repaired
form; its final phrase “or conversely” should be replaced by the fixed
orientation.

### Theorem 4 (two-shore component exchange): **GREEN**

Every component of `Z-K` is adjacent to `K` because `Z` is connected.  A
left-live component contains a connected `X`-rooted `P_b`-carrier, and a
distinct right-live component contains a disjoint connected `W`-rooted
`P_c`-carrier.  These, together with `K`, satisfy every hypothesis of
Theorem 1.  The uniqueness conclusion follows by comparing an arbitrary
member of each live-component family.  No hidden 4-connectivity assumption
is used here.

## B. `hc7_near_k7_fixed_root_rural_holonomy.md`

### Theorem 1 (fixed-root ordered-page coherence): **YELLOW**

For a loopless directed `Q` with at least two labels, nonempty pairwise
disjoint portal sets, and connected underlying graph, the proof is sound.
For every arc `i -> j`, failure of the set linkage implies failure for each
four-terminal choice.  The 4-connected Two Paths Theorem gives the same
unique plane embedding.  The face-propagation argument along a spanning
tree of the underlying graph is valid, and connectedness propagates the
choice of one open `alpha-beta` arc.  On that arc directed from `beta` to
`alpha`, alternation gives the strict order

\[
                 P_i\text{ entirely before }P_j.
\]

The literal statement is false in a vacuous edge case: let `I` have one
label, let `Q` have no arcs, and let `H=K_5`.  The underlying graph of `Q`
is connected under the standard one-vertex convention and all constraints
are vacuous, but `H` is not planar.

Loops are another unhandled case: for `i -> i` the proof cannot choose four
distinct terminals from arbitrary `P_i`.

**Exact repair.**  Require `|I|>=2` and `Q` loopless (equivalently here,
require a nonempty loopless arc set and weak connectivity).  The phrase
“after reversing the global orientation if necessary” is unnecessary once
the portal arc is explicitly directed from `beta` to `alpha`; in that
orientation an arc `i -> j` always means `P_i` before `P_j`.

### Corollary 2: **GREEN after the preceding repair**

Its contrapositive use is exact.  For an overlapping rotation, the common
portal set is nonempty by the rotation datum.  The two paths are disjoint
rooted carriers, Lemma 2 adds the common-row occurrence, and rotation-edge
Theorem 5 leaves at most one deficient spoke.  This gives `K_7^-`.

The result remains conditional on all portal sets participating in the
directed cycle satisfying the fixed-root theorem's disjointness hypotheses.
Actual portal sets `N_Z(F_i)` need not be disjoint in general, so this is a
real scope condition, not automatic rotation data.

### Lemma 3 (local flatness of signed basis exchanges): **YELLOW**

The proof is correct under the intended tournament interpretation, but that
interpretation is not stated precisely.  “Comparisons are assigned for every
ordered overlap transition” can literally be read as assigning both
`b <_a c` and, on the reverse transition, `c <_a b`; the later proof instead
uses exactly one direction for every contextual unordered pair.

**Exact repair.**  State that for each context `a` and each unordered pair
`{b,c}` disjoint from `a`, exactly one of `b <_a c` and `c <_a b` holds.
Thus every `<_a` is a tournament, and reversing traversal of a basis edge
reads the same sign in the opposite direction rather than adding a second
comparison.  Under this assumption:

* (2.2) makes `b<c` independent of context;
* the resulting relation is a tournament;
* absence of a star triangle makes that tournament acyclic and hence a
  linear order.

No additional long-cycle condition is needed.

### Corollary 4: **YELLOW**, becoming **GREEN** after both repairs

Once the comparisons are total contextual tournament signs and all of them
are realized using the same literal 4-connected connector, the same literal
root pair, and the theorem's pairwise-disjoint portal sets, Theorem 1 puts
them in one linear facial order.  A star triangle is a directed 3-cycle; a
context conflict supplies opposite constraints `b -> c` and `c -> b`, hence
a directed 2-cycle.  Corollary 2 then forces a private linkage on one edge.

The conclusion must not be applied when row portal sets overlap, when the
root pair changes, or when different comparisons live in different
connectors.  The note's trust boundary correctly records the last two
limitations; portal-set disjointness should be repeated there as well.

## Final audit status after repair

* Literal common-row `K_7` completion: **GREEN**.
* Common-row augmentation to the rotation-edge `K_7^-` shadow: **GREEN**.
* Four-connected page implication: **GREEN** after orienting the outcome.
* Fixed-root face/holonomy proof: **GREEN** after adding nonvacuity and
  looplessness.
* Basis triangle/square certificate: **GREEN** under the now-explicit
  tournament-sign convention.

There is no hidden proof of global holonomy here.  The surviving task is
still to transport literal roots and portal orders across a connector change
or to turn the intervening cutvertex/2-adhesion into a matching equality
state.
