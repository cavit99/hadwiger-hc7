# A leaf-rooted chromatic drop across a four-colour two-shore boundary

**Status:** proved; independently audited after the corrections recorded in
`hc7_leaf_rooted_chromatic_drop_audit.md`.

This theorem converts the four-colour boundary left by the minimal-bad
three-model contraction into a literal leaf-rooted chromatic-drop witness.
It does not assume an equitable boundary colouring and does not enumerate
boundary graphs.  The witness size is only a local parameter at this stage;
no recursive descent theorem for it is claimed here.

## 1. The contraction forest

### Theorem 1.1 (leaf-rooted five-colour drop)

Let `G` be a seven-chromatic graph such that every proper minor of `G` is
six-colourable and every edge contraction of `G` is six-chromatic.  Suppose

\[
                 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
\]

where `G[A]` and `G[B]` are nonempty and connected, there is no `A-B`
edge, every vertex of `S` has a neighbour in each of `A,B`, and
`G[S]` is four-colourable.

Then there are a forest `F_0` of at least two edges and a leaf edge
`e=uv` of `F_0` with the following properties.  Put

\[
                         H=G/(F_0-\{e\}).
\]

The endpoint `u` may be chosen to be a literal original vertex of `G`,
while `v` is the image of a connected vertex set in the same open shore,
and

\[
                         \chi(H)=6,
                 \qquad \chi(H/uv)=5.                 \tag{1.1}
\]

In particular, `H` has a six-colouring in which `u` is the unique vertex
of its colour.  The same conclusion holds with `v` as the unique sixth
colour, although `v` need not be literal.

### Proof

Choose spanning trees `T_A,T_B` of the two open shores and put

\[
                         F=E(T_A)\cup E(T_B).
\]

Contracting all edges of `F` turns `A,B` into two nonadjacent vertices,
each complete to `S`.  The resulting graph is exactly

\[
                         I_2\vee G[S],
\]

and is five-colourable: use four colours on `G[S]` and one common new
colour on the two vertices of `I_2`.

Choose an inclusion-minimal nonempty set `F_0 \subseteq F` for which
`G/F_0` is five-colourable.  The set `F_0` is a forest.  It has at least
two edges, because every single-edge contraction of `G` is
six-chromatic.

For every `e in F_0`, minimality gives

\[
                         \chi(G/(F_0-\{e\}))\ge6.
\]

This graph is a proper minor of `G` and is six-colourable: it contains at
least one contraction because `|F_0|>=2`.  Hence its chromatic number is
exactly six.  Its contraction of the image of `e` is `G/F_0`, which is
five-colourable.  A four-colouring of `G/F_0` would lift through the last
edge by giving one endpoint a fresh fifth colour, five-colouring the
six-chromatic predecessor.  Therefore `chi(G/F_0)=5`, and (1.1) follows.

Choose `e=uv` to be a leaf edge of the forest `F_0`, with `u` its leaf.
After all other edges of `F_0` have been contracted, `u` is still the
literal original leaf vertex, while `v` represents the connected other
component of `F_0-e` incident with `e`.  Both lie in the same original
open shore.

Finally take a five-colouring of `H/uv`.  Lift it to `H` by retaining the
colour of the contracted image on `v` and assigning a fresh sixth colour
to `u`.  This is proper, and `u` is the unique vertex of the fresh colour.
Interchanging the roles of the two endpoints gives the symmetric
colouring.  \(\square\)

## 2. The critical rooted kernel

### Theorem 2.1 (three regenerated levels at the drop edge)

In the setting of Theorem 1.1, let `C` be any induced subgraph of `H`
that is six-vertex-critical.  Then `u,v \in V(C)`, and

\[
 \begin{aligned}
   \chi(C/u v)&=5,\\
   \chi(C-u)=\chi(C-v)&=5,\\
   4\le\chi(C-\{u,v\})&\le5.                         \tag{2.1}
 \end{aligned}
\]

Consequently:

1. `C/uv` contains a `K_5` minor.  On expansion to `C`, the resulting
   `K_5` model either has one branch bag containing the named edge `uv`,
   or avoids both `u` and `v`, according as the contracted vertex is used
   or omitted by the quotient model;
