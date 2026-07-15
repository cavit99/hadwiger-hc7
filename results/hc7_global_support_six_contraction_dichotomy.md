# Global support-six contraction dichotomy

**Status:** proved.  This is a normal-form and handoff theorem, not a
closure of the support-six case and not a proof of `HC_7`.

## 1. Setup

For a graph `G` and a two-vertex set `P`, define

\[
 \mu_G(P)=\min\left\{
   \left|\bigcup_{B\in\mathcal M}B\right|:
   \mathcal M\text{ is a }K_5\text{-model in }G-P
 \right\},
\]

with value infinity if `G-P` has no `K_5` minor.  A pair `P` is a
**literal-`K_5` transversal** if every subgraph of `G` isomorphic to
`K_5` meets `P`.

An **actual seven-separation** is a separation `(A,B)` with

\[
 |A\cap B|=7,
 \qquad A-B\ne\varnothing,
 \qquad B-A\ne\varnothing.
\]

## 2. The theorem

### Theorem 2.1 (support-six contraction dichotomy)

Let `G` be a seven-connected `K_7`-minor-free graph.  Let `P` be a
literal-`K_5` transversal with

\[
                         \mu_G(P)=6.                    \tag{2.1}
\]

Choose a six-vertex `K_5` model `M` in `G-P`.  Then the following hold.

1. Four bags of `M` are singleton vertices forming a clique
   `Q={q_1,q_2,q_3,q_4}`, and the fifth bag is an edge `xy`.
2. Put

   \[
   D_x=\{q\in Q:xq\notin E(G)\},
   \qquad
   D_y=\{q\in Q:yq\notin E(G)\}.                       \tag{2.2}
   \]

   The sets `D_x,D_y` are nonempty and disjoint.  Up to interchanging
   `x,y`, the triple

   \[
   \bigl(|D_x|,|D_y|,
          |Q-(D_x\cup D_y)|\bigr)                      \tag{2.3}
   \]

   is one of

   \[
                (1,1,2),\quad(1,2,1),\quad
                (1,3,0),\quad(2,2,0).                 \tag{2.4}
   \]
3. For `W=Q\cup\{x,y\}`, the graph `G-W` is connected, and every
   literal vertex of `W` has a neighbour in `G-W`.
4. Let `H=G/xy`, and let `z` denote the contracted image of `xy`.
   Then `H` is `K_7`-minor-free and `Q\cup\{z\}` is a literal
   `K_5`.  Moreover, exactly one of the following structural alternatives
   is available:

   * `H` is seven-connected; or
   * `G` has an actual seven-separation `(A,B)` for which
     `x,y\in A\cap B`.

### Proof

Five nonempty branch sets of total order six have size multiset

\[
                              (2,1,1,1,1).              \tag{2.5}
\]

The two-vertex bag is connected, so its two vertices, denoted `x,y`, are
adjacent.  The four singleton bags form a literal `K_4`, denoted by `Q`.
For every `q\in Q`, adjacency between the edge-bag and the singleton bag
means that at least one of `xq,yq` is an edge.  Consequently

\[
                              D_x\cap D_y=\varnothing.  \tag{2.6}
\]

If `D_x` were empty, then `Q\cup\{x\}` would be a literal `K_5`
disjoint from `P`, contrary to the choice of `P`.  Thus `D_x` is
nonempty, and the same argument applies to `D_y`.  The two nonempty,
disjoint sets `D_x,D_y`, together with their common-contact complement,
partition a four-element set.  Interchanging `x,y` if necessary gives
exactly the four triples in (2.4).  This proves assertions 1 and 2.

Deleting fewer than seven vertices from a seven-connected graph leaves a
connected graph.  Hence `G-W` is connected.  Also every vertex of `G`
has degree at least seven, whereas a vertex of the six-set `W` has at
most five neighbours in `W`.  Every vertex of `W` therefore has a
neighbour outside `W`.  This proves assertion 3.

The contraction `H=G/xy` is a minor of `G`, and hence is
`K_7`-minor-free.  Every `q\in Q` is adjacent to at least one of `x,y`,
so its image is adjacent to `z` in `H`.  Therefore `Q\cup\{z\}` is a
literal `K_5` in `H`.

Suppose that `H` is not seven-connected.  Choose a vertex separator `T`
of `H` with `|T|\le 6`.  Necessarily `z\in T`.  Indeed, if `z\notin T`,
split `z` back into the adjacent vertices `x,y`.  All neighbours formerly
incident with `z` remain joined through the edge `xy`, so this split does
not join two distinct components of `H-T`; thus `T` would also separate
`G`, contrary to seven-connectivity.

Now put

