# Near-$K_7$ splitting round: the connectivity barrier and the exact exchange gap

## Status

This note audits the proposed upgrade of a normalized (K_7^-)- or
(K_7^{\vee})-model in a hypothetical minor-minimal counterexample to
(\mathrm{HC}_7).  It proves a sharp counterexample to every
connectivity-only splitting claim, gives a valid minimal-bag normal form, and
isolates the additional exchange statement that would actually have to use
7-contraction-criticality.  It does **not** close (\mathrm{HC}_7).

Throughout, (K_7^-) means (K_7) with one edge deleted, while
(K_7^{\vee}) means (K_7) with two adjacent edges deleted.

## 1. Normalized models

A (K_7^-)-model will be written

\[
 (A,C,D_1,D_2,D_3,D_4,D_5),
\]

where (A,C) are the only pair not required to be adjacent.  In a
(K_7)-minor-free graph, after making the model spanning, (A) and (C)
are genuinely anticomplete.

A (K_7^{\vee})-model will be written

\[
 (A,B,C,D_1,D_2,D_3,D_4),
\]

where only (AB) and (AC) are not required.  If the graph has no
(K_7^-)-minor, these two pairs are genuinely anticomplete.  In a
7-connected graph, the spanning normalization gives

\[
 |N(A)|\geq 7.
\]

For a (K_7^-)-model these neighbours lie in five bags; for a
(K_7^{\vee})-model with no (K_7^-)-minor they lie in only the four
(D_i).  Thus some unaffected bag is multiply hit.  The question is whether
that bag can be split or rerouted to repair the missing adjacency.

## 2. A sharp counterexample to connectivity-only splitting

### Proposition 2.1

There is a 7-connected graph (G) with minimum degree seven and Hadwiger
number six which has a spanning (K_7^-)-model in exactly the normalized
form above, with seven distinct attachments from the deficient bag into the
other five bags and three attachments in one bag.

Consequently, neither 7-connectivity, minimum degree seven, spanningness,
nor the portal-concentration conclusion implies that a multiply hit bag can
be split to produce a (K_7)-minor.

### Proof

Use the following standard labelling of the icosahedron (I).  Its vertices
are

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4,
\]

with subscripts modulo five, and its edges are

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.
\]

Let

\[
 G=K_2\vee I,
\]

and call the two new universal vertices (p,q).  The icosahedron is
5-connected, so

\[
 \kappa(G)=2+\kappa(I)=7.
\]

It is 5-regular, hence every old vertex has degree seven in (G), and so
(\delta(G)=7).

For any graph (X), adjoining one universal vertex raises the Hadwiger
number by exactly one.  The lower bound is immediate.  For the upper bound,
given a clique model in (K_1\vee X), either its universal vertex is unused,
or deleting the unique bag containing it leaves a clique model with one
fewer bag in (X).  Since (I) is planar and contains a (K_4)-minor,
(\eta(I)=4).  Therefore

\[
 \eta(G)=\eta(I)+2=6,
\]

so (G) has no (K_7)-minor.

Nevertheless the following seven bags form a spanning (K_7^-)-model:

\[
\begin{aligned}
 A&=\{t\}, & C&=\{b\},\\
 D_1&=\{u_0,w_0\}, & D_2&=\{u_1,w_1\},\\
 D_3&=\{u_2,u_3,u_4,w_2,w_3,w_4\},\\
 D_4&=\{p\}, & D_5&=\{q\}.
\end{aligned}
\]

The first two nontrivial (D_i) are connected.  The third is connected.
The cyclic edges give (D_1D_2,D_2D_3,D_3D_1), and the universal vertices
supply all pairs involving (D_4,D_5).  The bag (A) meets every (D_i),
as does (C), while (t b\notin E(I)).  These are precisely the adjacencies
of (K_7^-).

Finally, the seven neighbours of (A=\{t\}) outside (A) are

\[
 u_0,u_1,u_2,u_3,u_4,p,q.
\]

They are distributed among the five (D_i), with (D_3) hit three times.
Since (G) has no (K_7)-minor, no claimed splitting operation can succeed
on this model.  This proves the proposition. \(\square\)

The example is 2-apex and is 6-colourable: delete (p,q), apply the Four
Colour Theorem to (I), and give (p,q) two new colours.  It is therefore
not a 7-contraction-critical graph.  This pinpoints the missing input:
**any valid splitting theorem must use chromatic or contraction-critical
information, not just connectivity and the normalized model.**

The same construction works more generally with (K_2\vee P) whenever
(P) is a 5-connected planar graph containing a (K_5^-)-minor.

