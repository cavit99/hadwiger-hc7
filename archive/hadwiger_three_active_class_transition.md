# Three active portal classes: cut classification and operation-state lock

## 1. Purpose and local formulation

This note treats the first synchronization cell not covered by the
two-class splitter.  It is deliberately **local**.  In a join-prime
counterexample no singleton portal row is globally universal, so the phrase
"three active classes" below means three rows which remain unsynchronized in
the current closed society.  All other model adjacencies have already been
secured on both prospective pieces (for example by portal rows which are
universal on the society, or by fixed carriers outside it).

Let \(J\) be a two-connected graph and let

\[
                       P_1,P_2,P_3\subseteq V(J)              \tag{1.1}
\]

be its three active portal rows.  A **good split** is a partition

\[
                         V(J)=A\mathbin{\dot\cup}D             \tag{1.2}
\]

such that \(J[A]\) and \(J[D]\) are connected and both \(A,D\) meet
every \(P_i\).  Extending two disjoint connected transversals along a
spanning tree shows that it is equivalent to ask only for two disjoint
connected sets meeting all three rows.  Explicitly, join the two sets by
a shortest path and assign its internal vertices to one side so that the
two carriers become adjacent.  Contract the carriers, take a spanning tree
containing their joining edge, delete that tree edge, and expand.  The two
tree components give (1.2) without losing any portal contact.

In a one-complex-bag/singleton model, a good split gives two adjacent
connected branch sets, each retaining all required model adjacencies.
Together with the old singleton bags they form the next clique minor.  Thus
the first outcome below is a genuine rooted-model conclusion, not merely a
set bipartition.

The main result has two parts.

* A two-cut admits a complete, label-free classification.  Apart from an
  owned atom, only two exact quotient geometries survive.
* In a minor-critical graph the full operation spectra of distinct surviving
  shores are disjoint on the genuine adhesion.  The two-lobe geometry has a
  three-state anchored-contraction normal form.

The second assertion uses every faithful operation, and in particular every
edge-deletion transition.  It is the dynamic hypothesis missing from the
suspended-octahedron and diamond examples.

## 2. Capacity atoms at a two-cut

Fix a two-cut \(X=\{x,y\}\) of \(J\), and let

\[
                         C_1,\ldots,C_m                         \tag{2.1}
\]

be the components of \(J-X\).  Two-connectivity implies that every \(C_a\)
has a neighbour at both \(x\) and \(y\).  For an atom

\[
 {\cal A}_X=\{\{x\},\{y\},C_1,\ldots,C_m\},                   \tag{2.2}
\]

write

\[
 \rho(Z)=\{i\in[3]:Z\cap P_i\ne\varnothing\}.                \tag{2.3}
\]

We use two hypotheses which are exactly what the counterexample reductions
supply at an atomic three-class window.

1. **Capacity:** every lobe has

   \[
                              |\rho(C_a)|\ge2.                 \tag{2.4}
   \]

   In the spanning one-complex cell this follows directly from ambient
   \(r\)-connectivity.  Indeed, if \(r-4\) already-secured singleton labels
   occur on the lobe, then

   \[
       N_H(C_a)=X\cup U\cup\{b_i:i\in\rho(C_a)\}
   \]

   has order \(2+(r-4)+|\rho(C_a)|\), and is a proper cut.
2. **No owned row:** every \(i\in[3]\) occurs in at least two distinct atoms
   of \({\cal A}_X\):

   \[
       |\{Z\in{\cal A}_X:i\in\rho(Z)\}|\ge2.                    \tag{2.5}
   \]

If (2.5) fails, all portals of one active row are confined to one \(X\)-atom.
This is not declared harmless: it is the precise **owner descent** outcome.
The owner atom, with its two attachments when it is a lobe, is the smaller
core/ear on which the operation-critical analysis must recurse.

The distinction between portal vertices and atoms is important.  Two portals
of the same row inside one lobe still count as one atom.  Treating them as
two distributed contacts would make a false Hall argument.

### Lemma 2.1 (every split-free core has an ordered frame)

Assume \(|P_i|\ge2\) for \(i=1,2,3\).  Choose distinct \(s,t\in P_1\).
There is an ordering

\[
                         s=z_1,z_2,\ldots,z_n=t                 \tag{2.6}
\]

