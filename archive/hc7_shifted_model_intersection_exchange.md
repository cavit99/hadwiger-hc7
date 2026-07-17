# Intersection exchange for the shifted regenerated model

**Status:** written proof, independent audit pending.  This note compares
the exact straddling model from
[`hc7_shifted_pair_regeneration.md`](hc7_shifted_pair_regeneration.md)
with the original mixed-shore support-six model.  It does not prove
`HC_7`.

## Theorem 1.1

Let `S,U,V,s,x,v` be in the endpoint-rigid mixed-shore setup.  Suppose the
original support-six `K_5` model in `G-{s,x}` has branch sets

\[
 \{u_1\},\ldots,\{u_k\},\quad
 \{w_1\},\ldots,\{w_{4-k}\},\quad\{v,t\},             \tag{1.1}
\]

where `k in {2,3}`, the vertices `u_i` lie in `U`, and `t,w_j` lie in
`S-{s,x}`.  Write

\[
 A_0=\{u_1,\ldots,u_k,w_1,\ldots,w_{4-k},v,t\}        \tag{1.2}
\]

for its support.

Let `y in S` be the common missing boundary contact of all components of
`V-v`, and put `X=V-{v}`.  Suppose a regenerated support-six model in
`G-{s,v}` has the straddling form

\[
 \{q_1\},\ldots,\{q_h\},\quad
 \{r_1\},\ldots,\{r_{4-h}\},\quad\{z,t'\},            \tag{1.3}
\]

from Theorem 2.1 of the linked note.  Thus `1<=h<=3`, the vertices `r_j,t'`
lie in `S-{s}`, and for some orientation `{W,W'}={U,X}` one has

\[
                         q_i\in W,\qquad z\in W'.      \tag{1.4}
\]

Let `A_1` be the support in (1.3).  Then exactly one of the following
holds.

1. The two supports are separated by at least two vertices on each side:

   \[
                         |A_0\cap A_1|\le4.             \tag{1.5}
   \]

2. The singleton rows of the regenerated model lie in `U`, one has
   `h=k`, and for a vertex `z in X`,

   \[
                         A_1=(A_0-\{v\})\cup\{z\}.      \tag{1.6}
   \]

In particular, the only nonseparated return is a literal one-vertex
replacement of the old open-shore endpoint `v` by a vertex of `X`.

### Proof

The old support has exactly `k` vertices in `U`, exactly one vertex in
`V`, namely `v`, and exactly

\[
                              5-k                     \tag{1.7}
\]

vertices in `S`, namely `w_1,...,w_{4-k},t`.  It has no vertex in `X`.

Suppose first that `W=X`.  The `h` vertices `q_i` contribute nothing to
`A_0 cap A_1`; the opposite-side vertex `z in U` contributes at most one;
and the `5-h` boundary vertices of `A_1` meet at most all `5-k` boundary
vertices of `A_0`.  Therefore

\[
                   |A_0\cap A_1|\le1+(5-k)=6-k\le4.    \tag{1.8}
\]

This is outcome 1.

It remains that `W=U` and `z in X`.  The vertex `z` again contributes
nothing to the intersection.  Hence

\[
 |A_0\cap A_1|
       \le \min\{h,k\}+\min\{5-h,5-k\}.               \tag{1.9}
\]

For `h in {1,2,3}` and `k in {2,3}`, the right side of (1.9) is five
only when `h=k`; in every other case it is at most four.  Thus failure of
outcome 1 forces `h=k` and equality in both intersection terms.  The
`U`-vertices in (1.3) are then exactly `u_1,...,u_k`, while its boundary
vertices are exactly `w_1,...,w_{4-k},t`.  Since its sixth vertex `z`
lies in `X` and the old sixth vertex is `v`, equation (1.6) follows.
The two outcomes are mutually exclusive, completing the proof.  \(\square\)

## Corollary 1.2 (the nonseparated branch enters the audited exchange)

Assume additionally that `A_0` is a member of the critical support family
and that `P={s,x}` is its private globally support-maximal pair in the
sense of
[`hc7_one_vertex_support_exchange.md`](../results/hc7_one_vertex_support_exchange.md).
In outcome 2 of Theorem 1.1, the hypotheses of that one-vertex exchange
hold with

\[
                  A_0-A_1=\{v\},\qquad A_1-A_0=\{z\}.                \tag{1.10}
\]

Moreover `P` avoids `z`, since `z in X subseteq V-S`.  Consequently the
exchange theorem gives one of the following two rigorous returns.

1. The critical support family can be rebased from `A_0` to `A_1`, and
   the same pair `{s,x}` remains private and globally support-maximal.
2. A globally support-maximal private pair for `A_0` contains `z`.

### Proof

Equation (1.10) is (1.6), and `z` lies outside the boundary `S` containing
`s,x`.  The statement is therefore exactly Theorem 1.1, including its
final preserved-pair clause, of the cited audited result.  \(\square\)

## Exact contribution

This theorem removes arbitrary overlap from the regenerated-model problem.
The old and new supports either have intersection at most four, which is
the separated-support regime of the global support-six programme, or the
new model performs one named support exchange and immediately invokes an
existing audited exchange theorem.  What remains is to compose the
separated-support branch or prove that repeated one-vertex rebasing cannot
cycle without producing the global two-vertex transversal.
