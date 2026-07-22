# Eliminating concentrated reserve demands at degrees eight and nine

**Status:** written proof; [separate internal audit **GREEN**](hc7_low_degree_concentrated_reserve_elimination_audit.md).
This result eliminates the concentrated exclusive-reserve alternative in
both low-degree tight atomic cases.  It does not by itself prove `HC_7`.

## 1. Opposite responses for two independent boundary blocks

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le6\quad\text{for every proper minor }M\text{ of }G.   \tag{1.1}
\]

Let `u` have degree `d in {8,9}`, put `S=N_G(u)`, and suppose that
`G-N_G[u]` has exactly two nonempty components `E,F`, with

\[
                         N_G(E)=N_G(F)=S.                         \tag{1.2}
\]

Suppose

\[
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\},
 \qquad |I|=d-5,
 \qquad |T|=3,                                                   \tag{1.3}
\]

where `I,T` are independent.  For `P in {E,F}`, let
`mathcal R_P` be the set of equality types of `p,q` in proper
six-colourings of `G[P union S]` in which `I,T` are distinct exact
boundary colour classes.

### Lemma 1.1 (opposite pair responses)

Both response sets are nonempty, `pq` is a nonedge, and

\[
             \{\mathcal R_E,\mathcal R_F\}
                    =\bigl\{\{=\},\{\ne\}\bigr\}.              \tag{1.4}
\]

### Proof

Fix `P in {E,F}` and let `P'` be the other component.  The two sets

\[
                    \{u\}\cup I,
             \qquad P'\cup T                                    \tag{1.5}
\]

are disjoint and connected.  Contract a spanning tree in each and
six-colour the resulting proper minor.  Retain the colouring on
`P union {p,q}`, discard the contracted copies of `u,P'`, and expand the
two contraction colours over `I,T`, respectively.

This is proper because `I,T` are independent and every retained edge
incident with either block was represented at its contraction image.  The
two images are adjacent through an edge from `u` to `T`.  Each of `p,q`
is adjacent to the first image through `u` and to the second through the
fullness of `P'`.  Hence `I,T` are distinct exact boundary colour classes,
while `p,q` avoid both colours.  Thus `mathcal R_P` is nonempty.

If the two shores admitted the same equality type, choose one response of
that type on each shore.  Their complete boundary partitions agree after
a permutation of colour names, so the colourings glue to a six-colouring
of `G-u`.  Only three or four colours occur on `S`; an absent colour may be
assigned to `u`, contradicting (1.1).  The two nonempty response sets are
therefore disjoint subsets of \(\{=,\ne\}\), proving (1.4).  If `pq` were
an edge, both sets would equal \(\{\ne\}\), the same contradiction.
\(\square\)

## 2. A chosen connector and triple carrier force both responses

Retain the setup of Section 1 and assume additionally that

\[
                         \alpha(G[S])\le d-5.                    \tag{2.1}
\]

Suppose each of `p,q` has a neighbour in `T`, and that `E` contains

1. a `p`--`q` path `Q` whose open interior lies in `E`; and
2. a set `K subseteq E-V(Q)` such that `G[T union K]` is connected and
   contains an edge.

Thus `K` is a boundary-block carrier for `T` in the terminology of the
audited
[root-connector reflection theorem](hc7_order8_root_connector_reflection.md).

### Theorem 2.1 (dual response from one connector/carrier pair)

No graph satisfies these hypotheses.

### Proof

Lemma 1.1 gives `pq notin E(G)` and supplies an exact `I,T` response on
the closed `E`-shore.  We construct both possible responses on the closed
`F`-shore.

For the merged response, simultaneously contract spanning trees of the
three pairwise disjoint connected sets

\[
             \{u\}\cup I,
             \qquad T\cup K,
             \qquad V(Q).                                       \tag{2.2}
\]

