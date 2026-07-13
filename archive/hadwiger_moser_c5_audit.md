# Audit of the pure-Moser (C_5) route

This note audits only the proposed two-exterior-component argument at a
degree-seven vertex whose neighbourhood is the pure Moser spindle.  It
finds one important gap in the proposed ``monochromatic spanning tree''
shortcut, but confirms the exact-trace and external-path setup.

## 1. The five-root graph

Use the Moser labeling

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

The pair (13) is a nonedge.  For

\[
 U=\{0,2,4,5,6\},
\]

the edges of (M[U]) are

\[
 02,04,26,45,56,
\]

and hence

\[
 \overline{M[U]}=05,52,24,46,60,
\]

which is exactly the cycle (0,5,2,4,6,0).

## 2. Applicability of the external-path lemma

Let (G) be a minor-minimal counterexample to (mathrm{HC}_7), let
(d(v)=7), and suppose (G[N(v)]\cong M).  Then (G) is
7-contraction-critical and

\[
 d(v)=7+0,\qquad \alpha(N(v))=2.
\]

Thus the Rolek--Song equality-cell lemma applies with (k=7,s=0) and
the independent set (S=\{1,3\}).  Equivalently, one can argue directly
from the six-colouring of the minor obtained by contracting
(\{v,1,3\}): vertices (1,3) have the repeated colour and the five
vertices of (U) have five distinct colours.

For every edge (xy) of the displayed (C_5), the (x)- and (y)-roots
belong to one bichromatic component.  A corresponding path has all its
internal vertices outside (N[v]).  All five paths can be selected in
this one fixed colouring.  Moreover, paths for nonincident cycle edges
are vertex-disjoint: their two pairs of colour classes are disjoint.

If (G-N[v]) has components (C_1,C_2), the interior of each such path
lies wholly in one (C_i), so assigning that path the label (i) is
legitimate.  The assignment is a choice, not an invariant: a cycle edge
may have paths through both components.

There is no stronger simultaneous-disjointness conclusion.  Paths for
incident cycle edges use one common colour class and may meet in several
vertices of that colour, not merely in their common boundary root.

## 3. What Kriesell--Mohr actually closes

If one component, say (C_1), supports **all five** cycle edges, restrict
the five-coloured graph to (U\cup C_1).  Kriesell--Mohr Theorem 5,
applied to the unicyclic graph (C_5), gives a rooted (C_5)-certificate
there.  The five edges of (M[U]=\overline{C_5}) supply the complementary
bag adjacencies, so the five bags form a rooted (K_5)-model contained
in (U\cup C_1).  Then (C_2\cup\{1,3\}) is the reserved sixth bag and
(\{v\}) is the seventh.  This part of the proposed route is correct.

By contrast, four supported cycle edges forming a spanning tree do
**not** suffice by property ((*)).  Applying Theorem 5 to that tree
gives only the four corresponding certificate adjacencies.  Together
with (M[U]=\overline{C_5}), these form

\[
 \overline{C_5}\cup (C_5-e)=K_5-e,
\]

not (K_5).  The omitted cycle edge is a genuine nonedge between the
corresponding roots.  Repairing it with a path through the other exterior
component may consume the component needed for the reserved sixth bag;
showing that both operations can be performed disjointly is precisely a
new reserved-connector lemma, not a consequence of property ((*)).

Thus the proposed ``monochromatic-tree lemma'' does not, as stated,
close the pure-Moser cell.  A correct immediate target is either full
component confinement of all five (C_5) connections or a strengthened
four-plus-one lemma that also preserves a connected sixth bag.

## 4. Exact finite label patterns

For a selected family of five paths, binary component labels on the
cyclically ordered edges

\[
 05,52,24,46,60
\]

have, up to the dihedral group of the cycle and interchange of
(C_1,C_2), four types:

1. (11111) (monochromatic, already closed);
2. (11112) (a (4+1) split);
3. (11122) (a (3+2) split with the two minority edges consecutive);
4. (11212) (a (3+2) split with the two minority edges nonconsecutive).

Consequently there are exactly three mixed binary cases.  The (4+1)
case remains open after correcting the spanning-tree error.

If the state records **support sets** rather than one selected path, each
cycle edge has state (1,2,) or (B) (both).  In a genuinely unconfined
configuration there is at least one (1)-only and at least one (2)-only
edge.  There are fourteen such support-set orbits under the same
symmetries, represented by

\[
\begin{gathered}
11112,11122,1112B,11212,1121B,1122B,112B2,\\
112BB,11B2B,1212B,121BB,12B1B,12BBB,1B2BB.
\end{gathered}
\]

Any finite proof based on binary labels must either choose paths by an
explicit extremal rule or show that its moves remain valid when an edge
has support in both components.

## 5. Kempe-switch caveat

Switching the full bichromatic component of two uniquely represented
root colours preserves the exact trace, merely permuting the two root
colours.  This observation does not by itself move a path from one
exterior component to the other.  Switches involving the repeated colour
are more delicate: the two repeated roots need not lie in the same
component with the uniquely coloured root, so such a switch need not
preserve the repeated pair.  Any proposed mixed-pattern rerouting must
specify the switched component and verify the trace after the switch.

## Conclusion

The pure-Moser normalization and the full (C_5)-confinement target are
sound and sharply finite.  The claimed spanning-tree shortcut is false:
it stops at a rooted (K_5^-)-model.  The narrowest corrected next case
is the (4+1) label pattern together with a reserved-connector condition.
