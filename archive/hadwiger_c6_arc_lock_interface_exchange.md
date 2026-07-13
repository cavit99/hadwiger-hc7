# From a cyclic arc lock to an interface square

## 1. Purpose

The complementary-arc quotient in
`hadwiger_c6_double_overlap_arc_lock.md` forgets the placement of the
actual interface edges. This note extracts the part of that placement
which follows from connectivity alone and decorates it with the exact
minor-critical colouring transition.

The output is label-free. A strictly surplus interface is either a
four-piece square, on which an interface edge can be deleted without
changing the covering split, or a specific singleton-hub configuration.
In the square case every deletion witness either contains a bichromatic
interface excursion or has its repeated colour locked on the external
exposure of each side.

This does not eliminate the final singleton-hub or
noninterleaving-square residues. It replaces the unstructured phrase
"surplus interface" by two exact geometries.

## 2. Surplus gives a square or a singleton hub

Let \(G\) be \(k\)-connected. Suppose a connected region is partitioned
as

\[
 D=D_1\mathbin{\dot\cup}D_2,
\]

where both parts are nonempty and connected and at least one edge joins
them. Put

\[
 T_i=N_{D_{3-i}}(D_i),\qquad
 L_i=N_G(D_i)-(D_1\cup D_2).                       \tag{2.1}
\]

Thus \(T_i\) is a set of actual interface endpoints and \(L_i\) is the
external exposure of the part. Assume there is a nonempty set beyond
each displayed neighbourhood, as for a split inside one shore of a
full-shore adhesion. Call the split strictly surplus when

\[
 |L_i|+|T_i|\ge k+1\qquad(i=1,2).                 \tag{2.2}
\]

### Theorem 2.1 (interface square or singleton hub)

Under (2.2), one of the following holds.

1. The bipartite interface graph \(E(D_1,D_2)\) has a matching of size
   two. Moreover there are connected partitions

   \[
   D_1=X_1\mathbin{\dot\cup}X_2,\qquad
   D_2=Y_1\mathbin{\dot\cup}Y_2                    \tag{2.3}
   \]

   for which

   \[
   X_1X_2,\quad Y_1Y_2,\quad X_1Y_1,\quad X_2Y_2 \tag{2.4}
   \]

   are all present. Thus the four connected pieces contain a \(C_4\)
   as their adjacency skeleton.
2. After interchanging the two sides, all interface edges have a common
   end \(h\in D_1\), and

   \[
   |L_2|\ge k.                                    \tag{2.5}
   \]

   If additionally \(|L_1|\le k-2\), then

   \[
   D_1=\{h\}.                                     \tag{2.6}
   \]

#### Proof

If the interface has no matching of size two, the size-one case of
Kőnig's theorem says that all its edges have a common end \(h\). Say
\(h\in D_1\). Then \(T_2=\{h\}\), and (2.2) for \(D_2\) gives
\(|L_2|\ge k\).

If \(D_1-h\ne\varnothing\), take a component \(K\) of \(D_1-h\).
Every neighbour of \(K\) outside \(K\) belongs to
\(L_1\cup\{h\}\). This set has order at most \(k-1\) when
\(|L_1|\le k-2\), and separates \(K\) from the region beyond the
split, contrary to \(k\)-connectivity. Hence (2.6) holds.

Otherwise choose independent interface edges
\(p_1q_1,p_2q_2\), with \(p_i\in D_1\) and \(q_i\in D_2\). In \(D_1\),
take a \(p_1\)-\(p_2\) path and split it at one of its edges into two
connected adjacent seeds containing \(p_1,p_2\), respectively. Extend
the two seeds to a connected bipartition of all of \(D_1\): contract
the seeds, take a spanning tree containing the edge between them, and
delete that tree edge. This gives \(X_1,X_2\). The same construction in
\(D_2\) gives \(Y_1,Y_2\). Assign indices so that
\(p_i\in X_i,q_i\in Y_i\). The two matching edges and two internal
partition edges give (2.4). \(\square\)

### Corollary 2.2 (the exact exceptional arc geometry)

