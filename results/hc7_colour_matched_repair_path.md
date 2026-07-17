# A colour-matched path across a deficient rooted-minor branch set

**Status:** written proof; separate internal audit GREEN.  This is a conditional
lemma in the connected star--Kempe branch.  It does not prove `HC_7`.

## 1. Setup

Let `G`, `H`, `z`, `u`, and the proper six-colouring `phi` of `H` satisfy
the hypotheses of the star--Kempe compression theorem.  In particular,
`G` is a 7-contraction-critical graph and therefore is seven-connected.
Thus

\[
                         H=G-\{z,u\},
\]

the colour class `A` of a colour `alpha` is nonempty and anticomplete to
`{z,u}`, and, for every colour `gamma != alpha`, the induced subgraph

\[
                         H[A\cup V_\gamma]             \tag{1.1}
\]

is connected.  Fix a colour `beta != alpha`, put

\[
 X=A\cup V_\beta,\qquad Q=G-X,\qquad
 R=Q-\{z,u\},
\]

and write

\[
                         S=N_R(z),\qquad T=N_R(u).
\]

The restriction of `phi` to `R` is a proper four-colouring, and `T` uses
all four of its colours.

Let `(D_1,D_2,D_3,D_4)` be an `S`-rooted `K_4`-minor model in `R` that
maximizes the number of branch sets meeting `T`.  Suppose that
`D_j cap T` is empty.  Put

\[
 U_j=\bigcup_{i\ne j}D_i,
\]

and let `C_j` be the component of `R-U_j` containing `D_j`.  The audited
deficient-component theorem gives

\[
 C_j\cap T=\varnothing,
 \qquad
 N_G(C_j)=N_R(C_j)\mathbin{\dot\cup}N_X(C_j)
                    \mathbin{\dot\cup}\{z\}.          \tag{1.2}
\]

## 2. Colour-matched repair path

### Theorem 2.1

For every vertex `s in D_j cap S`, let `gamma=phi(s)`.  There is a path
`P` in `H[A cup V_gamma]` with one end in `C_j` and the other in `T` such
that

\[
             V(P)-V(C_j)-T\subseteq A\cup V_\gamma,   \tag{2.1}
\]

and no internal vertex of `P` belongs to `C_j cup T`.  Consequently,

\[
             Y_P=\{u\}\cup\bigl(V(P)-V(C_j)\bigr)     \tag{2.2}
\]

is a connected subgraph disjoint from `C_j` and adjacent to `C_j`.

#### Proof

The vertex `s` has colour `gamma`.  Since `D_j` is contained in `R`, the
colour `gamma` is one of the four colours used on `R`.  The set `T` uses
all four colours, so choose `t in T` with `phi(t)=gamma`.

By (1.1), the vertices `s` and `t` lie in the same connected graph
`H[A cup V_gamma]`; orient an `s`--`t` path `W` from `s` to `t`.  Let `t'`
be the first vertex of `T` on `W`, and let `c` be the last vertex of
`C_j` preceding `t'`.  Put `P=cWt'`.  Because `C_j cap T` is empty,
`c != t'`; by the choices of `c` and `t'`, the path `P` has exactly `c`
in `C_j` and exactly `t'` in `T`.  Every vertex of `P` lies in
`A cup V_gamma`, proving (2.1).

The graph obtained from `P` by deleting its vertices in `C_j` is a
nonempty terminal subpath ending at a vertex of `T`.  That endpoint is
adjacent to `u`, by the definition of `T`.  Hence (2.2) is connected.
The first edge of `P` leaving `C_j` joins `C_j` to `Y_P`, and the two
sets are disjoint.  This proves the theorem. \(\square\)

## 3. The expanded boundary and its surplus contacts

### Proposition 3.1

For every `i != j`,

\[
 N_R(C_j)\cap D_i\ne\varnothing,
 \qquad
 N_X(C_j)\ne\varnothing.                              \tag{3.1}
\]

Consequently, after relabelling so that `j=4`,

\[
 |N_G(C_4)|
   =1+|N_X(C_4)|+
       \sum_{i=1}^3 |N_R(C_4)\cap D_i|,               \tag{3.2}
\]

and each of the four nonconstant summands in (3.2) is at least one.  If
`G` has no separation of order seven, then the sum in (3.2) is at least
eight, so these four contact classes contain at least three vertices in
excess of the one-per-class baseline.

#### Proof

The branch set `D_j` is adjacent to every `D_i` with `i != j`.  Since
`D_j subseteq C_j`, the endpoint in `D_i` of an edge between those branch
sets belongs to `N_R(C_j) cap D_i`.  This proves the first assertion in
(3.1).

The set `X` dominates `Q`, and `C_j` is a nonempty subset of `Q`.
Therefore `C_j` has a neighbour in `X`, proving the second assertion.
Equation (3.2) now follows from the disjoint boundary identity (1.2) and
the containment `N_R(C_j) subseteq D_1 cup D_2 cup D_3` supplied by the
deficient-component theorem.  If there is no separation of order seven,
seven-connectivity first gives `|N_G(C_j)| >= 7`, and excluding an
order-seven separation strengthens this to `|N_G(C_j)| >= 8`.
Subtracting the five-vertex baseline proves the final assertion.
\(\square\)

## 4. Exact remaining obstruction

If `D_j` is the only branch set missing `T`, then

\[
 C_j,\ \{u\},\ \{z\},\ X,\ D_i\quad(i\ne j)          \tag{4.1}
\]

are the branch sets of a `K_7`-minor model with only the
`C_j`--`{u}` adjacency absent.  Theorem 2.1 supplies an actual path that
repairs that adjacency.  What it does not show is that the vertices of
the path can be reassigned while retaining four pairwise disjoint,
connected representatives for `X` and the other three `D_i`, together
with the repaired representative containing `u`, with all required
adjacencies.

Thus, in this branch, existence of the missing connection is no longer the
open problem.  The open problem is a branch-set-preserving path exchange:
either perform that reassignment, or prove that failure produces an actual
order-seven separation (and then align the two boundary colourings).

## 5. Dependencies

- [`hc7_star_kempe_five_core_compression.md`](../results/hc7_star_kempe_five_core_compression.md)
- [`hc7_maximal_rooted_k4_deficient_component_separator.md`](../results/hc7_maximal_rooted_k4_deficient_component_separator.md)