such that every prefix and every suffix induces a connected subgraph of
\(J\).  In every such ordering, if \(J\) has no good split, then, after
possibly interchanging \(P_2,P_3\),

\[
                 \max\{\operatorname{pos}(z):z\in P_2\}
                 \ \le\
                 \min\{\operatorname{pos}(z):z\in P_3\}.       \tag{2.7}
\]

Thus the three-class obstruction is an ordered web obstruction, not an
arbitrary hypergraph obstruction.

#### Proof

Add \(st\) if necessary and take an \(st\)-numbering of the resulting
two-connected graph.  Each internal vertex has an earlier and a later
neighbour.  The added edge joins only the two extreme vertices, so all
edges used to connect prefixes and suffixes are edges of \(J\).  This gives
(2.6).

For \(i=2,3\), a cut after position \(k\) splits \(P_i\) precisely when

\[
 \min\operatorname{pos}(P_i)\le k<
 \max\operatorname{pos}(P_i).                               \tag{2.8}
\]

Every such cut splits \(P_1\), because \(s,t\) are the two extremes.  If
the two integer intervals in (2.8) intersect, the corresponding connected
prefix/suffix partition is a good split.  In a split-free graph they are
disjoint, which is exactly (2.7), up to interchanging \(2,3\).
\(\square\)

## 3. The finite profile lemma

### Lemma 3.1 (three-class two-cut classification)

Assume (2.4)--(2.5).  Then one of the following holds.

1. \(J\) has a good split.
2. After permuting \(1,2,3\) and interchanging \(x,y\), \(m=2\) and

   \[
   \begin{aligned}
      \rho(C_1)&=\{1,2\},&\rho(C_2)&=\{1,3\},\\
      \rho(y)&=\{2,3\},&\rho(x)&\subseteq\{1\}.
   \end{aligned}                                             \tag{3.1}
   \]

   This is the **common-bottleneck pair**.
3. We have \(m=3\), and after relabelling the three lobes,

   \[
   \rho(C_{12})=\{1,2\},\quad
   \rho(C_{13})=\{1,3\},\quad
   \rho(C_{23})=\{2,3\},\quad
   \rho(x)=\rho(y)=\varnothing .                              \tag{3.2}
   \]

   This is the **cyclic three-shore frame**.

In particular, four or more lobes always give a good split.

#### Proof

For any set \(I\subseteq[m]\), the two sets

\[
 A_I=\{x\}\cup\bigcup_{a\in I}C_a,
 \qquad
 D_I=\{y\}\cup\bigcup_{a\notin I}C_a                       \tag{3.3}
\]

are connected, even if one of the lobe unions is empty: every lobe has a
neighbour at both cut vertices.  They are adjacent unless \(J\) has only
the two isolated cut vertices, which is impossible.  Consequently (3.3)
is a good split whenever both unions of profiles are \([3]\).

There is one other useful split.  If a lobe \(C_a\) has profile \([3]\),
then \(C_a\) and \(J-C_a\) are connected.  Hypothesis (2.5) says every
row occurs outside \(C_a\), so both sides meet every row.  Hence outcome 1
holds.  We may therefore assume every lobe profile is a two-set.  Encode a
lobe by the unique row it misses.

Suppose first that \(m\ge4\).  If at least two missing-row types each occur
twice, put one lobe of each type on either side of (3.3).  Each side then
contains two different two-set profiles and hence all three rows.  If all
three types occur, one type occurs twice; pair its two copies separately
with lobes of the other two types.  If only one type occurs, its missing row
can occur only at \(x,y\); (2.5) puts it at both cut vertices, so (3.3) is
good.  Finally suppose one type occurs once and the other \(m-1\) times.
Put the exceptional lobe together with one repeated lobe on one side.  The
other side contains a repeated lobe and misses only the repeated type's
row.  That row occurs in the exceptional lobe and, by (2.5), at one cut
vertex; assign this cut vertex to the repeated-only side.  Again (3.3) is
good.  This proves the last sentence of the lemma.

Let \(m=3\).  The same argument closes the cases in which all missing types
are equal or exactly two types occur.  If the three types are distinct, two
lobes together meet every row.  A remaining single lobe can be completed by
a cut vertex containing its missing row.  Thus a good split exists unless
both cut-vertex profiles are empty.  The remaining profiles are exactly
(3.2).

