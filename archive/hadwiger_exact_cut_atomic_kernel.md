# Atomic surplus and rooted-state kernels at an exact cut

## 1. Purpose

Two different phenomena have been conflated in the exact-seven-cut
recursion.

* A new cut of the same order may occur strictly inside the current
  shore.
* Before minor-criticality and rooted well-quasi-ordering are used, a
  single torso has no evident size bound even when no such nested cut
  occurs.

The first phenomenon can be removed altogether by starting at a minimum
fragment.  The second has an exact, label-preserving finite-kernel
theorem.  Neither statement colours the final surplus torso, but together
they show that following a tower of exact cuts is unnecessary.  When the
cut defining the minimum fragment has exactly two components, the remaining
two-shore object is one atomic surplus bad split.  A minimum cut with three
or more components is a separate atomic configuration; the two-shore
cyclic-hull theorem does not apply to it without an additional reduction.

Throughout, an `r`-minor-critical graph is not `r`-colourable while every
proper minor is `r`-colourable.

## 2. Minimum fragments turn every tight outcome into strict surplus

Let `G` be `k`-connected.  A **minimum fragment** is a component `D` of
`G-S`, where `S` is a `k`-cut, chosen with `|D|` minimum over all such
components and cuts.

### Theorem 2.1 (atomic surplus)

Let `D` be a minimum fragment, and let

\[
 D=X\mathbin{\dot\cup}Y
\]

be a partition into nonempty connected sets which are adjacent.  Put

\[
 P_X=N_S(X),\qquad T_X=N_Y(X),
\]

and define `P_Y,T_Y` symmetrically.  Then

\[
 |P_X|+|T_X|\ge k+1,
 \qquad
 |P_Y|+|T_Y|\ge k+1.                 \tag{2.1}
\]

#### Proof

Because `D` is a component of `G-S`, every neighbour of `X` outside `X`
lies in `P_X union T_X`.  Conversely every vertex of those two sets is a
neighbour of `X`, and hence

\[
 N_G(X)=P_X\mathbin{\dot\cup}T_X.                  \tag{2.2}
\]

Since `S` is a cut, `G-S` has a component `D'` other than `D`.  The set
in (2.2) is disjoint from `D'` and separates the nonempty connected graph
`X` from `D'`.  (It need not leave a vertex of `Y`: it is possible that
\(Y\subseteq T_X\).)  Thus `k`-connectivity gives
`|P_X|+|T_X| >= k`.

If equality held, (2.2) would be a `k`-cut and `X` would be a component
of `G-N_G(X)`: it is connected and every one of its external neighbours
has been removed.  Since `X` is a proper subset of `D`, this contradicts
the choice of `D`.  Therefore the first inequality in (2.1) is strict.
The proof for `Y` is identical.  \(\square\)

### Corollary 2.2 (no descent is needed)

In a seven-connected graph, every covering split of a minimum fragment
satisfies

\[
 |N_S(X)|+|N_Y(X)|\ge8,
 \qquad
 |N_S(Y)|+|N_X(Y)|\ge8.              \tag{2.3}
\]

Consequently any local theorem whose third outcome is precisely the
neighbourhood cut of one proper connected part of such a split, and whose
outcomes are

1. a target minor;
2. a colouring; or
3. a strictly nested exact seven-cut,

closes at once when applied to a minimum fragment: outcome 3 is
impossible by Theorem 2.1.  The finite state-depth theorem is needed only
if one starts from a non-atomic cut.  This assertion does not cover an
unrelated exact cut produced elsewhere in the graph.

In particular, if the cut defining a minimum fragment has exactly two
components and the hypotheses of the two-full-shore cyclic-hull theorem
hold there, a hypothetical `K7`-minor-free non-six-colourable graph has an
**atomic surplus bad split** on that fragment.  This is the sharp normal
form for the remaining two-shore interface exchange: both sides of the
split satisfy (2.3), so a proof may not terminate by exposing the
neighbourhood of either split part as another exact seven-cut.  The
minimum-fragment argument alone does not turn a cut with three or more
components into a two-shore cut; that atomic multi-component case remains
outside this particular cyclic-hull reduction.

## 3. Exact rooted state-minimality of every component

Fix a graph `J` on a labelled root set `S` of order `k`.  For an
`S`-boundaried graph `H` whose root graph is `J`, let

\[
 \mathcal E_r(H,S)
\]

be the equality partitions of `S` induced by proper `r`-colourings of
`H`.

An **`S`-rooted minor** keeps all labelled roots distinct.  Root branch
sets may contain non-root vertices, but no two roots are identified and
the prescribed root graph `J` is retained.  This is the usual labelled
minor relation.  Surplus root edges created by contractions may be
deleted.  Here "proper" means that the corresponding operations change
the underlying simple graph (so merely deleting a parallel copy created
during a contraction is not counted as a proper operation).

### Theorem 3.1 (rooted state-minimality)

Let `G` be `r`-minor-critical, let `S` be a separator, and let `C` be a
component of `G-S`.  Put

\[
 H=G[S\cup C].
\]

There is no proper `S`-rooted minor `H'` of `H` with

