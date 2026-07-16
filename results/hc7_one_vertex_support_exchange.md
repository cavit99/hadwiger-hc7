# One-vertex exchange in a critical family of small `K_5`-model supports

**Status:** written proof; independently audited in
[`hc7_one_vertex_support_exchange_audit.md`](hc7_one_vertex_support_exchange_audit.md).
This is a set-system
exchange lemma and a local application to the exceptional six-linkage
configuration.  It does not prove the support-six transversal theorem or
`HC_7`.

## 1. Critical-family exchange

For a family `A` of sets, write `tau(A)` for its transversal number.  Let
`F_5(G)` be the family of supports of all `K_5`-minor models in `G` whose
support has order five.  Every member of `F_5(G)` is therefore the vertex
set of a literal `K_5` subgraph.

### Theorem 1.1 (one-vertex support exchange)

Let `G` be a seven-connected `K_7`-minor-free graph for which

\[
                         \tau(\mathcal F_6(G))>2.       \tag{1.1}
\]

Let `C` be an inclusion-minimal family of six-vertex `K_5`-model supports
such that

\[
            \tau\bigl(\mathcal F_5(G)\cup\mathcal C\bigr)>2. \tag{1.2}
\]

Fix `A in C` and put

\[
 \mathcal H=\mathcal F_5(G)\cup(\mathcal C-\{A\}).     \tag{1.3}
\]

Suppose `A'` is another six-vertex `K_5`-model support and

\[
                    A-A'=\{y\},\qquad A'-A=\{w\}.      \tag{1.4}
\]

Then at least one of the following alternatives is available.

