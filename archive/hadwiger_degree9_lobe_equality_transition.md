# The unique-owner equality: exact traces, portal-edge transitions, and a parity barrier

## 1. The operation-level state forced at the lobe cut

Let \(G\) be a minor-minimal non-six-colourable graph and let \(S\) be
an exact seven-cut. Write the components of \(G-S\) as
\(C_1,\ldots,C_m\). Seven-connectivity makes every \(C_i\) full to
\(S\).

For a piece \(C_i\), let \(\mathcal E_i\) be the equality partitions of
\(S\) induced by six-colourings of \(G[S\cup C_i]\). A partition is
always required to have at most six nonempty independent blocks.

### Lemma 1.1 (every independent trace occurs on the other side)

For every nonempty independent set \(B\subseteq S\) and every \(i\),
there is a state

\[
 \Pi_{i,B}\in\bigcap_{j\ne i}\mathcal E_j-\mathcal E_i.             \tag{1.1}
\]

in which \(B\) is an exact block. Moreover

\[
                         q(\Pi_{i,B})\le 8-|B|.                      \tag{1.2}
\]

#### Proof

The connected set \(C_i\cup B\) may be contracted to one vertex \(z\).
It creates no loop because \(B\) is independent. Fullness makes \(z\)
adjacent to every vertex of \(S-B\). Colour the resulting proper minor
with six colours and expand only the boundary labels. The vertices of
\(B\) receive the colour of \(z\), and no vertex of \(S-B\) does, so
\(B\) is an exact block. The other \(7-|B|\) boundary vertices give
(1.2).

The colouring restricts to every unchanged piece \(j\ne i\). If the
same state extended to \(C_i\), align block colours and glue, producing
a six-colouring of \(G\). Hence it is rejected by \(C_i\). \(\square\)

This is stronger than saying that both sides are trace-complete: the
trace witnessing a contraction of one shore is accepted simultaneously
by all the other shores and rejected by the contracted shore.

### Lemma 1.2 (one-step transition at an arbitrary exact cut)

For every deletion of an interior vertex, and every deletion or
label-preserving contraction of an edge having at least one interior
end in \(C_i\), there is a state

\[
 \Pi_\mu\in
 (\mathcal E_i^\mu-\mathcal E_i)
 \cap\bigcap_{j\ne i}\mathcal E_j.                            \tag{1.3}
\]

#### Proof

Colour the proper minor \(G^\mu\), restrict to \(S\), and argue exactly
as in Lemma 1.1. If the state extended to the unoperated \(C_i\), it
would glue to a colouring of \(G\). \(\square\)

No neighbourhood-colour parameter is needed here: the vertex \(v\) lies
in one of the actual pieces and is already coloured in the proper minor.

## 2. What a portal-edge operation additionally forces

The transition in Lemma 1.2 is not an arbitrary state.

### Lemma 2.1 (portal-edge equality and unique contact)

Let \(u\in C_i\), \(x\in S\), and \(ux\in E(G)\). In every
six-colouring \(c\) of \(G-ux\),

\[
                             c(u)=c(x).                       \tag{2.1}
\]

If \(P_x\) is the block of the induced state containing \(x\), then

\[
                     P_x\cap N_S(u)=\{x\}.                    \tag{2.2}
\]

Every one of the other five colours occurs in \(N_G(u)-\{x\}\).
The same boundary state colours the label-preserving contraction
\(G/ux\).

#### Proof

If \(c(u)\ne c(x)\), restoring \(ux\) colours \(G\), proving (2.1).
Every other boundary neighbour of \(u\) must consequently avoid that
colour, giving (2.2). If another colour were absent from
\(N_G(u)-\{x\}\), recolour \(u\) with it and restore \(ux\). Finally,
after deleting \(ux\), its two ends have the same colour; identifying
them therefore preserves properness and gives a colouring of the
contraction. \(\square\)

