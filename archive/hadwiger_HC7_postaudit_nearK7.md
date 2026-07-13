# Post-audit \(\mathrm{HC}_7\) reduction: full-neighbourhood saturation and near-\(K_7\) obstructions

This note records only statements that survive the minor/colouring audit.  Its
standing object is a minor-minimal counterexample \(G\) to
\(\mathrm{HC}_7\).  Thus
\[
 \chi(G)=7,\qquad \eta(G)=6,
\]
every proper minor of \(G\) is 6-colourable, \(G\) is 7-connected, and
\(7\leq\delta(G)\leq 9\).  The upper bound follows from Mader's sharp
\(K_7\)-minor extremal bound.

The new external input used below is the theorem of Norin--Totschnig (2025):

> Every non-6-colourable graph contains \(K_7^\vee\) as a minor, where
> \(K_7^\vee\) is obtained from \(K_7\) by deleting two edges with a common
> end.

## 1. The saturating set is the whole neighbourhood

Let \(v\in V(G)\), put \(H=G-v\), and write \(S=N_G(v)\).

### Lemma 1.1 (contraction witnesses)

The set \(S\) is an inclusion-minimal six-colour-saturating set in \(H\).
More precisely, for every \(s\in S\) there is a proper 6-colouring \(c_s\)
of \(H\) such that
\[
 c_s(s)\notin c_s(S-\{s\}).
\]

#### Proof

Every proper 6-colouring of \(H\) uses all six colours on \(S\), since a
missing colour could be assigned to \(v\).

Fix \(s\in S\).  Since \(G\) is contraction-critical, \(G/vs\) has a
proper 6-colouring.  Denote the contracted vertex by \(q\).  Delete \(q\),
restore \(s\), and give \(s\) the colour of \(q\); retain the colours of all
other vertices.  This is a proper colouring of \(H\): every neighbour of
\(s\) in \(H\) was a neighbour of \(q\) in \(G/vs\).  On the other hand,
for every \(x\in S-\{s\}\), the edge \(vx\) becomes the edge \(qx\), so
\(c_s(x)\ne c_s(s)\).  Hence \(S-\{s\}\) is not saturating.  This holds for
every \(s\), proving inclusion-minimality. \(\square\)

An immediate but important correction follows.

### Corollary 1.2 (the old size-six cell is not CE-derived)

No proper subset of \(N_G(v)\) is six-colour-saturating in \(G-v\).  In
particular, if \(v\) is chosen with \(7\leq d(v)\leq9\), the minimal
saturating set arising from the counterexample has order \(7,8\), or \(9\),
never 6.

For later finite case work, the witnesses have fixed multiplicity patterns.
After naming the unique colour of \(s\) first, the multiplicities of the
other five colours on \(S-\{s\}\) are
\[
\begin{array}{c|c}
|S|&\text{possible multiplicities}\ \\\hline
7&(2,1,1,1,1),\\
8&(3,1,1,1,1)\text{ or }(2,2,1,1,1),\\
9&(4,1,1,1,1),\ (3,2,1,1,1),\text{ or }(2,2,2,1,1).
\end{array}
\]
This is just saturation plus Lemma 1.1, but it is stronger data than the
existence of an arbitrary minimal saturating set.

Thus the \(|S|=6\) complement cases \(\Delta=3,4\) in the earlier corrected
set-rooted target are genuine cases of a stronger universal statement, but
they are not cases produced by a minor-minimal counterexample to
\(\mathrm{HC}_7\).

### Proposition 1.3 (sharpened small-neighbourhood reduction)

If a counterexample to \(\mathrm{HC}_7\) exists, then there are \(G,v,H,S\)
such that
\[
\begin{gathered}
 G=H+v,\quad S=N_G(v),\quad 7\leq |S|=d_G(v)\leq9,\\
 \kappa(G)\geq7,\quad \kappa(H)\geq6,\quad
 \chi(H)=\eta(H)=6,
\end{gathered}
\]
\(S\) is inclusion-minimal six-colour-saturating with the contraction
witnesses of Lemma 1.1, and no \(K_6\)-model of \(H\) has every bag meeting
\(S\).

#### Proof

