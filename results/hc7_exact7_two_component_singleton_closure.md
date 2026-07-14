# Singleton component closure in the residual `(1,2)` cell

**Status:** proved and independently audited.

## 1. Statement

Let `G` be seven-connected, `K_7`-minor-free, and proper-minor-minimal
subject to not being six-colourable.  Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

be an actual separation with packet vector `(nu_L,nu_R)=(1,2)`.  Put
`H=G[S]` and assume that `H` belongs to the frozen 129-graph residual of
the audited adaptive `(1,2)` boundary theorem.  Suppose `G[R]` has exactly
two connected components and one of them is a singleton.

### Theorem 1.1

This configuration is impossible.

The residual hypothesis is essential to the stated proof.  The theorem
does not classify arbitrary seven-vertex neighbourhoods of independence
number two.

## 2. Reorientation at the singleton

Write the singleton component as `{q}` and the other rich component as
`C`.  Every open-shore component is `S`-full, so

\[
                              N_G(q)=S.                 \tag{2.1}
\]

In particular `d(q)=7`.  Dirac's neighbourhood inequality for a
7-contraction-critical graph gives

\[
                              \alpha(H)\le2.             \tag{2.2}
\]

Every component of `G[L]` is also `S`-full.  Since `nu_L=1`, there can be
only one such component; hence `G[L]` is connected.  Relative to the
degree-seven vertex `q`, therefore,

\[
                         G-N[q]=G[L]\mathbin{\dot\cup}C  \tag{2.3}
\]

has exactly two connected components, both full to `S=N(q)`.

The independently audited singleton-residual extraction says that the only
members of the frozen 129 residual satisfying (2.2) are

\[
                              H\cong M
                    \quad\hbox{or}\quad H\cong M+13,    \tag{2.4}
\]

where, in the standard labelling,

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.            \tag{2.5}
\]

If `H` is the pure Moser spindle, the audited complete two-component
Moser theorem applied at `q` contradicts (2.3).  It remains to exclude the
one-edge extension.

## 3. Direct two-anchor exclusion of `M+13`

Assume `H=M+13`.  The pairs `25` and `46` are vertex-disjoint nonedges,
while the remaining vertices `0,1,3` induce a triangle.

Let `A_1=G[L]` and `A_2=C`.  To colour the closed side
`G[S union A_i]`, let `j ne i` and contract in `G` the two disjoint
connected sets

\[
                       \{q,2,5\},\qquad A_j\cup\{4,6\}. \tag{3.1}
\]

They are connected by (2.1)--(2.3), and their images are adjacent through
the edges `q4,q6`.  Every one of `0,1,3` is adjacent to the first image
through `q` and to the second through the `S`-full component `A_j`.
Together with the literal triangle `013`, the two images consequently form
a `K_5`.

The contraction is proper, so it has a six-colouring.  Restrict to the
untouched side `A_i` and expand only the two independent literal pairs.
The `K_5` forces the exact boundary state

\[
                         25\mid46\mid0\mid1\mid3.       \tag{3.2}
\]

Doing this for `i=1,2` gives the same exact state on both closed sides of
the separation at `S`.  Permute one six-colour palette to align the five
blocks and glue the two side colourings to a six-colouring of `G-q`.
Exactly five colours occur on `S`, so the unused sixth colour can be given
to `q`, contradicting the choice of `G`.

This excludes `M+13`; the pure-Moser theorem excludes the other case in
(2.4), proving Theorem 1.1.  \(\square\)

## 4. Dependencies and scope

The proof uses only the following frozen inputs:

1. exact-seven packet packing, to orient the cell with `nu_L=1`;
2. the adaptive `(1,2)` residual and its audited independence-two
   extraction;
3. Dirac's neighbourhood inequality; and
4. the complete pure-Moser two-component closure.

The `M+13` exclusion in Section 3 is conceptual and does not use a finite
minor search.  This theorem eliminates every singleton component in the
two-component rich shore of the current residual, but says nothing about
an arbitrary boundary outside that residual.
