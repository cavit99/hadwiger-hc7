# A failed twin-seam RST pairing has a literal planar quotient

**Status:** proved conditional structural lemma.  It removes every hidden
clique cell from the four-web returned by a failed Robertson--Seymour--
Thomas pairing.  It does not turn the resulting planar quotient into a
rooted `C_4`, a `K_7`, a fixed pair, or a ranked handoff.

## 1. Frozen setting

Use the atomic twin-seam notation

\[
 Z=\{p,q\},\qquad I=T_D\cap T_E,\qquad |I|=3,
\]

\[
 A_0=T_D-T_E=\{a_1,a_2\},\qquad
 C_i=R_i\cup\{a_i\}\quad(i=1,2),
\]

where `R_1,R_2` are the two selected disjoint old `S`-full packets.  In
particular,

\[
 N_G(D)=Z\mathbin{\dot\cup}I\mathbin{\dot\cup}A_0,       \tag{1.1}
\]

and there is no edge from the old thin shore to the old rich shore.  Put

\[
 W=G[D\cup A_0\cup V(R_1)\cup V(R_2)\cup\{p,q\}].       \tag{1.2}
\]

Contract each connected reserve `C_i` to a named root `c_i`, and denote
the resulting literal quotient by

\[
                         Q=W/(C_1\mapsto c_1,
                               C_2\mapsto c_2).          \tag{1.3}
\]

The four roots are `p,c_1,q,c_2`.  Suppose one of the two RST feasibility
tests fails.  The Two Paths Theorem then supplies a same-vertex four-web
completion of `Q`, with the corresponding alternating frame order.  The
completion may add edges, but no new host vertices.

## 2. Cell elimination

### Theorem 2.1 (failed-pair planarization)

Every clique cell of the returned four-web has empty literal interior.
Consequently `Q` itself has a planar embedding in which the four named
roots occur on one face in the web-frame order.

### Proof

Assume that a web cell behind a facial triangle `Delta` contains a
literal vertex of `Q`.  Let `X` be one component of the subgraph of `Q`
induced by the literal vertices in that cell.  By the definition of a web,
every neighbour of `X` in `Q-X` belongs to `Delta`.

None of the four frame roots lies in a cell interior.  All vertices of
`W` outside `D` belong to `C_1`, `C_2`, or `Z`.  It follows that the lift
of `X` to `G` is a nonempty connected subset of `D`.

Each gate vertex of `Delta` contributes at most one literal neighbour to
the lifted set.  This is immediate for an uncontracted gate.  If the gate
is `c_i`, every edge from `D` to its expanded reserve `C_i` ends at the
single vertex `a_i`: equation (1.1) allows `D-A_0` edges, while old
thin--rich anticompleteness forbids every `D-R_i` edge.  Hence the three
web gates lift to a set `L(Delta)` of at most three literal vertices.

Equation (1.1) also shows that the only neighbours of `D` omitted from
`W` are the three vertices of `I`.  Therefore

\[
                         N_G(X)\subseteq
                         L(\Delta)\cup I,
 \qquad                  |N_G(X)|\le 6.                \tag{2.1}
\]

At least one of the four frame roots is not a member of the three-gate
set `Delta`.  Its literal expansion lies outside `X\cup N_G(X)`, since a
cell has no neighbour outside its gate.  Thus `N_G(X)` separates the
nonempty connected set `X` from a nonempty remainder of `G`.  This
contradicts seven-connectivity.  No cell can contain a literal vertex.

Deleting completion-only edges from the remaining plane rib preserves a
planar embedding and leaves `Q` as a literal spanning subgraph.  Its four
frame roots remain incident with the outer face in the certified cyclic
order.  \(\square\)

## 3. Immediate active-face state splice

The planar quotient has one direct proper-minor consequence.  This is
conditional on a **literal active face**; cofaciality of the four
contracted frame roots alone does not place the three omitted `I`-portal
sets on that face.

### Corollary 3.1 (failed-web list splice)