In the seven-connected complementary-arc lock, put the optional
external old-arm neighbour into \(L_i\), together with the boundary
contact row of that side. If no nested exact seven-cut occurs,
Proposition 4.1 of the arc-lock note gives (2.2) with \(k=7\).

Consequently every arc lock has an interface square unless one side is
a singleton hub and the external exposure of the other side has order
at least seven. More explicitly:

* in quotient type O, the hub exception can occur only when the common
  roots are consecutive on \(C_6\) and the long row also contains \(z\),
  so the long row is all of \(S\);
* in quotient type A, for consecutive roots the long exposure has order
  at least seven either when it contains the old endpoint (the six cycle
  labels plus the old-arm neighbour) or, if it avoids that endpoint, when
  it contains \(z\); there is one additional possibility when the long
  row contains the old endpoint: at distance two, its five cycle labels,
  \(z\), and the old-arm neighbour give exposure seven.

In every exceptional orientation the common interface end lies in the
short-row side, and that side is a singleton.

#### Proof

The two closed \(a\)-\(b\) arcs have respectively \(d+1\) and
\(7-d\) cycle vertices, where \(d\in\{1,2,3\}\). The vertex \(z\)
contributes at most one to either row, and in type A the old-arm
neighbour contributes one only to the piece containing the old
endpoint. A row plus that optional neighbour can have order at least
seven only in the cases listed. In each listed case the other, short
exposure has order at most five. Theorem 2.1 puts the common interface
end on the short side
and makes that side a singleton. \(\square\)

Thus, except for the listed hub cells, strict surplus cannot be
concentrated at one portal: it produces two independent interface
channels.

If \(D\) was chosen as a minimum fragment of a \(k\)-cut, the strict
inequalities (2.2) are automatic by the atomic-surplus theorem in
`hadwiger_exact_cut_atomic_kernel.md`. Moreover no later outcome may
be a nested exact \(k\)-cut: either side of such a cut would be a
smaller fragment. Thus the square below is the terminal local object,
not one step in an adhesion descent.

### Theorem 2.3 (atomic defect amplifies to an interface matching)

Let \(D=D_1\dot\cup D_2\) be a connected split of a minimum
\(k\)-fragment, and retain the notation \(L_i\) from (2.1). If, for an
integer \(q\ge1\),

\[
 |L_1|,|L_2|\le k-q,                              \tag{2.7}
\]

then the interface graph \(E(D_1,D_2)\) has a matching of size at least
\(q+1\).

#### Proof

Suppose its matching number is \(m\le q\). By Kőnig's theorem it has a
vertex cover \(C\) of order \(m\); put \(C_i=C\cap D_i\). If
\(D_i-C_i\ne\varnothing\), take a component \(K\) of that graph. An
edge from \(K\) to the other side has its other end in \(C_{3-i}\),
because its end in \(D_i\) is not in the cover. Internal neighbours of
\(K\) outside \(K\) lie in \(C_i\). Hence

\[
 N_G(K)\subseteq L_i\cup C,\qquad
 |N_G(K)|\le(k-q)+m\le k.                         \tag{2.8}
\]

An order below \(k\) contradicts \(k\)-connectivity; order \(k\) makes
\(K\) a fragment smaller than \(D\), contradicting atomicity. Thus
\(D_i=C_i\) for both \(i\), so \(D=C\) has only \(m\) vertices. But a
graph on \(m\) vertices has matching number at most
\(\lfloor m/2\rfloor<m\), a contradiction. \(\square\)

For a type O antipodal arc lock with \(z\) in both rows, when its split
shore \(D\) is the chosen minimum fragment, both exposures have order
five. Theorem 2.3 with \(k=7,q=2\) therefore gives

\[
 \nu(E(D_1,D_2))\ge3.                             \tag{2.9}
\]

This conclusion is independent of the colouring witness. In type A the
old-arm neighbour enlarges one exposure, so this particular invocation
only recovers a matching of size two; it must not be promoted to (2.9).

