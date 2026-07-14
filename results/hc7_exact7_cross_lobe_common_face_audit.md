# Independent audit: cross-lobe common face

Audited file: `hc7_exact7_cross_lobe_common_face.md`.

## Verdict

**GREEN.**  The common-face theorem, its exact-seven application, the
order-five exclusion, the six-label Hall matching, the alternating facial
word, and the repaired cofacial-reversal lemma are valid as stated.

The proof uses the generalized Two Paths Theorem only in its established
same-vertex form: a crossless tuple has an edge completion to a web with that
frame.  Artificial terminals encode literal boundary stars; no completion
edge is later treated as a host edge.

## 1. Four-terminal pages and the cell cut

For fixed distinct duties `i,j`, a crossing of

```text
alpha_i, alpha_j, tau_i, tau_j
```

is exactly a pair of disjoint `alpha_i-tau_i` and
`alpha_j-tau_j` paths.  All four artificial terminals are endpoints of the
two paths and there are no terminal-terminal edges.  Removing the two end
edges of each path therefore leaves two nonempty, vertex-disjoint connected
subgraphs of `C` which contact the two prescribed literal boundary pairs.
The failure-of-two-duties hypothesis consequently makes the tuple crossless.

The clique-cell elimination is sound.  Frame terminals are rib vertices in a
web, while every interior clique vertex has no neighbour outside its clique
and its supporting facial rib triangle `Delta`.  Let `D` be a component of
the actual graph on the `C`-vertices in the interior of one cell.  An actual
edge from `D` to another actual vertex in that cell would put the latter in
the same component, and every other actual `C`-neighbour lies in `Delta`.

Edges from `D` to the four represented boundary labels are encoded exactly
by the corresponding artificial-terminal stars.  If such a terminal belongs
to `Delta`, replacing it by its literal boundary label accounts for that
exit.  The only unrepresented members of the seven-boundary are

```text
c, a_k, t_k.
```

It follows literally that

\[
 N_G(D)\subseteq \mu(V(\Delta))\cup\{c,a_k,t_k\},
 \qquad |N_G(D)|\le 6.
\]

The nonempty cell component and the nonempty far side both survive deletion
of this set, contradicting seven-connectivity.  Thus no `C`-vertex is a
clique vertex.  The completion is same-vertex and all artificial terminals
are frame vertices, so no clique vertex remains at all.  The auxiliary graph
is therefore a spanning edge-subgraph of the planar rib.  Deleting completion
edges only merges faces and retains the asserted disk order.

## 2. Synchronizing the three pages

After the four artificial terminals are deleted, every literal neighbour of
those terminals is incident with the inherited outer face.  Three-connectivity
gives Whitney uniqueness for the embedding of `C`.  The two faces obtained
from duty pairs `12` and `13` both contain the nonadjacent witnesses
`p_1,q_1`.  Distinct facial cycles of a three-connected plane graph meet in
at most one edge, so these faces are equal.  The same comparison through
`p_2,q_2` identifies the `12` and `23` faces.  Hence all six complete portal
sets lie on one literal face.

In the exact-seven application, two disjoint duty carriers in `C`, together
with the disjoint full packet `Q`, fund the three old blocks.  Literal
old-block edges and the named `c-B_i` edges complete the reflection
contraction.  Nonreflection therefore supplies the abstract theorem's
failure hypothesis.  The `a_i` portals lie in `K`, the `t_i` portals lie in
`J`, and portals chosen on opposite lobes are nonadjacent.

## 3. The order-five exclusion

If `|C|=5`, then `K={k}`, `J={j}`, and the three gates are each adjacent to
both lobe vertices.  The external-neighbourhood cuts for `C-j` and `C-k`
give respectively

\[
 |A\cup N_S(X)|\ge 6,
 \qquad |B\cup N_S(X)|\ge 6.
\]

The first inequality makes at least two `U_i=N_X(t_i)` nonempty.  The funded
duty restrictions exclude `|F|=1` and `|F|>=2`; hence `F` is empty and,
because `T` is contained in `B` and `|B|>=4`, necessarily
\(B=T\cup\{c\}\).  The second inequality then makes at least two
`W_i=N_X(a_i)` nonempty.

For unequal indices, exact nonreflection forces every member of `U_i` to
equal every member of `W_j`.  The resulting unequal-index bipartite graph is
connected, except when its two index classes are the same two-set, in which
case it has two components.  Thus every nonempty `U_i` and `W_i` is supported
on at most two gate vertices.  The third gate contacts no member of
`S-{c}`.  It has at most two neighbours in `X`, the two lobe neighbours, and
possibly `c`, so its degree is at most five.  This contradicts
seven-connectivity.  Therefore `|C|>=6`.

## 4. Hall matching and the alternating word

If the six-label incidence graph failed Hall, choose nonempty `U` with
`|N_C(U)|<|U|`.  Since `|C|>=6` and `|N_C(U)|<=5`, a vertex of
`C-N_C(U)` survives.  The set

\[
 (S-U)\cup N_C(U)
\]

has order below seven, deletes every boundary exit except `U`, and by the
definition of `N_C(U)` leaves no edge from a surviving member of `U` into
the surviving part of `C`.  The old far side is untouched.  This is a valid
cut contradiction, so six pairwise distinct literal portals exist.

All six selected portals lie on the common facial cycle.  If the endpoints
of two duties did not alternate there, two complementary facial subpaths
would be disjoint carriers for those duties, forcing reflection.  Hence the
three pairs alternate pairwise.  Up to rotation, reflection, and renaming,
the unique circular word is

\[
 A\ B\ D\ A\ B\ D.
\]

## 5. Repaired cofacial reversal

Lemma 3.1 now explicitly requires `p_1,p_2,p_3` to be pairwise distinct and
`q_1,q_2,q_3` to be pairwise distinct.  Since the two triples lie in the
different lobes `K,J`, they are disjoint.  After deletion of at most two
vertices, three-connectivity leaves `C` connected and leaves a member of
each three-set.  Set-Menger therefore gives three vertex-disjoint `P-Q`
paths.

Every such path meets the three-cut `X`.  Disjointness and `|X|=3` force the
three paths to use exactly one distinct gate each.  Under the additional
single cofacial embedding hypothesis, appending only the six literal portal
edges gives three disjoint arcs with boundary order

\[
 a_1,a_2,a_3,t_1,t_2,t_3.
\]

The Jordan alternation obstruction forces the endpoint bijection to be
strictly decreasing:

\[
 a_1t_3,\qquad a_2t_2,\qquad a_3t_1.
\]

## Trust boundary

The proof establishes one common literal face and, under a separately stated
simultaneous-cofacial hypothesis, a literal reversal linkage.  It does **not**
identify the edge completions of the three four-terminal webs, produce a
simultaneous embedding of all six terminal stars, or transport the old
equality state.

In particular, the reversed carriers pair only the middle original duty
with itself.  Contracting all three carriers does not attain the old paired
partition or its transposition without an additional proper-minor or Kempe
transition.  No palette label may be identified with a block label merely
from this geometry.
