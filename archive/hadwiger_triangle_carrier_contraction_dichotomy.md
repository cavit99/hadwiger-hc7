# Triangle carriers: what contraction really gives

This note isolates the valid part of the proposed contraction route from
two connected (T)-carriers.  It also records the exact point at which a
multi-vertex carrier ceases to yield an ordinary seven-cut.

## 1. A single edge gives exactly the desired adhesion

### Lemma 1.1 (contractible edge or exact triangle seven-cut)

Let (G) be seven-connected, let (T) be a triangle, and put
(J=G-T).  Thus (J) is four-connected.  For every edge (uv\in E(J)),
one of the following holds:

1. (J/uv) is four-connected; or
2. there are vertices (r,s\in V(J)-\{u,v\}) such that
   ({u,v,r,s}) is a vertex cut of (J).  Consequently
   (T\cup\{u,v,r,s}) is an exact seven-cut of (G).

#### Proof

Suppose (J/uv) is not four-connected and let (w) be the contracted
vertex.  It has a separator (S) of order at most three.  The vertex (w)
must belong to (S), since otherwise the same set separates (J).  Put
(R=S-\{w\}).  Then

\[
   R\cup\{u,v\}
\]

separates (J).  Four-connectivity gives
(|R|+2\ge4).  Since (|S|\le3), we have (|R|\le2), so equality holds:
(|R|=2).  This proves (2).  Adding the three vertices of (T) gives a
seven-vertex separator of (G); seven-connectivity makes its order exact.
\(\square\)

Thus, in a branch of the proof in which proper exact seven-adhesions have
already been eliminated, every *first* edge contraction inside a connected
(T)-carrier preserves four-connectivity of (J).

## 2. The exact connected-carrier quotient

Let (D,E\subseteq V(J)) be disjoint connected sets, and let (d,e) be
their images after contraction.  Write

\[
   Q=J/D/E.
\]

### Lemma 2.1 (quotient or carrier adhesion)

Either (Q) is four-connected, or (Q) has a separator (S) of order at
most three satisfying

\[
   S\cap\{d,e\}\ne\varnothing.                 \tag{2.1}
\]

More precisely, if (Q-S) has a union of components (A') and
(X=S-\{d,e\}), then in (J-X) the inverse image of (A') is separated
from its complement after deleting precisely those of the carriers whose
contracted vertices lie in (S).

#### Proof

Take a separator (S) of (Q) of order at most three.  If it avoided
both (d,e), its inverse image would be the same set (S), and it would
separate the four-connected graph (J).  This proves (2.1).  The final
statement is just the definition of contraction: outside (D\cup E), no
edge or incidence is changed, and a path crossing a contracted carrier in
(Q) lifts to a path through that connected carrier in (J).  \(\square\)

The second outcome is the exact **two-carrier adhesion**.  Unlike Lemma
1.1, its adhesion need not have bounded cardinality after lifting: a
contracted vertex in (S) represents the whole corresponding carrier.

## 3. The rooted-(K_4) endpoint when the quotient stays connected

Assume now that (a,c\in V(J)-(D\cup E)), and that each of
({a},{c},D,E) is adjacent in (G) to all three vertices of (T)
(for (D,E), adjacency is collective).  If (Q) is four-connected,
apply the Fabila-Monroy--Wood theorem to the four roots (a,c,d,e).

* A rooted (K_4)-model lifts through the contractions to four branch
  sets in (J), each adjacent to all of (T).  Together with the three
  singleton vertices of (T), it is a (K_7)-model in (G).
* Otherwise (Q) is planar and (a,c,d,e) occur on a common face.

This is a rigorous rooted-minor-or-planar-quotient dichotomy.  The planar
quotient alone does **not** imply that (J) is planar or four-colourable:
expanding a contracted vertex with an arbitrary portal order can destroy
planarity and can raise chromatic number.  Consequently the Strong-HC4
triangle dichotomy applies only after one proves that the two carrier
expansions preserve four-colourability (or else yield the carrier adhesion
of Lemma 2.1).

## 4. Why sequential contraction needs a state invariant

Lemma 1.1 can be iterated only in the successive quotients.  If several
vertices have already been contracted to (d), a later noncontractible
edge gives a four-cut in the current quotient containing (d).  Its lift
contains the entire accumulated carrier and may have arbitrarily large
order.  Absence of an exact seven-cut in the original graph therefore does
not justify contracting a whole carrier while preserving
four-connectivity.

The smallest sharp example already occurs in the octahedral graph
(K_{2,2,2}), which is four-connected.  Contracting an edge joining two
parts produces a graph with a three-cut (the contracted vertex and one
remaining vertex from each of those two parts); lifting gives the expected
four-cut containing both ends of the edge.  Thus even one carrier edge can
destroy four-connectivity, and the separator alternative in Lemma 1.1 is
indispensable.

The live extension problem can now be stated without ambiguity:

> **Carrier expansion lemma needed.**  In the planar-quotient outcome,
> either the portal incidences of each minimal (T)-carrier occupy one
> interval in the rotation at its contracted vertex, so both carriers can
> be expanded while retaining a four-colourable core, or a noninterval
> expansion yields an ordinary exact seven-cut or the two-carrier adhesion
> of Lemma 2.1 with a nontrivial boundary-state transition.

Once the first alternative gives a four-colourable (J), the audited
triangle/Strong-HC4 dichotomy in
`hadwiger_triangle_strong_hc4_dichotomy.md` finishes immediately.

