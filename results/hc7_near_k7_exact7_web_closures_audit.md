# Independent audit: the two sharp five-defect full-shore cores

## Verdict

**GREEN.** The two web-closure notes

* `hc7_near_k7_exact7_k322_web_closure.md`, and
* `hc7_near_k7_exact7_c5_web_closure.md`

correctly close the two five-defect boundary types left by the exact
labelled quotient classification. Their shared conclusion is:

> Let \(G\) be seven-connected, let \(S\) be a seven-cut, and suppose
> \(G-S\) has exactly two components, both full to \(S\). If
> \[
> \overline{G[S]}\in
> \{K_3\dot\cup2K_2,\ C_5\dot\cup2K_1\},
> \]
> then \(G\) contains a \(K_7\) minor or is six-colourable.

The result is unbounded in the shore orders. It is a structural
crossing-versus-planar-web theorem, not finite portal enumeration.

The cited external input is used with its exact scope. Humeau--Pous,
*On the Two Paths Theorem and the Two Disjoint Paths Problem*,
arXiv:2505.16431, Theorem 1.5, says that a graph with a crossless tuple
\(T\) has a same-vertex edge-completion to a web with frame \(T\).
Its definitions give a planar \(k\)-rib with triangular faces, with an
optional clique inserted into each facial triangle and no other
neighbours for those clique vertices. That is precisely the form used
in both proofs.

## 1. The \(K_3\dot\cup2K_2\) crossing

Label

\[
 E(\overline{G[S]})=\{01,02,12,34,56\}.
\]

In one shore \(D_j\), attach artificial terminals \(t_i\) to the portal
sets of \(i\), for \(i=1,2,3,4\), and order them

\[
                         (t_1,t_3,t_2,t_4).
\]

A crossing therefore gives disjoint connected sets \(X,Y\subseteq D_j\)
with \(X\) meeting the portal sets of \(1,2\), and \(Y\) meeting those of
\(3,4\). With \(D_k\) the opposite full shore, the seven bags

\[
 \{1\},\quad\{3\},\quad\{5\},\quad D_k,\quad
 \{0,6\},\quad X\cup\{2\},\quad Y\cup\{4\}
\]

are disjoint and connected. Their 21 adjacencies check:

* the four boundary bags
  \(\{1\},\{3\},\{5\},\{0,6\}\) are pairwise adjacent;
* the \(X\)-bag uses its \(1\)-portal and the boundary edges
  \(23,25,26\);
* the \(Y\)-bag uses its \(3\)-portal and the boundary edges
  \(41,45,40\);
* the two large bags meet through \(24\); and
* \(D_k\) sees every boundary-containing bag by fullness.

Thus a crossing in either single shore gives a labelled \(K_7\) model.

## 2. The \(K_3\dot\cup2K_2\) crossless case

If no \(K_7\) minor exists, both four-terminal tuples are crossless.
The generalized Two Paths Theorem embeds each auxiliary shore graph in
a \(4\)-web on the same vertex set, with frame
\(1-3-2-4-1\).

Suppose an inserted facial clique \(X\) is nonempty. Its neighbours in
the auxiliary graph lie in its facial triangle. Replacing any artificial
terminal on that triangle by its actual boundary vertex accounts for all
neighbours in

\[
                 D_j\cup\{1,2,3,4\}.
\]

The shores are anticomplete, and the only omitted boundary vertices are
\(0,5,6\). Hence

\[
                       |N_G(X)|\le3+3=6.
\]

This neighbourhood separates \(X\) from the nonempty opposite shore,
contradicting seven-connectivity. Therefore every original shore vertex
lies in the planar rib.

The actual boundary graph on \(1,2,3,4\) is exactly the frame cycle:
its edges are \(13,32,24,41\), with diagonals \(12,34\) absent. Replacing
the terminals and adding those frame edges embeds each closed shore in a
disk. Gluing the two disks along the common frame makes

\[
                         G-\{0,5,6\}
\]

planar. Four-colour that graph, give \(0\) a fifth colour, and give the
nonadjacent pair \(5,6\) one sixth colour. This is a proper
six-colouring of \(G\).

No planarity assumption on either original shore is made: crosslessness
and seven-connectivity force it.

## 3. The \(C_5\dot\cup2K_1\) core

Write

\[
                        G[S]=C_5\vee K_2.
\]

For each shore, add five artificial terminals in the cyclic order of the
\(C_5\). A crossing gives two disjoint connected portal sets. Since
the shore is connected, a shortest connector between the two sets can be
split at one edge, enlarging them to disjoint adjacent connected sets.
The explicit seven bags in the source then form a \(K_7\) model, with
the opposite full shore as the seventh bag.

If both tuples are crossless, the same web theorem gives two \(5\)-webs.
An inserted facial clique has at most its three facial neighbours plus
the two universal boundary vertices, so its neighbourhood has order at
most five. Seven-connectivity again removes all inserted cliques.
The two bare five-ribs glue along their common boundary cycle, proving
that deletion of the two universal vertices leaves a planar graph.
Four colours there and two fresh colours on the universal adjacent pair
six-colour \(G\).

## 4. Why a mere pair of clean chains is not enough

The same-shore qualifier in the crossing theorem is essential. Let
\(H\) be the boundary with missing graph
\(K_3\dot\cup2K_2\), together with two nonadjacent singleton helpers,
each complete to the boundary. Then

\[
                  1-h_1-2,\qquad 3-h_2-4
\]

are disjoint boundary-clean paths for the two missing \(K_2\) pairs.
Nevertheless \(H\) has no \(K_7\) minor. Its connectivity is exactly
six. Thus two paths split between the two shores do not form the
labelled crossing needed by the model.

The exact branch-set search in
`contact_order7_five_edge_verify.py` proves the absence of a \(K_7\)
minor, and
`exact7_split_clean_crossing_counterexample_verify.py` independently
checks the two paths and all vertex cuts of order below six. Its output
is:

```
two split clean paths verified: (1, 7, 2) (3, 8, 4)
exact K7 branch-set search: none
vertex connectivity: exactly 6
```

This is the sharp reason the Kempe-trace theorem cannot promote any two
clean alternating regions directly to a \(K_7\). What closes the
seven-connected case is the stronger dichotomy: one shore contains a
true crossing, or both entire shore societies are coherent planar webs.

## 5. Consequence for the exact threshold

The exact quotient audit proves that every boundary with at most four
missing edges already gives a \(K_7\) minor from two full shores, and
that the two graphs above are the only five-edge exceptions. If a third
shore exists, both exceptions have explicit static \(K_7\) models.
With exactly two shores, Sections 1--3 close them by a \(K_7\)-minor or
a six-colouring.

Therefore no non-six-colourable, seven-connected, \(K_7\)-minor-free
graph has a full exact seven-adhesion with at most five boundary defects.
This is a rigorous closure of an infinite family of exact adhesions. It
does not by itself prove \(HC_7\): later defect layers and the production
of such an adhesion from every hypothetical counterexample remain
separate tasks.
