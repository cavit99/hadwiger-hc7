# The double same-bag residue: a sharp width-five counterarchitecture

## 1. Purpose

This note tests the strongest conclusion that can be drawn from the
static data now available in the double same-bag degree-nine Moser cell.
It gives an infinite family which simultaneously retains

* a balanced spanning rooted (K_4)-model;
* the two same-bag attachment alternatives;
* an ordered root-to-residue portal spine on each side;
* arbitrarily many distinct portals in every strict ordered-prefix row;
* the old cross-carrier edges (6R_0) and (5L_0); and
* global minimality of the ordinary-bag size potential.

Nevertheless every member has treewidth at most five.  Thus these data
alone force neither a (K_7)-minor nor a simultaneous root swap which
decreases the potential.  This is a sharpness construction, **not** a
hypothetical Hadwiger counterexample: it is not seven-connected and is
not contraction-critical.  Its role is to identify the precise extra
input that the double-spine closure theorem must use.

## 2. Construction

Fix integers (m\ge2) and (c\ge3).  Start with the pure Moser
neighbourhood on

\[
                 \{h,1,2,3,4,5,6\}
\]

and add the apex (v).  Thus the neighbourhood edges are

\[
 h1,h2,h3,h4,12,16,26,34,35,45,56,
\]

and (v) is adjacent to all seven neighbourhood vertices.

Add vertices

\[
 k,j,Q,R,
 \quad u_0,\ldots,u_{m-1},
 \quad w_0,\ldots,w_{m-1},
\]

and capacity vertices

\[
 x_1,\ldots,x_c,\qquad y_1,\ldots,y_c.
\]

The left edges are

\[
 k6,quad ku_i\ (0\le i<m),quad
 u_0u_1\cdots u_{m-1}Q,quad Q5,
\]

and (k,u_0) are each complete to ({h,1,2}).  For every (a),
add the triangle edges (kx_a,x_au_0).  Symmetrically, the right
edges are

\[
 j5,quad jw_i\ (0\le i<m),quad
 w_0w_1\cdots w_{m-1}R,quad R6,
\]

and (j,w_0) are each complete to ({h,3,4}).  Add
(jy_a,y_aw_0) for every (a).  Finally add the old ordinary-bag
edge (QR).  There are no further edges.

The script `degree9_complementary_star_probe.py`, function
`build_double_same_spines(m,c)`, constructs this graph exactly (with
the labels `D=6` and `C=5`).

## 3. The retained balanced model

Use

\[
\begin{aligned}
 L_6&=\{6,k,x_1,\ldots,x_c\},\\
 L_0&=\{u_0,\ldots,u_{m-1},Q\},\\
 R_5&=\{5,j,y_1,\ldots,y_c\},\\
 R_0&=\{w_0,\ldots,w_{m-1},R\}.
\end{aligned}                                             \tag{3.1}
\]

These four connected sets partition the vertices outside
({v,h,1,2,3,4}).  They form a clique model through

\[
 k u_0,quad 65,quad 6R,quad Q5,quad QR,quad jw_0.       \tag{3.2}
\]

The left roots (k,u_0) see (h,1,2), the right roots (j,w_0)
see (h,3,4), and (6,5) are in the indicated outer bags.

Let (K=L_6-6) and (J=R_5-5).  Then

\[
 K\not\sim R_5,R_0,qquad J\not\sim L_6,L_0,               \tag{3.3}
\]

so both gates are in the same-bag cell.  The old opposite carrier
contacts (6R_0) and (5L_0), as well as (L_0R_0), are retained.

Inside (L_0), every (k)-portal lies on the literal ordered spine

\[
 u_0-u_1-\cdots-u_{m-1}-Q,                                \tag{3.4}
\]

with the exterior root at (u_0) and both far-side contacts at (Q).
The right side has the symmetric order.  Thus this is the exact
root-bearing terminal geometry, not a quotient in which the order has
been forgotten.

## 4. Strict prefix capacities and the linkage obstruction

For (1\le i<m), put

\[
 P_i=\{u_0,\ldots,u_{i-1}\}.
\]

Its neighbours in the left outer root component (K) include the
(c+1) distinct vertices

\[
                         k,x_1,\ldots,x_c.                 \tag{4.1}
\]

Hence every ordered-prefix row has at least four distinct outer-bag
neighbours when (c\ge3), exactly matching the strict-surplus lower
bound.  The same holds on the right.

The multiplicity does not create the required rooted exchange.  In
the left outer root component, the only vertex adjacent to (6) is
(k).  Consequently there is no connected bipartition

\[
                         K=E\mathbin{\dot\cup}T             \tag{4.2}
\]

with (k\in E) and (T\sim6).  In particular there is no split with

\[
 k\in E,quad E\sim S_i,quad T\sim P_i,6,                 \tag{4.3}
\]

as required by the two-left-bag root exchange.  All (P_i)-to-(6)
linkages in (K\cup\{6\}) use the root (k).  Symmetrically, every
right exchange is blocked at (j).