## 3. What a valid one-bag split must actually preserve

The following elementary certificate is useful because it displays all the
simultaneous requirements hidden by the phrase "split the multiply hit
bag".

### Lemma 3.1 (one-bag split certificate)

Consider a (K_7^-)-model

\[
 (A,C,D_1,\ldots,D_5)
\]

and fix (D=D_i).  Suppose (D) has a partition (D=P\mathbin{\dot\cup}R)
such that

1. (P) and (R) are nonempty and connected;
2. (P) has a neighbour in each of (A) and (C);
3. (R) has a neighbour in (C) and in every (D_j) with (j\ne i).

Then (G) contains a (K_7)-minor.

### Proof

Because (D) is connected and (P,R) partition it, there is an edge between
(P) and (R).  Replace (A) by (A\cup P) and (D_i) by (R), leaving
the other five bags unchanged.  The enlarged (A)-bag is connected and is
now adjacent to (C).  The edge (PR) preserves its adjacency to the new
(D_i)-bag.  Condition 3 preserves all adjacencies required from (D_i).
Every other old adjacency is untouched. \(\square\)

There is a symmetric certificate with (A,C) interchanged.  The important
point is that multiple (A)-attachments are not enough.  A split of this
form needs redundant contact with the *opposite* deficient bag and must
leave one connected side carrying all four other clique adjacencies.  None
of these properties follows from the pigeonhole argument in the normalized
model.

In the icosahedral example, the large bag (D_3) contains three
(A)-portals and three (C)-portals.  Nevertheless any connector taken to
repair (AC) destroys the connected residual needed simultaneously to
retain the two cyclic end contacts.  The nonexistence of the certificate is
also forced abstractly by (\eta(G)=6).

## 4. Minimal branch sets are locked Steiner trees

Shrink each unaffected branch set while keeping the other six bags fixed.
The following normal form is valid for both (K_7^-) and
(K_7^{\vee}).

### Lemma 4.1 (leaf charging)

Let (D) be an unaffected bag, chosen inclusion-minimal subject to being
connected and retaining every required adjacency to the other six bags.
Let (T) be a tree on (D) that is also minimal with these properties.
Then every leaf (x) of (T) is the unique (D)-side portal for at least
one of the six other bags.  Distinct leaves can be charged to distinct
other bags.  Consequently (T) has at most six leaves.

If one bag (A) has at least two distinct neighbours in (D), then no leaf
can be charged to (A), and (T) has at most five leaves.

### Proof

If a leaf (x) were not uniquely responsible for any required adjacency,
then (T-x) would remain connected and would retain a required edge to
each other bag, contradicting minimality.  Charge (x) to one bag for which
it is uniquely responsible.  Two leaves cannot receive the same charge:
each would provide an attachment surviving deletion of the other.  This
gives at most six leaves.  If (A) has two portals in (D), deletion of
any one leaf leaves an (A)-attachment, so (A) cannot be a charge. \(\square\)

The same argument applies to every vertex whose deletion leaves the bag
connected, not only to tree leaves.

### Corollary 4.2 (non-cutvertex bound)

In the setting of Lemma 4.1, (D) has at most six vertices which are not
cutvertices of (G[D]).  If (A) has two portals in (D), it has at most five
such vertices.  In particular, a 2-connected multiply hit bag has order at
most five.

### Proof

If (D-x) is connected, inclusion-minimality says that deleting (x) must
destroy the adjacency to at least one other bag.  Charge (x) to such a bag.
As before, two different vertices cannot be uniquely responsible for the
same target bag.  There are six targets, or only five available charges when
the (A)-adjacency is redundant. \(\square\)

Thus every multiply hit bag of order at least six has a cutvertex.  At the
opposite extreme, a 2-connected bag of order five is fully saturated: every
vertex is the unique portal for one of the five target bags other than
(A).  This is a finite locked cell, not a free splitting cell.

### Lemma 4.3 (removable common portal)

For a (K_7^-)-model, suppose (x\in D_i) is adjacent to both deficient bags
(A,C), the graph (D_i-x) is connected, and (D_i-x) retains an adjacency to
(C) and every (D_j) with (j\ne i).  Then (G) has a (K_7)-minor.

For a (K_7^{\vee})-model, suppose (x\in D_i) is adjacent to (A) and to one
of (B,C), while (D_i-x) is connected and retains all six required
adjacencies of (D_i).  Absorbing (x) into (A) produces a (K_7^-)-model.

### Proof