Each set contains an edge, so the result is a proper minor.  The three
contraction images form a triangle.  The first is adjacent to the other
two through edges from `u`, and the second is adjacent to the third through
a `p`--`T` edge.  Six-colour the minor, retain its colouring on `F`, and
expand the three image colours only over `I,T,{p,q}`, respectively.  The
three independent blocks receive distinct colours, and every retained
incident edge was represented in the minor.  Hence `G[F union S]` realizes

\[
                              I\mid T\mid\{p,q\}.                 \tag{2.3}
\]

For the split response, apply the root-connector reflection theorem with

\[
       L=F,
       \qquad S=N_G(u),
       \qquad R'=E\cup\{u\},                                    \tag{2.4}
\]

with roots `p,q`, independent blocks `I,T`, root connector equal to the
open interior of `Q`, and carriers `{u}` for `I` and `K` for `T`.  The two
open sets in (2.4) are nonempty and anticomplete.  The connector is
nonempty because `pq` is a nonedge, and its interior is disjoint from the
two carriers.

The remaining boundary hypotheses follow from (2.1) and the assumed root
contacts.  There is an `I`--`T` edge, since otherwise `I` together with
one member of `T` would be an independent set of order `d-4`.  Each root
has a neighbour in `I`, since otherwise that root together with `I` would
have the same forbidden order.  Each root has a neighbour in `T` by
hypothesis.  Reflection therefore gives a proper six-colouring of
`G[F union S]` with exact partition

\[
                       I\mid T\mid\{p\}\mid\{q\}.                \tag{2.5}
\]

Choose (2.3) or (2.5) to match the `E`-shore response from Lemma 1.1.
After a permutation of colour names the two colourings agree on `S` and
glue to a proper six-colouring of `G-u`.  Again an absent boundary colour
may be assigned to `u`, contradicting (1.1). \(\square\)

## 3. Sparse reserve classification

Retain the degree-eight or degree-nine tight atomic setup of the audited
[concentrated exclusive-reserve response theorem](hc7_common_root_exclusive_reserve_response.md).
Thus a fixed proper six-colouring `c` of `G-u` has an independent boundary
colour class `I` of order `d-5` and five rainbow reserve vertices

\[
                         R=S-I.                                  \tag{3.1}
\]

Let `D` be the set of reserve nonedges whose fixed-colouring bichromatic
path has open interior in `E` but not in `F`, let

\[
 q=\binom52-|E(G[R])|,
 \qquad
 N=\bigl(\tbinom R2-E(G[R])\bigr)-D,                             \tag{3.2}
\]

and suppose `|D|>=7`.  The audited input gives

\[
 q\le8\quad(d=8),
 \qquad q\le9\quad(d=9),
 \qquad |N|=q-|D|.                                               \tag{3.3}
\]

### Lemma 3.1 (only two sparse reserve graphs survive)

The case `q=9` is impossible.  If `q=8`, then

\[
                         G[R]\cong2K_2\mathbin{\dot\cup}K_1.     \tag{3.4}
\]

If `q=7`, then

\[
                         G[R]\cong P_3\mathbin{\dot\cup}K_2.     \tag{3.5}
\]

### Proof

Whenever an edge `pq` of `G[R]` has an independent three-vertex complement
`T=R-{p,q}`, Lemma 1.1 applied to `I,T,p,q` says that `pq` must instead be
a nonedge.  Thus no such edge can occur.

If `q=9`, the reserve graph is one edge plus three isolated vertices, and
that edge has an independent triple as its complement.  This is impossible.

If `q=8`, the reserve graph has two edges.  If they share a vertex, either
edge at an end of the resulting `P_3` has an independent three-vertex
complement.  Hence the two edges are disjoint, proving (3.4).

If `q=7`, the reserve graph has three edges.  Up to isomorphism it is one
of

