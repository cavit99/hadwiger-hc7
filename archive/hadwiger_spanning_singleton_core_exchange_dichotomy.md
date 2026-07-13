# Clean core ear or a rooted-model split

## 1. Statement

The proper-core obstruction in a spanning one-complex-bag model has a
uniform connectivity description.  It does not require any Gallai
casework.

Let \(r\ge3\), let \(H\) be an \(r\)-connected graph, and suppose

\[
 V(H)=V(B)\mathbin{\dot\cup}S,\qquad
 S=\{b_1,\ldots,b_{r-1}\},                              \tag{1.1}
\]

where \(S\) is a clique, \(B\) is connected, and

\[
                    (B,\{b_1\},\ldots,\{b_{r-1}\})       \tag{1.2}
\]

is a spanning \(K_r\)-model.  Let \(R\) be any nonempty connected proper
induced subgraph of \(B\).  In the intended application, \(R\) is a
minimal unexpandable list core.

### Theorem 1.1 (core ear or rooted-model split)

At least one of the following holds.

1. **Clean core ear.**  Some component \(D\) of \(B-V(R)\) has at least
   two neighbours in \(R\).  In particular, \(R\) has an \(R\)-path whose
   interior lies in \(D\).
2. **Rooted-model split.**  \(H\) contains a \(K_{r+1}\)-minor whose
   first \(r-1\) branch sets are the singleton bags in \(S\).
3. **Exact universal-owner adhesion.**  The graph \(B-V(R)\) has exactly
   one component \(D\), there is a unique vertex \(q\in R\) adjacent to
   \(D\), every \(b_i\) has a neighbour in \(D\), and

   \[
                             N_H(D)=S\cup\{q\}.           \tag{1.3}
   \]

   This outcome without outcome 2 is possible only when \(R=\{q\}\).
   In particular, if \(R-\{q\}\ne\varnothing\), only outcomes 1 and 2
   occur.

#### Proof

Let \(D\) be a component of \(B-V(R)\), and put

\[
 X=N_R(D),\qquad
 Y=N_S(D).                                               \tag{1.4}
\]

The set \(X\) is nonempty because \(B\) is connected.  Also

\[
                            N_H(D)=X\cup Y.               \tag{1.5}
\]

Since \(R\ne\varnothing\), the set \(D\) is a proper nonempty shore of
\(H\).  If \(V(H)-(D\cup X\cup Y)\ne\varnothing\), then \(X\cup Y\)
is a vertex cut, and the \(r\)-connectivity of \(H\) gives

\[
                            |X|+|Y|\ge r.                 \tag{1.6}
\]

If the displayed complement is empty, then necessarily \(X=R\) and
\(Y=S\); because \(X\ne\varnothing\) and \(|S|=r-1\), the same inequality
holds.  Thus (1.6) is valid in either case.

