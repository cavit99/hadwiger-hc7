# Retained-bag colour views: exact states and the first portal cocycle exchange

## Status

This note makes two corrections and proves one exact exchange theorem.

* The sixteen `Q`-full normalizations of a spanning `K_7^vee` model are
  sixteen **structural** views, but only seven underlying retained-bag
  minors.  They do not provide sixteen independent colour states.
* Equality partitions of the six singleton bags have no cross-view parity
  by themselves.  A sharp `K_7`-minor-free expansion realizes the two
  repeated states independently in every neutral view.
* When the four retained neutral carriers are literal edges and their
  repeated states are rigid, the missing faithful datum begins with one
  portal matching bit per pair.  On the **selected minimal portal
  skeleton**, the state bits and matching bits satisfy an exact `Z_2`
  state-alignment theorem: a nonzero state-relative edge discrepancy
  gives an explicit `K_7` model, while zero discrepancy gives an explicit
  six-colouring of that skeleton.  Extra
  wrong-layer contacts require the fuller compatibility relation in
  Section 6 and are not silently discarded when colouring the host.

The last result is a genuine label-preserving exchange theorem for the
smallest carrier cell.  It does not yet treat an unbounded carrier.

## 1. The sixteen structural views are seven colour minors

Let a spanning `K_7^vee` model have bags

\[
        A,B,C,U_1,U_2,U_3,U_4,                     \tag{1.1}
\]

where only `AB` and `AC` are not required.  For a retained bag `X`, let
`V_X` be the minor obtained by contracting a spanning tree in each of the
other six bags and doing nothing inside `X`.

### Proposition 1.1 (view collapse and properness)

The sixteen normalizations in
`hadwiger_spanning_k7vee_qfull_normalization.md` have only the seven
underlying minors

\[
             V_A,V_B,V_C,V_{U_1},\ldots,V_{U_4}.    \tag{1.2}
\]

The four choices of omitted neutral label give the same minor for each of
`A`, `B`, and `C`; only the designation of the neutral triangle changes.
Moreover `V_X` is a proper minor exactly when at least one bag other than
`X` is nonsingleton.

Consequently all sixteen structural views are proper exactly when at least
two original bags are nonsingleton.  If exactly one bag `Z` is
nonsingleton, precisely the structural views retaining `Z` equal `G`; all
other retained-bag minors are proper.

#### Proof

For fixed `X`, the contraction map is independent of which three neutral
images are subsequently called `Q`.  This proves (1.2).  A spanning tree
contraction changes the graph precisely when its bag has at least two
vertices.  Hence `V_X=G` precisely when all six nonretained bags are
singletons.  The final assertions follow immediately. \(\square\)

In a non-six-colourable, `K_7`-minor-free graph not all seven bags can be
singletons: then the graph has seven vertices, is not complete, and is
six-colourable by assigning one colour to a nonadjacent pair.

## 2. Exact equality states and dark carrier classes

Assume `V_X` is proper in a proper-minor-minimal non-six-colourable graph,
and six-colour it.  Record only the equality partition on the six
contracted singleton bags.

### Proposition 2.1 (complete equality-state list)

Writing `R` for the rainbow state, the only possibilities are

\[
\begin{array}{c|c}
X&\hbox{singleton equality state}\\ \hline
A&R,\\
B&R\ \hbox{or}\ AC,\\
C&R\ \hbox{or}\ AB,\\
U_j&R,\ AB,\ \hbox{or}\ AC.
\end{array}                                            \tag{2.1}
\]

#### Proof

For `X=A`, the six singleton labels `B,C,U_1,\ldots,U_4` induce `K_6`.
For `X=B`, their graph is `K_6-AC`; for `X=C` it is `K_6-AB`.  For
`X=U_j`, their only nonedges are `AB,AC`.  Every colour class on the six
singletons is therefore a singleton except possibly one of the displayed
nonedges.  Since `BC` is an edge, both repeated pairs cannot occur at
once. \(\square\)

There is also a portal statement which equality notation alone suppresses.
For a colour `gamma`, put