Let \(m=2\).  If the two lobes have the same missing row, (2.5) puts that
row at both \(x\) and \(y\), and assigning the cut vertices to opposite
lobes gives a good split.  Hence their missing rows are different.  After
renaming, their profiles are

\[
                         \{1,2\},\qquad\{1,3\}.                \tag{3.4}
\]

To complete the first lobe requires a cut vertex in \(P_3\); to complete
the second requires the other cut vertex in \(P_2\).  If these two demands
have a matching into

\[
                              \{x,y\},                         \tag{3.5}
\]

we obtain a good split.  Otherwise Hall's theorem for this two-demand
system says that all occurrences of rows \(2,3\) on the cut lie at one
vertex, say \(y\).  Condition (2.5) guarantees that both rows do occur on
the cut, since each occurs in only one of the two lobes.  Thus

\[
                         \{2,3\}\subseteq\rho(y),
 \qquad \rho(x)\cap\{2,3\}=\varnothing .                       \tag{3.6}
\]

If \(1\in\rho(y)\), the singleton \(\{y\}\) meets all three rows, while
\(J-y\) is connected and meets all three rows (the two lobes are joined
through \(x\)).  This is a good split.  Therefore \(1\notin\rho(y)\),
while \(x\) may or may not lie in \(P_1\).  This is exactly (3.1).
\(\square\)

### Corollary 3.2 (all non-three-connected windows are typed)

Let \(J\) be a target-free three-class window satisfying (2.4).  At every
two-cut, either a row has a unique owner atom, or the cut has one of the
two exact forms (3.1)--(3.2).  There is no untyped two-cut residue.

This is an infinite-family statement: the lobes in (3.1)--(3.2) have
arbitrary order and internal structure.

## 4. The cyclic frame has no cut edge

The cyclic quotient contains one additional immediate rooted model.

### Lemma 4.1 (edge repair of the cyclic frame)

Assume (3.2).  Suppose the already-secured labels outside
\(\{1,2,3\}\) are represented by singleton bags adjacent to every lobe
and to \(x,y\).  If \(xy\in E(J)\), these bags together with the following
five branch sets form the next clique minor:

\[
 \{x\},\quad \{y\},\quad C_{12},\quad
 \{b_1\}\cup C_{13},\quad
 \{b_2\}\cup C_{23}.                                  \tag{4.1}
\]

Consequently a target-free cyclic frame has \(xy\notin E(J)\).

#### Proof

Every set in (4.1) is connected.  The first two see every lobe and see one
another through \(xy\).  The set \(C_{12}\) sees the last two sets through
its \(b_1\)- and \(b_2\)-contacts.  The last two sets see one another
through \(b_1b_2\in E(S)\).  All other pairwise adjacencies use the two-cut
attachments.  Thus (4.1) is a \(K_5\)-model.  Each secured singleton label
is adjacent to all five sets and to every other secured singleton, so they
extend (4.1) to the claimed clique model.  In the \(r\)-colour cell there
are \(r-4\) such labels, and the total order is
\(5+(r-4)=r+1\). \(\square\)

Notice that \(b_3\) is deliberately not a branch set in (4.1).  Reusing it
would incorrectly assume that \(x,y\) contact row \(3\).

## 5. Full minor-operation spectra on separated lobes

The static classification becomes useful because minor-criticality supplies
an operation at every edge, not just one selected contraction state.

Let \(G\) be non-\(r\)-colourable and suppose every proper minor of \(G\)
is \(r\)-colourable.  Let

\[
 V(G)=W\mathbin{\dot\cup}D_1\mathbin{\dot\cup}\cdots
                \mathbin{\dot\cup}D_m,                         \tag{5.1}
\]

where the nonempty \(D_i\) are pairwise anticomplete and every neighbour of
each \(D_i\) outside it belongs to \(W\).  In the spanning singleton cell
at a two-cut one takes

\[
                         W=S\cup\{x,y,v\};                      \tag{5.2}
\]

the apex \(v\) must be included whenever it has feet in more than one
lobe.

For a boundary-faithful proper minor operation \(\mu\) supported in \(D_i\)
(deletion of an internal edge or vertex, contraction of an internal edge,
or deletion of the whole open lobe is enough), let

\[
 \Sigma_i(\mu)=\{\Pi_W(c):c\text{ is an }r\text{-colouring of }G/\mu\}
                                                                    \tag{5.3}
\]

where \(\Pi_W(c)\) is the equality partition of the labelled set \(W\).
Colour names are immaterial; equality on \(W\) lets us align them by one
palette permutation.