2. `C-u` and `C-v` each contain a `K_5` minor; and
3. `C-{u,v}` contains a `K_4` minor.

The clique-minor conclusions use only the established cases `HC_4` and
`HC_5`.

### Proof

The five-colouring of `H/uv` lifts to five-colourings of each of `H-u`
and `H-v`: retain the contracted vertex's colour on the surviving
endpoint.  A six-critical subgraph of `H` therefore cannot omit either
endpoint, so `u,v in V(C)`.

The graph `C/uv` is a subgraph of `H/uv`, hence is at most
five-colourable.  If it were four-colourable, lifting across `uv` with one
fresh colour would five-colour `C`, a contradiction.  Thus
`chi(C/uv)=5`.

Vertex-criticality gives `chi(C-u),chi(C-v)<=5`.  Each is at least five,
because adding its omitted vertex with one fresh colour raises chromatic
number by at most one.  This proves the second line of (2.1).

Certainly `chi(C-{u,v})<=5`.  If it were at most three, colour it with
three colours and give `u,v` two distinct fresh colours.  This would
five-colour `C`, again a contradiction.  Hence its chromatic number is at
least four.

Apply `HC_5` to the three five-chromatic graphs in (2.1), and `HC_4` to
`C-{u,v}`.  If the quotient vertex is used by the first model, expanding
that branch bag replaces it by the connected edge `uv`.  If the quotient
vertex is omitted, the same model already lies in `C-{u,v}`.  \(\square\)

### Corollary 2.2 (rooted-model fork)

Exactly one of the following two chromatic branches occurs.

1. If `chi(C-{u,v})=5`, then `C-{u,v}` contains a `K_5` model avoiding
   both ends of the drop edge.
2. If `chi(C-{u,v})=4`, then `C-u` contains a `K_5` model having `{v}` as
   a singleton branch bag, and `C-v` contains a `K_5` model having `{u}`
   as a singleton branch bag.  Moreover, `C` contains a `K_5` model whose
   one branch bag contains the edge `uv`.

### Proof

The first branch is `HC_5`.  In the second branch, choose a
five-vertex-critical subgraph `D_v` of the five-chromatic graph `C-u`.
Since `(C-u)-v` is four-colourable, `v` belongs to `D_v`.  The theorem of
Martinsson--Steiner on five-vertex-critical graphs gives a `K_5` model in
`D_v` whose prescribed vertex `v` is a singleton bag.  Apply the same
argument to `C-v` with prescribed vertex `u`.  Finally choose a
five-vertex-critical subgraph of `C/uv`.  It must contain the contracted
vertex, because deleting that vertex leaves the four-colourable graph
`C-{u,v}`.  Prescribe that vertex as a singleton branch bag and expand it
back to the edge `uv`.  \(\square\)

The Martinsson--Steiner input is the established theorem from
*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*,
JCTB 164 (2024), 1--16 (arXiv:2209.00594): in a five-vertex-critical
graph any prescribed vertex may be chosen as a singleton bag of a
`K_5` model.

### Theorem 2.3 (uniform common-neighbour rooted composition)

Let `k>=1`, let `J` be any `(k+2)`-chromatic graph, let `uv` be an edge,
and suppose

\[
                         \chi(J-\{u,v\})\le k.
\]

Then `chi(J-{u,v})=k` and the common-neighbour set

\[
       X=N_J(u)\cap N_J(v)\cap V(J-\{u,v\})
\]

is colourful in `J-{u,v}`.  Consequently, whenever Strong Hadwiger is
known for `k` colours, `J` has a `K_{k+2}` model whose first two branch
bags are the literal singletons `{u}` and `{v}`.

### Proof

Put `R=J-{u,v}`.  If `R` were `(k-1)`-colourable, giving `u,v` two fresh
distinct colours would `(k+1)`-colour `J`.  Hence `chi(R)=k`.

Fix a `k`-colouring `phi` of `R` and a colour `i`.  Suppose no vertex of
`X` has colour `i`.  Recolour every colour-`i` neighbour of `u` with a
fresh colour `k+1`.  These vertices form an independent set.  None is a
neighbour of `v`, by the supposition on `X`.  We may now colour `u` with
`i` and `v` with colour `k+1`.  This is a proper `(k+1)`-colouring of
`J`, a contradiction.