Thus a portal-edge deletion witness contains both an exact equality and
a five-colour fan at its interior endpoint. Any positive equality-cut
argument must use the placement of that fan; the block condition alone
is not enough, as Section 4 shows.

## 3. Two general positive consequences

### Lemma 3.1 (trace--palette obstruction)

If \(C_i\) is \(k\)-colourable, then

\[
                              \alpha(G[S])\le k+1.            \tag{3.1}
\]

#### Proof

If \(B\subseteq S\) were independent with \(|B|\ge k+2\), Lemma 1.1
would give a state on the other pieces using at most
\(8-|B|\le6-k\) colours on \(S\). Colour \(C_i\) with \(k\) of the
remaining colours. Since its palette is disjoint from the boundary
palette, every edge from \(C_i\) to \(S\) is proper. This glues to a
six-colouring of \(G\), a contradiction. \(\square\)

### Lemma 3.2 (ordered-boundary palette split)

In the unique-owner equality of
hadwiger_degree9_unique_owner_lobe_boundary.md, put \(i=|I(U)|\).
Under the ordered-spine hypothesis, \(G[A(U)]\) is a subgraph of a
path. Consequently

\[
                         \chi(G[S])\le 3+i.                   \tag{3.2}
\]

If every component of \(G-S\) is \((3-i)\)-colourable, then \(G\) is
six-colourable.

#### Proof

Three ordered portal cutvertices \(a<b<c\) cannot have the edge \(ac\):
that edge, together with paths from the ordinary root to \(a\) and from
\(c\) to the far residue, would bypass the separator \(b\). Hence
edges among ordered portals occur only between consecutive portals, and
\(A(U)\) is bipartite.

Use two colours on \(A(U)\), and give each of \(r\) and the \(i\)
vertices of \(I(U)\) its own new colour. This proves (3.2), regardless
of the cross-edges. Colour every component of \(G-S\) with the
remaining \(3-i\) colours; components are pairwise anticomplete.
\(\square\)

Thus an equality obstruction has a genuinely high-chromatic shore:
at least one component has chromatic number at least \(4-i\). This
eliminates an infinite family, rather than only bounded-order shores.

## 4. A boundary compatible with every local portal-edge condition

The preceding operation facts still do not force a common state at the
abstract boundary level. Consider the admissible unique-owner boundary

\[
 S=\{r,a_1,\ldots,a_6\},                                    \tag{4.1}
\]

where \(a_1a_2\cdots a_6\) is a path and \(r\) is adjacent to
\(a_2,\ldots,a_6\), but not to \(a_1\). This is the exact
\(|I(U)|=0\) lobe boundary: the six \(a_j\) lie in the ordered ordinary
bag, and the \(r a_1\) edge is not forced.

Let \(\mathcal P\) be the proper partitions of \(S\) into at most six
blocks, and put

\[
\begin{aligned}
 \mathcal P_{\rm ev}&=\{\Pi\in\mathcal P:q(\Pi)\text{ is even}\},\\
 \mathcal P_{\rm odd}&=\{\Pi\in\mathcal P:q(\Pi)\text{ is odd}\}.
\end{aligned}                                               \tag{4.2}
\]

### Theorem 4.1 (parity survives traces and portal uniqueness)

The two families in (4.2) are disjoint and each contains an exact trace
for every nonempty independent \(B\subseteq S\). In addition, for every
\(x\in S\), each family contains a state in which \(\{x\}\) is a
block; one can choose the odd state with five blocks and the even state
with six blocks.

Consequently, for every possible portal neighbourhood
\(T\subseteq S\) and every \(x\in T\), both parity families contain a
state satisfying

\[
                       P_x\cap T=\{x\},                      \tag{4.3}
\]

the exact boundary restriction forced by Lemma 2.1.

#### Proof

The boundary has independence number three. If \(|B|=2\), the state
consisting of \(B\) and five singletons has six blocks; among the five
vertices outside \(B\) there is a nonedge, whose merger gives five
blocks. If \(|B|=3\), start with \(B\) and four singletons and merge a
nonedge outside \(B\), giving five and four blocks.

