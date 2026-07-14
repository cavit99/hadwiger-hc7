# Independent audit: single-missing curvature exchange

**Verdict:** **GREEN.**

Audited proof:

```text
results/hc7_exact7_single_missing_curvature_exchange.md
SHA-256: f18d5ee4daa96f44edb6060e9ba92eccce03d8fe4f9df654dbc7aaea9a8ebc88
```

The mathematical proof was audited at SHA-256
`6df426685dc7b95fa5c4fe545e5007d85861040b4524931d4fc4cd56c4b8059f`.
The final file changes only line 3 from `frozen proof draft awaiting
independent audit` to `proved and independently audited`.  Replacing that
one final status line in a byte stream reproduces the original audited hash
exactly, confirming that every other byte is unchanged.  The proof file was
not edited during this audit update.

## 1. Artificial-terminal Two Paths pages

Lines 45--50 use the generalized Two Paths theorem in its audited
same-vertex edge-completion form.  For a duty pair `i,j`, the four terminals
are newly adjoined, pairwise distinct vertices.  Their complete stars encode
all literal vertices in

```text
N_C(a_i), N_C(t_i), N_C(a_j), N_C(t_j).
```

Thus shared portal vertices and even coincident portal stars cause no
terminal collision.  A crossing consists of disjoint
`alpha_i-tau_i` and `alpha_j-tau_j` paths.  Because all four artificial
terminals are endpoints and there are no terminal--terminal edges, deleting
the first and last edge of each path leaves two nonempty, vertex-disjoint
connected subgraphs of `C` which contact the prescribed literal pairs.
Nonreflection, together with the disjoint full packet `Q`, forbids exactly
such a crossing.

No literal portal SDR is assumed at this stage.  The SDR is obtained later,
after the full portal sets have been placed on one face.

## 2. Clique-cell cut and deletion of completion edges

Lines 52--64 correctly reuse the pairwise clique-cell elimination.  Let `D`
be a component of actual `C`-vertices in one clique cell and let `Delta` be
its supporting rib triangle.  In the completed web a clique-cell vertex has
no neighbour outside its clique and `Delta`.  Any actual edge from `D` to a
second actual cell vertex puts that vertex in the same component `D`.
Consequently every remaining actual `C`-neighbour of `D` lies in `Delta`.

An edge from `D` to one of the four represented literal labels appears in
the auxiliary graph as an edge to the corresponding artificial terminal.
A frame terminal is a rib vertex, not a clique-cell vertex, so such a
terminal must belong to `Delta`.  Replacing it by its represented literal
label accounts for that host exit.  The only unrepresented boundary labels
are

```text
c, a_k, t_k,
```

where `k` is the third duty.  Hence the literal separator is

\[
 N_G(D)\subseteq \mu(V(\Delta))\cup\{c,a_k,t_k\},
 \qquad |N_G(D)|\le 6.
\]

The cell component and the old far shore both survive deletion, contradicting
seven-connectivity.  This reasoning uses the **vertices** of `Delta`, not
any edge of its completed triangle.  No completion edge is asserted to lie
in the host.

The completion is same-vertex, and all artificial terminals are frame
vertices.  Once actual `C`-vertices are excluded from clique cells, no cell
vertex remains.  Deleting completion edges therefore takes a spanning
subgraph of the planar rib; it can only merge faces.  Deleting the four frame
terminals then puts every neighbour in their four complete stars on one
face of the inherited embedding of `C`.  Since `C` is three-connected, each
face boundary is a simple cycle rather than a repeated facial walk.

## 3. Synchronizing the three pages

Lines 66--71 are valid with only two witnessed duties.  Whitney uniqueness
identifies the three spherical embeddings of the labelled three-connected
plane graph `C`.  The faces `F_12` and `F_23` both contain the chosen
vertices

\[
 p_2\in N_C(a_2)\cap K,
 \qquad q_2\in N_C(t_2)\cap J.
\]

They are distinct and nonadjacent because `K,J` are different components of
`C-X`.  In a three-connected plane graph, two distinct facial cycles cannot
both contain two nonadjacent vertices.  Thus `F_12=F_23`.  The identical
argument with the duty-3 witnesses gives `F_13=F_23`.  The common face is
therefore incident with all six **complete** portal sets, including the
possibly shared or concentrated duty-1 portals.