\[
       D_\gamma=\{x\in X:c(x)=\gamma\}.             \tag{2.2}
\]

If a singleton label `Y` has colour `gamma`, then

\[
       D_\gamma\cap N_X(Y)=\varnothing.             \tag{2.3}
\]

If `A,B` (or `A,C`) repeat, the corresponding class is dark to both
labels.  A colour absent from the singleton boundary is the unique free
class.  Thus a faithful state must record which **carrier vertices** lie
in each dark class and which portal classes they meet; (2.1) by itself
does not do so.

## 3. Sharp insufficiency of the seven equality families

Start with literal `K_7^vee` on vertices `x_A,x_B,x_C,x_{U_1},\ldots,
x_{U_4}`.  Add one private leaf `y_X` at every `x_X`, and use
`{x_X,y_X}` as the branch bag labelled `X`.

### Proposition 3.1 (independent neutral choices)

This graph is `K_7`-minor-free, every retained-bag view is proper and
six-colourable, and its exact state families are

\[
\begin{array}{c|c}
A&\{R\},\\
B&\{R,AC\},\\
C&\{R,AB\},\\
U_j&\{AB,AC\}\quad(j=1,2,3,4).
\end{array}                                            \tag{3.1}
\]

In particular, the four neutral view colourings may independently select
any of the sixteen words in `\{AB,AC\}^4`.  There is no parity or Helly
constraint on **chosen equality states**.

#### Proof

A pendant vertex cannot be a singleton branch set of a clique model of
order at least three.  Absorbing or deleting every pendant vertex turns
any such model into one in the `K_7^vee` core.  The core has seven
vertices and is not complete, so it has no `K_7` minor.

Every retained view contracts six nontrivial leaf edges and is proper.
For a neutral retained bag, its core endpoint sees all six singleton
labels.  A rainbow boundary leaves it no colour, while either repeated
state uses five colours and leaves a sixth colour for the core endpoint;
the leaf then receives a different colour.  The other three rows follow
in the same way from the boundary graphs used in Proposition 2.1. \(\square\)

The verifier
`near_k7_seven_view_state_counterarchitecture.py` checks (3.1), computes
treewidth five, and performs an exact `K_7` branch-set search.

This example is deliberately not seven-connected or minor-critical.  Its
point is exact: the mere existence of colourings of all proper retained
views supplies no cross-view relation.  Minor-criticality must be used
through a portal-faithful operation transition, not merely to assert that
the views are colourable.

### High-connectivity check: the icosahedral two-apex architecture

The sharp connectivity-only example `K_2 join I`, where `I` is the
icosahedron, has the spanning `K_7^vee` model of Proposition 1.2 in
`hadwiger_near_k7_two_complex_bag_round.md`.  With

\[
 A=\{b\},\quad B=\{t\},\quad C=\{u_0\},\quad
 P=\{p\},\quad Q=\{q\},
\]

and the two complex neutral bags `D,E` displayed there, exact retained-view
enumeration gives

\[
\begin{array}{c|c}
A&\{R\},\\
B&\{R,AC\},\\
C&\{R,AB\},\\
P,Q&\{AB,AC\},\\
D&\{R,AC\},\\
E&\{R,AB,AC\}.
\end{array}                                            \tag{3.2}
\]

Thus this seven-connected, `K_7`-minor-free example does **not** destroy
all repeated-state Helly structure: the four neutral views have the common
state `AC`.  It lies in the coherent two-apex alternative (although its
actual apex pair `p,q` is not the deficient pair `A,C`).  The computation
is independently reproducible with
`near_k7_icosahedron_retained_view_states.py`, which also checks
seven-connectivity and planarity after deleting `p,q`.

This is positive evidence for a high-connectivity state theorem, but not a
proof: the leaf expansion remains the sharp obstruction to deriving one
from colourability of the views alone.

## 4. The rigid edge-carrier skeleton

The smallest setting in which such a faithful transition appears has four
neutral carriers which are literal edges.  Let

\[
       D_i=p_iq_i\qquad(i=1,2,3,4)                 \tag{4.1}
\]