For \(B=\{x\}\), there are two vertex-disjoint nonedges avoiding \(x\).
Starting with seven singleton blocks, merge one and then the other,
giving six and five blocks while keeping \(x\) singleton. The explicit
witnesses for all seven choices of \(x\) are generated by
degree9_lobe_equality_parity_probe.py. A singleton block satisfies
(4.3) for every \(T\). \(\square\)

The verifier enumerates all 877 set partitions. For this boundary it
finds 66 proper states and 22 nonempty independent traces; every trace
occurs in both parities, and every portal label has the claimed
five-/six-block witnesses.

The five-block witness supplied by a portal-edge deletion on one side is
therefore not automatically common: it can lie in the opposite parity
family while being rejected by the operated side before the deletion.
Likewise, (2.2) does not by itself provide a rooted split.

## 5. Realization and the precise trust boundary

The state obstruction has two graph-level realizations, but one joint
property remains unproved.

1. The Dvořák--Swart realization theorem gives finite six-colouring
   realizers for each family in (4.2). The standard harmless
   two-edge-path augmentation connects the open interior and makes it
   full to \(S\) without changing the extension relation. Gluing the
   two open interiors along \(S\) gives two full connected shores with
   no common six-colour state.
2. Starting with any parity realizer, repeatedly delete an interior
   vertex or a nonboundary edge whenever the exact extension relation
   is unchanged. In the resulting deletion-minimal realizer, every
   such deletion adds an opposite-parity state. For an edge deletion,
   its ends have the same colour in every new extension, so the same
   state also extends after contraction. This includes
   boundary--interior portal edges while retaining the boundary label.
   Pairing the even and odd minimal realizers therefore satisfies every
   one-step transition in Lemmas 1.2 and 2.1.

The second construction is full as a boundaried graph. Indeed, for
every \(x\in S\) there are proper even and odd boundary colourings which
agree on \(S-\{x\}\). If \(x\) had no interior neighbour, an extension
of the accepted one would also extend the rejected one.

What is **not** proved is that deletion minimization preserves
connectedness of the open interior. Conversely, the harmless paths in
the first construction are deliberately redundant and fail the
one-step transition condition. Thus no claim is made here of a single
two-shore graph which is simultaneously

* open-connected and full on each side;
* transition-minimal for every internal and portal edge;
* seven-connected; and
* \(K_7\)-minor-free.

This is exactly the joint geometric package still available to a
positive \(HC_7\) argument. Any invocation of a theorem realizing that
joint package would be an unproved step.

## 6. Small-shore check

For the cone-over-\(P_6\) variant of (4.1), the script
degree9_lobe_equality_transition_search.py independently enumerates
all connected full shores on at most two interior vertices, including
all label-preserving vertex, internal-edge, and portal-edge operations.
There are 51 proper boundary states and 119 individually
operation-critical piece signatures. No two pieces even have disjoint
original extension families, so no transition counterarchitecture of
that order exists.

This finite statement also follows from Lemma 3.2: every one- or
two-vertex connected interior is three-colourable, and the boundary is
three-colourable, so disjoint three-colour palettes give a common state.

## 7. Exact remaining equality gap

The equality branch is now pinned between two rigorous facts.

* Genuine minor-criticality gives exact independent traces, endpoint
  equality, unique portal-block contact, and a five-colour fan for every
  deleted portal edge.
* All those **state-level** restrictions admit the parity separation
  (4.2); even actual one-step-minimal realizers exist, but their open
  interiors are not yet known to remain connected.

Therefore the next valid theorem must use the geometry of the five-colour
fan. It must show that, in a connected full shore, the Kempe paths from
the deleted portal endpoint either form the required label-preserving
rooted split/\(K_7\)-model, or synchronize two portal-edge witnesses to
one boundary state accepted by both shores. Abstract equality blocks,
including a common five-block *shape*, are insufficient.
