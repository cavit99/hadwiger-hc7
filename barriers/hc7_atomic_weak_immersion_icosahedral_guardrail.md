# Atomic weak-immersion guardrail in the two-apex icosahedron

**Status:** explicit barrier to collision-only completion and
collision-location descent; computer-assisted finite certificate; separate
internal audit GREEN.

This example is not a counterexample to `HC_7` or to an atomic theorem that
allows a global two-vertex `K_5`-model transversal or an order-seven
separation.  It realizes both of those terminal outcomes.  Its purpose is to
show that one atomic weak `K_7`-immersion, even together with the two opposite
singleton-root near-`K_7` models obtained by rounding it, does not by itself
identify the terminal pair or orient a collision descent.

The deterministic checker is
[`hc7_atomic_weak_immersion_icosahedral_guardrail_verify.py`](hc7_atomic_weak_immersion_icosahedral_guardrail_verify.py).

## 1. The host

Let `I` be the icosahedral graph with vertices

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and, with subscripts modulo five, edges

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.
\]

Add adjacent vertices `p,q`, each complete to `I`, and put

\[
                              G=K_2\vee I.
\]

The graph `I` has its standard spherical triangulation.  Consequently it is
planar and has no `K_5` minor.  It is also five-connected.  If at most six
vertices are deleted from `G`, either an apex remains and connects every
remaining vertex, or both apices and at most four vertices of `I` were
deleted.  Hence `G` is seven-connected.

The graph has no `K_7` minor.  Indeed, after removing from a hypothetical
`K_7` model the at most two branch sets which contain `p` or `q`, at least
five pairwise adjacent connected branch sets would remain wholly in `I`.
That would give a `K_5` minor in the planar graph `I`.

## 2. One atomic immersion

Use branch vertices

\[
                       p,q,t,u_0,u_1,u_3,w_1.
\]

Use the literal edge for every adjacent branch pair, and use the following
five paths for the nonadjacent pairs:

\[
\begin{array}{c|c}
\text{demand pair}&\text{path}\\ \hline
t,w_1&t-u_2-w_1\\
u_1,u_3&u_1-u_2-u_3\\
u_0,u_3&u_0-u_4-u_3\\
u_0,w_1&u_0-w_0-w_1\\
u_3,w_1&u_3-w_2-w_1.
\end{array}
\]

All 21 paths are pairwise edge-disjoint.  No branch vertex is internal on a
path.  The vertex `u_2` is internal on exactly the first two displayed
paths, whose demand edges are disjoint; `u_4,w_0,w_2` each occur internally
on one path, and there is no other internal vertex.  This is therefore an
atomic strong `K_7` immersion.

The two spanning rounded models from the atomic rounding theorem can be
taken literally as follows.  Omitting the `t-w_1` route gives the exact
`K_7-tw_1` model

\[
 \{t\},\ \{w_1\},\ \{p\},\ \{q\},\
 \{u_0,u_4,w_0\},\ \{u_1,u_2\},\
 \{u_3,w_2,b,w_3,w_4\}.
\]

Omitting the `u_1-u_3` route gives the exact `K_7-u_1u_3` model

\[
 \{u_1\},\ \{u_3\},\ \{p\},\ \{q\},\
 \{t,u_2\},\ \{u_0,u_4,w_0\},\
 \{w_1,w_2,b,w_3,w_4\}.
\]

In particular, the two deficient pairs are disjoint, and neither is the
terminal pair below.

## 3. The terminal pair and exact separator

Every `K_5` minor model in `G` meets `{p,q}`.  A model avoiding both vertices
would lie in `I`, contradicting planarity.  Thus `{p,q}` meets every ordinary
`K_5` model and, a fortiori, every dominating `K_5` model.

Moreover,

\[
                      \{p,q,u_0,u_1,u_2,u_3,u_4\}
                       =\{p,q\}\cup N_I(t)
\]

is an actual separator of order seven: deleting it isolates `t` from the
connected subgraph on `b,w_0,\ldots,w_4`.

