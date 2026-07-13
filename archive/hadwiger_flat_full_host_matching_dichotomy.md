# Flat two-layer full-host dichotomy

## Status

This note closes the full **literal edge-carrier** cell left open in
Section 6 of `hadwiger_seven_view_state_cocycle_exchange.md`.  The result
is uniform in the number of carriers and does not require a canonical
proper-minor colouring.  It also gives the exact residual for connected
two-shore carriers.

The central point is that a maximum matching of cross-nonedges does more
than test the separated-palette colouring.  If its single unmatched state
has the right type, it colours the boundary.  If every maximum matching
has the wrong exposed type, the alternating-reachability minimum vertex
cover supplies an explicit labelled clique model.

## 1. Setup

Let `n>=4`.  There are boundary vertices `a,b,c` with

\[
             bc\in E(F),\qquad ab,ac\notin E(F),                 \tag{1.1}
\]

and vertices

\[
             X=\{x_1,\ldots,x_n\},\qquad
             Y=\{y_1,\ldots,y_n\}.                              \tag{1.2}
\]

Both `X` and `Y` induce cliques.  Each index has a type `t_i in {0,1}`.
The following boundary edges are required:

\[
\begin{array}{c|cc}
t_i&x_i&y_i\\ \hline
0&a,b&b,c\\
1&b,c&a,c.
\end{array}                                                       \tag{1.3}
\]

In addition, the rigidity argument which produces these rows gives the
forced nonedges

\[
          t_i=0\Longrightarrow cx_i\notin E(F),\qquad
          t_i=1\Longrightarrow by_i\notin E(F).                  \tag{1.4}
\]

Arbitrary further edges are allowed except where (1.1) and (1.4) forbid
them.  In particular, the cross-edges between `X` and `Y` are arbitrary.

Define the bipartite **cross-nonedge graph** `M` with parts `X,Y` by

\[
       x_i y_j\in E(M)\quad\Longleftrightarrow\quad
       x_i y_j\notin E(F).                                      \tag{1.5}
\]

Write `nu(M)` for its matching number.

## 2. Full-host theorem

### Theorem 2.1 (matching-or-labelled-clique dichotomy)

Every graph `F` satisfying (1.1)--(1.5) has one of the following two
outcomes:

1. `F` is properly `(n+2)`-colourable;
2. `F` contains a `K_{n+3}` minor.

The assertion holds for every type word, homogeneous or mixed.

#### Proof

We distinguish the matching number of `M`.

**Perfect compatibility.**  If `nu(M)=n`, take a perfect matching of
cross-nonedges.  Give each matched pair one colour.  This properly colours
`X union Y` with `n` colours.  Give `a,b` one new colour and `c` a second
new colour.  Equations (1.1) and (1.5) show that this is a proper
`(n+2)`-colouring of all of `F`.

**Co-rank at least two.**  Suppose `nu(M)<=n-2`.  By Konig's theorem,
`M` has a vertex cover `C` of order `nu(M)`.  Its complement in
`X union Y` is a clique of `F`, because it contains no cross-nonedge; its
order is

\[
                  2n-|C|=2n-\nu(M)\ge n+2.                    \tag{2.1}
\]

Choose `n+2` singleton branch sets in that clique.  The connected branch
set `{b,c}` is adjacent to every one of them: `b` sees every `x_i` and
`c` sees every `y_i` by (1.3).  These are the branch sets of a
`K_{n+3}` minor.

It remains that `nu(M)=n-1`.  Fix a maximum matching.  It leaves exactly
one vertex `x_u` of `X` and one vertex `y_v` of `Y` unmatched.

If `t_u=0`, colour every matched nonedge pair with one colour, and give
the two unmatched vertices distinct colours.  This uses `n+1` colours on
`X union Y`.  Give `c` the colour of `x_u`, and give `a,b` the one fresh
colour.  This is proper by (1.1) and the first forced nonedge in (1.4).
Similarly, if `t_v=1`, give `b` the colour of `y_v` and give `a,c` the
fresh colour.  The second forced nonedge in (1.4) makes this proper.

We may therefore assume that no maximum matching leaves a type-zero
vertex of `X` unmatched or a type-one vertex of `Y` unmatched.  (It is
enough below to use the first half of this assumption.)

Starting at the unmatched vertex `x_u`, let `Z_X subseteq X` and
`Z_Y subseteq Y` be the vertices reachable by alternating paths, where
the first edge is outside the fixed maximum matching.  Flipping along an
alternating path ending in `Z_X` produces a maximum matching leaving its
last `X`-vertex unmatched.  Hence every vertex of `Z_X` has type one.

The standard alternating-path proof of Konig's theorem gives the minimum
vertex cover

\[
                 C=(X-Z_X)\mathbin\cup Z_Y,                    \tag{2.2}
\]

of order `n-1`.  Consequently

\[
                 K=Z_X\mathbin\cup(Y-Z_Y)                     \tag{2.3}
\]

