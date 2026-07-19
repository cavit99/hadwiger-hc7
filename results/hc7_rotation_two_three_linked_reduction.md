# Two--three linkage reduction for a two-demand rotation connector

**Status:** written proof; separate internal audit GREEN in
[`hc7_rotation_two_three_linked_reduction_audit.md`](hc7_rotation_two_three_linked_reduction_audit.md).

This note isolates the first standard linkage theorem which applies exactly
to the robust three-of-four demand patterns in a two-demand rotation.  It
does not close the rotation: the theorem applies to a five-terminal
completion of the connector, and failure returns a cut of that completed
connector rather than immediately returning a colour-compatible separation
of the host graph.  The gain is nevertheless uniform and unbounded.
Whenever all four displayed choices of five distinct terminals exist, each
corresponding completed connector of order at least seven has a cut of order
at most five.  Under the additional hypothesis that the host graph is
seven-connected, each such cut either lifts to an actual order-seven
separation or admits the external bypasses stated in Lemma 3.1.

## 1. A five-terminal completion

Let `H` be a graph and let

\[
                    a_0,a_1,a_2,b_1,b_2\in V(H)
                                                               \tag{1.1}
\]

be distinct.  Write

\[
 H^+(a_0,a_1,a_2;b_1,b_2)
   =H+b_1b_2+\{a_i b_j:i\in\{0,1,2\},\ j\in\{1,2\}\}.          \tag{1.2}
\]

Thus the five nominated vertices induce, among the added edges, a complete
bipartite graph with parts of orders three and two, together with the edge
joining the two vertices in the second part.

### Theorem 1.1 (Xie's two--three linkage theorem)

If the graph in (1.2) is six-connected, then `H` has vertex-disjoint
connected subgraphs `L,R` satisfying

\[
       \{a_0,a_1,a_2\}\subseteq V(L),\qquad
       \{b_1,b_2\}\subseteq V(R).                              \tag{1.3}
\]

