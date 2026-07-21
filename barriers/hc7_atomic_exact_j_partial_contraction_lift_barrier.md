# An unbounded lift of the first connectivity-losing contraction

**Status:** explicit barrier to connectivity-only separator lifting;
separate internal audit GREEN.

This family shows that an exact order-seven separator in the immediate
predecessor of a first bad contraction need not lift to an order-seven
separator in the original host.  The lifted interface can be arbitrarily
large even when the final quotient is the exact atomic graph

\[
                         J=K_8-\{xe,ab,cd\}.
\]

The examples contain an explicit `K_7` minor and are six-colourable.  They
are therefore not counterexamples to the full atomic theorem or to
`HC_7`; they isolate the failure of the quotient-to-host inference.

## 1. Construction

Delete the universal vertex `f` from `J` and put

\[
             B=J-f=K_7-\{xe,ab,cd\}                              \tag{1.1}
\]

on the vertex set `\{x,e,a,b,c,d,g\}`.  For an integer `r>=3`, let
`R=p_1\ldots p_r` be a path and define

\[
                              G_r=P_r\vee B.                       \tag{1.2}
\]

Thus every path vertex is adjacent to every vertex of `B`.  Let

\[
                              F=E(R).                              \tag{1.3}
\]

Contracting `F` turns the path into the universal label `f`, so

\[
                              G_r/F=J.                             \tag{1.4}
\]

## 2. Exact connectivity and inclusion-minimality

The graph `B` has vertex-connectivity five.  Its minimum degree is five,
and deleting at most four vertices leaves at least three vertices of a
complete graph with a matching deleted, which is connected.

In `P_s\vee B`, a disconnected remainder cannot retain a vertex on both
sides of the join.  Deleting the whole path and then a minimum cut of `B`
costs `s+5` vertices.  When `s>=3`, deleting all seven vertices of `B`
and then a cut vertex of the path costs eight.  For `s=2`, deleting `B`
leaves a connected edge, so the first construction is the smaller cut.
It follows directly that

\[
 \kappa(P_s\vee B)=
 \begin{cases}
  7,&s=2,\\
  8,&s>=3.
 \end{cases}                                                       \tag{2.1}
\]

Contracting an arbitrary subset `F'` of the path edges leaves a path on

\[
                              s=r-|F'|
\]

vertices.  If `F'` is a proper subset of `F`, then `s>=2`, so (2.1) shows
that `G_r/F'` is seven-connected.  The final quotient `J` is
six-connected.  Hence `F` is inclusion-minimal in the strong all-proper-
subsets sense, and the last contraction is the first connectivity-losing
one in every ordering of `F`.

In particular

\[
                              \kappa(G_r)=8,                         \tag{2.2}
\]

so the original host has no separator of order seven.

## 3. The exact predecessor cut and its unbounded host lift

Immediately before the last path-edge contraction, the quotient is
`P_2\vee B`.  Replacing the final image `f` in the six-cut

\[
                    V(J)-\{x,e\}=\{a,b,c,d,f,g\}
\]

by the two surviving path blocks gives the actual order-seven separator

\[
             \{a,b,c,d,g\}\cup V(P_2)                            \tag{3.1}
\]

between the two nonadjacent vertices `x,e`.

Expanding the two path blocks back to the original host replaces (3.1)
by

\[
                 S_r=\{a,b,c,d,g\}\cup V(R).                     \tag{3.2}
\]

In fact

\[
                         N_{G_r}(x)=N_{G_r}(e)=S_r,                \tag{3.3}
\]

so (3.2) is the exact separator naturally produced by this quotient cut.
Its order is

\[
                         |S_r|=r+5=6+|F|,                         \tag{3.4}
\]

which is unbounded.  Equation (2.2) simultaneously proves that no
different order-seven separator exists in the host.  Thus neither a
lexicographic ordering of these contractions nor all-subsets minimality
turns the immediate predecessor's seven-cut into a literal host seven-cut.

## 4. Explicit terminal `K_7` model

The family is terminal for a different reason.  Choose any path edge and
let `U,V` be the two nonempty path segments obtained by deleting it.  The
seven sets

\[
 U,\quad V,\quad \{g\},\quad \{x,a\},\quad \{e,c\},\quad
 \{b\},\quad \{d\}                                                \tag{4.1}
\]

form a `K_7`-minor model.  The sets `U,V` are connected and adjacent, and
the join makes both complete as branch sets to `B`.  The singleton `g` is
adjacent to all six octahedral vertices, while

\[
                 \{x,a\},\ \{e,c\},\ \{b\},\ \{d\}
\]

is the explicit `K_4` model in `K_{2,2,2}` used in the companion minimal-
landing theorem.

The same obstruction is visible directly in the atomic bridge language.
Take the literal `H_0` subdivision with branch `f=p_1`.  The vertex `p_2`
lies outside that subdivision and gives the `T`-path

\[
                              a-p_2-b,                              \tag{4.2}
\]

and also `c-p_2-d`.  Thus the bridge crosses an absent pair at the level
of endpoint supports, exactly the terminal condition in the
[audited `H_0` bridge theorem](../results/hc7_atomic_h0_bridge_quadrant_normal_form.md).
Its attachment set is not confined to one of the
four quadrants.  In a literal `H_0`, a quadrant contains only six branch
vertices, whereas a nontrivial bridge in a seven-connected host needs at
least seven distinct attachments.  Consequently this path-blowup family
cannot be made both quadrant-confined and seven-connected merely by
deleting cross contacts; a genuine test of that residue must use internal
vertices of a subdivided frame.

Finally, `B` is four-chromatic and `P_r` is bipartite, so join additivity
gives