is a literal clique of `F` of order `n+1`: within each layer this follows
from (1.2), and between the layers it follows because no edge of `M` has
both ends outside the cover (2.2).

If every type were one, the unmatched `y_v` would already have triggered
the preceding colouring.  Thus choose an index `r` of type zero.  Since
every member of `Z_X` has type one, `x_r` is outside `K`.  Use the
`n+1` singleton vertices of `K` as branch sets, together with

\[
                    A'=\{a,b,x_r\},\qquad C'=\{c\}.             \tag{2.4}
\]

The set `A'` is connected because a type-zero `x_r` sees both `a` and
`b`.  It is adjacent to every `x_i in Z_X` through the `X` clique.  It is
adjacent to every `y_j in Y-Z_Y`: if `t_j=0`, use `by_j`, and if `t_j=1`,
use `ay_j`.  The singleton `C'` sees every `y_j`, and it sees every
`x_i in Z_X` because all these indices have type one.  Finally `A'` and
`C'` are adjacent through `bc`.  Thus (2.3)--(2.4) form a
`K_{n+3}` model.  This exhausts all cases.  \(\square\)

### Corollary 2.2 (the rigid edge-carrier cell is closed)

In the flat branch of Theorem 5.2 of
`hadwiger_seven_view_state_cocycle_exchange.md`, retain every additional
intercarrier edge of the full host.  The switched endpoints satisfy
(1.1)--(1.4), and the two layers are cliques.  Therefore the full host is
either `(n+2)`-colourable or contains a `K_{n+3}` minor.

For `n=4`, a non-six-colourable `K_7`-minor-free host cannot realize the
rigid literal-edge carrier cell at all.  No canonical-deletion hypothesis
is needed.

### Theorem 2.3 (reserved-connector minimum-cover strengthening)

In the setup of Theorem 2.1, assume additionally that every paired
diagonal `x_i y_i` is an edge, as it is for a literal edge carrier, and
that `nu(M)=n-1`.  Then either a maximum matching exposes a type-zero
`X` vertex or a type-one `Y` vertex, giving the colouring in Theorem 2.1,
or there is a minimum cover `C` for which the complement clique `K` has a
rooted completion that keeps `{b,c}` as one reserved branch set.

More precisely, fix a maximum matching and form the alternating sets
`Z_X,Z_Y` from its unmatched `X` vertex.  Put

\[
 C=(X-Z_X)\cup Z_Y,\qquad
 K=Z_X\cup(Y-Z_Y),                                  \tag{2.5}
\]

and

\[
 R=\{a\}\cup(X-Z_X),\qquad W=\{b,c\}.             \tag{2.6}
\]

If no favourable maximum matching exists, then `R` and `W`, together
with the `n+1` singleton vertices of `K`, form a `K_{n+3}` model.  In
particular, `R subseteq C union {a}` is the requested connected branch
set adjacent to both the complement clique and the reserved connector.

#### Proof

As in Theorem 2.1, every vertex of `Z_X` has type one.  If there were no
type-zero index, the unmatched `Y` vertex of the fixed maximum matching
would be type one and would give the favourable exposed state.  Hence
there is a type-zero index `r`.  Its vertex `x_r` lies in `X-Z_X`.

The set `X-Z_X` is a nonempty subset of the clique `X`, and `a` is
adjacent to `x_r`; therefore `R` is connected.  It is adjacent to every
vertex of `Z_X` through the `X` clique.  Let `y_j in Y-Z_Y`.  If `t_j=1`,
then `ay_j` is a row edge.  If `t_j=0`, then `x_j notin Z_X`, because all
vertices of `Z_X` have type one; hence `x_j in R`, and the diagonal
carrier edge `x_jy_j` joins `R` to `y_j`.  Thus `R` is adjacent to all of
`K`.

The bag `W` is connected.  It is adjacent to every `X` vertex through
`b` and every `Y` vertex through `c`, so it meets every singleton bag in
`K`; it also meets `R` through `bx_r`.  Disjointness follows from (2.5),
and the claimed clique model follows. \(\square\)

The diagonal hypothesis is exactly what upgrades the more general model
`{a,b,x_r},{c}` in Theorem 2.1 to the reserved-connector model
`R,{b,c}`.  Without it, a type-zero vertex `y_j in Y-Z_Y` could be
anticomplete to `X-Z_X` and need not meet `R`.

This qualification is sharp already for `n=4`.  With type word `0001`,
let the cross-nonedge relation consist of

\[
 x_0y_0,\ x_0y_3,\ x_1y_0,\ x_1y_1,\ x_2y_0.
\]

It has matching number three and no maximum matching exposes a type-zero
`X` vertex or type-one `Y` vertex.  For the matching
`x_0y_3,x_1y_1,x_2y_0`, one has `Z_X={x_3}` and `Z_Y=emptyset`; the
candidate `R={a,x_0,x_1,x_2}` is anticomplete to the type-zero vertex
`y_0`.  The failure uses the missing diagonal contact `x_0y_0`.  The
more general branch sets of Theorem 2.1 still work because they place `b`
with `a`.

