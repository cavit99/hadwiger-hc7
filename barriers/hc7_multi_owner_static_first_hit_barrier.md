# Maximum first-hit rank does not resolve a two-owner branch-set split

**Status:** explicit finite barrier; deterministic verifier included; separate
internal audit GREEN in
[`hc7_multi_owner_static_first_hit_barrier_audit.md`](hc7_multi_owner_static_first_hit_barrier_audit.md).
This example is seven-connected and `K_7`-minor-free.  It shows that the
relaxed first-hit rank and branch-set minimality do not, without a
proper-minor colouring response, eliminate a split carrying two other
branch-set adjacencies.

The verifier is
[`hc7_multi_owner_static_first_hit_barrier_verify.py`](hc7_multi_owner_static_first_hit_barrier_verify.py).

## 1. Exact statement refuted

The example refutes the following model-local assertion.

> **Static two-owner first-hit assertion.**  Let `G` be a seven-connected,
> `K_7`-minor-free graph with a spanning labelled `K_7`-minus-one-edge
> model
>
> \[
>                    X,Y,D,U,F,P_0,Q_0,
> \]
>
> whose only possible missing pair is `X,Y`.  Fix roots in the seven
> branch sets, a connected subgraph `Z subseteq D`, permitted source ports
> in `Z`, and ranked labels among the six labels other than `D`.  Among
> compatible models, first maximize the relaxed first-hit rank and then
> minimize `|U|`.
>
> Suppose two edges from `Z` have distinct ends in `U`, and a root-free
> connected and co-connected side `W subsetneq U` separates those two
> ends.  Then at least one of the following holds:
>
> 1. `G` has a `K_7` minor;
> 2. there is a compatible labelled model with a smaller branch set `U`;
> 3. some nonempty connected set `C subseteq U` has
>    `|N_G(C)|=7`.

The third conclusion is deliberately local.  The example has unrelated
order-seven separations elsewhere in the graph, so it does not refute a
theorem allowed to return an arbitrary separation together with an
operation-specific boundary colouring.

## 2. The planar factor and the host

Start with NetworkX's deterministically labelled icosahedral graph on
vertices `0,...,11`.  List its twenty triangular faces lexicographically.
For the face in position `i`, add a vertex `12+i`, join it to the three
old vertices of the face, and join two face vertices precisely when their
faces share an edge.  Call the resulting graph `T`.

This is the 32-vertex dual-truncated-icosahedron triangulation.  Direct
verification gives

\[
 |T|=32,\qquad e(T)=90,qquad
 T\text{ planar},qquad \kappa(T)=5.                 \tag{2.1}
\]

Add adjacent vertices `p,q`, each complete to `T`, and put

\[
                              G=K_2\vee T.             \tag{2.2}
\]

### Lemma 2.1

The graph `G` is seven-connected and has no `K_7` minor.

#### Proof

If either `p` or `q` survives a vertex deletion, it joins all remaining
vertices.  If both are deleted, fewer than five further deletions leave
the five-connected graph `T` connected.  Conversely, deleting `p,q`
together with a five-vertex cut of `T` disconnects `G`.  Hence
`kappa(G)=7`.

In a `K_7`-minor model, at most two branch sets contain `p` or `q`.
Deleting those branch sets would leave five pairwise adjacent connected
branch sets wholly in `T`, and hence a `K_5` minor in the planar graph
`T`.  This is impossible. \(\square\)

## 3. A spanning labelled model and maximum first-hit rank

Define

\[
\begin{aligned}
 X&=\{11\},                  &Y&=\{0\},\\
 U&=\{12,13,14\},            &F&=\{16\},\\
 D&=V(T)-\{0,11,12,13,14,16\},\\
 P_0&=\{p\},                 &Q_0&=\{q\}.
\end{aligned}                                                   \tag{3.1}
\]

These sets partition `V(G)` and are connected.  One spanning tree of `D`
has the path

```text
1-17-2-18-8-15-7-29-9-21-3-20-6-19-5-26-4-23-24-10-25-30-31-28-27
```

together with the edge `21-22`.  Every two sets in (3.1) are adjacent
except `X,Y`.  The non-universal adjacencies may be witnessed by

\[
\begin{array}{c|ccccccccc}
\text{pair}&XD&XU&XF&YD&YU&YF&DU&DF&UF\\ \hline
\text{edge}&11\!-!27&11\!-!14&11\!-!16&0\!-!15&0\!-!12&
0\!-!16&1\!-!12&15\!-!16&14\!-!16.
\end{array}                                                    \tag{3.2}
\]