In the type O atom, three
independent interface edges can be extended, on each connected side, to
a partition into three connected rooted pieces: take a spanning tree,
remove two edges of the minimal subtree joining the three roots, and
assign the central vertex when necessary to one of the three parts.
Thus the antipodal atom has a genuine three-rung interface ladder, not
merely the \(C_4\) supplied by Theorem 2.1.

## 3. The square carries a fixed-geometry critical state

Assume now that \(G\) is \(r\)-minor-critical: \(G\) is not
\(r\)-colourable and every proper minor is. Let \(e=xy\) be one of the
two independent interface edges in Theorem 2.1, retaining the other.
The labelled boundary for the state below is
\(L=N_G(D)=L_1\cup L_2\).

### Theorem 3.1 (fixed-split state exchange)

There is an \(r\)-colouring \(c\) of \(G-e\) such that, writing
\(\alpha=c(x)=c(y)\), the state induced by \(c\) on the external
boundary is not extendible over the original \(D\). Deleting \(e\)
changes none of

* the connectedness of \(D_1,D_2\);
* their external contact rows;
* the covering property of those rows; or
* adjacency of \(D_1,D_2\).

Thus the new state is created inside one fixed covering geometry.

#### Proof

The second interface edge remains after deleting \(e\), so every listed
geometric property is unchanged. Colour the proper minor \(G-e\).
Restoring \(e\) would colour \(G\) unless its ends have the same colour,
so \(c(x)=c(y)\). If the induced boundary state extended over the
original \(D\), glue that extension to \(c\) outside \(D\); this would
again colour \(G\). Hence the state is genuinely new. \(\square\)

## 4. Palette lock or a bichromatic interface excursion

For \(\gamma\ne\alpha\), let \(K_i(\gamma)\) be the
\(\alpha/\gamma\)-component of \(G[D]-e\) containing the end of \(e\)
in \(D_i\). Call it an interface excursion if it uses an edge of
\(E(D_1,D_2)-\{e\}\).

### Theorem 4.1 (palette-or-excursion)

Put \(C_i=c(L_i)\), the set of colours appearing on the external
exposure of \(D_i\). For each \(i\in\{1,2\}\), either

1. some \(K_i(\gamma)\) is an interface excursion;
2. \(\alpha\in C_i\); or
3. \(C_i\) contains every one of the other \(r-1\) colours.

In particular, if \(|C_i|\le r-2\), absence of an interface excursion
forces

\[
 \alpha\in C_i.                                   \tag{4.1}
\]

#### Proof

Assume no \(K_i(\gamma)\) is an excursion. It is then contained in
\(D_i\). The edge-critical Kempe argument says that it must be anchored
at the external boundary: otherwise swapping \(\alpha,\gamma\) on that
whole component separates the colours of \(x,y\), after which \(e\)
can be restored. Hence, for every \(\gamma\ne\alpha\), the set \(C_i\)
contains \(\alpha\) or \(\gamma\). If it does not contain \(\alpha\),
it contains every other colour. This proves the trichotomy and (4.1).
\(\square\)

For the six-colour arc lock, a side whose total exposure uses at most
four colours has the exact dichotomy

\[
 \boxed{\text{a second-edge bichromatic excursion}}
 \quad\text{or}\quad
 \boxed{\text{the repeated edge colour is exposed on that arc}.}
 \tag{4.2}
\]

If an excursion component starts on one side and is anchored at a label
exclusive to the other arc, it is already a cross-arc carrier.
Otherwise all anchors remain native.

### Corollary 4.2 (missing colours make a coloured portal fan)

Assume that side \(i\) has no interface excursion and that
\(\alpha\in C_i\). Put

\[
 A_i=\{s\in L_i:c(s)=\alpha\},\qquad
 M_i=[r]-C_i.
\]

For every \(\gamma\in M_i\), some vertex of \(A_i\) has a
\(\gamma\)-coloured neighbour in \(D_i\), and that neighbour lies in
\(K_i(\gamma)\). Consequently

\[
 \max_{s\in A_i}
 \bigl|\{c(u):u\in N_{D_i}(s),\ c(u)\in M_i\}\bigr|
 \ \ge\
 \left\lceil\frac{|M_i|}{|A_i|}\right\rceil .      \tag{4.3}
\]