### Theorem 5.1 (operation-spectrum anti-coincidence)

If \(i\ne j\), and \(\mu,\nu\) are boundary-faithful proper operations
supported respectively in \(D_i,D_j\), then

\[
                            \Sigma_i(\mu)\cap
                            \Sigma_j(\nu)=\varnothing .          \tag{5.4}
\]

In particular this holds for every pair of edge deletions in distinct
lobes.  Every colouring of \(G-e\) gives the two ends of \(e\) one colour,
and the resulting full edge-defect state belongs to a lobe-specific state
class disjoint from all other lobe classes.

#### Proof

Suppose colourings \(c_\mu,c_\nu\) induce the same equality partition on
\(W\).  Permute the colours of one so that they agree literally on \(W\).
Use \(c_\nu\) on \(D_i\), where the operation \(\nu\) changed nothing, and
use \(c_\mu\) on every \(D_k\) with \(k\ne i\), including \(D_j\), where
\(\mu\) changed nothing.  Use their common colouring on \(W\).  There are
no edges between distinct open lobes, so these restrictions give a proper
\(r\)-colouring of the original graph \(G\), a contradiction.  This proves
(5.4).

For an edge deletion \(e=ab\), any \(r\)-colouring of \(G-e\) has
\(c(a)=c(b)\); otherwise restoring \(e\) gives an \(r\)-colouring of \(G\).
This proves the final assertion. \(\square\)

The theorem also shows exact novelty.  A state produced by an operation in
\(D_i\) cannot extend over the original \(D_i\) while retaining the
colouring of \(W\) and the other lobes, since that extension would colour
\(G\).  Thus each edge deletion/contraction creates a genuinely new state
on its own shore, and states created on different shores can never agree.

The same proof permits a **single boundary anchor**.  Namely, replace an
internal operation in \(D_i\) by contraction of a connected set
\(Z_i\subseteq D_i\cup\{w\}\) onto one retained label \(w\in W\), provided
\(Z_i-\{w\}\subseteq D_i\).  In the crossed colouring, use the colouring
from the opposite operation on the original \(D_i\); it contains all
original \(wD_i\)-edges.  This is the anchored form used below.  Allowing
two boundary anchors would identify labels and is not covered.

## 6. The common-bottleneck pair has a small state alphabet

Retain (3.1), and use the notation

\[
 C_{12}=C_1,\qquad C_{13}=C_2,\qquad p=x,\quad q=y.       \tag{6.1}
\]

Thus \(q\) owns precisely the two missing active contacts \(2,3\), while
\(p\) is dark to those rows and may contact row \(1\).  Assume here that
every secured singleton row is universal on the window
\(C_{12}\cup C_{13}\cup\{p,q\}\).  Perform either of the two rooted
contractions

\[
 C_{12}\cup\{q\}\longrightarrow q,\qquad
 C_{13}\cup\{q\}\longrightarrow q.                       \tag{6.2}
\]

These are proper boundary-anchored minor operations on opposite open
shores.

### Theorem 6.1 (three-state bottleneck lock)

In every \(r\)-colouring after either contraction in (6.2):

1. the singleton clique \(S\) is rainbow;
2. \(q\) receives the unique colour \(\alpha\) absent from \(S\);
3. \(p\) has a colour occurring on one of \(b_1,b_2,b_3\), and
   \(c(p)\ne\alpha\);
4. if \(p\in P_1\), only the two states \(p=b_2\) and \(p=b_3\) are
   possible; otherwise the alphabet is

   \[
                           p=b_1,\quad p=b_2,\quad p=b_3.       \tag{6.3}
   \]

After the equality relation of the apex \(v\) is included, the state sets
of the two contractions are disjoint.  Equivalently, if the same marked
state in (6.3) occurred on both sides, crossing the two colourings would
colour \(G\).

#### Proof

After either contraction, \(q\) is adjacent to \(p\), to all three active
singletons, and to every secured singleton: the contracted lobe supplies
row \(1\), one of rows \(2,3\), and the \(p\)-edge, while the original
vertex \(q\) supplies the other of rows \(2,3\).  Thus \(q\) is adjacent to
every vertex of the \((r-1)\)-clique \(S\).  It must use the unique missing
colour \(\alpha\), and its edge to \(p\) forbids \(\alpha\) at \(p\).

