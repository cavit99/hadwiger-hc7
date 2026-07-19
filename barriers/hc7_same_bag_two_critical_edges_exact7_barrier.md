# Two same-bag critical-edge responses do not allocate first-hit labels

**Status:** explicit finite barrier to an intermediate dynamic claim;
deterministic verifier included; separate internal audit GREEN in
[`hc7_same_bag_two_critical_edges_exact7_barrier_audit.md`](hc7_same_bag_two_critical_edges_exact7_barrier_audit.md).
The graph
contains a `K_7` subgraph and is not minor-minimal, so it is not a
counterexample to `HC_7`.

The accompanying checker is
[`hc7_same_bag_two_critical_edges_exact7_barrier_verify.py`](hc7_same_bag_two_critical_edges_exact7_barrier_verify.py).

## 1. Precise overstrong statement refuted

The following implication is false if `K_7`-minor exclusion and global
proper-minor criticality are omitted.

> Let `G` be seven-connected and seven-chromatic, with an actual
> order-seven separation whose two open shores are connected and adjacent
> to every boundary vertex.  Suppose `G` has a spanning labelled
> `K_7`-minus-one-edge model and two edges `e,f` joining the same two named
> branch sets such that deleting either edge preserves that model and both
> `G-e,G/e,G-f,G/f` are six-chromatic.  If six-colourings of `G-e` and
> `G-f` induce the same labelled boundary trace, then either that trace
> extends through both original closed shores or the five alternate
> colours at the common root have first-hit representatives in five
> distinct named branch sets.

The example below has neither conclusion.  It strengthens the adjacent
example in the existing joint-persistence barrier in two ways: the two
critical edges join the same pair of model branch sets, and their common
response is located at a literal order-seven separation.

## 2. Construction

Use the adjacent-edge graph from
[`hc7_joint_pair_first_hit_hall_barrier.md`](hc7_joint_pair_first_hit_hall_barrier.md),
with vertices

```text
v a b c1 c2 c3 c4 pA pB p1 r1 p2 r2 p3 r3.
```

On the common deletion of `va,vb`, retain its two six-colourings
`phi,psi`.  Their colour classes are

\[
\begin{array}{c|l|l}
&\phi&\psi\\ \hline
0&v,a,r1,r3&a,r1,r3\\
1&c1,pA,pB,p1,p2,p3&c1,pA,pB,p1,p2,p3\\
2&b,r2&v,b,r2\\
3&c2&c2\\
4&c3&c3\\
5&c4&c4.
\end{array}
\tag{2.1}
\]

Add a vertex `ell` with neighbourhood

\[
 S=\{pA,pB,p1,p2,p3,c2,c3\}.                     \tag{2.2}
\]

Give `ell` colour five in both displayed colourings.  The set `S` uses
the same three labelled colours in both responses, namely colour one on
the first five vertices and colours three and four on `c2,c3`.

Use the seven branch sets

\[
\begin{array}{c|l}
R&\{v\}\\
U&\{a,b,pA,pB\}\\
C_1&\{c1,c2,ell\}\\
C_2&\{c3,c4\}\\
Y_1&\{p1,r1\}\\
Y_2&\{p2,r2\}\\
Y_3&\{p3,r3\}.
\end{array}                                           \tag{2.3}
\]

They are connected, disjoint, spanning and pairwise adjacent except for
`Y1,Y2`.  The same model remains after deleting either or both of `va,vb`:
both edges join `R` to `U`, and `vpA,vpB` retain that model adjacency.

## 3. Exact-seven interface and critical responses

The old fifteen-vertex graph is eight-connected.  Adding `ell` with the
seven neighbours (2.2) makes the new graph exactly seven-connected.  After
deleting fewer than seven vertices, the old graph remains connected and a
surviving neighbour joins `ell` to it.  Deleting all of `S` isolates
`ell`.

The old graph minus `S` is connected.  Every member of `S` has a neighbour
there, so

\[
 V(G)=\{ell\}\mathbin{\dot\cup}S
       \mathbin{\dot\cup}(V(G)-S-\{ell\})             \tag{3.1}
\]

is an actual order-seven separation with two connected boundary-full open
shores.

The vertices

\[
                  \{v,a,b,c1,c2,c3,c4\}               \tag{3.2}
\]

