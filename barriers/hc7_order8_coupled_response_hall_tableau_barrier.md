# Coupled incident-edge switches do not resolve the Hall obstruction algebraically

**Status:** written lemma and explicit finite barrier; separate internal
audit GREEN in
[`hc7_order8_coupled_response_hall_tableau_barrier_audit.md`](hc7_order8_coupled_response_hall_tableau_barrier_audit.md).
This is not a counterexample to `HC_7`.  It isolates the exact
information which is, and is not, supplied by Proposition 3.1 of the
[positive boundary-excess theorem](../results/hc7_order8_positive_excess_frozen_outer_shore.md).

## 1. The inference refuted

The following data, taken by themselves, do not force the two opposite
boundary equality partitions to coincide and do not repair the
two-support Hall obstruction:

1. a common six-colouring after deleting two incident edges `wu,wq`, with
   `w,u,q` in one colour class;
2. two named Kempe-component interchanges, one restoring `wu` and one
   restoring `wq`;
3. a path between `u` and `q` made from those components and one joining
   edge;
4. two distinct induced equality partitions on the literal boundary;
5. two adjacent connected subgraphs `Q_0,Q_1`, each adjacent to every
   vertex of the old eight-boundary; and
6. an exact Hall-deficiency certificate of demand two for the partition
   legal on the `Q_0\cup Q_1` side.

The barrier is at the level of the literal boundary, switch footprints and
support incidences.  It does not assert that the finite shell below is
seven-connected, seven-chromatic, contraction-critical or `K_7`-minor-free.
Consequently it does not refute a positive theorem using those host-level
hypotheses.  In particular, it does not rule out an exact order-seven
separation or an explicit `K_7`-minor model forced by additional geometry.

## 2. A general coupled-switch normal form

Let `H=G-{wu,wq}` be properly coloured by `kappa`, with

\[
                    \kappa(w)=\kappa(u)=\kappa(q)=0.
\tag{2.1}
\]

Suppose the bypass alternative of the incident-edge theorem gives distinct
colours `i,j`, the `{0,i}`-component `A` containing `u`, and the
`{0,j}`-component `D` containing `q`.  Thus

\[
 w,q\notin A,\qquad w,u\notin D,
\tag{2.2}
\]

and either `A\cap D` is nonempty or an edge joins an `i`-coloured vertex
of `A` to a `j`-coloured vertex of `D`.

For a vertex set `T`, write `K_r(T)` for the vertices of `T` having colour
`r` in `kappa`.  Interchanging `0,i` on `A` changes the two boundary colour
classes to

\[
\begin{split}
 K'_0(T)&=(K_0(T)-A)\cup(K_i(T)\cap A),\\
 K'_i(T)&=(K_i(T)-A)\cup(K_0(T)\cap A),
\end{split}
\tag{2.3}
\]

and leaves every other class unchanged.  The analogous formula with
`D,j` gives the other response partition.

### Lemma 2.1 (the simultaneous-switch obstruction)

If `A,D` are disjoint, put

\[
 F=E_G(K_i(A),K_j(D)).
\tag{2.4}
\]

Then `F` is nonempty.  Simultaneously interchanging `0,i` on `A` and
`0,j` on `D`, and restoring `wu,wq`, gives a proper colouring of `G-F` in
which every edge of `F` has two ends of colour zero.  If `|F|=1`, this is
a third, explicitly coupled, one-edge response.

#### Proof

The individual interchanges are proper Kempe interchanges.  Since `A,D`
are disjoint, the simultaneous assignment can fail only on an edge between
them.  The old colouring is proper and the two palettes meet only in colour
zero.  Hence a newly monochromatic edge has an `i`-coloured end in `A` and
a `j`-coloured end in `D`, and both ends change to zero.  The bypass theorem
guarantees at least one such joining edge when the components are disjoint,
so `F` is nonempty.  Deleting all of `F` leaves a proper assignment.
Equation (2.2) says that `u` changes away from zero under the first switch,
that `q` changes away from zero under the second, and that `w` is changed
by neither.  Thus both incident edges can be restored.  This proves the
lemma. \(\square\)

The set `F`, rather than an abstract permutation of colour names, is the
literal obstruction to combining the two responses.

## 3. A minimum-order boundary tableau

The positive-excess setting has

\[
 B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |S|=8,\quad |W|\ge2,
\tag{3.1}
\]

so `|B|\ge9`.  The following example has equality.

Put

\[
\begin{split}
 B&=\{d,x_d,y_d,x_e,y_e,x_0,y_0,w,r\},\\
 S&=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\},\\
 W&=\{w,r\}.
\end{split}
\tag{3.2}
\]

Let the boundary edges be

