# Independent audit of missing-colour transport

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source
[`hc7_order8_shortest_path_hole_transport.md`](hc7_order8_shortest_path_hole_transport.md)
at SHA-256

```text
638c01d475bb8a18451fb982c7bcd648071db5768cee3db4b651d3b31a4b32c3
```

The shortest-path exclusion, exact four-colour conclusion, full-trace
shortcut, and unique missing-colour transport are correct.  The endpoint
edges and the vacuous `k<=2` case are scoped explicitly.

## 1. Internal states use exactly four colours

Let `c_0,...,c_k` be shortest between the disjoint sets `E_A,E_D`.
If an internal state belonged to either endpoint set, the corresponding
prefix or suffix would be a shorter path between the sets.  Hence

\[
              c_h\notin E_A\cup E_D\qquad(1\le h\le k-1).
\]

Every five-colour state belongs to exactly one endpoint set by hypothesis.
Thus no internal state is surjective.  Since all path vertices lie in
`R_5^{>=4}(H)`, every internal state uses exactly four colours.

## 2. Consecutive internal states cannot miss the same colour

Fix `1<=i<=k-2` and suppose that `c_i,c_{i+1}` both miss `m`.  Let their
single operated vertex change from `a` to `b`.  The old colour `a` remains
elsewhere, or `c_{i+1}` would use only three colours.  The new colour `b`
already occurs elsewhere under `c_i`, or `c_i` would use at most three.

Recolouring the operated vertex with the globally absent colour `m` is
therefore proper and retains all four old colours.  It gives a surjective
state `theta` adjacent to both `c_i` and `c_{i+1}`.  If `theta` belongs to
`E_A`, then

\[
                       \theta,c_{i+1},\ldots,c_k
\]

has length `k-i<k`, using `i>=1`.  If it belongs to `E_D`, then

\[
                       c_0,\ldots,c_i,\theta
\]

has length `i+1<k`, using `i<=k-2`.  The full-trace ownership hypothesis
puts `theta` in exactly one of these sets, so either case contradicts
shortestness.  Consecutive internal states have distinct missing colours.

## 3. The operated vertex transports the hole

Let `m_i,m_{i+1}` be the distinct missing colours.  Only the operated
vertex changes.  Since `m_i` is absent before and present after, it is the
new colour at that vertex and occurs there uniquely afterward.  Since
`m_{i+1}` is present before and absent after, it is the old colour at that
vertex and occurred there uniquely beforehand.  This gives both displayed
equalities and uniqueness assertions in the source.

## 4. Scope

The shortcut uses both inequalities `i>=1` and `i<=k-2`.  It therefore
does not cover the first or last path edge.  For `k<=2` there is no
internal-to-internal edge and the theorem is vacuous.  It also proves only
consecutive nonstationarity: a missing colour may reappear after one or
more intervening states, as the source now states explicitly.

The theorem assumes rather than proves that both extension languages meet
the four-or-five-colour state graph.  It is a boundary-colouring normal
form and supplies no branch-set labels, compatible separator colouring, or
`K_7`-minor model.
