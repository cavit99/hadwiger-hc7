# A cofacial-neighbour barrier to the rooted-Jorgensen principle

## Status

This is a verified counterexample to the proposed implication

\[
\begin{split}
 &H\text{ is six-connected and every component of }H-S\text{ meets }X
       \text{ for }|S|\le 6\\
 &\hspace{35mm}\Longrightarrow
 H\text{ is apex or has an }X\text{-meeting }K_6\text{ model}.
\end{split}
\]

The example is not apex and has no such rooted model.  It is, however,
two-apex, with a unique planarizing pair whose deletion also leaves `X`
cofacial.  Thus it does not refute the corrected coherent target.

The executable certificate is
`hc7_rooted_jorgensen_apex_barrier_verify.py`.

## 1. General construction

Let `T` be a five-connected plane graph and let `z` be a vertex of degree
at least seven.  Put

\[
             R=T-z,\qquad X=N_T(z),\qquad H=K_2\vee R,
\]

and call the two universal vertices of `H` `a,b`.

Deleting `z` merges all faces incident with `z`, so all vertices of `X`
occur on one face of the inherited plane embedding of `R`.

### Proposition 1 (the robust boundary hypothesis)

The graph `H` is six-connected, and for every set `S` of at most six
vertices, every component of `H-S` meets `X`.

#### Proof

Deleting one vertex lowers connectivity by at most one, so `R` is
four-connected.  The elementary join formula gives

\[
                       \kappa(K_2\vee R)=2+\kappa(R)\ge6.
\]

Fix `S` with `|S|<=6`.  If at least one of `a,b` survives, that universal
vertex makes `H-S` connected.  Moreover `|X|>=7`, so at least one member
of `X` survives; the unique component therefore meets `X`.

Suppose both `a,b` belong to `S`, and write `S_R=S-{a,b}`.  Thus
`|S_R|<=4`.  If a component `C` of `R-S_R` missed `X`, then `z` would
have no neighbour in `C`.  Consequently `C` would also be a component
separated from the rest of `T-S_R`, contradicting five-connectivity of
`T`.  Hence every component meets `X`.  \(\square\)

### Proposition 2 (no `X`-meeting `K6`)

No `K6` model in `H` has all six branch sets meeting `X`.

#### Proof

Suppose such a model exists.  Since the planar graph `R` has no `K5`
minor, the two universal vertices must occur in two distinct model bags:
if at most one bag met `{a,b}`, the other at least five bags would give a
`K5` model wholly in `R`; if one bag contained both, the same conclusion
would follow.

The remaining four bags lie wholly in `R`.  Each meets `X`; choosing one
`X`-vertex from each gives four distinct cofacial roots.  Those four bags
would form a `K4` model rooted at the four selected vertices.

This is impossible in a plane graph when the four roots lie on one face.
Indeed, contract the four disjoint connected bags in the closed disk
bounded by that face and retain four disjoint arcs from the contracted
bags to their root occurrences on the boundary.  It would give a plane
drawing of `K4` with all four vertices on the outer face, contradicting
that `K4` is not outerplanar.  \(\square\)

## 2. A deterministic explicit instance

Start with the icosahedron.  Subdivide every edge once and, in each old
triangular face, join the three subdivision vertices to form a triangle.
This is the frequency-two icosahedral triangulation `T0`, on 42 vertices.

With the deterministic NetworkX labelling used by the verifier, flip the
edge `12-15`: its two opposite vertices are `0,20`, so delete `12-15` and
add `0-20`.  Call the resulting triangulation `T` and put `z=20`.
The certificate checks

\[
 |T|=42,\quad e(T)=120,\quad \kappa(T)=5,\quad d_T(z)=7.
\]

It also checks

\[
 \kappa(R)=4,\quad \kappa(H)=6,
\]

and finds the inherited facial order

\[
                   0,15,8,23,17,1,12
\]

for `X`.  Exact planarity checks after every one- and two-vertex deletion
show that `H` is nonapex and that its **only** planarizing pair is
`{a,b}`.

## 3. Trust boundary

The counterexample proves that robust contact with `X` does not by itself
upgrade an unrooted `K6` to an `X`-meeting `K6`, even at connectivity six
and even when `H` is nonapex.  The missing alternative is exactly the
coherent two-apex outcome: the two universal vertices are the unique
global pair.

Thus a viable rooted-model principle strong enough to lift through a new
vertex with neighbourhood `X` must conclude

\[
        X\text{-meeting }K_6\quad\textbf{or}\quad
        \exists A,\ |A|\le2:\ H-A\text{ is planar and }X-A
        \text{ is cofacial},
\]

not `X`-meeting `K6` or apex.  Plain two-apexness of `H` would not be
enough: the cofacial clause is what permits the new vertex to be inserted
in the planar drawing.
