# Independent audit: path-intersection separator excess

**Verdict: GREEN.**  This audit checks source revision

```text
a857c7881308333eedca799bfe0d22b458c4f711d43ccacaeeb56f8dfbd46676
```

of `results/hc7_small_path_intersection_lobe.md`.  The theorem is valid with
its stated hypotheses and scope.  The audit was carried out independently of
the proof draft, with a second independent check of the contraction and
pullback step.  Finite local tests covered all 128 relevant lost-contact
subsets and 502 disconnected path-intersection patterns.  These tests are
supporting checks; the verdict rests on the written argument below.

## 1. Setup and disjointness

The seven boundary vertices are partitioned exactly as

\[
S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
\qquad |D|=3,\quad |E|=2.
\]

The sets `D` and `E`, and also `{r,z}` in the `Pi_B` case, are independent
because they are equality blocks of a proper colouring.  The path has no
boundary vertex other than `r,z`.  Since it avoids `C_2` and
`R=C_1-V(P)`, each family of branch sets used in Lemma 2.1 is pairwise
vertex-disjoint.

The set `T=V(P) cap V(C_1)` need not be consecutive on the path.  This is
harmless.  Splitting after its last vertex puts all of `T` on the `r`-side;
splitting before its first vertex puts all of it on the `z`-side.  Because
`C_1` is connected and both `R` and `T` are nonempty, there is an edge
between them.

## 2. The four `Pi_A` contractions

For `Lambda subseteq E union {r}`, the proof uses

\[
R\cup D,\qquad C_2\cup E,\qquad P_r,\qquad P_z.
\]

All four sets are connected.  Their six pairwise adjacencies are:

1. `R union D`--`P_r`: an `R`--`T` edge;
2. `R union D`--`P_z`: a retained `R`--`z` boundary contact;
3. `C_2 union E`--`P_r`: a `C_2`--`r` contact;
4. `C_2 union E`--`P_z`: a `C_2`--`z` contact;
5. `R union D`--`C_2 union E`: a `C_2` contact to any member of `D`;
6. `P_r`--`P_z`: the path splitting edge.

The other three containments are exact symmetric variants:

* for `Lambda subseteq E union {z}`, assign `R` to `D` and put `T` on
  the `z`-side;
* for `Lambda subseteq D union {r}`, assign `R` to `E` and put `T` on
  the `r`-side; and
* for `Lambda subseteq D union {z}`, assign `R` to `E` and put `T` on
  the `z`-side.

In each case `R` retains every contact in its assigned block and the
boundary endpoint on the opposite path side.  The full subgraph `C_2`
supplies all remaining boundary contacts.  The source does not need an edge
between `C_1` and `C_2`, and correctly does not assume one.

## 3. The two `Pi_B` contractions

When `Lambda cap D` is empty, the three branch sets are

\[
R\cup D,\qquad C_2\cup E,\qquad V(P).
\]

They are connected and pairwise adjacent respectively through a
`C_2`--`D` contact, an `R`--`T` edge, and a `C_2`--`r` contact.  If
`Lambda cap E` is empty, interchanging `D` and `E` gives the same proof.

## 4. Proper minor, exact pullback and gluing

Every contraction is a proper minor operation.  In particular, each
boundary-block branch set contains a nonempty connected host subgraph and
at least two boundary-block vertices, so at least one edge of a spanning
tree is contracted.

The representatives form a `K_4` in the `Pi_A` case and a `K_3` in the
`Pi_B` case.  Hence a six-colouring of the proper minor assigns distinct
colours to distinct boundary-block representatives.  Pulling those colours
back to the literal boundary is proper because:

* every equality block is independent;
* every edge from a boundary block to the untouched shore became incident
  with its representative; and
* clique adjacency distinguishes all different blocks.

Thus the pullback gives the exact partition, not merely a coarsening.  The
block-colour bijection on one closed shore extends to a permutation of all
six colours and makes the two closed-shore colourings agree vertex by vertex
on `S`.  Since there is no edge between the open shores, they glue to a
six-colouring of `G`.  The contrapositive portal-allocation conclusions are
therefore valid.

## 5. Separator identity and excess

With the standard external-neighbourhood convention,

\[
U=N_G(R)-S,
\qquad
S-\Lambda=N_G(R)\cap S.
\]

These sets are disjoint and give the exact identity

\[
N_G(R)=U\mathbin{\dot\cup}(S-\Lambda),
\qquad
|N_G(R)|=|U|+7-|\Lambda|.
\]

The opposite open shore `B` is nonempty and has no edge to `R subseteq A`.
Consequently `N_G(R)` separates nonempty vertex sets.  Seven-connectivity
gives `|N_G(R)|>=7`, equivalently `|U|>=|Lambda|`.

In `Pi_A`, failure of all four allocation containments forces
`|Lambda|>=2`; every empty or singleton subset is contained in one of the
four displayed sets.  In `Pi_B`, `Lambda` meets both disjoint blocks `D,E`,
again giving order at least two.  Therefore

\[
\varepsilon(R)=|U|-|\Lambda|=|N_G(R)|-7\ge0.
\]

Equality is equivalent to `|N_G(R)|=7`, and the preceding separation is
then an actual nontrivial order-seven separation.

## 6. Two-attachment classification

If `|U|<=2`, the inequalities force `|U|=|Lambda|=2`.  For `Pi_A`, the
two-subsets contained in none of

\[
D\cup\{r\},\quad D\cup\{z\},\quad
E\cup\{r\},\quad E\cup\{z\}
\]

are exactly `{r,z}` and `{d,e}` with `d in D,e in E`.  For `Pi_B`, a
two-set meeting both `D` and `E` has exactly that latter form.  Corollary
4.1 is correct.

## 7. Trust boundary

The theorem does not prove that the residual `R` is connected in every
first-entry configuration, does not handle a path meeting both named full
subgraphs, and does not show that positive separator excess decreases under
a further operation.  An exact seven-separator returned at excess zero is
not asserted to carry compatible colourings on its two shores.  No finite
test is used to infer an unbounded statement.