Thus the two sides exhibit the **same joint obstruction**: portal
capacity is large, but all capacity is attached behind the root which
also uniquely owns the carrier edge.  Counts do not distinguish this
from a splittable capacity state.

## 5. The ordinary-bag potential is already globally minimal

Consider every spanning rooted (K_4)-model on the same vertex set
with roots (k,u_0,j,w_0), permitting the two roots on either half to
exchange their outer/ordinary roles.  Require the outer left bag to
contain (6) and the outer right bag to contain (5).  Define

\[
 \Phi=|\text{left bag not containing }6|
       +|\text{right bag not containing }5|.               \tag{5.1}
\]

### Proposition 5.1

Every such model has

\[
                              \Phi\ge2(m+1),                \tag{5.2}
\]

and (3.1) has equality.

#### Proof

First, the bag rooted at (u_0) cannot contain (6).  If it did,
connectivity while avoiding the distinct root (k) would force it to
use the unique (u_0)-to-({5,6,R,Q}) corridor

\[
                  u_0u_1\cdots u_{m-1}Q.                  \tag{5.3}
\]

It would therefore contain the whole left spine through (Q).  The
bag rooted at (k) would then have no route or edge to both right-root
bags: outside the Moser boundary, every exit from
({k,x_1,\ldots,x_c}) is through (6) or one of the (u_i), all
already in the other left bag.  This contradicts the rooted
(K_4)-model adjacencies.  Hence the (k)-bag contains (6).

The ordinary (u_0)-bag must be adjacent to both right-root bags.
Any connected right-root bag entering the left spine must do so through
(Q) (the other boundary vertex (k) belongs to the first left bag),
and only one disjoint bag can contain (Q).  Therefore the (u_0)-bag
itself contains (Q).  Connectivity avoiding (k) again forces all
vertices of (5.3), so its order is at least (m+1).

The symmetric argument shows that the (j)-bag contains (5) and
that the ordinary (w_0)-bag contains the entire right spine through
(R), also of order at least (m+1).  This proves (5.2), and (3.1)
attains it. \(\square\)

For an independent finite check, the exact assignment routine
`min_balanced_ordinary_sum` enumerates all (4^{10}) assignments for
((m,c)=(4,0)) and returns

\[
  \Phi=10,quad
  (\{k,6\},\{u_0,u_1,u_2,u_3,Q\},
    \{j,5\},\{w_0,w_1,w_2,w_3,R\}).                       \tag{5.4}
\]

The capacity vertices are simplicial on an edge and can be assigned to
the corresponding outer bag without changing the lower-bound argument.

## 6. Uniform width-five certificate

### Proposition 6.1

Every graph in the family has treewidth at most five and hence has no
(K_7)-minor.

#### Proof

First eliminate every (x_a) and (y_a); each has two adjacent later
neighbours.  Next eliminate

\[
 u_1,u_2,\ldots,u_{m-1},qquad
 w_1,w_2,\ldots,w_{m-1}.                                  \tag{6.1}
\]

The successive later-neighbour sets on the left are
({k,u_0,u_{i+1}}), with (Q) replacing (u_{i+1}) in the last
step; the right side is symmetric.  Finish with

\[
 u_0,k,1,2,w_0,j,3,4,5,6,Q,R,h,v.                         \tag{6.2}
\]

The largest filled later-neighbour sets are

\[
\begin{array}{c|c}
u_0&\{1,2,k,Q,h\}\\
k&\{1,2,6,Q,h\}\\
1&\{2,6,Q,h,v\}\\
w_0&\{3,4,j,R,h\}\\
j&\{3,4,5,R,h\}\\
3&\{4,5,R,h,v\}\\
5&\{6,Q,R,h,v\}.
\end{array}                                                \tag{6.3}
\]

Every other set is smaller.  This is a width-five elimination order.
Since treewidth is minor-monotone and (operatorname{tw}(K_7)=6),
no member contains a (K_7)-minor. \(\square\)

Even adding both root-to-residue diagonals (kQ) and (jR) leaves
the same family of width-five certificates.  Thus one bypass on each
side is still insufficient when both bypasses use the unique carrier
owner.

## 7. Consequence for the live proof programme

The following implication is false:

> double same-bag attachment + ordered spines + strict portal counts +
> old cross-carrier edges + global potential minimality implies a
> (K_7)-minor or a smaller balanced model.

The missing hypothesis must distinguish **distributed linkage** from
capacity concentrated at one carrier-owning root.  In the actual
Hadwiger residue, the only presently available sources of that extra
information are:

1. seven-connectivity of the whole host, used in a label-preserving
   way rather than merely to count portals;
2. the one-step deletion/contraction colouring transitions; or
3. a two-shore capacity-state exchange theorem whose failure outputs a
   genuine adhesion that is colour-gluable.

A correctly sharp next lemma should therefore have a third outcome:

\[
\boxed{\text{paired exchange or }K_7\text{ model or a certified
small/knitted adhesion}.}                                  \tag{7.1}
\]

The construction realizes the adhesion outcome.  Any lemma omitting it
is disproved even after all currently known static portal data and
potential minimality are retained.
