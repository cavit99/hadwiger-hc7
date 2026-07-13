# Audit of the order-seven cyclic-hull reduction

## Verdict

The statements and verifier in `hadwiger_full_split_cyclic_hull.md` and
`order7_cyclic_hull_matrix_verify.py` are sound.  This note records the
points at which the reduction could otherwise lose a case.

## 1. Full splits and the eight assignments

After the two crossed carriers are made adjacent, contracting them and
choosing a spanning tree through their joining edge proves the connected
full-split extension.  If the oriented crossing fixes disjoint two-sets
\(A\) and \(B\), assign \(A\) to the first side and \(B\) to the second.
Each of the other three labels is seen by at least one side because the
two contact rows cover the seven-label boundary.  Assign it to one side
which sees it and delete every other contact edge.  Thus precisely

\[
 2^{7-4}=8
\]

minimal disjoint assignments suffice.  Contact overlaps cannot create a
new negative case, because clique-minor existence is monotone under adding
edges.

The quotient has exactly the advertised edges: the two split images are
adjacent, the opposite-shore image is complete to the boundary, and it is
anticomplete to the two split images because the original shores are
different components off the adhesion.

## 2. Crossless colouring

For a cyclic hull \(C\), \(|S-C|\le3\), so

\[
 7\ge |S-C|+4.
\]

The two-shore web-gluing theorem therefore makes \(G-(S-C)\) planar when
both tuples are crossless.  Four colours on this planar graph and two new
colours on the bipartite graph \(G[S-C]\) give a proper six-colouring;
all edges between the two vertex sets join disjoint palettes.

## 3. The \(4\times3\) incidence reduction

Földes--Hammer gives an induced \(2K_2,C_4\), or \(C_5\) in the missing
graph \(Q\).

* A \(C_5\) is already a cyclic hull because its complement is another
  five-cycle and the omitted two-vertex graph is bipartite.
* On a four-core, \(J=\overline Q\) induces either a four-cycle or two
  disjoint frame edges.  If the omitted triple is not a clique in \(J\),
  it is bipartite and the core is already a cyclic hull.
* The sole remaining case is \(Q[Z]=\overline K_3\).  The twelve
  core--triple incidences are then the only undetermined edges.

Hence the two core types and all \(2^{12}\) matrices in the verifier are
an exhaustive labelled check, not a sample from the unlabelled atlas.

## 4. Completeness of the minor checker

A seven-branch minor model in a nine-vertex graph uses seven, eight, or
nine vertices.  Its branch-size multiset is respectively

\[
 1^7,\qquad 2,1^6,\qquad 3,1^6\ \text{ or }\ 2,2,1^5.
\]

`partitions_7_of_9()` lists exactly these possibilities, including every
choice of unused vertices.  The connectivity and all twenty-one
pairwise-adjacency tests are direct.  An independent replay prints

\[
\begin{array}{c|rrrr}
Q[R]&\text{matrices}&K_7\text{-positive}&\text{hull}&\text{exception}\\\hline
2K_2&4096&1214&2876&6\\
C_4 &4096&127&3969&0.
\end{array}
\]

The six exceptions are exactly the labelled realizations of
\(2K_3\dot\cup K_1\).

## 5. Exceptional closure

The complement of \(2K_3\dot\cup K_1\) is
\(K_{3,3}\vee K_1\).  The closure theorem in
`hadwiger_k331_two_piece_closure.md` applies with the same hypotheses:
seven-connectivity, two connected full shores, and no \(K_7\)-minor.
Its two-piece surgery forces four-connectivity of each shore and makes
every vertex portal row triangle-limited.  Fullness then gives three
distinct portals for each independent boundary triple.  Every prescribed
triple in a two-connected graph roots a \(K_3\)-minor, so opposite shores
supply the two rooted triangles; with the universal boundary singleton
they form \(K_7\).

Thus no exceptional matrix survives in the counterexample-derived
setting.