The argument never identifies the three web completions and never treats a
completion edge as literal.  Only the invariant facial cycles of `C` are
synchronized.

## 4. Exact support and reflection hypothesis

Lines 75--94 inherit the legally attained paired state and its literal
inter-block and `c` adjacencies from the audited one-sibling funnel.  The
packet `Q` is connected, `S`-full, and disjoint from `C`.  Therefore two
disjoint duty carriers in `C`, together with `Q` funding the third duty,
give precisely the attained-state reflection contraction.  Nonreflection
correctly implies pairwise carrier failure.

The support identities supply nonadjacent witnesses for duties 2 and 3:
each `a_i` has a portal in `K`, each `t_i` has a portal in `J`, and the two
lobes are anticomplete in `C-X`.  No isolated-versus-concentrated gate case
is used.

## 5. The order-five exclusion

Lines 102--123 cover every facial size when `|C|=5`.  Then `K={k}`,
`J={j}`, and the common facial cycle contains the nonadjacent vertices
`k,j`.  It cannot be a triangle, so

\[
                         4\le |F|\le 5.
\]

If `|F|=5`, taking `F` as the outer face makes `C` a simple outerplanar
graph.  The outerplanar bound gives `|E(C)|<=7`, whereas
three-connectivity gives minimum degree at least three and hence
`|E(C)|>=8`.  This is a contradiction.

If `|F|=4`, the fifth vertex `w` is outside the common face.  Since all six
non-`c` portal sets are contained in `F`, `w` has no neighbour among those
six boundary labels.  It has at most four neighbours in the five-vertex
graph `C`, possibly the single boundary neighbour `c`, and no neighbour
outside `C union S` because `C` is a component of `G-S`.  Thus
`d_G(w)<=5`, contradicting seven-connectivity.  There is no omitted
`|F|=3` case and no facial-walk loophole.

## 6. Hall matching and endpoint coincidences

Lines 139--151 give a valid six-label Hall cut.  If a nonempty label set
`U` violates Hall, then

\[
 |N_C(U)|<|U|\le6,
\]

so `|N_C(U)|<=5`.  Because `|C|>=6`, a vertex of `C-N_C(U)` survives.
The set

\[
                         (S-U)\cup N_C(U)
\]

has order below seven.  All boundary exits except the labels in `U` are
deleted, and no surviving vertex of `U` has an edge into `C-N_C(U)` by the
definition of `N_C(U)`.  Componenthood of `C` in `G-S` excludes every other
exit, while the old far shore survives.  This contradicts
seven-connectivity.

The resulting six matched portals are pairwise distinct even when the
underlying complete portal sets overlap.  Since every complete portal set
lies on the common face, all six representatives lie on its facial cycle.
This is exactly where endpoint coincidences are eliminated.

## 7. Facial alternation and curvature

Lines 153--160 correctly convert nonreflection into pairwise alternation.
For four distinct points on a cycle, failure of alternation of the two
prescribed pairs gives two vertex-disjoint complementary cycle subpaths.
Those are literal connected carriers in `C`; together with `Q` they would
reflect the attained state.  Hence the three duties alternate pairwise, and
the unique circular duty word is, up to the stated symmetries,

\[
                            A\ B\ D\ A\ B\ D.
\]

After relabelling in this order, lines 162--167 meet every hypothesis of the
audited facial portal-incidence and curvature theorems:

* the six portal sets are nonempty and may overlap arbitrarily;
* they have six distinct representatives in the required cyclic order;
* opposite indices are exactly the three original duties;
* no two duties have vertex-disjoint facial subpaths, because the stronger
  carrier failure holds throughout `C`;
* every portal of the six labels lies on the one facial cycle;
* `C` is a three-connected plane component of `G-S`; and
* seven-connectivity supplies `delta(G)>=7`.

The circle theorem gives total incidence at most `|F|+6`, while planar
Euler curvature and the minimum-degree bound give at least `2|F|+6`.
Since a facial cycle is nonempty, these inequalities contradict one another.

Reflection then invokes only the already attained paired state and the
audited exact-state gluing operation.  No palette label, artificial
terminal, or web-completion edge is used as a literal host object.

## 8. Audit conclusion

All proof branches and dependencies check.  In particular, the frozen proof
handles shared portals, complete-star overlap, facial walks, the possible
triangle face, completion-edge deletion, representative coincidences, and
both gate-contact alternatives without an unstated SDR assumption.