If \(|X|\ge2\), choose distinct \(x,x'\in X\).  Connectedness of \(D\)
gives an \(x\)-to-\(x'\) path with all internal vertices in \(D\), which
is outcome 1.

We may therefore assume that every component of \(B-V(R)\) has exactly
one neighbour in \(R\).  Equation (1.6), together with
\(|S|=r-1\), then forces

\[
                              Y=S                         \tag{1.7}
\]

for every such component: every hanging component is adjacent to every
singleton bag.

Suppose there are two distinct components \(D_1,D_2\).  The set \(D_1\)
is connected.  Its complement inside \(B\),

\[
                              B-D_1,                     \tag{1.8}
\]

is also connected: it contains the connected core \(R\), and every other
component of \(B-V(R)\) attaches to \(R\).  The two sets in (1.8) are
adjacent through the unique attachment edge of \(D_1\), and both are
adjacent to every vertex of \(S\), the first by (1.7) and the second
because it contains \(D_2\).  Consequently

\[
                  D_1,\quad B-D_1,\quad
                  \{b_1\},\ldots,\{b_{r-1}\}             \tag{1.9}
\]

are \(r+1\) pairwise adjacent connected branch sets.  This is outcome 2.

It remains that \(B-V(R)\) has one component \(D\).  Its unique
attachment set is \(X=\{q\}\), and (1.7) gives (1.3).  This is outcome 3.
If \(R\) meets every singleton bag, then

\[
                  D,\quad R,\quad
                  \{b_1\},\ldots,\{b_{r-1}\}             \tag{1.10}
\]

are again \(r+1\) pairwise adjacent connected branch sets.  Thus absence
of outcome 2 forces some \(P_i=N_B(b_i)\) to miss \(R\), and because
\(B=R\mathbin{\dot\cup}D\), that portal class is wholly owned by \(D\).

Suppose now that \(R-\{q\}\ne\varnothing\).  For such an index \(i\), set

\[
                           C=(S-\{b_i\})\cup\{q\}.        \tag{1.11}
\]

The set \(C\) has order \(r-1\).  In \(H-C\), the set
\(D\cup\{b_i\}\) is connected because \(D\sim b_i\), and it has no edge
to the nonempty set \(R-\{q\}\): the unique \(D\)-to-\(R\) attachment
was \(q\), while \(b_i\) has no neighbour in \(R\).  Thus \(C\)
disconnects \(H\), contrary to \(r\)-connectivity.  Hence \(R\) meets
every singleton bag, and (1.10) gives outcome 2.  Therefore outcome 3
without outcome 2 forces \(R=\{q\}\).
\(\square\)

## 2. The rooted-model principle

The theorem turns an arbitrary portal-bearing hanging society with a
nontrivial core into one of two typed objects:

\[
\boxed{\text{clean exchange ear}\quad\text{or}\quad
       K_{r+1}\text{-model}.}
\tag{2.1}
\]

For a hypothetical \(HC_7\) counterexample, \(r=6\) and
\(H=G-v\) is six-connected.  Hence a proper minimal core in the spanning
one-complex-bag model either admits a clean ear or already gives the
\(K_7\)-minor.  A genuine uncolourable core cannot consist of one vertex
when every list contains the contraction colour, so the degenerate
\(R=\{q\}\) exception never occurs in that application.

## 3. Exact boundary

The theorem does not by itself show that a clean ear can replace part of
the minimal list core while preserving its obstruction.  That is the sole
dynamic step still required in this spanning singleton proper-core cell.

What it rules out completely is diffuse hanging complexity: in the
absence of an exchange ear, two hanging components are already too many,
and a sole one-attachment component is also impossible unless the core is
the attachment vertex itself.

## 4. Iterated consequence: the whole bag is an ear closure

### Corollary 4.1 (relative ear saturation)

Let (C_0\subseteq B) be any connected vertex set of order at least two.
Then either (H) contains the (K_{r+1})-minor in Theorem 1.1, or there is
a finite chain

\[
 C_0\subsetneq C_1\subsetneq\cdots\subsetneq C_m=V(B) \tag{4.1}
\]

such that, for every (t<m), the difference
(C_{t+1}-C_t) is one component of (B-C_t) and has at least two
distinct neighbours in (C_t).

#### Proof

Apply Theorem 1.1 to the connected induced subgraph (B[C_t]).  It has at
least two vertices, so the degenerate one-vertex outcome is unavailable.
If the target minor is not obtained and (C_t\ne V(B)), outcome 1 supplies
a component (D_t) of (B-C_t) with two attachments.  Put

\[
                         C_{t+1}=C_t\cup V(D_t).
\]

The new induced subgraph is connected and has strictly more vertices.
Finiteness makes the process terminate, and the only non-minor terminal
state is (C_m=V(B)). \(\square\)

Starting with a genuine minimal contraction core (R), every target-free
spanning bag is therefore its **relative ear closure**.  Portal-bearing
hanging societies cannot remain pendant owners; each is eventually joined
to the earlier core at two distinct vertices.  The remaining exchange
problem is to orient these ears among the branch pieces produced by the
full-core theorem while preserving all singleton labels.

### Corollary 4.2 (the complex bag is 2-connected)

If \(H\) has no \(K_{r+1}\)-minor of the form in Theorem 1.1 and
\(|B|\ge3\), then \(B\) has no cutvertex.

#### Proof

Suppose that \(q\) is a cutvertex and let \(D\) be one component of
\(B-q\).  Put \(R=B-D\).  Then \(R\) is a connected induced proper
subgraph, contains \(q\) and at least one vertex of a second component of
\(B-q\), and \(D\) has the unique attachment \(q\) in \(R\).  Thus the
clean-ear outcome of Theorem 1.1 is unavailable.  The degenerate
\(R=\{q\}\) outcome is also unavailable.  The theorem therefore supplies
the target minor, contrary to the hypothesis. \(\square\)

This is stronger than an ear chain chosen from one particular core:
pendant portal societies are impossible relative to **every** connected
induced side.  Hence all remaining exchange difficulty is confined to
2-connected owner blocks, exactly as predicted by the binary transit
theorem.

### Corollary 4.3 (every hanging terminal lies on a core ear)

Assume the target minor is absent, let \(R\subsetneq B\) be connected
with at least two vertices, and let \(z\in B-R\).  There is an \(R\)-path
whose internal vertices lie in \(B-R\) and whose interior contains \(z\).
In particular, every foot and every singleton portal outside a selected
core can be brought onto an individually prescribed clean core ear.

#### Proof

By Corollary 4.2, \(B\) is 2-connected.  The fan lemma gives two internally
vertex-disjoint paths from \(z\) to the vertex set \(R\), with distinct
ends in \(R\), chosen to have no other vertices in \(R\).  Their union is
the required \(R\)-path through \(z\). \(\square\)

The qualification “individually” is essential: 2-connectivity alone does
not give pairwise disjoint ears through an arbitrary collection of
terminals.  The next exchange theorem must use the minor-critical state
of the core to synchronize these individually available portal ears.

## 5. The terminal bag is 2-connected

### Theorem 5.1 (cutvertex elimination)

If (H) has no (K_{r+1})-minor, then the spanning complex bag (B=H-S)
is 2-connected.  Moreover every singleton bag has at least two distinct
portals in (B):

\[
                             |N_B(b_i)|\ge2
                         \qquad(1\le i\le r-1).          \tag{5.1}
\]

#### Proof

Suppose (q) is a cutvertex of (B), and let (D) be a component of
(B-q).  Since another component of (B-q) is nonempty,

\[
                         N_H(D)\subseteq S\cup\{q\}
\]

is a vertex cut.  Its order is at most (r), and (r)-connectivity forces

\[
                              N_S(D)=S.                  \tag{5.2}
\]

This holds for every component of (B-q).  Choose one component (D).
The set (B-D) is connected, contains (q) and at least one other
component, and is adjacent to (D).  By (5.2), both (D) and (B-D) are
adjacent to every singleton in (S).  Therefore

\[
                         D,\quad B-D,\quad \{b_i\}
                         \ (1\le i\le r-1)
\]

are the (r+1) branch sets of a clique model, a contradiction.  Hence
(B) has no cutvertex.

Finally, the neighbours of (b_i) outside (B) are the (r-2) other
vertices of the clique (S).  Since an (r)-connected graph has minimum
degree at least (r), (b_i) has at least two neighbours in (B).  This
is (5.1).

It remains only to justify the order convention in the word
``2-connected''.  The complex bag is nontrivial, so \(|B|\ge2\).  If
\(|B|=2\), connectedness makes its two vertices adjacent, while (5.1)
makes every singleton \(b_i\) adjacent to both of them.  Together with
the clique \(S\), these vertices induce a \(K_{r+1}\), again a
contradiction.  Thus \(|B|\ge3\); combined with the absence of a
cutvertex, this proves that \(B\) is 2-connected. \(\square\)

Thus the ear alternative does not lead to arbitrary repeated hanging
casework.  Its finite terminal object is one 2-connected society with
(r-1) labelled portal classes, each of multiplicity at least two.  The
remaining rooted-model question is exactly whether operation-critical
states force a connected bipartition of this society meeting every portal
class on both sides; the suspended-octahedron examples show that
2-connectivity and portal multiplicity alone do not suffice.

## 6. Two portal classes always synchronize

There is a sharp static base theorem for the synchronization problem.

### Lemma 6.1 (two-class connected splitter)

Let \(J\) be a 2-connected graph and let \(P,Q\subseteq V(J)\), with
\(|P|,|Q|\ge2\).  There is a partition

\[
                              V(J)=A\mathbin{\dot\cup}D \tag{6.1}
\]

such that \(J[A]\) and \(J[D]\) are connected and each of \(A,D\) meets
both \(P\) and \(Q\).

#### Proof

Choose distinct \(s,t\in P\), add the edge \(st\) if it is absent, and
take an \(st\)-numbering

\[
                         s=x_1,x_2,\ldots,x_n=t          \tag{6.2}
\]

of the resulting 2-connected graph.  Every internal vertex has a
neighbour of lower index and a neighbour of higher index.  The added edge
has both ends at the extremes, so these predecessor/successor edges are
edges of the original graph \(J\).  Consequently every prefix of (6.2)
induces a connected subgraph of \(J\), as does every suffix.

Let \(a\) and \(b\) be the minimum and maximum indices attained by
vertices of \(Q\).  Since \(|Q|\ge2\), \(a<b\).  Choose
\(a\le k<b\) and put

\[
                         A=\{x_1,\ldots,x_k\},\qquad
                         D=\{x_{k+1},\ldots,x_n\}.       \tag{6.3}
\]

The prefix and suffix are connected.  They contain \(s,t\), respectively,
and hence both meet \(P\); the choice of \(k\) makes both meet \(Q\).
\(\square\)

### Theorem 6.2 (at most two nonuniversal labels close)

In the setting of Theorem 5.1, suppose at most two portal classes
\(P_i=N_B(b_i)\) are proper subsets of \(V(B)\).  Then \(H\) contains a
\(K_{r+1}\)-minor.

#### Proof

By Theorem 5.1, \(B\) is 2-connected and every portal class has at least
two vertices.  Apply Lemma 6.1 to the two nonuniversal classes, repeating
one class if there is only one and using \(V(B)\) if there is none.  Let
\(A,D\) be the resulting connected partition.  Both parts meet the two
selected portal classes, and they meet every universal portal class
automatically.  Since \(B\) is connected, an edge joins \(A\) and \(D\).
Therefore

\[
                         A,\quad D,\quad
                         \{b_1\},\ldots,\{b_{r-1}\}      \tag{6.4}
\]

are \(r+1\) pairwise adjacent connected branch sets. \(\square\)

Thus any target-free one-complex/singleton cell has at least three
genuinely nonuniversal labels.  For every ordinary (non-apex-selected)
label this is equivalent to its colour occurring in some expansion list;
the selected label has the additional foot restriction and is deliberately
not included in that equivalence.  This closes an unbounded family for
every \(r\), and identifies the first possible synchronization obstruction.

### Proposition 6.3 (the suspended octahedron is the sharp static test)

The number three in Theorem 6.2 is best possible under static
connectivity and portal-multiplicity hypotheses.

For \(r=4\), let \(B\) be the triangle on \(x,y,z\), let
\(S=\{b_1,b_2,b_3\}\) be a triangle, and set

\[
 P_1=\{x,y\},\qquad P_2=\{y,z\},\qquad P_3=\{z,x\}.      \tag{6.5}
\]

The resulting graph \(H\) is the octahedron.  It is 4-connected and has
no \(K_5\)-minor, but no connected bipartition of \(B\) meets all three
portal classes on both sides.

For every \(r>4\), join this graph with a clique of order \(r-4\), put
the new universal vertices into \(S\), and give each new singleton the
universal portal class \(V(B)\).  The resulting graph is \(r\)-connected
and has no \(K_{r+1}\)-minor, while the same three-class obstruction
persists.

#### Proof

In (6.5), a bipartition meeting \(P_i\) on both sides must give opposite
colours to the two ends of each of the three edges \(xy,yz,zx\).  This
would 2-colour a triangle, which is impossible.  The displayed six-vertex
graph is \(K_{2,2,2}\), the octahedron; it is 4-connected and planar, so
it has no \(K_5\)-minor.

Universal-clique suspension raises both connectivity and Hadwiger number
by the clique order.  Hence the suspended graph is \(r\)-connected and
still has Hadwiger number at most
\((r-4)+4=r\).  The old three portal constraints are unchanged.
\(\square\)

This example also refutes a purely **laminar-ear** synchronization claim.
Take \(R\) to be one edge of the triangle \(B\).  The remaining vertex
lies on the unique one-vertex \(R\)-ear, so the ear system is as nested
and noncrossing as possible, yet the three portal classes do not split.

### Proposition 6.4 (why the static test is not operation-critical)

The suspended-octahedron society cannot be the unexpandable contraction
core in the present minor-critical argument.

#### Proof

Align the singleton colours as \(p_1,p_2,p_3\), and call the contraction
colour \(\alpha\).  Before the apex restriction, the three expansion lists
on \(x,y,z\) contain, respectively,

\[
                         \{\alpha,p_2\},\qquad
                         \{\alpha,p_3\},\qquad
                         \{\alpha,p_1\}.                 \tag{6.6}
\]

Universal suspension labels occur in none of these lists.  The apex has
one colour \(p_j\).  It can remove the second colour from at most the one
list in (6.6) containing \(p_j\), and only when the corresponding vertex
is a foot.  If no second colour is removed, colour the triangle
\(p_2,p_3,p_1\).  If one is removed, give that vertex \(\alpha\) and give
the other two vertices their two distinct displayed singleton colours.
In either case the lists colour \(B\).

Every induced proper subgraph has the restricted colouring as well.
Thus neither \(B\) nor a subgraph of it is an uncolourable expansion core.
\(\square\)

Proposition 6.4 locates the dynamic hypothesis which any three-or-more
class theorem must actually use: not merely ear nesting, portal
multiplicity, or high connectivity, but the nonextendable contraction
state together with its proper-minor transitions.  The next nontrivial
target is therefore a **three-class operation exchange**.  It must show
that an odd portal constraint cycle either acquires a common edge-operation
state on two shores or supplies an additional connected branch set.

There is a second sharp test: even one nonextendable contraction state is
not enough.

### Proposition 6.5 (the dynamic diamond counterarchitecture)

Let \(r=4\).  Let \(B\) be the diamond on vertices \(0,1,2,3\), with
missing edge \(23\), and let \(S=\{b_1,b_2,b_3\}\) be a clique.  Put

\[
 P_1=\{0,2\},\qquad P_2=\{0,3\},\qquad
 P_3=\{1,2,3\}.                                         \tag{6.7}
\]

Then \(H=B\cup S\) is 4-connected and planar, has no \(K_5\)-minor, and
has no connected bipartition of \(B\) meeting all three classes on both
sides.  Add a vertex \(v\) adjacent precisely to \(0,b_1,b_2\).  Contract
\(B\), align \(b_i\) with colour \(p_i\), and call the fresh colour
\(\alpha\).  The quotient forces \(v\) to colour \(p_3\), and its expansion
lists on \(0,1,2,3\) are

\[
 \{\alpha\},\qquad
 \{\alpha,p_1,p_2\},\qquad
 \{\alpha,p_2\},\qquad
 \{\alpha,p_1\}.                                       \tag{6.8}
\]

These lists do not colour \(B\).  Nevertheless the whole graph \(G\) is
4-colourable (and planar).  Thus

\[
 \boxed{\text{high connectivity + portal multiplicity + one
 unexpandable contraction state}}
\]

does not force the synchronized split or the target minor.

#### Proof

The graph \(H\) is the pentagonal bipyramid: its two apices are \(0,b_3\)
and its equatorial cycle is

\[
                         1,2,b_1,b_2,3,1.
\]

It is a 4-connected planar triangulation.  The three portal constraints
in (6.7) admit no connected split.  One direct check is short.  Splitting
\(\{0,2\}\) and \(\{0,3\}\) puts \(2,3\) on the side opposite \(0\).
To split \(\{1,2,3\}\), vertex \(1\) must lie with \(0\).  But
the resulting bipartition is exactly
\(\{0,1\}\mid\{2,3\}\).  The first side induces the edge \(01\), whereas
\(23\) is the unique missing diamond edge, so the second side is
disconnected.  Interchanging the two sides gives the same obstruction.

After contracting \(B\), its image is adjacent to \(S\cup\{v\}\).
Since \(v\sim b_1,b_2\) and \(v\nsim b_3\), the aligned quotient colour of
\(v\) is \(p_3\).  Formula (6.8) follows from (6.7) and the sole foot
\(0\).  Vertex \(0\) is forced to \(\alpha\); then \(2\) is forced to
\(p_2\), \(3\) to \(p_1\), and their common neighbour \(1\) has no
available colour.  Hence the selected state is unexpandable.

On the other hand, the following is a proper 4-colouring of \(G\):

\[
\begin{array}{c|cccccccc}
 &b_1&b_2&b_3&0&1&2&3&v\\ \hline
\text{colour}&p_1&p_2&p_3&p_3&\alpha&p_2&p_1&\alpha .
\end{array}                                             \tag{6.9}
\]

Geometrically, \(v\) is inserted into the facial triangle
\(0b_1b_2\) of the bipyramid, so \(G\) is planar as well. \(\square\)

The failure in Proposition 6.5 is exact: colouring (6.9) does not descend
through the chosen contraction because \(v\) shares \(\alpha\) with the
non-neighbour \(1\) inside \(B\).  A valid synchronization theorem must
therefore compare several faithful minor operations or use the global
assumption that \(G\) itself is non-\(r\)-colourable.  It cannot be proved
from the selected contraction core alone.

Equivalently, the example fails the first genuine transition axiom in the
strongest possible way.  In a non-\(r\)-colourable graph every
\(r\)-colouring of \(G-e\) gives the two ends of \(e\) one colour; otherwise
it also colours the restored edge.  Colouring (6.9) remains a colouring
after any edge deletion and keeps the deleted ends different.  Hence the
all-edge defect-state family, rather than the single contraction state, is
an explicit dynamic hypothesis which excludes this counterarchitecture.

The exhaustive verifier *verify_three_portal_split.py* checks all labelled
2-connected hosts through five bag vertices, distinguishes Property-B
failures from connectivity-only failures, verifies the 4-connected host
condition, and searches exact branch-set models in the displayed small
graphs.

### Proposition 6.6 (universal portal labels are join factors)

Assume in addition that (G) is a least-parameter, join-prime
counterexample, so every (r)-colouring of (H=G-v) uses every colour
on (N_G(v)).  Then no singleton portal class is universal in (B):

\[
                              P_i\ne V(B)
                         \qquad(1\le i\le r-1).         \tag{6.10}
\]

#### Proof

Suppose (P_i=V(B)).  If (v b_i\notin E(G)), take any proper
(r)-colouring of (H).  The clique (S) has (r-1) distinct
colours.  No vertex of (B) can use the colour of (b_i), since every
such vertex is adjacent to (b_i), and no other vertex of (S) uses
that colour.  Hence this colour occurs on (H) only at (b_i), which is
not a neighbour of (v).  This contradicts neighbourhood saturation.

Thus (v b_i\in E(G)).  The vertex (b_i) is adjacent to (v), to all
of (B), and to every other vertex of the clique (S).  It is therefore
universal in (G), giving the nontrivial join

\[
                              G=K_1\vee(G-b_i),
\]

contrary to join-primality.  This proves (6.10). \(\square\)

So universal portal classes are useful only before the standard join
reduction: each is either ruled out by colour saturation or is a literal
clique join factor.  In the normalized counterexample every singleton
label is genuinely active, and the synchronization theorem must exploit
the all-operation states rather than rely on a large universal-label
reserve.
