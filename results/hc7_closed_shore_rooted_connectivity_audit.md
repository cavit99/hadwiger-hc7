# Independent audit: closed-shore rooted connectivity

**Verdict:** GREEN.

**Audited source:** `results/hc7_closed_shore_rooted_connectivity.md`

**Source SHA-256:**
`ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`

This hash identifies the final candidate audited, including the explicit
Jordan-curve justification for the cofacial-`K_4` obstruction.

## Line-by-line mathematical check

### 1. Separator lift

Let `(X,Y)` be the prohibited separation of `J_Q=G[A union Q]` and put

\[
Z=(X\cap Y)\cup(S-Q).
\]

Because `Q subseteq X`, the set `Y-X` is contained in `A`. Its possible
neighbours outside `Y-X` are exhausted as follows:

- neighbours in `X-Y` inside `A union Q` are excluded by the separation;
- neighbours in `R` are excluded by the hypothesis that there is no `A-R`
  edge;
- neighbours in `S-Q` are deleted in `Z`;
- neighbours in `X intersect Y` are deleted in `Z`.

Thus `Y-X` is a nonempty union of components of `G-Z`. The nonempty set `R`
survives because `Z subseteq S union A`, so `G-Z` is disconnected. Moreover,

\[
|Z|\le (|Q|-1)+(7-|Q|)=6.
\]

This contradicts seven-connectivity. The internal-`|Q|`-connectivity lemma is
therefore correct, including the edge cases `|Q|=1` and `|Q|=7`.

### 2. Applicability of the rooted diamond theorem

For the four literal roots `Q={a_0,a_1,b_0,b_1}`, the preceding lemma gives
internal four-connectivity. Under the corollary's hypothesis `|A|>=2`, the
graph `G[A union Q]` has at least six vertices. These are exactly the relevant
hypotheses of Norin--Totschnig Lemma 10, which records Jorgensen's theorem:
an internally four-connected pair `(J,Q)` with `|V(J)|>=6` contains a
`Q`-rooted `K_4^-` model.

The four disjoint bags may be indexed by their distinct literal roots, so the
later references to the missing rooted pair are legitimate.

### 3. Facial-order argument

If the nonrequired pair of the rooted diamond were consecutive in the cyclic
order `a_0,a_1,b_0,b_1`, the two opposite required bag adjacencies would give
two vertex-disjoint paths joining alternating vertices of the disk boundary.
That is impossible in a disk. This rules out all four consecutive pairs.

If all six rooted adjacencies were present, contracting the four disjoint
rooted bags in the displayed disk would give an outerplanar embedding of
`K_4`, which is impossible. Equivalently, this is the standard web
obstruction to a rooted `K_4` at four cofacial vertices. Consequently the
unique missing pair is one of `a_0b_0` and `a_1b_1`.

The final source now states the equivalent Jordan-curve argument explicitly.
The corresponding standard web obstruction also appears in Fabila-Monroy and
Wood, *Rooted K4-Minors*, arXiv:1102.3760.

### 4. Expansion along one bad path

Suppose the missing pair is `a_i b_i`. Since the two bad paths are
vertex-disjoint and have the four distinct vertices of `Q` as their ends,
the internal vertices of each path lie in `S-Q`. The rooted diamond bags lie
in `A union Q`. Hence adjoining `P_i-b_i` to the `a_i`-bag:

- preserves its connectivity;
- preserves pairwise bag disjointness;
- uses the final edge of `P_i` to repair exactly the missing adjacency; and
- leaves the interior of `P_{1-i}` disjoint from every expanded bag.

The asserted literal `Q`-rooted `K_4` with a reserved connector follows.

## Scope and duplication check

The separator lemma is a direct closed-shore refinement of the standard
internal-connectivity observation used in this literature, but no duplicate
statement was found in the repository. The rural corollary with a reserved
second connector appears to be a genuine new consequence of that observation
and Jorgensen's rooted-diamond theorem.

This result does **not** produce the fifth rooted bag, an adaptive two-carrier
return, or a complete decoder. It converts the rural branch into the narrower
augmentation problem stated in the source.

## Promotion recommendation

Promote after the source status is updated. No mathematical repair is
required.
