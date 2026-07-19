# A paired source path gives a branch-set transfer or an order-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_paired_source_path_transfer_audit.md`](hc7_paired_source_path_transfer_audit.md).
This note is a
local continuation of the audited three-owner order-eight reduction.  It
keeps two specified edge-deletion responses on the separation returned by a
fan argument.  It does not synchronize the colourings of the two closed
shores, eliminate the other exact-seven terminal modes, or prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and suppose

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Use the notation and all the hypotheses of the audited
[three-owner concentration theorem](../results/hc7_three_owner_reserved_component_concentration.md).
Thus `G` has a spanning labelled minor model

\[
                 X,Y,D,U,F_1,F_2,F_3                 \tag{1.2}
\]

of `K_7` with at most the adjacency `X-Y` missing, and

\[
                 U=U_0\mathbin{\dot\cup}C.            \tag{1.3}
\]

Here `G[U_0]` and `G[C]` are connected, `C` is adjacent to `U_0`, and

\[
 N_G(C)=S=
 \{k_1,k_2\}\mathbin{\dot\cup}
 \{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.           \tag{1.4}
\]

The vertices `k_1,k_2` belong to `U_0`; each of the other six displayed
vertices is the unique member of `S` in the correspondingly labelled
branch set.  There are exactly three branch sets

\[
 I=\{R_1,R_2,R_3\}\subseteq\{X,Y,F_1,F_2,F_3\}       \tag{1.5}
\]

whose old contacts with `U` all lie in `C`.  In particular, every edge
from `C` to `R_i` ends at the vertex

\[
                         s_i:=s_{R_i}.                 \tag{1.6}
\]

For two of these branch sets, relabelled as `R_1,R_2`, the concentration
theorem supplies vertex-disjoint edges

\[
                         e=a_1s_1,\qquad f=a_2s_2,     \tag{1.7}
\]

where `a_1,a_2` are distinct vertices of `C`.  Deleting these two edges
gives the three endpoint-colour signatures

\[
 ({\rm equal},{\rm equal}),\qquad
 ({\rm equal},{\rm proper}),\qquad
 ({\rm proper},{\rm equal}),                          \tag{1.8}
\]

whereas `({\rm proper},{\rm proper})` is impossible.  The roots, the
selected boundary partition, and the fixed connected response subgraph in
`D`, together with its fixed edge to `U_0`, are the data used in the
lexicographic choice of (1.2): first maximize the relaxed literal first-hit
rank and then minimize `|U|`.

Let `P` be a shortest `a_1`--`a_2` path in `G[C]`, put

\[
                         T=\{k_1,k_2,s_1,s_2,s_3\},   \tag{1.9}
\]

and form

\[
                         H=G[C\cup T]/P.              \tag{1.10}
\]

Write `r` for the vertex obtained by contracting `P`.  Parallel edges, if
created, are immaterial.

## 2. The paired-source alternative

### Theorem 2.1

In the setting above, at least one of the following holds.

1. The seven branch sets can be changed, without changing their labels or
   the fixed response data, so that either they form an explicit
   `K_7`-minor model or they again form a spanning labelled
   `K_7`-minus-one-edge model, the relaxed first-hit rank does not decrease,
   and the new `U` branch set is a proper subset of the old one.
2. There is a nonempty connected proper subset `A` of `C` such that

   \[
                         |N_G(A)|=7,                  \tag{2.1}
   \]

   at least one of the edges `e,f` crosses between `A` and `N_G(A)`.  Every
   proper-minor colouring belonging to a crossing designated edge restricts
   to the corresponding operated closed `A`-shore.  If the five-fan fails,
   both `e,f` cross and all three endpoint-colour signatures in (1.8)
   restrict to the two-edge-deleted closed `A`-shore.

Consequently the first outcome contradicts the lexicographic choice of the
model (or the exclusion of a `K_7` minor).  The second outcome is an actual
order-seven separation retaining the two differently labelled operated
edges when the five-fan fails, and at least one of them in every case.
Together with any proper six-colouring obtained by deleting a crossing
designated edge, it is a generic exact-seven response interface in the
sense of the audited generic restart theorem.  It is not asserted that the
induced partition extends through the intact closed `A`-shore.

#### Proof

Apply the fan form of Menger's theorem in `H`, from `r` to the five-element
set `T`.

### 2.1 Failure of a five-fan

Suppose first that no five-fan exists.  There is then a set

\[
                         Z\subseteq V(H)-\{r\},
                         \qquad |Z|\le4,              \tag{2.2}
\]

separating `r` from `T-Z`.  The two direct edges `rs_1,rs_2` are the
images of `e,f`.  Hence

\[
                         s_1,s_2\in Z.                \tag{2.3}
\]

Let `A` be the literal lift in `C` of the component of `H-Z` containing
`r`; in particular, `P\subseteq A`.  Componenthood and (1.4) give

\[
                 N_G(A)\subseteq (S-T)\cup Z.         \tag{2.4}
\]

The two sets on the right are disjoint and have total order at most
`3+4=7`.

Since `|T|=5>|Z|`, choose `t\in T-Z`.  The vertex `t` lies outside both
`A` and `N_G(A)`.  Moreover `C` has a neighbour of `t`, by (1.4).  Such a
neighbour cannot belong to `A`, so `A` is a proper subset of `C`.  Thus
(2.4) is a nontrivial host separation.  Seven-connectivity forces equality
throughout:

\[
                    |Z|=4,\qquad
                    N_G(A)=(S-T)\mathbin{\dot\cup}Z,
                    \qquad |N_G(A)|=7.                \tag{2.5}
\]

Both `a_1,a_2` lie on `P\subseteq A`, while `s_1,s_2` lie in `Z`; hence
`e,f` both cross the separation.  Restricting any of the proper
six-colourings of `G-\{e,f\}` from (1.8) to

\[
                  G[A\cup N_G(A)]-\{e,f\}             \tag{2.6}
\]

preserves its endpoint-colour signature and its exact equality partition
on the new literal boundary.  This proves outcome 2.  Notice that the
argument makes no claim that the same partition colours the intact
`A`-shore.

### 2.2 A five-fan

Suppose now that a five-fan exists.  Stop every fan path at its first
vertex of `T`.  Replace the paths ending at `s_1,s_2` by the direct edges
`rs_1,rs_2`.  On lifting the contraction of `P`, the other three paths are
paths

\[
                         Q_1,Q_2,Q_3                  \tag{2.7}
\]

from `P` respectively to `k_1,k_2,s_3`.  They are pairwise disjoint
outside `P`; each meets `P` only at its initial vertex; and they avoid
`s_1,s_2`.

We distinguish whether the `P`--`s_3` path has an internal vertex in `C`.

#### Case A: the third-owner path has a nonempty internal part

Let `L_3` be the nonempty set of internal `C`-vertices of `Q_3` after its
initial vertex on `P`.  It induces a connected path, has an edge to `P`,
and has an edge to `s_3`.  Put

\[
 D_0=P\cup(V(Q_1)\cap C)\cup(V(Q_2)\cap C).           \tag{2.8}
\]

The subgraph `G[D_0]` is connected.  It has an edge to each of `k_1,k_2`
along the last edge of the relevant path, and it is disjoint from `L_3`.
The first edge of the third path joins `D_0` to `L_3`.

Every component of `C-(D_0\cup L_3)` has an edge to `D_0\cup L_3`, since
`C` is connected.  Assign each such component to one adjacent one of these
two connected sets.  This gives a partition

\[
                         C=D_0'\mathbin{\dot\cup}L_3', \tag{2.9}
\]

where both parts are nonempty and connected and have an edge between them.
Replace

\[
                         U\quad\hbox{by}\quad U_0\cup D_0',
 \qquad
                         R_3\quad\hbox{by}\quad R_3\cup L_3'.             \tag{2.10}
\]

The new `U` branch set is connected through either of the edges to
`k_1,k_2`; the enlarged `R_3` branch set is connected through the last
edge of `Q_3`; and their mutual adjacency is the edge between the two
parts in (2.9).  The direct edges `e,f` preserve the `U-R_1` and `U-R_2`
adjacencies.  The retained set `U_0` preserves the adjacencies to the other
branch sets and the fixed response edge from `D`.

All seven sets therefore remain connected, disjoint and spanning.  Every
old adjacency remains, except that the transfer may additionally repair
`X-Y`.  If it does, the seven sets are an explicit `K_7`-minor model.  If
it does not, they form a compatible labelled `K_7`-minus-one-edge model.
In the latter model the new `U` branch set is strictly smaller because
`L_3'` is nonempty.

The relaxed first-hit rank does not decrease.  A ranked path with label
different from `U` avoided all of the old branch set `U`, and therefore
avoids the transferred vertices.  If a ranked `U`-path ended in transferred
vertices, replace its terminal portion by a path in the fixed connected
response subgraph in `D` followed by the fixed edge into `U_0`.  This is
the same label-preserving replacement used in the audited
[first-hit rank transfer theorem](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md).
The prescribed roots and the selected boundary partition are unchanged.
Thus outcome 1 holds.

#### Case B: the third-owner path is direct

There is a vertex `p_3\in P` such that `p_3s_3` is an edge.  Choose

\[
                         a_i\in\{a_1,a_2\}-\{p_3\},   \tag{2.11}
\]

which is possible because `a_1\ne a_2`, and let `a_j` be the other
endpoint.  Let `C'` be the component of `C-a_i` containing `a_j`.  Since
`a_i` is an endpoint of `P`, the path `P-a_i` lies in `C'`; in particular,
`p_3\in C'`.  Put

\[
                         L=C-C'.                      \tag{2.12}
\]

The set `L` is nonempty and connected.  Indeed, it contains `a_i`, and
every component of `C-a_i` other than `C'` has a neighbour at `a_i`.

Suppose first that `C'` has no neighbour in `\{k_1,k_2\}`.  Componenthood
in `C-a_i`, (1.3), and (1.4) then give

\[
 N_G(C')\subseteq
 \{a_i\}\cup\{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.                   \tag{2.13}
\]

The right-hand side has order seven.  The connected set `U_0` is nonempty
and lies on the opposite side, so (2.13) is a nontrivial separation.
Seven-connectivity forces `|N_G(C')|=7`.  The selected endpoint `a_j`
belongs to `C'`, whereas `s_j\in N_G(C')`; also `p_3\in C'` and
`s_3\in N_G(C')`.  In particular the designated edge `a_js_j` crosses this
exact order-seven separation.  Its one-edge-deletion colouring restricts
to the corresponding operated closed shore, giving outcome 2.  (Both
`e,f` need not cross in this subcase.)

It remains that `C'` has a neighbour in `\{k_1,k_2\}`.  Replace

\[
                         U\quad\hbox{by}\quad U_0\cup C',
 \qquad
                         R_i\quad\hbox{by}\quad R_i\cup L.               \tag{2.14}
\]

The new `U` branch set is connected through the edge from `C'` to
`\{k_1,k_2\}`.  The enlarged `R_i` branch set is connected through
`a_is_i`.  The first edge of `P` at its endpoint `a_i` joins the two new
branch sets.  The direct edge `a_js_j` preserves the adjacency to `R_j`,
and `p_3s_3` preserves the adjacency to `R_3`.  The set `U_0` preserves all
other old adjacencies and the fixed response edge.

As in Case A, the resulting seven sets either form an explicit `K_7`-minor
model or a compatible labelled `K_7`-minus-one-edge model of no smaller
relaxed first-hit rank.  Its `U` branch set is strictly smaller because
`L` is nonempty.  Thus outcome 1 holds and the theorem is proved. \(\square\)

## 3. Exact contribution and trust boundary

The ordinary three-fan argument already proves that the concentrated
three-owner order-eight configuration has some order-seven separation.
The added content here is operation placement: in the five-fan failure,
both differently labelled deletion edges cross the returned boundary; in
the direct-third-owner endpoint case, at least one named deletion edge
crosses.  Hence every separation outcome carries a legal proper-minor
colouring into the smaller connected shore.

This theorem deliberately does **not** say that the boundary partition of
that colouring extends through the intact smaller shore, nor that the two
closed shores realize one common equality partition.  It also does not
close a generic exact-seven singleton shore, separator excess, or a
shore-filling positive-excess list-critical core.  Its role is only to
bridge a labelled order-eight obstruction to the already defined generic
order-seven response recursion, or to perform a strict rank-preserving
branch-set transfer.

The extreme path in which the third owner and one selected owner attach at
one endpoint of `P`, while `k_1,k_2` and the other selected owner attach at
the other endpoint, falls under Case B.  Removing the latter endpoint
leaves a component with no `k_1,k_2` neighbour, so seven-connectivity gives
the exact order-seven separation in (2.13); no unsupported strict transfer
is claimed for that example.

## 4. Dependencies

- [three-owner concentration and two-edge response](../results/hc7_three_owner_reserved_component_concentration.md)
- [rank preservation under a labelled branch-set transfer](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md)
- [generic exact-seven selected-response interfaces](../results/hc7_generic_exact7_response_restart.md)
- the fan form of Menger's theorem.
