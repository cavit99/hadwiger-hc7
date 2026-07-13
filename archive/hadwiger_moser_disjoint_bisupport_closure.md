# Closure from two vertex-disjoint bi-supported pentagon edges

## Paired-linkage gluing lemma

Let \(r\) be an independent boundary pair and let \(e_i,e_j\) be two
vertex-disjoint independent pairs among the other five boundary vertices.
Write \(w\) for the remaining boundary vertex.  Assume that \(w\) has a
neighbour in each of \(e_i,e_j\).  If **each** exterior component contains
vertex-disjoint paths linking the ends of \(e_i\) and the ends of \(e_j\),
with all path interiors exterior, then \(G\) is six-colourable.

The proof is exactly the contraction argument below: join the two disjoint
paths by a shortest internal connector, split at a connector edge, and
contract the resulting two adjacent connected terminal blocks together
with the star \(\{v\}\cup r\).  The three images and \(w\) form a
\(K_4\), forcing the exact matching state \(\{r,e_i,e_j\}\) on the
opposite side.  Performing the construction in both components gives the
same exact state on both sides and permits colour gluing.

This formulation is purely graph-theoretic: bichromatic support is one
way, but not the only way, to supply the two disjoint linkages.

## Bi-support corollary

Use the two-component pure-Moser setup and the exact trace with repeated
pair \(r=13\).  Let \(e_i,e_j\) be two vertex-disjoint edges of the
missing pentagon on the five uniquely coloured roots.  If both edges are
supported in both exterior components, then \(G\) is six-colourable,
contrary to the counterexample hypothesis.

### Proof

Fix one exterior component \(C_s\).  Since \(e_i,e_j\) are bi-supported,
there are bichromatic paths \(P_i,P_j\) for these pairs whose interiors
lie in \(C_s\).  The paths are vertex-disjoint: their terminal pairs use
four distinct unique colours, so even their two induced bichromatic
subgraphs are disjoint.

Both paths have nonempty interior because their terminal pairs are
nonedges.  Inside the connected graph \(C_s\), choose a shortest path
joining their interior vertex sets.  Its internal vertices avoid both
\(P_i,P_j\).  Delete one edge of this connector and assign its two
pieces to the corresponding paths.  This gives disjoint connected sets
\(H_i,H_j\), adjacent to one another, such that \(H_i\cup e_i\) and
\(H_j\cup e_j\) are connected.

Contract the three disjoint connected sets

\[
\{v\}\cup r,\qquad H_i\cup e_i,\qquad H_j\cup e_j.    \tag{1}
\]

Let \(w\) be the unique boundary root outside \(r\cup e_i\cup e_j\).
The three images in (1), together with singleton \(w\), form a \(K_4\):

* the star image sees the other three through \(v\);
* the two path images are adjacent through the selected connector edge;
* in the complement of a five-cycle, the vertex left outside two
  disjoint cycle edges has a neighbour in each edge, so \(w\) sees each
  path image.

Every six-colouring of this proper minor therefore induces, after
deleting \(v,C_s\) and expanding the boundary blocks, the **exact**
boundary state

\[
\{r,e_i,e_j\}
\]

on the opposite exterior side.  The four displayed blocks cover all
seven boundary vertices and their contracted/singleton images form a
clique, so no unrecorded boundary equality is possible.

Repeat the construction in the other exterior component.  It gives the
same exact state on the first side.  Permute colours to align the two
boundary colourings, glue across the anticomplete exterior components,
and assign to \(v\) a colour absent from \(N\).  This gives a
six-colouring of \(G\), a contradiction. \(\square\)

## Support-orbit consequence

In the order

\[
05,25,24,46,06
\]

the disjointness graph of the five missing edges is again a five-cycle.
Consequently the lemma eliminates the residual support orbits

\[
\boxed{11B2B,\quad12B1B,\quad12BBB,\quad1B2BB}.
\]

After the earlier boundary-state eliminations, the only support-orbit
types left for the \(13\)-trace are therefore

\[
\boxed{1112B,\quad1122B,\quad112B2,\quad112BB,\quad121BB}.
\]

The last two have two adjacent, rather than disjoint, bi-supported
pentagon edges; the first three have only one bi-supported edge.  The
lemma deliberately makes no claim about those cases.

There is nevertheless a useful linkage consequence for the two adjacent-
\(B\) orbits.  Index the pentagon edges by \(e_0,\ldots,e_4\) in the
displayed order.

* In \(112BB\), side 1 is the four-edge side and misses \(e_2\).
  Side 2 supplies vertex-disjoint paths for \(e_2,e_4\).  Therefore the
  paired-linkage gluing lemma closes the graph unless side 1 is a
  two-paths obstruction for the same pairing \((e_2,e_4)\).
* In \(121BB\), side 1 misses \(e_1\).  Side 2 supplies disjoint
  linkages for both pairs \((e_1,e_3)\) and \((e_1,e_4)\).  Hence a
  survivor must obstruct both prescribed linkages in side 1.

After the global cutvertex/two-cut closure, these are prescribed
two-paths obstructions inside an exterior component which is
3-connected whenever it has at least four vertices.  Ordinary
3-connectivity alone does not automatically imply two-linkedness, so a
further planar-web or minor-transition argument is still required.
