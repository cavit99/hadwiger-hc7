# Connectivity does not compose a same-shore singleton `K_6`

**Status:** explicit barrier, with a reproducible verifier in
`active/hc7_same_shore_singleton_k6_connectivity_barrier_verify.py`.

This construction falsifies the tempting carrier-composition statement

> seven-connectivity + an exact order-eight two-full-shore separation with
> four-colourable boundary + a `K_6` model having a prescribed same-shore
> edge as two singleton bags implies a `K_7` minor.

Consequently the active leaf-drop route must use the critical chromatic
response `chi(H)=6, chi(H/e)=5`; neither connectivity nor the regenerated
rooted model is enough by itself.

## 1. Construction

Let `I` be the icosahedral graph, with the standard NetworkX labelling, and
let

\[
                    G=\overline {K_2}\vee I.
\]

Write `a,b` for the two nonadjacent vertices of the `K_2`-complement.  Thus
both are complete to `I`.

In `I`, put

\[
 S_0=\{0,1,2,3,4,11\},\qquad
 A=\{5,6\},\qquad B=\{7,8,9,10\},
\]

and set `S=S_0 union {a,b}`.  The induced graph on `S_0` is the six-cycle

\[
                 0,1,2,3,4,11,0.                 \tag{1.1}
\]

The sets `A` and `B` are the two components of `I-S_0`; each is connected,
there are no `A-B` edges, and every vertex of `S_0` has a neighbour in each
of `A,B`.  Since `a,b` are universal to `I`, both `A` and `B` are literally
`S`-full.  Hence

\[
 (G[A\cup S],G[B\cup S])
\]

is an actual exact order-eight separation with two full open shores.
Moreover

\[
                  G[S]\cong\overline {K_2}\vee C_6,
              \qquad \chi(G[S])=3.               \tag{1.2}
\]

This is stronger than the four-colourable-boundary hypothesis arising in
the exact order-eight absorption theorem.

## 2. The host is seven-connected and `K_7`-minor-free

The icosahedral graph is five-connected.  Removing fewer than seven
vertices from `G` leaves it connected: if either of `a,b` remains, that
vertex joins all remaining icosahedral vertices; if both are removed, fewer
than five vertices were removed from `I`, which remains connected.  On the
other hand, deleting `a,b` and the five neighbours in `I` of any fixed
icosahedral vertex separates that vertex.  Thus

\[
                         \kappa(G)=7.              \tag{2.1}
\]

The graph has no `K_7` minor.  In any seven-bag clique model, at most two
bags contain `a` or `b`.  At least five bags therefore lie entirely in
`I`; they would form a `K_5` minor in the planar graph `I`, impossible.

## 3. A same-shore edge is represented by singleton `K_6` bags

Take the edge `uv=56` inside the shore `A`.  The following are six literal
branch sets in `G`:

\[
 \{5\},\quad \{6\},\quad \{1\},\quad
 \{2,3,4\},\quad \{a,0\},\quad \{b\}.             \tag{3.1}
\]

They are disjoint and connected.  The first four are pairwise adjacent:
`1-5`, `1-6`, and `5-6` are edges, the path `2-3-4` is connected, and it
meets the first three through `4-5`, `2-6`, and `1-2`.  The bag `{a,0}` is
connected and is adjacent to `{b}` through `0-b`; both apex bags are
adjacent to every one of the first four bags.  Hence (3.1) is a `K_6`
model in which `u=5` and `v=6` are prescribed singleton bags.

Combining (2.1), the exact full-shore geometry, (1.2), and (3.1) while the
host remains `K_7`-minor-free proves the claimed falsification.

## 4. Exact lesson for the proof spine

The positive carrier theorem cannot merely ask a singleton-rooted `K_6`
model to meet the opposite full shore by connectivity.  The icosahedral
example already supplies all of that unlabelled geometry.

The hypotheses not present here, and hence still capable of forcing the
desired composition, are precisely the critical drop response

\[
                \chi(H)=6,\qquad \chi(H/e)=5,
\]

together with the exact proper-minor colouring witnesses it generates.
The next constructive lemma must couple those witnesses to the labelled
model/carrier; deleting them from the statement makes it false.

The example also calibrates the correct disjunction.  The pair `{a,b}`
meets every `K_5` model in `G`, because deleting it leaves the planar
icosahedron.  Thus the example has the desired global support-transversal
terminal even though the displayed local `K_6` does not reveal that pair.
It refutes a forced-`K_7` carrier lift, but it supports rather than refutes
the sharper alternative

\[
        K_7\text{ minor}\quad\hbox{or}\quad
        \tau_5(G)\le2\quad\hbox{or a labelled near-model handoff}.
\]

In particular, any local composition invariant must be capable of
recovering a coherent pair which need not be the named drop-edge ends.
