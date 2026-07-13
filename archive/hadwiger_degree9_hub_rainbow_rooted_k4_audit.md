# Independent audit: the degree-nine rainbow rooted core

## Verdict

**GREEN.**  Theorems 2.1, 3.1, and 4.1 of
`hadwiger_degree9_hub_rainbow_rooted_k4.md` are valid.  In particular,
the Strong-\(\mathrm{HC}_4\) invocation has exactly the required
saturation hypothesis, and the resulting rooted model lifts through the
two contractions without identifying, enlarging, or overlapping a bag.

## 1. Contraction and rainbow trace

The two contracted stars are vertex-disjoint and connected.  Their
images are adjacent through the original edge \(vh\), so their colours
\(\alpha,\beta\) are distinct.  After deleting the centres, expanding
the two leaf sets monochromatically is proper: each leaf set is
independent, every leaf-to-outside edge was represented at its contracted
image, and every edge between the leaf sets has endpoints coloured
\(\alpha,\beta\).

At \(v\), the four selected common neighbours use two colours and only
two other neighbours remain, so \(|L_v|\ge2\).  Therefore any nonempty
\(L_h\) would give distinct representatives for \(L_v,L_h\).  It
follows for **every** colouring of the contracted minor that
\(L_h=\varnothing\).  Since \(W\) supplies exactly
\(\alpha,\beta\) and the residual set \(E\) has four vertices, \(E\)
must use the other four colours bijectively.  This verifies Theorem 2.1.

The Kempe-switch proof is also exact.  A switch involving two colours
of \(E\) does not affect either contracted image, whose colours are
\(\alpha,\beta\).  If two roots were in different bichromatic
components, switching one component would make their colours equal and
contradict the universal rainbow conclusion.

## 2. Strong-\(\mathrm{HC}_4\) hypothesis

Fix one six-colouring and let \(J\) be the union of the four colour
classes outside \(\{\alpha,\beta\}\).  Suppose a four-colouring of
\(J\) used at most three labels on \(E\).  Give the two original
colour classes in \(M-J\) two distinct fresh labels, disjoint from the
four-label palette on \(J\).  This is a proper six-colouring of all of
\(M\): each old class is independent, the two old classes have
different fresh labels, and every edge crossing to \(J\) has palettes
with disjoint labels.  The new colouring violates the universal rainbow
conclusion.  Hence every four-colouring of \(J\) uses all four colours
on \(E\), exactly the saturation hypothesis in the proved four-colour
case of Holroyd's Strong Hadwiger Conjecture.

The conclusion is an \(E\)-rooted \(K_4\)-model.  Since there are four
disjoint bags and four roots, each bag contains one root (possibly along
with other vertices), which is enough for the later adjacency to
\(\{h\}\).

## 3. Literal lifting

Neither contracted image belongs to \(J\), because their colours are
\(\alpha,\beta\).  All vertices of the rooted model are therefore
uncontracted vertices of \(G-(\{v,h\}\cup W)\).  Contracting the two
stars creates new edges only incident with a contracted image; it creates
no edge between two unaffected vertices.  Thus every bag edge, every
internal bag path, and every inter-bag adjacency of the model in \(J\)
already exists in \(G\).  The lift is literal.

Finally, each root lies in \(E\subseteq N(h)\), so the singleton
\(\{h\}\) is adjacent to all four bags, giving the claimed
\(K_5\)-model.

## 4. Exact limit

The note correctly does not claim a \(K_7\)-minor.  The rooted
\(K_4\)-model and \(\{h\}\) provide five branch sets.  Nothing proved
so far supplies two additional disjoint, adjacent connected sets each
meeting all four rooted bags.  That is a genuine remaining
portal/linkage requirement, not an automatic consequence of the rooted
core.
