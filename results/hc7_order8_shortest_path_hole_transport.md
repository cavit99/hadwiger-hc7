# Missing-colour transport along a shortest shore transition

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_shortest_path_hole_transport_audit.md`](hc7_order8_shortest_path_hole_transport_audit.md).

This note records a consequence of working in the four-or-five-colour
reconfiguration graph of the order-eight boundary.  Along the interior of
a shortest transition between the two shore-extension languages, every
one-vertex move changes the unique unused colour.  The statement is purely
about labelled boundary colourings; it does not construct a clique minor or
a compatible separator.

## 1. Setting

Let `H` be a graph and let `R_5^{>=4}(H)` be the graph whose vertices are
the proper colourings

\[
                         c:V(H)\longrightarrow[5]
\]

which use at least four colours, with two colourings adjacent when they
differ at exactly one vertex.

Let `E_A,E_D` be disjoint nonempty subsets of
`V(R_5^{>=4}(H))`.  In the shore application these are the boundary
colourings which extend through the two closed shores.  Assume that every
proper colouring of `H` using all five colours belongs to exactly one of
`E_A,E_D`.

Choose a shortest path

\[
                         c_0,c_1,\ldots,c_k             \tag{1.1}
\]

in `R_5^{>=4}(H)` with `c_0 in E_A` and `c_k in E_D`.
The endpoint hypothesis says precisely that both extension languages meet
the four-or-five-colour reconfiguration graph, so such a path exists when
that graph is connected.

## 2. Missing-colour transport theorem

### Theorem 2.1

For every index

\[
                         1\le i\le k-2,                 \tag{2.1}
\]

both `c_i,c_{i+1}` use exactly four colours, and their missing colours are
different.  More precisely, if `m_i` is the colour missing under `c_i` and
`m_{i+1}` is the colour missing under `c_{i+1}`, then the one operated
vertex `v_i` satisfies

\[
 c_i(v_i)=m_{i+1},\qquad c_{i+1}(v_i)=m_i,              \tag{2.2}
\]

and `v_i` is the unique vertex of colour `m_{i+1}` under `c_i` and the
unique vertex of colour `m_i` under `c_{i+1}`.

Thus every internal-to-internal move transports the unique missing colour:
the old missing colour appears at `v_i`, and the colour formerly carried
uniquely by `v_i` becomes the new missing colour.

#### Proof

Minimality of (1.1) implies

\[
 c_h\notin E_A\cup E_D\qquad(1\le h\le k-1).           \tag{2.3}
\]

Every five-colour state belongs to exactly one extension language by
hypothesis.  Hence every internal state in (2.3) is non-surjective.  It is
a vertex of `R_5^{>=4}(H)`, so it uses exactly four colours.

Fix `i` as in (2.1), and suppose first that `c_i,c_{i+1}` miss the same
colour `m`.  Let `v` be their unique operated vertex, recoloured from `a`
to `b`.  Both `a,b` differ from `m`.  The colour `a` still occurs away from
`v`, since otherwise `c_{i+1}` would use only three colours.  The colour
`b` already occurs away from `v` under `c_i`, because `m` is its unique
missing colour.

Recolour `v` with `m`.  The result is proper because `m` is absent from
all of `H`.  The preceding paragraph shows that all four old colours remain,
so the resulting colouring `theta` uses all five colours.  The same
colouring is obtained from either `c_i` or `c_{i+1}` by changing only `v`.
Thus

\[
                      c_i\;\theta\;c_{i+1}             \tag{2.4}
\]

is a two-edge path in the reconfiguration graph.

The full colouring `theta` belongs to exactly one of `E_A,E_D`.  If it
belongs to `E_A`, then

\[
                    \theta,c_{i+1},\ldots,c_k
\]

is a path between the two extension languages of length `k-i<k`, because
`i>=1`.  If `theta` belongs to `E_D`, then

\[
                    c_0,\ldots,c_i,\theta
\]

has length `i+1<k`, because `i<=k-2`.  Either conclusion contradicts the
choice of (1.1).  Therefore the two missing colours are distinct.

Since `m_i` is absent under `c_i` but present under `c_{i+1}`, the new
colour at the sole operated vertex is `m_i`.  Since `m_{i+1}` is present
under `c_i` but absent under `c_{i+1}`, its old colour is `m_{i+1}` and no
other vertex had that colour.  Conversely, `m_i` occurs under
`c_{i+1}` only at the operated vertex because it was wholly absent under
`c_i`.  This proves (2.2) and both uniqueness statements. \(\square\)

## 3. Exact scope

The theorem governs only edges whose two ends are internal states.  It says
nothing about the first edge `c_0c_1` or the last edge
`c_{k-1}c_k`, because an endpoint may itself use only four colours and its
membership in an extension language prevents the shortening argument used
above.

If `k<=2`, the index range (2.1) is empty and the theorem is vacuous.  In
particular, a two-edge transition through one rejected four-colour state
requires a separate host-level analysis of its two endpoint recolourings.

The result does not prove that both shore-extension languages meet
`R_5^{>=4}(H)`; this is an explicit hypothesis.  It also does not identify
a colour with a branch-set label, preserve a selected minor model, produce
an order-seven separation, or construct a `K_7`-minor model.  Its gain is a
canonical, nonstationary description of every genuinely internal move:
consecutive internal states have different missing colours once the
four-or-five-colour endpoint condition has been established.  Missing
colours may repeat at nonconsecutive states.

## 4. Dependency

- the strengthened
  [four-or-five-colour reconfiguration theorem](../results/hc7_order8_full_five_colour_reconfiguration.md),
  for connectivity of the live order-eight boundary space.
