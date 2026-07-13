# Rooted portal faces close four-connected and planar three-connected exact-seven thin shores

## 1. Scope and conclusion

Let `G` be a finite simple seven-connected graph.  Let

\[
                 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
                 \qquad |S|=7,                              \tag{1.1}
\]

where `L,R` are nonempty, there are no `LR` edges, `G[L]` is connected,
and every literal vertex of `S` has a neighbour in `L`.  Suppose `R`
contains three pairwise vertex-disjoint connected subgraphs
`P_1,P_2,P_3`, each of which contacts every literal vertex of `S`.

This is exactly the oriented `(nu_L,nu_R)=(1,3)` cell of the audited
exact-seven packet theorem, but the result below does not use
contraction-criticality, thinness of `L`, or any special graph on `S`.

### Theorem 1.1 (four-connected portal-face closure)

If `G[L]` is four-connected, then `G` contains a literal `K_7` minor.

Consequently, in a `K_7`-minor-free graph in the `(1,3)` cell, the thin
shore has vertex-connectivity at most three.  Combined with the audited
thin-shore exchange theorem, every surviving thin shore has

\[
                         \kappa(G[L])\in\{2,3\}.            \tag{1.2}
\]

The proof is a uniform rooted-model principle.  Four-connectivity first
turns every four independent literal portal choices into a rooted `K_4`
or one common portal face.  The rooted outcome lifts through the three
opposite packets to `K_7`; the facial outcome is impossible by one planar
degree count.

## 2. The literal rooted lift

For `s\in S`, put

\[
                         Q_s=N_L(s).                         \tag{2.1}
\]

Form the bipartite portal-incidence graph with left side `S`, right side
`V(L)`, and edge `sx` exactly when `x in Q_s`.  A set of distinct portal
vertices is **independent** when it can be matched to the same number of
distinct literal labels in `S`.

### Lemma 2.1 (four rooted portals lift literally)

Let `x_1,x_2,x_3,x_4` be distinct vertices of `L`, matched to distinct
labels `s_1,s_2,s_3,s_4\in S`, with `x_i\in Q_{s_i}`.  If `L` contains
a `K_4` model rooted at `x_1,x_2,x_3,x_4`, then `G` contains a literal
`K_7` model.

#### Proof

Let `B_i` be the rooted `K_4` bags, with `x_i in B_i`, and enlarge them
to

\[
                         B_i'=B_i\cup\{s_i\}.               \tag{2.2}
\]

The four enlarged bags remain disjoint, connected, and pairwise
adjacent.  Write

\[
                         S-\{s_1,s_2,s_3,s_4\}
                              =\{r_1,r_2,r_3\}.              \tag{2.3}
\]

The other three bags are

\[
                         A_j=P_j\cup\{r_j\}\quad(1\le j\le3).
                                                                    \tag{2.4}
\]

They are disjoint and connected.  They are pairwise adjacent because
`P_i` contacts the other packet's literal anchor.  Every `A_j` is
adjacent to every `B_i'` because `P_j` contacts the literal vertex
`s_i`.  Together (2.2) and (2.4) are seven pairwise adjacent literal
branch sets.  \(\square\)

No packet is identified with a colour class, and no contracted label is
expanded.  The proof uses only literal portal edges and the three
literal opposite-shore packets.

## 3. Seven-connectivity makes every portal usable

### Lemma 3.1 (rank four on every four labels)

For every `A\subseteq S` with `1\le |A|\le4`,

\[
                         \left|\bigcup_{s\in A}Q_s\right|
                              \ge |A|.                       \tag{3.1}
\]

In particular every four literal labels have distinct portal
representatives.

#### Proof

Suppose `U=\bigcup_{s\in A}Q_s` has order at most `|A|-1`.  In the
present theorem `L` has at least five vertices, so `L-U` is nonempty.
(The same argument remains valid for a three-connected `L`: it then has
at least four vertices, while `|U|\le3`.)
Delete

\[
                         Z=U\cup(S-A).                       \tag{3.2}
\]

Then `|Z|\le (|A|-1)+(7-|A|)=6`.  A component of `L-U` has no edge to
`A`, by the definition of `U`; it has no edge to `R` by (1.1); and all
other boundary vertices were deleted.  Hence `Z` separates this
component from the nonempty opposite shore `R`, contradicting
seven-connectivity.  \(\square\)

The next strengthening is the point needed for a *single* facial portal
structure.  Rank four alone would not put an unusable portal occurrence
on the distinguished face.

### Lemma 3.2 (every literal portal occurrence extends)