and retain singleton vertices `a,b,c`, with `bc` an edge and `ab,ac`
absent.  Every `D_i` is collectively adjacent to `a,b,c` and to every
other `D_j`.

Call `D_i` **rigid of type 0** if its retained-edge view admits the `AB`
state but not the `AC` state, and **rigid of type 1** if it admits `AC`
but not `AB`.  Write this type as `t_i`.

### Lemma 4.1 (forced rows)

After possibly interchanging the ends of `D_i`, the following edges may
be selected:

\[
\begin{array}{c|cc}
t_i&p_i&q_i\\ \hline
0& a,b&b,c\\
1& a,c&b,c.
\end{array}                                            \tag{4.2}
\]

Moreover both `p_i` and `q_i` have a neighbour in every other carrier
`D_j`.

#### Proof

In either repeated state there is one colour absent from the six singleton
boundary vertices.  That free colour is available at each end of `D_i`;
because the two ends are adjacent, the edge is colourable exactly when at
least one end has a second available boundary colour.

Suppose `t_i=0`.  Failure of the `AC` state says that each end sees the
`B` colour, each of the three other neutral colours, and the common
`AC` colour.  Hence each end meets `b`, every `D_j`, and at least one of
`a,c`.  The `AB` state can then extend only because one end, call it
`p_i`, misses `c`; it consequently meets `a`.  Collective contact with
`c` puts a `c`-edge at the other end `q_i`.  This gives the first row.
The second is symmetric under interchanging `b,c`. \(\square\)

The endpoint choice in the proof also records two forced nonedges which
are not shown in the selected-edge table (4.2): for type zero,
`p_i c` is absent, and for type one, `p_i b` is absent.  Equivalently,
after the switch (5.5), a type-zero `x_i` misses `c` and a type-one
`y_i` misses `b`.  These absences are used in the colouring step of
Theorem 6.4; they follow from rigidity, not merely from omitting an edge
from the minimal skeleton.

For every pair `i,j`, the bipartite contact graph between the two
two-vertex carriers has no isolated vertex.  It therefore contains a
perfect matching.  Select one and put

\[
 s_{ij}=\begin{cases}
 0,&p_ip_j,q_iq_j\text{ are selected},\\
 1,&p_iq_j,q_ip_j\text{ are selected}.
 \end{cases}                                           \tag{4.3}
\]

Let `H(t,s)` be the **minimal portal skeleton** consisting of `bc`, the
four carrier edges, the selected row edges (4.2), and the six selected
matchings (4.3).

## 5. Portal cocycle exchange

### Theorem 5.1 (rigid-edge state cocycle)

For the minimal skeleton `H(t,s)`, one of the following holds.

1. All four type bits are equal.  The four retained views have one
   coherent repeated state.
2. The type bits are not all equal and some

   \[
                 s_{ij}\ne t_i\mathbin\oplus t_j.    \tag{5.1}
   \]

   Then `H(t,s)`, and hence the original graph containing it, has an
   explicit `K_7` minor respecting the displayed boundary vertices and
   carrier endpoints.
3. The type bits are not all equal and

   \[
                 s_{ij}=t_i\mathbin\oplus t_j
                 \quad\text{for every }i<j.          \tag{5.2}
   \]

   Then the selected minimal skeleton `H(t,s)` has an explicit proper
   six-colouring.  This conclusion is deliberately not asserted for an
   ambient host containing additional intercarrier edges.

Thus the state bits `t` form a zero-cochain, the portal matchings `s`
form a one-cochain, and the only target-free mixed state is the
state-aligned coboundary `s=delta t`.  A nonzero edge of the discrepancy
cochain `s+delta t` gives a clique minor; zero discrepancy glues the
colour states.  This is stronger than, and should not be confused with,
ordinary vanishing cycle holonomy of `s`: a different coboundary can have
zero cycle holonomy while still having nonzero state-relative
discrepancy.

#### Proof: an opposite-type parallel edge

Suppose `t_i` and `t_j` differ and `s_{ij}=0`.  Let `k,l` be the other
indices.  The following seven branch sets form a `K_7` model:

\[
 \{b\},\quad\{c\},\quad
 \{p_i,p_j\},\quad\{q_i\},\quad\{q_j\},\quad
 D_k,\quad D_l.                                      \tag{5.3}
\]

The five carrier-derived bags are pairwise adjacent: the first is
connected by the parallel matching, it meets the two `q` singletons by
the carrier edges, `q_iq_j` is the other matching edge, and each whole
carrier meets both ends of every other carrier.  The `p` vertices of
opposite types collectively see both `b,c`; each `q` sees both; and each
whole carrier collectively sees both.  Adding the adjacent singleton
bags `b,c` proves (5.3).

#### Proof: a same-type crossed edge

Suppose `t_i=t_j` and `s_{ij}=1`.  Since the type word is mixed, choose
`k` of the opposite type and let `l` be the remaining index.  If any
opposite-type pair has a parallel selected matching, (5.3) already
applies.  We may therefore assume all opposite-type selected matchings
are crossed.

If `t_i=t_j=0`, use

\[
 \{a,p_i\},\quad \{b\},\quad \{c,q_i\},\quad
 \{p_j\},\quad \{q_j,p_k\},\quad D_l,\quad \{q_k\}.
                                                               \tag{5.4}
\]

Every displayed two-vertex bag is connected: `ap_i` and `cq_i` are row
edges, while `q_jp_k` is an opposite-type crossed matching edge.  The
same-type crossed matching gives `p_iq_j,q_ip_j`; the opposite-type
crossed matchings give `p_iq_k,q_ip_k,p_jq_k,q_jp_k`.
Together with the four carrier edges and the contacts to the whole bag
`D_l`, these edges check every pair in (5.4).  The row table (4.2) checks
all remaining pairs involving `a,b,c`.  Hence (5.4) is a `K_7` model.
For `t_i=t_j=1`, interchange `b` and `c` in (5.4).

The two cases are exactly the two ways in which (5.1) can occur.

#### Proof: the flat colouring

Assume (5.2), and define

\[
(x_i,y_i)=
\begin{cases}
(p_i,q_i),&t_i=0,\\
(q_i,p_i),&t_i=1.
\end{cases}                                           \tag{5.5}
\]

Equation (5.2) says precisely that the selected matching between every
pair is `x_ix_j,y_iy_j`.  Thus the `x_i` induce one `K_4`, the `y_i`
induce a second `K_4`, and the carrier edges are `x_iy_i`.

Give `x_i` colour `i` and `y_i` colour `i+1 modulo 4`.  Give `a,b` a
fifth colour and `c` a sixth.  The two `K_4`s are rainbow, the cyclic
shift makes every carrier edge proper, all carrier colours differ from
the two boundary colours, and `a,b` are nonadjacent.  This is a proper
six-colouring. \(\square\)

The verifier `near_k7_two_vertex_state_helly_verify.py` independently
checks all `14*64=896` mixed type/sign instances.  Its fourteen negative
instances are exactly the coboundaries (5.2), and it checks the displayed
six-colouring on each.

### Theorem 5.2 (uniform edge-carrier cocycle exchange)

Theorem 5.1 is not special to four neutral labels.  Let `n>=4`, replace
the four edges by `D_i=p_iq_i` for `i in [n]`, retain the same three
boundary vertices `a,b,c`, and impose the row table (4.2) and one selected
perfect matching of sign `s_ij` between every carrier pair.  Then exactly
one of the following holds.

1. All `t_i` are equal (one coherent repeated state).
2. The type word is mixed and `s_ij != t_i xor t_j` for some pair.  The
   skeleton contains a `K_{n+3}` minor.
3. The type word is mixed and `s=delta t`.  The selected minimal skeleton
   is properly `(n+2)`-colourable.

#### Proof

In the second outcome, choose a mismatched pair `i,j`.  If their types
differ, choose any two further indices `k,l` and use (5.3).  If their types
agree, choose `k` of the opposite type and any fourth index `l`; unless an
opposite-type parallel pair already gives (5.3), use (5.4).  This produces
the same seven-bag model on `a,b,c,D_i,D_j,D_k,D_l` as before.

