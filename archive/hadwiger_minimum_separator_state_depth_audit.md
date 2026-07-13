# Adversarial audit of minimum-separator state depth

## Verdict

The core result is valid: Lemmas 2.1 and 2.2 and Theorem 3.1 of
`hadwiger_minimum_separator_state_depth.md` survive overlapping adhesions,
and the linked-annulus operation is a proper minor under the stated strictness
intention.  I found no counterexample to the clean linkage or pumping step.

There is one correction.  Corollary 4.2 is false if "fixed boundary type"
means only a fixed *unlabelled* graph.  The sharper count (2^m) requires the
Menger-propagated bijections to preserve a fixed labelled boundary graph (or
one must count the union of all transported state universes).  The planar
(K_2\vee C_5) application has the needed extra fact when the five linkage
paths preserve cyclic order up to the dihedral group, but it must be stated
as a hypothesis of the sharpening.

## 1. Overlapping minimum cuts

Let (R=S\cap S') and (ell=k-|R|).  Deleting (R) from a
(k)-connected graph leaves an (ell)-connected graph: deleting any
further set of fewer than (ell) vertices deletes fewer than (k) vertices
from the original graph.  The two terminal sets (S-R,S'-R) are disjoint
and both have order (ell).  Set-Menger therefore gives (ell) disjoint
paths using all vertices of both sets as distinct endpoints.  Adding the
vertices of (R) as trivial paths is legitimate and cannot meet a
nontrivial path, because the latter were chosen in (G-R).

The two nesting inclusions used in the note are exact:

\[
 S-R\subseteq O'-I',\qquad S'-R\subseteq I-O.
\]

Indeed a vertex of (S-R) lies in (O\subseteq O'), and membership in
(I') would put it in (S'); the other inclusion is symmetric.  Truncate
each Menger path between its last (S)-vertex and first subsequent
(S')-vertex.  Its interior avoids both adhesions.  Leaving (I) and later
reaching (S'-R\subseteq I-O) would force another visit to (S); entering
(I'-O') would force an earlier visit to (S').  Hence every interior lies
in

\[
 (I\cap O')-(S\cup S').
\]

This remains true when the cuts overlap heavily, including
(|R|=k-1), and when (S=S') all paths are the prescribed trivial paths.

## 2. Concatenation through overlapping adhesions

For consecutive cuts put

\[
 A_i=(I_i\cap O_{i+1})-(S_i\cup S_{i+1}).
\]

The open annuli are pairwise disjoint.  For example, a vertex in both
(A_i) and (A_{i+1}) would lie in (O_{i+1}\cap I_{i+1}=S_{i+1}),
which both annuli exclude.  More generally nesting gives the same
contradiction for nonconsecutive annuli.  An old adhesion vertex cannot
occur in a later open annulus: (S_i\subseteq O_i\subseteq O_j), whereas
the later annulus is outside (O_j).

Adhesion membership is interval-convex along the chain.  If a vertex lies
in (S_i\cap S_j), then it lies in every (S_h) for (i\le h\le j),
because (O_i\subseteq O_h) and (I_j\subseteq I_h).  Thus a shared
vertex remains on one trivial labelled strand until it leaves the adhesion;
it cannot disappear and later collide with a different strand.  Consecutive
systems consequently meet only in their common adhesion, and the propagated
bijections concatenate to (k) simple disjoint labelled paths.

## 3. Pumping and properness

Between repeated states retain only

* (G[O_i]),
* (G[I_j]), and
* the chosen linkage-path edges.

All other edges between retained vertices are deliberately deleted, as are
all nonpath edges incident with path interiors.  Clean confinement ensures
that no deleted edge belongs to either retained induced side.  Contracting
the (a)-th path identifies only (s_j^a) with (s_i^a); disjointness
prevents identification of distinct labels.

After contraction the rooted inner graph (J) is exactly (G[I_j]) with
its roots transported to (S_i).  Edges of (G[S_j]) may become new edges
on (S_i), but they are part of (J), and their colouring restrictions are
already encoded in ({\cal F}_j).  Root edges belonging only to the outer
side can be allocated to (G[O_i]), not to (J).  Therefore

\[
 {\cal E}_r(J,S_i)={\cal F}_j={\cal F}_i,
\]

which is all the gluing argument needs; rooted-graph isomorphism is neither
claimed nor required.

Properness is also sound under the intended strictness condition.  If some
linkage path is nontrivial, contraction lowers the vertex count.  If all
paths are trivial, then (S_i=S_j); a genuinely strict nested pair has
annular material outside the retained sides, so at least one vertex or edge
is deleted.  For maximal clarity, "strict" should be formalized as strict
set inclusion (O_i\subsetneq O_{i+1}) or (I_{i+1}\subsetneq I_i), or
directly as the assertion that the displayed pumping operation deletes an
edge/vertex or contracts a nontrivial edge.

## 4. Exact counterexample to the boundary-specific count as written

Take (k=3,r=2) and let every adhesion induce the same unlabelled graph
(K_2\dot\cup K_1).  For a fixed labelled edge, exactly two of the three
two-block equality partitions are proper, so the text's parameter is
(m=2).  But an arbitrary propagated bijection can move the edge to any of
the three labelled pairs.  Across those transports the possible state
universes are the three different two-element subsets of the three
two-block partitions.  Even before asking which gadgets realize which
subfamilies, the proof no longer has a common two-state universe; the claimed
upper bound (2^m=4) does not follow (the union of all subsets of those
three universes already has seven members).

The valid replacement is:

> If, after transporting labels through the clean linkages, every inward
> extension family is a subset of one fixed (m)-element universe of
> equality partitions, then the depth is below (2^m).

In particular, a fixed labelled boundary graph suffices.  For the planar
(K_2\vee C_5) chain, cyclic order preservation makes every transport a
dihedral automorphism of the (C_5), so the same ten equality partitions
form a fixed universe and the (1024) bound is valid once that planar-order
claim is installed.