Thus (3.1) is a spanning labelled `K_7`-minus-one-edge model.  Prescribe
the roots

\[
 11,0,1,13,16,p,q
\]

in `X,Y,D,U,F,P_0,Q_0`, respectively, and put `Z=D`.

Rank all six labels

\[
                       X,Y,U,F,P_0,Q_0.                 \tag{3.3}
\]

Use the permitted ports `27,15,1,7,2,3` in `Z`.  The six one-edge paths

\[
 27\!-!11,\quad15\!-!0,\quad1\!-!12,\quad
 7\!-!16,\quad2\!-!p,\quad3\!-!q                  \tag{3.4}
\]

have distinct ports, are pairwise disjoint outside `Z`, and first meet a
ranked branch set at their distinct terminal vertices.  Hence the relaxed
first-hit rank is six.  Since only six labels are ranked, this is the
absolute maximum.

## 4. The two-owner split and branch-set minimality

The edges

\[
                         8\!-!13,\qquad19\!-!12       \tag{4.1}
\]

join `Z` to distinct vertices of `U`.  Take

\[
                         W=\{12,14\},\qquad U'=\{13\}. \tag{4.2}
\]

The graph `G[U]` is the path `13-12-14`; hence `W` and `U'` are
connected, `W` contains exactly one contact end from (4.1), and the root
`13` remains in `U'`.

For this split define

\[
 \Omega(W)=
 \{R\in\{X,Y,F,P_0,Q_0\}:E_G(U',R)=\varnothing\}.      \tag{4.3}
\]

The vertex `13` is adjacent to `0,p,q` and nonadjacent to `11,16`, while
`14` is adjacent to both `11` and `16`.  Therefore

\[
                            \Omega(W)=\{X,F\}.          \tag{4.4}
\]

So moving all of `W` into either owner loses the adjacency to the other.

### Lemma 4.1

There is no compatible model, with the fixed labels, roots and `Z`, whose
branch set labelled `U` is smaller than the set in (3.1).

#### Proof

The fixed subgraph `Z=D` fixes all twenty-six vertices of `D`.  The roots
fix the vertices `11,0,16,p,q,13` in their displayed branch sets.  Thus
only `12,14` can change ownership.

A smaller connected branch set containing the root `13` is one of
`{13}`, `{12,13}`, `{13,14}`.  The last is disconnected.  Neither `12`
nor `13` is adjacent to `11` or `16`.  Consequently `{12,13}` misses
both `X` and `F`; assigning the remaining vertex `14` can repair at most
one of those two adjacencies.  Finally, among the two movable vertices
only `12` is adjacent to `13`, so when `U={13}`, the two fixed branch
sets rooted at `11` and `16` cannot both acquire an adjacency to `U`.
Thus no smaller compatible model exists. \(\square\)

The verifier independently checks all `7^2` assignments of `12,14` to
the seven labels.  The only compatible assignment leaves both vertices
in `U`.

## 5. No local order-seven boundary

Every nonempty connected subset of `U` has full neighbourhood larger than
seven.  The exact orders are

\[
\begin{array}{c|c}
C&|N_G(C)|\\ \hline
\{12\},\{13\},\{14\}&8\\
\{12,13\},\{12,14\}&10\\
\{12,13,14\}&12.
\end{array}                                             \tag{5.1}
\]

In particular, the two-owner side `W` has a full neighbourhood of order
ten, not seven.  Lemma 2.1, Lemma 4.1 and (5.1), together with the maximum
rank in (3.4), refute the assertion in Section 1.

## 6. Exact trust boundary

This is a static barrier, not a counterexample to `HC_7`.

* The graph is six-colourable: four colours suffice for planar `T`, and
  `p,q` use two additional colours.
* It is not seven-chromatic or contraction-critical.
* No equality partition selected by a critical proper-minor operation is
  specified.
* The graph has unrelated order-seven separations.  For example, old
  degree-five vertices of `T` have degree seven in `G`.
* It is coherently two-apex: `G-{p,q}=T` is planar.

Thus the example does not refute a theorem which uses contraction-critical
colouring responses to return an arbitrary colour-compatible order-seven
separation or the coherent pair `{p,q}`.  It proves that maximum relaxed
first-hit rank, branch-set minimality, seven-connectivity and `K_7`-minor
exclusion alone cannot resolve the multi-owner case.

## 7. Verification

From the repository root run

```text
PYTHONPATH=active/runtime/deps python3 \
  barriers/hc7_multi_owner_static_first_hit_barrier_verify.py
```

Expected output:

```text
GREEN multi-owner static first-hit barrier: kappa=7, lambda=6, minimum U and local boundary orders verified
```
