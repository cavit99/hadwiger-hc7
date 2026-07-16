# Exact two-row states in the five-colour matching deletion

**Status:** The recolouring, local double-criticality, Kempe, Menger, and
branch-set statements in Sections 2--5 are proved here and have a separate
GREEN internal audit. The prescribed-path input in Section 6 is a published
theorem of Li--Ning--Zhang. Section 7 records a barrier: the path obtained in
Section 6 need not extend to the four-linkage used in Section 5. This note
does not prove $HC_7$.

The point of the note is to isolate the full content of the `chi(G-F)=5`
branch without introducing local seam terminology.  It leaves one standard
rooted-linkage obstruction rather than a family of labelled cases.

## 1. Setup

Let `G` be a seven-chromatic graph and let

\[
                 F=\{e,f,g\}
\]

be a matching.  Put `K=G-F` and assume that `K` has a proper five-colouring
`c`.  For a row `h=xy in F`, say that `h` is **equal** under `c` when
`c(x)=c(y)`, and write `D(c)` for the set of equal rows.

In the support-six application, write

\[
 e=aa',\qquad f=bb',
\]

and suppose that `e` and `f` are the two-vertex bags of disjoint support-six
`K_5` models with singleton cores `Q_e` and `Q_f`.  Thus `Q_e,Q_f` are
disjoint literal four-cliques, are disjoint from the endpoints of `F`, and
every vertex of `Q_e` has a neighbour in `\{a,a'\}`, while every vertex of
`Q_f` has a neighbour in `\{b,b'\}`.

## 2. Exact two-row rigidity

### Theorem 2.1

Every proper five-colouring `c` of `K` has

\[
                            |D(c)|\ge 2.                 \tag{2.1}
\]

If `D(c)=\{e,f\}`, then the four endpoints of `e` and `f` induce a literal
`K_4` in `G`.

#### Proof

If no row is equal, `c` is already a five-colouring of `G`.  If exactly one
row is equal, recolour one of its ends with one fresh sixth colour.  This
restores that row and gives a six-colouring of `G`.  Both conclusions
contradict `chi(G)=7`, proving (2.1).

Now suppose `D(c)=\{e,f\}`.  If one endpoint `x` of `e` and one endpoint `y`
of `f` were nonadjacent, recolour both `x` and `y` with one fresh sixth
colour.  They are nonadjacent, both formerly equal rows become proper, and
the third row was already proper.  This again gives a six-colouring of `G`.
Hence all four cross-edges between `e` and `f` are present.  Together with
`e` and `f`, they form the asserted `K_4`.  \(\square\)

Write

\[
 c(a)=c(a')=\alpha,\qquad c(b)=c(b')=\eta.
\]

The cross-edges show that `alpha != eta`.

### Corollary 2.2 (four edge-local double-critical pairs)

For every `x in \{a,a'\}` and `y in \{b,b'\}`,

\[
                         \chi(G-x-y)=5.                \tag{2.2}
\]

#### Proof

The restriction of `c` to `G-x-y` is proper: deleting `x` and `y` removes
the obstruction on both equal rows, and the third row was proper.  Conversely
`chi(G-x-y)>=chi(G)-2=5`, since two deleted vertices can always be restored
with two new colours.  \(\square\)

### Lemma 2.3 (common neighbour of every colour)

Fix a cross-edge `xy` as in Corollary 2.2 and the induced five-colouring of
`G-x-y`.  For every one of its five colours, `x` and `y` have a common
neighbour of that colour.

#### Proof

Fix a colour `beta`.  If there is no common `beta`-neighbour, recolour every
`beta`-coloured neighbour of `y` with one fresh sixth colour, give `y` colour
`beta`, and give `x` the fresh colour.  The recoloured neighbours of `y` are
independent and none is adjacent to `x`, by the assumed absence of a common
neighbour.  The resulting colouring is therefore a proper six-colouring of
`G`, a contradiction.  \(\square\)

This is the one-colour case of the familiar path lemma for a double-critical
edge, but the elementary proof above is edge-local and needs no global
double-critical hypothesis.

## 3. Two simultaneously locked outside colours

Let the endpoints of the proper third row `g` have distinct colours
`rho,sigma`, and put

\[
                    B=[5]-\{\alpha,\eta\}.
\]

Thus `|B|=3`.

### Theorem 3.1

For at least two colours `beta in B`, both of the following hold in `K`:

1. `a` and `a'` lie in one `alpha,beta` Kempe component;
2. `b` and `b'` lie in one `eta,beta` Kempe component.

#### Proof