For every remaining index `r`, add the whole edge `D_r` as one new branch
set.  It meets every boundary singleton bag used by the seven-bag model,
meets every endpoint or union of endpoints in that model through the
selected perfect matchings, and meets every other added whole carrier.
The result is a `K_{7+(n-4)}=K_{n+3}` model.

In the flat outcome define `x_i,y_i` by (5.5).  The `x_i` induce `K_n`,
the `y_i` induce a second `K_n`, and the carrier edges form a matching
between corresponding vertices.  Give `x_i` colour `i` and `y_i` colour
`i+1 modulo n`; give `a,b` one new colour and `c` another.  This is a
proper `(n+2)`-colouring. \(\square\)

Algebraically, the selected carrier matchings form the signed double cover
of `K_n`.  Switching carrier `i` interchanges `p_i,q_i` and adds the
coboundary of that switch to every incident sign.  The flat condition says
that switching by the state word `t` separates the cover into two literal
`K_n` layers.  The local models (5.3)--(5.4) show that any sign which
cannot be removed by this state switch in the mixed-state branch is already
enough state-relative discrepancy to create the full clique minor.  A
homogeneous type word is retained as the coherent-state outcome and is not
covered by that discrepancy assertion.

### Theorem 5.3 (connected two-shore version)

The minor half of Theorem 5.2 does not require literal edge carriers.
For each `i`, let a carrier be split into two nonempty disjoint connected
shores `P_i,Q_i` which are adjacent.  Replace the row table (4.2) by

\[
\begin{array}{c|cc}
t_i&P_i&Q_i\\ \hline
0&a,b&b,c\\
1&a,c&b,c,
\end{array}                                            \tag{5.6}
\]

where an entry means at least one edge from the indicated shore to each
listed boundary vertex.  Between every carrier pair select either the
parallel contacts

\[
                    P_iP_j,\quad Q_iQ_j              \tag{5.7}
\]

or the crossed contacts

\[
                    P_iQ_j,\quad Q_iP_j,             \tag{5.8}
\]

and call their sign `s_ij=0` or `1` respectively.

For every `n>=4`, if the type word is mixed and
`s_ij != t_i xor t_j` somewhere, these connected shores contain a
`K_{n+3}` model.  If `s=delta t`, switching the two shores in every
type-one carrier produces two disjoint labelled `K_n` models

\[
              (X_1,\ldots,X_n),\qquad(Y_1,\ldots,Y_n), \tag{5.9}
\]

with `X_i` adjacent to `Y_i` for every `i`.

#### Proof

Replace every singleton `p_i,q_i` in (5.3)--(5.4) by the connected shore
`P_i,Q_i`.  Every union used there remains connected because its two
shores have one of the selected contacts; every asserted adjacency is
one of (5.6)--(5.8) or an internal carrier contact.  Whole remaining
carriers are connected and meet both shores of every selected carrier.
The proof of the `K_{n+3}` model is therefore unchanged.

In the flat branch put `(X_i,Y_i)=(P_i,Q_i)` for type zero and
`(Q_i,P_i)` for type one.  The identity `s=delta t` turns every selected
pair into `X_iX_j,Y_iY_j`, giving the two labelled clique models; the
internal carrier contact gives `X_iY_i`. \(\square\)

Theorem 5.3 is label-preserving and arbitrary-order.  It isolates the
exact geometric input still missing at Gate A: produce two connected
state shores in each indecomposable carrier.  Once such shores exist,
wrong state-relative transport is already the target minor and aligned
transport is one coherent two-layer architecture; no further portal
enumeration is needed.

## 6. From the cocycle skeleton to the full compatibility relation

The correct finite state is not the equality word `AB/AC`.  It is the
pair

\[
     (\text{repeated-state bit},\ \text{portal transport bit}). \tag{6.1}
\]

For the selected minimal skeleton, compatibility is exactly the edgewise
identity `s=delta t`, equivalently vanishing of the state-relative
discrepancy `s+delta t`.  Ordinary cycle holonomy alone is weaker.  A full
host may have additional intercarrier edges, and these cannot be deleted
when the conclusion sought is a colouring.

