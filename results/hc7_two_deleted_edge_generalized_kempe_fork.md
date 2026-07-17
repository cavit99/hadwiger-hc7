# A generalized Kempe-chain fork for two deleted edges

**Status:** written proof, independently audited in
[`hc7_two_deleted_edge_generalized_kempe_fork_audit.md`](hc7_two_deleted_edge_generalized_kempe_fork_audit.md).
The theorem is uniform in the number of colours.  Its six-colour corollary applies to the
two opposite clique edges in the balanced order-eight configuration, but it
does not by itself produce a `K_7` minor or settle that configuration.

## 1. Relation to Moore--West

The reachable-set recolouring used below is the argument in the proof of
Theorem 3 of Moore and West, *Cycles in Color-Critical Graphs*, Electronic
Journal of Combinatorics **28** (2021), #P4.35.  Their theorem starts with a
colouring of `G-e`; because there is only one deleted edge, the opposite end
of `e` must belong to the reachable set.  Here two disjoint edges are
deleted.  The new point is that failure to reach the opposite end of the
first edge gives a proper colouring after restoring that edge, while
noncolourability of `G` forces the second deleted edge to remain
monochromatic.

The relevant result in the published Moore--West paper is **Theorem 3**, not
Theorem 2.

## 2. The two-edge fork

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
                         e=ab,\qquad f=cd
\]

be vertex-disjoint edges.  Put `H=G-{e,f}`.  Suppose that `phi` is a proper
`q`-colouring of `H` satisfying

\[
                 \phi(a)=\phi(b),\qquad \phi(c)=\phi(d).       \tag{2.1}
\]

Let `Omega` be a set of at least two colours containing
`alpha=phi(a)`, and let `sigma` be a cyclic permutation of `Omega`, fixing
all colours outside `Omega`.  Define a digraph `D_sigma` on `V(H)` by putting
an arc from `u` to `v` whenever

\[
             uv\in E(H)\quad\hbox{and}\quad
             \phi(v)=\sigma(\phi(u)).                         \tag{2.2}
\]

Let `F` be the set of vertices reachable from `a` in `D_sigma`.

### Theorem 2.1 (generalized Kempe-chain fork)

Exactly one of the following alternatives holds.

1. The vertex `b` belongs to `F`.  Consequently `H` contains a directed
   `a-b` path in `D_sigma`; along this path the colours advance in the
   cyclic order `sigma`.
2. The vertex `b` does not belong to `F`.  Replacing `phi(v)` by
   `sigma(phi(v))` for every `v in F` gives a proper `q`-colouring of
   `G-f`.  In its restriction to `H`, the ends of `e` have different
   colours and the ends of `f` still have equal colours.

#### Proof

Define

\[
 \phi_\sigma(v)=
 \begin{cases}
   \sigma(\phi(v)),&v\in F,\\
   \phi(v),&v\notin F.
 \end{cases}                                                \tag{2.3}
\]

This is a proper colouring of `H`.  Indeed, applying the same permutation
to both ends of an edge preserves their inequality, as does changing
neither end.  If an edge `uv` with `u in F` and `v notin F` became
monochromatic, then

\[
                         \sigma(\phi(u))=\phi(v).
\]

By (2.2), `D_sigma` would contain the arc `uv`; reachability of `u` would
then imply reachability of `v`, a contradiction.  The case with the roles
of `u,v` reversed is the same.

If `b in F`, reachability gives the path in alternative 1.  Its successive
colours follow `sigma` by (2.2).  A simple directed path may be chosen.

Suppose instead that `b notin F`.  Since `a in F`, (2.1) and (2.3) give

\[
       \phi_\sigma(a)=\sigma(\alpha)\ne\alpha
                     =\phi_\sigma(b).
\]

Thus the deleted edge `e` can be restored.  If the ends of `f` also had
different colours under `phi_sigma`, then both deleted edges could be
restored and `phi_sigma` would be a proper `q`-colouring of `G`.  This is
excluded by hypothesis.  Hence the ends of `f` remain equal, and
`phi_sigma` is a proper `q`-colouring of `G-f`.  This is alternative 2.
The alternatives are exclusive because they are distinguished by whether
`b` belongs to `F`.  \(\square\)

The symmetric statement holds after interchanging `e` and `f`.  Notice
that a cyclic permutation on more than two colours is a generalized Kempe
recolouring, not necessarily one ordinary two-colour Kempe interchange.

## 3. A near-clique consequence with fixed endpoints

Assume `q>=3`.  Suppose that `H` contains every edge except `e=ab` of a
clique on

\[
                         \{a,b,r_1,\ldots,r_{q-3}\},
\]

and retain the colouring `phi` from (2.1).  The vertices
`r_1,...,r_{q-3}` form a clique in `H` and are adjacent there to both
`a,b`.  Hence the `q-2` colours used on

\[
                         \{a,r_1,\ldots,r_{q-3}\}
\]

are distinct.  Let `gamma,delta` be the two remaining colours, and put

\[
                \sigma_+=(\alpha\ \gamma\ \delta),\qquad
                \sigma_-=(\alpha\ \delta\ \gamma),            \tag{3.1}
\]

fixing the other `q-3` colours.

### Corollary 3.1 (two fixed-end replacement paths or a response colouring)

At least one of the following holds.

1. For one of `sigma_+,sigma_-`, the reachable-set recolouring in
   Theorem 2.1 gives a proper `q`-colouring of `G-f`.  Its restriction to
   `H` makes `e` proper and keeps `f` monochromatic.
2. The graph

   \[
                          H-\{r_1,\ldots,r_{q-3}\}
   \]

   contains two distinct `a-b` paths `P_+,P_-`.  Along `P_+` the colours
   advance in the order `alpha,gamma,delta`, and along `P_-` they advance
   in the order `alpha,delta,gamma`.  Each path has length divisible by
   three and keeps the original endpoints `a,b` of the deleted clique
   edge.

#### Proof

Apply Theorem 2.1 separately to the two permutations in (3.1).  If either
application has its second outcome, assertion 1 holds.  Otherwise both
applications give directed `a-b` paths.

Every vertex on either path has one of the colours
`alpha,gamma,delta`.  The vertices `r_1,...,r_{q-3}` have the other
`q-3` colours, so both paths avoid them.  The first vertex after `a` on
`P_+` has colour `gamma`, while the first vertex after `a` on `P_-` has
colour `delta`.  Therefore the two paths are distinct.  Since both begin
and end in colour `alpha` and each step advances once around a three-cycle
of colours, their lengths are divisible by three.  \(\square\)

Each path also gives a label-preserving `K_{q-1}`-minor model in `H`:
take `V(P_+)-{b}` (or `V(P_-)-{b}`) as the branch set containing `a`,
and take `{b},{r_1},...,{r_{q-3}}` as singleton branch sets.  Thus the
path outcome regenerates the deleted near-clique with all
`r_i`-labels and the endpoint `b` fixed.

The corollary does **not** assert that `P_+` and `P_-` are internally
vertex-disjoint.  Their value is that they avoid the other `q-3` vertices
of the near-clique and preserve the named ends of its deleted edge.  Any
use in a clique-minor construction still requires a disjointness,
separation, or branch-set composition argument.

## Reference

Benjamin Moore and Douglas B. West,
[*Cycles in Color-Critical Graphs*](https://doi.org/10.37236/10177),
Electronic Journal of Combinatorics **28** (2021), #P4.35, Theorem 3 and
its reachable-set recolouring proof.
