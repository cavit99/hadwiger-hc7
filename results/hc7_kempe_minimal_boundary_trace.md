# Kempe-minimal boundary traces have pairwise bichromatic support

**Status:** written proof; separate internal audit GREEN in
[`hc7_kempe_minimal_boundary_trace_audit.md`](hc7_kempe_minimal_boundary_trace_audit.md).
This theorem gives a finite normalization of the double-contraction
colouring in the shore-filling two-root setting.  It does not make boundary
neighbourhoods laminar, allocate model labels, produce disjoint paths, or
prove `HC_7`.

## 1. Setting and extremal trace

Use the shore-filling setting and entrance edges

\[
                          e_i=z_i a_i\qquad(i=1,2)
\tag{1.1}
\]

from the audited
[two-root list-critical reduction](hc7_special_exact7_two_edge_list_core.md).
Let

\[
                         \widehat G=G/e_1/e_2
\tag{1.2}
\]

and let `q` be the contraction map.  A proper six-colouring `phi` of
`widehat G` expands to a colouring of `G-{e_1,e_2}` in which both pairs of
distinguished endpoints are monochromatic.

For a colour `gamma` used on the literal boundary, put

\[
 Y_\gamma=\{y\in Y:\phi(q(y))=\gamma\},
 \qquad
 \Gamma_\gamma=N_A(Y_\gamma),
\tag{1.3}
\]

and let `Pi_phi` be the equality partition of `Y`.  Write

\[
 C(\phi)=\sum_\gamma|\Gamma_\gamma|,
 \qquad
 d_F(\Pi)=|\Pi|-\omega\bigl(G[Y][\operatorname{sing}(\Pi)]\bigr).
\tag{1.4}
\]

Choose `phi` lexicographically minimizing

\[
                   \bigl(C(\phi),d_F(\Pi_\phi),|\Pi_\phi|\bigr)
\tag{1.5}
\]

over all proper six-colourings of `widehat G`.

## 2. Exact Kempe balance

### Lemma 2.1

Fix colours `alpha,beta`, let `W` be a union of components of
`widehat G[phi^{-1}({alpha,beta})]`, and let `phi^W` be obtained by
interchanging the two colours on `W`.  Then

\[
 C(\phi^W)-C(\phi)
 =|\Gamma'_\alpha\cap\Gamma'_\beta|
  -|\Gamma_\alpha\cap\Gamma_\beta|
 \ge0,
\tag{2.1}
\]

where primes denote the two boundary-neighbourhood sets after the switch.
If

\[
 E(\phi)=\sum_{v\in A}
   \bigl(d_{G[A]}(v)-|\mathcal L_\phi(v)|\bigr),
\tag{2.2}
\]

with lists defined by the boundary colours of `phi`, then

\[
                       E(\phi^W)-E(\phi)
                         =C(\phi^W)-C(\phi).
\tag{2.3}
\]

#### Proof

The switch is a proper colouring of `widehat G`; expansion still makes the
ends of each contracted edge monochromatic.  Only the `alpha,beta` terms
of `C` can change, and

\[
 \Gamma_\alpha\cup\Gamma_\beta
 =N_A(Y_\alpha\cup Y_\beta)
 =\Gamma'_\alpha\cup\Gamma'_\beta.
\]

Inclusion-exclusion gives the equality in (2.1), and the first coordinate
of (1.5) gives its inequality.  Finally,

\[
 E(\phi)=2|E(G[A])|-6|A|+C(\phi),
\]

which proves (2.3).  \(\square\)

## 3. Pairwise bichromatic support

### Theorem 3.1

For every two colours `alpha,beta` used on `Y`, some component of

\[
                 \widehat G[\phi^{-1}(\{\alpha,\beta\})]
\tag{3.1}
\]

meets both `q(Y_alpha)` and `q(Y_beta)`.

#### Proof

Suppose no component meets both classes.  Let `W` be the union of all
components meeting `q(Y_alpha)`.  Switching on `W` removes `alpha` from
the boundary and merges the blocks `Y_alpha,Y_beta`.

No edge of `G[Y]` joins the two old blocks, since its endpoints would lie
in one component of (3.1).  Their union is therefore still independent.
After the switch,

\[
 \Gamma'_\alpha=\varnothing,
 \qquad
 \Gamma'_\beta=\Gamma_\alpha\cup\Gamma_\beta.
\]

Equation (2.1) gives

\[
 C(\phi^W)-C(\phi)=-|\Gamma_\alpha\cap\Gamma_\beta|\le0.
\]

The first coordinate of (1.5) forces equality.

Let `k=|Pi_phi|`, and let `q_0,q_1` be the clique numbers of the
singleton-block graphs before and after the merger.  Removing the singleton
vertices among two anticomplete blocks lowers that clique number by at most
one, so

\[
                       q_0-1\le q_1\le q_0.
\]

The new demand is consequently

\[
                  (k-1)-q_1\le k-q_0=d_F(\Pi_\phi).
\]

If it is smaller, the second coordinate of (1.5) decreases.  If it is
equal, the third coordinate decreases.  Both contradict the choice of
`phi`, proving the theorem.  \(\square\)

### Corollary 3.2 (shore-confined quotient paths)

For every two boundary colours, a shortest path in the common component of
Theorem 3.1 from one boundary class to the other has no internal vertex in
`q(Y)`.  Its internal vertices all lie in one of

\[
                         A-\{a_1,a_2\},\qquad B.
\tag{3.2}
\]

When lifted to the literal graph `G`, the path is shore-confined except
that at each endpoint which is a contracted image `q(z_i)=q(a_i)`, the
distinguished edge `z_i a_i` may have to be prepended or appended.  Thus up
to two restored endpoint edges may be monochromatic; the lift need not be
a proper bichromatic path in `G-{e_1,e_2}`.

#### Proof

An internal boundary object would shorten the choice of path.  Removing
`q(Y)` from `widehat G` leaves the two anticomplete sets in (3.2), so the
path interior lies wholly in one.  Expanding a contracted endpoint gives
the stated correction and no other change.  \(\square\)

## 4. Exact scope

The result eliminates the possibility that two boundary colour blocks can
simply be merged by a Kempe switch after the lexicographic normalization.
It does not order the sets `Gamma_gamma` by inclusion: (2.1) controls only
the size of their overlap.  The paths for different colour pairs may use
different shores, intersect, and end at different literal members of a
colour block.

If the resulting list-critical core is proper, the existing selected-
response pullback supplies a strict connected-shore descent in its exact
composable case.  In the shore-filling case, the theorem supplies complete
pairwise blockwise Kempe support, but a simultaneous label-preserving
packaging theorem or compatible separator is still required.

## 5. Dependency

- [special two-root list-critical reduction](hc7_special_exact7_two_edge_list_core.md)