Choose a minimum-degree vertex \(v\).  All assertions except the strengthened
minimality and the equality \(S=N(v)\) are the standard minimal-counterexample
reduction: \(\kappa(G)\geq7\), deletion of \(v\) lowers connectivity by at
most one, \(\chi(H)=6\), and the known \(t=6\) case gives \(\eta(H)=6\).
Lemma 1.1 gives the strengthened assertion.  Finally, a \(K_6\)-model whose
six bags all meet \(S=N(v)\), together with the singleton bag \(\{v\}\),
would be a \(K_7\)-model. \(\square\)

The condition that \(H+v\) is a 7-connected, 7-contraction-critical,
\(K_7\)-minor-free extension is essential data.  Dropping it gives a
special case of Holroyd's Strong Hadwiger Conjecture for six colours, not an
equivalent reformulation of the CE reduction.

## 2. Extra information in the degree-seven case

Assume in this section that \(d(v)=7\), and continue to put
\(H=G-v\), \(S=N(v)\).

### Lemma 2.1 (five unique colours and a repeated pair)

In every proper 6-colouring of \(H\), exactly one colour occurs twice on
\(S\), and each other colour occurs once.  Let \(a,b\in S\) be the repeated
pair and let \(U=S-\{a,b\}\).  Then:

1. every two vertices of \(U\) are Kempe-connected in their two colours;
2. for every \(x\in U\), the bichromatic component in the colours
   \(c(x),c(a)\) that contains \(x\) contains at least one of \(a,b\).

#### Proof

Saturation and \(|S|=7\) give the stated multiplicities.  If two unique-colour
vertices \(x,y\) were in different bichromatic components, swapping their
two colours on the component containing \(x\) would remove the unique colour
of \(x\) from \(S\), contradicting saturation.  The same swap argument with
the repeated colour proves (2): if the component containing \(x\) contained
neither \(a\) nor \(b\), the unique colour of \(x\) would disappear from
\(S\). \(\square\)

For \(r\in\{a,b\}\), let
\[
 U_r=\{x\in U:x\text{ is Kempe-connected to }r\}.
\]
Then \(U_a\cup U_b=U\).  If \(U_r=U\) for one repeated vertex \(r\), the
rainbow set \(U\cup\{r\}\) is pairwise Kempe-connected.  Consequently the
Kriesell--Mohr pseudoforest criterion closes this subcase whenever
\[
 \Delta\bigl(\overline{H[U\cup\{r\}]}\bigr)\leq2.
\]
A surviving colouring must therefore have a genuine split
\(U_a\ne U\ne U_b\), or fail the displayed complement bound for every
repeated representative that covers all of \(U\).

## 3. Components beyond a degree-seven closed neighbourhood

Let \({\cal C}\) be the set of components of \(G-N[v]\), and put
\(m=|{\cal C}|\).

### Lemma 3.1 (every exterior component sees the whole neighbourhood)

For every \(C\in{\cal C}\),
\[
 N_G(C)=S.
\]

#### Proof

Certainly \(N(C)\subseteq S\).  If some \(s\in S\) were not in \(N(C)\),
then \(|N(C)|\leq6\), and deleting \(N(C)\) would separate \(C\) from the
still present vertex \(v\), contrary to 7-connectivity. \(\square\)

Contracting a component \(C_i\) therefore gives a helper vertex \(x_i\)
complete to \(S\); helpers from different components are pairwise
nonadjacent.

### Lemma 3.2 (three components force the required model)

If \(m\geq3\), then \(H\) has a \(K_6\)-model every bag of which meets
\(S\), and hence \(G\) has a \(K_7\)-minor.

#### Proof

Dirac's neighbourhood inequality gives \(\alpha(G[S])\leq2\).  By
\(R(3,3)=6\), \(G[S]\) contains a triangle, say on
\(t_1,t_2,t_3\).  Choose distinct
\(a_1,a_2,a_3\in S-\{t_1,t_2,t_3\}\) and distinct exterior components
\(C_1,C_2,C_3\).  The six bags
\[
 \{t_1\},\{t_2\},\{t_3\},
 \quad C_1\cup\{a_1\},C_2\cup\{a_2\},C_3\cup\{a_3\}
\]
are connected and disjoint.  The singleton bags are pairwise adjacent.
Lemma 3.1 makes each component bag adjacent to every singleton bag and to
every other component bag (for example, \(C_i\) has a neighbour
\(a_j\in C_j\cup\{a_j\}\)).  Thus they form the claimed \(K_6\)-model.
\(\square\)

