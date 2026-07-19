# Independent audit of rainbow first-hit linkages to a minimum boundary

**Verdict:** GREEN for Theorem 1, Corollary 2, and the stated trust
boundary at the exact source revision below.

**Audited source:** `results/hc7_literal_boundary_rainbow_linkage.md`

**Audited source SHA-256:**

```text
a858e87503d242ec446727821db0028bc8b703b63ad43f7ffbaea6544c487387
```

The proof text is unchanged from the independently checked revision; only
the source status line was updated before this hash was refreshed.

This is a separate internal mathematical audit, not external peer review.
It reconstructs the Rado deficiency certificate, its lift to a literal host
separator, every possible placement of a source or terminal in the Menger
set, and the exact order calculation using `|S|=k`.

## 1. Exact hypotheses and linkage quantifiers

The source set `P` lies in `V(G)-S`, while the nonempty sets

\[
                         S_1,\ldots,S_m
\]

are pairwise disjoint and partition the literal set `S`.  Hence the source
vertices and all terminal vertices are disjoint.  The assumption
`|P|>=m` supplies enough distinct unit-capacity sources; it does not assert
that paths may share an initial connected branch set.

The clean-linkage theorem used by the source selects one terminal from each
part `S_i`, links those selected terminals to distinct members of `P`, and
makes every selected terminal the first vertex of the whole union `S` met
by its path.  Reversing the directed paths if necessary gives exactly the
orientation used in Theorem 1.  Pairwise vertex-disjointness includes both
source and terminal endpoints.

The cited dependency is
`results/hc7_labelled_first_hit_rado_reduction.md`, SHA-256

```text
2bde8b468d236f26322d0072a503183efbc93f6bec9fa67f4a1a9fd101c9174f
```

Its adjacent GREEN audit is pinned to that exact revision.  In particular,
the directed network has one sink copy for each literal terminal and allows
the Menger separator to contain source vertices or selected terminal
copies.  These endpoint possibilities are retained below rather than
silently excluded.

## 2. Rado deficiency and a surviving source

If the desired labelled linkage does not exist, Rado's independent-
transversal theorem gives a nonempty index set `I` for which the clean
linkage rank is below `|I|`.  Directed vertex Menger then gives a path-
hitting set `Z` satisfying

\[
                              |Z|\le |I|-1.              \tag{A.1}
\]

The set `Z` may use vertices of `P`.  Nevertheless

\[
              |P|\ge m\ge |I|>|Z|
\]

shows that at least one source `p` is not in `Z`.  Thus the component `C`
of `p` in the nonterminal graph after deleting the nonterminal members of
`Z` is nonempty.  This remains valid when all members of `Z` are sources,
when some are selected terminal copies, or when `I=[m]`.

Map every nonterminal member of `Z` to itself and every selected terminal
copy in `Z` to its literal terminal.  The map is injective, so the resulting
literal set `bar(Z)` has order exactly `|Z|`.

## 3. Literal host-neighbourhood lift

Every nonterminal neighbour of `C` belongs to `bar(Z)`, by the definition
of the component after deleting the nonterminal members of `Z`.  Let
`t in S_I`.  If `t` has a neighbour in `C` and its directed sink copy is
not in `Z`, a path from the surviving source `p` through `C`, followed by
the last arc to that sink, avoids `Z`.  This contradicts the Menger
property.  Therefore

\[
 N_G(C)\subseteq \overline Z\ \cup\
                  \bigl(N_G(C)\cap(S-S_I)\bigr).        \tag{A.2}
\]

No endpoint case is omitted here.  A selected terminal whose copy belongs
to `Z` appears in `bar(Z)`; a source belonging to `Z` has been deleted;
and the chosen surviving source lies inside `C`, not in the displayed
neighbourhood.

Because each selected part is nonempty and the parts are disjoint,

\[
                         |S_I|\ge |I|>|Z|.
\]

Hence some selected terminal copy is not in `Z`.  Its literal terminal is
outside `C`, is not in `bar(Z)`, and, by the preceding path argument, has
no neighbour in `C`.  It is therefore outside the right-hand side of
(A.2).  The set in (A.2) is a genuine separator: `C` survives on one side
and that selected terminal survives on the other.

## 4. Exact separator order

The two sets on the right of (A.2) are disjoint: `bar(Z)` consists of
nonterminals and selected terminals, whereas the other set lies in the
unselected terminal parts.  In particular, its order is at most

\[
\begin{aligned}
 |Z|+|S-S_I|
   &\le (|I|-1)+k-|S_I|\\
   &\le (|I|-1)+k-|I|\\
   &=k-1.                                               \tag{A.3}
\end{aligned}
\]

The second inequality is in the correct direction because
`|S_I|>=|I|`.  This is the decisive specialization absent for unbounded
terminal branch sets.

Equation (A.2), the surviving vertices on both sides, and (A.3) give a
vertex separator of order at most `k-1`, contradicting `k`-connectivity.
Thus the linkage exists.  The proof also covers `m=1`: a deficient set
then has `I={1}` and `Z` empty, while `S-S_I` has order at most `k-1`.

## 5. Seven-vertex corollary

For `k=7` and `m<=5`, any five chosen source vertices give a set `P` of
order at least `m`.  Theorem 1 returns one path for every prescribed part,
using distinct sources; unused sources may simply be ignored.  The
corollary does not claim five paths when fewer than five terminal classes
are prescribed.

The final interpretation is therefore exact: once five model labels have
already been represented by pairwise disjoint nonempty subsets partitioning
a literal seven-boundary, a Hall--Rado first-hit rank defect is impossible.
It does not perform the preceding conversion from unbounded branch-set
labels to those literal boundary parts.

## 6. Trust boundary

The GREEN verdict proves only the following parameter-uniform statement:
a partition of an actual minimum-size boundary admits the clean labelled
linkage from distinct literal sources.

It does not prove any of the following.

1. A connected source branch set can be reused by several paths without
   first supplying distinct source vertices.
2. Unbounded terminal branch sets can replace the parts of `S`; the count
   in (A.3) would then fail.
3. The paths preserve a pre-existing minor model after absorption.
4. A raw order-seven separation carries compatible closed-shore boundary
   colourings.
5. `HC_7`.

Within the stated literal-source, partitioned-boundary scope, the theorem
and corollary are complete.