This is Theorem 1.2.1 of Shijie Xie,
[*6-Connected Graphs Are Two-Three Linked*](http://hdl.handle.net/1853/62273),
PhD dissertation, Georgia Institute of Technology (2019), pp. 3--4.  The
theorem is stronger than the often-quoted corollary
that every six-connected graph is two--three linked: only the completion
(1.2), rather than `H` itself, is required to be six-connected.

## 2. Application to the rotation datum

Use the notation and hypotheses of
[`hc7_near_k7_rotation_edge.md`](../results/hc7_near_k7_rotation_edge.md).
Thus the connected connector `Z` has attachment roots

\[
       \alpha\in N_Z(X),\qquad \beta\in N_Z(W),                 \tag{2.1}
\]

and portal sets `P_i=N_Z(F_i)`.  Suppose

\[
                 D=\{d_1,d_2\},\qquad E=\{e_1,e_2\}.           \tag{2.2}
\]

Assume `|D|=|E|=2`; thus `d_1!=d_2` and `e_1!=e_2`.  A label may still
occur once in each of `D` and `E`.  In the theorem below we
choose literal portal representatives and explicitly require the five
vertices used in each invocation to be distinct.  Failure of this choice
is a portal-collision case, not a linkage conclusion.

### Theorem 2.1 (four completed-connector cuts)

Assume that `G` has neither a `K_7` minor nor a `K_7^-` minor.

For `j\in\{1,2\}`, choose

\[
      p_1\in P_{d_1},\quad p_2\in P_{d_2},\quad q_j\in P_{e_j}
                                                               \tag{2.3}
\]

so that

\[
                     \alpha,p_1,p_2,\beta,q_j                 \tag{2.4}
\]

are distinct.  Then

\[
 H^D_j:=G[Z]^+(\alpha,p_1,p_2;\beta,q_j)                       \tag{2.5}
\]

is not six-connected.  If `|Z|>=7`, it has a separation of order at most
five.

Symmetrically, for `i\in\{1,2\}`, choose

\[
      q_1\in P_{e_1},\quad q_2\in P_{e_2},\quad p_i\in P_{d_i}
                                                               \tag{2.6}
\]

so that

\[
                     \beta,q_1,q_2,\alpha,p_i                 \tag{2.7}
\]

are distinct.  Then

\[
 H^E_i:=G[Z]^+(\beta,q_1,q_2;\alpha,p_i)                       \tag{2.8}
\]

is not six-connected and, if `|Z|>=7`, has a separation of order at most
five.

#### Proof

Suppose first that `H^D_j` is six-connected.  Apply Theorem 1.1 to
`H=G[Z]` and the ordered terminal sets displayed in (2.4).  It gives
vertex-disjoint connected subgraphs `L,R` of `G[Z]` such that

\[
       \{\alpha,p_1,p_2\}\subseteq V(L),\qquad
       \{\beta,q_j\}\subseteq V(R).                            \tag{2.9}
\]

The first is an `X`-rooted `D`-carrier, while the second is a
`W`-rooted `{e_j}`-carrier.  These two subgraphs cover three of the four
demand occurrences in (2.2).  The robust four-demand exclusion, Theorem 5
of the rotation note, therefore gives a `K_7^-` minor (and possibly a
`K_7` minor), contrary to the hypotheses.  Hence (2.5) is not
six-connected.

Interchanging the two orientations proves the assertion about (2.8): a
six-connected completion would give an `E`-carrier rooted at `W` disjoint
from a `{d_i}`-carrier rooted at `X`, again covering three demand
occurrences and contradicting the same theorem.  When `|Z|>=7`, a graph
which is not six-connected has a separation of order at most five by the
definition of vertex connectivity.  Connector orders at most six are a
finite small-order branch and are deliberately not converted into a
separation by this theorem.
\(\square\)

### Exact scope of the representative condition

The distinctness hypothesis is not cosmetic.  A single connector vertex
may belong to two portal sets, the two roots may coincide, a root may itself
be a required portal, and
a portal class common to `D` and `E` may have only one vertex.  These events
create literal collisions to which Theorem 2.1 does not apply.  Some
detachable common-portal and shared-attachment cases are covered by existing
results, but same-side multi-label collisions and general root--portal
coincidences require separate analysis.  Duplicating one literal vertex
into two terminals would be invalid.  Theorem 2.1 handles only the
complementary, genuinely five-terminal case.

### Lemma 2.2 (shape of a completed-connector cut)

Let `H^+=H^+(a_0,a_1,a_2;b_1,b_2)`, and let

\[
          V(H)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,
          \qquad A,B\ne\varnothing,                            \tag{2.10}
\]

be a separation of `H^+`.  Then either one of `A,B` contains no nominated
terminal, or

\[
               \{b_1,b_2\}\subseteq T                         \tag{2.11}
\]

and the surviving members of `\{a_0,a_1,a_2\}` occur on both open sides.

#### Proof

Suppose both open sides contain a nominated terminal.  The added edge
`b_1b_2` prevents surviving members of `\{b_1,b_2\}` from occurring on
different open sides.  If one of them survives outside `T`, every surviving
`a_i` is adjacent to it by an added edge, and hence every surviving
nominated terminal lies on the same open side.  The other side would then
be terminal-free, contrary to the supposition.  Thus both `b_1,b_2` lie in
`T`.  Since both open sides still contain nominated terminals, surviving
members of the remaining triple must occur on both sides. \(\square\)

For (2.5), the exceptional alternative (2.11) says that the cut contains
the literal pair `\{\beta,q_j\}` and separates members of
`\{\alpha,p_1,p_2\}`.  For (2.8), it contains `\{\alpha,p_i\}` and separates
members of `\{\beta,q_1,q_2\}`.  Thus every low-order cut returned by
Theorem 2.1 is either a terminal-free lobe or a cut containing one exact
root--portal pair.  This is substantially more rigid than an arbitrary
five-cut of `G[Z]`.

If `C` is a terminal-free component of `H^+-T`, none of the added edges
in (1.2) is incident with `C`.  Consequently

\[
                         N_{G[Z]}(C)\subseteq T.                \tag{2.12}
\]

In a seven-connected host this forces at least `7-|T|` distinct literal
neighbours of `C` outside `Z`.  Moreover `N_G(C)` is the boundary of an
actual separation: `C` is one nonempty open side, while a vertex in the
other open side of (2.10) is not adjacent to `C` in `G[Z]` and hence
survives outside `C\cup N_G(C)`.  Thus

\[
                              |N_G(C)|\ge7.                    \tag{2.13}
\]

Equality in (2.13) is an actual order-seven separation.  Otherwise this
is a positive-excess full-neighbourhood separation.  In particular, a
terminal-free lobe behind a five-cut has at least two external neighbours.
The unresolved issue is the ownership of those neighbours by the seven
named branch sets, not their existence.

Consequently a cut which does not already return such a full-neighbourhood
separation has the following exact form.  It contains the nominated pair
`\{b_1,b_2\}`, and `H^+-T` has at most three components, each containing
at least one surviving member of `\{a_0,a_1,a_2\}`; those surviving
members occur in at least two components.  In the rotation application
these are at most three connected lobes, each anchored by at least one
surviving member of the old-root/old-portal triple (or, in the reverse
orientation, of the new-root/new-portal triple).  A nominated `a_i` may
itself lie in `T`; no unanchored connector component remains.

### Proposition 2.3 (lower-demand orientations)

The same external theorem gives exact confined reductions for the
orientations in which one side has fewer than two demands.

   1. Suppose `D={d}` and `E={e_1,e_2}`, where `e_1!=e_2`.  Choose

   \[
       p\in P_d,\qquad q_1\in P_{e_1},\qquad q_2\in P_{e_2}
   \]

   so that `\beta,q_1,q_2,\alpha,p` are distinct.  If `G` has no `K_7`
   minor, then

   \[
             G[Z]^+(\beta,q_1,q_2;\alpha,p)                   \tag{2.14}
   \]

   is not six-connected.

2. Suppose `D={d}` and `E={e}`.  Choose `p\in P_d`, `q\in P_e`, and any
   `r\in Z` so that `\alpha,p,r,\beta,q` are distinct.  If `G` has no
   `K_7` minor, then

   \[
                    G[Z]^+(\alpha,p,r;\beta,q)                \tag{2.15}
   \]

   is not six-connected.

The symmetric statements hold after interchanging the old and new
orientations.  If `|Z|>=7`, every non-six-connected graph in (2.14) or
(2.15) has a cut of order at most five.

#### Proof

If (2.14) were six-connected, Theorem 1.1 would give disjoint connected
subgraphs containing `\{\beta,q_1,q_2\}` and `\{\alpha,p\}`.  They are the
two rooted carriers meeting all of `E` and all of `D`, respectively, so
Theorem 2 of the rotation note gives a `K_7` minor.

For (2.15), the same theorem gives one connected subgraph containing
`\alpha,p,r` and another containing `\beta,q`.  Forgetting the harmless
extra terminal `r`, these are again the two rooted carriers required by
Theorem 2 of the rotation note.  The symmetric assertions are identical.
\(\square\)

This proposition is the precise sense in which lower-demand cases close:
they close when the corresponding completed connector is six-connected.
The audited entrance-edge theorem does not remove the low-connectivity
alternative, because its paths live in all of `G` and may leave `Z`.

## 3. Lifting a completed-connector cut to the host

The following elementary lemma records exactly what seven-connectivity
adds to any one of the cuts returned by Theorem 2.1.

### Lemma 3.1 (order seven or external bypasses)

Let `G` be seven-connected, let `Z\subseteq V(G)`, and let `H` be a graph
on vertex set `Z` containing `G[Z]`.  Suppose

\[
               Z=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,
       \qquad A,B\ne\varnothing,\quad |T|=t\le5,               \tag{3.1}
\]

and `H` has no `A`--`B` edge.  Fix `a\in A` and `b\in B`.  Then one of
the following holds.

1. `G` has an actual separation of order seven whose boundary contains
   `T` and separates `a` from `b`.
2. There are at least `8-t` internally vertex-disjoint `a`--`b` paths in
   `G-T`.  Every one of these paths has an internal vertex outside `Z`.

#### Proof

Deleting `T` from a seven-connected graph leaves a
`(7-t)`-connected graph.  Since `H` contains `G[Z]` and has no
`A`--`B` edge, there is no `a`--`b` path in `G[Z]-T`; in particular `a`
and `b` are nonadjacent.

Let `r` be the minimum order of an `a`--`b` separator in `G-T` (with the
ends excluded).  Seven-connectivity gives

\[
                              r\ge7-t.                          \tag{3.2}
\]

If equality holds, let `R` be such a separator.  Then `T\cup R` has order
seven and deleting it leaves `a` and `b` in different nonempty components.
It is therefore the boundary of an actual order-seven separation.

If equality does not hold, `r\ge8-t`.  The vertex form of Menger's theorem
gives at least `8-t` internally vertex-disjoint `a`--`b` paths in `G-T`.
No one of them can lie in `Z`, since `G[Z]-T` has no `A`--`B` path.  Hence
each has an internal vertex outside `Z`. \(\square\)

### Corollary 3.2 (the exact residual after two--three linkage)

Assume additionally that `G` is seven-connected.  For every cut of a
completed connector in Theorem 2.1, and every choice of vertices on its two
open sides, either an actual order-seven separation is obtained or the cut
is bypassed outside `Z` by at least three internally disjoint paths when its
order is at most five (and by more when the cut is smaller).

The bypass paths are literal host paths.  Their first vertices outside `Z`
are distinct, but they may lie in the same named branch set or outside every
named branch set.  Thus Corollary 3.2 does not itself provide the two
rooted connected subgraphs in the rotation note.  A continuation would
have to allocate the external bypasses to the required distinct labels or
prove that their concentration carries the selected proper-minor boundary
partition onto an order-seven separation.  That is an open requirement,
not a dichotomy proved here.

## 4. Relation to the entrance-edge theorem

The audited entrance-edge ordered-two-path theorem applies when `G` is
seven-connected, the two nominated entrance edges are disjoint, and the six
nominated vertices are distinct.  It closes a one-continuation-per-side
problem only when the returned paths are already known to remain in the
intended exchange region, or when their first exits are separately decoded.
It cannot by itself be applied to `G[Z]`, because `G[Z]` need not be
seven-connected.

Theorem 2.1 is the correct confined analogue for the robust rotation
patterns: it asks for six-connectivity only after adding seven explicit
edges among five literal terminals, and it returns a cut of that same
completed connector when the desired connected subgraphs do not exist.
Lemma 3.1 independently supplies paths between a selected pair of vertices
on opposite sides of the cut.  It does not say that a particular path
returned by the entrance-edge theorem evades the cut: such a path may meet
`T` or may have both of its relevant vertices on one side.  No palette
colour is identified with a branch-set label in this reduction.

## Trust boundary

This note proves neither `HC_7` nor the two-demand rotation composition
target.  Specifically, it does not prove that

* a cut of one of the four completed connectors has a boundary of order
  exactly seven in `G`;
* the order-seven boundary, when obtained, has one complete equality
  partition extending to both closed shores;
* externally bypassing paths first meet distinct fixed branch sets; or
* the four low-order cuts arising from the four robust patterns are
  mutually compatible.

When all four valid five-terminal choices exist, `|Z|>=7`, and the host is
seven-connected, it replaces an unstructured failure of two connected
subgraphs by four bounded cuts, each accompanied by an order-seven return or
explicit external bypasses.  A continuation should work with their common
refinement and the selected proper-minor response, not with another generic
connectivity assertion about `G[Z]`.