## 3. Connected two-shore form

Replace every `x_i,y_i` by disjoint nonempty connected shores `X_i,Y_i`.
Assume the two labelled families are pairwise adjacent within each family,
and interpret (1.3) as shore-to-boundary contact.  Put an edge in `M`
exactly when the corresponding two shores are anticomplete.

### Theorem 3.1 (two-shore state dichotomy)

One of the following holds:

1. `nu(M)=n` (perfect compatible transport);
2. `nu(M)=n-1` and some maximum matching exposes either a type-zero
   `X`-shore or a type-one `Y`-shore;
3. the shores and `a,b,c` contain a labelled `K_{n+3}` model.

#### Proof

For `nu(M)<=n-2`, repeat the minimum-cover proof of Theorem 2.1, treating
each connected shore outside the cover as one branch set and adjoining
`{b,c}`.

For `nu(M)=n-1`, suppose outcome 2 fails.  Repeat the alternating-path
construction (2.2).  The shores indexed by `Z_X union (Y-Z_Y)` give
`n+1` pairwise adjacent connected branch sets.  Choose type-zero `r` and
replace (2.4) by

\[
          A'=X_r\mathbin\cup\{a,b\},\qquad C'=\{c\}.            \tag{3.1}
\]

All connectivity and adjacency checks in Theorem 2.1 use only the
labelled contacts (1.3), so they remain valid.  If there is no type-zero
index, every unmatched `Y`-shore has type one and outcome 2 holds.  \(\square\)

### Corollary 3.2 (paired-shore reserved-connector lift)

In Theorem 3.1, assume in addition that each paired pair `X_i,Y_i` is
adjacent, as it is when they are the two shores of one connected carrier.
In the co-rank-one proof of outcome 3, the model can be chosen with the
reserved branch set `W={b,c}` and

\[
 R=\{a\}\cup\bigcup_{i:\,X_i\notin Z_X}X_i.        \tag{3.2}
\]

Indeed, the `X_i` in the union are pairwise adjacent connected sets and
include a type-zero shore meeting `a`, so `R` is connected.  It meets
every `Z_X` shore through the within-family contacts.  A shore
`Y_j notin Z_Y` meets `a` when `t_j=1`, and when `t_j=0` it meets the
paired shore `X_j subseteq R`.  The verification for `W` is unchanged.
Thus the alternating minimum cover gives the same rooted completion for
connected paired shores as for literal carrier edges.

The two nonminor outcomes are now sharply identified compatibility
states rather than an unstructured portal residue.  In the literal-edge
case they are both colourable; for an unbounded carrier, the remaining
task is precisely to compose the perfect or singly exposed transport
with the carrier's internal proper-minor colour state.

## 4. Palette audit for an operated edge

Let `e=x_i y_j` be an actual cross-edge, and let `phi` be an
`(n+2)`-colouring of `F-e` in which the ends of `e` have the same colour.
Let `P_X,P_Y` be the colour sets on the two `n`-cliques and put

\[
                     d=|P_X-P_Y|=|P_Y-P_X|.                    \tag{4.1}
\]

After adjoining unused colour names if necessary, there are exactly
`n+2` available names, and hence `d in {0,1,2}`.  The common colours pair
`n-d` vertices of `X` with `n-d` vertices of `Y`.  Every such pair except
the operated pair is an edge of `M`; the operated pair is the newly
available edge in `M+e`.

Moreover:

* If `d=0`, these pairs form a perfect matching of `M+e`.  This is exactly
  the canonical separated-palette operation state.
* If `d=1`, one colour is outside `P_X union P_Y`.  Since `b` avoids
  `P_X`, `c` avoids `P_Y`, and `b,c` are adjacent, at least one of them
  uses a layer-unique colour.  If it is `c`, the uniquely coloured
  `X`-vertex has type zero; if it is `b`, the uniquely coloured
  `Y`-vertex has type one, by (1.3).
* If `d=2`, no colour lies outside `P_X union P_Y`.  Thus `b` uses a
  `Y`-unique colour at a type-one vertex and `c` uses an `X`-unique colour
  at a type-zero vertex.

This is the exact operation-state palette trichotomy.  Theorem 2.1 shows
that, for literal edge carriers, no further normalization of this
proper-minor colouring is necessary: the original full host already has
the colour-or-clique dichotomy.  For connected shores, the `d=1,2`
outcomes explain exactly why the residual in Theorem 3.1 is a singly
exposed transport state.

## 5. Verification

`near_k7_operation_state_dichotomy_probe.py` exhausts every type word and
every cross-nonedge relation for `n=4` (the four diagonal carrier pairs
remain actual edges).  It independently constructs and verifies the
colouring or the displayed minimum-cover clique model in every case.  It
reports

```
relations checked: 65536
outcomes: {'perfect-colour': 22896, 'corank-minor': 9616,
           'exposed-colour': 30384, 'alternating-minor': 2640}
```

The computation is only an audit; Theorems 2.1 and 3.1 are proved above
for every `n>=4`.
