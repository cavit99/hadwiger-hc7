# Equal/equal active-face repair forces literal boundary anchors

**Status:** proved and independently audited.  The theorem turns a
low-load failed-web page into a state-preserving one-sided repair and then
converts every remaining Kempe obstruction on the opposite shore into
literal rooted paths.  It does not yet package those paths into a `K_7`, a
fixed pair, or a strict exact-seven handoff.

## 1. A state-anchored component-switch lemma

Let

\[
                 G=G_L\cup G_R,
 \qquad          S=V(G_L)\cap V(G_R),                 \tag{1.1}
\]

where there is no edge between `V(G_L)-S` and `V(G_R)-S`.  Let

\[
                 e=ab\in E(G_R-S)                    \tag{1.2}
\]

and let `kappa` be a `q`-colouring of `G_R-e` with

\[
                 \kappa(a)=\kappa(b)=i.               \tag{1.3}
\]

Suppose that `lambda` is a proper `q`-colouring of `G_L` whose restriction
to `S` equals that of `kappa`.  Thus `lambda` and `kappa` glue to a
`q`-colouring of `G-e` in which `e` is the only possible monochromatic
edge.

### Lemma 1.1 (locked pair or two literal anchors)

If `G` is not `q`-colourable, then for every colour `j!=i` one of the
following holds in the literal bichromatic graph

\[
          (G_R-e)[\kappa^{-1}(\{i,j\})].               \tag{1.4}
\]

1. there is an `a-b` path; or
2. there are vertex-disjoint paths `P_a,P_b` from `a,b`, respectively, to
   two distinct vertices of `S`, and the interiors of both paths avoid
   `S`.

#### Proof

Let `C_a,C_b` be the two bichromatic components containing `a,b`.  If they
are equal, that component contains the path in outcome 1.

Suppose they are distinct.  If, say, `C_a` avoids `S`, interchange `i` and
`j` on the whole component `C_a`.  This preserves properness of the
colouring of `G_R-e`, makes `ab` proper, and leaves every colour on `S`
unchanged.  The switched colouring therefore still glues to `lambda`, now
giving a proper `q`-colouring of all of `G`, a contradiction.  Hence both
`C_a` and `C_b` meet `S`.

In each component choose a shortest path from its named endpoint to `S`
and stop at its first vertex of `S`.  The two paths are disjoint because
their components are distinct.  Their terminal vertices in `S` are also
distinct, and their interiors avoid `S` by construction.  This is outcome
2.  \(\square\)

The statement uses literal components and literal boundary vertices.  It
does not identify the alternate colour `j` with a branch-set label.

## 2. Repairing one edge from an equal/equal state

Retain (1.1).  Let

\[
                 f=dt,
 \qquad          d\in V(G_L)-S,
 \qquad          t\in S,                              \tag{2.1}
\]

and assume that `e,f` are vertex-disjoint.  Suppose `D=G_L-S` is connected
and has a plane embedding with a facial cycle `F` containing every vertex
of `D` which has a neighbour in `S`.

Because `a,b in V(G_R)-S`, the shore anticompleteness in (1.1) gives

\[
                         E_G(D,\{a,b\})=\varnothing.    \tag{2.2a}
\]

Let `kappa` be a proper `q`-colouring of `G-{e,f}` satisfying

\[
       \kappa(a)=\kappa(b),
 \qquad\kappa(d)=\kappa(t).                            \tag{2.2}
\]

For `x in D`, put

\[
       L_\kappa(x)=[q]-\kappa(N_G(x)\cap S).            \tag{2.3}
\]

### Lemma 2.1 (active-face one-conflict repair)

Assume `q>=6` and

\[
       |\kappa(N_G(x)\cap S)|\le q-3
                         \qquad(x\in V(F)).             \tag{2.4}
\]

Then the restriction of `kappa` to `G_R` extends across `D` to a proper
`q`-colouring `phi` of `G/e`.  Moreover,

\[
                 \phi|_{G_R}=\kappa|_{G_R}.             \tag{2.5}
\]

In particular the exact equality partition induced on every labelled
subset of `S` is unchanged.

#### Proof