There is an exact completion test in the flat branch.  Switch by `t` and
retain the notation `x_i,y_i` from (5.5).  The selected skeleton contains
both `K_n` layers.  Form a bipartite graph `M_F` with left vertices
`1_L,...,n_L` (the colours used on the `x` layer) and right vertices
`1_R,...,n_R` (the vertices of the `y` layer), putting

\[
       i_Lj_R\in E(M_F)
       \quad\Longleftrightarrow\quad
       x_iy_j\notin E(F).                            \tag{6.2}
\]

Here `F` is the full edge-carrier host after the switch; in particular the
diagonal is absent from `M_F` because `x_jy_j` is a carrier edge.

### Proposition 6.1 (flat completion matching)

After fixing colour `i` on `x_i`, this `x`-layer assignment extends to
all intercarrier edges of `F` using the `n`-colour carrier palette if and
only if `M_F` has a perfect matching.  The colours on the `y` layer may
be any permutation supplied by that matching; this does not assert that
the particular cyclic permutation displayed in Theorem 5.2 itself
extends.

#### Proof

Fix colour `i` on `x_i`.  Since the `y` layer is a `K_n`, its use of the
same `n` colours is a permutation: assigning colour `i` to `y_j` is
proper across the two layers exactly when `x_iy_j` is not an edge.  Thus
the permitted assignments are precisely the edges of `M_F`, and a full
assignment is precisely a perfect matching. \(\square\)

The deletion-critical form of this relation has a uniform classification.

### Theorem 6.2 (maximal incompatible relations are rectangular)

Let `M` be a bipartite graph with equal parts `L,R` of order `n`.  Suppose
`M` has no perfect matching, but `M+e` has a perfect matching for every
nonedge `e` between `L` and `R`.  Then there are a nonempty
`S subseteq R` and a (possibly empty) `T subseteq L` with

\[
                  |T|=|S|-1                         \tag{6.3}
\]

such that

\[
 E(M)=(T\mathbin\times S)\ \cup\
      (L\mathbin\times(R-S)).                       \tag{6.4}
\]

Conversely every graph of the form (6.4) is edge-maximal without a perfect
matching.

#### Proof

By Hall's theorem choose nonempty `S subseteq R` with
`|N_M(S)|<|S|`, and put `T=N_M(S)`.  Since `|T|<|S|<=n`, both `S` and
`L-T` are nonempty.  Add any missing edge from `L-T` to `S`.  By
hypothesis the resulting graph has a perfect matching, so the old Hall
defect on `S` must disappear.  Only one new neighbour was added; hence
`|T|=|S|-1`.

Any missing edge inside `T x S` or between `L` and `R-S` would not
enlarge `N_M(S)`.  Adding it would leave the Hall defect unchanged,
contrary to maximality.  All those edges are therefore present.  By the
definition of `T`, no edge joins `L-T` to `S`, proving (6.4).

Conversely, add `uv` with `u in L-T` and `v in S`.  Match `v` to `u`,
match `S-{v}` bijectively to `T`, and match `R-S` bijectively to the
remaining vertices of `L-T`.  All these edges exist by (6.4), giving a
perfect matching. \(\square\)

Applied to Proposition 6.1, suppose every deletion of an actual
wrong-layer edge `x_i y_j` (including a carrier edge on the diagonal)
produces a canonical separated-palette gluing.  Then `M_F` is either
already gluable, or the entire obstruction is one rectangle

\[
                  (L-T)\mathbin\times S,
              \qquad |S|=|T|+1.                    \tag{6.5}
\]

of actual cross-layer contacts.  This is a uniform finite-boundary
criticality theorem for every `n`: arbitrary incompatible operation states
collapse to one rank-one Hall block.  It is stronger than enumerating
portal patterns.  In the literal edge-carrier relation every diagonal is
an actual contact, so Theorem 6.4 below shows that this rectangle is
already impossible for `n>=2`.  A rectangular residue remains relevant
only for an operation quotient which suppresses the diagonal constraints,
as isolated in Proposition 6.5.

