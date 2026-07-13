# A counterexample to the universal rainbow-rooted statement \(\mathbf R_7\)

## 1. The statement being refuted

The alternate residual statement \(\mathbf R_7\) asserted:

> If \(H\) is a \(6\)-connected graph with
> \(\chi(H)=\eta(H)=6\), \(c\) is a proper \(6\)-colouring of
> \(H\), and \(x_i\) is a vertex of colour \(i\) for
> \(i=1,\ldots,6\), then \(H\) has a \(K_6\)-model rooted at
> \(x_1,\ldots,x_6\).

Here \(\eta\) denotes the Hadwiger number.  The construction below
disproves this statement.  It does **not** disprove Hadwiger's
Conjecture, and it does not produce a \(7\)-chromatic graph without a
\(K_7\)-minor.

## 2. A labelled near-icosahedron

All subscripts in this section are taken modulo \(5\).  Let \(I\) have
vertices
\[
  t,b,u_0,u_1,u_2,u_3,u_4,w_0,w_1,w_2,w_3,w_4
\]
and the following edges:

* \(tu_i\) and \(bw_i\) for every \(i\);
* \(u_i u_{i+1}\) and \(w_i w_{i+1}\) for every \(i\);
* \(u_iw_i\) and \(u_iw_{i-1}\) for every \(i\).

This is the icosahedral graph.  Put
\[
  F:=I-tu_0.
\]
The two faces of \(I\) incident with \(tu_0\) merge in \(F\), so
\[
  t,u_1,u_0,u_4
\]
occur in this cyclic order on the boundary of one face of \(F\).

### Lemma 2.1.  \(F\) is planar and \(4\)-connected.

**Proof.** Planarity is immediate from the standard icosahedral
embedding.

The icosahedral graph is \(5\)-connected.  For completeness, this can
be checked directly from the displayed description: \(I\) is maximal
planar; its twenty triangles are exactly
\[
 tu_i u_{i+1},\quad bw_iw_{i+1},\quad
 u_i u_{i+1}w_i,\quad u_iw_{i-1}w_i
 \qquad (i\in\mathbb Z_5),
\]
and hence are all facial, and the adjacency description has no induced
\(4\)-cycle.  In a maximal planar graph a separator of order \(3\) is
a separating triangle, while, in the absence of a separating triangle,
a separator of order \(4\) gives a separating chordless \(4\)-cycle.
Thus neither type of separator occurs in \(I\).

Deleting one edge lowers vertex-connectivity by at most one.  Indeed,
if \(G\) is \(k\)-connected and \(G-e-S\) is disconnected for
\(|S|\le k-2\), then the only edge of \(G-S\) between two components
of \(G-e-S\) is \(e=xy\).  Deleting \(S\) together with one of
\(x,y\) separates \(G\) (using the other endpoint when one component
is a singleton), contradicting \(k\)-connectivity.  Consequently
\(\kappa(F)\ge4\).  On the other hand,
\(d_F(t)=d_F(u_0)=4\), so \(\kappa(F)\le\delta(F)=4\).  Hence
\(\kappa(F)=4\). \(\square\)

### Lemma 2.2.  \(\chi(F)=\eta(F)=4\).

**Proof.** The subgraph induced by
\(\{b,w_0,w_1,w_2,w_3,w_4\}\) is the odd wheel with rim \(C_5\),
so it is \(4\)-chromatic.  Since \(F\) is planar, the Four Colour
Theorem gives \(\chi(F)\le4\).  Thus \(\chi(F)=4\).

Planarity gives \(\eta(F)\le4\).  The same odd wheel has the following
\(K_4\)-model:
\[
  \{b\},\qquad \{w_0\},\qquad \{w_1\},\qquad
  \{w_2,w_3,w_4\}.
\]
The last branch set is connected, \(w_0w_1,w_1w_2,w_4w_0\) give
the three required rim adjacencies, and \(b\) is adjacent to every
other branch set.  Hence \(\eta(F)=4\). \(\square\)

### Lemma 2.3.  The facial quadruple is rainbow in a proper
\(4\)-colouring of \(F\).

