# Common-host double-contraction lock allocation

**Status:** proved and independently audited.  This is a graph-global
lemma for two disjoint named edges.  In the atomic `HC_7` twin seam it
forces a common double-equality colouring in the common edge-deletion host
and allocates at least three, and often four, literal bichromatic locks to
one of the two named edges.  It does not identify colours with model rows or
with exact-seven boundary duties.

## 1. Setup and terminology

Let `q>=2`.  Let `G` satisfy

\[
        \chi(G)=q+1,
        \qquad\text{and every proper minor of }G\text{ is }q\text{-colourable}.
                                                               \tag{1.1}
\]

Let

\[
                         e=ab,\qquad f=cd                 \tag{1.2}
\]

be vertex-disjoint edges, and put

\[
                         H=G-\{e,f\},                    \tag{1.3}
\]

where both operations in (1.3) are edge deletions.

Write `[q]={1,...,q}` for the colour set.

Fix a proper colouring `kappa` of a graph `X`.  If two vertices `x,y`
have the same colour `i`, say that the pair `xy` is **`i-j` locked** when
`x,y` lie in the same component of the subgraph of `X` induced by the two
colour classes `i,j`.  Thus an `i-j` lock contains a literal `x-y` path
whose vertices all have colours in `{i,j}`.

The independently audited
[common edge-deletion fork](hc7_common_edge_deletion_k6_fork.md) proves in
the `q=6` twin-seam application that `H` is connected and exactly
six-chromatic and has a spanning `K_6` model.  The arguments below do not
use that model.  They use the stronger proper-minor hypothesis (1.1)
directly.

## 2. The exact three-state signature

### Lemma 2.1 (three available states, one forbidden state)

The graph `H` has a proper `q`-colouring `kappa` satisfying

\[
                  \kappa(a)=\kappa(b),
                  \qquad
                  \kappa(c)=\kappa(d).                  \tag{2.1}
\]

No proper `q`-colouring of `H` satisfies both

\[
                  \kappa(a)\ne\kappa(b),
                  \qquad
                  \kappa(c)\ne\kappa(d).                \tag{2.2}
\]

More precisely, writing the state of a colouring of `H` in the order
`(e,f)`, the following hold.

1. State `(equal,equal)` exists, obtained from `G/e/f`.
2. Every `q`-colouring of `H+e=G-f`, restricted to `H`, has state
   `(proper,equal)`, and at least one such colouring exists.
3. Every `q`-colouring of `H+f=G-e`, restricted to `H`, has state
   `(equal,proper)`, and at least one such colouring exists.
4. State `(proper,proper)` does not occur in any `q`-colouring of `H`.

### Proof

Because `e,f` are vertex-disjoint, contracting both of them produces a
proper minor `G/e/f`.  By (1.1), this minor has a proper `q`-colouring.
Expand the two contracted vertices back to the pairs `{a,b}` and `{c,d}`,
giving both ends of each contracted edge the colour of its image.  Every
edge of `H` maps to an edge of `G/e/f`; in particular, a cross-edge between
the two endpoint pairs maps to an edge between the two distinct contracted
vertices.  The expanded assignment is therefore a proper colouring of
`H`, and it has (2.1).

Conversely, a `q`-colouring of `H` with (2.2) remains proper after restoring
both `e` and `f`.  It would be a `q`-colouring of `G`, contrary to
`chi(G)=q+1`.  This proves clauses 1 and 4.

The graph `H+e=G-f` is a proper minor of `G`, so it has a
`q`-colouring.  Its edge `e` is necessarily proper.  The ends of `f` must
be equal in every such colouring, since otherwise restoring `f` would give
a `q`-colouring of `G`.  This proves clause 2.  Clause 3 is symmetric.
\(\square\)

The colouring in Lemma 2.1 will be called a **double-contraction
colouring**.  It is a common state in the literal two-edge sense.  It is a
colouring of `H`, not of either one-edge restoration.

## 3. Exact component-switch lemma

Let `i,j` be two colours of a proper colouring `kappa` of a graph `X`, and
let

\[
                    C_1,\ldots,C_m
\]

be the components of `X[kappa^{-1}({i,j})]`.  For a vector
`s=(s_1,...,s_m) in F_2^m`, interchange `i` and `j` on precisely those
components `C_r` for which `s_r=1`.

### Lemma 3.1 (two-pair component switching)

Every vector `s` gives a proper colouring of `X`.

Suppose `x_1,x_2` have one common colour in `{i,j}`, and `y_1,y_2` have
one common colour in `{i,j}` (the two common colours may be equal or
different).  Define linear forms on `F_2^m` by

\[
 \lambda_x(s)=s_{r(x_1)}+s_{r(x_2)},\qquad
 \lambda_y(s)=s_{r(y_1)}+s_{r(y_2)},                    \tag{3.1}
\]