\[
                              \chi(G_r)=6.                          \tag{4.3}
\]

This is another explicit reason that the family is outside the
minor-critical `HC_7` hypotheses.

## 5. The exact earlier-partial-loss residue

The [companion theorem](../results/hc7_atomic_exact_j_minimal_forest_landing.md)
closes the case in which the whole forest landing
on `J` is inclusion-minimal: it returns precisely the `K_7` branch above
or an order-seven separator.  In an arbitrary contraction programme,
however, connectivity may first fail at a proper partial contraction.

The exact general statement behind that residue is the following.  Here
`F_0` and all its subsets are edge sets.

### Lemma 5.1 (minimal partial-loss bundle boundary)

Let `G` be seven-connected, let `F_0` be a nonempty edge set of a forest
in `G`, and assume

\[
 P=G/F_0\text{ is not seven-connected},\qquad
 G/F'\text{ is seven-connected for every }F'\subsetneq F_0.       \tag{5.1}
\]

Then `P` is six-connected.  Every separator `T` of `P` of order at most
six has all of the following properties.

1. `|T|=6`.
2. `T` contains the image of every nontrivial component of `F_0`.
3. Its literal full expansion `T^+` is a separator of `G` with

   \[
                              |T^+|=6+|F_0|.                       \tag{5.2}
   \]

4. If `F_0` is a matching, every vertex of `T^+` has a neighbour in
   every component of `G-T^+`.

#### Proof

Fix an edge `h` of a nontrivial tree component of `F_0`, let `z_h` be
that component's image in `P`, and put

\[
                         H_h=G/(F_0-\{h\}).                        \tag{5.3}
\]

Minimality in (5.1) makes `H_h` seven-connected.  In `H_h`, the vertex
`z_h` is split into two adjacent vertices representing the two components
of the tree after deleting `h`.

Let `U` be a separator of `P` with \(|U|\le6\).  If `z_h notin U`, splitting
`z_h` replaces one vertex inside one component of `P-U` by a connected
edge and cannot join two components.  The same set `U` would therefore
separate `H_h`, a contradiction.  Thus `U` contains `z_h` for every
nontrivial forest component.  Replacing `z_h` in `U` by its two split
images gives a separator of `H_h` of order `|U|+1`.  Seven-connectivity
then forces \(|U|+1\ge7\), and hence `|U|=6`.

It follows that `P` has no separator of order at most five.  If `P` has
at least eight vertices, its failure of seven-connectivity supplies a cut
of order at most six, so \(\kappa(P)=6\).  If `P` has seven vertices, every
proper predecessor `H_h` has at least eight vertices; the preceding
argument still excludes every cut of `P` of order at most five.  A
noncomplete graph on seven vertices has connectivity at most five, so in
this case `P=K_7` and again \(\kappa(P)=6\).  Fewer than seven quotient
vertices are impossible because a one-edge split predecessor would still
have at most seven vertices and could not be seven-connected.

Now fix a six-separator `T`.  Every nontrivial fibre image belongs to `T`.
Replacing each such image by the vertices of its tree fibre therefore
does not change the open components: the components of `G-T^+` are in
bijection with those of `P-T`.  A tree with `m` edges has `m+1` vertices,
so expanding its image adds exactly `m` boundary vertices.  Summing over
the forest components proves (5.2) and shows that `T^+` is a host
separator.

Suppose finally that `F_0` is a matching.  The preceding no-small-cut
argument makes `P` six-connected, so every component of `P-T` is adjacent
to every ordinary vertex of `T`: its neighbourhood is a separator
contained in the six-set `T`.  For a matching edge `h=x_hy_h`, use the
seven-connected predecessor `H_h` in (5.3) and the set

\[
                  T_h=(T-\{z_h\})\cup\{x_h,y_h\}.                 \tag{5.4}
\]

This is an order-seven separator whose components correspond to those of
`P-T`.  The neighbourhood of each component is a separator contained in
`T_h`; seven-connectivity forces it to equal `T_h`.  Hence both literal
endpoints `x_h,y_h` meet every lifted component.  Repeating this for every
matching edge, together with the ordinary-vertex conclusion, proves item
4.  \(\square\)

Thus splitting one edge back always gives an exact order-seven boundary
in its immediate predecessor, but expanding all earlier fibres gives only
the bundle boundary (5.2).  Its size is not bounded independently of
`|F_0|`, as Sections 1--3 demonstrate sharply.

If `F_0` is a matching of at most three edges, (5.2) has order at most
nine and is pointwise full to every lifted component.  The matching size

\[
                       \beta=|F_0|,
             \qquad |T^+|-7=\beta-1                              \tag{5.5}
\]

is an honest bounded-interface parameter.  It is not yet a proved
recursive rank: no theorem shows that the next ownership-preserving
atomic instance has smaller `\beta`.

The unresolved case is therefore exact.  The first bad quotient `P` is a
partial expansion rather than `J`; its six-cut need not project to one of
the three antipodal cuts of `J`, and fibres hit by the cut may contain
arbitrarily many route vertices.  Closing that case requires the remaining
contraction map together with the `H_0` bridge/quadrant structure,
`K_7`-minor exclusion, or the proper-minor colouring response.  The bare
first-loss argument supplies none of those ownership conclusions.

## 6. Trust boundary

The construction proves an unbounded **lifting barrier**, not a
full-hypothesis counterexample.  It has an explicit `K_7` minor, is
six-colourable, and violates quadrant confinement through (4.2).  It does
not refute the exact minimal-forest landing theorem, the atomic bridge
theorem, or `HC_7`.  It proves that any successful partial-contraction
argument must use those additional hypotheses rather than connectivity
and contraction minimality alone.
