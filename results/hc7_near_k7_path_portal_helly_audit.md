# Independent audit: path-portal Helly dichotomy

## Verdict

**GREEN.**  The integer cut condition, the same-row singleton case, the
clique branch-set construction, and the application after wholesale
transfer are all correct.  The result applies to any fixed assignment of
transferred pieces to foreign rows; it does not by itself choose or
compare those assignments.

## 1. Exact integer cut condition

For row `F_i`, let

\[
 \ell_i=\min\{j:p_j\in R_i\},\qquad
 r_i=\max\{j:p_j\in R_i\}.
\]

The left side of cut edge `p_jp_{j+1}` contains a portal of `F_i` iff
`ell_i<=j`; the right side contains one iff `j<r_i`.  Thus the feasible
integer cuts for row `i` are exactly

\[
                         \{\ell_i,\ldots,r_i-1\}.
\]

Their intersection is nonempty exactly when

\[
                         \max_i\ell_i<\min_i r_i.
\]

The strict inequality is necessary: if the two extrema are equal, no
integer `j` can be simultaneously at least the first and strictly below
the second.

## 2. Failure gives the stated ordered obstruction

When the strict inequality fails, take `a` with minimum `r_a` and `b`
with maximum `ell_b`.  Then `r_a<=ell_b`.

If `a!=b`, every portal index of `F_a` is at most `r_a`, and every portal
index of `F_b` is at least `ell_b`; hence all portals of the first row
occur weakly before all portals of the second.  Equality is allowed and
means one path vertex may be adjacent to both disjoint rows.

If `a=b`, the general inequalities `ell_a<=r_a` and
`r_a<=ell_a` force equality.  Since a path has only one vertex at that
index and `R_a` is nonempty, `R_a={p_{ell_a}}` is literally a singleton.
This exhausts the same-row extremal case; it is not silently treated as
two distinct ordered rows.

Either obstruction makes a common cut impossible, so the alternatives
are mutually exclusive as well as exhaustive.

## 3. Clique-minor branch sets

In the overlap outcome, the two path intervals are nonempty, connected,
disjoint, and adjacent through `p_jp_{j+1}`.  Each interval has an actual
portal edge to every `F_i`.  The `F_i` are connected, pairwise disjoint,
pairwise adjacent, and disjoint from the path.  Therefore

\[
             P[0,j],\quad P[j+1,m],\quad F_1,\ldots,F_s
\]

are `s+2` connected, disjoint, pairwise adjacent branch sets.  No
transitive adjacency or contracted quotient edge is used.

For `s=5` this is a literal `K_7` model.

## 4. Applicability after wholesale transfer

Whole-piece transfer keeps every transferred piece inside one connected
foreign bag and converts each old piece--path attachment into an actual
edge from `P` to that row.  The five retained rows remain connected,
disjoint, and pairwise adjacent.  Their portal sets on `P` are nonempty:
the four neutral rows retain their fixed endpoint edges, and the
contacted twin retains the required `PE` edge (using the transfer cut
edge when necessary).

Every lobe left in the deficient bag after unrestricted minimization has
neighbourhood contained in `P`.  A minor model need not be spanning, so
those lobes may be omitted.  The path `P` and the five foreign bags then
satisfy Theorem 1 exactly.

The wholesale transfer used here is an unrestricted model
normalization.  It need not preserve a previously marked two-duty Hall
certificate.  Accordingly the Helly theorem describes the path portals
for one fixed resulting row assignment; comparing different assignments
is a separate state/exchange problem.

## Scope

The theorem reduces every fixed path interface to a common-cut `K_7`, a
singleton portal row, or one ordered pair of portal spans.  It does not
eliminate the latter two alternatives, colour across their gap, or
establish that one wholesale assignment avoids them.
