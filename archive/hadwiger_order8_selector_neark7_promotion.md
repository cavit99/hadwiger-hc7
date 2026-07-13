# Equality selectors promote to a near-`K_7` obstruction

## 1. Literal equality gadgets are impossible at high connectivity

The dynamic selector counterarchitecture uses the six-colour equality
gadget

\[
                         E_6(a,b)=K_7-ab.                    \tag{1.1}
\]

Its incompatibility with the target setting is stronger than the visible
two-cut in the constructed graph.

### Lemma 1.1 (literal equality-gadget closure)

If a six-connected graph contains `K_7-ab` as a subgraph, then it
contains a `K_7` minor.

### Proof

Let `Z` be the five vertices other than `a,b`.  They induce `K_5` and
each is adjacent to both `a,b`.  Since the ambient graph is
six-connected, deleting the five vertices of `Z` leaves it connected.
Hence there is an `a-b` path `P` internally disjoint from `Z`.

Split `P` across any edge into adjacent connected sets `A,B`, with
`a in A` and `b in B`.  The seven branch sets

\[
                         A,B,\{z\}\quad(z\in Z)              \tag{1.2}
\]

are pairwise adjacent: `A,B` see one another across the split edge,
each sees every singleton through `a` or `b`, and the five singletons
form a clique.  They are a `K_7` model.  QED.

Thus the equality gadgets in `G_*` cannot be repaired by merely adding
redundant attachments while retaining a literal `K_7-ab`.  In a
six-connected target-free realization, equality has to be distributed
across the far shore.

The selector core itself has a second, even more relevant closure.

### Theorem 1.2 (uniform singleton-core fan completion)

Let `t>=3` and let `G` be `(t-1)`-connected.  Suppose there are

* a clique `C` of order `t-3`;
* a connected subgraph `D` disjoint from `C`; and
* adjacent vertices `x,y` disjoint from `C union D`,

such that each of `D,{x},{y}` is adjacent to every vertex of `C`.
Then `G` contains a `K_t` minor.

### Proof

The graph `G-C` is two-connected.  Fix `d in D`.  By the Fan Lemma it
has two internally disjoint paths from `d` to the two distinct vertices
`x,y`.  On each path, retain only the tail after its last vertex in `D`.
Absorb the internal vertices of the two tails into bags containing `x`
and `y`, respectively, while keeping `D` as one connected bag.  The two
new bags are disjoint, see `D` through the first edges of the tails, and
see one another through `xy`.

Together with the `t-3` singleton vertices of `C`, these three bags are
`t` pairwise adjacent branch sets: the hypotheses supply all contacts
to `C`.  Hence they form a `K_t` model.  QED.

For `t=7`, this is the exact label-preserving completion of a
`K_7^vee` model whose unaffected `K_4` core consists of singleton bags.
It is a parameter-uniform rooted-model principle, not a wheel-specific
calculation.

### Corollary 1.3 (almost-double-cone completion)

Let `G` be six-connected.  Suppose `Z={z_0,...,z_4}` induces `K_5`,
`xy` is an edge disjoint from `Z`, and both `x,y` are adjacent to the
same four vertices `z_1,...,z_4`.  Then `G` has a `K_7` minor.

### Proof

Apply Theorem 1.2 with
`C={z_1,...,z_4}` and `D={z_0}`.  QED.

In `G_*`, the proxy clique `Y` is such a `K_5`, the selector edge is
`xc_3`, and both ends see the same four proxies
`y_0,y_2,y_3,y_4`.  Therefore the selector already forces a `K_7` in
any six-connected supergraph, independently of the equality gadgets.
The equality gadgets explain the colour relation; Lemma 1.2 explains
why its concentrated five-colour core cannot survive high connectivity.

## 2. The distributed two-option selector

Let `F` be a graph with labelled vertices

\[
                    R=\{r_0,r_1,r_2,r_3,r_4\},\quad x,y.    \tag{2.1}
\]

Say that `F` is a **two-option selector at `r_0`** when all of the
following hold.

1. In every six-colouring of `F`, the five vertices of `R` have
   different colours.
2. In every six-colouring, each of `x,y` has either the colour of `r_0`
   or the unique colour absent from `R`.
