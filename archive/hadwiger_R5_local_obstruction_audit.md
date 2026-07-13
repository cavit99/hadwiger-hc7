# Audit of the claimed (R_5) reduction

This note records a finite obstruction to any attempt to eliminate the
(s=5) residual using only the stated portal/(U)-set/(Phi) calculus.  It is
**not** a counterexample to (mathrm{HC}_7): it fails the global minimum-degree
and connectivity hypotheses.

## 1. The graph

Let

\[
V(H)=\{v,y,a,b,c,d,e,f,g\}.
\]

There is no edge (vy).  Both (v) and (y) are adjacent to every vertex of
({a,b,c,d,e,f,g}).  The remaining edges are

\[
ab,\ cd,\ ac,\ ae,\ bf,\ bg,\ ce,\ df,\ dg,\ ef,\ eg,\ fg.
\]

Equivalently, the adjacency lists are

\[
\begin{array}{c|l}
v&a,b,c,d,e,f,g\\
y&a,b,c,d,e,f,g\\
a&v,y,b,c,e\\
b&v,y,a,f,g\\
c&v,y,d,a,e\\
d&v,y,c,f,g\\
e&v,y,a,c,f,g\\
f&v,y,b,d,e,g\\
g&v,y,b,d,e,f.
\end{array}
\]

Fix the following branch sets in (H-v):

\[
B_1=\{a,b\},\quad B_2=\{c,d\},\quad B_3=\{e\},\quad
B_4=\{f\},\quad B_5=\{g\},\quad B_6=\{y\}.
\]

They are connected.  The model edges can be chosen as follows:

\[
\begin{array}{c|ccccc}
 &B_2&B_3&B_4&B_5&B_6\\ \hline
B_1&ac&ae&bf&bg&ay\\
B_2&&ce&df&dg&cy\\
B_3&&&ef&eg&ey\\
B_4&&&&fg&fy\\
B_5&&&&&gy.
\end{array}
\]

Thus this is a (K_6)-model.  It partitions (V(H-v)), so (Z=\varnothing).
The apex contacts (B_1,ldots,B_5), but not (B_6), hence (s=5) and
(C=B_6=\{y\}).

## 2. Fan and portal data

The seven paths

\[
v-x-y\qquad(x\in\{a,b,c,d,e,f,g\})
\]

are internally disjoint.  They form a maximum (v)-(y) package because
(d_H(v)=7).  Moreover this maximum package is unique as an unordered
package: its seven paths have pairwise disjoint interiors drawn from the
seven available nonterminal vertices, so every path has exactly one internal
vertex.  Consequently

\[
L=\{a,b,c,d,e,f,g\}.
\]

Every (v)-(y) path, maximum or not, has its last exit in this same set,
because (N(y)\setminus\{v\}=\{a,b,c,d,e,f,g\}).

For (U(x)=\{k:x\text{ is the unique }B_i\text{-side attachment to }B_k\}),
the values are

\[
\begin{aligned}
U(a)&=\{2,3\},&U(b)&=\{4,5\},\\
U(c)&=\{1,3\},&U(d)&=\{4,5\},\\
U(e)&=\{1,2,4,5,6\},\\
U(f)&=\{1,2,3,5,6\},\\
U(g)&=\{1,2,3,4,6\}.
\end{aligned}
\]

For example, the only (B_1)-(B_2) and (B_1)-(B_3) edges are (ac)
and (ae), while the only (B_1)-(B_4) and (B_1)-(B_5) edges are
(bf) and (bg).  The two (B_1)-(B_6) edges (ay,by) prevent (6)
from belonging to either (U(a)) or (U(b)).  The calculation for (B_2)
is symmetric.  A singleton branch set has its sole vertex as its unique
attachment vertex to every other branch set.

Thus (B_1) and (B_2) are precisely saturated double-portal,
multi-contact bags: their two (U)-sets partition the four other contact
indices.

## 3. Rigidity and the local hard-core conditions

In (G[B_1]=K_2), neither (a) nor (b) is a cutvertex: deleting either
leaves one connected vertex.  Likewise neither (c) nor (d) is a
cutvertex of (G[B_2]).  Therefore (R1) is false at (a,b,c,d).  It is
also false at each singleton (e,f,g) under the standard cutvertex
definition.

