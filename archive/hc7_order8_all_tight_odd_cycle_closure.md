# Paired two-connected all-tight kernels at an order-eight boundary close

**Status:** archived, superseded by the uniform paired all-tight closure;
[separate internal audit](hc7_order8_all_tight_odd_cycle_closure_audit.md)
GREEN at the recorded mathematical revision.  This file preserves the
stronger explicit odd-cycle certificate.  It does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Among all nonempty connected sets `R` satisfying

\[
 G-(R\cup N_G(R))\ne\varnothing,
 \qquad |N_G(R)|\ge 8,
\tag{1.2}
\]

choose one lexicographically minimizing

\[
                  \bigl(|N_G(R)|,|R|\bigr).
\tag{1.3}
\]

Suppose the minimum boundary has order eight.  Put `S=N_G(R)`, and assume
we are in the full-component outcome of the minimum-positive-excess normal
form: `G-S` has exactly two components `A,D`, and both components are
adjacent to every literal vertex of `S`.  (In the alternative outcome that
normal form already supplies an order-seven component response.)

Let `phi` be a proper six-colouring of `G[S]` which extends through neither
closed shore.  For `Z in {A,D}` and `v in Z`, put

\[
 L_Z(v)=[6]\setminus
     \{\phi(s):s\in N_G(v)\cap S\}.
\tag{1.4}
\]

Assume that, for both `Z=A,D`,

1. `G[Z]` is vertex-minimal subject to not being `L_Z`-colourable;
2. every vertex is tight:
   \[
                         d_{G[Z]}(v)=|L_Z(v)|;
   \tag{1.5}
   \]
3. `G[Z]` is an odd cycle.

The triangle is allowed as an odd cycle.

## 2. Constant lists and four boundary colours

### Lemma 2.1

For each `Z in {A,D}`, all lists `L_Z(v)` are the same two-element set.
Moreover `phi` uses exactly four colours on `S`, and every vertex of each
open shore has a neighbour in every one of the four boundary colour
classes.

### Proof

The internal degree on an odd cycle is two, so (1.5) gives
`|L_Z(v)|=2` for every vertex.

We use the elementary equality case of degree-choosability for an odd
cycle.  If two adjacent vertices of an odd cycle have different
two-element lists, orient the cycle as

\[
                         v_1v_2\cdots v_nv_1
\]

so that `L(v_1) ne L(v_n)`.  Choose a colour in
`L(v_1)-L(v_n)` for `v_1`, and colour `v_2,...,v_n` greedily in that
order, each time avoiding the colour of the preceding vertex.  At `v_n`
the chosen colour of `v_1` is unavailable anyway, so the closing edge is
proper.  Thus a non-colourable odd cycle with two-element lists has one
common list at every vertex.

By (1.4), the sets of boundary colours seen by the vertices of one shore
are therefore identical and have order four.  Every literal vertex of `S`
has a neighbour in that shore.  Hence every colour used by `phi` on `S`
belongs to this common four-set.  Conversely every member of the common
four-set occurs on `S`.  Thus `phi` uses exactly four colours, and every
shore vertex sees every boundary colour class.  The other shore is
identical. \(\square\)

## 3. Reduction to two finite orders

### Lemma 3.1

If `G` has no order-seven singleton-side response, then

\[
                         |A|+|D|\le 8.
\tag{3.1}
\]

Consequently the unordered pair of shore orders is either `(3,3)` or
`(3,5)`.

### Proof

Write `a=|A|`, `d=|D|`, and `s=a+d`.  If a vertex of either open shore
had degree seven, its full neighbourhood would be an actual order-seven
separator: the other open shore lies outside its closed neighbourhood.
Deleting any incident edge gives the usual proper-minor response.  Exclude
this terminal outcome.

No shore vertex has degree eight.  Indeed its singleton set would satisfy
(1.2), with boundary order eight and side order one, contradicting the
lexicographic choice (1.3), since both odd cycles have order at least three.
Seven-connectivity now gives degree at least nine at every shore vertex.
Each has two internal neighbours, so it has at least seven neighbours in
`S`.  Hence the number `e_cross` of edges from `A union D` to `S` satisfies

\[
                            e_{\rm cross}\ge 7s.
\tag{3.2}
\]

The two cycles contribute exactly `s` internal edges.  Mader's strict
bound in a seven-connected seven-chromatic `K_7`-minor-free graph is

\[
                         |E(G)|\le5|V(G)|-16=5s+24.
\tag{3.3}
\]

