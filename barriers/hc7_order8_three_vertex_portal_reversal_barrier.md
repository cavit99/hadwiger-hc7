# Three-vertex portal classification and the endpoint-reversal barrier

**Status:** written finite classification and computer-assisted barrier;
separate internal audit GREEN in
[`hc7_order8_three_vertex_portal_reversal_barrier_audit.md`](hc7_order8_three_vertex_portal_reversal_barrier_audit.md).  The deterministic verifier is
[`hc7_order8_three_vertex_portal_reversal_barrier_verify.py`](hc7_order8_three_vertex_portal_reversal_barrier_verify.py).
This note concerns one small subcase of the connected order-eight
interface.  It does not prove `HC_7` and the displayed barrier is not a
counterexample to `HC_7`.

## 1. Setting

Let

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
\]

Assume that `G[S]` contains the two vertex-disjoint triangles

\[
 d x_d y_d d,\qquad e x_e y_e e,                 \tag{1.1}
\]

that `d,e` are nonadjacent, and that their degrees in `G[S]` are exactly
two.  Put

\[
                         W=\{x_e,y_e,x_0,y_0\}.    \tag{1.2}
\]

Suppose that `P_0,P_1,D,E` are pairwise disjoint connected subgraphs
outside `S` such that:

1. `P_0,P_1` are adjacent and each is adjacent to every vertex of `S`;
2. `D` is adjacent to every vertex of `S-{d}` and anticomplete to `d`;
3. `E` has three vertices, is adjacent to every vertex of `S-{e}`, and
   is anticomplete to `e`;
4. every vertex of `E` is adjacent to `d` and has a neighbour in `D`;
5. for some `v in E`,

   \[
                       N_E(x_d)=N_E(y_d)=\{v\}.    \tag{1.3}
   \]

These are precisely the static consequences in the order-three residue.
Indeed, the three merged-root Kempe paths enter `E` at three distinct
vertices of three distinct private colours.  Thus all three vertices of
`E` are `d`-portals.  No such path can move from one of these vertices to
another vertex of `E`, because an alternating path for one private colour
cannot use a vertex carrying another private colour.  Its next vertex is
therefore in `D`, proving item 4 pointwise.

Only the two triangles in (1.1) are used below.  Extra forest edges in
`G[S-{d,e}]` can only add adjacencies to the displayed minor models.

## 2. Exact positive classification

### Theorem 2.1

Under the hypotheses of Section 1, `G` contains a `K_7` minor unless all
of the following hold, up to reversing the three-vertex path `E`:

\[
 E=a b c,\qquad v=a,\qquad
 N_E(w)=\{c\}\quad\hbox{for every }w\in W.        \tag{2.1}
\]

In particular, the only static survivor is an induced path whose common
`x_d,y_d` portal is one end and whose four remaining boundary portal sets
are all concentrated at the opposite end.

#### Proof

It is enough to find a vertex `w in W` and a nonempty proper connected
set `C subset E` such that

\[
                         v\in C,\qquad N_E(w)\cap C\ne\varnothing. \tag{2.2}
\]

Put `F=E-C`.  The following seven sets are then pairwise disjoint:

\[
 P_0,\quad P_1,\quad \{d\},\quad\{x_d\},\quad\{y_d\},
 \quad C\cup\{w\},\quad V(D)\cup F\cup\{e\}.     \tag{2.3}
\]

They are connected.  For the last set, every member of `F` has a
neighbour in `D`, and `D` has a neighbour at `e`.  The first two sets are
adjacent and meet every other set through its displayed boundary vertex.
The next three sets form the first triangle in (1.1).  The set
`C union {w}` meets all three through `v` and the fact that every vertex
of `E` is adjacent to `d`.  The final set meets `d` through any member of
the nonempty set `F`, and meets `x_d,y_d` through `D`.  Finally,
`C union {w}` is adjacent to the final set because every vertex of `C`
has a neighbour in `D`.  Hence (2.3) is an explicit `K_7`-minor model.

If `E` is a triangle, take any `w in W` and `q in N_E(w)`.  The set
`{v}` if `q=v`, and `{v,q}` otherwise, satisfies (2.2).  If `E` is a
three-vertex path and `v` is its middle vertex, the same choices work.
Finally suppose `E=abc` and `v=a`.  If any member of `W` has a neighbour
at `a` or `b`, take `C={a}` or `C={a,b}`, respectively.  Thus (2.2) fails
exactly when every one of the four nonempty portal sets is the singleton
`{c}`.  This is (2.1). \(\square\)