More generally, \(m\) exterior helpers together with a
\(K_{6-m}\) subgraph of \(G[S]\) give an \(S\)-traversing \(K_6\)-model.
In particular, if \(m=2\) and \(G[S]\) contains a \(K_4\), the counterexample
is impossible; if \(m=1\), a \(K_5\) is impossible.  Hence the one-component
cell satisfies \(\omega(G[S])\leq4\).

The case \(m=0\) is also impossible: then \(S=V(H)\), and a \(K_6\)-model
in \(H\) (the known \(t=6\) theorem) is automatically met by \(v\).
Consequently
\[
 1\leq m\leq2. \tag{3.1}
\]

### Lemma 3.3 (a five-vertex \(K_4\)-model closes the two-component case)

Suppose \(m=2\).  If \(G[S]\) has a \(K_4\)-model whose union uses at most
five vertices of \(S\), then \(G\) has a \(K_7\)-minor.

#### Proof

Use the four bags of that model and choose two distinct unused vertices
\(a_1,a_2\in S\) for the bags \(C_1\cup\{a_1\}\) and
\(C_2\cup\{a_2\}\).  Lemma 3.1 supplies all adjacencies involving these
last two bags.  The resulting six bags form an \(S\)-traversing
\(K_6\)-model in \(H\). \(\square\)

There is a sharp elementary description of what remains locally.  The next
finite classification is an **external input**, not proved in this note.  It
is the seven-vertex neighbourhood lemma proved by Kawarabayashi--Toft
([KT05, Section 2]) and invoked in the proof of Norin--Totschnig, Claim 4.4:

> If a graph \(J\) on seven vertices satisfies \(\alpha(J)\leq2\) and has no
> \(K_4\) subgraph, then it contains a spanning Moser spindle.

These are exactly the hypotheses used below: \(|S|=7\), Dirac gives
\(\alpha(G[S])\leq2\), and the two-component helper construction rules out
a \(K_4\) subgraph.

Label the Moser spindle \(M\) by
\[
 V(M)=\{a,b,c,d,e,p,q\}
\]
and
\[
 E(M)=\{ab,ac,bc,bp,cp,ad,ae,de,dq,eq,pq\}.
\]
Thus it consists of the two diamonds on \(\{a,b,c,p\}\) and
\(\{a,d,e,q\}\), with missing edges \(ap,aq\), together with the edge
\(pq\).

### Proposition 3.4 (exact two-component local residual)

If \(m=2\) and the local construction of Lemma 3.3 does not close the
case, then, after relabelling, \(G[S]\) is one of
\[
 G[S]=M
 \quad\text{or}\quad
 G[S]=M+bd,
\]
where \(bd\) may be replaced by any one of the four cross-edges
\(bd,be,cd,ce\).  All four one-cross-edge extensions are isomorphic.

Equivalently, the graph6 codes of the complements of the two residual
graphs are respectively `FBZco` and `Fq?zO`.

#### Proof

By Lemma 3.2 and its \(m=2\) specialization, \(G[S]\) has no \(K_4\)
subgraph.  The Moser-spindle lemma gives a spanning copy of \(M\).

The nonedges of \(M\) fall into three types:
\[
 \{ap,aq\},\qquad
 Y=\{bq,cq,dp,ep\},\qquad
 X=\{bd,be,cd,ce\}.
\]
Adding \(ap\) or \(aq\) creates a \(K_4\) subgraph.  Adding, for example,
\(bq\in Y\) gives the five-vertex \(K_4\)-model
\[
 \{a\},\ \{d\},\ \{e\},\ \{b,q\};
\]
the other members of \(Y\) are symmetric.

Finally, any two edges from \(X\) give a \(K_4\)-model on at most five
vertices.  If they share an end, for example \(bd,be\), then
\(\{a,b,d,e\}\) is a \(K_4\).  If they are disjoint, for example
\(bd,ce\), use
\[
 \{a\},\ \{b\},\ \{c\},\ \{d,e\}.
\]
Lemma 3.3 closes all these cases.  Hence any still-surviving neighbourhood
has at most one cross-edge and no other added edge, and so is one of the two
displayed isomorphism types. \(\square\)