For every incidence `sx` with `s\in S` and `x\in Q_s`, there are three
other distinct labels and three distinct portal representatives, all
different from `s,x`.  Thus `sx` belongs to a matched portal set of
order four.

#### Proof

Delete `s` on the label side and `x` on the portal side of the incidence
graph.  If the remaining bipartite graph had matching number at most
two, Konig's theorem would give a vertex cover `U_0\cup W_0` of
order at most two, where `U_0\subseteq S-\{s\}` and
`W_0\subseteq V(L)-\{x\}`.  Choose four labels

\[
                         A\subseteq(S-\{s\})-U_0;           \tag{3.3}
\]

this is possible because `6-|U_0|\ge4`.  Since a label in `A` is not in
the cover, all of its portal neighbours other than possibly `x` lie in
`W_0`.  Therefore

\[
                         \left|\bigcup_{a\in A}Q_a\right|
                             \le |W_0|+1\le3,               \tag{3.4}
\]

contrary to Lemma 3.1.  Hence the residual matching has order at least
three; adjoining `sx` proves the claim.  \(\square\)

## 4. Rooted `K_4` or one face containing every portal

Let `mathcal B` be the family of four-element independent portal sets.
These are the bases of the rank-four truncation of the transversal
matroid presented by `(Q_s:s\in S)`.  Hence their basis-exchange graph
is connected: two members can be joined by exchanges which change one
portal vertex at a time.  Consecutive four-sets therefore share three
actual vertices.

### Lemma 4.1 (global facial coherence)

Either `G` has a `K_7` minor, or `L` is planar and its unique plane
embedding has one face `F` satisfying

\[
                         \bigcup_{s\in S}Q_s\subseteq V(F). \tag{4.1}
\]

#### Proof

Apply the rooted-`K_4` theorem of Fabila-Monroy and Wood to every member
of `mathcal B` in the four-connected graph `L`.  A rooted model gives
`K_7` by Lemma 2.1.  Assume none exists.  The rooted theorem says that
`L` is planar and that every member of `mathcal B` lies on one face.

Because `L` is three-connected, its plane embedding is unique up to
reflection and two distinct faces share at most two vertices.  Along a
basis-exchange step the two four-sets share three vertices, so their
faces must be the same.  Connectivity of the basis graph gives one face
`F` containing every vertex which occurs in a member of `mathcal B`.
Lemma 3.2 says that every literal portal vertex occurs in such a member,
which proves (4.1).  \(\square\)

This is precisely the SDR facial-coherence mechanism from
`results/hc7_near_k7_active_root_face_exchange.md`, here supplied with
the missing literal Hall and occurrence-coverage arguments forced by
the actual seven-separation.

## 5. The facial outcome violates the planar degree budget

### Lemma 5.1 (no four-connected facial shore)

The facial outcome of Lemma 4.1 is impossible in a seven-connected
host satisfying (1.1).

#### Proof

Take `F` as the outer face of the plane graph `L`, write

\[
                 f=|V(F)|,\qquad h=|V(L)-V(F)|,
                 \qquad n=f+h,\quad m=|E(L)|.             \tag{5.1}
\]

Four-connectivity gives degree at least four *inside `L`* to every
vertex of `F`.  If `z\notin V(F)`, then (4.1) says that `z` has no
neighbour in `S`, while (1.1) says that it has no neighbour in `R`.
Thus all neighbours of `z` lie in `L`.  Seven-connectivity of `G` gives

\[
                         d_L(z)=d_G(z)\ge7.                 \tag{5.2}
\]

Consequently

\[
                         2m\ge4f+7h.                        \tag{5.3}
\]

On the other hand, the outer-face form of Euler's planar bound is

\[
                         m\le3n-3-f,                        \tag{5.4}
\]

because `L` is simple and every bounded face has length at least three.
Equivalently,

\[
                         2m\le4f+6h-6.                      \tag{5.5}
\]

The inequalities (5.3) and (5.5) give `h\le-6`, a contradiction.  This
also covers `h=0`; no separate outerplanar exception is being hidden.
\(\square\)

### Proof of Theorem 1.1

Lemma 4.1 gives a literal `K_7` or the coherent facial outcome.  Lemma
5.1 excludes the latter.  \(\square\)

## 6. Exact new frontier

The theorem eliminates an infinite connectivity class at once.  In the
audited `(1,3)` cell, the earlier thin-shore exchange already proves that
`L` is two-connected.  Theorem 1.1 now proves that it is not
four-connected.  Thus only the following two structural levels remain:

1. `kappa(L)=2`, where every 2-cut has exactly two lobes by the audited
   three-lobe construction; or
2. `kappa(L)=3`, where the three-connected rooted-`K_4` web theorem gives
   either one rural face or a lobe behind three literal gate vertices.

