# Atomic support motifs at an exact seven-adhesion

## 1. What equality really supplies

Let \(G\) be a hypothetical \(HC_7\) counterexample, put \(H=G-v\),
and suppose an atomic support motif gives an inclusion-minimal separator
\(Z\) of order six between two rooted support shores. Put

\[
                              S=Z\cup\{v\}.               \tag{1.1}
\]

The two reachable components \(R_1,R_2\) in \(H-Z\) satisfy

\[
                N_H(R_1)=Z=N_H(R_2).                     \tag{1.2}
\]

Each contains a support piece meeting \(N_G(v)\), so

\[
                N_G(R_1)=S=N_G(R_2).                     \tag{1.3}
\]

Thus \(S\) is a full seven-adhesion. Seven-connectivity also makes every
other component of \(G-S\) full.

There is no further automatic boundary adjacency. In particular,

\[
                 z\in Z\quad\not\Longrightarrow\quad zv\in E(G).
                                                               \tag{1.4}
\]

Minimality says that \(z\) has neighbours in both open shores, not that it
is itself a neighbourhood root of \(v\).

## 2. Why the atomic complement is not the boundary complement

The atomic graphs \(K_3,P_4,3K_2\) occur in the complement of a
seven-piece **support quotient**. An edge of that quotient records the
existence of at least one edge somewhere between two connected pieces.
After taking an internal separator \(Z\), that witnessing edge may lie:

* between two vertices of \(Z\);
* between \(Z\) and a leftover fragment of a support piece; or
* entirely outside \(Z\).

Conversely, two vertices of \(Z\) in support pieces which are adjacent in
the quotient need not be adjacent to one another. Hence the atomic
support motif neither bounds
\(|E(\overline{G[S]})|\) from above nor identifies the isomorphism type
of \(\overline{G[S]}\).

The order-seven full-shore theorems remain applicable to \(S\), but only
with their actual conclusions:

* all complements with at most five edges are closed;
* at six edges the sole surviving type is
  \(C_6\dot\cup K_1\);
* with three shores, block gluing constrains the chromatic type of
  \(G[S]\), but two shores need not accept a common equality state.

The atomic quotient alone does not move the boundary into one of the
already closed layers.

## 3. A seven-connected sharp counterarchitecture

The following graph realizes the exact \(K_3\) support motif while its
full seven-boundary is the sharp unresolved six-edge type.

Let

\[
 S=\{0,1,2,3,4,5,6\},\qquad v=0,
\]

and define

\[
       \overline{G[S]}=01\,12\,23\,34\,45\,50
                       \ \dot\cup\ \{6\};                \tag{3.1}
\]

that is, the missing boundary edges form the six-cycle
\(0\,1\,2\,3\,4\,5\,0\), while \(6\) is isolated in the complement.
Add four vertices \(a,b,c,d\), each adjacent to every vertex of \(S\).
Among these four vertices put only the edges

\[
                              ad,\qquad cd.               \tag{3.2}
\]

Then

\[
        G-S=R_A\dot\cup R_B,\qquad
        R_A=G[\{a,c,d\}],\quad R_B=\{b\},                 \tag{3.3}
\]

and both components are full to \(S\).

### Lemma 3.1

The graph \(G\) in (3.1)--(3.2) is exactly seven-connected.

#### Proof

Deleting all seven vertices of \(S\) separates \(R_A\) from \(R_B\), so
\(\kappa(G)\le7\). Delete at most six vertices. At least one boundary
vertex remains.

If an outside vertex remains, it is adjacent to every remaining boundary
vertex, and every other outside vertex is joined through any remaining
boundary vertex. Hence the remaining graph is connected. If all four
outside vertices were deleted, at most two boundary vertices were also
deleted. The graph \(G[S]=K_7-C_6\) remains connected after deletion of
at most two vertices: among at least five surviving vertices, a
disconnection would put at least three vertices on one side, making each
vertex on the other side have at least three nonneighbours, whereas every
vertex of \(K_7-C_6\) has at most two. Thus no cut of order at most six
exists.
\(\square\)

### Lemma 3.2

In \(H=G-v\), the following seven connected pieces have support graph
exactly \(K_7-K_3\):

\[
\begin{aligned}
 A&=\{a\},\qquad B=\{b\},\qquad C=\{c\},\\
 D_1&=\{2,5,d\},\qquad D_2=\{1,3\},\qquad
 D_3=\{4\},\qquad D_4=\{6\}.                             \tag{3.4}
\end{aligned}
\]

The missing triangle is \(A,B,C\), and every one of the seven pieces
meets \(N_G(v)\).

#### Proof

The vertices \(a,b,c\) are pairwise nonadjacent. Every one is adjacent
to every \(D_i\), because it is complete to \(S-\{v\}\); additionally
\(a,c\) see \(d\). The piece \(D_1\) is connected through \(d\), and
\(D_2\) is connected because \(13\in E(G[S])\).

The four \(D_i\)'s are pairwise adjacent. The piece \(D_1\) sees all
others through \(d\). Between the remaining pieces use

\[
          14,\qquad 16,\qquad 46;
\]

all are boundary edges under (3.1). Thus their support is \(K_4\),
proving the quotient claim.

Finally \(v=0\) is adjacent in \(G[S]\) to \(2,3,4,6\), and it is
adjacent to all four outside vertices. Hence
\(A,B,C,D_1,D_2,D_3,D_4\) are all contacted. \(\square\)

The seven-piece frame is exactly the simultaneous-split construction,
not just an abstract quotient. Before splitting, use the six old bags