**Proof.** Define \(c\) by
\[
\begin{array}{c|cccccccccccc}
x&t&b&u_0&u_1&u_2&u_3&u_4&w_0&w_1&w_2&w_3&w_4\\ \hline
c(x)&4&1&3&1&2&1&2&2&3&4&3&4.
\end{array}
\]
Checking the four displayed edge families in the definition of \(I\)
shows that this is a proper colouring of \(F\).  In particular,
\[
  (c(t),c(u_1),c(u_0),c(u_4))=(4,1,3,2),
\]
so the four vertices on the new face have four distinct colours.
\(\square\)

## 3. The six-connected graph

Let \(p,q\) be adjacent new vertices, each complete to \(F\), and set
\[
  H:=K_2\vee F.
\]

### Lemma 3.1.  \(\kappa(H)=6\).

**Proof.** Delete at most five vertices.  If at least one of \(p,q\)
remains, that vertex is adjacent to every other remaining vertex.  If
both are deleted, at most three vertices were deleted from \(F\), and
\(F\) remains connected by Lemma 2.1.  Thus \(H\) is \(6\)-connected.
The vertex \(t\) has degree \(d_F(t)+2=6\) in \(H\), so
\(\kappa(H)\le\delta(H)=6\). \(\square\)

### Lemma 3.2.  \(\chi(H)=\eta(H)=6\).

**Proof.** Chromatic number is additive under joins, so
\[
  \chi(H)=\chi(K_2)+\chi(F)=2+4=6.
\]

Adding one universal vertex raises the Hadwiger number by exactly one.
The lower bound follows by adding the universal singleton to a maximum
clique model.  Conversely, in any clique model either the universal
vertex is unused, or its branch set can be discarded and all remaining
branch sets form a clique model in the old graph.  Applying this fact
twice gives
\[
  \eta(H)=2+\eta(F)=6.
\]
\(\square\)

Extend the colouring in Lemma 2.3 by assigning two new colours to
\(p\) and \(q\).  Then
\[
  X:=\{p,q,t,u_1,u_0,u_4\}
\]
is a rainbow transversal of this proper \(6\)-colouring of \(H\).

## 4. There is no \(K_6\)-model rooted at \(X\)

### Lemma 4.1 (alternating terminals on a face).

Let \(a,b,c,d\) occur in this cyclic order on the boundary of a face
of a plane graph \(P\).  Then \(P\) has no \(K_4\)-model rooted at
\(a,b,c,d\).

**Proof.** Such a model would have disjoint branch sets
\(A,B,C,D\) containing \(a,b,c,d\), respectively.  The adjacency of
\(A\) and \(C\), together with their connectedness, gives an
\(a\)-\(c\) path in \(A\cup C\) plus one edge between the two sets.
Likewise \(B\cup D\) contains a \(b\)-\(d\) path.  These two paths are
vertex-disjoint.  Delete the open face and view the rest of the plane
graph in the complementary closed disc.  The two pairs of endpoints
alternate on the boundary of that disc, so the Jordan curve theorem
forbids two such disjoint paths. \(\square\)

### Theorem 4.2.  \(H\) has no \(K_6\)-model rooted at \(X\).

**Proof.** Suppose such a model exists.  The branch sets rooted at
\(p\) and \(q\) use those two vertices.  Therefore each of the four
branch sets rooted at \(t,u_1,u_0,u_4\) lies wholly in \(F\).  Those
four branch sets are connected in \(F\), are pairwise disjoint, and
are pairwise adjacent by edges of \(F\).  They would be a \(K_4\)-model
in \(F\) rooted at \(t,u_1,u_0,u_4\), contrary to Lemma 4.1 and the
facial order from Section 2. \(\square\)

Lemmas 3.1 and 3.2 and Theorem 4.2 give the promised counterexample to
\(\mathbf R_7\).

The root set \(X\) is not colour-saturating.  Indeed, keep every value
in the table of Lemma 2.3 except change \(c(t)\) from \(4\) to \(3\).
This is still proper because the deleted edge is \(tu_0\), while the
remaining neighbours \(u_1,u_2,u_3,u_4\) of \(t\) have colours
\(1,2,1,2\).  The four facial vertices now have colours
\((3,1,3,2)\).  After giving \(p,q\) their two private colours, only
five colours occur on \(X\).  Consequently, adding a new vertex with
neighbourhood exactly \(X\) does not produce a \(7\)-chromatic graph:
the missing sixth colour extends to that vertex.

