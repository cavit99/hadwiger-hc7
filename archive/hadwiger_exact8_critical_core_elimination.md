# Eliminating the five-chromatic exact-eight boundary core

## 1. The seven-vertex critical-core lemma

### Lemma 1.1

Every 4-vertex-critical graph `Y` on seven vertices has a vertex `y` such
that `Y-y` contains a `K_4` minor.

### Finite proof and certificates

The complete unlabeled graph atlas has 1,044 simple graphs on seven
vertices.  Exact backtracking for three- and four-colourability leaves
the following seven 4-critical graphs.  In each row the vertices are
`0,...,6`; after the edge list, the displayed vertex is deleted and the
four following sets are a `K_4` model in the remainder.

\[
\begin{array}{c|l|l}
 &E(Y)& y;\text{ four branch bags}\\ \hline
0&01,02,03,04,12,16,26,34,35,45,56
 &1;\ 0|3|4|256\\
1&03,04,05,06,12,14,15,23,24,34,36,56
 &0;\ 1|2|4|356\\
2&01,03,04,13,14,23,24,25,26,36,45,56
 &0;\ 2|3|6|145\\
3&03,04,06,13,15,16,24,25,26,34,35,45
 &0;\ 1|3|5|246\\
4&04,05,06,12,13,16,23,25,26,34,35,45,46
 &0;\ 1|2|3|46\\
5&01,05,06,13,14,23,24,25,26,34,36,45,56
 &0;\ 2|3|4|56\\
6&01,02,05,06,12,13,16,23,24,34,35,45,46,56
 &0;\ 1|2|3|46.
\end{array}                                             \tag{1.1}
\]

Every nonsingleton bag in (1.1) is visibly connected.  Reading the edge
list checks all six interbag adjacencies, so the right column is a direct
certificate independent of the enumeration.

The companion program `exact8_gallai_core_atlas_probe.py` supplies the
exhaustiveness certificate.  It asserts the atlas totals `1253` overall
and `1044` at order seven; tests every order-seven graph by an exact
colouring backtrack; obtains exactly the seven rows above; and runs an
exact connected-branch-set search for each displayed deletion.  Its
output ends with

```text
atlas/order7 1253 1044
4critical cores 7
survivors []
```

The trust boundary is the standard complete graph-atlas data, the short
Python backtracking/minor search, and the Python runtime.  The edge lists
and branch bags in (1.1) make the positive half independently checkable
by hand.

## 2. The three-choice gate is four-colourable

### Theorem 2.1

Let `X` be the eight-vertex adhesion of a `K_7`-minor-free bilateral full
gate.  Then

\[
                              \chi(G[X])\le4.          \tag{2.1}
\]

### Proof

The uniform reserve lift gives

\[
                         \eta(G[X-x])\le4
                         \qquad(x\in X).              \tag{2.2}
\]

The established case `HC_5` makes every graph in (2.2) four-colourable,
so `chi(G[X])<=5`.  Suppose equality held.  Then `G[X]` would be
5-vertex-critical.  Gallai's theorem for a `k`-critical graph on at most
`2k-2` vertices makes `G[X]` a nontrivial join of two smaller critical
graphs.  At order eight the chromatic split `2+3` is impossible: its
factors would be `K_2` and an odd cycle, of odd total order.  Hence

\[
                         G[X]=K_1\vee Y               \tag{2.3}
\]

for a 4-critical seven-vertex graph `Y`.

By Lemma 1.1, some `Y-y` has a `K_4` model.  Adding the universal vertex
of (2.3) gives a `K_5` model in `G[X-y]`, contradicting (2.2).  Therefore
equality cannot hold and (2.1) follows.  QED.

This proves the conclusion sought in the invalid Kempe-star argument of
Theorem 7.2 in `hadwiger_c6_exact8_state_gate.md`, but by a different
route.  It does not repair that argument: a star supplied by property
`(*)` does not create the missing adjacencies among its leaf bags.

## 3. Remaining operation theorem

The bilateral adhesion is now unconditionally four-colourable.  The live
obstruction is therefore purely an extension-state obstruction: no
four-colour boundary partition extends compatibly across both full
shores, while every proper internal operation supplies an
endpoint-complete six-colour transition.  The next theorem must turn
three such incompatible transition choices into either a common boundary
state or a reserve-core `K_5` model; no five-chromatic boundary branch
remains.
