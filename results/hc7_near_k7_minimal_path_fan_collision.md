# Fan collision at a minimum deficient branch set of a near-`K_7` model

**Status:** written proof; separate internal audit — **GREEN**.

This note proves a label-preserving consequence of ordinary fan theory for
one globally minimum branch set of a `K_7`-minus-one-edge minor model.  It
does not prove `HC_7`.  In particular, the minimization below ranges over
near-`K_7` models, not over the more restrictive valid component-contact
configurations in the active defect-one programme.

## 1. Oriented near-clique models

An **oriented `K_7^-` model** in a graph `G` is a tuple

\[
                         (B_1,B_2,B_3,B_4,B_5,L,R)          \tag{1.1}
\]

of pairwise disjoint nonempty connected vertex sets such that

1. the five sets `B_i` are pairwise adjacent;
2. each of `L` and `R` is adjacent to every `B_i`.

The order distinguishes the two branch sets corresponding to the ends of
the missing edge.  If `G` has no `K_7` minor, then `L` and `R` are
anticomplete: one edge between them would make the seven sets in (1.1) a
`K_7`-minor model.

Assume that `G` is seven-connected, has no `K_7` minor, and contains an
oriented `K_7^-` model.  Among all such models, including both orientations
of their deficient pair, choose (1.1) so that

\[
                              |L|                             \tag{1.2}
\]

is minimum.  For `x in L`, put

\[
 P_L(x)=\{i\in\{1,\ldots,5\}:N_G(B_i)\cap L=\{x\}\}.       \tag{1.3}
\]

Thus `P_L(x)` consists of the named branch sets for which `x` is the
unique contact vertex in `L`.

### Proposition 1.1 (path normal form)

Either `L` is a singleton, or `G[L]` is an induced path.  In the latter
case, if `s,t` are its endpoints, then

\[
                 |P_L(s)|\ge2,\qquad |P_L(t)|\ge2,          \tag{1.4}
\]

and the two private-label sets are disjoint.  After interchanging `s,t`
if necessary, exactly one of the following holds:

\[
\begin{array}{c|c|c}
\text{case}&|P_L(s)|&|P_L(t)|\\ \hline
2+2&2&2\\
2+3&2&3.
\end{array}                                                \tag{1.5}
\]

In the `2+2` case there is one index

\[
 e\in\{1,\ldots,5\}-\bigl(P_L(s)\cup P_L(t)\bigr).        \tag{1.6}
\]

In the `2+3` case the two private-label sets partition the five indices.

#### Proof

Suppose `|L|>=2` and `x` is a non-cutvertex of `G[L]`.  If
`P_L(x)` is empty, replacing `L` by `L-{x}` preserves all five contacts.
If `P_L(x)={i}`, replace

\[
                  (B_i,L)\quad\text{by}\quad
                  (B_i\cup\{x\},L-\{x\}).                 \tag{1.7}
\]

The enlarged `B_i` is connected, and the edge from `x` to `L-{x}` makes
the two replacement sets adjacent.  Every other `B_j` retains a contact
with `L-{x}`.  The old adjacencies among the `B_i` and from `R` to the
`B_i` persist.  Finally, `L-{x}` remains anticomplete to `R`.  Thus either
operation gives an oriented `K_7^-` model with a smaller distinguished
branch set, contrary to (1.2).

Consequently every non-cutvertex `x` of `G[L]` satisfies

\[
                              |P_L(x)|\ge2.                 \tag{1.8}
\]

The sets `P_L(x)` belonging to distinct vertices are disjoint.  A
connected graph with at least two vertices has at least two
non-cutvertices.  On the other hand, (1.8), disjointness of the sets
`P_L(x)`, and the fact that there are only five labels show that there are
at most two.  Hence there are exactly two.  A connected graph with exactly
two non-cutvertices is a path.  Indeed, if some vertex has degree at least
three, the three-edge star at that vertex extends to a spanning tree with
at least three leaves, and every leaf of a spanning tree is a
non-cutvertex of the ambient graph.  If the maximum degree is at most two,
the connected graph is a path or a cycle; a cycle has no cutvertices.
This proves the path claim and (1.4).  The two disjoint private-label sets
lie in a five-element set, which gives precisely (1.5) and (1.6).
\(\square\)

## 2. Clean paths and explicit branch-set replacements

Assume from now on that `L` is a path with endpoints `s,t`.  A path from a
vertex of `L` to one of the other six model branch sets is **clean** if,
apart from its first vertex in `L` and its last vertex in the target branch
set, it avoids all seven branch sets in (1.1).

### Lemma 2.1 (clean-path exchange)

The following alternatives hold.

