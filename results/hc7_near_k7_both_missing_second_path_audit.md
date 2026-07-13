# Independent audit: both-missing second-path normalization

## Verdict

**GREEN after the incorporated span-wording clarification.**  Fixing the
exact both-missing deficient path and minimizing one twin bag forces that
twin to be an induced path.  Its five required row labels have endpoint
ownership `2+(at most 1)+2`.

## 1. The comparison class is preserved

Let `X` be a detachable proper part of `B`.  If its monopoly set is
empty, deleting `X` leaves `B-X` connected and retains every required
`B`-row adjacency.  Both fixed absences survive because the deficient
bag `A` is unchanged.

If `Omega_B(X)={R}`, transfer all of `X` into `R`.  The old `X-R` edge
makes the enlarged row connected, and an edge across the connected
split `X|(B-X)` restores the required adjacency between that row and the
residual `B`.  Every other `B`-row contact remains outside `X`.

The only delicate target is `R=C`.  Here `A` is anticomplete not only to
old `C` but also to `X subseteq B`, because `AB` is an exact absent pair.
Thus `C union X` remains anticomplete to `A`; both `AB` and `AC` are
preserved.  For `R=U_i`, `C` is unchanged.  The comparison therefore
stays among models with fixed `A`, exact absent pairs, and smaller `B`.
It follows that every detachable part owns at least two of the five
labels `C,U_1,...,U_4`.

## 2. Why `B` is a path

For any spanning tree `T` of `G[B]`, every leaf singleton is detachable:
`T-x` witnesses connectedness of `B-x`.  Monopoly sets of distinct leaf
singletons are disjoint, and each has order at least two.  Five labels
permit at most two leaves, while every nontrivial tree has at least two.
Hence every spanning tree is a path.

If `G[B]` had a vertex incident with three graph edges, that three-edge
star is a forest and extends to a spanning tree retaining degree at least
three.  Therefore `Delta(G[B])<=2`; connectedness makes it a path or a
cycle.  In a cycle, three singleton deletions are detachable and would
require six disjoint monopoly labels.  The cycle is impossible, so the
induced subgraph `G[B]` is a path (with the singleton case separated).

## 3. Exact endpoint ownership and span statement

For `B=b_0...b_n`, both endpoint singletons are detachable.  Their
monopoly sets are disjoint and each has order at least two, consuming at
least four of the five row labels.  Membership in an endpoint monopoly
set says that the entire nonempty portal set of that row is exactly that
endpoint.  Hence at most one row remains outside the two endpoint
bundles.

At an arbitrary path edge, its two connected sides are detachable.  The
two disjoint side-monopoly sets again consume at least four labels.  A
row whose portal set meets both sides belongs to neither, so at most one
row crosses that edge.  Equivalently, **no path edge** belongs to two
distinct first-to-last portal spans.  This does not mean that the closed
spans are vertex-disjoint: two singleton spans in the same endpoint
bundle coincide at that endpoint, and the possible mobile span may also
touch an endpoint.  The corrected source states the exact edge version.

## 4. Scope and residual

The theorem uses exact `AB,AC` absence; without it, transferring a
singleton-owner part from `B` into `C` could create a forbidden `A-C`
edge in the fixed comparison class.  It neither shortens the deficient
path `A` nor supplies the three full neutral-row shores needed for a
`K_7` model.

Combined with the endpoint-shadow theorem, the exact nontrivial residue
is two anticomplete induced paths: `A` has its fixed `2+2` neutral-row
endpoints, while minimized `B` has two endpoint bundles covering at least
four of `C,U_1,...,U_4` and at most one mobile row.  Eliminating that
crossed frame still requires a label-faithful two-path/three-shore
exchange, a matching full-adhesion state, or one coherent two-apex
embedding.
