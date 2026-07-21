# Attachment-set comparison at a one-tree first connectivity loss

**Status:** written proof; separate internal audit GREEN.

This note combines the
[attachment-hull theorem](hc7_partial_loss_attachment_hull.md) with the
[clean-root attachment criterion](hc7_atomic_h0_clean_three_arm_closure.md)
in the case of one nontrivial contracted tree.  It identifies the
exact order-seven outcome, the exact comparison condition that supplies a
second full shore, and the remaining attachment-set obstruction.  A final
realisation theorem shows that the obstruction cannot be eliminated using
seven-connectivity and inclusion-minimality alone.

## 1. Setup

Let `G` be seven-connected, let `F_0` be a nonempty forest in `G`, and assume
that

\[
                              P=G/F_0
\]

is not seven-connected, while `G/F'` is seven-connected for every proper
edge subset `F'` of `F_0`.  Let `T` be a separator of `P` of order six.
Assume that `F_0` has exactly one nontrivial component `R`, whose image in
`P` is `z`.  Put

\[
                         O=T-\{z\}, \qquad |O|=5,
\]

and let \(\mathcal C\) be the set of components of `P-T`, regarded as literal
connected subgraphs of `G`.  For \(C\in\mathcal C\), define

\[
             A_C=\{v\in V(R):v\text{ has a neighbour in }C\}.
                                                               \tag{1.1}
\]

Write `L` for the leaf set of the nontrivial tree `R`.  The attachment-hull
theorem gives

\[
                N_G(C)=O\mathbin{\dot\cup}A_C,
                \qquad \operatorname{hull}_R(A_C)=R             \tag{1.2}
\]

for every \(C\in\mathcal C\).  In particular, every member of `O` and every
leaf of `R` is adjacent to every lifted component.

## 2. The hull condition is exactly a common leaf condition

### Lemma 2.1 (leaf-core characterisation)

Let `R` be a finite nontrivial tree, with leaf set `L`, and let
\(A\subseteq V(R)\).  Then

\[
                       \operatorname{hull}_R(A)=R
              \quad\Longleftrightarrow\quad L\subseteq A.       \tag{2.1}
\]

#### Proof

Suppose first that the minimal subtree containing `A` is all of `R`.  If a
leaf `l` were not in `A`, deleting `l` from that subtree would leave a
connected subgraph still containing `A`, contrary to minimality.  Hence
\(L\subseteq A\).

Conversely, every component of `R-h` contains a leaf of `R`, for every edge
`h` of `R`: starting in either component and walking away from `h` must end
at such a leaf.  Thus every edge lies on a path between two leaves.  Any
connected subgraph containing all leaves therefore contains every edge of
`R`, and so is all of `R`.  Hence \(L\subseteq A\) implies
\(\operatorname{hull}_R(A)=R\).  \(\square\)

Consequently the entire set-system conclusion of (1.2) is

\[
                         A_C=L\cup X_C,
                 \qquad X_C\subseteq V(R)-L.                    \tag{2.2}
\]

There is no additional interval or laminarity condition in the
attachment-hull statement itself.

## 3. Inclusion-minimal attachment sets

Choose \(C\in\mathcal C\) so that `A_C` is inclusion-minimal in the finite
family \(\{A_D:D\in\mathcal C\}\).  Put

\[
                              S_C=N_G(C)=O\cup A_C.              \tag{3.1}
\]

### Theorem 3.1 (comparison or internal antichain residue)

Exactly one of the following alternatives holds.

1. There is a component \(D\in\mathcal C-\{C\}\) such that

   \[
                              A_C\subseteq A_D.                  \tag{3.2}
   \]

   In this case `D` is adjacent to every vertex of `S_C`.

2. For every \(D\in\mathcal C-\{C\}\), the sets `A_C` and `A_D` are
   incomparable.  More precisely, there are internal vertices

   \[
        r_D\in A_C-A_D,\qquad s_D\in A_D-A_C,
        \qquad r_D,s_D\in V(R)-L.                               \tag{3.3}
   \]

   Moreover, every attachment set `A_D`, including `A_C`, induces a
   disconnected subgraph of `R`.

#### Proof

If (3.2) holds, every lifted component is adjacent to every member of `O`,
and the definition of `A_D` shows that `D` is adjacent to every member of
`A_C`.  Thus `D` is adjacent to all of `S_C`.

Suppose now that (3.2) fails for every \(D\ne C\).  Inclusion-minimality of
`A_C` rules out \(A_D\subsetneq A_C\), while equality would imply (3.2).
The failure of (3.2) also says \(A_C\nsubseteq A_D\).  Hence the two sets
are incomparable, and both differences in (3.3) are nonempty.  By Lemma
2.1, `L` is contained in both sets, so both difference witnesses are
internal vertices of `R`.