Every facial list in (2.3) has order at least three by (2.4).  A vertex of
`D-F` has no neighbour in `S`, so its list is the full set `[q]`, of order
at least six and hence at least five.  Choose an edge `xy` of `F` and
distinct colours from `L_\kappa(x),L_\kappa(y)`.  Thomassen's
precoloured-outer-edge list-extension theorem gives an `L_\kappa`-colouring
of `D`.

The list definition makes every edge from `D` to `S` proper.  In
particular `d` receives a colour different from `kappa(t)`, so the edge
`f=dt` is repaired.  The restriction of `kappa` to `G_R` is proper except
for the equal pair `ab`; after identifying that pair it is a proper
colouring of `G_R/e`.  Equation (2.2a) ensures that identifying `a,b`
creates no unrecorded edge from their image into `D`.  Gluing the
list-colouring of `D` to that fixed
restriction therefore gives the claimed colouring of `G/e`, and (2.5) is
built into the construction.  \(\square\)

The proof repairs `f` without changing even one vertex of the opposite
closed shore.  This is stronger than merely producing some colouring of
`G/e`.

## 3. Twin-seam consequence

Use the frozen atomic twin-seam notation

\[
 e=zu,
 \qquad f=dt,
 \qquad S=\Omega_D,
 \qquad G_L=G[D\cup\Omega_D],
 \qquad G_R=G[B_D\cup\Omega_D].                        \tag{3.1}
\]

Here `z,u in B_D`, `d in D`, and `t in Omega_D`.  Let `kappa` be a
six-colouring of `G/e/f`, expanded to `G-{e,f}`.  It is the audited
equal/equal state.  Suppose the failed-RST planarization has an active
facial cycle `F` containing every `Omega_D` attachment to `D`, and suppose

\[
       |\kappa(N_G(x)\cap\Omega_D)|\le3
                         \qquad(x\in V(F)).             \tag{3.2}
\]

### Theorem 3.1 (equal/equal active-face anchor exchange)

There is a six-colouring `phi` of `G/e`, expanded to `G-e`, such that

\[
                 \phi|_{B_D\cup\Omega_D}
                    =\kappa|_{B_D\cup\Omega_D}.        \tag{3.3}
\]

Let `i=kappa(z)=kappa(u)`.  For each of the five other colours `j`, the
literal `i-j` subgraph of

\[
                   G[B_D\cup\Omega_D]-e               \tag{3.4}
\]

contains either

1. a `z-u` path; or
2. two vertex-disjoint paths from `z,u` to distinct literal vertices of
   `Omega_D`, with both interiors contained in `B_D`.

Every displayed path avoids `D` and the gate edge `f`.  Thus a low-load
failed page replaces an arbitrary response-matched lock by a literal
opposite-shore lock-or-two-anchor certificate in the **same** equal/equal
boundary state.

#### Proof

Lemma 2.1 with `q=6` gives `phi` and (3.3).  Apply Lemma 1.1 with
`lambda=phi|_{D\cup\Omega_D}` and
`kappa|_{B_D\cup\Omega_D}`.  A proper colouring of `G` is excluded by the
hypothetical-counterexample kernel, so the lemma gives the asserted path
alternative for every `j`.  The two open shores are anticomplete, and the
paths of Lemma 1.1 lie entirely in the right closed shore; stopping at
their first boundary vertices puts their interiors in `B_D`.  Since
`d notin B_D\cup\Omega_D`, none can use `f`.  \(\square\)

### Corollary 3.2 (exact residual after planarization)

For every equal/equal response in the failed-RST branch, at least one of
the following occurs.

1. Some literal `Omega_D` attachment is not on the proposed active facial
   cycle.
2. Some facial vertex sees at least four boundary colours in that response.
3. The state-preserving colouring (3.3) and all five literal
   lock-or-two-anchor certificates of Theorem 3.1 occur.

This trichotomy is exhaustive and contains no palette-to-model lift.

### Theorem 3.3 (sharp nonempty-list refinement)

Retain the active facial cycle and equal/equal colouring of Theorem 3.1,
but do not assume (3.2).  For `x in F`, put

\[
       L(x)=[6]-\kappa(N_G(x)\cap\Omega_D),
 \qquad
       H=\{x\in F:|L(x)|\le2\}.                         \tag{3.5}
\]

Then the anchor conclusion of Theorem 3.1 holds unless at least one of the
following literal list obstructions occurs.

1. Some facial list is empty; equivalently, one facial vertex sees all six
   boundary colours.