There is a stronger target-free bound before deletion-criticality is used.

### Theorem 6.3 (co-rank at most one)

In the flat full host, let `M_F` be the cross-nonedge graph from (6.2) and
write `nu=nu(M_F)` for its maximum matching size.  Then the carrier core
on `X union Y` satisfies

\[
       \chi(F[X\cup Y])=\omega(F[X\cup Y])=2n-\nu.  \tag{6.6}
\]

If the full host has no `K_{n+3}` minor, then

\[
                         \nu\ge n-1.                \tag{6.7}
\]

Thus the full compatibility relation is either perfect, or has exactly
one unmatched state.  Co-rank two already gives the target minor.

#### Proof

A matching of order `nu` in `M_F` pairs `nu` cross-nonadjacent vertices,
which may share colours; colour every remaining core vertex separately.
This gives `2n-nu` colours.  By Konig's theorem, `M_F` has a vertex cover
of order `nu`.  Delete that cover from the `2n` carrier vertices.  No
cross nonedge remains, so the surviving vertices form a literal clique of
order `2n-nu`.  This proves (6.6).

The connected bag `{b,c}` is adjacent to every carrier vertex: in type
zero every shore vertex sees `b` or `c` according to (4.2), and the same
is true in type one.  If `nu<=n-2`, the clique just found has order at
least `n+2`; adjoining `{b,c}` gives a `K_{n+3}` model.  This proves
(6.7). \(\square\)

The same minor argument remains valid for the connected two-shore version
of Theorem 5.3: a vertex outside a minimum cover denotes a connected shore,
and the cross-nonedge definition says that all surviving shores are
pairwise adjacent.

If `nu=n`, Proposition 6.1 gives the `(n+2)`-colouring.  Hence a
target-free, noncolourable flat edge-carrier host has exactly `nu=n-1`.
Canonical colourings after deletion of the internal carrier edges would
already rule out that last co-rank-one case.

### Theorem 6.4 (diagonal canonical-deletion obstruction)

Let `n>=2`.  In a flat edge-carrier host, suppose that for every `i`,
deleting the internal carrier edge `x_i y_i` makes the separated-palette
gluing of Proposition 6.1 possible in the same switched frame.  Then
`M_F` has a perfect matching, and the host is `(n+2)`-colourable.  No
mixed-type assumption is needed.

#### Proof

Deleting `x_i y_i` adds the diagonal edge `i_L i_R` to `M_F`.  Suppose
that `M_F` has no perfect matching, and choose a nonempty Hall-deficient
set `S subseteq R`.  For `M_F+i_Li_R` to have a perfect matching, this
one new edge must repair the Hall defect on `S`.  Consequently

\[
                  i_R\in S\quad\hbox{and}\quad
                  i_L\notin N_{M_F}(S)              \tag{6.8}
\]

for every `i`.  Hence `S=R` and `N_{M_F}(S)` is empty.  Thus `M_F` has no
edges.  When `n>=2`, adding one diagonal edge to the empty bipartite graph
still cannot produce a perfect matching, a contradiction.  Proposition
6.1 now supplies the colouring. \(\square\)

Under the stronger hypothesis that deleting **every** actual cross-layer
edge gives canonical gluing, Theorem 6.2 gives the same contradiction in
rectangular language.  All carrier diagonals lie in the complement block
`(L-T) times S`; hence every index lies in both `L-T` and `S`.  This forces
`T` empty and `S=R`, while `|T|=|S|-1` forces `n=1`.

The word **canonical** remains essential.  Ordinary minor-criticality
only promises some `(n+2)`-colouring after deleting `x_i y_i`; it does not
prove that this colouring preserves the switched two-layer palette and
hence adds `i_Li_R` to the same relation `M_F`.  The exact remaining
operation problem is to normalize the proper-minor colouring for even a
strategically chosen carrier-edge deletion, or to turn its noncanonical
palette into a labelled rerouting.  Static portal enumeration cannot
supply this transition.