\[
 d x_d,\ x_dy_d,\ y_dd,\ x_ey_e,
 \quad r x_d,\ r x_e,\ x_dx_e.
\tag{3.3}
\]

All unlisted boundary pairs are nonedges.  Give the boundary the central
colour classes

\[
 \{w\}\mid\{d,r\}\mid\{x_d\}\mid\{x_e\}
       \mid\{y_d,y_e,x_0,y_0\}.
\tag{3.4}
\]

The sixth colour is unused on `B`.  This is proper for (3.3).

Take the boundary footprint of `A` in Lemma 2.1 to be `{y_d}` and that of
`D` to be `{d}`.  The joining edge is the single boundary edge `dy_d`.
The two switches give

\[
\begin{split}
 \Sigma_E={}&\{w,y_d\}\mid\{d,r\}\mid\{x_d\}\mid\{x_e\}
                 \mid\{y_e,x_0,y_0\},\\
 \Sigma_C={}&\{w,d\}\mid\{r\}\mid\{x_d\}\mid\{x_e\}
                 \mid\{y_d,y_e,x_0,y_0\}.
\end{split}
\tag{3.5}
\]

Here `Sigma_E` is the partition legal on the first closed side and
`Sigma_C` is the partition legal on the side containing `Q_0,Q_1`.
The notation records orientation only; no claim about a complete extension
language is made in this finite tableau.

For `Sigma_C`, the singleton vertices

\[
                         U=\{r,x_d,x_e\}
\tag{3.6}
\]

induce a triangle and hence form a maximum singleton clique.  The two
blocks outside `U` are

\[
 C_1=\{w,d\},\qquad C_2=\{y_d,y_e,x_0,y_0\}.
\tag{3.7}
\]

Their required boundary sets are

\[
 R_U(C_1)=C_1\cup\{r,x_e\},
 \qquad R_U(C_2)=C_2\cup\{r\}.
\tag{3.8}
\]

Now take adjacent connected supports `Q_0,Q_1` such that `Q_0` is adjacent
to every vertex of `B`, while `Q_1` is adjacent to every vertex of
`B-\{r\}` and misses `r`.  Both supports are adjacent to every literal
vertex of `S`; the vertex `e` may lie in `Q_0`, as it does in the explicit
shell in Section 4.  In the incidence graph of the transported-partition
theorem, `Q_0` is incident with both `C_1,C_2` and `Q_1` with neither.
Thus

\[
 N(\{C_1,C_2\})=\{Q_0\},
\tag{3.9}
\]

which is exact Hall failure at demand two.  The other partition in (3.5)
has demand three: its maximum singleton clique is `{x_d,x_e}`.

This is the smallest possible boundary order in (3.1), uses the strongest
nontrivial two-block Hall failure, and has `|F|=1` in Lemma 2.1.  Yet the
partitions in (3.5) remain different.  Therefore neither the coupled
switch formulas nor the exact Hall certificate supplies a common partition.

## 4. Literal realization of the switch and support data

For completeness, the deterministic verifier constructs a finite graph
containing the tableau.  Its two deleted edges are `uw,qw`.  It has two
components outside `B`, called `E` and `C`, and

\[
                         C=Q_0\mathbin{\dot\cup}Q_1.
\tag{4.1}
\]

The subgraphs `Q_0,Q_1` are connected, adjacent and have exactly the
contacts described above.  The vertex `e` belongs to `Q_0`, both subgraphs
have a neighbour at `e`, and the edges `ex_e,ey_e,x_ey_e` give the second
old boundary triangle.

In the central colouring, the `{0,4}`-component through `u` meets `B`
exactly in `{y_d}`, the `{0,1}`-component through `q` meets `B` exactly in
`{d}`, and their only edge with a colour-4 end in the first and a colour-1
end in the second is `y_dd`.  Switching the first component properly
colours `G-qw` and induces `Sigma_E`; switching the second properly colours
`G-uw` and induces `Sigma_C`.

The realization is deliberately only a local shell.  Its low-degree
subdivision vertices make it far from seven-connected, so it cannot be
used against a theorem which converts failure into a small separator.

The verifier is
[`hc7_order8_coupled_response_hall_tableau_barrier_verify.py`](hc7_order8_coupled_response_hall_tableau_barrier_verify.py).

## 5. Consequence for the active proof step

Proposition 3.1 and Hall failure can close the branch only through an
additional host-level statement.  Such a statement must couple the literal
joining set `F` or an intersection `A\cap D` to at least one of:

- a third connected subgraph meeting one complete required boundary set;
- a full neighbourhood of order seven carrying the same complete boundary
  partition on both closed shores; or
- an explicit `K_7`-minor construction.

Comparing the two equality partitions, even when their switches have one
literal joining edge and the Hall deficiency has demand exactly two, is
insufficient.
