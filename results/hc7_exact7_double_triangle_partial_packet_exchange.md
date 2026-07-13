# Double-triangle partial-packet exchange in the exact `(1,2)` cell

**Status:** proved and independently audited.  This is a partial closure
package for exact `(1,2)` adhesions; it does not close the whole cell.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

be an actual separation in a 7-connected, strongly
7-contraction-critical, `K_7`-minor-free graph.  The exact packet maxima
are

\[
                              (\nu_L,\nu_R)=(1,2).
\]

Thus the thin shore `L` contains one but not two disjoint `S`-full
packets, while the rich shore `R` contains two but not three.  In
particular, seven-connectivity makes every open-shore component `S`-full,
so `G[L]` is connected and `G[R]` has at most two components.  Suppose

\[
                    S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{z\},
                    \qquad H[A]\cong H[B]\cong K_3,       \tag{1.1}
\]

where `H=G[S]`.

The results below do two things:

1. close every near-full thin-shore split except one exact crossed-pure
   pattern; and
2. identify the exact proper-minor state transfer that repairs that
   pattern when one additional partial carrier exists on the rich shore.

They apply whether the rich shore is connected or has two components.

## 2. Exact demand-three normalization

### Lemma 2.1

For each of the ten absolute-demand-three boundary orbits in the audited
adaptive `(1,2)` residue, there is an independent set `I` such that every
proper equality partition `Pi` containing `I` as an exact block satisfies

\[
                              d_H(\Pi)=3.                 \tag{2.1}
\]

#### Proof

In the nine orbits with `alpha(H)=3`, take a maximum independent triple
`I`.  The four-vertex graph `H-I` is nonsplit, so it is `2K_2` or `C_4`.
The split-remainder criterion gives minimum demand three, while

\[
  \max d_H(\Pi)=1+|S-I|-\omega(H-I)=1+4-2=3.
\]

For the Moser spindle in the standard labeling

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]

take `I={0,5}`.  The remainder contains the triangle `126` and the
disjoint edge `34`, so it is nonsplit and has clique number three.  Again
the minimum demand is three and

\[
                     \max d_H(\Pi)=1+5-3=3.
\]

Thus (2.1) holds in every case. `square`

Contracting the thin full packet together with this `I` therefore returns
an exact boundary state of demand **exactly** three.  The remaining problem
is not to lower an unknown demand: it is to fund precisely one more block
than the two rich full packets can fund.

## 3. The adaptive one-extra-carrier theorem

Let `Pi` be the equality partition returned by the thin-packet contraction.
Choose a maximum clique `C` among its singleton blocks.  Since
`d_H(Pi)=3`, exactly three blocks of `Pi` are not represented by the literal
singletons in `C`; call them `B_1,B_2,B_3`.

### Theorem 3.1 (one partial carrier closes)

Let `P_1,P_2` be disjoint `S`-full packets in `R`.  Suppose, after permuting
`B_1,B_2,B_3`, that `R-(P_1 union P_2)` contains a connected subgraph `T`
such that

1. `T` contacts every literal vertex of `B_3`; and
2. for every `c in C`, either `T` contacts `c` or `c` has a neighbour in
   `B_3`.

Then `G` is six-colourable.

#### Proof

In the rich closed shore contract the three disjoint connected sets

\[
             P_1\cup B_1,\qquad P_2\cup B_2,\qquad T\cup B_3.             \tag{3.1}
\]

The first two representatives are adjacent because `P_1` contacts every
vertex of `B_2`.  Each is adjacent to the third because the corresponding
full packet contacts every vertex of `B_3`.  The first two representatives
are adjacent to every `c in C` by fullness, and the third is adjacent to
`c` by hypothesis 2.  Together with the literal clique `C`, the three
representatives therefore form a clique indexed exactly by the blocks of
`Pi`.

The contraction is proper and every proper minor is six-colourable.
Restrict a six-colouring of this minor to the untouched thin closed shore
and expand only the independent literal blocks `B_i`.  The representative
clique makes the induced equality partition on `S` exactly `Pi`.  This
matches the state originally returned on the rich closed shore.  A palette
permutation aligns the two colourings on every literal boundary vertex,
and they glue because there is no `LR` edge. `square`

### Rich-shore interpretation

* If `R` is connected, the extra carrier may lie in a connector outside
  two selected full packets, or be peeled from one packet while the
  remainder still carries one of the other returned blocks.
