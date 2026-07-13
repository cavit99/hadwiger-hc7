# Independent audit: interface-capacity linkage

## Verdict

**GREEN**, with two expository clarifications only.  Lemma 6.1 of
`hadwiger_degree9_type2_cutvertex_closure.md` is a valid application of
the endpoint-allowed set form of Menger's theorem, and the separator it
produces is a genuine separator of the whole graph, not merely of the
induced shore graph.

## Endpoint convention

Put \(H=G[Q\cup D]\).  The set form of Menger says that if there are
fewer than \(|D|\) pairwise vertex-disjoint \(D\)-to-\(I\) paths, then
there is a set \(Z\subseteq V(H)\), allowed to meet \(D\cup I\), with
\(|Z|<|D|\), such that \(H-Z\) has no path from \(D-Z\) to \(I-Z\).
This is precisely the version used in the proof.  Thus the cases
\(I\subseteq Z\) or \(Z\cap D\ne\varnothing\) are legitimate and are
handled correctly.

## Global-cut check

Let \(A\) consist of \(P\) and all components of \(H-Z\) meeting
\(I-Z\); if \(I\subseteq Z\), let \(A=P\).  Then no edge of
\(G-(R\cup Z)\) leaves \(A\):

1. all \(P\)-to-\(S\) edges end in \(R\), and all \(P\)-to-\(Q\)
   edges end in \(I\);
2. a vertex of \(Q\subseteq C\) has no neighbour in \(S-F\) or in a
   different component of \(G-S\), because \(C\) is a component with
   exact boundary neighbourhood \(F\);
3. different components of \(H-Z\) are anticomplete; and
4. an edge from a selected component to \(D-Z\) would create an
   \((I-Z)\)-to-\((D-Z)\) path in \(H-Z\).

The side \(A\) is nonempty because it contains \(P\).  Since
\(|Z|<|D|\), some \(d\in D-Z\) remains.  No selected component can
contain \(d\), by the same Menger separation, so \(d\notin A\).  Hence
\(R\cup Z\) separates the whole graph.  Moreover \(R\cap Z=\varnothing\)
because \(R\subseteq S\), while \(Z\subseteq Q\cup D\) and
\(D=F-R\).  Therefore

\[
 |R\cup Z|=|R|+|Z|<|R|+|D|=|F|=k,
\]

contradicting \(k\)-connectivity.

With \(|D|\) disjoint paths, all \(|D|\) vertices of \(D\) are used
as distinct initial vertices.  Consequently no vertex of \(D\) can be
internal to a path, and all internal vertices lie in \(Q\), as claimed.

## Wording repairs

The source should explicitly say “the endpoint-allowed set form of
Menger's theorem.”  Corollary 6.2 should say that the paths lie in
\(G[Q\cup D]\) and have all internal vertices in \(Q\), rather than
saying simply that they are “paths in \(Q\).”  Neither change affects
the theorem.