## 5. What survives: an exact result for the planar join family

The counterexample shows why being rainbow in one chosen colouring is
too weak.  The condition arising from a genuinely \(7\)-critical apex
extension is stronger: the apex neighbourhood must see every colour in
**every** proper \(6\)-colouring.  For the join family this stronger
condition is enough.

Thus a logically appropriate replacement for universal \(\mathbf R_7\)
would quantify over a *colour-saturating set* \(S\): every proper
\(6\)-colouring of \(H\) uses all six colours on \(S\), and the desired
\(K_6\)-model need only have every branch set meet \(S\).  Taking
\(S=N_G(v)\) is exactly what vertex-criticality supplies in
\(H=G-v\).  The next theorem verifies this corrected statement for the
planar join family.

We use the standard rooted-\(K_4\) theorem of Fabila-Monroy and Wood:
if \(P\) is a \(3\)-connected plane graph and \(a,b,c,d\) are distinct,
then \(P\) has a \(K_4\)-model rooted at them if and only if they are
not all incident with one face.

### Theorem 5.1 (colour-saturating sets root \(K_4\)).

Let \(P\) be a \(4\)-connected planar graph with \(\chi(P)=4\), and
let \(S\subseteq V(P)\).  Suppose that every proper \(4\)-colouring of
\(P\) uses all four colours on \(S\).  Then \(P\) has a \(K_4\)-model
whose four branch sets each meet \(S\).

**Proof.** Fix a proper \(4\)-colouring and choose a rainbow quadruple
\(s_1,s_2,s_3,s_4\in S\).  If they are not cofacial, the rooted-
\(K_4\) theorem finishes the proof.

Otherwise they lie on a face \(f\).  If some \(x\in S\) is not on
\(f\), replace the root having colour \(c(x)\) by \(x\).  The new
rainbow quadruple is not cofacial: a distinct face of a
\(3\)-connected plane graph cannot share three distinct vertices with
\(f\).  The rooted-\(K_4\) theorem again finishes the proof.

It remains that \(S\subseteq V(\partial f)\).  Add a new vertex \(z\)
inside \(f\) adjacent to every vertex of its boundary.  The resulting
graph is planar, so the Four Colour Theorem gives it a proper
\(4\)-colouring.  Every vertex of \(\partial f\), and hence every
vertex of \(S\), avoids the colour of \(z\).  Thus this colouring uses
at most three colours on \(S\), contrary to the hypothesis. \(\square\)

### Corollary 5.2 (the corrected set-rooted statement for joins).

Let \(P\) be as in Theorem 5.1, let \(J=K_2\vee P\), and let
\(S\subseteq V(J)\) meet all six colours in every proper
\(6\)-colouring of \(J\).  Then \(J\) has a \(K_6\)-model every
branch set of which meets \(S\).

**Proof.** Write \(V(K_2)=\{p,q\}\).  The colours on \(p,q\) are
private in every proper \(6\)-colouring of \(J\), so saturation forces
\(p,q\in S\).  Moreover \(S\cap V(P)\) meets all four colours in every
proper \(4\)-colouring of \(P\).  Apply Theorem 5.1 in \(P\), and add
the singleton branch sets \(\{p\},\{q\}\). \(\square\)

### Corollary 5.3 (one-vertex extensions of \(K_2\vee P\)).

Let \(P\) be as in Theorem 5.1, let \(J=K_2\vee P\), and obtain \(G\)
from \(J\) by adding one vertex \(v\) with arbitrary neighbours in
\(J\).  If \(\chi(G)=7\), then \(G\) has a \(K_7\)-minor.

**Proof.** Write \(V(K_2)=\{p,q\}\).  In every proper
\(6\)-colouring of \(J\), \(p,q\) receive two colours used nowhere
else and the restriction to \(P\) is a proper \(4\)-colouring.  If
\(v\) missed either \(p\) or \(q\), its unique colour could be used on
\(v\), so \(vp,vq\in E(G)\).