* If `R` has two components, each component is `S`-full and there are
  exactly two of them.  The third carrier must be split from one component;
  there is no intercomponent connector.

This is an actual distinction in the geometry, but not in the state
transfer: Theorem 3.1 is the common endgame in both cases.  The carrier is
chosen **after** `Pi` is returned, so no palette colour is identified with
a pre-existing packet label.

## 4. Four carriers from a near-full thin split

For a connected set `X` in an open shore put

\[
                              D(X)=S-N_S(X).
\]

Call a vertex `a in A` **`A`-pure** when it has no boundary neighbour
outside `A`; define `B`-pure symmetrically.

### Lemma 4.1 (triangle-transversal obstruction)

Let `H=G[S]`, without assuming the double-triangle decomposition (1.1).
Suppose the thin shore contains disjoint nonempty connected sets `X,Y`
with an `XY` edge and `|D(X)|,|D(Y)|<=1`.  If `G` has no `K_7` minor,
then

\[
                         D(X)\cup D(Y)
\]

meets every triangle of `H`.

#### Proof

Otherwise let `T` be a boundary triangle disjoint from
`D(X) union D(Y)`.  Since

\[
 |N_S(X)\cap N_S(Y)|\ge5,
\]

there are distinct vertices
`r_1,r_2 in S-(T union D(X) union D(Y))`.  Let `P_1,P_2` be the two
disjoint rich `S`-full packets.  The seven sets

\[
 P_1\cup\{r_1\},\quad P_2\cup\{r_2\},\quad X,\quad Y,
 \quad\{t\}\quad(t\in T)
\]

are connected, disjoint and pairwise adjacent.  Packet fullness supplies
all packet-to-boundary incidences.  The two anchors join each packet bag
to both thin carriers and join the packet bags to one another.  The given
`XY` edge joins the carriers, while `T` is a triangle contacted by both.
This is a literal `K_7` model, a contradiction. `square`

Thus the first obstruction is label-free: the two defects of adjacent
near-full carriers must form a transversal of all boundary triangles.

### Theorem 4.2 (crossed-pure funnel)

Suppose the thin shore contains disjoint nonempty connected sets `X,Y`
with an `XY` edge and

\[
                              |D(X)|,|D(Y)|\le1.           \tag{4.1}
\]

Then `G` contains a literal `K_7` minor unless, after interchanging
`X,Y` and `A,B` if necessary,

\[
 D(X)=\{a\},\quad D(Y)=\{b\},\quad
 a\in A,\quad b\in B,                                   \tag{4.2}
\]

where `a` is `A`-pure and `b` is `B`-pure.

#### Proof

Let `P_1,P_2` be the two disjoint rich full packets and put

\[
                         C=N_S(X)\cap N_S(Y).
\]

If `C` contains one of the boundary triangles, say `A`, choose distinct
`r_1,r_2 in C-A`.  This is possible because `|C|>=5`.  The seven bags

\[
 P_1\cup\{r_1\},\quad P_2\cup\{r_2\},\quad X,\quad Y,
 \quad\{a_1\},\{a_2\},\{a_3\}                            \tag{4.3}
\]

are connected, disjoint and pairwise adjacent.  Packet fullness supplies
all packet incidences, the anchors join each packet bag to `X,Y`, the
given `XY` edge joins the thin carriers, and `A` is a triangle.  Thus (4.3)
is a literal `K_7` model.

Consequently the union `D(X) union D(Y)` must meet both `A` and `B`.
By (4.1), both defects are distinct singletons, one in each triangle;
orient them as in (4.2).

Suppose `a` has a boundary neighbour `c outside A`.  The set
`X'=X union {c}` is connected and is adjacent to every singleton of `A`:
`X` contacts `A-{a}` and the edge `ca` repairs the last adjacency.
The set `Y` contacts all of `A`, since it misses only `b in B`.

If `c!=b`, let

\[
                     \{r_1,r_2\}=S-(A\cup\{b,c\});
\]

if `c=b`, choose any two vertices of `S-(A union {b})`.  In either case
`r_1,r_2` are contacted by both thin carriers.  Replacing `X` by `X'` in
(4.3) gives a literal `K_7` model.  Hence `a` must be `A`-pure.  The
symmetric argument makes `b` `B`-pure. `square`

