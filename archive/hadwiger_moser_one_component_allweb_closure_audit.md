# Adversarial audit: sole-exterior all-web Moser closure

## Verdict

**GREEN after the completion-edge and notation repairs now present in
hadwiger_moser_one_component_allweb_closure.md.**

The exact theorem is:

> In the degree-seven pure-Moser sole-exterior configuration, if none
> of the five pairs of disjoint missing-cycle edges has its two portal
> paths disjointly routed through the exterior component, then the
> whole graph is six-colourable.

Thus every surviving sole-exterior configuration has a crossed frame.

## 1. The five-tuple crossing equivalence

Let the missing-edge cycle on \(U\) have order

\[
u_0,u_1,u_2,u_3,u_4.
\]

The present \(C_5=G[U]\) has pentagram order

\[
u_0,u_2,u_4,u_1,u_3.
\]

For any four terminals in this present-cycle order, their alternating
pairing consists of two vertex-disjoint edges of the missing cycle.
As the omitted terminal varies, these are exactly the five pairs of
disjoint missing-cycle edges.

Attach an artificial terminal \(t_i\) to the complete portal set
\(N_C(u_i)\).  A generalized-tuple cross is therefore exactly two
vertex-disjoint portal paths for one of the five frames.  Generalized
crosses use tuple paths whose interiors contain no other terminal, so
no hidden terminal can occur internally.

## 2. Five-web and inserted cliques

If every frame is crossless, the generalized Two Paths Theorem embeds
the auxiliary graph, after edge-only completion on the same vertex set,
in a five-web with the terminals as its frame.

Every inserted-clique vertex is an original vertex of \(C\), because
the five terminals are rib/frame vertices and the completion adds no
vertices.  For a nonempty inserted clique \(X\), all represented
neighbours outside \(X\) lie among its three facial attachments.

Replace artificial attachments by their roots in \(U\), and add the
only omitted boundary roots \(a,b\).  All actual neighbours of \(X\)
then lie in at most

\[
3+2=5
\]

vertices.  There is no edge from \(v\) into \(C\), and \(v\) survives
on the far side.  This contradicts seven-connectivity.  Hence the web
has no nonempty clique insertion.

## 3. Replacement by the real boundary cycle

After obtaining the plane rib, delete every completion edge except its
five frame edges and the original auxiliary edges.  Relabel \(t_i\) by
\(u_i\).  The portal edges become exactly the original
\(U\)-to-\(C\) edges.  Because the terminal frame order was the present
cycle order, its five frame edges are exactly \(E(G[U])\).

Thus the resulting graph is precisely \(G[C\cup U]\), embedded in a
disk with \(G[U]\) as boundary.  Deleting arbitrary completion chords
before relabelling is necessary; retaining them is unnecessary and
could obscure the claim that the displayed graph is the original
induced subgraph.

## 4. The \(4+1+1\) colouring

Four-colour \(G[C\cup U]\).  Give \(a,b\) the fifth colour and \(v\)
the sixth.

* \(a,b\) are nonadjacent.
* Every edge from \(a\) or \(b\) into \(C\cup U\) joins colour five
  to one of colours one through four.
* \(v\) has no neighbour in \(C\).
* Its seven neighbours are exactly \(U\cup\{a,b\}\), using colours one
  through five.

All vertices and edges of \(G\) are covered, so this is a proper
six-colouring.

## 5. Scope

The theorem eliminates the complete simultaneous five-web family, not
the crossed-frame residue.  One crossed frame supplies two disjoint
missing-edge carriers but does not by itself package all five roots
into a rooted \(K_5\), nor does it automatically preserve an
\(a\)-to-\(b\) connector outside those bags.

The next valid target must retain the placement of the other three
portal classes and the \(a,b\) portals.  A generic assertion that one
cross forces a rooted \(K_5\) is stronger than what has been proved.

