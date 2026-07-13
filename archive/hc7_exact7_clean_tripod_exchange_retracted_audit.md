# Independent audit: RETRACTED exact-seven clean two-tripod exchange

## Verdict

**RED as an exchange proof.**  The displayed carrier construction after
(2.3) is sound, but the proof's key neighbourhood containment (2.2) does
not follow when the advertised unused components are present.  More
fundamentally, the selected-sector hypotheses already contradict the
assumption that `G[L]` is three-connected.  Thus the implication in
Theorem 1.1 is only vacuously true in the stated three-connected setting;
it does not establish a nontrivial clean-tripod exchange.

## 1. Each selected arm already exposes a two-cut

Fix `i`.  Since `C_i` is a component of `C-z_C`, every edge from `C_i`
to `C-C_i` has its other endpoint at `z_C`.  Since `C` and `D` are
different components of `L-T`, there is no `C_iD` edge.  Hypothesis 3
forbids every edge from `C_i` to `T-{t_i}`.  Consequently

\[
                     N_L(C_i)\subseteq\{z_C,t_i\}.
\]

Both vertices really can occur, but that does not help.  After deleting
`{z_C,t_i}`, the nonempty set `C_i` has no neighbour in the rest of
`L`.  There are certainly vertices outside it: `D_i` is nonempty and is
disjoint from both deleted vertices and from `C_i`.  Hence
`{z_C,t_i}` separates `G[L]`, contrary to three-connectivity.

The same contradiction follows from any `D_i`, using
`{z_D,t_i}`.  Therefore even one arm satisfying hypotheses 1--3 is
impossible in the stated setting.  No comparison of the two tripod
centres is needed.

This yields a valid, stronger elementary replacement:

> If `T` is a three-cut of a three-connected graph, `C` is a component
> of `L-T`, `z in C`, and `K` is a component of `C-z`, then `K` has
> neighbours at at least two vertices of `T`.

Indeed, otherwise `N_L(K)` is contained in `z` together with at most one
gate vertex, an order-at-most-two separator.

## 2. The advertised unused components invalidate (2.2)

Even if one temporarily ignores the preceding contradiction, equation
(2.2)

\[
                     N_L(H_i)\subseteq\{z_C,z_D\}
\]

is false under the theorem's explicit allowance of arbitrary additional
components of `C-z_C` and `D-z_D`.  The set `H_i` contains `t_i`.  An
unused component `F` of `C-z_C` may have a neighbour at `t_i`; that
vertex of `F` then lies in `N_L(H_i)` but is neither centre.  The three
listed conditions constrain only the selected `C_j,D_j`, not unused
components.

In fact, three-connectivity forces an unused component to meet at least
two gate vertices, by the replacement observation above, so this is not
a merely artificial possibility.  Once (2.2) fails, deleting
`{z_C,z_D} union N_S(H_i)` need not isolate `H_i`, and the claimed bound
`|N_S(H_i)|>=5` is unavailable.

A nonvacuous version of the carrier proof would have to assume the
closed-sector condition

\[
                     N_L(H_i)\subseteq\{z_C,z_D\}
\]

directly.  But that condition itself is incompatible with the present
three-connected clean-arm setup for essentially the same two-cut reason.
Crossed gate incidence is therefore mandatory, not an exceptional next
case.

## 3. Conditional audit of the remaining construction

Conditional on (2.2), the subsequent reasoning is correct:

1. `H_1,H_2,H_3` are disjoint and connected.  The centres are distinct
   because `z_C in C`, `z_D in D`, and the lobes are disjoint; neither
   centre lies in a selected component after its deletion.  The three
   gate vertices are also distinct.
2. Seven-connectivity would give `|N_S(H_i)|>=5`, because the asserted
   separator has order `2+|N_S(H_i)|` and the opposite open shore
   survives.
3. Three subsets of a seven-set, each of size at least five, have a
   common label `q`: their three complements have total size at most
   six.
4. The three carriers in (3.1) have all three pairwise adjacencies.  For
   `B_1B_2` one may use the edge from `z_C` to `C_2` (or the edge from
   `z_D` to `D_1`); the other two pairs use the stated centre-to-sector
   edges.
5. After excluding `q`, each of the three portal sets has size at least
   four.  Hall's condition for three sets is immediate, so the SDR
   `s_1,s_2,s_3` exists.
6. Enlarging each carrier by its literal anchor preserves disjointness,
   connectivity and the carrier clique.  The three remaining literal
   labels anchor the three disjoint `S`-full packets.  Packet fullness
   supplies every packet--packet and packet--carrier adjacency, giving
   seven literal branch bags.

Thus there is no hidden collision among the centres or selected sector
components, and the final bag check is sound.  The failure is earlier:
the clean sectors cannot coexist with three-connectivity, and unused
components make the claimed separator containment false even before
that contradiction is used.

## 4. Disposition

Do not promote Theorem 1.1 as a new exchange result.  Replace it, if
useful, by the elementary **crossed-arm necessity** above: every
component of `C-z_C` meets at least two literal gate vertices.  That is
the actual structural information forced by three-connectivity and
shows that the programme should start directly with crossed sectors.
