# A seven-connected realization of the exact-eight parity obstruction

## 1. Result

Let

\[
                         X=W_5\mathbin{\dot\cup}3K_1           \tag{1.1}
\]

be the eight-vertex boundary from the antipodal/antipodal exact-eight
gate.  Split its proper at-most-six-block equality states into the even
and odd block-count families.

### Theorem 1.1

There is a finite seven-connected graph `G*` with `G*-X` equal to two
anticomplete connected components `C_even,C_odd`, both full to `X`, such
that

1. the exact six-colour extension relations of the two closed shores are
   respectively the even and odd state families;
2. `G*` is not six-colourable; and
3. `G*` has an explicit `K_7` model.

Consequently, neither actual graph realizability nor seven-connectivity,
even combined with bilateral fullness and every exact-block parity
condition, breaks the parity obstruction.  A positive `HC_7` theorem
must also use `K_7`-minor-freeness (or an equivalent forbidden-model
consequence).

## 2. The base parity shores

Proposition 5.1 of `hadwiger_c6_exact8_state_gate.md` gives closed shores
`H_even,H_odd` with the exact even/odd relations, connected open
interiors, and collective fullness to `X`.  Take their open interiors
disjoint and identify their copies of `X`.

Write the wheel boundary as

\[
                         B=\{z,r_1,r_2,r_3,r_4\},              \tag{2.1}
\]

where `z` is universal in `B`, the rim edges form the four-cycle
`r_1r_2r_3r_4r_1`, and the two missing pairs are

\[
                         r_1r_3,\qquad r_2r_4.                 \tag{2.2}
\]

Choose one isolated boundary vertex `t` from the `3K_1` part and an old
interior vertex `c` of the even shore.

## 3. A colouring-neutral displayed packet

Add the following vertices and edges to the even open side.

* Add `q_13` adjacent to `r_1,r_3`, and `q_24` adjacent to `r_2,r_4`.
* Add a vertex `a`.  For every `b in B`, add `p_b` and the path
  `a-p_b-b`.
* Add `m` and the path `t-m-a`.
* For `q in {q_13,q_24}`, add `h_q` and the path `q-h_q-a`.
* Add `n` and the path `a-n-c`.

Call the augmented even shore `H'_even`.

### Lemma 3.1

The exact boundary extension relation of `H'_even` is still the even
family, and its open interior is connected and full to `X`.

#### Proof

Start with any extending colouring of `H_even`.  Choose an arbitrary
colour for `a`.  Each `q_ij` avoids the at most two colours on its two
boundary neighbours.  Each `p_b` and `m` avoids the at most two colours
on the ends of its length-two path.  After the colours of `a,q_13,q_24`
are chosen, each `h_q` avoids at most two colours; similarly `n` avoids
the colours on `a,c`.  Six colours are more than enough at every step.
Thus every old extension extends over the new gadget.  Restriction gives
the converse.

All new open vertices join `a`, directly or through one middle vertex,
and `a` joins the old open interior through `n,c`.  Hence the augmented
open interior is connected.  The old fullness contacts are untouched.
QED.

### Lemma 3.2 (literal `K_7` before amplification)

The union of `H'_even` and the odd open shore contains a `K_7` model.

#### Proof

Use five leaf bags rooted at `B`:

\[
 \{r_1,q_{13}\},\quad \{r_3\},\quad
 \{r_2,q_{24}\},\quad \{r_4\},\quad \{z\}.                    \tag{3.1}
\]

The two subdivided missing pairs supply the two absent adjacencies; all
other leaf--leaf adjacencies are literal edges of the wheel `W_5`.

Use as the sixth bag

\[
 A=\{t,m,a\}\cup\{p_b:b\in B\}\cup\{h_{q_{13}},h_{q_{24}}\}.
                                                                    \tag{3.2}
\]

It is connected, and `p_b-b` makes it adjacent to the leaf rooted at
`b`.  Finally take the entire odd open interior as the seventh bag `R`.
It is connected and disjoint from (3.1)--(3.2).  Fullness gives an edge
from `R` to each root in `B` and an edge from `R` to `t`.  Thus `R` is
adjacent to all first six bags.  The seven displayed bags form `K_7`.
QED.

The paths added above are deliberately colouring-neutral.  The model is
therefore not smuggled in by imposing a new boundary inequality.

## 4. False-twin connectivity amplification

Replace every open-side vertex `u` in both shores by an independent set

\[
                              T_u\quad\text{of order }7.        \tag{4.1}

For every old open-side edge `uv`, add all edges between `T_u,T_v`.
For every old edge `xu` with `x in X`, join `x` to all of `T_u`.
Keep the boundary `X` unchanged.  Call the resulting graph `G*`.

### Lemma 4.1 (extension relations are preserved)

A boundary colouring extends over an amplified shore if and only if it
extends over the corresponding unamplified shore.

#### Proof

An old colouring extends by giving every member of `T_u` the old colour
of `u`.  Conversely, from a colouring of the amplified shore select one
representative of every `T_u`.  Complete adjacency between twin classes
and complete boundary-to-class adjacency make the selected colours a
proper colouring of the old shore.  QED.

### Lemma 4.2 (`G*` is seven-connected)

#### Proof

Delete at most six vertices.  Every twin class `T_u` still contains a
vertex.  Since each unamplified open interior was connected, each
remaining amplified open side is connected by selecting one survivor
from every class along old paths.

At least two vertices of the eight-set `X` remain.  For every remaining
boundary vertex `x` and on each side, old fullness supplied an open
neighbour class; that class still has a survivor.  Thus every remaining
boundary vertex joins both connected open sides.  The entire remaining
graph is connected.  No set of at most six vertices is a cut, proving
seven-connectivity.  QED.

Selecting one representative from each twin class used in (3.1)--(3.2)
preserves the explicit `K_7` model of Lemma 3.2.  Lemma 4.1 preserves the
disjoint parity extension relations, so the glued graph remains non-six-
colourable.  This completes the proof of Theorem 1.1.

## 5. Trust boundary

The amplification introduces many redundant twins.  Hence `G*` is not
minor-critical and does not satisfy the internal one-step novelty of a
minimal counterexample.  It intentionally contains `K_7`.  The theorem
therefore refutes only arguments using

\[
 \text{seven-connectivity + bilateral fullness + parity state data}
\]

without the forbidden-minor or proper-minor geometry.  The live positive
target must use at least one of those two remaining inputs.