\[
 \mathcal E_r(H',S)=\mathcal E_r(H,S).              \tag{3.1}
\]

#### Proof

Perform in `G` the deletions and contractions which realize `H'` inside
`S union C`, leaving every other component of `G-S` unchanged.  This
gives a proper minor `G'` of `G`.

There is no hidden interaction with another component.  A vertex of `C`
has no neighbour outside `C union S`.  If a root branch set contains
vertices of `C`, contracting it into its labelled root preserves all
old edges from that root to the other components and creates no edge
from an interior vertex of `C` to them.  Any surplus edge between two
roots created inside the branch sets may be deleted; every prescribed
edge of `J` is retained.

If `G'` had an `r`-colouring, its state `Pi` on `S` would belong to
`E_r(H',S)`.  By (3.1), `Pi` extends over the original graph `H` as
well.  Permute the colours of that extension so that the blocks of `Pi`
agree pointwise with the colouring of `G'` outside `C`, and glue.  This
would `r`-colour `G`, a contradiction.  Hence `G'` is not
`r`-colourable, contrary to minor-criticality.  \(\square\)

The equality in (3.1) is essential.  A one-step operation in a critical
side is allowed, and in fact required, to unlock a new state realized by
the opposite side.

## 4. Uniform finite kernels for fixed boundary and palette

### Theorem 4.1 (finite rooted-state kernel)

For fixed integers `r,k` and a fixed labelled root graph `J`, there is a
finite family

\[
 \mathfrak K(r,J)
\]

such that every component side `G[S union C]` occurring at a separator
`S` with `G[S]=J` in an `r`-minor-critical graph is isomorphic, as a
rooted graph, to a member of `K(r,J)`.

#### Proof

There are finitely many equality states on `S`, and therefore finitely
many possible extension families `E_r(H,S)`.

Graphs with a fixed finite labelled root set are well-quasi-ordered by
the rooted minor relation, by the labelled form of the Graph Minor
Theorem.  Fix one extension family `F`.  The rooted-minor-minimal members
of

\[
 \{H:\mathcal E_r(H,S)=F\}
\]

form an antichain and hence are finite.  Taking the union over the
finitely many families `F` gives a finite set `K(r,J)`.

Theorem 3.1 says that every component side in an `r`-minor-critical graph
is one of these rooted-minor-minimal members.  \(\square\)

For clarity, the relation used here really is the standard labelled
minor relation restricted to graphs with root graph `J`.  Use a finite
antichain of labels: give root `i` its own label and every non-root a
common label distinct from all root labels.  Under the equality label
order, the branch set for target root `i` must contain a source vertex
with label `i`, namely the unique source root `i`.  Since every target
root occurs and branch sets are disjoint, no source root can be swallowed
by a different branch set.  Both source and target contain every edge of
`J`, so those edges can be retained, while any surplus root edge may be
deleted.  Hence restricting to the fixed-`J` class does not introduce a
stricter, potentially non-well-quasi-ordered relation.

This is an existence theorem; the resulting bound from the Graph Minor
Theorem is not a practical enumeration bound.  It should not be confused
with an effective protrusion replacement theorem: no computable numerical
value of the kernel bound is asserted here.

## 5. The whole exact-cut graph is bounded

Let

\[
 \Omega_r(J)
\]

be the proper equality states of `J` with at most `r` blocks, and put

\[
 b(r,J)=\max_{H\in\mathfrak K(r,J)}(|V(H)|-|S|).
\]

### Theorem 5.1 (bounded exact-cut obstruction)

If an `r`-minor-critical graph `G` has a separator `S` with `G[S]=J`,
then

\[
 |V(G)|\le
 |S|+|\Omega_r(J)|\,b(r,J).                        \tag{5.1}
\]

#### Proof

Let `C_1,...,C_m` be the components of `G-S`, and put

\[
 \mathcal F_i=\mathcal E_r(G[S\cup C_i],S).
\]

The graph `G` is `r`-colourable exactly when
`intersection_i F_i` is nonempty.  Hence this intersection is empty.

Delete `C_i`.  The resulting proper minor is `r`-colourable, so it
supplies a state

\[
 \phi_i\in\bigcap_{j\ne i}\mathcal F_j.
\]

When `m=1`, the empty intersection here is understood as
`Omega_r(J)`; the colouring of `G-C_1=J` supplies the asserted state.

Necessarily `phi_i notin F_i`, or all components could be glued using
that state.  The states `phi_i` are pairwise distinct: if
`phi_i=phi_j`, the witness for deleting `C_i` puts that state in `F_j`,
whereas the witness for deleting `C_j` puts it outside `F_j`.
Thus

\[
 m\le|\Omega_r(J)|.                                 \tag{5.2}
\]

Theorem 4.1 bounds every `|C_i|` by `b(r,J)`.  Summing and using (5.2)
gives (5.1).  \(\square\)

### Corollary 5.2 (HC7)

For every fixed seven-vertex boundary graph `J`, there is a constant
`B_J` such that a six-minor-critical graph having a seven-cut inducing
`J` has at most `B_J` vertices.  Since there are only finitely many
graphs `J` on seven vertices, one constant works for every exact
seven-cut.

This closes the **unbounded-order** part of the exact-cut problem, not
the finite residue.  In the current constructive programme the more
useful conclusion is Corollary 2.2: choose an atom first and discard each
tight outcome that is the neighbourhood of a proper connected part of
that minimum fragment.  If its defining cut has two components, one then
attacks only the surplus two-shore interface; a cut with three or more
components remains a different atomic case.  A claim that exact states
alone glue the final atom would still be false; the portal placement or
rooted-minor geometry must be used.

## 6. Final audit boundary

The rooted-kernel proof uses only three facts which must not be weakened.

1. Roots are never deleted or identified with one another.  Allowing a
   boundary identification would change the state space.
2. The *whole* exact extension family is preserved in Theorem 3.1.  A
   single transition state, or equality only after forgetting root
   labels, is insufficient for the gluing argument.
3. The operations realizing the rooted minor are actual operations in
   the original component side.  Replacing a side by an abstract graph
   with the same state family, but which is not its rooted minor, need not
   produce a minor of `G` and is not justified by minor-criticality.

Subject to these qualifications, Theorems 3.1--5.1 are direct
consequences of minor-criticality and labelled minor well-quasi-ordering.
They do not assume planarity, a cyclic boundary order, or a two-component
cut.
