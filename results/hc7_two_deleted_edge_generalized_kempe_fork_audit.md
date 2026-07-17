# Independent audit: two-deleted-edge generalized Kempe fork

**Audited file:** `results/hc7_two_deleted_edge_generalized_kempe_fork.md`
**SHA-256:** `880b9d30946357b1df0540543b5ffe1d38def7f68224577ebe476e4bed9a6370`
**Verdict:** **GREEN.**  Theorem 2.1 and Corollary 3.1 are correct as
stated.  No substantive correction is required.  The result remains only
the stated fork: its path outcome does not itself give disjoint paths or a
`K_7`-minor model.

This revision generalizes the near-clique corollary from six colours and a
five-clique to every `q>=3` and a retained `K_{q-1}` minus one edge.  During
the audit, the phrase “the other three colours” was corrected to “the other
`q-3` colours”; the hash above is for the corrected theorem.

## Citation check

The cited source and theorem number are correct for the published paper:
Benjamin Moore and Douglas B. West, *Cycles in Color-Critical Graphs*,
Electronic Journal of Combinatorics **28** (2021), #P4.35, Theorem 3.
The proof of that theorem defines the same directed graph from a cyclic
permutation, recolours the set reachable from one end of the deleted edge,
and forces the other end to be reachable.  Thus the draft accurately
distinguishes the cited one-deleted-edge argument from its elementary
two-deleted-edge extension.

Primary source:
<https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p35/pdf/>

## Line-by-line mathematical check

### Theorem 2.1

1. A cyclic permutation of a set of at least two colours moves
   `alpha`, so `sigma(alpha) != alpha`.
2. Recolouring every reachable vertex by the same permutation preserves
   every edge with both ends inside or both ends outside the reachable
   set.
3. If a crossing edge became monochromatic, its orientation from the
   reachable end to the unreached end would satisfy the defining colour
   relation and make the latter reachable.  This proves that the
   recolouring is proper on `H`.
4. If `b` is reachable, a simple directed `a-b` path can be chosen and
   its colours advance according to `sigma`.
5. If `b` is not reachable, the recolouring separates the colours of
   `a,b`, so `e` can be restored.  If it also separated the ends of `f`,
   restoring both deleted edges would give a forbidden `q`-colouring of
   `G`.  Hence the ends of `f` remain equal and the recolouring is proper
   on `G-f`.
6. The alternatives are exhaustive and exclusive because they are
   exactly the cases `b in F` and `b notin F`.

The argument does not require contraction-criticality or minimality; the
sole global hypothesis used at the fork is that `G` is not
`q`-colourable.  Vertex-disjointness of `e` and `f` is correctly retained
for the later clique application.

### Corollary 3.1

1. The hypothesis that `H` retains every edge except `e=ab` of the
   displayed `K_{q-1}` implies that the `q-3` vertices `r_i` form a clique
   and are adjacent to both `a,b`.  Hence they receive `q-3` pairwise
   distinct colours, all different from `alpha`, while `a,b` both receive
   `alpha`.  Exactly two colours `gamma,delta` remain.
2. The permutations in (3.1) are well-defined for every `q>=3`: they cycle
   `alpha,gamma,delta` and fix the other `q-3` colours.
3. Starting from `alpha`, a directed path for either three-cycle remains
   in its three-colour support, since every arc advances by that cycle.
   Hence both paths avoid every `r_i`.
4. Their first vertices after `a` have colours `gamma` and `delta`,
   respectively.  Thus the two simple paths are distinct.
5. Both paths start and end with colour `alpha`, and every arc advances
   one step around a three-cycle, so each path length is divisible by
   three.
6. For either path `P`, the set `V(P)-{b}` is nonempty, connected, contains
   `a`, and is adjacent to the singleton `{b}` through the last edge of
   `P`.  It is adjacent to every singleton `{r_i}` through the retained
   edge `ar_i`; the singleton branch sets `{b},{r_1},...,{r_{q-3}}` are
   pairwise adjacent by the retained near-clique.  These are therefore
   pairwise disjoint branch sets of a label-preserving `K_{q-1}`-minor
   model in `H`.

For `q=3`, the indexed family of reserved vertices is empty.  Each path
has positive length divisible by three, and the two branch sets
`V(P)-{b}` and `{b}` form the asserted labelled `K_2`-minor model.  Thus no
unstated `q>=4` or nonempty-reserved-clique assumption is used.

## Optional clarity edits

The following is not a correctness issue:

- The proof could explicitly say that reachability from an
  `Omega`-coloured vertex stays within `Omega`; this is already immediate
  from the arc definition.
- The corollary actually gives exclusive outcomes, but the weaker phrase
  “at least one” is valid.

## Trust boundary

The audit does **not** infer that the two replacement paths are internally
disjoint, that their union repairs the second deleted edge, or that the
regenerated labelled `K_{q-1}` model can automatically be composed with
other branch sets to make a larger clique minor.  Those are precisely the
remaining composition obligations identified in the theorem file.
