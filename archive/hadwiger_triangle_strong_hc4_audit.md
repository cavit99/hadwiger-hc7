# Independent audit: triangle plus a four-colourable core

## Verdict

Theorem 1.1 of `hadwiger_triangle_strong_hc4_dichotomy.md` is **green**.
It uses exactly the proved (k=4) case of Holroyd's Strong Hadwiger
Conjecture and its recolouring has no hidden planarity or connectivity
assumption.

## The external input

Martinsson and Steiner prove the following statement for (k=4): if a
graph (H) is (4)-colourable and a set (X\subseteq V(H)) takes all
four colours in every proper (4)-colouring, then (H) has an
(X)-rooted (K_4)-minor, i.e. four disjoint connected pairwise adjacent
branch sets, each meeting (X).

Source: A. Martinsson and R. Steiner, *Strengthening Hadwiger's conjecture
for 4- and 5-chromatic graphs*, JCTB 164 (2024), 1--16,
<https://arxiv.org/abs/2209.00594>.

If the hypothesis holds, then (H) is automatically four-chromatic: a
colouring with at most three colours, regarded as a four-colouring with an
unused label, would violate it.  Thus there is no mismatch between the
paper's chromatic formulation and the formulation used in the note.

## Audit of the two branches

Let (T=q_1q_2q_3), (J=G-T), and

\[
 X=N_J(q_1)\cap N_J(q_2)\cap N_J(q_3).
\]

If (X) sees all four colours in every four-colouring, Strong HC4 gives an
(X)-rooted (K_4).  Every branch set contains a vertex adjacent to all
three (q_i), so the rooted model plus the three singleton (q_i) is
indeed a (K_7)-model.

Otherwise take a four-colouring whose colour-zero class (Z) misses
(X).  The class (Z) is independent.  For every
(u\in Z\cap N(q_1)), either (u) misses (q_2), or it sees (q_2) and,
because (u\notin X), misses (q_3).  Recolour the first kind with a
fresh colour (4), the second kind with a fresh colour (5).  There are
no conflicts inside (J): the recoloured set was independent and the two
colours were fresh.  Colour (q_1,q_2,q_3) by (0,4,5).  The definition
of the two kinds verifies all three triangle-to-core interfaces.  This is
a proper six-colouring.

Therefore

\[
  \chi(G-T)\le4
  \quad\Longrightarrow\quad
  \chi(G)\le6\ \text{ or }\ K_7\preccurlyeq G.
\]

In particular, a seven-chromatic (K_7)-minor-free graph satisfies
(chi(G-T)\ge5) for every triangle (T).