The (R2) condition is false at (a,b), since
(N(v)\cap B_1=\{a,b\}), and false at (c,d) for the same reason.  It is
true at (e,f,g), each of which is the sole contact representative of its
singleton bag.

The displayed nonempty (U)-sets show that (R3) holds at every portal.
Consequently (a,b,c,d) are pure-(R3) portals, while (e,f,g) are mixed
(R2+R3), not pure-(R2).  Hence every last exit of every maximum or rooted
(v)-(C) path is rigid.

The (R3) instances at (a,b,c,d) are essential in the precise local sense
of RPC Theorem 6.3:

* after deleting (a), every path from (b) to (B_2) or (B_3) starts
  outside (B_1) through one of the singleton bags (B_4,B_5,B_6);
* after deleting (c), the symmetric statement holds from (d);
* after deleting (b), every path from (a) to (B_4) or (B_5) first
  uses (c,e), or (y); (e,y) are singleton-bag vertices and (c) is
  itself a unique attachment of (B_2);
* after deleting (d), the symmetric statement holds with first hop
  (a,e), or (y).

Thus every possible detour has an internal vertex that is either in a
singleton branch set or is itself a unique attachment.  No detour satisfies
the leaf-Steiner hypothesis.  For (e,f,g), deleting the portal empties its
source bag, so the bridge repair is unavailable.  There are no cutvertex
portals and therefore no free cut sides.  The (R2) size condition also
holds: (|B_6|=1\ge |B_i|-1=0) for (i=3,4,5).  Finally (C) is a
singleton, so it has no removable leaf-Steiner vertex.

Accordingly the example satisfies the **local** hard-core/locked-core
conditions and lies in the terminal combinatorial shape called (R_5):
the multi-portal bags are non-cut, multi-contact, have two portals, and each
of those portals has (|U|=2).

## 4. Exhaustive model certificate

There is also a short hand check of uniqueness.  Put (F=H-v).  Its clique
number is four, and its four (K_4)'s are

\[
\{a,c,e,y\},\quad\{b,f,g,y\},\quad\{d,f,g,y\},\quad
\{e,f,g,y\}.
\]

A (K_6)-model supported on six vertices would be a (K_6) subgraph.  One
supported on seven vertices has five singleton branch sets, which would span
a (K_5).  Neither is possible.  A model on all eight vertices has branch
sizes either (3,1,1,1,1,1), again forcing a (K_5) on the singleton
sets, or (2,2,1,1,1,1).  In the latter case the four singleton sets must
be one of the four displayed (K_4)'s.  The complement-pair check is:

\[
\begin{array}{c|c|c}
\text{singleton }K_4&\text{possible connected pairings of its complement}
 &\text{obstruction}\\ \hline
acey&(bf,dg),(bg,df)&bf\text{ or }bg\text{ misses }c\\
bfgy&(ae,cd)&cd\text{ misses }b\\
dfgy&(ab,ce)&ab\text{ misses }d\\
efgy&(ab,cd)&\text{works (cross-edge }ac\text{).}
\end{array}
\]

This proves directly that the displayed model is unique up to permutation of
the six branch-set labels.

The script [`r5_local_search.py`](r5_local_search.py) enumerates every
unordered partition of every support (W\subseteq V(H-v)), 
(|W|\ge 6), into six nonempty branch sets.  It checks induced connectivity
of each branch set and an edge between every pair.  There are

\[
\binom86 S(6,6)+\binom87 S(7,6)+\binom88 S(8,6)
=28+168+266=462
\]

partitions.  Its output is

```text
vertices ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'y')
edges 19
partitions_checked 462
models 1
best (5, 12)
(5, 12, ({'a','b'}, {'c','d'}, {'e'}, {'f'}, {'g'}, {'y'}))
```

Thus the displayed family is the unique (K_6)-model in (H-v), up to a
permutation of its six labels.  In particular there is no (K_6)-model all
six of whose branch sets meet (N(v)), and the displayed model is the unique
(Phi)-maximizer, with

\[
\Phi=(5,0,-12).
\]

The enumeration includes non-spanning models.  Alternatively, any model in
the connected graph (H-v) can be enlarged to a spanning model by absorbing
each unused component into an adjacent branch set.  The unique spanning
partition then forces the four singleton bags, and neither ({a}) nor
({b}) alone is adjacent to the other five displayed bags (similarly for
(c,d)), so the two doubletons cannot be shrunk.