Thus `X` contains all `k` colours in every `k`-colouring of `R`; it is
colourful.  Strong Hadwiger for `k` colours gives an `X`-rooted `K_k`
model in `R`.  Every one of its `k` bags contains a common neighbour of
`u,v`.  Adding `{u}` and `{v}` therefore gives `k+2` pairwise disjoint,
connected and pairwise adjacent bags, with the two prescribed singleton
bags.  \(\square\)

### Corollary 2.4 (the four-chromatic drop branch is label-faithful)

In the four-chromatic branch of Corollary 2.2, the critical graph `C` has
a `K_6` model with singleton branch bags `{u}` and `{v}`.

### Proof

Apply Theorem 2.3 to `J=C` and `k=4`, using the established Strong
Hadwiger theorem for four colours.  \(\square\)

For comparison, applying Strong Hadwiger separately gives the weaker
statement below.  Put

\[
 R=C-\{u,v\},\qquad A_u=N_C(u)\cap V(R),\qquad
 A_v=N_C(v)\cap V(R).
\]

Both `A_u` and `A_v` are colourful in `R`: every proper four-colouring
of `R` uses all four colours on each set.  Consequently the Strong
Hadwiger theorem for four colours gives an `A_u`-rooted `K_4` model and
an `A_v`-rooted `K_4` model in `R`.

If `R` has one `K_4` model every branch bag of which meets both `A_u` and
`A_v`, then adjoining the singleton bags `{u},{v}` gives a label-faithful
`K_6` model in `C`.

### Proof

If a four-colouring of `R` omitted a colour on `A_u`, give `u` that
omitted colour and give `v` one fresh fifth colour.  This would
five-colour `C`, a contradiction.  The argument for `A_v` is symmetric.
Apply the Martinsson--Steiner Strong Hadwiger theorem for four colours to
each colourful set.  For the final assertion, every one of the four bags
contacts both `u` and `v`, while `uv` is an edge.  \(\square\)

Theorem 2.3 shows that no two-set composition gap remains: six-chromaticity
forces the *intersection* `A_u cap A_v` itself to be colourful.  The
remaining HC7 issue is instead to preserve a connected part of the
opposite old shore while lifting this labelled `K_6` back through the
minimal contraction forest.

## 3. Application to the exact excess-eight/nine residue

The audited two-full-shore absorption theorem, together with the audited
universal-pair elimination, proves that every surviving expanded boundary
in the two-component minimal-bad residue is four-colourable.  The original
minimal `HC_7` counterexample is strongly seven-contraction-critical, so
Theorems 1.1--2.1 apply.

Thus every surviving residue contains a literal shore vertex `u`, a
connected same-shore carrier represented by `v`, and a six-critical minor
with all three of the following simultaneously regenerated:

* a `K_5` model obtained from `C/uv`, which either uses `uv` in one bag or
  avoids both endpoints;
* a `K_5` model avoiding either chosen endpoint; and
* a `K_4` model avoiding both endpoints.

Corollary 2.2 sharpens this to an exact fork: either a `K_5` model avoids
the whole drop edge, or both orientations have a `K_5` model singleton-
rooted at the opposite endpoint.

The size of the minimal forest `F_0` is a finite local witness size.  The
leaf edge may be contracted to reach the five-chromatic quotient, or one
of the endpoint-avoiding models may instead be used.  However, contracting
the leaf exits the seven-chromatic hypothesis class, and no theorem here
returns a new two-shore instance with a smaller minimal forest.  Thus
`|F_0|` is only a candidate ingredient for a later recursive rank, not a
rank already proved to decrease along the active proof spine.

## 4. Trust boundary

The theorem does not yet turn the regenerated models into a
`K_7`.  In particular, the `K_5` models in Theorem 2.1 need not be small,
disjoint, or label-aligned.  It supplies a literal root but not the missing
global rank.  The remaining frontier is a rooted-model composition theorem
at this drop edge, not another classification of four-colour boundaries.