In particular, if the repeated colour has a unique external
representative on the side, that portal sees every colour absent from
the side exposure.

#### Proof

Fix \(\gamma\in M_i\). The component \(K_i(\gamma)\) must be externally
anchored. No external vertex has colour \(\gamma\), by the definition
of \(M_i\), so an anchoring vertex has colour \(\alpha\) and belongs to
\(A_i\). Its neighbour in the bichromatic component has colour
\(\gamma\), since adjacent vertices cannot both have colour \(\alpha\).
This proves the first assertion. Assign each missing colour to one such
anchor and apply the pigeonhole principle. \(\square\)

### Theorem 4.3 (full Kempe path decomposition)

For every \(\gamma\ne\alpha\), one of the following occurs.

1. There is an \(\alpha/\gamma\) \(x\)-\(y\) path in \(G-e\) using an
   edge of \(E(D_1,D_2)-\{e\}\).
2. There are \(s_\gamma\in L_1,t_\gamma\in L_2\) and an
   \(\alpha/\gamma\) path \(R_\gamma\) from \(s_\gamma\) to
   \(t_\gamma\) whose internal vertices avoid \(D\).

For distinct colours \(\gamma,\delta\), paths \(R_\gamma,R_\delta\)
can intersect only in vertices of colour \(\alpha\).

#### Proof

The full edge-critical Kempe fact says that \(x,y\) lie in one
\(\alpha/\gamma\) component of \(G-e\): otherwise swap that component
at \(x\) and restore \(e\). Choose a simple \(x\)-\(y\) path in the
component. If it uses another interface edge, outcome 1 holds.
Otherwise it must leave \(D\) in passing from \(D_1\) to \(D_2\).
Take its last exit from \(D_1\) before its first subsequent entry into
\(D_2\). The intervening subpath gives outcome 2. A common vertex of an
\(\alpha/\gamma\) and an \(\alpha/\delta\) path has colour in
\(\{\alpha,\gamma\}\cap\{\alpha,\delta\}=\{\alpha\}\). \(\square\)

Thus failure of a second interface route does not leave an abstract
state: it produces five colour-labelled connectors across the two
exposures. Their only possible mutual overlap is an
\(\alpha\)-coloured bottleneck.

### Corollary 4.4 (the sole alpha-absent two-sided lock in type O)

Consider quotient type O, with no old-arm exposure, and suppose
\(\alpha\) occurs on neither complementary arc row. If neither side has
an interface excursion, then the roots are antipodal, \(z\) belongs to
both rows, and, up to a dihedral symmetry and a colour permutation, the
boundary state is

\[
 (c(c_0),\ldots,c(c_5),c(z))
   =(0,1,2,3,1,2,4),\qquad \alpha=5,              \tag{4.4}
\]

or the state obtained by interchanging the colours on \(c_4,c_5\).
In the first state the two repeated-colour pairs are

\[
 c_1c_4,\qquad c_2c_5,                            \tag{4.5}
\]

and these pairs alternate around \(C_6\). In the second state the pairs
are \(c_1c_5,c_2c_4\), the unique nested alternative.

For each repeated pair, Theorem 4.3 gives either an internal interface
route or a connector outside \(D\) with exactly those boundary ends. In
the first state, two vertex-disjoint outside connectors give the
required alternating carriers. If they do not exist, the Two Paths
Theorem puts the outside four-terminal graph in its web outcome; all
overlap between the two colour-specific witness connectors is confined
to \(\alpha\)-vertices. The second state is the exact monotone
alpha-absent residue; boundary-state analysis alone does not turn its
nested connectors into a crossing.

#### Proof

With no excursion and no exposed \(\alpha\), Theorem 4.1 makes each row
contain all five other colours. Hence each row has at least five
vertices. Two complementary closed arcs of \(C_6\), with optional
copies of \(z\), can both have order at least five only when the roots
are antipodal and \(z\) belongs to both.

