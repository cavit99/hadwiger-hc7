# The two-defect disconnected-bag residue closes

## Status

This note closes the `B-X` disconnected outcome of the audited
palette-to-label theorem in the `HC_7` singleton/bipartite shell.  The
proof uses only seven-connectivity and literal branch sets.  It does not
use planarity, colour-state gluing, or a quotient-minor computation.

The only `d=2` residue left after this theorem is concentration of an
entire singleton portal class on the two same-parity witnesses.

## 1. Exact shell and witness rows

Let `G` be seven-connected.  Suppose

\[
 V(G)=\{v\}\mathbin{\dot\cup}V(B)
       \mathbin{\dot\cup}S,\qquad
 S=\{b_s,b_t,q_1,q_2,q_3\},                              \tag{1.1}
\]

where `S` is a clique and `B` is connected.  Suppose the apex has exactly
the two displayed nonneighbours in the singleton clique:

\[
             vb_s,vb_t\notin E(G),qquad vq_i\in E(G)
             \quad(1\le i\le3).                            \tag{1.2}
\]

Assume that the same-side deficient-label transversal from
`../results/hc7_near_k7_palette_label_alignment.md` has produced distinct
vertices `x_s,x_t in B` with

\[
\begin{array}{c|c|c|c}
 &v&\text{missed singleton}&\text{seen singleton rows}\cr\hline
x_s&\checkmark&b_s&b_t,q_1,q_2,q_3\cr
x_t&\checkmark&b_t&b_s,q_1,q_2,q_3.
\end{array}                                               \tag{1.3}
\]

Put

\[
                X=\{x_s,x_t\},\qquad
                L=\{v,b_s,b_t,q_1,q_2,q_3\},
                \qquad O=\{q_1,q_2,q_3\}.                 \tag{1.4}
\]

The two vertices of `X` lie in one bipartition class of the original
bipartite bag, so they are nonadjacent.  This fact is not needed below;
only the literal rows (1.3) are used.

## 2. Every component has an exact seven-row boundary

### Lemma 2.1 (component row classification)

Assume `B-X` is disconnected and let `R` be one of its components.  Then

\[
                         N_G(R)\subseteq X\cup L.            \tag{2.1}
\]

If `G` has no `K_7` minor, then

\[
       N_X(R)=X,qquad |N_L(R)|=5,                           \tag{2.2}
\]

and the unique member of `L-N_L(R)` belongs to `O`.

#### Proof

The spanning decomposition (1.1) gives (2.1).  Another component of
`B-X` remains outside `R union N_G(R)`, so `N_G(R)` is an actual vertex
cut.  Seven-connectivity gives

\[
                              |N_G(R)|\ge7.                  \tag{2.3}
\]

Connectedness of `B` gives `N_X(R) ne empty`.  If `R` met only one
member of `X`, (2.1)--(2.3) would force `N_L(R)=L`.  The same full-row
conclusion may also occur when `R` meets both witnesses.

Whenever `N_L(R)=L`, the seven branch sets

\[
        \{b_s\},\ \{b_t\},\ \{q_1\},\ \{q_2\},\ \{q_3\},
        \quad R,\quad \{v,x_s,x_t\}                         \tag{2.4}
\]

form a `K_7` model.  The last bag is the connected star at `v`; it sees
all five singleton bags by (1.3), and it is adjacent to `R` through
`N_X(R)` (and also through `v` if `v in N_L(R)`).  The set `R` sees all
five singleton bags, while those bags form a clique.

Thus in the target-free branch `R` does not see all of `L`.  Equations
(2.1)--(2.3) now force equality in

\[
             7\le |N_G(R)|=|N_X(R)|+|N_L(R)|le2+5=7.
                                                                    \tag{2.5}
\]

This proves (2.2): every component meets both witnesses and misses
exactly one exterior row.

It remains to exclude a missed row in `{v,b_s,b_t}`.  If `R` misses `v`
or `b_s`, use