## 5. Exactly what the example does and does not prove

It proves that the local axioms defining the terminal saturated (R_5)
shape are consistent and do not themselves force either a contact-increasing
reassignment or a six-contact (K_6)-model.

It does **not** satisfy the (t=7) minimal-counterexample package:

\[
\delta(H)=5<7.
\]

Also (N_H(a)=\{v,y,b,c,e\}) separates (a) from the triangle on
({d,f,g\}), so

\[
\kappa(H)\le 5<7.
\]

No claim is made that (H) is (7)-critical, (7)-contraction-critical,
or a counterexample to (mathrm{HC}_7).  Any genuine elimination of (R_5)
must therefore use the global criticality/(7)-connectivity hypotheses in a
way that excludes this explicit local pattern.

There is nevertheless one useful consequence of (7)-connectivity for the
saturated subcell.  Suppose in a genuine standing configuration that (B_i)
has saturated portals (alpha,beta), so their (U)-sets partition
(S\setminus\{i\}).  Put (R=B_i\setminus\{alpha,beta\}).  Saturation says
that no vertex of (R) has a neighbour in any of the other four contact bags.
Since (Z=varnothing),

\[
N_G(R)\subseteq\{\alpha,\beta,v\}\cup (N_G(R)\cap C).
\]

If (R) is nonempty, every other contact bag lies outside
(R\cup N(R)), so (N(R)) is a vertex separator.  Hence

\[
7\le |N(R)|\le 3+|N(R)\cap C|,
\]

and therefore (|N(R)\cap C|\ge4), or at least five if (v) has no neighbour
in (R).  In particular, if (|C|\le3), then (R) is empty.  Thus with
singleton (C), every saturated double-portal bag in a (7)-connected
configuration must be exactly the two-vertex edge
(B_i=\{alpha,beta\}).  The finite obstruction above realizes precisely
this two-vertex escape, though without (7)-connectivity.

## 6. Independent gaps in the claimed reduction to (R_5)

There are also two formal errors before the residual is reached.

1. Moving a non-cut singleton-(U) portal from a bag of size (p) into a
   target bag of size (q) changes the square sum by
   (2(q-p+1)).  Since the third coordinate of (Phi) is minus this sum,
   the move is non-decreasing for (Phi) exactly when (q\le p-1), not
   when (q\ge p-1).  At a (Phi)-maximum, the strict case (q\le p-2)
   is impossible and only (q=p-1) is neutral.  The case (q\ge p) is a
   genuine stuck singleton-(U) case omitted by Theorem A.5.  Therefore the
   conclusion that every terminal non-(R2) portal has (|U|\ge2), and the
   resulting bounds in A.6, do not follow.

2. In Theorem A.2, one private target (B_k) owned by a portal-bearing cut
   side (K) does not imply (U(\alpha')\subseteq\{k\}) for every other
   portal (\alpha'\in K).  The same side may privately own several target
   bags, with distinct portals being their distinct unique attachment
   vertices.  The fact that each fixed target has at most one unique
   attachment vertex only makes those (U)-sets disjoint; it does not make
   their union a singleton.  Hence the asserted cutvertex elimination in
   A.3 is not established by A.2.

3. The proposed two-step raise in Lemma 0.8 does not repair the singleton-
   (U) obstruction.  If (U_old(alpha)=\{k\}) and (alpha) is moved from
   (B_i) into (B_k), every old (B_i)-(B_k) edge becomes internal to the
   enlarged (B_k).  The guaranteed replacement cross-edge is a former
   internal edge (alpha r) with (r in B_i\setminus\{alpha\}).  Consequently
   every guaranteed new (B_k)-(B_i) cross-edge is incident with (alpha):
   in fact (i in U_new(alpha)), rather than (U_new(alpha)=varnothing).
   Moving (alpha) onward from (B_k) into (C) therefore deletes the only
   guaranteed (B_k)-(B_i) attachment and destroys the model.  The claimed
   SPPA second step is unavailable.

There is a further global issue in the RPC reduction: moving a last exit into
(C) raises contact only when the moved last exit is itself in (N(v)).
General last exits of (v)-(C) paths need not be direct neighbours of
(v).  Thus a non-cut, cross-edge-redundant, residual-contact last exit that
is not in (N(v)) is not absorbed by PNCP/SPPA as stated.
