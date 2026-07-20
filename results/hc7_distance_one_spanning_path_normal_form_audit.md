# Audit of the shore-spanning distance-one path normal form

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_distance_one_spanning_path_normal_form.md`](hc7_distance_one_spanning_path_normal_form.md)

**SHA-256:**
`7a0ebf669e8fe47d7f609c662879905bf198e67a04677ab132f399e908ce15a9`

The final revision changes only the source status line to link this audit;
the audited mathematics is unchanged.

This is a separate internal proof audit, not external peer review.  The
verdict is conditional on the setting stated in Section 1 of the source,
in particular on the existence and asserted boundary contacts of the
connected adjacent partition `C=Q_0 dotcup Q_1`.

## 1. Induced-path and separator checks

Because every vertex of `E` is an internal vertex of the selected shortest
two-colour path, any nonconsecutive edge of `G[E]` would replace a path
interval by one edge.  The replacement still has the same two boundary
components as its ends and has no internal boundary vertex.  It is strictly
shorter, so `G[E]` is exactly the induced path asserted in Lemma 2.1.

For a proper prefix `E_i^-`, the only neighbour in `E-E_i^-` is
`p_{i+1}`.  There are no `E`--`C` edges.  Hence

\[
 N_G(E_i^-)=\bigl(N_G(E_i^-)\cap B\bigr)\mathbin{\dot\cup}\{p_{i+1}\}.
\]

This full neighbourhood is an actual separator: the prefix is nonempty,
and the nonempty opposite shore `C` lies outside the prefix and its full
neighbourhood.  If the prefix has at most seven boundary neighbours, the
separator has order at most eight; seven-connectivity makes its order seven
or eight.  Deleting the crossing edge `p_i p_{i+1}` gives the stated
proper-minor colouring response by the usual restriction-and-gluing
argument.  The suffix calculation is identical.  Thus, after excluding
that response, every proper prefix and suffix meets at least eight of the
nine boundary vertices.  No hidden boundary or shore neighbour is omitted
from this count.

## 2. Audit of the seven branch sets

For a full--full cut, the four nonsingleton branch sets are

\[
 E_i^-\cup\{x_e\},\quad E_i^+\cup\{y_e\},\quad
 Q_0\cup\{x_0\},\quad Q_1\cup\{y_0\}.
\]

They are disjoint because the four anchors are distinct boundary vertices
and `E,C,B` are disjoint.  Each is connected: the two path parts are full
to the boundary, and each `Q_j` is adjacent to `x_0,y_0` because both are
in `S-{e}`.  The two path branch sets are adjacent through
`p_i p_{i+1}`, and the two `Q` branch sets are adjacent by the assumed
adjacent partition of `C`.

Every path--`Q` cross pair is adjacent.  For example, either path part has
an edge to the anchor `x_0` in the first `Q` branch set and to `y_0` in the
second.  Finally, all four branch sets are adjacent to each of
`d,x_d,y_d`: the path parts are boundary-full, while both `Q` parts are
adjacent to every vertex of `S-{e}`.  The three singleton branch sets form
the displayed boundary triangle.  This checks all 21 required pairwise
adjacencies and proves Theorem 3.1.

## 3. Audit of the prefix/suffix trichotomy

For any cut after `p_i`, the prefix is boundary-full exactly when
`F_*<=i`, and the suffix is boundary-full exactly when `i<L_*`.
Consequently a full--full cut exists exactly when `F_*<L_*`; the integer
chosen in the source automatically satisfies `1<=i<r`.

If `F_*=L_*`, the chosen extremal boundary vertices `a,b` are both adjacent
to `p_{F_*}` by the definitions of first and last contact.  Coincidence
`a=b` is harmless.

If `F_*>L_*` and `L_*<=i<F_*`, then `i<f(a)` makes the prefix miss `a`,
and `i>=ell(b)` makes the suffix miss `b`.  Lemma 2.1 says each side misses
at most one boundary vertex, so the two sides are respectively full to
`B-{a}` and `B-{b}`.  Moreover `a` and `b` cannot coincide, since every
boundary vertex satisfies `f(s)<=ell(s)`.  The three numerical comparisons
are mutually exclusive and exhaustive, so the stated trichotomy is exact.

## 4. Trust boundary

The source proves a conditional normal form for the shore-spanning
distance-one outcome.  It does not eliminate the shared-portal case or the
oppositely missing-contact case, and it does not prove that every live
distance-one outcome has a shore-spanning path.  The audit found no stronger
claim in the source and no unverified branch-set adjacency.