The proof is label-preserving: the five branch sets between `P_0,P_1`
are rooted at the literal vertices `d,x_d,y_d,w,e`.  It does not identify
a private colour with a branch-set label.

## 3. The survivor is not excluded by the static hypotheses

The exceptional portal order in (2.1) is genuine.  The following graph
retains an actual proper six-colouring and all three alternating paths.

Take the boundary graph consisting of exactly the two triangles (1.1).
Let

\[
 E=u_1u_2u_3,
\]

join every `u_i` to `d`, join `u_1` to `x_d,y_d`, and join `u_3` to all
four vertices of `W`.  Let `D` be the star with centre `z` and leaves
`b_1,b_2,b_3`.  Join every `u_i` to `z`, every `b_i` to `e`, and `z` to
all six vertices of `S-{d,e}`.  Finally take adjacent vertices `P_0,P_1`,
each complete to `S`, and add no other edges.

There is a proper six-colouring in which

\[
\begin{array}{c|c}
\text{colour}&\text{vertices}\
\hline
\alpha&d,e,z\\
1&x_d,x_e,x_0\\
2&y_d,y_e,y_0\\
\beta_1&u_1,b_1,P_0\\
\beta_2&u_2,b_2,P_1\\
\beta_3&u_3,b_3.
\end{array}                                             \tag{3.1}
\]

For each `i`, the path

\[
                         d u_i z b_i e               \tag{3.2}
\]

uses exactly the colours `alpha,beta_i`.  Distinct paths meet only at the
common endpoints `d,e` and the common internal `alpha`-vertex `z`; their
internal vertex sets have common intersection exactly `{z}`.  Thus the example retains the actual
colour-indexed path information, not only the portal quotient.

The exact branch-set solver in the adjacent verifier proves that this
17-vertex graph has no `K_7` minor.  Subdividing the unused edge
`u_2u_3` once or twice gives examples with `|E|=4` and `|E|=5` while
preserving (3.1)--(3.2), `|N_E(d)|=3`, and three vertices of `E` adjacent
to `D`.  The exact solver separately excludes a `K_7` minor in both
subdivided graphs.  This also agrees with the standard fact that
subdividing an edge does not change the existence of a `K_7` minor.

Even two distinct `D`-side neighbours of `E` are insufficient without
host-level information.  Add a path `z r z'` inside `D`, join `z'` to
any one `u_i`, colour `z'` with `alpha`, and give `r` a colour different
from `alpha`.  Then

\[
                         |N_D(E)|=2,                 \tag{3.3}
\]

the three paths (3.2) remain, and the verifier again finds no `K_7`
minor for each of the three choices of `i`.

The base example also displays exactly which opposite-response hypothesis
is missing.  Besides the merged-root colouring (3.1), its closed
`D union E` side admits the split-root boundary partition.  Give the two
three-vertex boundary classes colours `1,2`, give `d,e` the distinct
colours `0,3`, and put

\[
 c(z)=0,\quad c(u_1)=c(u_3)=3,\quad c(u_2)=1,
 \quad c(b_1)=c(b_2)=c(b_3)=1.                       \tag{3.4}
\]

This is proper and induces
`X | Y | {d} | {e}` on `S`.  Thus the example does not have the rejected
split-root response required in the live branch.

## 4. Exact scope and missing hypothesis

The examples in Section 3 have low connectivity and are not
contraction-critical.  They are not claimed to realize the rejected
split-root boundary partition on one shore, nor the operation-specific
proper-minor response on a positive-excess full-neighbourhood boundary.
They therefore do not refute the live `HC_7` target.

They do prove that the following data are insufficient by themselves:

- the two rooted boundary triangles;
- adjacent boundary-full subgraphs `P_0,P_1`;
- complementary one-defect connected subgraphs `D,E`;
- three distinct literal `d`-portals in `E` and pointwise `E-D` contacts;
- a common `x_d,y_d` portal; and
- all three colour-indexed alternating paths.

The order-three case is reduced exactly to the endpoint-reversal pattern
(2.1).  Closing it in the hypothetical counterexample must use a genuinely
host-level input: seven-connectivity together with the full literal
neighbourhood of `E`, and the incompatible deletion/contraction colouring
response which rules out (3.4).  Merely adding another `E-D` contact or
subdividing the path does not provide the missing conclusion.