Put \(S=N_G(v)\cap V(P)\).  If some proper \(4\)-colouring of \(P\)
missed a colour on \(S\), combine it with the two singleton colours on
\(p,q\) and give the missing colour to \(v\), a proper
\(6\)-colouring of \(G\).  Therefore \(S\) satisfies Theorem 5.1.
Take the resulting four branch sets in \(P\).  Together with
\(\{p\},\{q\},\{v\}\) they form a \(K_7\)-model in \(G\). \(\square\)

Thus the planar join family supports the critical-apex implication
needed by Hadwiger even though it refutes the much stronger universal
rainbow-rooted statement \(\mathbf R_7\).

## 6. A valid general replacement target of size at most nine

Call \(S\subseteq V(H)\) **six-colour-saturating** if every proper
\(6\)-colouring of \(H\) uses all six colours on \(S\).

### Proposition 6.1 (the corrected small-set reduction).

If a minimal counterexample \(G\) to \(\mathrm{HC}_7\) exists, there
are a vertex \(v\), the graph \(H=G-v\), and an inclusion-minimal
six-colour-saturating set \(S\subseteq N_G(v)\) such that
\[
 \kappa(H)\ge6,\qquad \chi(H)=\eta(H)=6,
 \qquad 6\le |S|\le9,
\]
and no \(K_6\)-model of \(H\) has every branch set meeting \(S\).

**Proof.** A minor-minimal counterexample is
\(7\)-contraction-critical, hence \(7\)-connected by Mader and has
minimum degree at least \(7\) by Dirac's neighbourhood-independence
bound.  Mader's sharp extremal bound
\(|E(G)|\le5|V(G)|-15\) for \(K_7\)-minor-free graphs gives a vertex
\(v\) of degree at most \(9\).  Thus \(7\le d(v)\le9\), and
\(\kappa(G-v)\ge6\).

Criticality gives \(\chi(H)=6\).  The established \(t=6\) case of
Hadwiger gives a \(K_6\)-minor in \(H\), while a \(K_7\)-minor in
\(H\) would also be one in \(G\); hence \(\eta(H)=6\).

Every proper \(6\)-colouring of \(H\) uses all six colours on
\(N_G(v)\), or the missing colour extends to \(v\).  Choose an
inclusion-minimal saturating subset \(S\) of that neighbourhood.  It
has at least six vertices and at most \(d(v)\le9\).  Finally, a
\(K_6\)-model whose six bags all meet \(S\subseteq N_G(v)\), together
with the singleton branch set \(\{v\}\), is a \(K_7\)-model in
\(G\), which is impossible. \(\square\)

### Lemma 6.2 (essential-colour witnesses).

For every \(s\in S\) in Proposition 6.1 there is a proper
\(6\)-colouring \(c_s\) of \(H\) and a colour \(i_s\) such that
\(s\) is the unique vertex of \(S\) with colour \(i_s\).

**Proof.** Minimality says that \(S-\{s\}\) is not saturating, so
some proper \(6\)-colouring misses a colour \(i_s\) on
\(S-\{s\}\).  Since the same colouring must use all six colours on
\(S\), the vertex \(s\) has colour \(i_s\), uniquely on \(S\).
\(\square\)

### Lemma 6.3 (the size-six case has valid Kempe paths).

If \(|S|=6\), every proper \(6\)-colouring is bijective on \(S\).
For such a colouring, the two vertices of \(S\) with colours \(i\)
and \(j\) lie in the same \((i,j)\)-Kempe component for every
\(i\ne j\).

**Proof.** Saturation and \(|S|=6\) imply bijectivity.  If the two
roots were in different bichromatic components, swap \(i,j\) on the
component containing the colour-\(i\) root.  No other vertex of \(S\)
in that component has colour \(j\), and the colour-\(i\) root was
unique on \(S\).  After the swap colour \(i\) is absent from \(S\),
contrary to saturation. \(\square\)

Accordingly, a sound replacement for \(\mathbf R_7\) is the following
strictly structured statement:

> Every \(6\)-connected graph \(H\) with \(\chi(H)=\eta(H)=6\) and
> an inclusion-minimal six-colour-saturating set \(S\) of order
> \(6,7,8\), or \(9\) has a \(K_6\)-model whose branch sets all meet
> \(S\).