\[
\begin{aligned}
 A^0&=\{a,1,3\},& B^0&=\{b,4\},&
 K_1&=\{2,d\},\\
 K_2&=\{c\},& K_3&=\{6\},& U&=\{5\}.                    \tag{3.5}
\end{aligned}
\]

They form a spanning \(K_6\)-model in \(H\). The first five are
contacted and \(U\) is not, since \(05\notin E(G)\). Split
\(A^0\) as \(\{a\}\dot\cup\{1,3\}\), split \(B^0\) as
\(\{b\}\dot\cup\{4\}\), and assign \(U\) to \(K_1\). This gives
precisely (3.4).

Put

\[
                              Z=\{1,2,3,4,5,6\}.          \tag{3.6}
\]

In \(H-Z\), the component containing \(A,C,D_1-Z\) is
\(\{a,c,d\}=R_A\), while \(B=\{b\}=R_B\). Every \(z\in Z\) is adjacent
to both components. Hence \(Z\) is an inclusion-minimal six-separator
and (1.2)--(1.3) hold. Notice explicitly that

\[
                         v1,v5\notin E(G),                \tag{3.7}
\]

so the invalid inference in (1.4) fails twice.

The boundary complement in (3.1) is exactly
\(C_6\dot\cup K_1\), the sole six-edge type not eliminated by
*hadwiger_contact_order7_threeedge_closure.md*. Thus even
seven-connectivity, a full exact adhesion, contact of all seven support
pieces, and the exact atomic \(K_3\) quotient do not force a previously
closed boundary-complement type.

For audit purposes, this graph is not an \(HC_7\) counterexample. It is
six-colourable and it has the explicit \(K_7\)-model

\[
       \{0\},\quad\{2\},\quad\{4\},\quad\{6\},\quad
       \{a\},\quad\{d\},\quad\{1,b\}.                     \tag{3.8}
\]

One six-colouring uses the four boundary classes
\(\{0,1\},\{2,3\},\{4,5\},\{6\}\) and the two outside classes
\(\{a,b,c\},\{d\}\).

The point of the example is logical independence: the \(K_7\)-model in
(3.8) uses the internal placement of the \(d\)-portals. Treating
\(R_A,R_B\) only as two black-box full shores leaves precisely the
\(C_6\dot\cup K_1\) boundary residue.

The example does **not** satisfy contact maximality: deleting the
singleton bag \(\{0\}\) from (3.8) leaves an \(N_G(v)\)-meeting
\(K_6\)-model in \(H\). Thus it does not refute a theorem which combines
the full-shore geometry with contact maximality or all-operation state
novelty. It shows exactly that the three full-shore inputs, by
themselves, cannot supply that missing theorem.

## 4. The limited positive consequence

The existing machinery does give a clean conditional closure.

### Proposition 4.1

At an equality adhesion (1.1), if
\(|E(\overline{G[S]})|\le5\), then the cell is impossible in a
hypothetical counterexample: the existing closure gives either a
\(K_7\)-minor or a six-colouring.  For at most four missing edges the
two full shores already give the \(K_7\)-minor directly.  If there are
three components of \(G-S\) and the boundary complement is
\(C_6\dot\cup K_1\), then a \(K_7\)-minor also exists.

#### Proof

The first assertion is Theorem 13.1 of
*hadwiger_contact_order7_threeedge_closure.md*.  Its two exceptional
five-edge web cores must not be described as black-box two-shore minor
packings: in the crossless outcome their closure is a six-colouring.
For the second assertion, label
the complementary cycle \(0\,1\,2\,3\,4\,5\,0\) and let \(6\) be the
universal boundary vertex. For three full shores \(R_1,R_2,R_3\), use

\[
 \{0\},\quad\{2\},\quad\{4\},\quad\{6\},\quad
 R_1,\quad R_2\cup\{1\},\quad R_3\cup\{3\}.              \tag{4.1}
\]

The four singletons form a clique. Fullness supplies every remaining
adjacency, including those between shore bags through the displayed
anchors. \(\square\)

Therefore an atomic equality cell which survives the existing
full-shore theory must have exactly two shores when its boundary has six
missing edges, and that boundary must be \(C_6\dot\cup K_1\); or it must
have at least seven missing boundary edges. This is useful, but it is
not a closure of an atomic motif.

## 5. Operation states

The full-shore block-gluing theorem constructs a common state only from
a suitable proper colouring of \(G[S]\) and enough *other* full shores
to realize its colour blocks. In the two-shore atomic equality cell,
those hypotheses need not hold.

Likewise, *hadwiger_exact7_kempe_trace_exchange.md* says that a failed
common repair produces an alternating chain of actual Kempe regions,
with clean connectors or named dirty hits. It does not assert that two
arbitrary full shores accept a common equality state. The
\(C_6\dot\cup K_1\) architecture above therefore reaches exactly the
known operation-state residue: one must exploit internal portal placement
inside a shore, as (3.8) does, or synchronize the alternating dirty-hit
chains. Neither conclusion follows from the atomic support graph and
fullness alone.

## 6. Outcome

The comparison produces an honest negative answer to the proposed
boundary-classification shortcut:

\[
\boxed{\text{atomic support motif + exact full seven-adhesion}
\not\Rightarrow
\text{an already closed boundary type}.}
\]

The strongest immediate positive statement is Proposition 4.1. The
remaining dynamic target is internal: use the multiply hit named support
piece to split the \(C_6\dot\cup K_1\) two-shore cell, or use two faithful
operations to force one of the clean/dirty Kempe-chain exchanges. Any
argument which assigns \(vz\) for all \(z\in Z\) is invalid.

Whether contact maximality forces a common operation state in this sharp
cell remains open. The displayed six-colourable architecture cannot
answer that question—it has a global common state—and is not presented
as doing so.