2. `|H|>=3`.
3. `H={x,y}`, the list orders are one and two, and `(D,L)` contains a
   colouring harmonica from the singleton-list vertex to the two-list
   vertex in the sense of Postle--Thomas.
4. `H={x,y}` and both lists are singletons, where either `x,y` are
   nonadjacent or their singleton colours are equal.

#### Proof

Assume that all lists are nonempty.  Every vertex off `F` has the full
six-element list, and every facial vertex outside `H` has a list of order
at least three.

If `H` is empty, Lemma 2.1 applies.  If `H={x}`, precolour `x` from its
nonempty list and precolour either facial neighbour with a distinct colour
from its list of order at least three.  Thomassen's outer-edge theorem
colours `D`.

Suppose `H={x,y}`.  If both lists have order at least two, the Two Lists of
Size Two Theorem of Postle and Thomas colours `D`, whether or not `x,y`
are adjacent.  If their list orders are one and two, their one-list/two-list
theorem colours `D` unless the directed colouring-harmonica obstruction in
outcome 3 occurs.  Finally suppose both lists are singletons.  When `x,y`
are adjacent and their singleton colours differ, precolour that outer edge
and apply Thomassen's theorem.  The only cases not covered are precisely
outcome 4.

In every colourable case, the resulting list-colouring repairs `f` while
fixing `kappa` on `B_D union Omega_D`, exactly as in Lemma 2.1.  Lemma 1.1
then supplies all five lock-or-two-anchor certificates.  This proves the
theorem.  \(\square\)

