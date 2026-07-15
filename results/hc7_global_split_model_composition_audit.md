# Audit of support-six model composition

**Verdict:** **GREEN.**  The rooted-triangle construction, common-core
composition, matching-contraction separator bound and the two published
three-clique applications are correct.  The theorem deliberately stops
before extracting its hypotheses from the global support family.

## 1. Rooted-triangle and common-core branch

After contracting the three disjoint prescribed roots in Lemma 1.1, deleting
an ordinary quotient vertex is the image of `H-v`, while deleting a root
image is the image of `H-V(A_i)`.  Thus the quotient is two-connected.
The two-fan from the third root to an `a_1-a_2` path gives three disjoint
connected bags: split the path across one edge between the two fan ends and
put the trimmed fan in the third bag.  The split edge and the last fan edges
give the three required adjacencies.  Expanding the contractions preserves
the named roots.

In Theorem 2.1, enlarging each `A_i` to its rooted-triangle bag does not lose
collective adjacency to the literal clique `Q`.  Corollary 2.2 uses exactly
the deletion budget

\[
                         |Q|+|A_i|\le r+2<r+3,
\]

so `G-Q-V(A_i)` is connected.  For support six, the common singleton core
is disjoint from each two-vertex bag and the assumed pairwise bag
disjointness supplies precisely the three roots required by the theorem.

## 2. Parallel-contraction branch

For a separator `T` after contracting a matching, replacing each contracted
image in `T` by its two literal endpoints increases the order by exactly
`rho(T)`.  A path surviving in the original graph would map to a walk
surviving in the quotient, so the lifted set remains a separator.  This
proves

\[
                           |T|+\rho(T)\ge k.
\]

With three contracted edges in a seven-connected graph, separators of
orders four, five and six must contain respectively at least three, two and
one contraction images.  In each equality case the lift has order seven
and retains the two nonempty quotient sides, so the claimed actual
seven-separation is legitimate.

Contraction cleanliness ensures that no contracted edge meets any other
model support.  Hence the five vertices `Q_i union {z_i}` are distinct
within each model and form a literal `K_5`; expanding a quotient branch set
through the matching restores connected, disjoint branch sets in `G`.

## 3. Published-theorem verification

Theorem 3.2(1) matches Theorem 1.11 of Kawarabayashi--Luo--Niu--Zhang,
*European Journal of Combinatorics* 26 (2005), 293--308: a
`(k+2)`-connected graph with three literal `k`-cliques whose union has
order at least `3k-3` contains a `K_{k+2}` minor.  At `k=5`, these are
seven-connectivity and union order at least twelve.

Theorem 3.2(2) matches Theorem 1.10 of Niu--Zhang, *Discrete Mathematics*
309 (2009), 4095--4107: a `(k+2)`-connected non-`(k-3)`-apex graph with
three literal `k`-cliques meeting pairwise in at most `k-2` contains a
`K_{k+2}` minor.  At `k=5`, `non-(k-3)-apex` is exactly non-two-apex and
the intersection threshold is three.  No omitted order hypothesis occurs
in either cited theorem.

Under contraction cleanliness, intersections of quotient cliques are
exactly intersections of the singleton cores, and the three contractions
reduce the union by exactly three.  Corollary 3.3 follows.  If the original
six-supports meet pairwise in at most one vertex, inclusion--exclusion gives
union order at least fifteen, so the stated special case is also correct.

## 4. Exact limitation

The audit confirms rather than removes the two live gaps.  A separated
triple need not have private split edges, and parallel contractions need
not preserve seven-connectivity.  The affine pair-cover barrier gives an
explicit abstract family with unique failed-pair witnesses but no
contraction-clean triple.  Therefore this composition theorem is sound,
but its hypotheses cannot be inferred from the audited set-system
extraction alone.