where `r(v)` is the index of the bichromatic component containing `v`.
After the switches selected by `s`, the first pair has different colours
exactly when `lambda_x(s)=1`, and the second pair has different colours
exactly when `lambda_y(s)=1`.

Consequently, if both pairs are unlocked in the `i-j` subgraph, there is a
simultaneous component switch which makes both pairs proper.

### Proof

Swapping two colours on one whole bichromatic component preserves properness.
Indeed, edges internal to the component remain bichromatic; an edge from
the component to a vertex of colour `i` or `j` would place that vertex in
the same component; and edges to all other colour classes are unaffected.
The components are disjoint, so any selected family may be switched
simultaneously.

Both ends of each displayed pair start with the same colour.  Exactly one
of its ends changes colour precisely when the selected-component bits of
its two ends differ.  This proves (3.1).

A pair is unlocked precisely when its ends lie in distinct components,
which is equivalent to its form in (3.1) being nonzero.  If the two
nonzero forms are equal, any vector on which their common value is one
solves both equations.  If they are distinct, then over `F_2` they are
linearly independent, so the map

\[
        s\longmapsto(\lambda_x(s),\lambda_y(s))
\]

is onto `F_2^2`; in particular, `(1,1)` has a preimage.  Thus both pairs
can be made proper simultaneously.  \(\square\)

This is the point at which switching whole components, rather than one
chosen path, matters.  It covers both crossed and uncrossed placements of
the four endpoints among the bichromatic components.

## 4. Same-colour allocation

### Theorem 4.1

Let `kappa` be a double-contraction colouring of `H`.  Suppose

\[
       \kappa(a)=\kappa(b)=\kappa(c)=\kappa(d)=i.       \tag{4.1}
\]

For every colour `j` different from `i`, at least one of the pairs `ab,cd` is `i-j`
locked in `H`.  Hence one of the two named pairs is locked for at least

\[
                       \left\lceil\frac{q-1}{2}\right\rceil       \tag{4.2}
\]

of the other colours.  For `q=6`, the lower bound is three.

### Proof

Fix `j` different from `i`.  If both pairs were unlocked in the `i-j` subgraph,
Lemma 3.1 would give another proper `q`-colouring of `H` in which both
pairs are proper.  This contradicts the second assertion of Lemma 2.1.
Thus at least one pair is locked for each of the `q-1` choices of `j`.
Counting these locks with multiplicity over the two named pairs proves
(4.2).  \(\square\)

## 5. Distinct-colour allocation

### Theorem 5.1

Let `kappa` be a double-contraction colouring of `H`, and suppose

\[
       \kappa(a)=\kappa(b)=i,
       \qquad
       \kappa(c)=\kappa(d)=k,
       \qquad i\ne k.                                  \tag{5.1}
\]

Put `J=[q]-{i,k}` and define

\[
\begin{aligned}
 U&=\{j\in J:ab\text{ is not }i\text{-}j\text{ locked}\},\\
 V&=\{j\in J:cd\text{ is not }k\text{-}j\text{ locked}\}.
\end{aligned}                                          \tag{5.2}
\]

Then one of the following holds:

1. `U` is empty;
2. `V` is empty; or
3. there is one colour `theta` in `J` such that
   `U=V={theta}`.

In addition, at least one of `ab,cd` is locked in the `i-k` bichromatic
subgraph.  Consequently, one of the two named pairs is locked for at least

\[
                              q-2                         \tag{5.3}
\]

of its `q-1` possible alternate colours.  For `q=6`, the lower bound is
four.

### Proof

Suppose `beta` is in `U` and `delta` is in `V`, with `beta` different from
`delta`.  Since both lie
in `J`, the palettes `{i,beta}` and `{k,delta}` are disjoint.  Because
`beta` is in `U`, switching one suitable `i-beta` component makes `ab` proper.
Because `delta` is in `V`, switching one suitable `k-delta` component makes
`cd` proper.

The two switched vertex sets are disjoint: every vertex of the first has
colour in `{i,beta}`, while every vertex of the second has colour in
`{k,delta}`.  Moreover, the first switch introduces neither `k` nor
`delta`, and the second introduces neither `i` nor `beta`.  The switches
therefore commute, each remains a switch of a bichromatic component after
the other, and their simultaneous result is a proper colouring.  The first
switch does not affect `c,d`; the second does not affect `a,b`.  Their
combined result makes both deleted edges proper, contradicting Lemma 2.1.

It follows that

\[
           \beta=\delta\quad\text{for every }\beta\in U,
                                      \delta\in V.       \tag{5.4}
\]

If either set is empty, outcomes 1 or 2 hold.  If both are nonempty,
(5.4) forces each to be a singleton and forces their unique elements to
be equal, proving outcome 3.