Use the singleton (P=\{x\}) in the exchange from Lemma 3.1.  Connectivity
of (D_i) supplies an edge from (x) to (D_i-x), which preserves adjacency
between the enlarged (A)-bag and the residual (D_i)-bag.  In the
(K_7^{\vee}) case exactly one of the two missing adjacencies at (A) is
repaired and no required adjacency is lost. \(\square\)

Consequently, after minimizing the model, every common portal for a missing
pair is locked either by being a cutvertex or by being the unique portal for
some other target.  This is the exact local obstruction that any global
rerouting theorem must overcome.

Thus portal concentration does yield structure, but the structure is a
**locked Steiner tree**, not an automatic split.  Every removable leaf is
protecting another clique adjacency.  This is precisely the phenomenon
realized geometrically by the icosahedral example.

Indeed, in that example the large spanning bag can be shrunk to

\[
 \{u_2,u_3,u_4,w_3\}.
\]

Its tree has centre (u_3) and leaves (u_2,u_4,w_3).  The first two leaves
are the unique contacts to (D_2,D_1), respectively, and the third is the
unique contact to (C), while (A) hits all three upper vertices.  Thus even
the inclusion-minimal core is exactly a locked tree of the type described
above.

There is a limited, valid exchange rule.  Suppose a leaf (x) of (D)
is adjacent to both (A) and (C), (D) has another (A)-portal, and
(D-x) loses at most one required adjacency, say to (E).  Moving (x)
from (D) into (A) repairs (AC).  If no adjacency is lost, this gives
(K_7).  If exactly (DE) is lost, it gives a new (K_7^-)-model whose
deficient pair is (D,E).  This "deficiency transport" is rigorous, but it
does not terminate: a sequence can cycle among locked bags, and a leaf may
uniquely support several other adjacencies.

## 5. The extra paths supplied by criticality

Contraction-criticality supplies a genuine mechanism that is absent in the
2-apex counterexample, but it still lacks branch-set avoidance.

### Lemma 5.1 (Kempe detours around every edge)

Let (G) be (k)-critical and let (xy\in E(G)).  In every
((k-1))-colouring of (G-xy), the vertices (x,y) receive the same
colour, say (0).  For each other colour (i), the (0/i)-coloured
subgraph contains an (x)-(y) path.

### Proof

If (x,y) had different colours, the colouring would also colour (G).
If they lie in different (0/i)-components, interchange colours (0,i)
on the component containing (x).  Then (x,y) have different colours,
again giving a proper ((k-1))-colouring of (G). \(\square\)

For (k=7), every internal edge of a minimal bag therefore has five
bichromatic detours.  Detours belonging to different second colours can
intersect only at vertices of colour (0).  Independently,
7-connectivity gives six internally vertex-disjoint uncoloured detours
around an edge.

Neither assertion gives the needed exchange.  A Kempe detour may run
through several reserved branch sets; different detours may share
colour-0 vertices; and an uncoloured Menger detour may use the unique portal
whose preservation is the point of the rerouting.  Treating any of these
paths as free would repeat the branch-set-overlap error already identified
in the Claim 4.4 route.

### 5.2 Every-neighbourhood-nonedge witnesses

There is a stronger source of prescribed colourings when the deficient bag
is a singleton minimum-degree vertex.  Let (v) have degree seven in a
hypothetical counterexample and put (N=N(v)).  For **every** nonedge
(xy) of (G[N]), contract the connected star on ({v,x,y}) to a vertex (q).
Every 6-colouring of this proper minor gives (q) one colour and gives the
five vertices of (N-\{x,y\}) the other five colours bijectively.  Indeed,
they avoid the colour of (q); if one of the remaining five colours were
missing, expanding (x,y) with the colour of (q) and assigning the missing
colour to (v) would 6-colour (G).

This means that every nonedge of the seven-vertex neighbourhood is an
accessible repeated pair, not merely the pair arising accidentally in one
colouring.

Suppose now that a normalized model has deficient bag (A=\{v\}) and an
unaffected bag (D) contains two nonadjacent (v)-portals (x,y).  Use the
star-contraction colouring for this pair.  The other five neighbours are
rainbow and, by the audited Kriesell--Mohr argument, root a (K_5)-model
using only their five colour classes.  Since (D) contains an (x)-(y) path,
a (K_7)-model follows whenever one such rooted certificate is disjoint from
an (x)-(y) connector: Dirac's bound (\alpha(G[N])\le2) makes every one of
the five roots adjacent to at least one of (x,y), so the connector is the
sixth bag and ({v}) is the seventh.