There are no edges between the two open components, so, writing
`h=|E(G[S])|`, equations (3.2)--(3.3) give

\[
                  s+e_{\rm cross}+h\le5s+24,
                  \qquad 3s+h\le24.
\tag{3.4}
\]

Thus `s<=8`.  Both component orders are odd and at least three, giving
only `(3,3)` and `(3,5)`. \(\square\)

### Lemma 3.2

The pair `(3,3)` is impossible.

### Proof

Here `s=6`.  Summing degrees over the eight boundary vertices and using
seven-connectivity gives

\[
                         e_{\rm cross}+2h\ge56.
\tag{3.5}
\]

On the other hand, (3.3) gives

\[
                         e_{\rm cross}+h\le48,
\tag{3.6}
\]

while (3.2) gives `e_cross>=42`.  Subtracting (3.6) from (3.5) gives
`h>=8`, whereas (3.6) and `e_cross>=42` give `h<=6`, a contradiction.
\(\square\)

## 4. The equality residue has an explicit `K_7` model

### Lemma 4.1

The pair `(3,5)` gives an explicit `K_7`-minor model.

### Proof

Now `s=8`.  Equation (3.4) forces `h=0`, and equality holds throughout
(3.2)--(3.3).  Thus every shore vertex has exactly seven boundary
neighbours.  Summing degrees over the eight boundary vertices gives

\[
                         e_{\rm cross}+2h\ge56.
\]

This too is an equality, so every boundary vertex has exactly seven
neighbours in `A union D`.  Consequently the nonedges between `S` and
`A union D` form a perfect matching.

Write the triangle as `a_0a_1a_2a_0`, the five-cycle as
`d_0d_1d_2d_3d_4d_0`, and name the boundary vertex uniquely nonadjacent
to `u in A union D` by `x_u`.  The following seven pairwise disjoint sets
are connected:

\[
\begin{aligned}
 B_1&=\{x_{a_0},x_{a_1},x_{a_2},x_{d_0},a_0,a_1,d_1\},\\
 B_2&=\{x_{d_1}\},\\
 B_3&=\{a_2,x_{d_2}\},\\
 B_4&=\{d_2,x_{d_3}\},\\
 B_5&=\{d_0,x_{d_4}\},\\
 B_6&=\{d_3\},\\
 B_7&=\{d_4\}.
\end{aligned}
\tag{4.1}
\]

They are pairwise adjacent.  For completeness, one witnessing edge for
each pair is displayed below; entries in row `i`, column `j` witness
`B_i`--`B_j`.

\[
\begin{array}{c|cccccc}
 &B_2&B_3&B_4&B_5&B_6&B_7\\ \hline
B_1&a_0x_{d_1}&a_0a_2&x_{a_0}d_2&a_0x_{d_4}
    &x_{a_0}d_3&x_{a_0}d_4\\
B_2&&x_{d_1}a_2&x_{d_1}d_2&x_{d_1}d_0
    &x_{d_1}d_3&x_{d_1}d_4\\
B_3&&&a_2x_{d_3}&a_2x_{d_4}&x_{d_2}d_3&x_{d_2}d_4\\
B_4&&&&d_2x_{d_4}&d_2d_3&x_{d_3}d_4\\
B_5&&&&&x_{d_4}d_3&d_0d_4\\
B_6&&&&&&d_3d_4
\end{array}
\tag{4.2}
\]

Every cross edge in (4.2) avoids its unique forbidden matched pair, and
the remaining entries are edges of the triangle or five-cycle.

Thus (4.1) is a `K_7`-minor model, contrary to (1.1). \(\square\)

## 5. The conditional closure

### Theorem 5.1

Under the hypotheses of Section 1, the all-tight odd-cycle pair cannot
survive.  More precisely, either a shore vertex has degree seven and gives
a strict singleton-side generic exact-seven response, or `G` contains the
explicit `K_7`-minor model of Lemma 4.1.

### Proof

If a degree-seven shore vertex exists, its singleton side is strictly
smaller than either odd-cycle shore and its full neighbourhood is an
order-seven separator.  Otherwise Lemmas 3.1--4.1 give the explicit minor.
\(\square\)

### Corollary 5.2 (residual two-connected all-tight kernels)

Suppose more generally that both spanning all-tight kernels are
two-connected, without assuming that they are odd cycles.  Then the only
cases not eliminated by Theorem 5.1 or an immediate explicit `K_7` model
are

\[
        G[A]\cong G[D]\cong K_5
        \quad\text{or}\quad
        G[A]\cong G[D]\cong K_4.
\tag{5.1}
\]