Proposition 6.1 shows that this statement implies \(\mathrm{HC}_7\).
Corollary 5.2 proves it for the structural family
\(H=K_2\vee P\) with \(P\) \(4\)-connected and planar.  The unresolved
case is no longer an arbitrary prescribed-root problem: it is a
set-rooted problem with at most nine terminals and strong witnesses
from Lemma 6.2.

## 7. A complement-degree criterion

For a proper colouring \(c\) and roots in distinct colour classes,
say that two roots are **Kempe-connected** if a path between them uses
only their two colours.

We use the following precise theorem of Kriesell and Mohr (*Kempe
Chains and Rooted Minors*, 2019): every graph each of whose connected
components contains at most one cycle has property \((*)\).  In the
form needed here, if \(M\) is such a graph on a rainbow transversal
\(S\), and the ends of every edge of \(M\) are Kempe-connected, then
there are pairwise disjoint connected bags \((B_s:s\in S)\), with
\(s\in B_s\), such that \(B_s\) and \(B_t\) are adjacent whenever
\(st\in E(M)\).

### Theorem 7.1 (maximum complement degree two).

Let \(c\) be a proper \(k\)-colouring of a graph \(H\), and let
\(S=\{s_1,\ldots,s_k\}\) be rainbow.  Suppose every pair of vertices
of \(S\) is Kempe-connected and
\[
  \Delta\bigl(\overline{H[S]}\bigr)\le2.
\]
Then \(H\) has a \(K_k\)-model rooted at \(S\).

**Proof.** Put \(M:=\overline{H[S]}\).  Every component of \(M\) is
an isolated vertex, a path, or a cycle, so every component has at most
one cycle.  Apply the quoted Kriesell--Mohr theorem to obtain disjoint
connected rooted bags \((B_s:s\in S)\) that are adjacent for every
edge \(st\in E(M)\).

If \(st\notin E(M)\), then \(st\in E(H[S])\), and this root edge
itself joins \(B_s\) and \(B_t\).  Thus every two bags are adjacent,
and they form a rooted \(K_k\)-model. \(\square\)

### Corollary 7.2 (a closed cell of the corrected \(t=7\) target).

In Proposition 6.1, if \(|S|=6\) and
\(\Delta(\overline{H[S]})\le2\), then \(G\) has a \(K_7\)-minor.
Consequently, a counterexample with \(|S|=6\) must satisfy
\[
  \Delta(\overline{H[S]})\ge3.
\]

**Proof.** Lemma 6.3 supplies all pairwise Kempe connections, and
Theorem 7.1 supplies a rooted \(K_6\)-model.  Since every root lies in
\(S\subseteq N_G(v)\), adding \(\{v\}\) gives a \(K_7\)-model.
\(\square\)

### Remark 7.3 (what Dirac's neighbourhood bound does and does not give).

For the minimum-degree vertex \(v\) in Proposition 6.1, Dirac's bound
is
\[
 \alpha(G[N(v)])\le d(v)-5.
\]
If \(d(v)=7\), this says \(\alpha(G[N(v)])\le2\).  Equivalently, the
complement of the neighbourhood is triangle-free.  It does **not**
imply maximum degree at most two: the graph
\[
 G[N(v)]\cong K_3\mathbin{\dot\cup}K_4
\]
satisfies \(\alpha=2\), while its complement is \(K_{3,4}\), of
maximum degree four.  This example also respects the local clique
bound \(\omega(G[N(v)])\le4\): a \(K_5\) in \(N(v)\) would give a
\(K_6\) subgraph with \(v\), and a \(7\)-connected graph containing a
\(K_6\) subgraph has a \(K_7\)-minor by contracting the connected
complement of that \(K_6\).

There is nevertheless a useful residual description when \(d(v)=7\).
For every \(x\in N(v)\), its non-neighbours inside \(N(v)\) form a
clique (otherwise \(x\) and two nonadjacent non-neighbours form an
independent triple).  The local clique bound makes that clique have
order at most four.  Hence, in the size-six cell not settled by
Corollary 7.2, a vertex has exactly three or four non-neighbours in
\(S\), and those non-neighbours form a clique.  Eliminating these
\(\Delta=3,4\) configurations requires information beyond Dirac's
independence inequality.
