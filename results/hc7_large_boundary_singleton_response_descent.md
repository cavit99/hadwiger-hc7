# Large `K_5`-minor-free boundaries force a smaller singleton response

**Status:** written proof; separate internal audit GREEN in
[`hc7_large_boundary_singleton_response_descent_audit.md`](hc7_large_boundary_singleton_response_descent_audit.md).

This note gives a host-level reduction for the two-shore exact-block
setting.  It does not use the internal structure of the list-critical
subgraphs: before a boundary of order at least ten can reach the paired
list-critical endpoint, density already forces a singleton-side response
with smaller boundary.  Consequently the paired-kernel obstruction in the
current enlarged-boundary configuration can survive only at boundary order
nine.

## 1. A strict form of Mader's bound in a counterexample

### Lemma 1.1

Let `G` be a seven-connected, seven-chromatic graph with no `K_7` minor.
If `n=|V(G)|` and `m=|E(G)|`, then

\[
                             m\le 5n-16.              \tag{1.1}
\]

#### Proof

Mader's exact extremal theorem gives `m<=5n-15`.  Suppose equality holds.
Jorgensen's equality classification says that a `K_7`-minor-free graph
with `5n-15` edges is either `K_{2,2,2,3}` or a five-clique sum of
edge-maximal two-apex graphs.

The exceptional graph `K_{2,2,2,3}` has connectivity six.  A nontrivial
five-clique sum has a separator of order five.  The only remaining
possibility is one edge-maximal two-apex graph.  Such a graph is
six-colourable: delete an apex set of order at most two, four-colour the
remaining planar graph, and give the two deleted vertices two fresh
colours.  Each alternative contradicts one of the hypotheses on `G`.
Thus equality in Mader's bound is impossible, and integrality gives
(1.1).  \(\square\)

## 2. The boundary-order reduction

### Theorem 2.1 (large-boundary singleton response)

Let `G` satisfy

\[
 \chi(G)=7,\qquad \kappa(G)\ge7,\qquad
 K_7\not\preccurlyeq G,
\tag{2.1}
\]

and let

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,             \tag{2.2}
\]

where `A,D` are nonempty.  Suppose `G[B]` has no `K_5` minor and put
`b=|B|`.  If `b>=10`, then some vertex `v in A union D` satisfies

\[
                          7\le d_G(v)<b.               \tag{2.3}
\]

#### Proof

Put `n=|V(G)|` and `s=|A|+|D|=n-b`.  Suppose, for a contradiction, that
every vertex in `A union D` has degree at least `b`.  Seven-connectivity
gives degree at least seven at every boundary vertex.  Summing degrees and
using Lemma 1.1 yields

\[
              b(n-b)+7b\le 2|E(G)|\le10n-32.          \tag{2.4}
\]

If `b=10`, the left side is `10n-30`, contradicting (2.4).  If `b=11`,
(2.4) gives `n<=12`, whereas the two nonempty shores give `n>=b+2=13`.

It remains to consider `b>=12`.  Rearranging (2.4) gives

\[
 (b-10)n
   \le b^2-7b-32
    =(b-10)(b+3)-2.                                  \tag{2.5}
\]

Thus `n<b+3`, and integrality gives `n<=b+2`.  The two nonempty shores
give the reverse inequality, so `|A|=|D|=1`.  Since `G[B]` has no `K_5`
minor, the established `t=5` case of Hadwiger's conjecture gives a proper
four-colouring of `G[B]`.  The two shore vertices are nonadjacent by
(2.2), so assigning both one fresh fifth colour gives a proper
five-colouring of `G`, contrary to (2.1).

All values `b>=10` lead to a contradiction.  Hence (2.3) holds. \(\square\)

### Corollary 2.2 (strict response boundary)

Assume additionally that every proper minor of `G` is six-colourable.
For the vertex `v` supplied by Theorem 2.1, the set `N_G(v)` is the literal
boundary of a nontrivial singleton-side separation of order strictly less
than `b`.  For every edge `vx`, a proper six-colouring of `G-vx` induces a
boundary partition which

1. extends through `G-v`;
2. extends through `G[N_G[v]]-vx`; and
3. is rejected by the intact graph `G[N_G[v]]`.

If `d_G(v)=7`, this is an exact order-seven response interface; if
`d_G(v)>=8`, it is a strict positive-boundary-order descent.

#### Proof

Assume `v in A`; the case `v in D` is symmetric.  The nonempty set `D` is
anticomplete to `A`, so it lies outside `N_G[v]`.  Hence `N_G(v)` is the
boundary of a nontrivial separation.  Its order lies in the range (2.3).

The edge-deleted graph `G-vx` is a proper minor and has a proper
six-colouring.  Its ends have one colour, since otherwise restoring `vx`
would six-colour `G`.  The outside and edge-deleted singleton-side
restrictions give items 1 and 2.  If their boundary partition extended
through the intact singleton side, aligning colour names and gluing it to
the outside restriction would six-colour `G`.  This proves item 3 and the
last assertion. \(\square\)

## 3. Consequence for the paired list-critical branch