The three gate vertices form a facial triangle in the **web
completion**, but they need not induce a triangle in `L`: the rooted-web
theorem only says that `L` is a spanning subgraph of that completion.

The four-connected case does **not** leave a planar or apex residue: the
planar degree budget closes it completely.  For a three-connected planar
shore the same count only gives

\[
                         3f+7h\le4f+6h-6,
                         \qquad h\le f-6,                  \tag{6.1}
\]

so a genuine rural society can survive.  For a nonplanar
three-connected shore, a web cell has a literal three-vertex gate `T`
and a nonempty component `K` with `N_L(K)=T`; seven-connectivity forces

\[
                         |N_S(K)|\ge4.                      \tag{6.2}
\]

The next exchange must therefore act on a width-two lobe or on this
width-three, at-least-four-label web cell.  Merely repeating the
four-connected argument would ignore the exact place at which its degree
budget loses one unit on each facial vertex.  The following two
propositions record exactly what survives at connectivity three.

### Proposition 6.1 (planar three-connected residue is cubic-rich)

Assume the setup of Theorem 1.1 except that `L` is three-connected and
planar.  If `G` has no `K_7` minor, then one face `F` contains every
literal `S`-portal.  Put

\[
 f=|V(F)|,\qquad h=|V(L)-V(F)|,
 \qquad e=\sum_{z\notin V(F)}(d_L(z)-7).                  \tag{6.3}
\]

Then `h\ge1`, `e\ge0`, and

\[
 \#\{x\in V(F):d_L(x)=3\}
 \;\ge\;h+6+e+
       \sum_{\substack{x\in V(F)\\ d_L(x)\ge5}}(d_L(x)-4). \tag{6.4}
\]

In particular at least `h+6\ge7` vertices of the portal face have
`L`-degree three, and every such vertex is adjacent to at least four
literal vertices of `S`.

#### Proof

Lemmas 3.1 and 3.2 remain valid for a three-connected `L`, as noted in
the proof of Lemma 3.1.  Apply the planar three-connected version of the
rooted-`K_4` theorem and the same basis-exchange argument as in Lemma
4.1.  A rooted outcome lifts by Lemma 2.1; otherwise all portal
occurrences lie on one face `F`.

All vertices off `F` have no external neighbours, and therefore have
`L`-degree at least seven.  The exact degree lower bound and Euler upper
bound give

\[
 \sum_{x\in V(F)}d_L(x)+7h+e
       \le2m\le4f+6h-6.                                  \tag{6.5}
\]

Equivalently,

\[
 \sum_{x\in V(F)}(4-d_L(x))\ge h+6+e.                    \tag{6.6}
\]

Three-connectivity gives `d_L(x)\ge3`.  Separate in (6.6) the positive
terms at degree three and the negative terms at degree at least five;
this is exactly (6.4).  If `h=0`, the three-connected graph `L` would be
outerplanar, while every finite simple outerplanar graph has a vertex of
degree at most two.  Thus `h\ge1`.  Finally a degree-three face vertex has
total degree at least seven in `G`, has no neighbour in `R`, and all of
its neighbours outside `L` lie in `S`; it consequently contacts at least
four literal boundary vertices.  \(\square\)

Thus the planar three-connected obstruction is not an arbitrary rural
page: it has a linear supply of literal four-label portal vertices on
its distinguished face.

### Corollary 6.2 (three cyclic portal arcs give the literal `K_7`)

The planar three-connected residue of Proposition 6.1 is empty: under
the setup of Theorem 1.1, a planar three-connected `L` forces a literal
`K_7` minor.

#### Proof

Let `D` be the set of degree-three vertices on the common portal face.
Proposition 6.1 gives `|D|\ge7`, and every `x\in D` contacts at least
four labels in `S`.  Counting the incidences between `D` and the seven
literal labels, some label `q\in S` has at least

\[
                         \left\lceil\frac{4|D|}{7}\right\rceil
                              \ge4                           \tag{6.7}
\]

neighbours in `D`.  Choose three of them, `u_1,u_2,u_3`, in their cyclic
order on the facial cycle.

Partition that cycle into three nonempty, pairwise disjoint contiguous
arcs `X_1,X_2,X_3`, with `u_i in X_i`.  The three arcs are connected and
pairwise adjacent through the three cycle edges at their interfaces.
For each `i` put

\[
                         A_i=N_S(u_i)-\{q\}.                \tag{6.8}
\]

Every `A_i` has order at least three.  The three sets have distinct
representatives `s_1,s_2,s_3`: Hall's condition is automatic, since a
one-set union has order at least three, a two-set union has order at
least three, and the three-set union also has order at least three.