The secured singleton colours are also forbidden at \(p\).  Hence \(p\)
equals one of \(b_1,b_2,b_3\).  Its active portal profile is either empty
or \(\{1\}\), giving exactly (6.3) and its two-state subcase.

Finally regard the two contractions as the operations \(\mu,\nu\) in
Theorem 5.1, with \(q\) retained as a common boundary label.  Equality on
\(S\cup\{p,q,v\}\) would let us use the colouring from the second
contraction on the original first lobe and conversely, restoring both
lobes.  This is impossible. \(\square\)

This is the promised **capacity--state web exchange** in the first
three-class cell.  The quotient obstruction is not an unstructured portal
society: it is one common bottleneck carrying a two- or three-symbol state,
and the two entire all-operation spectra must occupy disjoint symbols
(including the apex mark).

## 7. The three-connected alternative is a genuine core descent

The preceding theorem disposes of all untyped two-cuts.  For the remaining
statement assume explicitly that the closed three-class window \(J\), with
its labelled external boundary \(L\), is full and relatively
\(r\)-connected in the sense of
hadwiger_label_free_portal_splitter.md.  Assume also that the ambient graph
is \(r\)-connected; this is what turns a tight relative boundary into a
full shore.  If \(J\) is three-connected, apply the label-free portal
splitter to the forbidden pattern consisting of two disjoint adjacent
connected transversals of \(P_1,P_2,P_3\).  Realization of this pattern is
a good split, and it lifts through every contraction: expand the unique
branch set containing the contracted vertex to both ends of the edge.

Consequently, for \(|J|\ge5\), one of the following holds.

1. the rooted split (and hence the target model) exists;
2. a three-connectivity-preserving edge contraction keeps the window full,
   relatively \(r\)-connected, and split-free, while creating a genuinely
   new exact boundary-colouring state; or
3. the contraction exposes a tight relative \(r\)-boundary, whose shore is
   full to that boundary.

This is Theorems 3.1 and 4.1 of
hadwiger_label_free_portal_splitter.md specialized to three active rows.
Its hypotheses are not consequences of three-connectivity alone; fullness,
relative connectivity, and the closed-side factorization must be verified
in each application.  Moreover, outcome 2 is only a **one-step descent**,
not closure.  It is a real reduction in the original graph because its new
state is compared with the original side.  Repeating arbitrary contractions
through already-colourable quotient graphs and pigeonholing their states
would be invalid.

Under those explicit hypotheses, combining this with Corollary 3.2 gives
the uniform trichotomy

\[
\boxed{
 \begin{array}{c}
 \text{rooted connected split / target,}\quad
 \text{strict owner or contractible-core descent,}\quad
 \text{exact two- or three-shore state lock.}
 \end{array}}                                                \tag{7.1}
\]

## 8. Audit and exact remaining gap

1. **Connectivity.**  Two-connectivity is used only to make every lobe
   adjacent to both cut vertices.  The profile lower bound (2.4) is stated
   separately; it must not be inferred in a local window unless the
   displayed ambient cut count is available.
2. **Portal multiplicity.**  Two portal vertices in one lobe do not count as
   two atoms.  Their concentration is the owner-descent outcome, not a
   Hall match.
3. **Label preservation.**  Every rooted-model construction lists its
   branch sets.  Lemma 4.1 intentionally drops \(b_3\), and the remaining
   secured singleton bags retain their literal labels.
4. **Apex.**  The state support includes \(v\).  Omitting it would identify
   pinned and unpinned states and make the crossing argument false.
5. **Static counterexamples.**  The suspended octahedron and dynamic
   diamond satisfy static connectivity/portal constraints, but they do not
   satisfy Theorem 5.1's full all-edge defect-state system: their ambient
   graphs are colourable, and a deleted edge can retain differently coloured
   ends.  They therefore do not survive (7.1).

What is not proved here is that the disjoint state alphabets in Theorem 6.1
must intersect.  The abstract transition-diamond construction shows that
minor novelty alone cannot prove this.  Closing the two-lobe residue must
use the actual placement of the \(P_1\)-portals or an edge-deletion Kempe
carrier which transports one of the symbols in (6.3) across the bottleneck.
The cyclic residue similarly needs an exchange among its three private lobe
spectra.  The gain is that these are now the only non-three-connected
three-active-class geometries, for lobes of arbitrary size.