Continue under the hypotheses of Corollary 2.2.  Assume additionally the
setting of the exact-block Kempe-transition theorem: the boundary contains
the fixed independent block `I={d}`, both open shores are full to `B`, and
a shortest exact-`I` transition has distance at least two.  It supplies two
induced vertex-minimal list-uncolourable subgraphs, one in each shore.

Corollary 2.2 shows in general that, outside an exact order-seven response
or a strict boundary-order descent, necessarily `|B|<=9`.  In the current
enlarged-boundary branch one has

\[
                  B=(S-\{e\})\mathbin{\dot\cup}W,
                  \qquad |S|=8,\qquad |W|\ge2,
\]

and hence `|B|=7+|W|>=9`.  Therefore this branch necessarily has

\[
                         |B|=9,\qquad |W|=2.          \tag{3.1}
\]

The complementary-component transfer used next is independent of the old
order-eight notation.  Let `K_A` be the selected list-critical subgraph in
`A`.  If `K_A` is proper, choose any component `R` of
`G[A-V(K_A)]` and six-colour the proper minor `G-R`.  The induced labelled
colouring on `N_G(R)` cannot extend through the intact graph
`G[R union N_G(R)]`, since such an extension would glue directly to the
colouring of `G-R` and six-colour `G`.  Thus `R` is a smaller connected
full-neighbourhood response side satisfying

\[
          |R|<|A|,
          \qquad |N_G(R)|\ge7,                       \tag{3.2}
\]

where the second inequality follows because its full neighbourhood
separates it from the nonempty opposite shore in a seven-connected graph.
The same argument applies to a proper kernel in `D`.  This is a strict
decrease in the order of the connected response side.  It is **not** by
itself an allowed recursive descent in the labelled order-eight proof
spine: it uses a fresh trace, its new boundary order is uncontrolled, and
it preserves neither the exact block `{d}` nor inherited minor-model
labels.

Therefore the only paired-kernel endpoint not covered by one of these
reductions has boundary order nine and both list-critical subgraphs
spanning their respective shores.

For completeness, this spanning endpoint has one further exact property.
Fix the internal boundary colouring `phi`.  For every `a in A` and
`z in D`, minimality gives list-colourings of `A-a` and `D-z`; gluing both
to `phi` gives a proper six-colouring of `G-{a,z}`.  In that colouring,
both deleted vertices see all six colours.  Indeed, a colour excluded from
the list of `a` occurs on a literal boundary neighbour, while a colour in
its list must occur on an internal neighbour in every list-colouring of
`A-a`, or that colouring would extend to `a`.  The same argument applies
to `z`.

There is also a sharp local degree accounting at this endpoint.  For
`Z in {A,D}` and `v in Z`, put

\[
\begin{aligned}
 \varepsilon_Z(v)
   &=d_{G[Z]}(v)-\bigl(6-|\phi(N_G(v)\cap B)|\bigr),\\
 \rho_Z(v)
   &=|N_G(v)\cap B|-|\phi(N_G(v)\cap B)|.
\end{aligned}                                                    \tag{3.3}
\]

List-criticality gives `epsilon_Z(v)>=0`, and direct counting gives

\[
                         d_G(v)=6+\varepsilon_Z(v)+\rho_Z(v).     \tag{3.4}
\]

Outside both an exact order-seven response and a strict boundary-order
response at the nine-vertex boundary, every shore vertex has degree at
least nine: its full neighbourhood separates it from the nonempty opposite
shore.  Hence

\[
                         \varepsilon_Z(v)+\rho_Z(v)\ge3           \tag{3.5}
\]

for every vertex of both spanning kernels.  The subgraph induced by the
vertices with `epsilon_Z(v)=0` is a Gallai forest, by the standard
degree-choosability argument.  In particular every tight vertex has at
least three repeated boundary-colour incidences.

Thus the exact remaining mechanism is not mere colour saturation.  It is
to convert these two simultaneous, fixed-trace saturated deletion
colourings, together with (3.5), into an explicit `K_7`-minor model or a
colour-compatible order-seven separation.

## 4. Trust boundary and external inputs

Theorem 2.1 is unbounded and does not depend on the sizes or internal
structures of the shores.  It does not close the order-nine spanning
paired-kernel endpoint.  The proper-kernel reduction only returns an
unlabelled smaller connected response side; it does not control its boundary
order, preserve the exact block or minor-model labels, or align the two
extension languages.

The proof uses:

- W. Mader, *Homomorphiesatze fur Graphen*, Math. Ann. **178** (1968),
  154--168: `|E(G)|<=5|V(G)|-15` for `K_7`-minor-free graphs; and
- L. K. Jorgensen, *Extremal graphs for contractions to K7*, Ars Combin.
  **25C** (1988), 133--148: the equality classification used in Lemma 1.1.

The Gallai-forest assertion uses the degree-choosability theorem.

The equality classification and its connectivity consequences are already
quoted and audited in
[`hc7_eight_connected_order_bound.md`](../results/hc7_eight_connected_order_bound.md).
The fixed-block transition and the earlier order-eight version of the
proper-kernel transfer are in
[`hc7_two_full_shore_exact_block_kempe_transition.md`](../results/hc7_two_full_shore_exact_block_kempe_transition.md)
and
[`hc7_total_trace_rejection_kernel.md`](../results/hc7_total_trace_rejection_kernel.md),
respectively.