1. A clean path from `L` to `R` gives an explicit `K_7`-minor model.
2. If `|P_L(s)|=2`, `i in P_L(s)`, and a clean path joins a vertex of
   `L-{s}` to `B_i`, then there is an oriented `K_7^-` model whose
   distinguished branch set is `L-{s}`.
3. More generally, if `I` is a proper subset of `P_L(s)` of order
   `|P_L(s)|-1` and there are paths from `L-{s}` to the distinct sets
   `B_i`, `i in I`, which are pairwise disjoint outside `L` and clean,
   then there is an oriented `K_7^-` model whose distinguished branch set
   is `L-{s}`.

The analogous statements hold at `t`.

#### Proof

For item 1, adjoin to `L` the clean path without its last vertex in `R`.
This connected enlargement of `L` is adjacent to `R`, is disjoint from the
other six branch sets, and retains all five old contacts.  Together with
`R,B_1,...,B_5` it is a `K_7`-minor model.

For item 3, write `j` for the unique index in `P_L(s)-I`.  For every
`i in I`, enlarge `B_i` by the corresponding clean path without its first
vertex in `L`.  The hypotheses make these enlargements connected and
pairwise disjoint.  Enlarge `B_j` by `s`, and replace `L` by `L-{s}`.
The set `B_j union {s}` is connected because `j in P_L(s)`, and it is
adjacent to `L-{s}` through the first edge of the old path `G[L]`.  The
clean paths restore the contacts with the sets `B_i`, `i in I`.  Every
index outside `P_L(s)` already has a contact vertex in `L-{s}`.  All old
adjacencies among the five named branch sets and from `R` to them persist,
and `L-{s}` remains anticomplete to `R`.  This is the required model.

Item 2 is the special case `|P_L(s)|=2`; that is the only use of item 2
below.  The proof at `t` is symmetric.  \(\square\)

By the global minimality in (1.2), none of the replacements in items 2 or
3 can occur.

## 3. Five-fan collision

Assume

\[
                              |L|\ge3,                       \tag{3.1}
\]

and put `L^circ=L-{s,t}`.  Fix `x in L^circ`.  The graph `G-{s,t}` is
five-connected.  Choose five vertices, one from each of any five distinct
sets among

\[
                         B_1,\ldots,B_5,R.                   \tag{3.2}
\]

The Fan Lemma supplies five paths from `x` to those vertices which are
pairwise internally disjoint and have distinct ends.

For each fan path, start at `x`, take its last vertex in `L`, and then take
the first vertex after it which belongs to one of the six sets in (3.2).
The resulting terminal subpath is clean.  Call its final branch set the
**first clean branch set** of that fan path.  The five terminal subpaths
are pairwise disjoint outside `L`; in particular, if they have the same
first clean branch set, their first vertices in that branch set are
distinct.

### Theorem 3.1 (minimum-path fan collision)

Under (1.1)--(3.1), every five-fan just described has the following form.

1. In the `2+2` case, all five fan paths have `B_e` as their first clean
   branch set, where `e` is the unique index in (1.6).  Consequently
   `B_e` contains at least five distinct first-entry vertices.
2. In the `2+3` case, all five fan paths have one and the same first clean
   branch set `B_i`, for some `i in P_L(t)`.  Consequently that branch set
   contains at least five distinct first-entry vertices.

#### Proof

No first clean branch set is `R`, by Lemma 2.1(1).  Since
`|P_L(s)|=2`, no first clean branch set has its index in `P_L(s)`, by
Lemma 2.1(2) and the minimality of `L`.

In the `2+2` case, the same argument at `t` excludes every index in
`P_L(t)`.  The only remaining set in (3.2) is `B_e`, proving item 1.

In the `2+3` case, two distinct first clean branch sets with indices in
`P_L(t)` would be supplied by two different fan paths.  Their clean
terminal subpaths are disjoint outside `L`; Lemma 2.1(3), applied at `t`,
would replace `L` by `L-{t}`.  Thus at most one such index occurs.  The
two private-label sets partition all five indices, so every fan path first
enters that one set `B_i`.  Distinctness of the five entry vertices follows
from internal disjointness of the fan.  \(\square\)

The theorem is a collision statement, not a labelled splitting theorem.
The five paths may enter five different vertices of one large branch set
without providing two connected pieces of that branch set which retain
the required adjacencies.

## 4. The balanced case returns a genuine separation

Continue in the `2+2` case and let `e` be as in (1.6).  Let `C` be the
component of

\[
                         G-\bigl(\{s,t\}\cup V(B_e)\bigr)   \tag{4.1}
\]

which contains the nonempty path `L^circ`.

### Theorem 4.1 (balanced full-neighbourhood separation)

The component `C` is disjoint from `R` and from every `B_i` with `i!=e`.
Moreover,