In the first case `phi` uses two boundary colours; in the second it uses
three.  Thus the residual all-tight two-connected problem is a bounded
literal contact-allocation problem, not an unbounded critical-kernel
family.

### Proof

The degree-choosability equality theorem says that a two-connected
all-tight kernel is a complete graph or an odd cycle.  If either kernel is
an odd cycle, Lemma 2.1 forces four boundary colours.  Formula (5.2) below
then forces any clique kernel on the other shore to be `K_3`, which is
itself an odd cycle.  Thus Theorem 5.1 removes every case containing an
odd-cycle kernel.

Suppose a kernel is `K_r`.  Its lists have order `r-1`.  Hall's theorem
shows that an uncolourable assignment of `(r-1)`-element lists on `K_r`
has one common list: a deficient subfamily of fewer than `r` lists is
impossible because each individual list already has order `r-1`, while a
deficiency among all `r` lists forces their union, and hence every list,
to have order `r-1`.  Fullness then shows, as in Lemma 2.1, that the
complement of this common list is exactly the set of colours used on `S`.
If `b` colours occur on `S`, then

\[
                              r=7-b.                  \tag{5.2}
\]

Two-connectedness gives `r>=3`, so `b<=4`.  The case `b=4` is `K_3`,
already included in Theorem 5.1.  If `b=1`, then each kernel is `K_6`.
Use the six vertices of `A` as singleton branch sets and use `D union S`
as the seventh branch set.  It is connected because `D` is connected and
full to `S`, and it is adjacent to every vertex of `A` because every
`A`-vertex sees the sole boundary colour.  This is a `K_7`-minor model.

Only `b=2,3` remain, giving respectively `K_5,K_4` on both shores by
(5.2). \(\square\)

### Theorem 5.3 (two-connected all-tight pair closure)

Retain the host, minimum-boundary, full-component, common-colouring,
vertex-minimality and tightness hypotheses of Section 1, but replace the
assumption that both kernels are odd cycles by the assumption that both are
two-connected.  Then either a degree-seven vertex gives a strict
singleton-side generic exact-seven response, or `G` contains an explicit
`K_7`-minor model.

#### Proof

Corollary 5.2 reduces the only cases not already covered by Theorem 5.1 or
an explicit `K_7` model to

\[
                   (G[A],G[D])=(K_5,K_5)
              \quad\hbox{or}\quad (K_4,K_4).           \tag{5.3}
\]

Thus `|V(G)|` is respectively `18` or `16`.  Suppose there is no
degree-seven vertex.  No vertex has degree eight: its singleton would be
an eligible connected set with boundary order eight and nonempty opposite
side, giving the lexicographically smaller pair `(8,1)` in place of
`(8,|R|)`, where `|R|` is four or five.  Seven-connectivity therefore gives

\[
                              \delta(G)\ge9.            \tag{5.4}
\]

Writing `n=|V(G)|` and using the strict host edge bound gives

\[
                       \frac{9n}{2}\le |E(G)|le5n-16,
\]

and hence `n>=32`, contrary to `n in {16,18}`.  A degree-seven vertex must
therefore exist.  Since `n>8`, its full neighbourhood is the boundary of a
nontrivial singleton-side separation.  Deleting any incident edge gives
the standard generic exact-seven response, and the singleton is strictly
smaller than either original clique shore. \(\square\)

## 6. Exact gain and trust boundary

The theorem eliminates the entire paired two-connected all-tight family.
The two odd cycles may initially have arbitrary order; the only remaining
clique pairs are bounded, and the host density closes them without contact
casework.  The proof uses the host-level lexicographic normalization, the
exact all-tight list assignment, seven-connectivity and global
`K_7`-minor exclusion.

It does not prove that every minimum order-eight response interface reaches
paired spanning all-tight two-connected kernels.  All-tight Gallai trees
with cutvertices require the separate multiblock machinery, while positive
list-degree excess remains the unbounded response-coupling branch.

## 7. Dependencies

- [minimum positive-excess separator normal form](../results/hc7_minimum_positive_separator_normal_form.md);
- the Borodin--Erdos--Rubin--Taylor degree-choosability characterization,
  used in full in Corollary 5.2; see P. Erdos, A. L. Rubin and H. Taylor,
  *Choosability in graphs*, Congressus Numerantium **26** (1979),
  125--157; and
- [the strict Mader bound for the present host](../results/hc7_large_boundary_singleton_response_descent.md),
  Lemma 1.1.
