# Independent cold audit: rigid cross-arm double-root cover

## Verdict

**GREEN for Theorem 1.1, the existence assertion in Corollary 1.2,
Corollary 2.1, and Proposition 3.1, after two scope repairs recorded
below.**  Neither repair strengthens a theorem.

1. The final sentence of Corollary 1.2 may speak of an actual labelled
   `K_5` model only after adding the graph-support hypothesis introduced in
   Section 2.  Under the abstract hypotheses of Section 1, its members are
   merely sets.
2. The last paragraph of the displayed proof of Proposition 3.1 invokes
   the one-root forced-replacement conclusion of the earlier corrected
   cross-arm theorem, although that conclusion is not included among this
   note's self-contained hypotheses.  The proposition nevertheless follows
   immediately, and more strongly, from its preceding paragraph: if every
   small support contains both vertices of `Z`, then either vertex of `Z`
   is a one-vertex transversal of `F`, contradicting `tau(F)>2`.

No counterexample was found after testing the four possible `5/6` size
combinations and both possible literal-arm orientations.

## 1. Theorem 1.1

Let `R` be a two-subset of `A` meeting `I=A cap X`.  Since
`tau(F)>2`, it misses some member `D_R`.  This member cannot equal `A`,
because `A` contains both vertices of `R`.  The private pair therefore
meets `D_R`.

If `D_R` contains exactly one private root, say `p`, avoidance of the two
vertices of `R` gives

\[
                         |A\cap D_R|\le |A|-2.
\]

The comparison with the separated-arm threshold is valid in every size
combination:

| `|A|` | `|D_R|` | upper bound from avoiding `R` | threshold `max-2` |
|---:|---:|---:|---:|
| 5 | 5 | 3 | 3 |
| 5 | 6 | 3 | 4 |
| 6 | 5 | 4 | 4 |
| 6 | 6 | 4 | 4 |

Thus `D_R` is literally a member of the exact-one-root family
`mathcal B_p`, not merely a support with a suggestive label.  Rigidity
forces

\[
                          D_R=X\cup\{p\}.
\]

But a vertex of `R cap I` lies in `X`, contradicting the choice that
`D_R` avoid `R`.  The same argument excludes exact trace `{q}`.  Since
the private pair meets `D_R`, both roots belong to it.  This proves
Theorem 1.1.

No assumption that the witnesses `D_R` are distinct is used.  The result
also does not control which other at most four vertices they contain.

## 2. Corollary 1.2

For fixed `a in I` and `b in A-{a}`, apply Theorem 1.1 to
`R={a,b}`.  The returned set contains `p,q`, so its order-five/six bound
leaves at most four other elements.  This is the complete abstract
conclusion.

The phrase "carries an actual bounded labelled model" is valid in the
intended application where `F` is a family of vertex supports of actual
`K_5` models.  It is not a consequence of the abstract set-family
hypotheses as currently positioned in Section 1.

## 3. Literal-arm orientation

If the two rigid arms have order five, exact-one-root membership implies
`p,q notin X`, and hence `|X|=4`.  A `K_5` model supported on five
vertices has five singleton bags, so both arms are literal cliques.  Thus
`X` is a `K_4` and each private root is complete to it.

If `pq` were an edge, `X union {p,q}` would be a literal `K_6`.  The
claimed connectivity lift is sound.  A seven-connected graph has at least
eight vertices, so the complement of this six-set is nonempty and remains
connected after deleting the six clique vertices.  If one clique vertex
had no neighbour in that complement, the other five clique vertices would
separate it from the complement.  Hence the connected complement contacts
all six singleton clique bags and supplies a seventh branch bag.  This
would give a `K_7` minor.  Therefore `pq` is absent.

An order-five support containing both roots would be a literal clique and
would contain the missing edge `pq`; hence every double-root support has
order six.  In any spanning five-bag model on six vertices there is exactly
one two-vertex bag and four singleton bags.  The two nonadjacent roots
cannot be different singleton bags and cannot jointly form the connected
two-vertex bag.  Exactly one root is therefore in the edge bag and the
other is a singleton.  This verifies both orientations and does not assume
that one orientation is preferred or consistent across different
supports.

## 4. Two-apex consistency check

Let `H=G-Z`.  Deleting at most four vertices from `H` deletes at most six
vertices from the seven-connected graph `G`, so `H` is five-connected
under the standard order convention; it is planar by hypothesis.

A small `K_5` model avoiding `Z` would be a `K_5` minor in `H`.  If it
contained exactly one vertex of `Z`, delete the entire branch bag that
contains that vertex.  The remaining four bags lie in `H`, remain
pairwise adjacent, and use at most five vertices.  They form a
support-at-most-five `K_4` model, contradicting the audited
five-connected-planar exclusion theorem.  Hence every small `K_5` support
contains both vertices of `Z`.

At this point the proposition is already proved: every member of `F`
contains each vertex of `Z`, so `tau(F)<=1`, contrary to the standing
condition `tau(F)>2`.  Alternatively, in an application that explicitly
imports the full corrected cross-arm theorem, the source's forced-
replacement contradiction is also valid.  The direct transversal proof
is self-contained and avoids that unstated dependency.

## 5. Trust boundary

The audited result is a set-system forcing lemma plus a local orientation
fact.  It does not make the double-root supports distinct, align their
two-vertex bags, confine their other vertices to `A union P`, or compose
opposite orientations into disjoint branch sets.  It excludes the
two-apex architecture but does not close the non-two-apex rigid cell.