Each row now has exactly five vertices and therefore displays the five
colours bijectively. In particular the common vertices \(c_0,c_3,z\)
receive three distinct colours. The remaining two colours must each
occur once on \(\{c_1,c_2\}\) and once on
\(\{c_4,c_5\}\). Properness on the cycle forbids equal colours on
\(c_1c_2\) and on \(c_4c_5\), leaving exactly the two states in (4.4).
This proves the two listed pairings.

For the web assertion, form the graph outside \(D\) after deleting the
other three boundary labels \(c_0,c_3,z\). If a set of at most three
vertices separated a terminal-free component, that component would be
separated in \(G\) by those vertices together with
\(\{c_0,c_3,z\}\), a set of order at most six. Seven-connectivity
forbids this. The bare-web consequence of the Two Paths Theorem
therefore applies whenever the two demanded paths do not exist.
\(\square\)

### Lemma 4.5 (one clean cross-arc connector repairs the quotient)

In either helper geometry O or A, take antipodal roots
\(c_0,c_3\), put \(z\) in both rows, and let

\[
 N_S(D_1)=\{c_0,c_1,c_2,c_3,z\},\qquad
 N_S(D_2)=\{c_0,c_3,c_4,c_5,z\}.
\tag{4.6}
\]

Let \(F_1,F_2\) denote the two connected full helper branch sets used
in the corresponding quotient O or A. If a connected subgraph \(R\),
disjoint from \(S\cup D\cup F_1\cup F_2\), has a neighbour at one
label of
\(\{c_1,c_2\}\) and one label of \(\{c_4,c_5\}\), then \(G\)
contains a \(K_7\)-minor.

We call such a connector **clean**; in particular none of its internal
support is a boundary label or a vertex already reserved by a helper
bag.

#### Certified proof

Contract the five pairwise disjoint connected sets
\(R,D_1,D_2,F_1,F_2\) to their respective helpers and delete all
surplus contacts. There are two helper geometries and four conservative
cross-arc pairs. Every one of the eight quotients has an explicit
seven-bag model. The disjointness hypothesis is essential: without it,
the quotient would use one original branch set twice.

The dependency-free verifier
`c6_arc_cross_connector_verify.py` reconstructs all eight graphs and
checks bag disjointness, connectivity, and all twenty-one bag
adjacencies. It does not call a minor solver. \(\square\)

### Corollary 4.6 (clean alpha-absent alternative)

In either alpha-absent state of Corollary 4.4, assume \(G\) is
\(K_7\)-minor-free. Let \(\gamma_1,\gamma_2\) be the two colours
repeated once in each exclusive arc. For each \(i\), either

1. an \(\alpha/\gamma_i\) path uses an interface edge other than \(e\);
   or
2. every outside connector supplied for that colour meets
   \(F_1\cup F_2\).

If outcome 1 occurs for both colours, then
\(E(D_1,D_2)-\{e\}\) contains distinct edges \(f_1,f_2\) whose
endpoint-colour pairs are

\[
 \{\alpha,\gamma_1\},\qquad
 \{\alpha,\gamma_2\}.                              \tag{4.7}
\]

Thus the alpha-absent residue is either a three-edge coloured interface
lock or a **dirty helper-core lock**. A bare outside web disjoint from
the reserved helpers is eliminated, but an arbitrary Kempe connector
may not be declared clean.

#### Proof

An outside connector for either repeated colour has ends at the unique
boundary occurrences of that colour, one in each exclusive arc. If it
avoids \(F_1\cup F_2\), Lemma 4.5 gives a \(K_7\)-minor. Otherwise it
is dirty, giving outcome 2. If it is not outside, Theorem 4.3 gives
outcome 1. An interface edge on an
\(\alpha/\gamma_i\) path has endpoint colours
\(\alpha,\gamma_i\), and the two selected edges are distinct because
\(\gamma_1\ne\gamma_2\). \(\square\)

### Lemma 4.7 (a clean long common-root connector is positive)

Keep the antipodal rows (4.6). In either helper geometry, a connected
subgraph disjoint from \(S\cup D\cup F_1\cup F_2\) and having
neighbours at both labels of one of