Now apply Lemma 3.1 to the `i-k` subgraph.  If both pairs were unlocked,
a component switch would make both proper, again contradicting Lemma 2.1.
Thus at least one is `i-k` locked.

If `U` is empty, `ab` is locked for all `q-2` colours in `J`; if `V` is
empty, the symmetric assertion holds for `cd`.  In outcome 3, both pairs
are locked for the `q-3` colours in `J-{theta}`, and the `i-k` lock gives
one of them one further lock.  These cases prove (5.3).  \(\square\)

### Corollary 5.2 (cross-edge sharpening)

If at least one cross-edge joins `{a,b}` to `{c,d}` in `G`, then the two
contracted vertices are adjacent in `G/e/f`.  Their colours in every
double-contraction colouring are therefore distinct, so Theorem 5.1
applies.  For `q=6`, one named pair has at least four common-host locks.

## 6. One-restoration lock transfer into the common host

The three-state signature also puts many locks on **each** named pair,
although generally in two different response colourings.

### Theorem 6.1

Let `rho_e` be any `q`-colouring of `H+e`.  By Lemma 2.1 it has state
`(proper,equal)`.  If the common `rho_e`-colour of `c,d` is `k`, then
`cd` is `k-j` locked in `H+e` for every `j` different from `k`.
Moreover, it remains `k-j` locked after deleting `e`, and hence in `H`,
for at least `q-2` choices of `j`.

Symmetrically, every `q`-colouring of `H+f` gives at least `q-2`
common-host locks for `ab`.  For `q=6`, each named pair therefore has a
response colouring in which it has at least four literal bichromatic lock
paths lying wholly in `H`.

### Proof

Fix `j` different from `k`.  If `c,d` lay in distinct components of the
`k-j` subgraph of `H+e`, switch the component containing exactly one of
them.  The result is still a proper colouring of `H+e`, so in particular
the restored edge `e` remains proper.  The switch makes `f` proper as
well.  Restoring `f` would therefore give a `q`-colouring of `G`, a
contradiction.  Thus `cd` is locked for every one of the `q-1` alternate
colours in `H+e`.

Let the two distinct colours on the proper edge `e=ab` in `rho_e` be
`r,s`.  The edge `e` belongs to the `k-j` induced subgraph only when
`{r,s}={k,j}`.  This can happen for at most one choice of `j`.  For every
other `j`, deleting `e` changes no edge of the `k-j` subgraph, so the
`c-d` lock remains in `H`.  At least `q-2` common-host locks remain.  The
assertion for `ab` follows by interchanging `e` and `f`.  \(\square\)

The two response colourings in Theorem 6.1 may be unrelated, and lock
paths belonging to different palettes need not be internally disjoint.

## 7. Atomic `HC_7` consequence and exact scope

In the frozen twin seam put

\[
                          e=zu,\qquad f=dt.
\]

The common host `H=G-{e,f}` therefore has a six-colouring in which

\[
                          z=u,\qquad d=t                 \tag{7.1}
\]

as colour equalities.  In that one colouring, one of the following is
literal:

1. one named pair is joined in `H` by bichromatic lock paths for at least
   three alternate colours; or
2. the two equality colours are distinct, and one named pair has such
   paths for at least four alternate colours.

If any cross-edge between the endpoint pairs is present, only the second
case occurs.  Every path asserted here lies entirely in the one common
edge-deletion host `H`; neither restored edge is used.

In addition, the two one-edge responses give four common-host locks for
`dt` and four common-host locks for `zu`, respectively, by Theorem 6.1.
Those two four-lock systems need not use the same colouring; the
double-contraction allocation above is the statement that couples both
named pairs inside one colouring.

The result removes one genuine ambiguity: a common two-edge equality state
exists, and its two lock systems cannot both be sparse or independently
oriented.  It does **not** prove any of the following.

* The lock paths for different alternate colours need not be internally
  disjoint.  They may share vertices of the common equality colour.
* Palette colours are not branch-set labels.  The theorem does not place
  `z,u,d,t` in rows of the spanning `K_6` model or split a row.
* The colouring (7.1) is not a colouring of `G/e` or `G/f`: restoring
  either contracted edge to the expanded host makes that edge
  monochromatic.
* Restricting (7.1) to the two exact-seven boundaries need not give the
  same legally returned equality partition as either one-edge response.
* No fixed `K_5`-transversal pair or strictly ranked `F_12` handoff follows
  from lock allocation alone.

Thus the new lemma is an operation-coupled common-host input for the
double-lock decoder.  The remaining step is still label-faithful: turn the
majority locked pair, together with the spanning `K_6` model and the two
opposite one-edge response signatures, into a row split/reselection,
literal terminal outcome, or globally ranked exact-seven transition.
