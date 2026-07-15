# Independent audit: substituted-host rooted-`K_4` obstruction

**Verdict:** GREEN after uniform fill-clique elimination was moved ahead of
the skeleton-degree arguments.

**Audited source:** `results/hc7_direct_reserve_rooted_k4_obstruction.md`

**Source SHA-256:**
`4309877d4b2a76e7f473b998aaf362b5b7525049be1283f20b9fd6fb038c54ca`

## 1. Canonical nonedges

The vertices `x,y,r` are all bad-path endpoints. Such endpoints have
singleton lists. Since they lie in `W`, whose lists always contain label
one, their lists are singleton `{1}`. The canonical equivalence

\[
0\in\Lambda(w)\quad\Longleftrightarrow\quad zw\in E(G)
\]

therefore gives `zx,zy,zr notin E(G)`. The setup is exact.

## 2. Fabila-Monroy--Wood classification and fill cliques

Theorem 15 of Fabila-Monroy and Wood says that a graph with four nominated
vertices either has the corresponding rooted `K_4` minor or is a spanning
subgraph of an obstruction in one of classes `A`--`F`. Here "spanning"
means that `J` and the containing obstruction have the same vertex set.

In every obstruction, a fill clique `X_T` is disjoint from the base
skeleton and has neighbours only in `T union X_T`, where `T` is a
three-vertex facial triangle. All nominated vertices lie in the skeleton.
If `X_T` were nonempty, orient the separation with

\[
X=J-X_T,\qquad Y=J[T\cup X_T].
\]

Then all four roots lie in `X`, `Y-X=X_T` is nonempty, and
`|X intersect Y|<=3`. This contradicts the audited internal
four-connectivity of `(J,Q')`. Thus every fill clique is empty before any
skeleton-degree claim is used.

This ordering is essential: without it, a nominated vertex of degree two
in the skeleton could acquire extra fill-clique neighbours.

## 3. Degree transfer to the host graph

After fill elimination, a skeleton-degree-two nominated vertex has
`d_J(z)<=2`. The induced host `J` already contains every vertex of `A` and
the three selected boundary vertices. There are no `z-R` edges because
there is no `A-R` edge. Hence all neighbours of `z` outside `J` lie in the
four-set `S-{x,y,r}`, and

\[
d_G(z)\le2+4=6.
\]

This contradicts seven-connectivity. The transfer uses no completion edge
and omits no possible outside-neighbour class.

## 4. Elimination of classes `A`, `B`, `C`, `E`, and `F`

- In `B`, `C`, and `F`, every nominated vertex has skeleton degree two.
- In `A`, three nominated vertices have degree two. If `z` is the remaining
  nominated vertex `p`, the other three nominated vertices are pairwise
  nonadjacent, contradicting the literal edge `xy` in the spanning
  subgraph `J`.
- In `E`, exactly two nominated vertices have degree two and the only edge
  between nominated vertices is the outer edge joining the other two.
  Therefore literal `xy` forces `x,y` to be those outer nominees and leaves
  `z` among the degree-two nominees.

All five eliminations are correct after the uniform fill-clique step.

## 5. The surviving class `D`

With all fill cliques empty, a class-`D` obstruction is the literal planar
web skeleton with all four nominated vertices on its outer face. Since `J`
is a spanning subgraph, restricting the embedding and deleting edges gives
a planar embedding of literal `J`; edge deletion only merges faces, so the
four roots remain incident with one common face.

Conversely, four cofacial vertices cannot root a `K_4` model: contracting
the four disjoint rooted bags would produce an outerplanar `K_4`, or,
equivalently, the model would contain disjoint paths joining alternating
boundary pairs. Thus the two outcomes are exclusive.

## 6. Scope

The theorem exactly reduces failure of a substituted rooted `K_4` to a
clean literal rural embedding. It does not create an exact-seven adhesion
or decode the three omitted boundary portals. The remaining obligation in
the source is therefore stated without overclaiming.