\[
                         N_G(C)\subseteq\{s,t\}\cup V(B_e), \tag{4.2}
\]

both open sides of the full-neighbourhood separation are nonempty, and

\[
                         |N_G(C)|\ge7,
 \qquad |N_G(C)\cap V(B_e)|\ge5.                           \tag{4.3}

If

\[
                         |N_G(C)\cap V(B_e)|=5,             \tag{4.4}

then this is an actual separation of order exactly seven.  In particular,
(4.4) holds whenever `|B_e|=5`.

#### Proof

Suppose `C` met `R` or one of the other four named branch sets.  A path in
`C` from `L^circ` to their union, stopped at its first encountered model
branch set and shortened after its last vertex in `L`, is clean.  If it
ends in `R`, Lemma 2.1(1) gives a `K_7` minor.  If it ends in one of the
four `B_i`, its index belongs to one of the two private-label pairs, and
Lemma 2.1(2), at the appropriate endpoint of `L`, gives a smaller
distinguished branch set.  Both alternatives contradict the hypotheses.
This proves the first assertion.

Equation (4.2) follows directly from the definition of the component in
(4.1).  The first open side contains `C`; the second contains `R` and the
four sets `B_i`, `i!=e`.  Hence the full-neighbourhood separation is
actual.  Seven-connectivity gives `|N_G(C)|>=7`.

Both `s` and `t` have neighbours in `L^circ`, so they belong to `N_G(C)`.
Together with (4.2), this proves the second inequality in (4.3).  The same
five distinct boundary vertices can also be seen from Theorem 3.1 by
choosing the five fan targets in `R` and the four private-labelled branch
sets: every fan path must cross from `C` into `B_e`, and the five crossing
vertices are distinct.

If (4.4) holds, (4.2) and the membership of `s,t` show that the boundary
has exactly seven vertices.  If `|B_e|=5`, inequalities (4.2)--(4.3) force
(4.4).  \(\square\)

The theorem supplies no upper bound on the number of vertices of `B_e`
which meet `C`.  Thus ordinary fan theory returns an exact order-seven
separation only under the additional equality (4.4).

## 5. The unbalanced and atomic residues

In the `2+3` case, Theorem 3.1 gives a five-fold first-entry collision in
one branch set whose index lies in `P_L(t)`.  In particular, the following
clean two-fan is impossible: two paths from one vertex of `L^circ` to two
distinct sets `B_i,B_j` with `i,j in P_L(t)`, pairwise disjoint outside
`L`, and internally disjoint from all seven old model branch sets.  Such a
two-fan would trigger Lemma 2.1(3).

This absence does not by itself give a small separator in `G`.  Any
separator obtained after deleting or contracting the other model branch
sets need not lift with the same order: those branch sets may contain
arbitrarily many vertices and may reconnect the separated pieces.

When `|L|=2`, the set `L^circ` is empty and the five-connected fan argument
has no root.  The endpoint-private pattern is still `2+2` or `2+3`, but
this is a separate atomic edge case.  A proof there must use an operation
on the edge of `G[L]`, or a different rooted-model exchange; Theorem 3.1
does not address it.

## 6. Exact trust boundary for the active `HC_7` programme

The conclusions above use seven-connectivity and `K_7`-minor exclusion,
but not seven-chromaticity or contraction-critical proper-minor
colourings.  They therefore identify exactly what ordinary Menger--Perfect
augmentation can and cannot supply.

1. The minimization in (1.2) is over all oriented `K_7^-` models in the
   fixed graph.  Enlarging a `B_i` along a clean path preserves a
   near-`K_7` model, but it need not preserve a colour-matched path, a
   protected component label, a valid cut interval, or an inclusion-maximal
   defect-one component selection.
2. Theorem 3.1 is consequently a valid near-`K_7` normalization and may be
   used as input to the separate near-clique route, but it is not a strict
   descent among the full valid defect-one configurations.
3. In the balanced case, the unresolved host-level statement is to prove
   \(\lvert N_G(C)\cap V(B_e)\rvert=5\), or instead to produce compatible
   six-colourings of the two closed shores.  Seven-connectivity gives only
   the opposite inequality.
4. In the unbalanced case, the unresolved statement is a label-distinct
   clean two-fan, a label-preserving split of the collision branch set, or
   a literal order-seven separation.  A quotient or block-cutvertex in the
   cleaned auxiliary graph does not suffice.
5. The two-vertex path is not reduced by the fan argument.  Its edge-deletion
   or edge-contraction colour response must be coupled to the five named
   branch sets.

Thus the endpoint-private path does yield a uniform collision principle,
but not the requested exchange-or-gluing theorem.  The missing ingredient
is a label-faithful use of proper-minor colouring responses inside the
single collision branch set.
