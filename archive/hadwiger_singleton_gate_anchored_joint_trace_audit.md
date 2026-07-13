# Audit of the root-anchored joint \(56\)-trace

## Verdict

**GREEN for Lemma 2.1, Theorem 3.1, Lemmas 4.1--4.2, and the protected-peel
certificate.  YELLOW as a closure route:** the aligned Kempe component
does not yet supply the protected carrier partition.

## 1. The star contraction really expands

In \(G-56\), the three leaves \(h,5,6\) are pairwise nonadjacent.  The
set \(\{v,h,5,6\}\) is connected through \(v\), so contracting it after
deleting \(56\) is a legitimate proper-minor operation.

If the contraction vertex receives colour \(\alpha\), assigning
\(\alpha\) to \(h,5,6\) after deleting \(v\) is proper.  Every outside
vertex adjacent to one of those leaves was adjacent to the contraction
vertex and hence avoids \(\alpha\).  The only possible leaf-leaf edge was
\(56\), and it was deleted.

The neighbourhood of \(v\) then uses at most five colours: \(h,5,6\)
use one and \(1,2,3,4\) use at most four.  If a selected exterior root
\(s\sim h\) has colour \(\sigma\) absent from \(1,2,3,4\), then
\(\sigma\ne\alpha\), so it is absent from all of \(N(v)\).  Since
\(s\notin N[v]\), assigning \(\sigma\) to \(v\) creates no hidden
\(vs\)-conflict.

## 2. Literal attachment of the selected root

For a left root, \(\sigma\) differs from the colours on \(h,1,2\).
Thus, if it occurs on the four uncontracted boundary vertices, it occurs
at \(3\) or \(4\), and

\[
                            s-h-(3\text{ or }4)-5
\]

is bichromatic.  If it is absent, choosing \(v\) in colour \(\sigma\)
gives the bichromatic tree with centre \(v\) on \(h,5,6\).  The right-root
case is symmetric through \(1\) or \(2\) and the endpoint \(6\).

In the resulting colouring of \(G-56\), \(5,6\) must lie in the same
\(\alpha\sigma\)-component.  Otherwise swapping the component containing
\(5\) makes the ends of \(56\) different and restores \(56\), giving a
six-colouring of \(G\).  This is the only step using non-six-colourability,
and it is exactly the step unavailable in \(K_2\vee I\).

Because \(5,6\) have one colour, the colouring descends to \(G/56\), so
the side-labelled split-cycle theorem is applicable without an extra
assumption.

## 3. Singleton-state bookkeeping

The five bags

\[
                         \{h\},\{r\},C,D_e,D_v
\]

form a rooted \(K_5^-\) after deleting \(1,2\): only \(D_eD_v\) is
missing.  The roots \(h,r,6,e,v\) are all adjacent to both deleted
vertices.  Thus a rooted \(K_5\) upgrade really would give \(K_7\).

Lemma 4.1 is immediate but useful: \(J=G-\{1,2\}\) is five-connected,
and if it were planar the Four Colour Theorem plus two fresh colours for
the adjacent vertices \(1,2\) would six-colour \(G\).  Thus the use of
Kelmans--Seymour is legitimate, and the static \(K_2\vee I\) obstruction
is excluded because its corresponding core is planar.

For Lemma 4.2, the required \(rD_v\)-edge cannot end at \(v\), because
\(r\notin N[v]\).  A path inside the connected bag \(D_v\) from \(v\)
to an \(r\)-portal must start through a neighbour of \(v\).  The only
available neighbours not already in the other displayed bags are \(3,4\),
so at least one lies in \(D_v\).

For the protected peel, \(D_e\cup X\) is connected through \(XD_e\),
meets \(D_v\) through \(5v\) (or \(6v\)), and meets \(Y\) because a
connected graph split into two nonempty connected vertex sets has an edge
between them.  Condition (5.2) preserves every carrier contact.  This
accounts for all pairs of the seven displayed bags.

## 4. The exact non-implication

Theorem 3.1 asserts that the selected root lies in the same bichromatic
**component** as the critical edge.  It does not assert that a chosen
\(5\)-\(6\) path contains the root, avoids the other deficient bag, or
has a carrier trace whose deletion leaves all protected contacts in one
connected remainder.  None of those conclusions follows from Kempe
connectedness alone.

Accordingly, it would be invalid to replace the remaining step by

\[
 \text{root-aligned fan member}\quad\Longrightarrow\quad
 \text{protected peel}.
\]

The missing input remains a label-preserving path/bridge exchange or a
one-step deletion/contraction argument at the common blocking portal.