The imported statements are Theorems 1.2 and 1.3 of Postle--Thomas,
[*Five-list-coloring graphs on surfaces III. One list of size one and one
list of size two*](https://arxiv.org/abs/1608.05759).  The former restates
their two-lists theorem from Part I.  Outcome 4 is retained because two
prescribed singleton lists at nonadjacent outer vertices are not covered
by either theorem.

### Corollary 3.4 (four-connected pages have no directed harmonica)

If, in addition, `D` is four-connected and `|F|>=4`, outcome 3 of Theorem
3.3 is impossible.

#### Proof

Let `x` be the singleton-list end and `y` the two-list end of a contained
colouring harmonica.  The first recursive harmonica step contains a literal
triangle `xvw`.  The harmonica definition gives

\[
             L(v)-L(x)=L(w)-L(x)=L_0,
 \qquad      |L_0|=2.                                  \tag{3.6}
\]

The vertices `v,w` are distinct from both `x` and the terminal `y`.
Because `H={x,y}`, their lists have order at least three.  Formula (3.6)
then forces `L(v)=L(w)=L_0 union L(x)`, of order three.  Every vertex of
`D-F` has the full six-element list, so `x,v,w` all lie on `F`.  The outer
facial cycle of a four-connected plane graph is induced, while an induced
cycle of length at least four contains no triangle on three of its
vertices.  This contradiction excludes the harmonica.  \(\square\)

### Theorem 3.5 (every unlocked anchor switch creates a sharp page state)

Retain the active-face setting of Theorem 3.1.  Fix an alternate colour
`j` for which the `i-j` graph in (3.4) has no `z-u` path.  Let `C_z,C_u`
be its two endpoint components.  For `r in {z,u}`, interchange `i,j` on
`C_r`, producing a colouring `rho_r` of
`G[B_D union Omega_D]-e`.

Then:

1. `rho_r` makes `e` proper;
2. its literal boundary colour change is supported exactly on the nonempty set
   `C_r intersect Omega_D`;
3. its induced equality partition on `Omega_D` differs from the original
   equal/equal boundary partition;
4. the two transition supports for `r=z,u` are disjoint; and
5. the active-face list assignment

   \[
          L_r(x)=[6]-\rho_r(N_G(x)\cap\Omega_D)
                         \qquad(x\in D)                 \tag{3.7}
   \]

   is not colourable.  Consequently it has at least one of the four sharp
   obstructions in Theorem 3.3: an empty facial list, at least three heavy
   vertices, a directed one-list/two-list harmonica, or a retained
   double-singleton pair.

#### Proof

The endpoint components are distinct.  The component-switch lemma preserves
properness on the right closed shore and changes exactly one end of `e`,
proving item 1.  Theorem 3.1 and Lemma 1.1 show that both components meet
`Omega_D`; their intersections with the boundary are disjoint because the
components themselves are disjoint.  A component switch changes no vertex
outside its component, proving items 2 and 4.

If `rho_r` induced the original equality partition on `Omega_D`, permute
the colours of the state-preserving left-side colouring `phi` from Theorem
3.1 so that its boundary colours agree with `rho_r`.  The two closed-side
colourings would then glue; `phi` repairs `f` and `rho_r` repairs `e`, so
the result would be a six-colouring of `G`.  This proves item 3.

If (3.7) coloured `D`, glue that list-colouring to `rho_r`.  Every
`D-Omega_D` edge is proper by the list definition, including `f=dt`, while
`e` is proper by item 1.  This would six-colour `G`.  Hence (3.7) is not
colourable.  The list case analysis in the proof of Theorem 3.3 applies
verbatim to `rho_r`; whenever none of the four recorded obstructions is
present it supplies such a list-colouring.  This proves item 5.  \(\square\)

Thus an unlocked equal/equal lock is not merely a pair of paths.  It gives
two disjointly supported boundary moves, and **each** move is certified
by a named planar list obstruction.  This is the finite state-transition
object to be composed with packet reflection or the global rank.

### Corollary 3.6 (support algebra and packet demand)

For the transition `rho_r`, let

\[
 I=\{s\in\Omega_D:\kappa(s)=i\},\qquad
 J=\{s\in\Omega_D:\kappa(s)=j\},\qquad
 A_r=C_r\cap\Omega_D.                                 \tag{3.8}
\]

Then `A_r` is a nonempty proper subset of `I union J`.  More precisely,
switching `i,j` on a subset `A subseteq I union J` preserves the unlabelled
equality partition of `Omega_D` if and only if

\[
                         A=\varnothing
             \quad\hbox{or}\quad A=I\cup J.            \tag{3.9}
\]

In the normalized symmetric twin-seam cell, where
`nu_{B_D}^{Omega_D}=1`, let `Pi_r` be the equality partition induced by
`rho_r`.  Then

\[
                         d_{G[\Omega_D]}(\Pi_r)\ge2.    \tag{3.10}
\]

#### Proof

Only vertices in `I union J` can lie in the switched bichromatic
component.  Formula (3.9) follows by comparing the two old colour blocks
`I,J` with the two new blocks

\[
 (I-A)\cup(A\cap J),\qquad (J-A)\cup(A\cap I).
\]

The support `A_r` is nonempty by Theorem 3.5(2), and Theorem 3.5(3)
excludes the second partition-preserving possibility in (3.9).  This
proves the first assertion.

For (3.10), suppose instead that `d(Pi_r)<=1`.  Apply exact packet
reflection to the one `Omega_D`-full packet in `B_D`, the open shore on
which `rho_r` is already colour-intact.  It gives either a literal `K_7`
or a proper colouring of the opposite closed shore `D union Omega_D`
whose exact boundary partition is `Pi_r`.  The first outcome is excluded
by the kernel.  In the second, permute its palette to agree with `rho_r`
on `Omega_D` and glue.  The opposite-shore colouring is proper on `f`,
while `rho_r` is proper on `e`, so this six-colours `G`, again impossible.
Thus `d(Pi_r)>1`, proving (3.10).  \(\square\)

The conclusion is deliberately state-level.  Two disjoint transition
supports carrying demand at least two are not automatically two disjoint
model rows or a strict global handoff.

## 4. Exact remaining gap

Theorem 3.1 is a uniform rooted-path principle, but it is not the atomic
double-lock exchange theorem.  Paths belonging to different alternate
colours may intersect, their boundary endpoints need not represent five
different duties, and a `z-u` lock is not a model row.  The remaining
decoder must use the reserve packets, the crossed proper/equal response,
and the global `mathcal F_12(G)` rank to turn the five certificates into
one of:

1. a common exact state and six-colouring;
2. a literal `K_7` or coherent fixed pair; or
3. a strictly smaller packet-one exact-seven handoff.

After Theorem 3.3, the active-face failures are no longer an undifferentiated
high-load class: they are a six-colour-saturated portal, at least three
two-list portals, one directed harmonica, or a double-singleton pair.  The
off-face alternative and these four structures remain live and must be
handled by the same terminal/rank discipline.