Consequently a surviving model satisfies the following **universal
nonedge lock**:

\[
 \begin{split}
 &\text{for every nonedge (xy) among two portals in one bag,}\\
 &\text{every corresponding rooted (K_5) certificate meets every}\
   \text{ (x)-(y) connector available for the sixth bag.}
 \end{split}
\]

This is stronger than the one-colouring obstruction, and suggests a
multicut attack: combine the locks for all nonedges among the portals and
try to extract a separator of order at most six.  No Helly or packing lemma
currently justifies that extraction.  In particular, the five prescribed
Kempe colour classes may still run through all reserved branch sets, so the
star contraction alone does not perform the Steiner exchange.

The smallest useful new lemma would have to be a **Kempe--Steiner exchange
lemma**: in the locked-tree normal form, some leaf transfer or internal-edge
rerouting repairs its lost target adjacencies while avoiding the other
reserved bags.  The hypotheses must explicitly include
7-contraction-criticality; Proposition 2.1 disproves the statement without
it.

## 6. Why standard splitter and knitted theorems do not close the gap

1. Tutte--Seymour splitter theorems preserve 3-connectivity and the
   existence of a fixed 3-connected minor along a deletion/contraction
   sequence.  They do not preserve seven-way branch-set terminals and do
   not turn a (K_7^-)-minor into (K_7).  Proposition 2.1 is already a
   counterexample to such an inference.

2. The current general knitted theorem of Kawarabayashi--Yu states that an
   (8\ell)-connected graph is (\ell)-knitted.  Even a direct application
   to a seven-terminal split would ask for connectivity on the order of 56,
   not seven.  More importantly, the object needing the connected
   bipartition is an individual branch set after the other bags have been
   reserved; global 7-connectivity gives no comparable connectivity inside
   that residue.  See
   <https://arxiv.org/abs/2606.01586>.

3. General rooted-minor and locally-spanning machinery currently gives
   sharp low-connectivity statements for connectivity at most four, not
   this prescribed six- or seven-bag exchange.  See
   <https://arxiv.org/abs/2003.04011>.

Thus invoking "knittedness", "linkage", or "the splitter theorem" without
a new avoidance statement does not advance the proof.

## 7. A structurally sharp next target

The counterexample suggests the following dichotomy as a useful research
target, not as an established theorem.

> **Near-model split/2-apex target.**  A 7-connected (K_7)-minor-free
> graph with a spanning normalized near-(K_7) model either admits a valid
> branch-set exchange improving (K_7^{\vee}) to (K_7^-), or improving
> (K_7^-) to (K_7), or has a 2-apex decomposition compatible with the
> model.

The icosahedral construction shows that the 2-apex alternative is
necessary and sharp.  In a hypothetical (\mathrm{HC}_7) counterexample it
would be impossible, because every 2-apex graph is 6-colourable by the Four
Colour Theorem.  Proving this dichotomy for all normalized models would
therefore close the near-clique route.

This target may still be theorem-strength.  It resembles the unresolved
apex-structure phenomena around highly connected (K_6)-minor-free graphs,
so it should not be called routine.  A more local and falsifiable first
step is:

> **Locked-bag target.**  In a 7-contraction-critical (K_7)-minor-free
> graph, a size-minimal spanning (K_7^-)- or (K_7^{\vee})-model cannot
> have every multiply hit unaffected bag in the locked-Steiner-tree state
> of Lemma 4.1.

An attack on this statement should combine the leaf charges with the five
Kempe detours of Lemma 5.1.  Its stopping criterion is precise: if the only
way to choose a detour is to demand that it avoid an arbitrary prescribed
union of four or five branch sets, then the route has merely restated the
missing exchange lemma and has stalled.

## 8. Net result

The near-(K_7) theorem still provides a valuable normalized obstruction,
but portal multiplicity is not close to a split on its own.  The strongest
new conclusions of this round are:

* a fully explicit 7-connected, minimum-degree-seven, (K_7)-minor-free
  graph realizing the exact portal-concentrated (K_7^-) obstruction;
* a precise one-bag split certificate displaying the required simultaneous
  residual contacts;
* a minimal-bag theorem reducing every multiply hit bag to a locked Steiner
  tree with at most five leaves;
* five critical Kempe detours around every internal bag edge; and
* the exact remaining need for a contraction-critical
  Kempe--Steiner avoidance/exchange lemma, or a structural 2-apex
  alternative.

No currently identified splitter, linkage, knitted, or rooted-minor theorem
supplies that missing avoidance.
