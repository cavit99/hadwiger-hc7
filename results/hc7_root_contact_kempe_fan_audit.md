# Independent audit: root-contact Kempe paths and cycles

**Verdict:** **GREEN** for the stated results and their stated scope.

**Audited source:**
[`hc7_root_contact_kempe_fan.md`](hc7_root_contact_kempe_fan.md).

**Audited SHA-256:**
`27ba3ee3f82d8b3450fb741130bdd516206cb3205c9e72602edca4936be8161b`.

This was a separate internal audit of the exact source revision identified
above.  It checked the simultaneous Kempe interchange in Theorem 1.1, both
directions of the max-flow/min-cut argument in Theorem 2.1, Corollary 2.2,
and the contraction expansion and both colour cases in Theorem 3.1.
The exact promoted revision was rechecked on 2026-07-16 after its status
header was updated; the mathematical statements and proofs remain covered
by the audit below.

## 1. The one-colour-at-a-time Kempe argument

Fix `theta!=gamma`.  If no `gamma-theta` component meets both `A_gamma`
and `A_theta union B_theta`, interchange the two colours on all components
meeting `A_gamma`.  These are whole, pairwise disjoint bichromatic
components, so the resulting colouring is proper.  Every member of
`A_gamma` is switched, while the contrary assumption ensures that no
member of `A_theta` or `B_theta` is switched.  Consequently both roots miss
`gamma`, contradicting the universal colour-domination hypothesis.

The component thereby obtained contains the claimed path.  Its two root
edges give either an `a`-cycle or an `a-b` path according to the selected
terminal contact.  For distinct terminal colours `theta,phi`, the two
ambient bichromatic vertex sets intersect only in `C_gamma`; hence the
stated intersection control is exact.

## 2. The rainbow-transition min--max formula

The standard vertex-split network realizes the path family exactly.  More
explicitly, each original vertex `v` has an arc from its in-copy to its
out-copy of capacity one; every edge of `T_gamma` gives the two directed
arcs between the appropriate out- and in-copies; the source arcs, original
edge arcs, and target-to-colour arcs have unbounded capacity; and each
colour-to-sink arc has capacity one.  Integral flow decomposition therefore
gives vertex-disjoint paths, while the colour-to-sink capacities force
distinct terminal colours.  Conversely, every family counted by
`nu_gamma` routes an integral flow of the same order.  If desired, every
unbounded capacity can be replaced by `q`, since cutting all `q-1` colour
arcs gives a cut of capacity `q-1`.

For a fixed vertex set `Z`, deleting the vertex arcs of `Z` and the sink
arcs of the `r_gamma(Z)` colours reachable in `T_gamma-Z` disconnects the
source from the sink.  This gives a cut of capacity

\[
                         |Z|+r_\gamma(Z).
\]

In the other direction, let `C` be any finite cut and let `Z` be the
vertices whose capacity-one arcs occur in `C`.  A path in `T_gamma-Z` from
`A_gamma-Z` to a target of colour `theta` lifts through the network without
using `C` until it reaches the colour vertex `t_theta`.  Its sink arc must
therefore lie in `C`.  Distinct reachable colours give distinct such arcs,
so

\[
             \operatorname{cap}(C)\ge |Z|+r_\gamma(Z).
\]

The two inequalities prove the displayed min--max equality.

If `Z` avoids `C_gamma`, then each Theorem 1.1 path for a colour not counted
by `r_gamma(Z)` must meet `Z` in that colour class.  Different missed
colours require different vertices of `Z`.  This proves (2.3), and hence a
minimizer avoiding `C_gamma` can occur only when `nu_gamma=q-1`.  The final
assertion of Theorem 2.1 follows.

## 3. The two-transition corollary

Theorem 1.1 gives `nu_gamma>=1`.  If `nu_gamma>=2`, an integral maximum
flow supplies the first outcome.  Otherwise `nu_gamma=1`; because `q>=3`,
this is less than `q-1`, so Theorem 2.1 forces every minimizer to contain a
`gamma`-coloured vertex.  A minimizer of cost one is therefore `{z}` with
`r_gamma({z})=0`, exactly the second outcome.  The outcomes are exclusive:
the second makes every transition contain `z`, precluding two
vertex-disjoint transitions.

## 4. The contraction-critical rooted form

Let `H=G/as`, let `w` be the contraction vertex, and let `d` be the chosen
`q`-colouring of `H`.  The source defines the restriction exactly by

\[
 c_s(s)=d(w),\qquad c_s(v)=d(v)\quad(v\in V(J)-\{s\}),
\]

with `lambda=d(w)` and `gamma=d(b)`.  Every neighbour of `a` other than
`s` is adjacent to `w` in `H`, which makes `s` the unique
`lambda`-coloured neighbour of `a`.  Every neighbour of `b` in `J` is
adjacent to `b` in `H`, so `b` misses `gamma`.  Finally, any colouring of
`J` in which neither root is colour-dominating would extend to `G`, because
`a,b` are nonadjacent; thus `a` is colour-dominating in `c_s`.

When `lambda!=gamma`, switching the `lambda-theta` component containing
`s` would make `a` lose `lambda` unless that component contains a
`theta`-coloured neighbour of `a`.  The switch does not touch `gamma`, so
`b` would continue to miss it; the required neighbour is therefore forced.
A path from `s` to such a neighbour, together with its two root edges,
gives the claimed cycle through the actual edge `as`.  For distinct
`theta,phi`, the corresponding paths lie respectively in
`C_lambda union C_theta` and `C_lambda union C_phi`.  Their intersection is
contained in `C_lambda`; hence the full cycles intersect only in the root
`a` and `lambda`-coloured vertices, exactly as stated.

When `lambda=gamma`, the same switch makes `a` lose `lambda` if there is no
`a`-contact of colour `theta`.  Since `b` initially misses `lambda`, it can
then become colour-dominating only through a `theta`-coloured neighbour in
that component, which switches to `lambda`.  This proves precisely the
stated alternative and yields respectively the rooted cycle or rooted
`a-b` path.  If `s` is adjacent to `b`, then `wb` is an edge of `H`, so
`d(w)!=d(b)` and the `lambda!=gamma` case applies.  The count `q-2=4` for
`q=6` is therefore correct.

## 5. Scope and unresolved assumptions

No unresolved assumption or proof gap was found in Theorems 1.1, 2.1, 3.1
or Corollary 2.2 at the audited revision.  The finite graph and standard
vertex-splitting conventions are the only background conventions used.
The source correctly limits the conclusion: the bottleneck is a separator
only in `T_gamma`, the coloured paths and cycles are not minor-model labels,
and no `HC_7` conclusion or label-preserving split follows without an
additional theorem.