Fix `beta in B`.  Suppose first that the `alpha,beta` component containing
`a` omits `a'`.  Interchange `alpha` and `beta` on this component.  The row
`e` becomes proper and `f` remains equal.  Theorem 2.1 says that the new
five-colouring must still have at least two equal rows, so `g` must become
equal.  The exact Kempe toggle rule then forces

\[
                         \{\rho,\sigma\}=\{\alpha,\beta\}. \tag{3.1}
\]

Similarly, failure of item 2 for `beta` forces

\[
                         \{\rho,\sigma\}=\{\eta,\beta\}.  \tag{3.2}

The fixed pair `\{rho,sigma\}` can satisfy (3.1) for at most one member of
`B`, and (3.2) for at most one member of `B`.  It cannot satisfy one equation
of each kind: equality of `\{alpha,beta\}` and `\{eta,gamma\}`, with
`beta,gamma` outside `\{alpha,eta\}`, would force `beta=eta` and
`gamma=alpha`.  Hence at most one colour in `B` fails either item.  At least
two colours satisfy both.  \(\square\)

For either of these two colours `beta`, Lemma 2.3 supplies a vertex of colour
`beta` adjacent to any prescribed cross-pair, for example to `a` and `b`.
Such witnesses lie outside the endpoint `K_4`, and witnesses of different
colours are distinct.  Thus the exact-two state supplies two distinct
outside vertices, each contacting both row bags, as well as the two locked
Kempe-component families.

## 4. The all-three-equal branch

If `D(c)=F`, the punctured-cube theorem already gives the exact statement
needed here: the six endpoints have no independent transversal containing
one endpoint of each row.  No stronger conclusion about the endpoint graph
is used in this note.

For orientation only, the following two elementary consequences are safe.
The three common row colours cannot all coincide, since then every
cross-row edge is absent from `K` and every transversal is independent.  If
two rows have common colour `alpha` and the third has a different common
colour, then each endpoint of the third row is complete to at least one of
the first two rows; otherwise its two chosen nonneighbours would complete an
independent transversal.  These observations do not close the all-equal
branch.

## 5. Four-linkage decoder

Retain an exact-two state `D(c)=\{e,f\}` and put

\[
                         C=V(e)\cup V(f),\qquad H=G-C.
\]

By Theorem 2.1, `C` is a literal four-clique.  If `G` is seven-connected,
then `H` is three-connected.

### Theorem 5.1 (separator or labelled `K_6`)

Exactly one of the following is available.

1. There is an actual separation of `G` with boundary `C union X`, where
   `|X|=3`, which places the two named support-six models in opposite closed
   shores.
2. There are four pairwise vertex-disjoint `Q_e-Q_f` paths
   `P_1,...,P_4` in `H`, with distinct ends and no internal vertex in
   `Q_e union Q_f`.  The six bags

   \[
                           e,\ f,\ P_1,\ldots,P_4       \tag{5.1}
   \]

   form a literal labelled `K_6` model in `G`.

#### Proof

Apply the vertex form of Menger's theorem to `Q_e,Q_f` in `H`.  If four
disjoint paths do not exist, a set `X` of order at most three separates the
two four-cliques.  Since `H` is three-connected and neither four-clique is
deleted by `X`, one has `|X|=3`.  Each surviving part of a four-clique lies
in one component of `H-X`; assigning the remaining components arbitrarily
gives the asserted actual exact-seven separation.  The endpoints `e,f` lie
in its boundary `C`, so both named models are retained in their declared
closed shores.

Otherwise truncate the four Menger paths at their first and last core
vertices.  Since each core is a four-clique and all four ends are distinct,
the path bags are pairwise adjacent.  Every path bag contacts `e` through
its `Q_e` end and `f` through its `Q_f` end.  Finally `e` and `f` are
adjacent because their four endpoints form `C=K_4`.  This proves (5.1).
\(\square\)

The exact-seven boundary in item 1 preserves the two selected support
models.  A third support may cross it.  The existing cross-star theorem
describes that trace, but no claim that all three models are already ranked
is made here.

Orient every `P_i` from `Q_e` to `Q_f`.  A vertex of a path is an
**e-contact** (respectively **f-contact**) if it has a neighbour in the
two-vertex bag `e` (respectively `f`).

### Theorem 5.2 (nonmonotone member gives `K_7`)

If some `P_i` contains an f-contact `x` strictly before a distinct later
e-contact `y`, then `G` contains a literal `K_7` minor.

#### Proof

Choose any edge `rs` of the oriented subpath `xP_i y`.  Replace `P_i` by
the prefix ending at `r` and the suffix beginning at `s`.  The prefix keeps
the `Q_e` end and contains `x`; the suffix keeps the `Q_f` end and contains
`y`; and the edge `rs` joins the two new bags.  Consequently

\[
 e,\ f,\ \{P_j:j\ne i\},\ P_i[Q_e,r],\ P_i[s,Q_f]
\]

are seven pairwise adjacent disjoint connected bags.  \(\square\)

Thus every four-linkage in a `K_7`-minor-free host is **monotone**: on each
oriented member all e-only contacts precede all f-only contacts, and there
is at most one common-contact vertex.

## 6. A global raw path or a three-cut

The two outside-colour witnesses from Section 3 give one clean global
consequence.

### Theorem 6.1 (two-witness path or three-cut)

Let `u,v` be two distinct vertices of `H`, each contacting both `e` and
`f`.  Then at least one of the following holds.

1. `H` has a vertex cut of order three; hence `C` together with that cut is
   an actual exact-seven boundary in `G`.  No side assignment for the three
   named supports is asserted in this alternative.
2. For any distinct choices
   `q in Q_e-\{u,v\}` and `r in Q_f-\{u,v\}`, `H` has a `q-r` path
   passing through both `u` and `v`.  Along that path an f-contact precedes
   a distinct later e-contact, in one of its two orientations.

#### Proof

The graph `H` is three-connected.  If it has no cut of order three, it is
four-connected.  The path theorem of Li, Ning and Zhang says that in a
`k`-connected graph, for fixed distinct ends `q,r`, there is a `q-r` path
through any prescribed set of `k-2` further vertices.  Apply it with
`k=4` and prescribed vertices `u,v`.  The required choices of `q,r` exist
because the two cores are disjoint four-sets.  Whichever of `u,v` occurs
first on the resulting path is an f-contact, while the other is a later
e-contact.  \(\square\)

Primary source: Binlong Li, Bo Ning and Shenggui Zhang, *Long paths and
cycles passing through specified vertices under the average degree
condition*, arXiv:1109.4344, path theorem in the abstract and Theorem 4.

The path in item 2 is deliberately called **raw**.  It may meet either
terminal clique internally and it is not asserted to be a member of a
four-linkage.

## 7. Sharp augmentation barrier

The tempting implication

\[
 \text{raw nonmonotone path in a four-connected }H
 \quad\Longrightarrow\quad
 \text{nonmonotone member of a four-linkage}             \tag{7.1}
\]

is false, even with a proper five-colouring and two different-colour common
contacts.

Let

\[
 Q_e=\{x_1,x_2,x_3,x_4\},\quad
 Q_f=\{y_0,y_2,y_3,y_4\},\quad
 Z=\{z_0,z_1,z_2,z_3\}.
\]

Make `Q_e,Q_f` cliques, put no edge between them, assign the subscript as
the colour, and join `z_i` to every core vertex of a different colour.  Add
the edge `z_2z_3`.  This is properly five-coloured.  Direct deletion of at
most three vertices leaves it connected, while deleting `Z` separates the
two cores, so the graph is exactly four-connected.

Here is a short verification of the lower bound on connectivity.  Each core
survives deletion of at most three vertices.  Every `z_i` has at least three
neighbours in each core.  If a surviving `z_i` loses all its neighbours in
one core, all three deletions have been spent there; then every other gate
vertex survives, and one of a different colour joins the surviving core
vertex to the untouched opposite core.  Some surviving gate vertex therefore
joins the two surviving core cliques.  Every other surviving gate vertex has
a neighbour in at least one of them.  The remainder is connected.

Declare the core `Q_e` to contact `e`, the core `Q_f` to contact `f`, and
`z_2,z_3` to contact both bags.  There is a raw nonmonotone path

\[
                         x_1z_2z_3y_0.                \tag{7.2}
\]

However every `Q_e-Q_f` path meets `Z`.  Four disjoint such paths use all
four vertices of `Z`, exactly one on each path.  Hence no member can contain
both `z_2,z_3`, and every four-linkage is monotone under the declared
contacts.

The example can be extended by two equal row bags of colours `0` and `1`:
join the first bag to `Q_e`, the second to `Q_f`, and join `z_2,z_3` to
both.  Then the `0,2` and `0,3` components connect the first row, the `1,2`
and `1,3` components connect the second row, and `z_2,z_3` are the two
different-colour common witnesses from Section 3.  Thus the two Kempe locks
alone do not repair (7.1).

This construction is not claimed to be a strongly contraction-critical,
`K_7`-minor-free graph.  It establishes the exact trust boundary: completing
the five-colour branch now requires either

* an augmentation theorem using the full minor-critical or `K_7`-free
  hypotheses;
* a direct `K_7` decoder for the four-vertex gate outcome; or
* an accepted exact-seven handoff arising from a three-cut.

Further subdivision into labelled seam cases would not address this
standard rooted-linkage obstruction.