\[
 \{c_0,c_2\},\quad\{c_0,c_4\},\quad
 \{c_3,c_1\},\quad\{c_3,c_5\}                    \tag{4.8}
\]

forces a \(K_7\)-minor.

#### Proof

Contract the subgraph to \(h\) as in Lemma 4.5. The four pairs in
(4.8), in both helper geometries, are the additional eight explicit
models checked by `c6_arc_cross_connector_verify.py`. \(\square\)

Thus a \(K_7\)-free **clean** connector caught at a common cycle root
can only run to a cycle neighbour of that root:

\[
 c_0\longleftrightarrow\{c_1,c_5\},\qquad
 c_3\longleftrightarrow\{c_2,c_4\}.               \tag{4.9}
\]

The common portal \(z\) is not restricted by this one-connector
certificate.

### Corollary 4.8 (clean common-alpha overlap has one orientation)

In the antipodal lock, let \(R,R'\) be clean outside Kempe connectors,
whose noncommon ends lie in opposite exclusive arcs. If their interiors
intersect, then \(G\) has a
\(K_7\)-minor.

Consequently, in a \(K_7\)-minor-free graph:

1. every clean outside connector has a common endpoint, by Lemma 4.5;
2. a clean connector caught at \(c_0\) or \(c_3\) has one of the local
   orientations in (4.9), by Lemma 4.7; and
3. connectors of opposite orientation are internally vertex-disjoint.

If two different colour-connectors use the same common endpoint, that
endpoint has colour \(\alpha\). All connectors sharing an internal
\(\alpha\)-vertex must therefore have their exclusive ends in the same
arc.

#### Proof

The union of the portions of \(R,R'\) from a common internal vertex to
their two exclusive ends is connected, disjoint from
\(D\cup F_1\cup F_2\), and meets one exclusive label of each arc.
Lemma 4.5 applies. The first three
conclusions follow immediately. For the final assertion, a common
endpoint of an \(\alpha/\gamma\) and an
\(\alpha/\delta\) connector has colour in
\(\{\alpha,\gamma\}\cap\{\alpha,\delta\}=\{\alpha\}\); opposite
exclusive ends would contradict the first sentence. \(\square\)

This closes the arbitrary-overlap part of the **clean** common-alpha
residue: clean shared alpha vertices cannot mix the two arc
orientations. Dirty paths meeting a reserved helper core remain.

### Corollary 4.9 (only \(z\) carries a clean multicolour overlap)

No two clean connectors of different non-alpha colours caught at
\(c_0\) or \(c_3\) have a common internal vertex. Hence every genuine
clean multicolour common-alpha overlap is caught at \(z\), has
\(c(z)=\alpha\), and all of its exclusive ends lie in one of
\(\{c_1,c_2\}\), \(\{c_4,c_5\}\). It contains at most two connector
colours.

#### Proof

By (4.9), a connector caught at \(c_0\) has other end \(c_1\) or
\(c_5\). Both are adjacent to \(c_0\), so neither has colour
\(\alpha=c(c_0)\). Its colour therefore uniquely determines the
non-alpha colour of that connector. Two differently coloured
connectors use the two different ends \(c_1,c_5\), hence have opposite
orientations and are internally disjoint by Corollary 4.8. The proof at
\(c_3\) is identical.

At \(z\), every cycle label is adjacent to \(z\), so an exclusive end
again has a non-alpha colour and supports only its own connector colour.
Corollary 4.8 forces all connectors sharing an internal vertex to end in
one exclusive arc, which has only two labels. \(\square\)

The clean first/last-shared-alpha analysis has therefore terminated in
an atomic two-connector object: two \(z\)-to-\(c_i\) Kempe paths with
\(c_i\) in the same exclusive two-set, possibly sharing alpha vertices.
The complementary residual is now stated honestly: a Kempe path meets
one of the reserved helper cores before it becomes a clean connector.

### Lemma 4.10 (detachable dirty-core repair)

Let \(R\) be one of the connector subgraphs used in Lemma 4.5, except
that it may meet \(F_1\cup F_2\). Suppose, for each helper it meets,
there is a connected adjacent partition

\[
 F_j=A_j\dot\cup B_j
\]

such that

1. \(H=(R-(F_1\cup F_2))\cup\bigcup_j A_j\) is connected and retains
   the two prescribed connector contacts;
2. every \(B_j\) is connected, disjoint from \(H\), and retains every
   boundary contact and helper adjacency used for \(F_j\) in the
   corresponding certificate; and
3. the retained \(B_j\)'s are disjoint from \(D_1,D_2\) and from each
   other.

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Use \(H\) for the connector helper in the appropriate archived model
and use \(B_j\) in place of every dirty full helper. Conditions 1--3
give pairwise disjoint connected preimages and retain every conservative
quotient edge. The verification in Lemma 4.5 now lifts verbatim.
\(\square\)

Thus a dirty connector survives only when every first/last passage
through a helper lies in a simultaneous locked core: peeling the passage
would destroy a boundary portal or one of the helper adjacencies needed
by the quotient. This is the exact arc-lock analogue of the detachable
terminal-arm obstruction in `hadwiger_clean_gate_minimal_bypass.md`;
ordinary helper contact is not itself an obstruction.

### Lemma 4.11 (four-label capacity of the nested dirty passage)

Normalize the nested common-root residue by taking the connector ends
(c_1,c_5) around (c_0).  Suppose one reserved helper has been split
into a connected passage (A) and a connected retained helper (B),
where (A) is adjacent to (B), (B) retains every boundary contact
except possibly (c_0), and (A) retains contacts with
(c_5,c_0,c_1).
This is the only one-defect helper pattern not already repaired by the
one-defect quotient census.

In either helper geometry O or A, if (A) also has a boundary contact
at one of

\[
                 c_2,qquad c_3,qquad c_4,       \tag{4.10}
\]

then the quotient contains a (K_7)-minor.  Consequently, in a
(K_7)-minor-free graph every such passage satisfies

\[
                N_S(A)\subseteq
                Z_0:=\{c_5,c_0,c_1,z\}.          \tag{4.11}
\]

After a half-turn, the other possible capacity block is
(Z_3=\{c_2,c_3,c_4,z\}).

#### Certified proof

For each of the three extra contacts in (4.10) and each of the two
helper geometries, contract (A,B,D_1,D_2) and the other full helper
to the corresponding quotient vertices.  The following seven-bag
models use the quotient numbering
(c_i=i,z=6,B=7,F=8,D_1=9,D_2=10,A=11):

\[
\begin{array}{c|c|l}
 &N_S(A)-\{c_0,c_1,c_5\}&\text{seven bags}\\ \hline
O&\{c_2\}&0|1|6|8|5,7|3,9|2,11\\
O&\{c_3\}&0|1|6|8|5,7|2,9|3,11\\
O&\{c_4\}&0|1|6|8|5,7|2,9|3,4,11\\
A&\{c_2\}&0|1|6|8|9|2,11|3,5,7\\
A&\{c_3\}&0|1|6|8|9|3,11|2,5,7\\
A&\{c_4\}&0|1|6|8|9|2,5,7|3,4,11 .
\end{array}
\]

Here commas join vertices within one bag and vertical bars separate
bags.  The dependency-free verifier
`c6_arc_block_capacity_verify.py` reconstructs all six quotients and
checks disjointness, connectivity, and all twenty-one bag adjacencies.
The half-turned assertion follows by symmetry. \(\square\)

The point of Lemma 4.11 is not the six cells themselves.  They identify
an intrinsic **capacity block**: once a passage has the contacts needed
for the nested connector, any contact outside one fixed four-element
block repairs the target minor.

### Theorem 4.12 (block-capacity gate principle)

Let (G) be (k)-connected, let (S\subseteq V(G)), and let (A)
be a nonempty connected set with
(V(G)-(A\cup N_G(A))\ne\varnothing).  Suppose a local target
certificate has the following capacity property for some
(Z\subseteq S):

> if (N_G(A)\cap(S-Z)\ne\varnothing), then the target minor exists.

If the target minor does not exist and
(X=N_G(A)-S), then

\[
                  |X|\ge k-|Z|.                 \tag{4.12}
\]

Moreover:

1. if equality holds in (4.12) and (N_G(A)\cap S=Z), then
   (Z\cup X=N_G(A)) is an exact (k)-vertex adhesion separating
   (A) from the far side;
2. if (A) is a proper subset of a minimum (k)-fragment of (G),
   then
   \[
                  |X|\ge k-|Z|+1.               \tag{4.13}
   \]

#### Proof

In a target-minor-free graph the capacity property gives
(N_G(A)\cap S\subseteq Z).  Since (A) is connected and has a
nonempty far side, (N_G(A)) separates two vertices.  Hence
(k)-connectivity gives

\[
k\le |N_G(A)|=|X|+|N_G(A)\cap S|
             \le |X|+|Z|,
\]

which is (4.12).  Under equality and full contact with (Z), every
inequality displayed above is an equality, so
(N_G(A)=Z\dot\cup X) has order (k), proving part 1.

For part 2, equality in (4.12) would again force
(|N_G(A)|=k).  Because (A) is connected and has a far side, it is
a (k)-fragment.  It is strictly smaller than the chosen minimum
(k)-fragment, a contradiction.  Thus (4.12) is strict, which is
(4.13). \(\square\)

For the present seven-connected problem, Lemma 4.11 and Theorem 4.12
give the promised label-free closure mechanism **for the normalized
one-defect nested passage**.  Its capacity block has order four.
Therefore such a passage behind at most two nonboundary gates is
impossible; three gates force an exact seven-adhesion (and hence force
contact with the whole block); and a passage properly contained in the
selected minimum seven-fragment must have at least four nonboundary
gates.  Thus every one-defect nested fan or bridge arm of gate width at
most two is eliminated simultaneously, without enlarging the (C_6)
atlas.  The only atomic survivor in this class is a four-gate locked
helper core (or, outside the chosen atom, a three-gate exact adhesion
available for colour gluing).  A passage whose retained helper has
additional portal defects is not covered by Lemma 4.11 and remains a
separate portal-lock case.

## 5. Exact limit and the next lemma

Theorems 2.1--4.1 do not justify the stronger assertion that every
bichromatic excursion peels into a positive \(K_7\) model. An excursion
may enter the other side and return through the same portal region while
all boundary anchors remain native. Nor may new states from different
edge deletions be pigeonholed: the same state can be created many times.

Nor does a locked portal core, by itself, force a separator bounded by
the number of portal classes.  For every \(m\), take the
\(m\times3\) grid, let the dirty passage be its middle column, and let
the two portal classes be the entire left and right columns.  Deleting
the passage leaves no connected subgraph meeting both portal classes,
but the \(m\) pairwise vertex-disjoint horizontal row paths show that
every separator between the two classes has order at least \(m\).
Thus the next step must use the edge-deletion/contraction transition
axiom or the ambient exact adhesion; portal incidence and helper
connectivity alone cannot yield the desired small cut.

The remaining local statement is now narrower and reusable.

> **Ordered-square exchange target.** In a \(K_7\)-minor-free cyclic
> arc lock, a fixed-geometry state-critical interface square satisfying
> (4.2) has an alternating pair of portal carriers, unless its
> edge-deletion witness contains a three-edge coloured interface lock
> or its remaining connectors form one clean common-alpha lock or meet a
> reserved helper core.

Inside a minimum fragment there is no nested exact-cut exit.  By the
block-capacity gate principle, every normalized one-defect dirty nested
helper passage in that atom has at least four nonboundary gates; every
one- or two-gate passage in this class has been eliminated, and a
three-gate passage outside the atom is an exact-adhesion case.  The
cross-arc outcome lifts through the existing positive branch-set
certificates. Unlike the original arc-lock question, the remaining
object has a \(C_4\) interface skeleton. In the only alpha-absent
states, every clean outside-web route is eliminated; the exact residual
is two differently coloured retained interface edges, a clean
same-arc two-connector fan, or a dirty helper core with at least four
nonboundary gates.