\[
 K_3\mathbin{\dot\cup}2K_1,
 \quad K_{1,3}\mathbin{\dot\cup}K_1,
 \quad P_4\mathbin{\dot\cup}K_1,
 \quad P_3\mathbin{\dot\cup}K_2.                                \tag{3.6}
\]

In the first three graphs, respectively any triangle edge, any star edge,
or the middle path edge has an independent three-vertex complement.  They
are impossible, leaving (3.5). \(\square\)

## 4. Elimination of every low-degree concentration

### Theorem 4.1

The concentrated setup of Section 3 is impossible for both `d=8` and
`d=9`.

### Proof

Lemma 3.1 removes `q=9`.  There are two remaining cases.

**Case `q=7`.**  Name the three edges of (3.5) `ab,bc,de`, and put

\[
                         T=\{a,c,d\},
             \qquad    \{p,q\}=\{b,e\}.                         \tag{4.1}
\]

The triple `T` is independent, `pq` is a nonedge, and each root has a
neighbour in `T`.  All seven reserve nonedges belong to `D`.  Choose the
fixed-colouring `E`-interior paths for `ac,ad,be`.  The open interior of
the `be` path is the root connector.  The union of the open interiors of
the `ac` and `ad` paths is a carrier for `T`.  It is disjoint from the
connector because the two constructions use disjoint sets of colours in
the fixed colouring.  Theorem 2.1 gives a contradiction.

**Case `q=8`.**  Write the two reserve edges in (3.4) as
`a_0a_1,b_0b_1`, and let `e` be the isolated vertex.  For each
`i,j in {0,1}`, the set

\[
             T_{ij}=\{a_i,b_j,e\}                                \tag{4.2}
\]

is independent, and its complementary pair is the cross nonedge
`a_{1-i}b_{1-j}`.  The four choices give four distinct complementary
pairs.  Here `|N|<=1`, so choose `i,j` such that this complementary pair
belongs to `D`; call it `{p,q}` and put `T=T_{ij}`.  Each root is adjacent
to its matching-edge mate in `T`.

All three pairs within `T` are reserve nonedges.  At most one belongs to
`N`, so two members of `D` span a tree on `T`.  Choose the fixed-colouring
`E`-interior path for `pq` and the two paths for that spanning tree.  The
first supplies the root connector and the union of the latter two open
interiors supplies a carrier for `T`.  Their fixed-colouring colour sets
are disjoint, so Theorem 2.1 again gives a contradiction. \(\square\)

### Corollary 4.2 (universal rooted `K_5` in both tight atomic cases)

In either tight atomic outcome of the audited low-degree common-root
classification, `G-u` contains an `R`-rooted `K_5`-minor model.

### Proof

The audited
[five-reserve Kempe-packet theorem](hc7_common_root_five_reserve_kempe_packet.md),
Corollary 3.2, gives either such a rooted model or at least seven reserve
nonedges exclusive to one shore.  Relabel the shores if necessary.  The
latter alternative is exactly the setup eliminated by Theorem 4.1.
\(\square\)

## 5. Exact trust boundary

The proof uses one fixed colouring only to select a root connector and a
disjoint carrier for an independent triple.  Proper-minor colourings first
force opposite responses for two independent boundary blocks.  A
three-block contraction and root-connector reflection then force both pair
responses on the other shore, so one complete boundary partition glues.

No direct `K_7`-minor model or seventh branch set is constructed.  The
conclusion eliminates all degree-eight and degree-nine concentrated
exclusive-reserve cases and forces an `R`-rooted `K_5` in both tight atomic
cases.  That rooted model may use both exterior components.  The theorem
does not make it shore-confined, reserve an `I`-connected seventh branch
set, or prove `HC_7`.

## Inputs

- [five-reserve Kempe packet](hc7_common_root_five_reserve_kempe_packet.md)
- [concentrated exclusive-reserve responses](hc7_common_root_exclusive_reserve_response.md)
- [root-connector reflection](hc7_order8_root_connector_reflection.md)