3. The edge `xy` belongs to `F`.
4. Both cross modes occur:
   \[
   (x=r_0,\ y=\text{fresh}),\qquad
   (x=\text{fresh},\ y=r_0).                               \tag{2.2}
   \]

This definition is invariant under palette permutations.  The explicit
far shore in the dynamic wheel note is a two-option selector with

\[
       R=(c_2,c_0,c_4,c_5,z),\qquad x=x,\quad y=c_3.         \tag{2.3}
\]

### Theorem 2.1 (two virtual edges create a near-clique source)

If `F` is a two-option selector at `r_0`, then

\[
                         J=F+xr_0+yr_0                      \tag{2.4}
\]

is not six-colourable, while each of `J-xr_0` and `J-yr_0` is
six-colourable.

Consequently `J` contains a `K_7^\vee` minor by the
Norin--Totschnig near-`K_7` theorem.

### Proof

In a six-colouring of `J`, the two new edges forbid `x,y` from using the
colour of `r_0`.  Items 1--2 therefore force both to use the unique fresh
colour.  This contradicts the old edge `xy`, proving that `J` is not
six-colourable.

For `J-xr_0`, use the first cross mode in (2.2): `x` has the anchor
colour and `y` the fresh colour.  The remaining new edge `yr_0` is
proper.  The second cross mode colours `J-yr_0` symmetrically.

The cited theorem says that every graph with no `K_7^\vee` minor is
six-colourable.  Its contrapositive applied to `J` gives the final
claim.  QED.

### Corollary 2.2 (faithful realization of the virtual edges)

Suppose a host graph contains `F` and also contains internally
vertex-disjoint paths `P_x,P_y`, internally disjoint from `F`, joining
`x` to `r_0` and `y` to `r_0`, respectively (their only common vertex
may be `r_0`).  Then the host contains `J` as a minor and hence contains
a `K_7^\vee` minor.

### Proof

Contract the internal vertices of `P_x,P_y` toward their labelled ends.
This adds the two edges in (2.4) without identifying any two vertices of
`F`.  Apply Theorem 2.1.  QED.

The conclusion is deliberately `K_7^\vee`, not `K_7`.  Completing the
near-clique requires the independent label-preserving split-versus-
two-apex theorem already isolated in the near-`K_7` programme.

## 3. What the three displayed states do and do not imply

The states `rho,tau,mu` in the dynamic wheel note show that the far side
**accepts** the two cross modes and, after one operation, the double-
anchor mode.  Existence of these three colourings alone does not imply
items 1--2 of the selector definition.  A far shore may accept further
boundary modes which are irrelevant to those three witnesses.

Therefore the following inference is invalid without an additional
minimality argument:

\[
 \rho,\tau,\mu\text{ occur}
 \quad\Longrightarrow\quad
 F\text{ is a two-option selector}.                         \tag{3.1}
\]

The exact missing step is now finite and operation-sensitive:

> **Selector normalization target.**  In the atomic wheel residue of a
> proper-minor-minimal counterexample, either an additional far-side
> boundary mode already yields the two protected columns or a six-
> colouring of the whole graph, or the far-side extension relation
> reduces to a two-option selector at one active root.

Once this normalization is proved, Theorem 2.1 promotes the selector to
`K_7^\vee`.  The remaining geometric task is to realize the two virtual
anchor edges by disjoint paths, or to turn their failure into an
order-at-most-six adhesion.  This is exactly a two-linkage problem, not a
new raw portal enumeration.

## 4. Strategic consequence

The explicit counterarchitecture and Lemma 1.1 leave two genuinely
different possibilities for a coherent selector in the target graph.

1. **Concentrated equality.**  A literal or rooted equality core behaves
   like `K_7-ab`; six-connectivity supplies the missing bypass and closes
   it to `K_7`.
2. **Distributed equality.**  No five-vertex clique core is exposed.
   The selector-normalization step gives the two-option relation, and
   Theorem 2.1 yields `K_7^\vee` after two virtual anchor paths.

Thus the dynamic wheel obstruction feeds directly into the independent
near-`K_7` split-versus-two-apex route.  The new reusable principle is:

\[
 \boxed{\text{a five-colour selector is either locally completable, or
 promotes to a near-`K_7` source via two labelled virtual edges.}}      \tag{4.1}
\]

What is not proved is selector normalization or the faithful realization
of both virtual edges in an arbitrary seven-connected counterexample.