Proposition 3.4 is a reduction, not a claim that the two Moser-spindle
neighbourhoods actually occur in a counterexample.  Eliminating them needs
information internal to the one or two exterior components; contracting
each entire component to a single universal helper loses exactly that
information.

### Proposition 3.5 (the exact Claim 4.4 model and its overlap obstruction)

Use the labelling of the Moser spindle in Norin--Totschnig, Figure 1.  Thus
the seven neighbours of \(v\) are
\[
 u_1,u_2,u_3,u_4,u_5,u'_3,u'_4,
\]
and, after using symmetry, \(u'_3u'_4\notin E(G)\).  Their Claim 4.4
argument applies verbatim to the present 7-contraction-critical graph: in
\(G/vu'_4/vu'_3\), every 6-colouring is rainbow on
\(\{v',u_1,\ldots,u_5\}\), and the Kempe-cycle theorem gives a
\((u_1,\ldots,u_5)\)-rooted \(C_5\)-model
\[
 \mathcal B=(B_1,\ldots,B_5)
 \quad\text{in }G-\{v,u'_3,u'_4\}.
\]
The complementary spindle edges make the five bags pairwise adjacent.
Together with \(\{v\}\) and \(\{u'_3\}\), they form a
\(K_7^\vee\)-model; its only possibly missing pairs are
\[
 \{u'_3\}B_2\quad\text{and}\quad \{u'_3\}B_4.
 \tag{3.2}
\]
(An added cross-edge may already supply one of them.)

If an exterior component \(C\) of \(G-N[v]\) is disjoint from
\(\bigcup_iB_i\), then \(G\) has a \(K_7\)-minor.

#### Proof

The colouring and Kempe-cycle assertions are exactly the proof of
Norin--Totschnig Claim 4.4; that part uses contraction-criticality, not the
assumption that \(K_7^\vee\) is excluded.  The spindle adjacencies visible
in their Figure 1 show that \(u'_3\) is adjacent to the roots
\(u_1,u_3,u_5\), leaving only (3.2).

By Lemma 3.1, \(C\) has neighbours at \(u'_3,u_2,u_4\).  Hence
\(C\cup\{u'_3\}\) is connected and is adjacent to every \(B_i\), including
\(B_2\) and \(B_4\) through the root vertices \(u_2,u_4\).  Replacing
\(\{u'_3\}\) by \(C\cup\{u'_3\}\) therefore upgrades the displayed
near-clique to a \(K_7\)-model. \(\square\)

Consequently, in a counterexample every exterior component must intersect
the union of the five bags of every Claim 4.4 certificate used above.  This
is a genuine strengthening of the two Moser residuals, but it does **not**
eliminate them.  The bags are built from Kempe chains in the whole graph
\(G-\{v,u'_3,u'_4\}\), and those chains may use vertices from every
component of \(G-N[v]\).  If \(C\cap\bigcup_iB_i\ne\varnothing\), absorbing
all of \(C\) into the \(u'_3\)-bag overlaps existing bags and is not a valid
minor operation.  Claim 4.4 contains no avoidance or rerouting assertion
that would leave an exterior component disjoint.  Thus the proposed direct
upgrade fails exactly at branch-set disjointness; proving the required
avoidance/splitting lemma remains additional work.

## 4. What the Norin--Totschnig near-clique gives

Write a \(K_7^\vee\)-model as
\[
 (A,B,C,D_1,D_2,D_3,D_4),
\]
where the only non-required pairs are \(A B\) and \(A C\).  The six bags
\(B,C,D_1,\ldots,D_4\) form a \(K_6\)-model.

### Lemma 4.1 (singleton near-cliques upgrade)

A 7-connected graph containing \(K_7^\vee\) or \(K_7^-\) as a subgraph
contains a \(K_7\)-minor.

#### Proof

Let \(X\) be the seven vertices of the near-clique.  There is a component
\(W\) of \(G-X\): otherwise the deficient vertex has degree at most five,
contrary to 7-connectivity.  Every vertex of \(X\) has a neighbour in
\(W\).  Indeed, if \(x\in X\) did not, then
\(N(W)\subseteq X-\{x\}\), so the at most six vertices \(N(W)\) would
separate \(W\) from \(x\).  Contract \(W\) into the deficient vertex's bag.
This supplies the one or two missing adjacencies and gives a \(K_7\)-model.
\(\square\)

Thus every Norin--Totschnig model in a counterexample has a nontrivial bag.

### Lemma 4.2 (outside-component contact obstruction)

Let \(W\) be a component outside the union of the seven bags of a
\(K_7^\vee\)-model.  Then:

1. \(|N(W)|\geq7\);
2. if \(W\) meets each of \(A,B,C\), then \(G\) has a \(K_7\)-minor;
3. consequently, in a \(K_7\)-minor-free graph the vertices of \(N(W)\)
   lie in at most six bags, and some bag contains at least two distinct
   vertices of \(N(W)\).

#### Proof

If \(|N(W)|\leq6\), deleting \(N(W)\) separates \(W\) from at least one of
the seven nonempty bags, contradicting 7-connectivity.  If \(W\) meets
\(A,B,C\), absorb the connected set \(W\) into \(A\).  The enlarged bag is
connected and becomes adjacent to both \(B\) and \(C\), while retaining all
four required adjacencies to the \(D_i\).  This is a \(K_7\)-model.  Hence
at least one of the three bags is not met by \(W\); pigeonhole applied to at
least seven attachment vertices in at most six bags proves (3). \(\square\)

There is a useful two-way spanning normal form.  Every minor model can be
made spanning by assigning each outside component to an adjacent bag.
Therefore a counterexample furnished by the Norin--Totschnig theorem falls
into one of the following two cases.

* **A \(K_7^-\)-minor exists.**  Take a spanning model and call its unique
  nonadjacent bags \(A,C\).  They are genuinely anticomplete, or the model is
  a \(K_7\)-model.  The open neighbourhood \(N(A)\) is a separator of order
  at least seven and is contained in the other five bags.  Thus one of those
  bags contains at least two attachment vertices of \(A\).

* **No \(K_7^-\)-minor exists.**  In a spanning \(K_7^\vee\)-model both
  pairs \(A B,A C\) are genuinely anticomplete.  Hence \(N(A)\) is a
  separator of order at least seven contained in only
  \(D_1,\ldots,D_4\).  Some \(D_i\) contains at least two attachment
  vertices of \(A\).

This is the precise portal-concentration obstruction left by the near-clique
theorem.  Splitting the multiply hit bag while preserving all clique-model
adjacencies is the missing operation; 7-connectivity alone does not perform
that split.

Finally, if a \(K_7^\vee\)-model lies wholly in \(H=G-v\), its six-bag
clique core cannot have all six bags meet \(S=N(v)\), since then adding
\(\{v\}\) gives a \(K_7\)-model.  This is the exact valid contact conclusion;
the theorem does not allow the near-clique model to be prescribed to avoid
\(v\), nor does it give an arbitrary rooted \(K_6\)-model.

## 5. Remaining gap after this audit

The corrected CE-derived target is Proposition 1.3 with
\(S=N(v)\), \(|S|\in\{7,8,9\}\), and the contraction witnesses of Lemma
1.1.  For a degree-seven vertex the exterior has one or two components; in
the two-component case the only unresolved local neighbourhoods are the
Moser spindle and its one-cross-edge extension from Proposition 3.4.
For those two neighbourhoods, Proposition 3.5 adds that every exterior
component must be entangled with every available Claim 4.4 rooted-cycle
certificate.  A component avoided by one certificate would immediately
upgrade its \(K_7^\vee\)-model to \(K_7\).

Independently, the Norin--Totschnig model can be normalized to the
portal-concentration dichotomy in Section 4.  Upgrading every such model in
a 7-connected contraction-critical graph would prove the missing
\(\mathrm{HC}_7\) case itself, so it cannot be treated as a routine linkage
lemma.  The exact new gap is to use contraction-colouring or internal
component structure to split a multiply hit near-clique bag (or, locally, to
reroute a Claim 4.4 certificate off one of the one/two universal exterior
components) without destroying the other required branch-set adjacencies.

### Source note

`[KT05]` is K. Kawarabayashi and B. Toft, *Any 7-chromatic graph has
\(K_7\) or \(K_{4,4}\) as a minor*, Combinatorica 25 (2005), 327--353.
The seven-vertex Moser-spindle classification is in their Section 2 and is
used explicitly by Norin--Totschnig in the proof of their Claim 4.4.
