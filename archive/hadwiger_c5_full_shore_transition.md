# Operation-level constraints in the sharp \(C_5\) full-shore cell

## 1. Setting

Let \(G\) be a proper-minor-minimal counterexample to
\(\mathrm{HC}_7\).  Suppose \((A,B)\) is a separation with adhesion
\(S=A\cap B\), where

\[
 |S|=7,\qquad
 Q:=\overline{G[S]}=C_5\dot\cup2K_1.
\]

Write the complementary cycle as

\[
 q_0q_1q_2q_3q_4q_0
\]

and the two isolated vertices of \(Q\) as \(r_1,r_2\).  Thus
\(G[S]=C_5\vee K_2\), after relabelling the cycle.  Let \(D_A,D_B\)
be distinct components of \(G-S\), each connected and adjacent to every
vertex of \(S\).  Seven-connectivity implies that these are the only two
components in the sharp cell.

An exact six-colour state on \(S\) is either

* \(s_i\): the single complementary edge \(q_iq_{i+1}\) is one colour
  block, giving six boundary colours; or
* \(d_i\): two disjoint complementary edges form colour blocks, giving
  five boundary colours.

There are five states of each kind.

This note uses actual vertex and edge deletions in \(G\).  It does not
infer operation transitions from an abstract state signature.

### Lemma 1.1 (exactly two components)

The graph \(G-S\) has exactly the two components \(D_A,D_B\).

#### Proof

Every component \(D\) of \(G-S\) has \(N(D)=S\): its neighbourhood is
contained in the seven-set \(S\), and seven-connectivity gives the
reverse inequality.  If a third component \(D_3\) existed, use the bags

\[
 \{q_0\},\quad\{q_2\},\quad\{r_1\},\quad\{r_2\},
 \quad D_A,\quad D_B\cup\{q_1\},\quad D_3\cup\{q_3\}.
\]

The four singleton bags form a clique because \(q_0q_2\in E(G[S])\).
Every shore is full, the two anchored shores see one another through
their anchors, and the unanchored shore sees both anchors.  Hence these
are seven pairwise adjacent connected bags, a contradiction. \(\square\)

## 2. A general operation-level transition lemma

For a side \(A\), let \(\mathcal E_A\) be the exact states extending to
a six-colouring of \(G[A]\), and define \(\mathcal E_B\) similarly.
The two families are disjoint, since a common exact state lets the side
colourings be aligned and glued.

### Lemma 2.1 (rainbow transition witnesses)

Let \(x,y\in A-S\), and let \(s\in S\).

1. For every \(x\in A-S\), deletion of \(x\) produces a state
   \(\pi_x\in\mathcal E_B\setminus\mathcal E_A\) and a colouring of
   \(G[A]-x\) with state \(\pi_x\) in which all six colours occur on
   \(N_G(x)\).
2. For every internal edge \(xy\in E(G[A-S])\), deletion of \(xy\)
   produces a state
   \(\pi_{xy}\in\mathcal E_B\setminus\mathcal E_A\) and a colouring
   in which \(x,y\) have the same colour.  Each of \(x,y\) has a
   neighbour of every other colour.
3. For every portal edge \(xs\in E(G)\), deletion of \(xs\) produces a
   state \(\pi_{xs}\in\mathcal E_B\setminus\mathcal E_A\) such that

   \[
   c(x)=c(s),\qquad
   N_S(x)\cap P_{\pi_{xs}}(s)=\{s\},                 \tag{2.1}
   \]

   where \(P_\pi(s)\) is the boundary block of \(s\) in \(\pi\).
   Moreover \(x\) has a neighbour of every colour other than \(c(s)\).

The symmetric statements hold for operations on side \(B\).

#### Proof

Colour the proper minor obtained by the indicated deletion and restrict
the colouring to the two sides.  Its exact boundary state extends the
unchanged opposite side.  If it also extended the original operated
side, the two original sides could be aligned and glued, contrary to
the choice of \(G\).  Hence the state lies in the displayed difference.

For a vertex deletion, a colour absent from \(N_G(x)\) could be assigned
to \(x\), producing a six-colouring of \(G\).  This proves item 1.