\[
                         S=(T-\{z\})\cup\{x,y\}.        \tag{2.7}
\]

Deleting `S` from `G` gives exactly the same nonempty components as
deleting `T` from `H`.  Thus `S` separates `G`, and

\[
                              |S|=|T|+1\le7.            \tag{2.8}
\]

Seven-connectivity forces `|S|=7`; hence `|T|=6`.  Taking two nonempty
unions of components of `G-S` as the open shores gives an actual
seven-separation with `x,y\in S`.

Conversely, suppose that `G` has an actual seven-separation whose
boundary contains `x,y`.  Contracting `xy` replaces those two boundary
vertices by `z`, so the same two nonempty open shores are separated in
`H` by a set of order six.  Hence `H` is not seven-connected.  The two
alternatives in assertion 4 are therefore mutually exclusive as well as
exhaustive.  This proves assertion 4. \(\square\)

## 3. Criticality specialization and exact palette input

### Corollary 3.1

Assume additionally that `G` is a minor-minimal counterexample to
`HC_7`.  In the notation of Theorem 2.1,

\[
                              \chi(H)=6.                \tag{3.1}
\]

For every proper six-colouring `c` of `H`, write `c(z)=alpha`.  Then each
of `x` and `y` has in `G` a neighbour in every one of the other five
colour classes.

### Proof

Minor-minimality gives `chi(H)\le6`.  If `H` had a colouring with at most
five colours, split `z` back into `x,y`, initially giving both endpoints
the colour of `z`, and recolour one endpoint with a fresh sixth colour.
This would be a six-colouring of `G`, a contradiction.  Hence (3.1)
holds.

Now fix a six-colouring `c` of `H`.  Pull it back to a colouring of
`G-xy` in which `x,y` both have colour `alpha`.  If, say, `x` had no
neighbour of another colour `beta`, recolour `x` with `beta` and leave
`y` with colour `alpha`.  This resolves the edge `xy` and creates no new
monochromatic edge, again producing a six-colouring of `G`.  Therefore
`x` sees every colour other than `alpha`; the argument for `y` is
identical. \(\square\)

The corollary is the exact palette information available for a future
transversal pullback.  It supplies literal colour contacts, but it does
not identify those contacts with prescribed branch-set labels.

## 4. What this says about the global support potential

The only support-six failure of literal-`K_5` transversality is a
complementary split of one vertex of a literal `K_5`: contraction of the
edge-bag produces `Q\cup\{z\}`, while lifting `z` produces exactly one of
the four deficiency patterns (2.4).

The two branches of Theorem 2.1 locate the next obstruction precisely.

* If `xy` is not seven-contractible, the obstruction canonically exposes
  an actual exact-seven adhesion containing both split vertices.
* If `xy` is seven-contractible, the literal-`K_5` transversal `P` need
  not survive in the proper minor `H`.  Conversely, a two-vertex
  transversal `{z,a}` found in `H` need not pull back to either
  `{x,a}` or `{y,a}` in `G`; the automatic lift is the three-set
  `{x,y,a}`.

Thus the missing result is a **stateful two-transversal pullback** across
the four complementary split types, with an exact-seven separation as
the noncontractible handoff.  The palette contacts in Corollary 3.1 are
the criticality input to such a theorem.

There is also a basic logical limitation on a proposed strict support
exchange.  If `P` is chosen globally to maximize `mu_G(P)`, then a
conclusion of the form

\[
 \text{`a }K_7\text{', or `an avoided pair', or }
 \mu_G(P')>\mu_G(P)                                    \tag{4.1}
\]

cannot use its third alternative.  On seven-connected `K_7`-minor-free
hosts, proving (4.1) at a maximizing pair is therefore exactly the
avoided-pair theorem, rather than an intermediate monotonicity lemma.
Furthermore, constructing a new `K_5` model for `P'` proves only an upper
bound on `mu_G(P')`; proving a strict increase requires excluding every
model of support at most `mu_G(P)` in `G-P'`.

## 5. Trust boundary

The following statements are proved here.

* the four literal support-six normal forms;
* connectedness and full attachment of the six-vertex exterior;
* the seven-connected-contraction versus actual-seven-adhesion
  dichotomy;
* in a minimal `HC_7` counterexample, exact six-chromaticity of the
  contraction and the five-colour contact condition at both split
  endpoints.

The theorem does **not** prove any of the following.

* that a literal-`K_5` transversal pulls back through the split;
* that either branch yields a common equality state or a six-colouring;
* that the exact-seven adhesion is already closed by existing packet
  theorems;
* that the five palette contacts occupy five prescribed model rows;
* that the support potential itself is a strict global rank.

Accordingly this result is a uniform global handoff theorem, not a
closure of the support-six rung.