\[
 \{b_s,v,x_t\},\quad \{b_t\},\quad
 \{q_1\},\{q_2\},\{q_3\},\quad \{x_s\},\quad R.          \tag{2.6}
\]

The first bag is connected through `vx_t` and `x_tb_s`.  It sees every
other displayed bag.  The component `R` meets both vertices of `X` and,
because its sole missed row is `v` or `b_s`, it sees `b_t` and all three
vertices of `O`.  Every remaining adjacency follows from (1.3) or the
clique on `S`.  Hence (2.6) is a `K_7` model.

If `R` misses `b_t`, interchange `s,t` and use

\[
 \{b_t,v,x_s\},\quad \{b_s\},\quad
 \{q_1\},\{q_2\},\{q_3\},\quad \{x_t\},\quad R.          \tag{2.7}
\]

Thus a target-free component can miss only one member of `O`.  \(\square\)

## 3. Two exact components give the target minor

### Theorem 3.1 (two-defect cut closure)

Under (1.1)--(1.3), if `B-X` is disconnected, then `G` contains a
`K_7` minor.

#### Proof

Suppose not.  Choose two distinct components `R_1,R_2` of `B-X`.
By Lemma 2.1, each component meets both `x_s,x_t`, sees
`v,b_s,b_t`, and sees exactly two of the three ordinary rows.  Let
`q in O` be the unique ordinary row missed by `R_2`; the row missed by
`R_1` may be the same or different.

Use the following seven branch sets:

\[
 \boxed{
 \{b_s,q,v\},\quad
 \{b_t\},\quad
 \{q'\}\ (q'\in O-\{q\}),\quad
 \{x_s\},\quad
 R_1\cup\{x_t\},\quad
 R_2.}                                                     \tag{3.1}
\]

There are `1+1+2+1+1+1=7` bags.  They are nonempty, connected and
pairwise disjoint.  Connectivity of the first bag uses the two edges
`b_sq` and `qv`; connectivity of `R_1 union {x_t}` uses
`x_t in N_X(R_1)`.

We verify every non-clique adjacency explicitly.

* The first bag sees `b_t` and both singleton members of `O-{q}` through
  the clique `S`; it sees `x_s` through `vx_s`; it sees
  `R_1 union {x_t}` through `vR_1` (also through `vx_t`); and it sees
  `R_2` through `vR_2` or `b_sR_2`, despite `R_2` missing `q`.
* The singleton `b_t` sees `x_s` by (1.3), sees `R_1 union {x_t}`
  through `R_1b_t` (although `x_t` itself misses `b_t`), and sees
  `R_2b_t` by Lemma 2.1.
* Each `q' in O-{q}` sees `x_s,x_t` by (1.3), sees `R_2` because
  `R_2` misses only `q`, and sees `R_1 union {x_t}` through `x_t`
  even if `q'` is the row missed by `R_1`.
* The bag `{x_s}` sees `R_1 union {x_t}` through an `x_s-R_1` edge and
  sees `R_2` through an `x_s-R_2` edge.
* Finally `R_1 union {x_t}` sees `R_2` through an `x_t-R_2` edge.

All pairs not mentioned are singleton pairs inside the clique `S` or are
contained in the checks above.  Thus (3.1) is a literal `K_7` model, the
desired contradiction.  \(\square\)

### Corollary 3.2 (exact remaining `d=2` cell)

In a seven-connected `K_7`-minor-free singleton/bipartite shell with two
apex-nonneighbour labels, the deficient-label transversal `X` satisfies

\[
                              B-X\text{ is connected}.        \tag{3.2}
\]

Therefore the audited palette-to-label theorem leaves only its other
outcome:

\[
                       P_i\subseteq X
           \quad\text{for some singleton portal class }P_i. \tag{3.3}
\]

The present theorem closes the entire disconnected-bag branch; it makes no
claim yet about the concentrated portal class in (3.3).