1. There is an inclusion-minimal family
   `C' subseteq (C-{A}) union {A'}` for which

   \[
       \tau\bigl(\mathcal F_5(G)\cup\mathcal C'\bigr)>2,
                                                               \tag{1.5}
   \]

   and every such inclusion-minimal family contains `A'`.
2. There is a two-vertex set `R` such that

   \[
       w\in R,\qquad R\cap A=\varnothing,qquad
       R\text{ meets every member of }\mathcal H,       \tag{1.6}
   \]

   and

   \[
                \mu_G(R)=6=\max_{|P|=2}\mu_G(P).       \tag{1.7}
   \]

Here `mu_G(P)` is the minimum support order of a `K_5` model in `G-P`.
The first alternative is a legal rebasing of the critical family onto
`A'`; the second moves a globally support-maximal private pair onto the new
vertex `w`.

Moreover, suppose a two-set `P` meets every member of `H` and is disjoint
from `A union {w}`.  In alternative 1 the same pair `P` is disjoint from
`A'` and remains a private pair for `A'` relative to `H`; in particular,
`mu_G(P)=6`.

#### Proof

Minimality of `C` gives

\[
                           \tau(\mathcal H)\le2.        \tag{1.8}
\]

In fact `tau(H)=2`.  If `H` had a transversal of order at most one,
then either it already met `A`, or adjoining one vertex of `A` would give
a transversal of `H union {A}` of order at most two, contrary to (1.2).

First suppose

\[
                  \tau(\mathcal H\cup\{A'\})>2.       \tag{1.9}
\]

Choose an inclusion-minimal subfamily `C'` of
`(C-{A}) union {A'}` for which (1.5) holds.  Such a family exists by
(1.9).  It must contain `A'`, since otherwise it is a subfamily of
`C-{A}` and (1.8) would give transversal number at most two.  This is
alternative 1.

Now suppose instead that

\[
                  \tau(\mathcal H\cup\{A'\})\le2.      \tag{1.10}
\]

Choose a transversal `R_0` of this family with order at most two.  The set
`R_0` is disjoint from `A`: if it met `A`, it would meet `A` as well as
every member of `H`, contradicting (1.2).  Since it meets `A'` and is
disjoint from `A`, equation (1.4) forces `w in R_0`.

The preceding observation gives `|R_0|=2`; put `R=R_0`.  Then (1.6)
holds.  In particular, `R` meets every support-five model, so

\[
                              \mu_G(R)\ge6.             \tag{1.11}
\]

The support `A` is disjoint from `R`, so it gives a six-vertex model in
`G-R` and hence `mu_G(R)<=6`.  Thus `mu_G(R)=6`.

Finally, (1.1) says that every two-set misses some member of
`F_6(G)`.  Therefore `mu_G(P)<=6` for every two-set `P`, proving (1.7)
and alternative 2.  The proof selects an alternative according to the
strict dichotomy between (1.9) and (1.10); the two displayed conclusions
are not asserted to be logically incompatible after their auxiliary
conditions are forgotten.

For the final assertion, equation (1.4) gives
`A' subseteq A union {w}`.  Hence the assumed pair `P` is disjoint from
`A'`, while it still meets every member of `H`.  The support `A'` gives
`mu_G(P)<=6`, and the fact that `P` meets `F_5(G)` gives the reverse
inequality.  Thus `mu_G(P)=6`.  \(\square\)

## 2. Canonical exchange core

The preceding dichotomy has a fixed, support-independent formulation which
is useful for iteration.

### Theorem 2.1 (canonical exchange core)

In the setting of Theorem 1.1, let `T(H)` be the nonempty family of all
two-vertex transversals of `H`, and define

\[
 Z_{\mathcal H}=V(G)-\bigcup_{R\in\mathcal T(\mathcal H)}R.   \tag{2.1}
\]

Then:

1. `A subseteq Z_H`;
2. `G[Z_H]` contains no literal `K_5`;
3. if `A' subseteq Z_H` is any six-vertex `K_5`-model support, then

   \[
                    \tau(\mathcal H\cup\{A'\})>2,       \tag{2.2}
   \]

   so `A'` may replace `A`, and every member of `T(H)` is a private
   transversal for `A'` relative to `H`; and
4. every vertex `w notin Z_H` belongs to a two-vertex transversal `R` of
   `H` which is disjoint from `A` and satisfies

   \[
                    \mu_G(R)=6=\max_{|P|=2}\mu_G(P).    \tag{2.3}
   \]

Thus all support replacements inside the fixed induced subgraph
`G[Z_H]` preserve the same family of private pairs.  Leaving that subgraph
does not create a new uncontrolled case: the first outside vertex already
lies in a globally support-maximal private pair.

#### Proof

The family `T(H)` is nonempty by (1.8).  Since
`tau(H union {A})>2`, no member of `T(H)` meets `A`; hence
`A subseteq Z_H`, proving item 1.

If a five-set `K subseteq Z_H` induced a literal `K_5`, then
`K in F_5(G) subseteq H`.  Every member of `T(H)` would have to meet
`K`, while the definition of `Z_H` makes every such member disjoint from
`K`.  This contradiction proves item 2.

Let `A'` be as in item 3.  Every transversal of `H` of order at most two
is disjoint from `Z_H`, and hence from `A'`.  It cannot therefore be a
transversal of `H union {A'}`.  This proves (2.2).  The same observation
says that every member of `T(H)` meets `H` and avoids `A'`, which is the
asserted private-pair statement.

Finally let `w notin Z_H`.  By definition, some
`R in T(H)` contains `w`.  Item 1 makes `R` disjoint from `A`.
Then `R` meets `F_5(G)` and avoids the six-vertex support `A`, so
`mu_G(R)=6`; equation (1.1) makes this value globally maximal.
This proves item 4.  \(\square\)

## 3. Application to a length-two repaired contact

Use the canonical `3+1` configuration of
[`hc7_disjoint_k6minus_support6_bridge_augmentation.md`](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md):

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},
\]

where `Q={a_0,a_1,a_2,a_3}` is a clique, `xy` is an edge, `x` is
adjacent to `a_0,a_1,a_2`, and `y` is adjacent to `a_3`.

### Corollary 3.1 (length-two replacement)

Suppose that `a_3-w-x` is a path whose internal vertex `w` lies outside
`A`.  Then

\[
                         A'=Q\cup\{x,w\}               \tag{3.1}
\]

is a six-vertex `K_5`-model support.  It has both of the following labelled
models:

\[
 \{a_0\},\{a_1\},\{a_2\},\{a_3\},\{w,x\},             \tag{3.2}
\]

and

\[
 \{a_0\},\{a_1\},\{a_2\},\{x\},\{a_3,w\}.             \tag{3.3}
\]

If `A` belongs to the critical family in Theorem 1.1, then either the
critical family can be rebased onto `A'`, or a globally support-maximal
private pair for `A` contains `w`.  If the original private pair `P` for
`A` also avoids `w`, then the rebasing alternative retains the same pair
`P` as a private pair for `A'`.

#### Proof

For (3.2), the four singleton sets indexed by `Q` form a clique.  The edge
branch set `{w,x}` is adjacent to `a_0,a_1,a_2` through `x` and to `a_3`
through `w`.  For (3.3), the four singleton vertices
`a_0,a_1,a_2,x` form a clique.  The edge branch set `{a_3,w}` is adjacent
to the first three singletons through `a_3` and to `x` through `w`.
Thus both displays are labelled `K_5` models on the support (3.1).

Now `A-A'={y}` and `A'-A={w}`, so Theorem 1.1 applies.  \(\square\)

## 4. Exact contribution and limitation

The theorem supplies a legal exchange operation at the point where a
residual six-terminal crossing repairs one missing contact with a single
internal vertex.  It does not assert that repeated rebasing is acyclic.
Nor does a maximal private pair containing `w` automatically preserve the
old six-linkage or remain nonadjacent.  A complete argument still needs a
strict rank for repeated support exchanges, or a labelled regeneration
theorem after the private pair moves to `w`.