The collision endpoints therefore do not reveal the global terminal pair.
Thus the two rounded deficient pairs need not themselves be terminal.  A
proof may still exploit other host data; the example only rules out reading
the global pair directly from those two pairs.

## 4. Equal-score relocation

The first immersion avoids `w_4` completely.  The same graph has another
atomic immersion with the same
[bookkeeping potential](../results/hc7_atomic_weak_k7_immersion_rounding.md#4-impact-on-the-weak-immersion-programme)
`(M,T,H,L)=(1,0,0,26)` and `Q=1`, but avoiding `u_2` completely.
Use branch vertices

\[
                         p,q,t,u_0,u_4,w_0,w_3
\]

and literal edges for adjacent branch pairs, together with

\[
 t-u_1-w_0,\quad t-u_3-w_3,\quad u_0-w_4-w_3,
 \quad u_4-w_4-w_0,\quad w_0-b-w_3.
\]

Here `w_4` is the unique collision vertex, on the disjoint demands
`u_0-w_3` and `u_4-w_0`; `u_1,u_3,b` are private internal vertices.  Both
immersions use 26 edges.  Consequently, replacing an immersion by one which
avoids its old collision need not decrease this potential or the number of
collision vertices.  The two witnesses give a literal equal-potential
two-way relocation between `u_2` and `w_4`.

This refutes the proposed local descent

> choose an immersion avoiding the current collision vertex and conclude
> that the collision potential decreases.

It does not refute a host-level potential which also detects the persistent
two-apex pair; no such potential is proved here.

## 5. The paired-linkage obstruction in the common frame

For the first collision, use the common partition of `G-u_2`

\[
 \{t\},\ \{w_1\},\ \{u_1\},\ \{u_3,w_2,b,w_3,w_4\},
 \quad \{u_0,u_4,w_0\},\ \{p\},\ \{q\}.
\]

Its two missing pairs are `t-w_1` and `u_1-u_3`; the collision vertex
`u_2` meets the first four bags and the two apex bags, but misses the clean
bag `D=\{u_0,u_4,w_0\}`.  Every connected subgraph of `D` adjacent to both
`{t}` and `{w_1}` meets every connected subgraph of `D` adjacent to both
`{u_1}` and `\{u_3,w_2,b,w_3,w_4\}`.  The checker exhausts the seven
nonempty subsets of this three-vertex bag and verifies the assertion.

Thus the paired linkage from Theorem 3.5 can genuinely fail at the sharp
terminal example.  This finite check illustrates the obstruction; the
general singleton-allocation proposition in the companion result explains
why connectivity alone cannot eliminate it.

## 6. Minimum excess does not control collision degree

There is also an atomic branch-transit witness whose collision is the
degree-13 apex `p`.  Use branch vertices

\[
                         b,p,q,t,u_0,u_1,u_2
\]

and every available direct branch-pair edge except those consumed below.
Use the seven nontrivial paths

\[
\begin{gathered}
 b-w_3-u_3-t,\quad b-w_4-u_0,\quad b-w_0-u_1,\quad
 b-w_1-u_2,\\
 p-u_4-u_0,\quad p-w_2-u_2,\quad u_0-p-u_2.
\end{gathered}
\]

The first six paths replace their corresponding nonedge or consumed direct
edge; the final path is the `u_0-u_2` demand and passes through the branch
vertex `p`.  All path edges are distinct.  Thus `p` has its branch role and
one foreign transit role, while every other vertex has at most one role.
The total excess is `M=1` and the route length is 29.

Since this host has no `K_7` minor, no immersion has `M=0`; hence `M=1` is
globally minimum.  Minimizing collision excess alone therefore does not
force a collision of degree at most nine.  This does not refute the fuller
tie-break `(M,T,H,L)`: the two non-branch witnesses above have `T=0` and
are preferred to this branch-transit witness, which has `T=1`.  Nor does it
refute an existential low-degree choice in another host.  It fixes the
scope of the averaging argument precisely.
