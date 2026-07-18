# First-entry components at an exact order-seven separation

**Status:** written proof; separate internal audit GREEN.  This is a
conditional reduction in the hard exact order-seven `(1,2)` branch.  It
closes every non-direct first-entry component with at least five boundary
contacts and identifies the exact remaining bridge geometry.  It does not
split that bridge or prove `HC_7`.

## 1. Setup

Let `G` be seven-connected, `K_7`-minor-free, not six-colourable, and
suppose that every proper minor of `G` is six-colourable.  Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
 \qquad E_G(L,R)=\varnothing,                         \tag{1.1}
\]

where `L,R` are nonempty.  Assume that `H=G[S]` is one of the ten
absolute-demand-three boundary graphs covered by the audited
defect-two-carrier theorem.

Every component of `G[L]` is adjacent to all seven vertices of `S`.
Indeed, its whole neighbourhood is contained in `S`, it is separated from
the nonempty shore `R`, and seven-connectivity forces all seven boundary
vertices into its neighbourhood.  Fix one such connected `S`-full
subgraph `P_0` in `L`; it is the opposite full subgraph used by the
adaptive contraction in the proof below.

Let `P_1,P_2` be vertex-disjoint connected subgraphs of `G[R]`, each
adjacent to every literal vertex of `S`.  Let `Q` be an `r-z` path in
`G[R union S]`, where `r,z in S`, whose internal vertices lie in `R` and
which meets `P_1 union P_2`.  Orient `Q` from `r`, and let `y` be its first
vertex in `P_1 union P_2`.

If `y` is the first vertex after `r`, call the entry **direct**.  Otherwise
let `K` be the component of

\[
                         R-(P_1\cup P_2)               \tag{1.2}
\]

containing the nonempty internal prefix of `Q` before `y`.  Define

\[
 T_K=N_G(K)\cap S,
 \qquad
 A_K=N_G(K)\cap(V(P_1)\cup V(P_2)).                   \tag{1.3}
\]

Thus `T_K` records literal boundary contacts and `A_K` records distinct
attachment vertices on the two selected full connected subgraphs.

## 2. Reduction theorem

### Theorem 2.1

Under the setup above, at least one of the following holds.

1. `G` is six-colourable.
2. The path `Q` has a direct first entry into `P_1 union P_2`.
3. The component `K` in (1.2) is defined and satisfies

   \[
        r\in T_K,
        \qquad |T_K|\le4,
        \qquad |A_K|\ge3,                             \tag{2.1}
   \]

   and its whole-graph neighbourhood is exactly

   \[
                         N_G(K)=T_K\mathbin{\dot\cup}A_K. \tag{2.2}
   \]

Consequently, in a hypothetical counterexample every non-direct first
entry lies in a connected subgraph with boundary defect at least three and
at least three distinct attachments to the selected pair.  In particular,
the first-entry programme closes the whole unbounded family in which the
pre-entry component has at least five literal boundary contacts.

### Proof

Suppose the entry is not direct.  Every internal vertex of the `r-y`
subpath except `y` belongs to `R-(P_1 union P_2)`.  Since those vertices
form a connected set, they all lie in one component `K` of (1.2).  The
first edge of `Q` gives a literal `r-K` edge, so `r in T_K`, and the last
edge before `y` shows that `A_K` is nonempty.

There is no `L-R` edge.  Moreover, because `K` is a component after
deleting `P_1 union P_2`, every neighbour of `K` in `R-K` lies in the
selected pair.  This proves (2.2).

Suppose first that `|T_K|>=5`.  Then `K` is a connected third subgraph,
disjoint from the two full connected subgraphs, whose boundary defect has
order at most two.  Apply Theorem 2.2 of the audited connected-rich
carrier exchange: for the fixed hard boundary graph and this defect set,
choose the prescribed maximal independent block and contract it together
with `P_0` on the opposite shore.  Every exact state returned by that
proper-minor operation
reflects through `P_1,P_2,K`.  The two closed-side colourings align on `S`
and glue, making `G` six-colourable.  This is outcome 1.

We may therefore assume `|T_K|<=4`.  The set in (2.2) separates the
nonempty connected set `K` from the nonempty opposite shore `L`.
Seven-connectivity gives

\[
                         |T_K|+|A_K|\ge7.              \tag{2.3}
\]

Hence `|A_K|>=3`, proving (2.1) and outcome 3.  \(\square\)

## 3. What lexicographic minimization does not add

Choosing `P_1,P_2` to minimize their total order and then choosing `Q` to
minimize its intersection with their union does not turn outcome 3 into a
split.  The three attachment vertices may be indispensable portal or
branch vertices of minimal trees spanning the seven boundary contact
classes.  A path through `K` can then replace a segment only by deleting a
required contact, losing the edge between the two selected subgraphs, or
using at least as many vertices.

The correct next input is therefore a proper-minor colouring response at a
literal attachment, or a label-preserving multi-segment bridge exchange.
Path existence and lexicographic order alone do not provide a smaller pair
of boundary-full connected subgraphs.

## 4. Dependencies and scope

- [Two full connected subgraphs and Kempe compression](hc7_exact7_two_full_subgraph_kempe_compression.md)
- [Connected-rich defect-two carrier exchange](../results/hc7_exact7_connected_rich_cutvertex_exchange.md), Theorem 2.2
- [First-entry minimality barrier](../barriers/hc7_first_entry_packet_minimality_barrier.md)

The theorem assumes that the relevant hard boundary graph and two full
connected subgraphs already exist on the correct shore.  It does not
produce the forced bichromatic path, handle a direct entry, preserve a
previously selected minor model, synchronize a new order-seven boundary,
or reduce the support-at-most-four three-attachment case.