For later operation quotients in which the internal diagonals have been
suppressed from the relation, the mixed-type part of a rectangular
co-rank-one obstruction still has an exact closure.

### Proposition 6.5 (abstract mixed rectangular branch)

Let `X={x_1,...,x_n}` and `Y={y_1,...,y_n}` be two clique layers with the
switched boundary rows forced by Lemma 4.1, but do not assume here that
every diagonal `x_i y_i` is present.  Suppose the cross-nonedge graph has
the rectangular form (6.4), and the type word is mixed.  Then the
two-layer row host is `(n+2)`-colourable or contains a `K_{n+3}` minor.

#### Proof

A maximum matching of the rectangular graph may leave any prescribed
vertex of `L-T` and any prescribed vertex of `S` unmatched: match the
other `|S|-1` vertices of `S` to `T`, and match `R-S` to the remaining
vertices of `L-T`.

If `L-T` contains `x_i` of type zero, choose it unmatched.  Colour the
core from that maximum matching, let `c` share the singleton colour of
`x_i`, which misses `c`, and give `a,b` one fresh colour.  This is an
`(n+2)`-colouring.  Symmetrically, if `S` contains `y_j` of type one,
leave it unmatched, let `b` share its colour, and give `a,c` one fresh
colour.

It remains to consider

\[
       L-T\subseteq\{x_i:t_i=1\},\qquad
       S\subseteq\{y_i:t_i=0\}.                    \tag{6.9}
\]

Choose a type-zero index `r` and a type-one index `s`.  Then `x_r in T`
and `y_s in R-S`.  The set

\[
                         K=(L-T)\cup S              \tag{6.10}
\]

is a literal carrier clique of order `n+1`.  The bag
`Z={x_r,a,y_s}` is connected through `a` and is adjacent to every member
of `K`, using `x_r` for the `X` members and `y_s` for the `Y` members.
The connected bag `W={b,c}` is adjacent to every member of `K`, and it
meets `Z` through `x_r b` and `y_s c`.  The `n+1` singleton bags in `K`
together with `Z,W` form a `K_{n+3}` model. \(\square\)

This proposition is not needed in the literal edge-carrier setting of
Theorem 6.4: there all diagonals are present, and the rectangle is already
impossible for `n>=2`.  Its scope is an operation relation which has first
removed or quotiented those diagonal constraints.

If the matching exists, give `a,b` and `c` the two fresh colours as in
Theorem 5.2.  If it fails, Hall's theorem returns an exact set of carrier
states whose available colour set is too small.  This is the first
faithful full-host state: it is a relation, not one sign bit.

Hall failure alone still does not force a clique minor.  There is a sharp
eleven-vertex example.  Take `t=(0,0,0,1)`, the flat signs
`s_ij=t_i xor t_j`, and add

\[
                   x_0y_3,\quad x_1y_3,\quad x_2y_3. \tag{6.11}
\]

Together with the carrier edge `x_3y_3`, these forbid all four carrier
colours at `y_3`, so `M_F` has no perfect matching.  Exact branch-set
search nevertheless finds no `K_7` minor, and the graph has the explicit
five-colouring recorded in
`near_k7_two_vertex_state_helly_verify.py`.  Thus even a static full portal
relation needs the minor-critical operation transition: one must show
that a Hall-defect relation changes under a proper deletion/contraction,
or that its persistence creates a labelled rerouting.

This gives a concrete design requirement for the unbounded-carrier
theorem:

> associate to every proper-minor colour state a labelled two-terminal
> portal transport relation; prove that a nontrivial cycle of transports
> reroutes a branch set into a `K_7` model, while a flat family composes to
> a faithful six-colouring or a rural two-apex expansion.

The leaf expansion proves that the first coordinate alone cannot work.
Theorems 5.1--5.2 show that state-aligned transport completely decides the
selected minimal skeleton.  Proposition 6.1 identifies the exact extra
relation needed for the full edge-carrier host, while (6.11) proves that
static Hall failure is not enough.  Extending the operation-sensitive
relation from an edge to a `Q`-indecomposable partial-2-tree carrier is the
precise remaining state-exchange problem.
