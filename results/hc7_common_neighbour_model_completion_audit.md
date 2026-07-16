# Internal audit of common-neighbour model completion

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_common_neighbour_model_completion.md`
- final theorem SHA-256:
  `0b7fc2dd4add78bcb8e245a24156082aa17fac07c7200a970c3cc6a4d689de02`
- independently audited mathematical revision SHA-256:
  `692f65cf5ae1092e40963909d29f278a9387aa4972cc4423241fb589b3e2db17`

The final hash is a metadata-only rebind.  Replacing the final theorem's
status paragraph by the pre-promotion status paragraph reproduces the
independently audited mathematical hash exactly.  The theorem statement,
hypotheses, proof, corollary, and application are byte-for-byte unchanged;
only the status text was updated to link this GREEN audit after promotion.

This is a separate internal mathematical audit, not external peer review.  It
checks Theorem 1.1, Corollary 2.1, and the stated application to the active
endpoint-rigid configuration.  In particular, it checks the set-Menger
argument when a separator is allowed to contain terminal vertices, the exact
separator budget, branch-set disjointness after the paths are added, and all
adjacencies in the resulting `K_k` model.

An earlier draft displayed five old branch sets in the uniform theorem.  That
indexing typo was corrected to `M_1,...,M_{k-2}` before the hash above was
taken.  No mathematical gap remains from it.

## 1. Initial model and the case in which every branch set meets `W`

The given model has `k-2` nonempty, pairwise disjoint connected branch sets
`M_i`, and they are pairwise adjacent.  Because it lies in `G-{a,b}`, both
singleton sets `{a}` and `{b}` are disjoint from all model branch sets.  If
every `M_i` meets `W`, then each is adjacent to each singleton: a vertex of
`M_i\cap W` is adjacent to both `a` and `b`.  The edge `ab` supplies the last
adjacency.  Thus

\[
                 M_1,\ldots,M_{k-2},\{a\},\{b\}
\]

are exactly `k` disjoint connected pairwise adjacent sets.  The immediate
`K_k` conclusion is valid for every `k>=3`.

## 2. Cardinalities in the deficient-branch-set case

Let `I` index the `h>=1` branch sets missing `W`, and select one vertex `c_i`
from each.  The selected set `A`, the unused common-neighbour set `T`, and the
deleted set

\[
       Z=\left(\bigcup_i M_i-A\right)\cup\{a,b\}
\]

are pairwise disjoint.  The selected vertices do not lie in `W`, by the
definition of `I`.  Hence every model vertex that does lie in `W` remains in
`Z`, and there are at most `m-h` such vertices.  Therefore

\[
 |Z|=m-h+2,
 \qquad
 |T|\ge |W|-(m-h)\ge k-m+h\ge h+1.
\]

All three inequalities use only the stated hypotheses `|W|>=k` and
`m<=k-1`; no hidden equality or boundary-size assumption is used.

The extreme arithmetic cases are also safe.  For `h=1`, `T` still has at
least two vertices.  For the largest possible `h`, the support contains at
least one vertex for every branch set and the same displayed estimates
remain valid.  In the sharp case `m=k-1`, failure of the desired linkage can
indeed use the whole order-`k` separator allowance; the proof does not
silently claim a smaller cut.

## 3. Menger alternative and the actual separator

Apply the vertex-set form of Menger's theorem in `G-Z`.  If fewer than `h`
pairwise vertex-disjoint `A`--`T` paths exist, there is an `A`--`T`
separating set `X` of order at most `h-1`.  This formulation permits `X` to
meet the terminal sets, which is harmless here:

- `|A|=h` implies `A-X` is nonempty;
- `|T|>=h+1` implies `T-X` is nonempty; and
- by the separating property, no path in `G-(Z union X)` joins those two
  nonempty sets.

Thus `Z union X` is genuinely an actual vertex separator of `G`, not merely
a relative separator in `G-Z`.  Its order satisfies

\[
 |Z\cup X|\le (m-h+2)+(h-1)=m+1\le k.
\]

Since `G` is `k`-connected, an actual separator has order at least `k`.
Consequently every inequality is forced to equality in the surviving
separator alternative, and the separator has order exactly `k`.  This
justifies outcome 2 exactly as stated.

## 4. Linkage normalization and branch-set disjointness

In the other Menger alternative there are `h` disjoint `A`--`T` paths.
Under the standard set-linkage convention their ends in `A` and `T` are
distinct.  The same conclusion follows even from the more permissive path
definition: `h` disjoint paths, each containing an `A`-vertex, already use
all `h` vertices of `A`, so no one path can consume an additional selected
vertex.  The paths can therefore be indexed by their unique starts `c_i`.

Every old model vertex outside `A` lies in `Z`, so a path in `G-Z` meets the
old model only at its own initial selected vertex.  Stopping at the first
visit to `W` preserves pairwise disjointness.  That first vertex is in `T`,
because every vertex of `W` already used by the old model lies in `Z`.
The stopped paths have distinct endpoints because the original paths were
vertex-disjoint.

For each deficient index `i`, adjoining its stopped path to `M_i` therefore:

- preserves connectivity;
- introduces no intersection with another branch set;
- introduces no intersection with `{a}` or `{b}`, since both were deleted
  into `Z`; and
- preserves every old branch-set adjacency.

Every enlarged branch set now contains a vertex of `W`, as does every
unchanged branch set.  Hence every branch set is adjacent to both `a` and
`b`, while `ab` joins the two singleton branch sets.  Together with the old
pairwise model adjacencies, this accounts for every adjacency among the `k`
proposed branch sets.  The resulting `K_k`-minor model is valid and
label-preserving.

## 5. Singleton-shore corollary

In Corollary 2.1, `V={v}` and fullness of the open shore imply that `v` is
adjacent to every vertex of `S`.  The boundary hypothesis on `s` gives

\[
        vs\in E(G),\qquad
        S-\{s\}\subseteq N_G(v)\cap N_G(s),\qquad
        |S-\{s\}|=7.
\]

The two vertices `v,s` are distinct because `v` lies in `G-S`.  Hypothesis
(2.1), applied to this two-set, supplies a `K_5` model of support at most six
in `G-{v,s}`.  These are precisely Theorem 1.1's hypotheses with

\[
              k=7,\quad a=v,\quad b=s,\quad W=S-\{s\}.
\]

The theorem therefore returns a `K_7` minor or an actual order-seven
separator, exactly as claimed.  Neither the unused component `U` nor any
unstated adjacency between the open shores is invoked.

## 6. Active-configuration application and scope

The application in Section 3 is conditional on the three hypotheses it
names: the global support-at-most-six response for every deleted pair, the
universal boundary vertex `s`, and fullness of both open shores.  Under
those hypotheses, Corollary 2.1 excludes a singleton opposite shore whenever
the host has neither a `K_7` minor nor an actual order-seven separation.
This deduction is independent of the complementary-defect pattern of the
particular six-vertex `K_5` model.

The theorem does **not** eliminate an opposite shore with two or more
vertices, prove that `V-v` is connected, or settle any of the remaining
mixed-shore configurations.  It also does not turn an order-seven separator
into a contradiction; it deliberately records that separator as the second
outcome.  These limitations agree with the theorem's stated scope.

## 7. Falsification checks

I attempted to break the proof at the three extremal points where a false
completion lemma commonly fails:

1. allowing a failed-linkage separator to delete terminal vertices;
2. taking maximum support `m=k-1`, where the cut budget is tight; and
3. letting `W` overlap the old model as much as the hypotheses permit.

The nonempty-terminal counts, exact order calculation, and placement of all
old `W`-vertices in `Z` respectively close those possibilities.  I found no
construction satisfying the hypotheses while avoiding both stated
outcomes.  The proof is self-contained apart from the standard vertex-set
form of Menger's theorem.