Finally, suppose some `A_D` induced a connected subgraph of `R`.  Its
minimal spanning subtree would then have vertex set `A_D`; but (1.2) says
that this subtree is `R`.  Therefore `A_D=V(R)`, which contains `A_C` and
gives (3.2), a contradiction.  Thus every `A_D` is disconnected in the
second alternative.  \(\square\)

The comparison in (3.2) is also necessary for the particular component
`D` to be `S_C`-full: since all components are full to `O`, one has

\[
        D\text{ is adjacent to every vertex of }S_C
              \quad\Longleftrightarrow\quad A_C\subseteq A_D.  \tag{3.4}
\]

If `G` is seven-chromatic and every proper minor of `G` is six-colourable
(the strong seven-contraction-critical hypothesis used here), Proposition
3.1 of the attachment-hull theorem then supplies the exact-block
six-colouring response on both closed shores in the first alternative.  No
such second response follows from the size of `A_C` in the antichain
alternative.

### Corollary 3.2 (the exact order-seven case)

The following are equivalent:

1. `|S_C|=7`;
2. `|A_C|=2`;
3. `R` is a path and `A_C=L`, where `L` consists of its two ends.

When these conditions hold, every other \(D\in\mathcal C\) satisfies
\(A_C\subseteq A_D\).  Thus `S_C` is an actual order-seven separator with
an opposite component adjacent to all of `S_C`; in the strongly
seven-contraction-critical setting just defined it has the two exact-block
responses described above.

#### Proof

Equation (3.1) and `|O|=5` give the equivalence of the first two statements.
Every nontrivial tree has at least two leaves, and Lemma 2.1 gives
\(L\subseteq A_C\).  Hence `|A_C|=2` holds exactly when `R` has two leaves
and `A_C=L`.  A finite tree has exactly two leaves exactly when it is a
path.  Since every `A_D` contains `L`, it then contains `A_C`.

There are at least two components of `P-T`.  Removing `S_C=N_G(C)` separates
`C` from any other such component, so `S_C` is the asserted separator; the
fullness and colouring conclusions follow from (3.4) and the attachment-hull
response proposition.  \(\square\)

More generally, the comparison alternative with \(|A_C|\le4\) gives a
two-sided full separator of order at most nine.  The inequality alone does
not imply the comparison alternative.

## 4. Literal clean-root support

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},
\]

and let `T_0` be a fixed subdivision of `H_0` in `G`.  For a point `v` of
`T_0`, let `sigma_{T_0}(v)` denote the one- or two-element set of branch
vertices supporting its segment, as in the clean-root attachment theorem.

Assume in addition that \(x\in O\), and let \(C\in\mathcal C\) satisfy

\[
                             V(C)\cap V(T_0)=\varnothing.         \tag{4.1}
\]

Define a bipartite graph `M_C^L` with left side `\{e,f,g\}`, right side

\[
                     L_0=L\cap (V(T_0)-\{x\}),                  \tag{4.2}
\]

and edge `hl` exactly when \(h\in\sigma_{T_0}(l)\).

### Proposition 4.1 (common leaves with distinct clean supports)

If `M_C^L` has a matching saturating `\{e,f,g\}`, then `G` contains an
explicit `K_7`-minor model.  Consequently, if `G` has no `K_7` minor, then

\[
                               \nu(M_C^L)\le2,                   \tag{4.3}
\]

and there is a nonempty \(Y\subseteq\{e,f,g\}\) satisfying

\[
                         |N_{M_C^L}(Y)|<|Y|.                    \tag{4.4}
\]

#### Proof

Every member of `O` is adjacent to `C`, so

\[
                              X=G[V(C)\cup\{x\}]
\]

is connected.  By (4.1), it meets `T_0` exactly in `x`.  Lemma 2.1 and
(1.2) say that every leaf in `L_0` is adjacent to `C`, hence belongs to the
attachment set of `X` on `T_0`.  A matching saturating `\{e,f,g\}` in
`M_C^L` is therefore a clean attachment matching for `X`.  The clean-root
attachment theorem gives the explicit `K_7`-minor model.  The remaining
claims follow by contraposition and Hall's theorem.  \(\square\)

This proposition is literal: only leaves that themselves lie on `T_0` have
endpoint support in (4.2).  A leaf outside `T_0`, or a path from a leaf to
`T_0`, does not acquire a support label by relabelling.  Thus (4.4) is the
exact clean-support residue when the common leaves do not close the atomic
frame.

## 5. Arbitrary attachment antichains occur at a first loss

The preceding antichain alternative is not an artefact of the proof.

### Theorem 5.1 (realisation of every common-leaf set system)

Let `R` be any finite nontrivial tree with leaf set `L`, and let

