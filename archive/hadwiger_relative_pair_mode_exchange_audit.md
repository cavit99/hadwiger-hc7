# Audit of the relative all-\(q\), all-singleton theorem

## Verdict

**GREEN, conditional on one explicitly stated external result:** the
set-terminal Two Paths/Web Theorem in Section 6 of
`hadwiger_relative_pair_mode_exchange.md`.

The extension from one singleton label to an arbitrary number
\(s\ge0\) is valid.  No inequality in the proof deteriorates with
\(s\).

## Exact proved statement

Let \(q\ge3\), \(s\ge0\), and \(k=2q+s\).  Let \(S\) be a labelled
set of order \(k\), and let \(C\) be a finite connected
\(S\)-boundaried graph such that:

1. \(|C|\ge2\);
2. \(C\) is full to \(S\): every label of \(S\) has a neighbour in
   \(C\);
3. for every nonempty proper \(X\subsetneq C\),
   \[
   |(N_C(X)-X)\mathbin{\dot\cup}N_S(X)|\ge k;
   \]
4. \(S\) is partitioned as
   \[
   S=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q
     \mathbin{\dot\cup}R,
   \qquad |B_i|=2,\quad |R|=s.
   \]

Then either:

* two distinct pair blocks have vertex-disjoint connected carriers in
  \(C\); or
* a nonempty proper \(X\subsetneq C\) has relative boundary exactly
  \(k\).

No ambient graph, far shore, edges inside \(S\), minimum-degree
assumption, or ambient \(k\)-connectivity is used.

## Inequality audit

Assume neither conclusion.  Every proper nonempty relative boundary
then has size at least \(k+1\).

1. If a vertex \(x\) carries one pair, any component of \(C-x\) must
   miss a root from each of the other \(q-1\) pairs.  Its boundary is
   at most
   \[
   1+k-(q-1)=k-q+2<k,
   \]
   since \(q\ge3\).  Hence no one-vertex carrier exists.

2. A vertex sees at most one root in each pair and at most all \(s\)
   singleton labels, so
   \[
   d_S(x)\le q+s=k-q,
   \qquad d_C(x)\ge(k+1)-(q+s)=q+1.
   \]
   Thus \(|C|\ge q+2\).

3. If an internal separator has order \(a\le q-1\), each component
   fully contacts at least \(q-a\) pair blocks.  For \(q\ge a+2\),
   two components admit distinct fully contacted blocks and give the
   two carriers.  For \(q=a+1\), failure of that choice forces every
   component to have the same single full pair block.  Each component
   then misses exactly one root from each of the other \(a\) blocks,
   misses no singleton, and uses all \(a\) separator vertices; its
   relative boundary is exactly \(k\).  Therefore the no-conclusion
   case makes \(C\) \(q\)-connected.

4. A failed two-pair demand gives a web.  Any inserted clique part has
   relative boundary at most
   \[
   3+(k-4)=k-1,
   \]
   so the web is bare.  Hence every pair of pair blocks has a common
   portal face.  Planarity and \(q\)-connectivity reduce to
   \(3\le q\le5\).

5. If the faces for \((B_i,B_j)\) and \((B_i,B_h)\) differ, their
   intersection is a vertex or edge carrying \(B_i\).  A component
   behind that carrier misses a root from every other pair and has
   boundary at most
   \[
   2+k-(q-1)=k-q+3\le k.
   \]
   This is strict when \(q>3\), and is a forbidden tight boundary when
   \(q=3\).  Thus all pair-root portal sets lie on one face.

6. After triangulating bounded faces, an interior vertex can contact
   only singleton labels.  Therefore
   \[
   d_C(x)\ge(k+1)-s=2q+1\ge7
   \]
   in the interior, while every outer vertex has degree at least
   \(q+1\ge4\).  The triangulated-disk curvature identity then has
   nonpositive left side but value \(6\), the final contradiction.

The cancellation of \(s\) in the interior-degree bound is the key
reason the theorem extends unchanged to arbitrarily many singleton
labels.

## Sole remaining dependency

The proof requires precisely the following form of Two Paths.

> **Set-terminal Two Paths/Web Theorem.**  Given a graph \(H\) and
> four nonempty (not necessarily disjoint) vertex sets
> \(P_1,P_2,P_3,P_4\), adjoin distinct independent terminals
> \(t_1,t_2,t_3,t_4\) with \(N(t_i)=P_i\), in cyclic frame order.
> If the augmented graph has no two vertex-disjoint connected supports,
> one joining \(P_1\) to \(P_3\) and one joining \(P_2\) to \(P_4\),
> then it has a crossless same-vertex edge-maximal completion consisting
> of a planar rib with \(t_1,t_2,t_3,t_4\) on its outer face, together
> with clique parts behind facial triangles; every neighbour outside
> an inserted clique part lies in its supporting triangle.

Only this web conclusion is used.  In particular, the relative theorem
does **not** assume a rooted clique theorem, arbitrary linkedness, or a
Graph Minors decomposition.  If the cited generalized Two Paths
theorem available to the final write-up is stated only for four
individual terminals, the derivation of the displayed set-terminal
version by adjoining the four artificial terminals must be included.
That derivation is the only literature/packaging point still requiring
source-level verification; the argument after the web conclusion is
self-contained.

## Scope note

This is a genuine uniform contact-or-tight-separator lemma, not a proof
of Hadwiger's Conjecture.  To use it globally one still must derive such
a \(q\)-pair boundary mode and the relative inequality from a
counterexample, or show that failure of the inequality yields a
colour-gluable adhesion.
