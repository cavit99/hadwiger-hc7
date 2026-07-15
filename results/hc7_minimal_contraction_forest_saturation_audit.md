# Independent audit: minimal contraction-forest saturation

**Verdict:** **GREEN after one clarification of minimality.**

The quotient identities remain exact when `F_0` has several components,
the edge-by-edge colouring lift is valid, and Corollary 2.1 expands to the
two literal connected sides of the chosen forest cut.  The theorem now
states explicitly that **no proper subset**, including the empty set, has
the required colouring property.

## 1. Minimality convention

The phrase “nonempty inclusion-minimal set for which” must mean

\[
 F_0\ne\varnothing,qquad G/F_0\text{ is `q`-colourable},qquad
 G/F'\text{ is not `q`-colourable for every }F'\subsetneq F_0.
\]

If minimality were taken only among nonempty qualifying sets, the theorem
would be false.  For example, take `G=K_2`, `q=2`, and let `F_0` be its
single edge.  It is minimal among nonempty sets and its contraction is
two-colourable, but `H_e=G` is also two-colourable and neither endpoint has
an external neighbour of the unused colour.  The corrected statement
excludes this example because the empty subset already qualifies.

With the explicit all-proper-subsets convention, minimality gives that
every `H_e=G/(F_0-{e})` is not `q`-colourable, including when `F_0` is a
singleton.

## 2. Quotients with several forest components

Let `T` be the component of `(V(G),F_0)` containing `e`.  Since `F_0` is a
forest, `T-e` has exactly two connected components.  Contracting
`F_0-{e}` turns those two components into distinct adjacent vertices
`x_e,y_e`; the original edge `e` survives between them.  Every other
component of `F_0` is already contracted to one vertex.

Passing from `H_e` to `K` contracts only `x_ey_e`.  It does not merge or
otherwise change any vertex arising from another component of `F_0`.
Consequently:

* every vertex of `H_e-{x_e,y_e}` is canonically the same quotient vertex
  as one in `K-z_e`;
* an edge among two such vertices occurs in one graph exactly when it
  occurs in the other; and
* deleting `x_e,y_e` from `H_e` gives exactly `K-z_e`.

Cross-edges between distinct components of `F_0` cause no problem: they
become ordinary edges between the corresponding quotient vertices in both
graphs.

## 3. Edge-by-edge colour saturation

Fix a proper `q`-colouring `phi` of `K` and put `c=phi(z_e)`.  Every
external neighbour of `x_e` or `y_e` remains distinct from `z_e` after the
last contraction and is adjacent to `z_e`; it therefore cannot have colour
`c`.

If, say, `x_e` has no external neighbour of a colour `d!=c`, retain `phi`
away from `z_e`, give `x_e` colour `d`, and give `y_e` colour `c`.  This is
proper because:

1. no external neighbour of `x_e` has colour `d` by assumption;
2. no external neighbour of `y_e` has colour `c` by properness at `z_e`
   in `K`; and
3. `x_ey_e` receives two different colours.

All edges away from this pair retain the proper quotient colouring.  This
would `q`-colour `H_e`, contradicting minimality.  Interchanging the two
ends proves saturation on both sides.  The argument is independent for
every `e in F_0` and every colouring of `K`; it does not require `F_0` to
be connected.

As a useful consistency check, the same lifting argument also shows
automatically that `chi(K)=q` and `chi(H_e)=q+1`: a `(q-1)`-colouring of
`K` would lift to a `q`-colouring of `H_e`, while a `q`-colouring of `K`
always lifts using one fresh colour.

## 4. Literal-leaf corollary

For a leaf `u` of `T`, no edge of `F_0-{e}` is incident with `u`, so `u`
is not identified with another original vertex.  The opposite quotient
vertex represents all of the connected tree `T-u`.  The two saturation
claims are therefore exactly Theorem 1.1 applied to the two sides of the
leaf edge.

## 5. Corollary 2.1 and expansion

The hypotheses give

\[
 \chi(H_e)=q+1=(q-1)+2,qquad
 \chi(H_e-\{x_e,y_e\})=chi(K-z_e)=q-1.
\]

Thus the uniform common-neighbour rooted theorem applies with `k=q-1`.
Its common-neighbour set is precisely the displayed `X_e`, under the
canonical identification above.  Strong Hadwiger for `q-1` gives the
rooted `K_{q-1}` model, and adjoining singleton bags `{x_e},{y_e}` gives a
`K_{q+1}` model in `H_e`.

When this model is lifted to `G`, every quotient vertex is replaced by its
connected preimage under the contractions in `F_0-{e}`.  In particular,
the singleton bags `{x_e}` and `{y_e}` expand to exactly the two connected
components of `T-e`.  Their preimages are disjoint, their mutual adjacency
is the original edge `e`, and every quotient adjacency has an original
edge witnessing it.  Hence the expansion claim is literal and valid even
when other components of `F_0` also occur in other model bags.

## 6. Exact scope

The result universally quantifies over every terminal colouring, but it
does not select one fixed system of contact vertices valid for all
colourings.  It also does not imply that some `z_e` is chromatically
critical in `K`, preserve a seventh branch carrier, or turn `|F_0|` into a
recursive rank.  With those limits, the corrected theorem is GREEN.