\[
                  A_1,\ldots,A_m\subseteq V(R),
                  \qquad m\ge2,\qquad L\subseteq A_i
                                                                  \tag{5.1}
\]

be any family of vertex sets.  There is a seven-connected graph `G` and a
forest `F_0=E(R)` such that:

1. `G/F_0` has a separator `T` of order six and is not seven-connected;
2. `G/F'` is seven-connected for every proper subset
   \(F'\subsetneq F_0\);
3. `F_0` has `R` as its unique nontrivial component; and
4. the lifted components of `(G/F_0)-T` have attachment sets exactly
   `A_1,...,A_m` in `R`.

#### Proof

Take new independent vertices `c_1,...,c_m`.  Let `H` consist of the tree
`R`, these new vertices, and precisely the additional edges

\[
                              c_i v\quad(v\in A_i).              \tag{5.2}
\]

Let `O` be a disjoint five-vertex clique and form the join

\[
                              G=K_5\vee H.                       \tag{5.3}
\]

First, `H` is two-connected.  Deleting a vertex `c_i` leaves `R` and all
remaining `c_j` attached to it.  If a vertex `r` of `R` is deleted, every
component of `R-r` contains a leaf of the original tree `R`.  Since every
`A_i` contains every leaf, any one surviving `c_i` joins all those
components, and every other `c_j` has a surviving leaf neighbour.  Thus
`H-r` is connected as well.  Hence `H` has no cut vertex.

Now delete at most six vertices from `G`.  If a vertex of `O` remains, it
is adjacent to every other surviving vertex.  If all five vertices of `O`
are deleted, at most one vertex of `H` is also deleted, and the remainder
is connected by two-connectivity.  Thus `G` is seven-connected.

Contracting every edge of `R` replaces it by one vertex `z` and gives

\[
                         G/F_0=K_5\vee K_{1,m}.                  \tag{5.4}
\]

This graph is six-connected but not seven-connected: deleting
\(T=O\cup\{z\}\) leaves the `m` isolated vertices `c_i`, whereas deleting
at most five vertices leaves either a vertex of `O` or the entire star.
The components outside `T` are the singletons `\{c_i\}`, and (5.2) gives
their literal attachment sets `A_i`.

It remains to verify inclusion-minimality.  Let \(F'\subsetneq E(R)\) and
let `R'=R/F'`.  At least one edge of `R` remains uncontracted, so `R'` is a
nontrivial tree.  For each `i`, let `A_i'` be the image of `A_i` in `R'`.
Every edge of `R'` is the image of an uncontracted edge of `R`.  By Lemma
2.1, `A_i` meets both sides of that original edge; therefore `A_i'` meets
both sides of its image.  Hence

\[
                           \operatorname{hull}_{R'}(A_i')=R'.    \tag{5.5}
\]

Applying the same deletion argument as above to the graph `H'` formed
from `R'` and the vertices `c_i` shows that `H'` is two-connected.  Since

\[
                              G/F'=K_5\vee H',                   \tag{5.6}
\]

the join argument shows that `G/F'` is seven-connected.  This holds for
every proper `F'`, proving all four assertions.  \(\square\)

For example, take `R` to be a path and choose the sets
\(A_i=L\cup X_i\), where the `X_i` form an arbitrarily large Sperner family
of subsets of the internal vertices.  The resulting first-loss instance
has an arbitrarily large attachment antichain.  Thus neither cardinality,
tree convexity arguments applied only to the hulls, nor inclusion-minimality
of `F_0` can force a comparison.

The construction deliberately does not refute a `K_7`-minor-free theorem.
Indeed, the five vertices of `O` together with the ends of any edge of `R`
induce a literal `K_7` subgraph in `G`.  Its role is sharper: it proves that
the exclusion of a `K_7` minor and its label-preserving interaction with the
fixed atomic subdivision must be used essentially to eliminate the
antichain alternative.

## 6. Exact remaining alternatives

For a one-tree first loss, the currently proved alternatives are therefore:

1. a literal clean-support matching on three common leaves, which closes to
   an explicit `K_7`-minor model under the hypotheses of Proposition 4.1;
2. an attachment-set comparison, which gives an opposite full component
   and, in the strongly contraction-critical setting, exact-block responses
   on both shores;
3. the order-seven specialisation `A_C=L` with two leaves, where the
   comparison is automatic; or
4. a Hall-deficient clean-support pattern together with an antichain of
   disconnected attachment sets, each pair having private internal
   vertices in both directions.

The fourth alternative is not a same-form reduction and does not provide a
bounded separator.  The realisation theorem proves that connectivity and
first-loss minimality alone cannot improve it.  Any closure must use an
additional `K_7`-free atomic ownership argument, a contraction-critical
colouring incompatibility among the private internal vertices, or a new
well-founded host reduction.