Assume `|D|>=2`.  In the plane embedding inherited from Theorem 2.1,
suppose `D` has a facial cycle `F` containing every vertex of `D` with a
neighbour in

\[
                       \Omega_D=Z\mathbin{\dot\cup}I
                                      \mathbin{\dot\cup}A_0.    \tag{3.1}
\]

Contract a spanning tree of `D` to one vertex `z_D`, take any proper
six-colouring `c` of the proper minor `G/D`, and restrict it to `G-D`.
If

\[
 \bigl|c(N_G(x)\cap\Omega_D)\bigr|\le3
                         \qquad\text{for every }x\in V(F),       \tag{3.2}
\]

then `c` extends across the literal lobe `D` and six-colours `G`.

Consequently, in a hypothetical counterexample, every total-contraction
state has one of the following literal residuals.

1. Some `I`-portal lies off the proposed common active face (or, more
   generally, some `Omega_D` attachment lies off `F`).
2. The heavy set

   \[
      B_c=\{x\in V(F):
          |c(N_G(x)\cap\Omega_D)|\ge4\}                         \tag{3.3}
   \]

   contains two nonadjacent vertices.
3. The heavy set has at least three vertices.
4. Its only two vertices are adjacent on `F`, and both have the same
   singleton list

   \[
      \{1,\ldots,6\}-c(N_G(x)\cap\Omega_D)=\{c(z_D)\}.           \tag{3.4}
   \]

In outcome 4, when `|F|>=4`, deleting or contracting the literal facial
edge joining the two heavy vertices reproduces the same exact boundary
state.  For a triangular active face the singleton-list lock is retained
without that promotion.  A matching state from the opposite shore would
then glue; the corollary does not itself produce that match.

### Proof

For each `x in D`, give `x` the list

\[
                 L(x)=\{1,\ldots,6\}
                    -c(N_G(x)\cap\Omega_D).                       \tag{3.5}
\]

Every vertex strictly inside `F` has no external neighbour and therefore
has the full six-element list.  Under (3.2), every facial list has order
at least three.  Precolour two adjacent vertices of `F` with distinct
available colours and apply Thomassen's outer-face list-extension theorem:
the remaining outer lists have order at least three and every interior
list has order at least five.  The resulting list-colouring of `D` avoids
the colour of every literal boundary neighbour and therefore glues to the
restriction of `c` on `G-D`.  This restores every edge of `G`, including
both named twin-seam edges, and gives the forbidden proper/proper
six-colouring.

The four residuals are the contrapositive and the independently audited
heavy-set sharpening of this same list splice.  The contraction colour
`c(z_D)` lies in every list because `z_D` is adjacent to every member of
`Omega_D`.  If there are zero or one heavy vertices, Thomassen's theorem
still applies after precolouring a suitable outer edge.  If the only two
heavy vertices are adjacent, failure of distinct representatives forces
both lists to be the singleton `{c(z_D)}`.  For `|F|>=4`, the
facial-edge argument can be carried out directly without a connectivity
assumption on `D`: contract their edge `xy` in the displayed plane graph.
The image of `F` is an outer cycle of order at least three.  Give the image
of `xy` the singleton list `{c(z_D)}` and retain every other list.  One of
its outer neighbours has a list of order at least three, so precolour that
neighbour differently and apply Thomassen's theorem.  This colours
`G/xy` while leaving the boundary state fixed.  Splitting the contracted
vertex back into two vertices of colour `c(z_D)` and deleting only `xy`
colours `G-xy` with the same state.  This proves the final assertion.
\(\square\)

## 4. Exact consequence and limit

The failed RST branch is therefore not an arbitrary web with hidden clique
pieces.  It is a literal planar four-root quotient.  The plane rib may
still be arbitrarily large and internally four-connected relative to its
frame.  Seven-connectivity does not make the failed pairing feasible:
the three common labels in `I` are precisely enough to restore global
connectivity while the planar order remains crossed.

No completion edge is a host edge, and the theorem gives no control over
how a spanning common-host `K_6` model intersects the planar page.  A
separate state-sensitive or fixed-pair argument is still required.
