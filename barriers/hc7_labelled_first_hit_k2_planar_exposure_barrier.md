# Seven-connectivity and `K_7`-minor exclusion do not bound first-hit exposure

**Status:** explicit unbounded barrier to an intermediate
linkage-to-separator claim.  The graph is seven-connected and
`K_7`-minor-free, and all five terminal classes are connected.  It is
six-colourable and is not a hypothetical counterexample to `HC_7`.

The construction strengthens the simpler barrier in
[`hc7_labelled_first_hit_rank_host_lift_barrier.md`](hc7_labelled_first_hit_rank_host_lift_barrier.md):
the failure of the host lift persists after `K_7`-minor exclusion is added.
Consequently, the proper-minor colouring response (or an equivalent
response-preserving exchange axiom) is indispensable.

## 1. The planar graph

Let `I` be the icosahedral graph.  Form its **edgewise subdivision** `J` as
follows.  For every edge `uv` of `I`, introduce a vertex `m_{uv}`, replace
`uv` by the path

\[
                         u m_{uv} v,
\]

and, for every facial triangle `uvw` of `I`, add the central triangle

\[
                   m_{uv}m_{vw}m_{wu}m_{uv}.
\]

Thus every old triangular face is divided into four triangular faces.
The graph `J` is a planar triangulation on 42 vertices.  It is
five-connected.  This last statement can either be checked from the usual
separator criterion for a planar triangulation (every triangle is facial
and there is no chordless four-cycle), or replayed directly by the
deterministic verifier accompanying this note.

Fix an old vertex `v` of `I`.  Its five neighbours occur in a cycle

\[
                         v_1v_2v_3v_4v_5v_1.
\]

Put

\[
 C=\{v\}\cup\{m_{vv_i}:1\le i\le5\}.
\]

Then `J[C]` is a wheel: the five edge-midpoints form its rim and `v` is
its hub.  Its literal neighbourhood is the ten-cycle

\[
 W=v_1,m_{v_1v_2},v_2,m_{v_2v_3},\ldots,
   v_5,m_{v_5v_1},v_1.                                  \tag{1.1}
\]

In particular, `C` and `W` are connected, `|C|=6`, `|W|=10`, and

\[
                            N_J(C)=W.                    \tag{1.2}
\]

There are vertices outside `C union W`; choose two of them and call them
`t_1,t_2`.

## 2. The seven-connected `K_7`-minor-free host

Add two adjacent vertices `a,b`, each complete to `J`, and call the
resulting graph

\[
                            G=K_2\vee J.                 \tag{2.1}
\]

### Lemma 2.1

The graph `G` is seven-connected and has no `K_7` minor.

#### Proof

Delete at most six vertices of `G`.  If at least one of `a,b` remains, it
joins every remaining vertex.  If both are deleted, at most four vertices
of `J` were deleted, and the five-connectivity of `J` leaves the remainder
connected.  Hence `G` is seven-connected.

Suppose that `G` had a `K_7`-minor model.  At most two branch sets of the
model contain `a` or `b`.  The other at least five branch sets lie wholly
in `J`, and their pairwise adjacencies are edges of `J`.  They would form a
`K_5`-minor model in the planar graph `J`, a contradiction.  \(\square\)

## 3. Connected labelled terminals and the failed lift

Take as source set the five rim vertices of the wheel `J[C]`:

\[
                   P=\{m_{vv_i}:1\le i\le5\}.
\]

Define five pairwise disjoint connected terminal classes by

\[
 T_1=\{t_1\},\qquad T_2=\{t_2\},\qquad
 T_3=\{a\},\qquad T_4=\{b\},\qquad T_5=W.              \tag{3.1}
\]

Use the terminal-sink network of the Rado--gammoid first-hit reduction:
all vertices in `T=T_1 union ... union T_5` are forbidden internally and
are represented by directed terminal sinks.

### Lemma 3.1

For `I={1,2}`,

\[
                          r_P(T_I)=0.                    \tag{3.2}
\]

The empty set is therefore a minimum relative separator, while the
surviving source component has a literal host boundary of order twelve.

#### Proof

Equations (1.1)--(1.2) say that deleting `W` separates `C` from every old
vertex outside `C union W`.  The two universal vertices are also deleted
as terminals.  Hence `C` is a component of `G-T`, and there is no clean
path from `P` to either `t_1` or `t_2`.  This proves (3.2).

In the host graph, however,

\[
                          N_G(C)=W\cup\{a,b\},
\]

which has order twelve.  All twelve vertices belong to the three terminal
classes omitted from `I`.  Thus the relative separator of order zero does
not lift to an order-seven host separator.  \(\square\)

## 4. Exact scope

This example simultaneously satisfies:

* seven-connectivity;
* `K_7`-minor exclusion;
* five nonempty, pairwise disjoint and connected terminal classes;
* five distinct source vertices; and
* a strict Rado rank defect.

It refutes any inference that attempts to bound omitted-label exposure by
using only connectivity, minor exclusion, or connectedness of the named
terminal sets.  It does not carry the selected proper-minor colouring
response, a contraction-critical law, or the complete labelled
near-`K_7` geometry of the active branch.  Indeed, `J` is planar and hence
four-colourable, so `G` is six-colourable.

Accordingly, a positive `HC_7` theorem must use the response dynamically:
an omitted label with several exposed literal vertices must augment the
labelled first-hit rank, shorten the response-preserving kernel, construct
a `K_7`-minor model, or force a common boundary colouring.  It cannot be
discarded by a static host-separator count.

## 5. Verification

Run from the repository root:

```text
python3 barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier_verify.py
```

Expected output:

```text
GREEN K2-planar first-hit exposure barrier
J: vertices=42 edges=120 connectivity=5 C=6 W=10
G: vertices=44 edges=205 connectivity=7 exposure=12
rank(T1 union T2)=0; K7-minor excluded by planarity of J
```
