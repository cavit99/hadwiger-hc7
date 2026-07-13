# Two exceptional Moser packet cycles already contain `K_7`

**Status:** proved and independently audited, with an exact six-row
branch-set certificate.  No cross-packet rung, packet adjacency, or palette
argument is used.

## 1. Literal setting

Let `S={0,...,6}` induce the standard Moser spindle

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.           \tag{1.1}
\]

Let `T,P,Q` be pairwise disjoint connected `S`-full subgraphs outside `S`.
Suppose `P` contains a cycle `Z_P` with six pairwise distinct
literal portals `p_0,...,p_5`, and `Q` contains a cycle `Z_Q` with portals
`q_0,...,q_5`, in the cyclic orders displayed by their indices, such that

\[
\begin{array}{c|cccccc}
i&0&1&2&3&4&5\\ \hline
\text{boundary neighbour of }p_i,q_i&2&4&5&3&1&0.
\end{array}                                             \tag{1.2}
\]

Arcs between consecutive selected portals may have arbitrary positive
length.  No condition is imposed on where the packets meet literal vertex
`6`.  The same theorem holds with `P,Q` interchanged.

### Theorem 1.1 (exceptional cyclic-packet completion)

Under these hypotheses, `G` contains a literal `K_7` minor.

Thus in an actual exact-seven `(1,2)` adhesion, two packet cores cannot both
realize the exceptional cyclic order (1.2): connectedness and fullness of
either packet supply a clean path from the seventh boundary literal to its
cycle, and the thin shore supplies `T`.

## 2. Six gap-avoiding base models

First suppress every open cycle arc to one edge and contract `T` to a
boundary-universal vertex `t`.  Write a string such as `p_2p_3p_4` for the
connected path on those consecutive cycle vertices.  For each `g`, delete
the cycle edge `p_gp_{g+1}` (indices modulo six) and add the edge `6p_g`.
The following row consists of seven branch sets forming a `K_7` model.

| gap `g` | seven branch sets |
|---|---|
| 0 | `{0}`; `{3,q3,q4}`; `{t}`; `{2,q0,q1,q5}`; `{1,p2,p3,p4}`; `{5,6,p0,p5}`; `{4,p1}` |
| 1 | `{1,6,p1,q4}`; `{4}`; `{5,p2,p3,p4,p5}`; `{2,q0,q1,q2,q5}`; `{3,q3}`; `{0}`; `{t}` |
| 2 | `{1,q4}`; `{4,6,p1,p2}`; `{q0,q1,q2,q5}`; `{3,p3,p4,p5,q3}`; `{2,p0}`; `{0}`; `{5,t}` |
| 3 | `{p0,p1,p2,p5}`; `{0,3}`; `{5,q0,q1,q2}`; `{6,p3}`; `{4,t}`; `{1,p4,q4,q5}`; `{2}` |
| 4 | `{0,p5}`; `{5,p0,p1,p2}`; `{4,q0,q1,q5}`; `{2}`; `{3,6,p3,p4}`; `{1,q2,q3,q4}`; `{t}` |
| 5 | `{1,q3,q4}`; `{0}`; `{6,p4,p5}`; `{2,p0,p1,q0,q5}`; `{4,5,q2}`; `{t}`; `{3,p2,p3}` |

### Lemma 2.1 (the table is literal)

Every row consists of seven nonempty, pairwise vertex-disjoint, connected
sets, and every two sets have a literal edge between them in the graph just
described.

#### Verification

Connectivity uses only:

* the two cycle edges other than the deleted gap;
* the portal edges from (1.2);
* the displayed edge `6p_g`;
* the Moser edges (1.1); and
* the edges from `t` to `S`.

Every pairwise adjacency is checked against the same five edge classes.
There are exactly 21 pairs in each row.  The deterministic verifier

`results/hc7_exact7_moser_cyclic_packet_completion_verify.py`

checks nonemptiness, disjointness, connectivity, and prints one literal
witness edge for every one of the 126 row/pair incidences.  It terminates
with

`CERTIFIED six gap-avoiding literal K7 models`.

This finite table is not an existence search: its seven branch sets are the
certificate.  The verifier merely guards the 126 routine edge checks.

## 3. Lifting from an arbitrary packet contact

Because `P` is `S`-full, choose `z in P` adjacent to literal vertex `6`.
Inside connected `P`, take a shortest path from `z` to `Z_P`, and prepend
the edge `6z`.  After shortening at the first cycle hit, this gives a path

\[
 R:6\longrightarrow x,
 \qquad V(R)\cap(S\cup V(Z_P))=\{6,x\}.                 \tag{3.1}
\]

Thus the location of the original `6`-portal inside `P` is irrelevant.

Let `A_g` be a selected-portal-free arc of `Z_P` from `p_g` to `p_{g+1}`
whose interior contains `x`.  If `x=p_i` is itself a selected portal, take
`g=i`, so that `x=p_g`; do not use the preceding arc.
Use row `g` of the table.  In that row, literal vertices `6,p_g` lie in the
same branch set and the base edge `p_gp_{g+1}` is not used at all.

Replace the artificial edge `6p_g` inside that branch set by the literal
path

\[
                         R\cup xA_gp_g.                  \tag{3.2}
\]

Ignore the rest of `A_g` from `x` toward `p_{g+1}`.  This preserves
connectedness and creates no intersection with another bag.

For every other subdivided cycle arc, lift the corresponding base model in
the standard literal way.  If both end portals lie in one bag, add the whole
open arc to that bag.  If they lie in two bags and their base edge witnesses
an adjacency, split the open arc at one literal edge and assign its two
sides to the two bags.  Unused open-arc vertices may be omitted.  Hence all
cycle connectivity and adjacency in Lemma 2.1 survives arbitrary
subdivision.

Finally replace `t` by the actual connected packet `T`.  A table bag
containing both `t` and a boundary vertex becomes `T` together with that
vertex and is connected because `T` is `S`-full.  Every table adjacency
using a `t-s` edge lifts to a literal edge from `T` to `s`.  All other bags
and edges are unchanged.

We have therefore lifted the selected row to seven literal, connected,
disjoint, pairwise adjacent branch sets in `G`.  This proves Theorem 1.1.

## 4. Exact consequence and scope

The theorem eliminates the atomic coherent-cylinder residue, rather than
merely describing it:

* the two exceptional cycles may lie in one rich component or in two
  different rich components;
* no path or edge between them is required;
* the portal of `6` may occur anywhere in the connected packet, not merely
  on the cycle; and
* arbitrary extra packet vertices and edges are harmless because the model
  uses a subgraph.

What remains outside this theorem is a packet whose three attained-duty
hulls form the alternating web without containing a literal exceptional
cycle of the form (1.2), or an attained state whose duties are not the Moser
three-pair state.  No reduction of the general `(1,2)` cell to Moser is
claimed.
