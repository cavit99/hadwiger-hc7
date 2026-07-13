# Bilateral all-crossless closure in the Moser reserved connector

## Theorem

Let (G) be seven-connected. Let

\[
 U=\{u_0,u_1,u_2,u_3,u_4\}
\]

induce a 5-cycle in the circular order

\[
 \Omega=(u_0,u_2,u_4,u_1,u_3).
 \tag{1}
\]

Let (w,a,b) be three further vertices and let (D_a,D_b) be nonempty,
connected, pairwise anticomplete shores such that

\[
 N(D_a)\subseteq U\cup\{w,a\},\qquad
 N(D_b)\subseteq U\cup\{w,b\},
 \tag{2}
\]

and every vertex of (U) has a neighbour in each shore. Assume that
(ab\notin E(G)), that a vertex (v) sees precisely
(U\cup\{a,b\}) among the displayed vertices, and that the displayed
sets cover (V(G)).

For (i\in\mathbb Z_5), let the missing-cycle edge be
(e_i=u_iu_{i+1}), with indices in the missing-cycle order
((u_0,u_1,u_2,u_3,u_4)). For either shore (D), call the frame
((e_i,e_j)) linked if the two disjoint missing-cycle edges have
vertex-disjoint portal paths through (D), allowing a length-zero path
when its two portal sets meet.

If all five frames are crossless in both (D_a) and (D_b), then (G)
is six-colourable. In particular, the two shores cannot both be
all-crossless in a minor-minimal counterexample to (HC_7).

## Proof

### 1. Five separate frame failures are one tuple failure

Fix a shore (D). Form (A_D) from (G[D]) by adjoining five
independent artificial terminals (t_i), where

\[
 N_{A_D}(t_i)=N_D(u_i).
 \tag{3}
\]

Put the terminals in the circular order

\[
 (t_0,t_2,t_4,t_1,t_3),
 \tag{4}
\]

matching (1). A cross of a circular terminal tuple consists of two
vertex-disjoint paths whose four distinct ends alternate in the tuple.

Choose any four terminals from (4). There is only one alternating
pairing of those four labels. In the order (4), its two pairs are exactly
two vertex-disjoint edges of the missing cycle

\[
 u_0u_1u_2u_3u_4u_0.
\]

For example, after omitting (u_1), the order is
((u_0,u_2,u_4,u_3)), and the alternating pairs are
(u_0u_4) and (u_2u_3). Rotating the omitted label gives the five
pairs of disjoint missing-cycle edges, once each.

Deleting the artificial terminal ends of a tuple cross produces the
corresponding two disjoint portal paths in (D), and adjoining the
terminal edges reverses this operation. Therefore

\[
 A_D\text{ has a cross with frame (4)}
 \quad\Longleftrightarrow\quad
 \text{one of the five Moser frames is linked in }D.
 \tag{5}
\]

Thus the five individual crossless hypotheses are exactly, not merely
approximately, the assertion that the single five-terminal tuple (4) is
crossless.

### 2. The tuple theorem produces one simultaneous web

Apply the same-vertex generalized Two Paths Theorem for a crossless
tuple (Humeau--Pous, Theorem 1.5) to (A_D). It gives an edge-only
completion on the same vertex set to a 5-web whose frame is (4). The web
has a planar rib with the five terminals on its outer frame; every
non-rib vertex belongs to a clique inserted behind a facial triangle and
has no web-neighbour outside that clique and the triangle.

No original shore vertex can belong to an inserted clique. Suppose that
(X\subseteq D) is the nonempty vertex set of one such clique, behind a
rib triangle (F). Replace every artificial terminal in (F) by its
corresponding label in (U), retaining the shore vertices of (F), and
call the resulting set (\widehat F). Then

\[
 |\widehat F|\le3.
\]

Every original edge from (X) to (U) is represented in (A_D) by
an edge to the corresponding artificial terminal, so all such neighbours
are accounted for by (\widehat F). By (2), the only original neighbours
not represented in (A_D) are (w,a) on the (a)-side, or (w,b) on
the (b)-side. Hence

\[
 |N_G(X)|\le |\widehat F|+2\le5.
 \tag{6}
\]

The opposite nonempty shore lies outside (X\cup N_G(X)), so (6)
contradicts seven-connectivity. Thus every original vertex and edge of
(A_D) lies in the planar rib.

Replace (t_i) by (u_i), preserving all incident portal edges, and
add the five edges of the present cycle in order (1) along the outer
frame. This gives one closed-disk embedding of the actual graph

\[
 P_D=G[D\cup U]
 \tag{7}
\]

with the same labelled cycle (G[U]) as its boundary. This is a
simultaneous pentagonal patch: no representative portal and no
independently chosen four-terminal embedding occurs in the argument.

### 3. Bilateral disk gluing

Apply (7) to (D_a) and (D_b). Reverse one disk if needed and identify
their boundary cycles label by label. The two shores are anticomplete, so
the two disk drawings on opposite sides of their common boundary give a
sphere embedding of

\[
 P=G[D_a\cup D_b\cup U].
 \tag{8}
\]

By the Four Color Theorem, (P) has a proper colouring with colours
(1,2,3,4). Give (a,b) colour (5), and give (w,v) colour (6).
The pair (a,b) is independent, (vw\notin E(G)), every shore and root
uses only the first four colours, and (2) lists all remaining possible
edges. Hence this is a proper six-colouring of (G). This proves the
theorem. \(\square\)

## Audit boundary

The implication proved here would be false if one knew only that five
unrelated four-terminal embeddings existed. What makes it valid is (5):
the five forbidden linkages are precisely all crosses of one fixed
circular five-terminal tuple. The generalized Two Paths Theorem is
applied once to that tuple. The same-vertex and edge-only clauses are
essential, because they ensure that all original shore vertices and
portal edges survive in the single rib before the bilateral gluing.

The theorem does not say that one crossed shore alone closes the reserved
connector. Its exact consequence is that every survivor has a crossed
Moser frame in at least one of the two shores.
