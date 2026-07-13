# Seven-edge packet exchange: the unavoidable prism outcome

## 1. Audited starting point

The seven-edge atlas and packet funnel reproduce exactly:

* 31 nonsplit quotient-negative boundary types;
* 18 direct cyclic-hull closures;
* three additional types sent to a nested exact seven-cut by the
  nonbipartite compatibility graph;
* seven fully positive matching-packet triangles;
* two centre-locked matching-packet triangles; and
* one rank-two theta packet core.

The command

\[
 \texttt{.venv/bin/python equality\_gate\_seven\_edge\_packet\_atlas.py}
\]

reruns every branch-set certificate and returns the asserted
\(7+2+1\) residue. This is a sound finite funnel, not a closure.

## 2. A uniform torso-connectivity lemma

The following observation is label-free and may be useful for importing
rooted linkage theorems.

### Lemma 2.1 (clique-completed shore torso)

Let \(G\) be \(k\)-connected, let \(S\) be a \(k\)-vertex cut, and let
\(D\) be a component of \(G-S\). Form

\[
 T_D=G[D\cup S]+\binom{S}{2};
\]

that is, add every missing edge inside \(S\). Then \(T_D\) is
\(k\)-connected.

### Proof

Let \(X\subseteq V(T_D)\) have order below \(k\). The nonempty set
\(S-X\) is a clique and therefore lies in one component of \(T_D-X\).
Any other component \(C\) is contained in \(D-X\). Since \(D\) is a
component of \(G-S\),

\[
                         N_G(C)\subseteq X.
\]

The graph \(G-X\) still contains a vertex of \(S-X\) and a component of
\(G-S\) other than \(D\), so \(X\) would disconnect \(G\), contrary to
\(k\)-connectivity. Hence \(T_D-X\) is connected. \(\square\)

For the present programme, every shore therefore has a seven-connected
clique-completed torso. The difficulty is label preservation: a rooted
linkage theorem applied after completing \(S\) may use a boundary edge
which is missing in the original graph. Any successful use must return
either routes avoiding those artificial edges or an operation state
which repairs them.

## 3. Sharp counterarchitecture to the naive triangle theorem

A packet triangle being pairwise linkable does **not** imply a triple
linkage or a two-cut.

### Proposition 3.1 (triangular-prism packet)

There is a three-connected planar shore with six singleton portal
classes and three disjoint demands such that every two-demand subset is
linkable, but the three demands are not simultaneously linkable.

### Construction

Take the triangular prism with triangles

\[
                  0\,2\,3\,0,\qquad1\,4\,5\,1
\]

and matching edges \(01,25,34\). Use the demands

\[
                         02,\qquad13,\qquad45.       \tag{3.1}
\]

Every pair of demands has disjoint path carriers. Explicitly, use

\[
 \{02,\,1\!-\!4\!-\!3\},\qquad
 \{02,\,45\},\qquad
 \{1\!-\!0\!-\!3,\,45\}.                   \tag{3.2}
\]

for the demand pairs \(\{02,13\}\), \(\{02,45\}\), and
\(\{13,45\}\), respectively.

There is no simultaneous triple. The six singleton portal roots exhaust
the six prism vertices. Three disjoint carriers would therefore give
each demand exactly its two roots, but \(13\) is not an edge.

The verifier packet_triangle_prism_counterarchitecture_verify.py
enumerates all simple path carriers, verifies the three pairwise
linkages, proves absence of a triple, and checks that the core has
vertex connectivity three.

Thus the proposed implication

\[
 \text{pairwise packet triangle}
 \Longrightarrow
 \text{triple linkage or a two-separation}
\]

is false. The coherent planar/prism branch is mandatory.

## 4. Correct uniform target

The smallest plausible linkage theorem is therefore a
**packet prism-or-adhesion theorem**, not a pure augmentation lemma:

> Let three disjoint portal demands be pairwise linkable in a connected
> shore but not simultaneously linkable. Then either
>
> 1. a separation of order at most two localizes one packet state; or
> 2. after replacing pieces attached through sets of order at most three
>    by cliques, the six portal classes occur in one coherent planar
>    prism society.

This is not proved here. Proposition 3.1 shows that both conclusions are
needed. It also identifies the correct structural tool: Seymour's
3-planar form of the Two Paths Theorem and the more elaborate
\((2,3)\)-linkage/frame machinery, rather than three independent
applications of Menger's theorem.

In the Hadwiger application, either branch has additional leverage:

* a two-separation combines with the exact seven-cut descent and
  operation-state gluing; and
* a coherent prism has bounded portal order, so seven-connectivity and
  the full boundary rows can either eliminate its inserted pieces or
  turn the prism into the target minor.

The attempted six-defect \(C_6\) proof exposes precisely this
principle, but its SPQR face-synchronization step is false as written.
The rank-two/rank-two counterexample in
`c6_rank_four_leaf_counterexample.py` shows that simultaneous web
states, rather than one reflected web, are required there as well.

## 5. Theta packet

The rank-two theta residue cannot be reduced to a matching triangle by
choosing three disjoint demands: its missing graph has matching number
two. Its packet graph itself is a theta, so the corresponding uniform
object should be a two-cycle packet society. The natural analogue of
Section 4 is:

> an edge-covered theta packet either has two cycle linkages which
> exchange through a common carrier, or it admits one coherent
> 3-planar theta embedding, or a packet-bearing lobe lies behind an
> adhesion of order at most two.

Again this is a target, not a proved theorem. The current atlas supplies
individual owners only; it does not synchronize their paths.

## 6. Exact progress and remaining gap

The new rigorous information is:

1. the exact-seven full-adhesion threshold is six defects: all layers
   through five are closed, while the sole six-defect
   \(C_6\dot\cup K_1\) SPQR residue remains open;
2. clique-completing the boundary makes each individual shore torso
   seven-connected; and
3. a three-connected triangular prism is a sharp counterarchitecture to
   every packet theorem lacking a coherent planar outcome.

The immediate priority is to repair the simultaneous-web SPQR exchange
at six defects. Conditional on that repair, closing the seven-edge layer
requires combining the packet prism-or-adhesion structure with
proper-minor state transitions. Further label enumeration alone cannot
remove Proposition 3.1.