The proof does not use an edge between `P_1,P_2`; distinct boundary anchors
create that adjacency.  It therefore applies unchanged when the rich
packets lie in two components and when they lie in one connected component.

### Corollary 4.3 (cutvertex structure)

If the thin shore has a cutvertex `w`, then either `G` contains a literal
`K_7` minor or:

1. `L-w` has exactly two components; and
2. those components miss distinct pure vertices lying in different
   boundary triangles.

#### Proof

For every component `D` of `L-w`,

\[
                           N_G(D)\subseteq S\cup\{w\}.
\]

Seven-connectivity gives `|N_S(D)|>=6`.  With two components, take one as
`X` and the other together with `w` as `Y`; Theorem 4.2 applies.

If there are at least three components, put one component on one side and
all the others together with `w` on the other.  If two of the latter have
different singleton defects, or one has empty defect, their union is
`S`-full.  Choose the isolated side so that this happens.  If all component
defects are the same singleton, both sides miss at most that one vertex.
In every case the common contact set contains an entire one of `A,B`, and
the model (4.3) closes.  Thus only two components and the crossed-pure
outcome (4.2) survive. `square`

### Corollary 4.4 (Moser consequence)

In the double-triangle representation of the Moser spindle, one cross edge
joins the triangles and `z` sees the other two vertices of each triangle.
Thus neither triangle has a pure vertex.  The Moser thin shore consequently
has no cutvertex and admits no split satisfying (4.1).  In particular it
cannot have order two: minimum degree seven would make the two singleton
pieces each contact at least six boundary vertices, invoking Theorem 4.2.

This does **not** exclude the singleton thin shore `|L|=1`: a singleton
has no cutvertex, and Dirac's neighbourhood bound permits the Moser
boundary.  No claim that `L` is 2-connected is made here; the singleton
case must be eliminated separately before such a conclusion is available.

## 5. Why contact data alone cannot finish

The crossed-pure alternative in Theorem 4.2 is real at the quotient level.
Let

\[
 H=K_3[012]\mathbin{\dot\cup}K_3[345]\mathbin{\dot\cup}\{6\}.
\]

Add rich packet vertices `p_1=7,p_2=8`, each complete to `S`, and adjacent
to each other.  Add adjacent carrier vertices `x=9,y=10`, where `x` is
complete to `S-{0}` and `y` is complete to `S-{3}`.  This is the strongest
static quotient suggested by a crossed-pure split, including connected-rich
packet adjacency.

It has no `K_7` minor.  Indeed the following bags form a tree decomposition,
with the displayed tree edges:

\[
\begin{array}{lll}
 D_1=\{4,5,7,8,9,10\},&D_2=\{3,4,5,7,8,9\},
   &D_3=\{2,7,8,9,10\},\\
 D_4=\{1,2,7,8,9,10\},&D_5=\{6,7,8,9,10\},
   &D_6=\{0,1,2,7,8,10\},
\end{array}
\]

\[
             D_2D_1,\quad D_1D_3,\quad D_1D_5,
             \quad D_3D_4,\quad D_4D_6.                 \tag{5.1}
\]

Every bag has order at most six, so the quotient has treewidth at most
five.  Since `tw(K_7)=6` and treewidth is minor-monotone, it has no `K_7`
minor.

This quotient is not seven-connected and is not contraction-critical.  It
does not refute the target theorem.  It does prove that fullness, two
near-full thin carriers, and even adjacency of the rich packets do not by
themselves close the crossed-pure case.  Seven-connectivity and exact
proper-minor state witnesses must enter after Theorem 4.2.

The deterministic verifier

`active/hc7_exact7_double_triangle_four_carrier_probe.py`

independently checks this example by exhaustive deletion/contraction and
tests all crossed-pure markings of the ten hard boundary orbits.

## 6. Exact remaining constructive step

After Lemma 2.1, let `Pi` be the actual state returned by the thin packet.
The target is now concrete:

* in a connected rich shore, extract the Theorem 3.1 carrier from a
  connector between, or a peel of, two selected full packets;
* in a two-component rich shore, split one full component so that one part
  is the Theorem 3.1 carrier and the other still funds a different returned
  block.

Failure must be converted into a separator of order at most six or into a
one-step deletion/contraction state transition.  Merely adding more contact
edges to the four-carrier quotient cannot work, as (5.1) shows.