induce `K_7`, while recolouring `v` with a seventh colour gives a proper
seven-colouring.  Hence `chi(G)=7`.

The colouring `phi` properly colours `G-va`, and `psi` properly colours
`G-vb`.  In the first response `v,a` are equal; in the second `v,b` are
equal, so the colourings descend to `G/va` and `G/vb`.  Each of these four
proper minors contains a `K_6` subgraph, and therefore

\[
       \chi(G-va)=\chi(G/va)=\chi(G-vb)=\chi(G/vb)=6. \tag{3.3}
\]

The two responses agree literally on `S`, and their common trace extends
through the singleton closed shore by giving `ell` colour five.  It cannot
extend through the opposite original closed shore: that shore is the old
graph and contains the `K_7` in (3.2).

## 4. Same-bag first-hit Hall failure

Use `phi` and the singleton root `v`.  Among its five alternate colours,
the supports in the named branch sets satisfy

\[
 \operatorname{supp}(3)=\{C_1\},\qquad
 \operatorname{supp}(4)=\operatorname{supp}(5)=\{C_2\}. \tag{4.1}
\]

Indeed the relevant root neighbours are `c2,c3,c4`.  Thus the three
colours `3,4,5` have only two possible first-hit labels.  Hall's condition
fails, so no five-label first-hit allocation exists.

There is also a further critical response inside the repeated first-hit
branch set `C2`.  Deleting the edge `c3c4` admits the six-colouring

\[
\begin{array}{c|l}
0&b,ell,r2\\
1&c1,pA,pB,p1,p2,p3\\
2&a,r1,r3\\
3&c2\\
4&c3,c4\\
5&v.
\end{array}                                             \tag{4.2}
\]

This colouring has exactly the same labelled trace on `S` as `phi`, and
its equal colours on `c3,c4` descend to `G/c3c4`.  Both the deletion and
contraction are exactly six-chromatic: each is six-colourable by (4.2),
while deleting or contracting one edge of the clique (3.2) retains a
`K_6`.

Thus merely asking for one additional proper-minor response supported
inside the repeated first-hit branch set does not repair the local
palette-to-label failure.  In a positive theorem that response must be
coupled to global `K_7`-minor exclusion or to a model-preserving split; its
existence alone is insufficient.

Even deleting the singleton repeated-exposure source `v` retains the same
boundary trace.  One such six-colouring of `G-v` is

\[
\begin{array}{c|l}
0&c4,ell\\
1&c1,pA,pB,p1,p2,p3\\
2&b,r2\\
3&c2\\
4&c3\\
5&a,r1,r3.
\end{array}                                             \tag{4.3}
\]

The remaining six vertices of the clique (3.2) show that `G-v` is exactly
six-chromatic.  Thus the barrier already supplies selected-trace responses
both inside the repeated label and at the repeated-exposure source.  The
missing positive ingredient cannot be the bare existence of either probe;
it must use `K_7`-minor exclusion to convert their literal geometry.

This is a direct counterexample to the implication in Section 1.  It also
shows that the single-attainment branch of a fixed-trace two-edge fork is
not automatically terminal: both individually critical edges attain the
same trace, yet the old model labels remain concentrated.

## 5. Exact trust boundary

The construction deliberately has both global defects excluded in the
active `HC_7` branch.

1. It contains the literal `K_7` in (3.2).
2. It is not minor-minimal: deleting `ell` leaves that same seven-chromatic
   graph.

The example therefore does not refute a theorem whose alternatives include
an explicit `K_7`-minor model, nor a theorem which uses every proper-minor
response of a hypothetical counterexample.  Its purpose is sharper: the
two selected critical edges, same-model-bag geometry, exact-seven boundary,
common labelled trace and seven-connectivity still do not produce the
palette-to-label allocation.  A positive theorem has to spend global
`K_7`-minor exclusion and use a further proper-minor response through
literal model geometry, rather than merely invoke its existence.

## 6. Verification

From the repository root run

```text
python3 barriers/hc7_same_bag_two_critical_edges_exact7_barrier_verify.py
```

Expected output:

```text
GREEN same-bag exact-seven two-edge barrier: kappa=7, chi=7, shared trace, internal/root responses, Hall failure, explicit K7
```
