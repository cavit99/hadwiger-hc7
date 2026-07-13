# Two-defect rooted face and portal-capture closure

## Status

This note closes one of the two exact low-portal residues left by the
audited palette-to-label theorem.  In the two-defect singleton shell, the
five canonical witnesses either give a literal `K_7`, or they all lie on
one face of a fixed 4-connected planar remainder.  If an ordinary portal
class is captured by the two deficient witnesses, the nested-triangle
theorem then gives a literal `K_7` or one global two-apex pair.

Thus the portal-capture alternative is empty in a hypothetical minimal
`HC_7` counterexample.  The only remaining two-defect residue is that
deleting the two deficient witnesses disconnects the bipartite bag.

## 1. Setup

Use the spanning singleton shell of
`../results/hc7_near_k7_palette_label_alignment.md` with `k=7`.  Write

\[
 S=\{b_1,\ldots,b_5\},\qquad
 J=\{s,t\},\qquad O=S-\{b_s,b_t\}.
\]

Assume `G` is seven-connected and let `x_s,x_t` be the two distinct
witnesses in one bipartition class supplied by Theorem 2.3 there.  Thus

\[
\begin{array}{c|cc|c}
 &b_s&b_t&O\\ \hline
 v   &0&0&1\\
 x_s &0&1&1\\
 x_t &1&0&1
\end{array}                                                \tag{1.1}
\]

where `1` means adjacency to every vertex in the indicated set.  The
vertices `b_s,b_t` are also complete to `O`, because `S` is a clique.

## Theorem 2.1 (five-root facial alternative)

Either `G` has a `K_7` minor, or `H=G-O` is planar and

\[
                 v,b_s,b_t,x_s,x_t                         \tag{2.1}
\]

all lie on the boundary of one face in the unique plane embedding of
`H`.

### Proof

Deleting the triangle `O` from a seven-connected graph leaves a
4-connected graph `H`.  Every vertex in (2.1) is adjacent to all three
vertices of `O`.

Apply the rooted-`K_4` theorem to any four of the five displayed roots in
`H`.  A rooted `K_4` model, together with the three singleton bags of
`O`, is a literal `K_7` model.  Hence, in the target-free branch, no
four-subset has a rooted `K_4`.  The rooted theorem says that `H` is
planar and each four-subset is cofacial.

Fix the four-set `v,b_s,b_t,x_s` and its face `F`.  The set
`v,b_s,b_t,x_t` lies on a face `F'`.  Since `H` is 4-connected it is
3-connected, so two distinct faces share at most two vertices.  The
faces `F,F'` share the three vertices `v,b_s,b_t`; hence `F=F'`.  This
proves (2.1).  QED.

## Theorem 3.1 (captured ordinary portal closes)

Suppose, for some `b_i in O`,

\[
                         P_i=N_B(b_i)=\{x_s,x_t\}.          \tag{3.1}
\]

Then `G` has a `K_7` minor or `G` is two-apex.  Consequently (3.1) is
impossible in a `K_7`-minor-free minimal counterexample to `HC_7`.

### Proof

Write `O={q_1,q_2,q_3}` with `q_3=b_i`.  Put `H=G-O`.  The complete
neighbourhood of `q_3` in `H` is

\[
             N_H(q_3)=\{v,b_s,b_t,x_s,x_t\}.               \tag{3.2}
\]

Indeed, `q_3` sees `v` because its label is not deficient, sees `b_s,b_t`
inside the singleton clique, and its neighbours in `B` are exactly those
in (3.1).  There are no other vertices in the spanning shell.

Every vertex in (3.2) is adjacent to both `q_1,q_2`: this is immediate
for `v,b_s,b_t`, and follows from (1.1) for `x_s,x_t`.  Therefore

\[
              N_H(q_3)\subseteq N_H(q_1)\cap N_H(q_2).     \tag{3.3}
\]

The nested neutral-triangle rooted-model theorem in
`../results/hc7_near_k7_nested_triangle_rooted_model.md` now gives a
`K_7` minor or proves that `G-{q_1,q_2}` is planar.  The latter is one
literal global two-apex pair.  In a minimal counterexample it yields a
6-colouring by the Four Colour Theorem plus two fresh colours.  QED.

## Corollary 4.1 (exact surviving two-defect residue)

Assume every singleton portal set has order at least two and `G` is a
`K_7`-minor-free minimal counterexample.  Then

\[
                         B-\{x_s,x_t\}\text{ is disconnected}. \tag{4.1}
\]

### Proof

Corollary 2.5 of the palette-to-label theorem says that either (4.1)
holds or an ordinary portal set equals `{x_s,x_t}`.  Theorem 3.1 excludes
the latter.  QED.

The next P4 task is therefore not portal capture but a faithful exchange
across the actual components of `B-{x_s,x_t}`.  Theorem 2.1 fixes one
planar remainder and one face containing the five operation witnesses;
any rural outcome from that exchange must use this same embedding rather
than choose a new local apex pair.
