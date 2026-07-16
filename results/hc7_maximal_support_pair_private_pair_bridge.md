# A globally maximal support pair with a private avoided model

**Status:** proved and independently internally audited in
[`hc7_maximal_support_pair_private_pair_bridge_audit.md`](hc7_maximal_support_pair_private_pair_bridge_audit.md).
This note aligns two existing support-six normalizations.  It does not
prove the support-six transversal theorem or `HC_7`.

## 1. Definitions and hypotheses

Let `G` be a finite seven-connected graph with no `K_7` minor.  For
`r in {5,6}`, let

\[
 \mathcal F_r(G)=\{V(\mathcal M):\mathcal M\text{ is a }K_5
      \text{-minor model in }G,\ |V(\mathcal M)|\le r\}.
\]

Thus `mathcal F_5(G)` is exactly the family of vertex sets of literal
`K_5` subgraphs.  For a two-vertex set `P`, put

\[
 \mu_G(P)=\min\{|V(\mathcal M)|:\mathcal M\text{ is a }K_5
      \text{-minor model in }G-P\},                    \tag{1.1}
\]

with value infinity when `G-P` has no `K_5` minor.

The proved
[literal-`K_5` transversal theorem](../results/hc7_global_literal_k5_transversal.md)
gives

\[
                         \tau(\mathcal F_5(G))\le2.     \tag{1.2}
\]

Assume for the remainder of the note the contradictory support-six
hypothesis

\[
                         \tau(\mathcal F_6(G))>2.       \tag{1.3}
\]

No chromatic or contraction-critical hypothesis is needed below.

## 2. The maximal-pair/private-pair bridge

### Theorem 2.1

Under (1.2)--(1.3), there are a nonempty family

\[
                 \mathcal C=\{A_1,\ldots,A_m\}
                    \subseteq\mathcal F_6(G)-\mathcal F_5(G)       \tag{2.1}
\]

and two-vertex sets `P_1,...,P_m` such that:

1. `mathcal C` is inclusion-minimal subject to

   \[
       \tau(\mathcal F_5(G)\cup\mathcal C)>2;            \tag{2.2}
   \]

2. every `A_i` has order six;
3. `P_i` is disjoint from `A_i` and meets every member of
   `mathcal F_5(G) union (mathcal C-{A_i})`;
4. every `P_i` is globally maximal for the support potential:

   \[
                  \mu_G(P_i)=6=\max_{|R|=2}\mu_G(R);     \tag{2.3}
   \]

5. the set-pairs `(A_i,P_i)` satisfy

   \[
       A_i\cap P_i=\varnothing,
       \qquad A_i\cap P_j\ne\varnothing\quad(i\ne j),  \tag{2.4}
   \]

   and consequently `m<=28`.

Thus every member of one bounded exact-six witness family has a private
pair which is simultaneously a transversal of every literal `K_5` and a
globally `mu_G`-maximal pair.

#### Proof

Put

\[
 \mathcal E=\mathcal F_6(G)-\mathcal F_5(G).
\]

Every member of `mathcal E` has order exactly six.  By (1.2)--(1.3),
there is an inclusion-minimal nonempty subfamily
`mathcal C subseteq mathcal E` such that

\[
 \tau(\mathcal F_5(G)\cup\mathcal C)>2.               \tag{2.5}
\]

This proves assertions 1--2.  Write
`mathcal C={A_1,...,A_m}`.  For each `i`, set

\[
 \mathcal H_i=\mathcal F_5(G)\cup(\mathcal C-\{A_i\}). \tag{2.6}
\]

Minimality of `mathcal C` gives `tau(mathcal H_i)<=2`, while (2.5) says
`tau(mathcal H_i union {A_i})>2`.

Choose a transversal `P_i^0` of `mathcal H_i` of order at most two.  It
must be disjoint from `A_i`: if `P_i^0 cap A_i` were nonempty, then
`P_i^0` would meet `A_i` as well as every member of `mathcal H_i`, contrary
to `tau(mathcal H_i union {A_i})>2`.

If `|P_i^0|<2`, enlarge it to a two-set `P_i` using vertices outside `A_i`.
This is possible because a seven-connected graph has at least eight
vertices, whereas `|A_i|=6`.  If it already has order two, put
`P_i=P_i^0`.  The resulting pair remains a transversal of `mathcal H_i`
and remains disjoint from `A_i`.  This proves assertion 3.

Since `mathcal F_5(G) subseteq mathcal H_i`, the pair `P_i` meets every
support-five model.  Hence `mu_G(P_i)>=6`.  The support `A_i` has order
six and is disjoint from `P_i`, so it supplies a model in `G-P_i` and
gives `mu_G(P_i)<=6`.  Therefore

\[
                              \mu_G(P_i)=6.              \tag{2.7}
\]

Finally, (1.3) says that no two-set is a transversal of
`mathcal F_6(G)`.  For every two-set `R`, some member of
`mathcal F_6(G)` is therefore disjoint from `R`, and consequently

\[
                              \mu_G(R)\le6.             \tag{2.8}
\]

Equations (2.7)--(2.8) prove assertion 4.

For distinct `i,j`, the support `A_i` belongs to `mathcal H_j`, so the
transversal `P_j` meets `A_i`.  Together with `A_i cap P_i=varnothing`,
this proves (2.4).  Bollobas's Two Families Theorem, with set-pair sizes
six and two, now gives

\[
                              m\le {8\choose6}=28.       \tag{2.9}
\]

This proves assertion 5. \(\square\)