For an edge deletion, restoring the edge can fail only if its ends have
the same colour.  If an internal endpoint missed one of the other five
colours on its neighbourhood, recolouring that endpoint would restore
the edge and colour \(G\).  This proves item 2.

For a portal edge \(xs\), the same argument gives \(c(x)=c(s)\) and the
five-colour neighbourhood condition at \(x\).  If \(x\) had another
neighbour \(z\in S\setminus\{s\}\) in the block \(P_{\pi_{xs}}(s)\),
then the undeleted edge \(xz\) would already be monochromatic.  This
proves (2.1). \(\square\)

Condition (2.1) is a genuine portal restriction: every portal deletion
must select an opposite-side state in which that portal is the unique
contact of its boundary colour block.

## 3. A two-piece shore split forces the minor

The following unbounded-order lemma is the basic label-preserving shore
surgery needed in this cell.

### Lemma 3.1 (six-contact two-piece split)

Suppose one shore contains disjoint connected sets \(X,Y\) which are
adjacent and satisfy

\[
 |N_S(X)|\ge6,\qquad |N_S(Y)|\ge6.                   \tag{3.1}
\]

If \(D'\) is the opposite connected full shore, then \(G\) contains a
\(K_7\)-minor.

#### Proof

Let \(C\) be the cycle of \(G[S]=C_5\vee K_2\).  At most two vertices of
\(C\) are missed by at least one of \(X,Y\).  Since a vertex cover of
\(C_5\) has order three, there is an edge \(ab\in E(C)\) disjoint from
the missed vertices.  Thus both \(X\) and \(Y\) touch both \(a,b\).

Among the three vertices of \(C-\{a,b\}\), choose distinct \(c,d\) such
that \(X\) touches \(c\) and \(Y\) touches \(d\).  Each shore piece
misses at most one of the three candidates, so distinct representatives
exist.  The seven bags

\[
 \{a\},\quad\{b\},\quad\{r_1\},\quad\{r_2\},
 \quad X\cup\{c\},\quad Y\cup\{d\},\quad D'          \tag{3.2}
\]

are connected and disjoint.  The first four form a clique.  Each of the
next two sees \(a,b\), they see one another through the \(X\)-\(Y\)
edge, and their cycle anchors see \(r_1,r_2\).  Finally \(D'\) sees every
other bag through its boundary vertex.  Hence \(3.2\) is a \(K_7\)-model.
\(\square\)

### Corollary 3.2 (nonsingleton shores are 2-connected)

Every full shore \(D\in\{D_A,D_B\}\) has either one vertex or is
2-connected.  In particular a nonsingleton shore has no leaf, bridge,
or cutvertex.

#### Proof

First suppose that \(D\) has a bridge.  Its two components \(X,Y\) after
deleting the bridge are connected and adjacent.  The external
neighbourhood of \(X\) is contained in \(S\) together with the endpoint
of the bridge in \(Y\).  It separates \(X\) from the opposite shore, so
seven-connectivity gives \(|N_S(X)|\ge6\).  Symmetrically
\(|N_S(Y)|\ge6\), and Lemma 3.1 applies.

Now suppose \(z\) is a cutvertex of \(D\), and choose two components
\(C_1,C_2\) of \(D-z\).  For each \(j\), the set
\(N_S(C_j)\cup\{z\}\) separates \(C_j\) from the opposite shore, so
\(|N_S(C_j)|\ge6\).  Put \(X=C_1\) and \(Y=C_2\cup\{z\}\).  These sets
are disjoint, connected, adjacent, and each has at least six boundary
neighbours.  Lemma 3.1 again gives the minor. \(\square\)

This improves the finite order-two, order-three, and order-four shore
closures in a different direction: it excludes every articulation
geometry at arbitrary shore order.

### Lemma 3.3 (locked two-cuts)

Let \(D\) be a surviving nonsingleton shore and let
\(\{z_1,z_2\}\) be a two-vertex cut of \(D\).  For any two components
\(C_1,C_2\) of \(D-\{z_1,z_2\}\), put

\[
 A_j=N_S(C_j),\qquad Z_i=N_S(z_i).
\]

Then \(|A_1|,|A_2|\ge5\), both \(z_1,z_2\) have a neighbour in each
\(C_j\), and the following two locking conditions hold:

\[
\begin{aligned}
(&|A_1\cup Z_1|\le5\quad\text{or}\quad
  |A_2\cup Z_2|\le5),\\
(&|A_1\cup Z_2|\le5\quad\text{or}\quad
  |A_2\cup Z_1|\le5).                               \tag{3.3}
\end{aligned}
\]

In particular:

1. two components of \(D-\{z_1,z_2\}\) cannot both have at least six
   boundary neighbours;
2. if \(|A_1|\ge6\), then
   \[
   |A_2|=5,\qquad Z_1\cup Z_2\subseteq A_2,
   \]
   and symmetrically with the indices reversed.

#### Proof

The external neighbourhood of \(C_j\) is contained in
\(S\cup\{z_1,z_2\}\).  Seven-connectivity gives \(|A_j|\ge5\).
Since \(D\) has no cutvertex by Corollary 3.2, each component \(C_j\)
has a neighbour at both \(z_1,z_2\).

The sets

\[
 C_1\cup\{z_1\},\qquad C_2\cup\{z_2\}
\]

are disjoint, connected, and adjacent.  If both had at least six
boundary neighbours, Lemma 3.1 would give a \(K_7\)-minor.  This is the
first line of (3.3).  Interchanging \(z_1,z_2\) gives the second line.

If \(|A_1|,|A_2|\ge6\), the first line is already impossible.  If
\(|A_1|\ge6\), both alternatives involving \(A_1\) fail, so (3.3)
forces
\(|A_2\cup Z_1|\le5\) and \(|A_2\cup Z_2|\le5\).
Together with \(|A_2|\ge5\), these are exactly the displayed
containments. \(\square\)

Thus any remaining two-cut is not arbitrary: all but possibly one of
its bridges have an exact five-vertex contact set which contains the
boundary contacts of both cut vertices.

## 4. Two disjoint missing-edge linkages force the minor

### Lemma 4.1 (rooted two-linkage closure)

Suppose one shore contains paths \(P_{01}\) from \(q_0\) to \(q_1\) and
\(P_{23}\) from \(q_2\) to \(q_3\), whose interiors lie in the shore and
which are internally vertex-disjoint.  Then \(G\) contains a
\(K_7\)-minor.

The same holds for any two vertex-disjoint edges of the complementary
cycle \(Q[C]\).

#### Proof

Let \(D'\) be the opposite full shore.  Use the seven bags

\[
 \{q_0\},\quad \{q_3\},\quad \{r_1\},\quad \{r_2\},
 \quad (V(P_{01})-\{q_0\})\cup\{q_4\},
 \quad V(P_{23})-\{q_3\},\quad D'.                  \tag{4.1}
\]

The fifth bag is connected because \(q_1q_4\in E(G[S])\); the sixth is
connected as a truncated path.  The first and second bags are adjacent
because \(q_0q_3\in E(G[S])\).  The fifth bag sees \(q_0\) through its
path and sees \(q_3\) through \(q_1q_3\).  The sixth sees \(q_3\) through
its path and sees \(q_0\) through \(q_2q_0\).  The fifth and sixth bags
are adjacent through \(q_4q_2\).  Both see \(r_1,r_2\), and the opposite
full shore sees every boundary-containing bag.  These are all 21
adjacencies. \(\square\)

Thus a surviving shore is not merely unable to split as in Lemma 3.1:
it also fails every rooted two-linkage for two vertex-disjoint missing
edges of \(G[S]\).

## 5. The singleton-shore polarity and its list-critical consequence

Assume \(D_A=\{a\}\).  Since it is full, a boundary state extends over
\(a\) exactly when it uses at most five boundary colours.  Therefore

\[
 \mathcal E_A=\{d_0,d_1,d_2,d_3,d_4\}.              \tag{5.1}
\]

The exact-block constraints and disjointness force

\[
 \mathcal E_B=\{s_0,s_1,s_2,s_3,s_4\}.              \tag{5.2}
\]

Indeed, for every complementary edge \(e_i\), its exact-block edge is
\(\{s_i,d_i,d_{i+3}\}\).  The last two states already belong to
\(\mathcal E_A\), so the \(B\)-side must realize \(s_i\), and it can
realize no \(d_j\).

Fix named colours on a state \(d_i\).  For \(x\in D_B\), let

\[
 L_i(x)=[6]\setminus c_i(N_S(x))                    \tag{5.3}
\]

be the colours available after the boundary is precoloured by \(d_i\).
The shore \(D_B\) is not \(L_i\)-colourable for any \(i\).

### Lemma 5.1 (simultaneous deletion-critical lists)

For every \(x\in D_B\), there is an index \(i=i(x)\) such that
\(D_B-x\) is \(L_i\)-colourable but \(D_B\) is not.  Consequently

\[
 |L_i(x)|\le d_{D_B}(x).                             \tag{5.4}
\]

For every internal edge \(xy\in E(D_B)\), there is an index \(j\) and
an \(L_j\)-colouring of \(D_B-xy\) in which \(x,y\) have the same colour
and each endpoint sees all five other colours.

#### Proof

Apply Lemma 2.1.  Every opposite-side transition state is one of the
five states in (5.1), giving the asserted list colouring after a vertex
or edge deletion.  If (5.4) failed, an \(L_i\)-colouring of \(D_B-x\)
would leave some colour of \(L_i(x)\) unused on the at most
\(d_{D_B}(x)\) internal neighbours of \(x\), extending to \(D_B\).  The
edge statement is Lemma 2.1(2). \(\square\)

This is stronger than saying that five abstract transitions exist:
every actual internal vertex and edge is critical for at least one of
the five concrete precolouring list assignments.

### Lemma 5.2 (a degree constraint from the five simultaneous lists)

Let \(x\in D_B\).  Put

\[
 T=N_S(x)\cap\{q_0,\ldots,q_4\},\quad k=|T|,
 \qquad h=|N_S(x)\cap\{r_1,r_2\}|.
\]

Let \(p_i(T)\) be the number of the two paired edges in \(d_i\) whose
both endpoints lie in \(T\).  Then

\[
 |L_i(x)|=6-h-k+p_i(T),                              \tag{5.5}
\]

and minimum degree gives

\[
 |L_i(x)|\le d_{D_B}(x)-1+p_i(T).                   \tag{5.6}
\]

In particular:

1. if \(T\ne V(C_5)\), at most one index \(i\) can have
   \(|L_i(x)|>d_{D_B}(x)\);
2. if \(x\) is adjacent to all five cycle vertices, then
   \(d_G(x)\ge8\).

#### Proof

The two paired boundary blocks save one distinct forbidden colour each
time both endpoints are in \(T\), proving \(5.5\).  Since the sharp cell
has exactly the two components,

\[
 d_{D_B}(x)+k+h=d_G(x)\ge7,
\]

which gives \(5.6\).

The value \(p_i(T)\) is at most one unless \(T\) contains all four
vertices covered by the matching \(d_i\).  A proper subset \(T\) can do
this for at most one of the five maximum matchings of a \(C_5\).  This
proves item 1.

If \(T=V(C_5)\), then \(p_i(T)=2\) and
\(|L_i(x)|=3-h\) for every \(i\).  If \(d_G(x)=7\), then
\(d_{D_B}(x)=2-h\), so every one of the five lists has size
\(d_{D_B}(x)+1\).  This contradicts Lemma 5.1 for the deletion witness
at \(x\).  Hence \(d_G(x)\ge8\). \(\square\)

There is also a portal-specific sharpening.  If \(x\) sees all five
cycle vertices, deleting the portal edge \(xq_j\) must use the unique
double-matching state in which \(q_j\) is the unmatched singleton.
Otherwise the mate of \(q_j\) in its paired block would violate the
private-block condition \(2.1\).

## 6. The forced Kempe web in the singleton-shore case

### Lemma 6.1 (cyclic Kempe paths)

Fix \(i\in\mathbb Z_5\) and any colouring of side \(B\) with state
\(s_i\).  There is a \(q_{i+2}\)-\(q_{i+3}\) Kempe path and a
\(q_{i+3}\)-\(q_{i+4}\) Kempe path whose internal vertices lie in
\(D_B\).  Each path uses only the two colours of its ends.

#### Proof

Consider, for example, the two-colour subgraph on the colours of
\(q_{i+2},q_{i+3}\).  These colours occur at no other boundary vertex in
state \(s_i\).  If the two terminals were in different components,
swap the two colours on the component containing \(q_{i+2}\).  The two
terminals would then have the same colour, while all other boundary
blocks would be unchanged.  This would extend the double state formed by
the disjoint complementary edges
\(q_iq_{i+1}\) and \(q_{i+2}q_{i+3}\), contrary to (5.2).  Thus the
Kempe path exists and has no internal boundary vertex.  The other path
is identical. \(\square\)

Combining Lemmas 4.1 and 6.1 gives an exact structural obstruction.
Every one of the five single-pair colourings supplies two adjacent-edge
Kempe paths, but no paths for two vertex-disjoint complementary edges
can be internally disjoint.  Thus the remaining singleton-shore object
is an interlaced five-terminal Kempe web, not an arbitrary connected
shore.

## 7. Facial pieces in the generalized five-web

For one shore \(D\), form the auxiliary graph \(A_D\) by adding
terminals \(t_0,\ldots,t_4\), with

\[
 N_{A_D}(t_i)=N_D(q_i).
\]

If none of the five rooted two-linkages from Lemma 4.1 exists, the
generalized Two Paths Theorem places \(A_D\) in a five-web with frame
\((t_0,\ldots,t_4)\).  The next observation removes all genuine
facial attachments from that web.

### Lemma 7.1 (facial-triangle pieces are empty)

Let \(U\subseteq D\) be nonempty, and suppose its external
neighbourhood in \(A_D\) is contained in a set \(T\) of at most three
vertices.  Assume \(U\) contains no frame terminal.  Then this
configuration cannot occur.

In particular, no nonempty set of actual shore vertices can lie in a
clique inserted behind a facial triangle of a five-web, or on a
terminal-free side of a web separation of order at most three.

#### Proof

Replace every artificial terminal \(t_i\in T\) by the original boundary
vertex \(q_i\), and retain every vertex of \(T\cap D\).  Call the
resulting set \(\widehat T\); it has order at most three.

If \(u\in U\) has a cycle-boundary neighbour \(q_i\), then
\(ut_i\in E(A_D)\).  Since all \(A_D\)-neighbours of \(U\) outside \(U\)
lie in \(T\), either \(t_i\in T\) or \(t_i\in U\); the latter is excluded
by the hypothesis.  Thus every cycle-boundary neighbour of \(U\) is
represented in \(\widehat T\).  The only boundary neighbours not
represented in \(A_D\) are \(r_1,r_2\).  Consequently

\[
 N_G(U)\subseteq \widehat T\cup\{r_1,r_2\},
\]

a set of order at most five.  It separates \(U\) from the opposite full
shore, contradicting seven-connectivity. \(\square\)

Thus the web alternative contains no hidden clique modules: every
actual shore vertex lies in the bare planar rib, and no separating
triangle has an actual terminal-free side.

### Corollary 7.2 (tight degrees in the bare rib)

For \(x\in D\), put

\[
 d_A(x):=d_{A_D}(x)
       =d_D(x)+|N_S(x)\cap\{q_0,\ldots,q_4\}|.
\]

Then \(d_A(x)\ge5\).  If \(d_A(x)=5\), then \(x\) is adjacent to both
\(r_1,r_2\) and \(d_G(x)=7\).

If \(D\) is nonsingleton, every such degree-five web vertex has at most
three cycle neighbours.

#### Proof

The sharp cell has exactly two components, so

\[
 d_G(x)=d_A(x)+|N_S(x)\cap\{r_1,r_2\}|.
\]

Minimum degree seven and the last term being at most two prove the first
two assertions.  If \(D\) is nonsingleton, Corollary 3.2 gives
\(d_D(x)\ge2\).  The equality
\(d_A(x)=d_D(x)+|N_S(x)\cap V(C_5)|=5\) then leaves at most three cycle
neighbours. \(\square\)

This is the requested facial-triangle reduction: a facial piece cannot
be an operation-irrelevant module because connectivity removes it
outright.  Any remaining low-degree rib vertex is palette-tight and is
governed by an actual deletion transition.

## 8. Former exact remaining gap

The operation-level information proves the following portrait for a
surviving \(C_5\dot\cup2K_1\) full-shore cell:

1. there are exactly two full shores;
2. every nonsingleton shore is 2-connected;
3. every vertex deletion, internal edge deletion, and portal-edge
   deletion has the rainbow/private-block witness of Lemma 2.1;
4. a two-piece six-contact split or a rooted linkage for two disjoint
   missing edges immediately gives a \(K_7\)-minor;
5. if one shore is a singleton, the opposite shore is simultaneously
   critical for the five lists \(L_i\), every cycle-complete vertex has
   degree at least eight, and the shore carries the interlaced Kempe web
   of Lemma 6.1.

6. in the five-web alternative every facial insertion and every
   terminal-free triangle side is empty; the actual shore is a bare rib
   of auxiliary minimum degree five.

At the stage represented by Sections 1--7, what was not yet proved was
the **web-to-split lemma**:

> A 2-connected full shore satisfying all five simultaneous deletion
> and edge-transition conditions cannot block every pair of disjoint
> complementary-edge linkages.

This is the exact additional structural input needed in the singleton
cell.  Pairwise Kempe connectivity alone is insufficient: the witnesses
for different \(s_i\) use different colourings, while Lemma 4.1 requires
two disjoint paths present simultaneously.  Any continuation must use
the operation-level rainbow witnesses or seven-connectivity to align
those paths; the static six-signature table cannot do so.

The script `c5_two_piece_portal_models.py` independently searches all
two-piece boundary-contact quotients with collective full contact.  It
finds 40 labelled minimal \(K_7\)-forcing patterns in three symmetry
orbits and replays exact seven-branch-set models.  Lemma 3.1 is the
uniform hand-provable subfamily needed above; the computation is not
used in its proof.

## 9. Closure by simultaneous five-web planarity

The former gap is now bypassed completely.  Apply the five-terminal
auxiliary construction of Section 7 separately to each of the two full
shores.  For either shore, a crossing consists (up to dihedral symmetry)
of disjoint portal paths for the pairs \(q_0q_2\) and \(q_1q_4\).
Together with adjacent connected enlargements of those paths, the four
boundary singleton bags \(q_0,q_1,r_1,r_2\), and the opposite full shore,
these paths give an explicit \(K_7\)-model.

Consequently, in the absence of a \(K_7\)-minor both five-terminal tuples
are crossless.  Complete each auxiliary graph, by adding edges on its
fixed vertex set, to a maximally crossless graph.  The generalized Two
Paths Theorem identifies each completion as a five-web with the terminals
as its frame.  Lemma 7.1 removes every inserted clique: an inserted
clique has at most its three facial vertices plus \(r_1,r_2\) in its
original neighbourhood, contradicting seven-connectivity because the
opposite shore is nonempty.  Thus each actual shore lies in the bare
planar rib and has a disk embedding with \(q_0q_1q_2q_3q_4q_0\) as its
boundary.

Glue the two disk embeddings on opposite sides of this boundary cycle.
The shores are anticomplete, so this produces a plane embedding of

\[
  G-\{r_1,r_2\}.
\]

The Four Color Theorem gives four colours to this planar graph, and two
fresh colours give distinct colours to \(r_1,r_2\).  Hence the sharp
\(C_5\dot\cup2K_1\) full-shore core always has a \(K_7\)-minor or is
six-colourable.  The complete proof, including the explicit crossing
model and the same-vertex web-completion interface, is recorded in
`hadwiger_c5_full_web_closure.md`.

Therefore the exact remaining gap stated above is closed for shores of
arbitrary order; none of the operation-level transition conditions from
Sections 2, 5, and 6 is needed for the final closure.
