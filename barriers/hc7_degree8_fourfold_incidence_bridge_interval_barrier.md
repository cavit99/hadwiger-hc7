# Four incidence splits need not leave a bridge interval

**Status:** explicit finite barrier to an intermediate local inference;
deterministic verifier included.  This is not a counterexample to `HC_7` or
to a theorem using the full seven-connected contraction-critical setup.

The barrier concerns the following tempting inference from the audited
[bilateral response-cycle theorem](../results/hc7_degree8_aligned_pair_bilateral_cycle.md):

> boundary compactness, two full shores, one named bilateral Kempe
> operation, its odd trace cycle, and the four incidence splits together
> force a nonempty off-path bridge, a proper attachment interval, or a
> smaller component of the same anti-neighbourhood.

That inference is false.  The four incidence graphs can split because the
two selected paths exhaust their open shores.

The adjacent verifier is
[`hc7_degree8_fourfold_incidence_bridge_interval_barrier_verify.py`](hc7_degree8_fourfold_incidence_bridge_interval_barrier_verify.py).

## 1. Construction

Let

\[
 I=\{i_1,i_2,i_3\},\qquad T=\{t_1,t_2,t_3\},\qquad
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\}.
\]

On `S`, take the two triangles

\[
                     pt_1i_1p,\qquad qi_2t_2q,
\]

and the joining path

\[
                         i_1t_3i_3t_2,
\]

with no other boundary edges.  Add a vertex `u` adjacent exactly to `S`.
The two components of `G-N[u]` are

\[
                         E=\{e\},\qquad F=\{x,y\}.
\]

Make `e` adjacent to every vertex of `S`, add `xy`, make `x` adjacent to
`S-{q}`, and make `y` adjacent to `S-{p}`.  There are no further edges.
Thus both `E` and `F` are connected and adjacent to every boundary vertex.

The boundary satisfies all static hypotheses used to select the aligned
pair: `I,T` are independent, `pq` is a nonedge, each root contacts both
blocks, and there is an `I`--`T` edge.  Moreover `alpha(G[S])=3`.  The
boundary consists of two triangles joined by a path, so it has treewidth at
most two; consequently `G[S]-Z` has no `K_4` minor for every two-set `Z`.

## 2. One named operation and its odd cycle

Use colours `a,b,gamma,delta` and the following two fixed shore
colourings:

\[
\begin{array}{c|ccccc}
 &I&T&p&q&\text{open shore}\\ \hline
 c_E&a&b&\gamma&\gamma&e:\delta\\
 c_F&a&b&\gamma&\delta&x:\delta,\ y:\gamma.
\end{array}
\]

Both are proper.  In `c_E`, the full `gamma`--`delta` component containing
`q` is the even path

\[
                              P_E=p-e-q.
\]

In `c_F`, the corresponding component is the odd path

\[
                              P_F=p-x-y-q.
\]

They represent the same singleton `{q}` boundary interchange, read in
opposite directions: merged to split on `E`, and split to merged on `F`.
Their union is an induced odd cycle `p-e-q-y-x-p`.  Hence shore ownership,
path parity, and the named colouring-operation provenance are all literal
in the graph.

## 3. Shore-filling vacuity

Here

\[
                       P_E^\circ=E,\qquad P_F^\circ=F.
\]

After deleting the appropriate path interior, there is no residual shore
component.  Each of `J_I(P_E),J_T(P_E),J_I(P_F),J_T(P_F)` therefore
consists of the three named block vertices as isolated vertices.  Each
incidence graph formally splits its block between three connected
components, exactly as required by the conclusion of Corollary 4.1 of the
bilateral response-cycle theorem.

There is nevertheless no off-path shore component, hence no bridge
attachment interval to minimize and no smaller component of `G-N[u]`
enclosed by such an interval.  A proof cannot begin by choosing one without
first disposing of this shore-filling case.

Nor does passing to bridges of the whole odd cycle create a proper
interval.  The graph left after deleting `p,e,q,y,x` is connected, and it
has a neighbour at every vertex of that cycle.  Its attachment hull is the
whole cycle.

The construction is order-minimum for this local parity certificate.
There are nine prescribed vertices in `S\cup\{u\}`.  Since `pq` is absent,
an even `p`--`q` path needs at least one internal vertex and an odd one
needs at least two.  The displayed graph has exactly twelve vertices.

## 4. `K_7`-minor exclusion and the missing host hypotheses

The fill-elimination order

```text
p q i2 t1 i1 t2 i3 t3 u e x y
```

has width five.  Therefore `G` has treewidth at most five and has no
`K_7` minor.  This also implies that every minor of `G` is six-colourable.
The verifier additionally proves

\[
                         \kappa(G)=5,qquad \chi(G)=5.
\]

Thus the example deliberately fails two indispensable global hypotheses:
it is not seven-connected and it is not seven-chromatic.

It also fails the universal opposite-response conclusion that
contraction-criticality supplies.  Each shore realizes both endpoint
equality types.  Besides the displayed colourings, proper colourings are

\[
\begin{array}{c|ccccc}
 &I&T&p&q&\text{open shore}\\ \hline
 E\text{ split}&0&1&2&3&e:4\\
 F\text{ merged}&0&1&2&2&x:3,\ y:4.
\end{array}
\]

Accordingly, the construction preserves one selected failed interchange;
it does not realize the full opposite-singleton response languages in
Theorem 2.1.

## 5. Exact consequence

The odd trace cycle and four incidence splits are not, by themselves, a
bridge theorem.  Any positive next lemma must include the shore-filling
case as an explicit alternative and then genuinely use information absent
here, such as seven-connectivity together with the universal proper-minor
colouring responses or a rooted-minor consequence of attachments spanning
the whole cycle.

In particular, the rank for a proposed restart may still be measured on a
literal component of the unchanged anti-neighbourhood, but the existence
of such a component cannot be inferred from the incidence splits alone.