Now use the seven bags

\[
 X_i\cup\{s_i\}\quad(1\le i\le3),\qquad \{q\},\qquad
 P_j\cup\{r_j\}\quad(1\le j\le3),                         \tag{6.9}
\]

where

\[
                         \{r_1,r_2,r_3\}
                           =S-\{q,s_1,s_2,s_3\}.           \tag{6.10}
\]

The first three bags are connected, are pairwise adjacent through the
facial cycle, and each sees `{q}` through `u_iq`.  The last three are
connected and pairwise adjacent by packet fullness.  Each packet bag
sees every arc bag through its literal anchor `s_i`, and sees `{q}` by
fullness.  Thus (6.9) is a literal `K_7` model.  \(\square\)

This construction is the promised step beyond facial coherence.  It
uses the planar degree deficit to create three rich literal roots, then
uses the facial order itself as a three-bag clique carrier.  No planar
expansion, apex choice, or colour-state transfer remains in this branch.

### Proposition 6.3 (nonplanar web cell has a three-vertex gate)

Assume instead that `L` is three-connected and nonplanar and that `G`
has no `K_7` minor.  Then there is a three-element set

\[
                         T=\{t_1,t_2,t_3\}\subseteq V(L) \tag{6.7}
\]

and a nonempty component `K` of `L-T` such that

\[
                         N_L(K)=T,
                         \qquad |N_S(K)|\ge4.              \tag{6.8}
\]

The set `T` is a facial triangle of a web completion containing `L` as a
spanning subgraph; it is **not** asserted to be a clique in `L`.

If `L[T]` is a triangle, then the four carrier portal sets

\[
 N_S(K),\quad N_S(t_1),\quad N_S(t_2),\quad N_S(t_3)      \tag{6.9}
\]

have no system of distinct representatives.  Since the first set has
order at least four, Hall's theorem localizes the failure entirely on
the gate: for some nonempty `I\subseteq\{1,2,3\}`,

\[
                   \left|\bigcup_{i\in I}N_S(t_i)\right|<|I|. \tag{6.10}
\]

Thus, conditional on the gate being a literal triangle, a surviving
nonplanar torso has a gate vertex with no boundary contact, two gate
vertices whose combined boundary contact has order at most one, or three
whose combined boundary contact has order at most two.  If the gate is
not a literal triangle, the missing gate edge is a separate live
obstruction.

#### Proof

Choose any matched four-portal set, which exists by Lemma 3.1.  It has
no rooted `K_4`, by Lemma 2.1.  The three-connected rooted-web theorem
of Fabila-Monroy and Wood makes `L` a spanning subgraph of a web.  Since
`L` is nonplanar, some web cell is nonempty.  The standard web-cell
argument, written out and checked in the companion audit (Section 6), then
gives the three gate vertices and component in (6.8), disjoint from the
four chosen roots.  The gate is a triangle in the web rib, not necessarily
in `L`.  All
neighbours of `K` outside `L` lie in `S`, so

\[
                         N_G(K)=T\cup N_S(K).              \tag{6.11}
\]

At least one of the four roots lies outside `K\cup T`; the nonempty
opposite shore also lies outside.  Hence (6.11) is an actual separator.
Seven-connectivity gives `|N_S(K)|\ge4`.

Now assume conditionally that `L[T]` is a triangle.  If the four sets in
(6.9) had distinct representatives
`s_0,s_1,s_2,s_3`, then

\[
 K\cup\{s_0\},\qquad \{t_1,s_1\},\qquad
 \{t_2,s_2\},\qquad \{t_3,s_3\}                         \tag{6.12}
\]

would be four disjoint connected pairwise adjacent bags: `T` is a
triangle and every gate vertex has a neighbour in `K`.  Anchor the three
opposite full packets at the other three vertices of `S`, exactly as in
Lemma 2.1.  This gives a literal `K_7`, a contradiction.  Therefore
(6.9) has no SDR.  No Hall-deficient subfamily can contain `N_S(K)`,
because that set alone has order at least four while the entire family
has only four members.  A deficient subfamily of the three gate sets
gives (6.10).  \(\square\)

Corollary 6.2 closes the planar branch completely.  Proposition 6.3
leaves the nonplanar branch at an actual three-vertex adhesion.  When
that adhesion is a literal triangle, its only obstruction to the same
seven-bag lift is the explicitly Hall-deficient gate; otherwise the
missing gate edge must itself be repaired or exploited.  Thus every
surviving three-connected thin shore is nonplanar and contains this
labelled web cell, but the web completion must not be confused with the
literal graph.