### Remark 2.2 (relation to the established bound twenty-seven)

Equality in (2.9) forces, by the equality case of Bollobas's theorem, an
eight-set `X` for which

\[
                         \mathcal C={X\choose6}.         \tag{2.10}
\]

In particular `tau(mathcal C)=3`.  The separately proved,
computer-assisted
[nine-vertex support-six closure](../results/hc7_nine_vertex_support_six_closure.md)
excludes such a family in the present graph after placing `X` inside a
nine-set.  Such a nine-set exists: a seven-connected graph has at least
eight vertices, and the order-eight case would be `K_8` and hence contain
a `K_7` minor.  Thus that additional result sharpens `m<=28` to `m<=27`, just
as in the existing bounded-critical-kernel theorem.  The elementary bridge
proved here uses only the bound twenty-eight.

### Corollary 2.3 (equivalence of the live formulations)

For a seven-connected `K_7`-minor-free graph,

\[
 \tau(\mathcal F_6(G))>2
 \quad\Longleftrightarrow\quad
 \max_{|P|=2}\mu_G(P)=6.                               \tag{2.11}
\]

#### Proof

The forward implication is Theorem 2.1.  Conversely, if the maximum is
six, then every two-set `P` satisfies `mu_G(P)<=6`.  Thus every two-set is
disjoint from the support of some member of `mathcal F_6(G)`, so no
two-set is a transversal of that family. \(\square\)

## 3. Consequence for the existing labelled extraction

Fix any `i`, write `P_i={p,q}`, and let

\[
 \mathcal H_i=\mathcal F_5(G)\cup(\mathcal C-\{A_i\}),
 \qquad A=A_i,\qquad P=P_i,\qquad
                         \mathcal F=\mathcal H_i\cup\{A_i\}
\]

be the family furnished by Theorem 2.1.  It satisfies every hypothesis of
the proved
[private-pair extraction theorem](../results/hc7_support_six_private_pair_v_extraction.md):
`mathcal F subseteq mathcal F_6(G)`, `tau(mathcal F)>2`, and `P` is
disjoint from `A` while meeting every other member.  No critical-family
minimality is required by that theorem.

### Corollary 3.1 (additional models at a maximal private pair)

There are supports `B,C in mathcal H_i` such that

\[
 \begin{aligned}
  &P\cap B=\{p\},\qquad P\cap C=\{q\},\\
  &|A\cap B|\le4,\qquad |A\cap C|\le4.
 \end{aligned}                                         \tag{3.1}
\]

Moreover the proved
[dichotomy for additional models through a private pair](../results/hc7_private_pair_cross_arm_dichotomy.md)
applies to this same globally maximal pair.  Consequently exactly one of
the following holds.

1. There are such `B,C` for which `A,B,C` are pairwise separated in the
   small-support sense

   \[
    |U\cap V|\le\max\{|U|,|V|\}-2
       \quad(U,V\in\{A,B,C\},\ U\ne V).                \tag{3.2}
   \]

2. There are `k in {5,6}` and a `(k-1)`-set `X`, disjoint from `P`, for
   which the separated supports containing `p` and `q` are respectively
   `X union {p}` and `X union {q}`; for every `a in A cap X`, the two
   replacement supports

   \[
                  (A-\{a\})\cup\{p\},\qquad
                  (A-\{a\})\cup\{q\}                  \tag{3.3}
   \]

   also belong to `mathcal F`.

#### Proof

Equation (3.1) is Theorem 1.1 of the private-pair extraction note applied
to `G,mathcal F,A,P`.  The two alternatives are exactly Theorem 1.1 of
the linked dichotomy applied to the same data. \(\square\)

### Corollary 3.2 (bounded family of split-model normal forms)

For every `A_i in mathcal C`, choose a `K_5` model whose support is
`A_i`.  The proved
[support-six contraction dichotomy](../results/hc7_global_support_six_contraction_dichotomy.md)
applies with the globally maximal private pair `P_i`.  Consequently each
chosen model consists of four singleton branch sets and one two-vertex
branch set `x_i y_i`, with one of the four complementary deficiency
patterns in that theorem.  For each `i`, either `G/x_i y_i` is
seven-connected or splitting a separator of that contraction produces an
actual order-seven separation of `G` whose boundary contains `x_i,y_i`.

This conclusion holds separately for every member of the bounded family
`mathcal C`.  It does not assert that the two-vertex branch sets can be
chosen compatibly, that their contractions preserve connectivity
simultaneously, or that the resulting order-seven separations share an
induction parameter.

#### Proof

Theorem 2.1 says that `P_i` meets every literal `K_5` and that
`mu_G(P_i)=6`; the support `A_i` is disjoint from `P_i`.  These are exactly
the pair and model hypotheses of the linked contraction dichotomy. \(\square\)

## 4. Exact contribution and remaining gap

Theorem 2.1 removes one quantifier mismatch in the support-six programme:
every member of one bounded witness family has a private pair that is a
globally `mu_G`-maximal pair and a transversal of every literal `K_5` in
`G`.

It does **not** prove that an arbitrary globally maximal pair is private
for a member of a bounded critical kernel.  It also does not:

- align the two-vertex branch sets of `A,B,C`;
- make the three model supports disjoint;
- compose the three models into a `K_7` minor;
- produce a two-set of support height at least seven; or
- equip an order-seven separation with a pair- and model-preserving strict
  induction parameter.

Those are precisely the remaining extraction and simultaneous-composition
obligations in the
[support-six frontier](../active/hc7_support_six_frontier.md).
