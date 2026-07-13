# The homogeneous shell as a double-rainbow rooted-`K_4` problem

## 1. Setup

Let `G` be seven-connected.  Let

\[
 Q=\{q_1,q_2,q_3\}
\]

be the neutral triangle and put `H=G-Q`.  Assume `H` has a spanning
partition

\[
 \{a\}\mathbin{\dot\cup}\{b\}\mathbin{\dot\cup}\{c\}
 \mathbin{\dot\cup}X_1\mathbin{\dot\cup}X_2
 \mathbin{\dot\cup}X_3,                            \tag{1.1}
\]

where the `X_i` are nonempty and connected and the only interclass
contacts are those of the homogeneous exceptional word `(c,c,a)`:

\[
\begin{gathered}
 bc;\qquad
 X_1\sim a,b,X_2;\qquad
 X_2\sim a,b,X_1,X_3;\qquad
 X_3\sim b,c,X_2.                                  \tag{1.2}
\end{gathered}
\]

Every `q_i` is adjacent to `a,b,c` and has a neighbour in every `X_j`.
The other three homogeneous words follow by reversing the piece path or
interchanging `b,c`.

Put

\[
 B_0=\{a,b\}\cup X_1,qquad D=X_2\cup X_3.         \tag{1.3}
\]

The set `B_0` is connected.  A set in `H` is **`Q`-rainbow** if it
contains a neighbour of each `q_i`.

## 2. The clean rooted-model certificate

### Lemma 2.1 (double-rainbow peel)

Suppose `D` has a partition

\[
                         D=R\mathbin{\dot\cup}S     \tag{2.1}
\]

such that

1. `R,S` are nonempty, connected and adjacent;
2. both are `Q`-rainbow;
3. both are adjacent to `c`; and
4. both are adjacent to `B_0`.

Then `G` has a `K_7` minor.

#### Proof

The four sets

\[
                         B_0,\quad\{c\},\quad R,\quad S \tag{2.2}
\]

are disjoint and connected.  The first two are adjacent through `bc`.
The hypotheses give all four adjacencies from `R,S` to the first two and
the adjacency `RS`.  Thus (2.2) is a `K_4` model in `H`.

Every bag in (2.2) is adjacent to all three vertices of `Q`: the bag
`B_0` contains `a,b`, the singleton bag is `c`, and `R,S` are rainbow.
Together with the three singleton bags `q_1,q_2,q_3`, they give seven
pairwise adjacent connected bags.  QED.

This is the desired triple-set rooted-`K_4` in its smallest form.  It is
not a quotient model: `R,S` are actual connected sides and each of the
nine required neutral incidences is witnessed by an actual edge.

## 3. What seven-connectivity gives before any web theorem

### Lemma 3.1 (three-route relative core)

There is no partition

\[
                         D=A\mathbin{\dot\cup}W
                              \mathbin{\dot\cup}C    \tag{3.1}
\]

with `A,C` nonempty, no `A-C` edge, `|W|<=2`, and

\[
                         X_2\subseteq A\cup W,qquad
                         X_3\subseteq C\cup W.       \tag{3.2}
\]

Consequently the minimum order of an `X_2-X_3` vertex separation inside
`D` is at least three; in the standard set-to-set form of Menger there
are three vertex-disjoint `X_2-X_3` routes with distinct ends.

#### Proof

Suppose (3.1)--(3.2) exist.  In

\[
                         G-(Q\cup\{b\}\cup W),       \tag{3.3}
\]

the vertices in `A` can reach outside `D` only through `a` and `X_1`,
which remain on the `X_2` side.  The vertices in `C` can reach outside
`D` only through `c`, which remains on the `X_3` side.  The forbidden
contacts in (1.2) give no edge between those two sides.  Thus (3.3) is
disconnected.  Its deleted set has order at most six, contradicting
seven-connectivity.  QED.

### Lemma 3.2 (three `c` portals)

One has

\[
                              |N_{X_3}(c)|\ge3.       \tag{3.4}
\]

#### Proof

The only neighbours of `c` are `b`, the three vertices of `Q`, and
vertices of `X_3`.  Since `d_G(c)>=7`, (3.4) follows.  QED.

There is a symmetric multiplicity statement at `a` across `X_1 union
X_2`; the asymmetric form (3.4) is the one needed to give both sides of
(2.1) an edge to the singleton bag `c`.

The interface itself has the same order-three lower bound.

### Lemma 3.3 (three independent interface edges)

The bipartite graph of edges between `X_2` and `X_3` has a matching of
order at least three.  In particular at least three distinct vertices of
`X_3` have neighbours in `X_2`.

#### Proof

If the interface graph had no matching of order three, Konig's theorem
would give a vertex cover `W subseteq X_2 union X_3` of order at most two.
Then there is no edge from `X_2-W` to `X_3-W`, so `W` supplies the
forbidden separation in Lemma 3.1.  QED.

## 4. A reserve core and purification of its pendant lobes

Inside `X_3`, choose a connected subgraph `W` minimal by vertex inclusion
subject to meeting the five portal classes

\[
 N_{X_3}(b),\quad N_{X_3}(c),\quad
 N_{X_3}(q_1),N_{X_3}(q_2),N_{X_3}(q_3).            \tag{4.1}
\]

After deleting cycle edges, `W` may be taken to be a tree with at most
five leaves, every leaf witnessing a portal class which would be lost on
deletion.  Put

\[
 A=N_{X_3}(X_2),\qquad C=N_{X_3}(c).                \tag{4.2}
\]

Both `A` and `C` have order at least three by Lemmas 3.2--3.3.

### Lemma 4.1 (mixed off-core lobe gives the peel)

If a component `K` of `X_3-W` meets both `A` and `C`, then the clean
double-rainbow partition of Lemma 2.1 exists.

#### Proof

Choose inside `X_2` a connected subgraph `T` meeting

\[
 N_{X_2}(B_0),N_{X_2}(q_1),N_{X_2}(q_2),N_{X_2}(q_3).
\]

All four sets are nonempty and `X_2` is connected, so such a `T` exists.
Because `K` meets `A`, an edge joins `K` to `X_2`; enlarge `T` within
`X_2`, if necessary, to reach the `X_2` end of that edge.  Then
`T union K` is connected, `Q`-rainbow, and adjacent to both `B_0` and
`c`.  It is disjoint from `W`.

The tree `W` is connected, `Q`-rainbow, and adjacent to both `b subseteq
B_0` and `c`.  The component `K` has an edge to `W`, because it is a
component of the complement of `W` in the connected graph `X_3`.
Thus `T union K` and `W` are disjoint adjacent connected transversals of
all five sets in Section 5 below.  Extend them to a connected adjacent
partition of `D` by the spanning-tree argument following (5.5), and
apply Lemma 2.1.  QED.

### Lemma 4.2 (pendant off-core lobes are interface-pure)

Assume `G` has no `K_7` minor.  Let `K` be a component of `X_3-W` having
at most one neighbour in `W`.  Then `K` meets `A` and misses `C`.

#### Proof

If `K` missed `A`, every neighbour of `K` would lie among its possible
single attachment in `W` and the five singleton vertices

\[
                         b,c,q_1,q_2,q_3.
\]

Those at most six vertices separate `K` from `a union X_1 union X_2`,
contrary to seven-connectivity.  Hence `K` meets `A`.  If it also met
`C`, Lemma 4.1 would give `K_7`.  Therefore it misses `C`.  QED.

### Lemma 4.3 (`c`-bridges have attachment surplus)

Assume `G` has no `K_7` minor.  Let `K` be a component of `X_3-W` which
meets `C`.  Then

1. `K` misses `A`;
2. `K` misses at least one of the five shell labels
   `b,c,q_1,q_2,q_3`; and
3. if it misses `m` of those labels, then

   \[
                         |N_W(K)|\ge m+2.            \tag{4.3}
   \]

In particular every off-core component carrying a `c`-portal has at
least three distinct attachments on the reserve tree.

#### Proof

The first assertion is Lemma 4.1.  If `K` met all five shell labels, then
`K` and `W`, together with the five singleton bags

\[
                         b,c,q_1,q_2,q_3,
\]

would be seven pairwise adjacent connected bags: the five singletons form
a clique, both connected sets see all five, and `K` is adjacent to `W`.
Thus `K` misses at least one shell label.

Because `K` misses `A`, every external neighbour of `K` lies in
`N_W(K)` or is one of the `5-m` contacted shell vertices.  This
neighbourhood separates `K` from `a union X_1 union X_2`.  Seven-
connectivity gives

\[
                         7\le |N_W(K)|+(5-m),
\]

which is (4.3).  QED.

Consequently every off-core component carrying a new `c`-portal is a
three-attachment `W`-bridge.  The unresolved geometry is no longer an
arbitrary block tree: its pendant lobes are all `X_2`-side lobes, while
every `c`-side lobe lies on a theta subgraph through the reserve core.  Crossing
attachment intervals of those multi-attachment bridges are the natural
society-cross input.  A complete proof still has to stabilize the bridges
before concluding that all noncrossing intervals give the compatible
rural outcome.

## 5. The exact remaining carrier lemma

Before asking for two carriers, one connected rainbow carrier already has
an exact rooted-model dichotomy.

### Theorem 5.1 (rainbow carrier contraction)

Let `P subseteq H-{a,b,c}` be connected and `Q`-rainbow, and let `p` be
the vertex obtained by contracting `P` in `H`.  At least one of the
following holds.

1. `G` has a `K_7` minor.
2. `H/P` is four-connected and planar, with `p,a,b,c` on one face.
3. There is a set `Y subseteq V(H)-P` with `|Y|<=2` such that

   \[
                         H-(P\cup Y)                 \tag{5.1}
   \]

   is disconnected.  Every component `K` of (5.1) satisfies

   \[
                         |N_H(K)\cap P|\ge4-|Y|.     \tag{5.2}
   \]

If `|P|=2`, outcome 3 in a seven-connected graph is an exact seven-cut:
necessarily `|Y|=2` and

\[
                         Q\cup P\cup Y              \tag{5.3}
\]

has order seven.

#### Proof

Put `J=H/P`.  Suppose first that `J` is four-connected.  Apply the
Fabila-Monroy--Wood rooted-`K_4` theorem to the four roots `p,a,b,c`.
If it gives a rooted model, lift the `p`-bag by replacing `p` with the
connected set `P`.  That bag is adjacent to every vertex of `Q` because
`P` is rainbow; the other three rooted bags contain `a,b,c`, each of
which is adjacent to all of `Q`.  The four lifted bags together with the
three singleton bags in `Q` give `K_7`.  The only alternative in the
rooted theorem is outcome 2.

If `J` is literally `K_4` on `p,a,b,c`, its four singleton vertices are
already the required rooted `K_4`; expanding `p` gives outcome 1 exactly
as above.  This case is separated because, under the standard convention,
`K_4` is not called four-connected although it has no separator of order
at most three.

Suppose now that `J` is neither four-connected nor `K_4`.  Then `J` has a
separator `Z` of order at most three with at least two components in
`J-Z`.  It must contain `p`: otherwise four-connectivity of `H-Z` would
make `J-Z` connected.  Put `Y=Z-{p}`.  Then `|Y|<=2` and expanding the
contraction gives (5.1).  For every component `K`, another component of
`H-(P union Y)` remains, so `N_H(K)` genuinely separates `H`; hence it
has order at least four.  All its neighbours outside `P` lie in `Y`,
proving (5.2).

Finally let `|P|=2`.  The set in (5.3) separates in `G` and has order at
most `3+2+2=7`.  Seven-connectivity forces its order to be at least seven,
so `|Y|=2` and (5.3) is exact.  QED.

Outcome 2 is the precise cofacial/rural branch.  Expanding `P` in the
face is legitimate exactly when its induced society has the compatible
rotation; otherwise `P` is the first local nonrural conflict.  Outcome 3
is the precise capacity branch.  Thus Theorem 5.1 supplies the desired

\[
              \boxed{K_7}\quad/\quad
              \boxed{\text{cofacial carrier}}\quad/\quad
              \boxed{\text{carrier-centred adhesion}}          \tag{5.4}
\]

without enumerating a portal row.

### The five-set target

For `i=1,2,3`, put

\[
 A_i=N_D(q_i),\qquad
 A_b=N_D(B_0),\qquad A_c=N_D(c).                    \tag{5.5}
\]

Every `A_i` meets both `X_2` and `X_3`; `A_b` meets both pieces; and
`|A_c|>=3` by Lemma 3.2.  Lemma 2.1 says it is enough to pack two
disjoint connected transversals of the five sets in (5.5); once they are
packed, a spanning-tree extension gives the connected adjacent partition
of all of `D`.

For completeness, the extension is elementary.  Contract the two
connected transversals to distinct vertices, take a spanning tree of the
contracted connected graph, and delete an edge on the path between the
two contraction vertices.  The two tree components lift to a partition
of `D` into adjacent connected sets containing the respective
transversals.  All five incidences are retained.

Thus the precise structural target is the following, with no Moser labels
other than the five terminal classes.

> **Five-set double-carrier lemma.**  Let a connected graph `D` have a
> two-shore presentation `D=X union Y`, where `X,Y` are connected and the
> relative `X-Y` separator order is at least three.  Let
> `A_1,A_2,A_3,A_4` each meet both shores, and let `A_5 subseteq Y` have
> order at least three.  Under the portal-minimality inherited from a
> first nonrural society, either `D` has two disjoint connected
> transversals of all five sets, or the society is rural in the forced
> order.

The phrase *portal-minimality* cannot simply be deleted.  Packing two
connected transversals of five arbitrary subsets is a genuine disjoint
Steiner-tree problem and does not follow from three-connectivity alone.
What Lemmas 3.1--3.2 prove is that every separator obstruction of order at
most two is already impossible in the exceptional shell.  The remaining
proof obligation is to use first-conflict portal minimality to show that a
failure with no such gate has the web/cofacial form; this conclusion does
not follow from relative three-connectivity alone.

## 6. Adversarial finite evidence and its exact status

The verifier `near_k7_double_rainbow_partition_search.py` uses pieces of
order four.  It repeatedly deletes optional edges until no further edge
can be removed while retaining the exact shell, `kappa(H)>=4` and
`kappa(G)>=7`.  Across 200 independently minimised expansions, the clean
partition of Lemma 2.1 always exists for the baseline portal assignment.

For five of those expansions the verifier also exhausts all `64^3`
minimal choices of one portal in each piece for each neutral vertex.  A
choice with a fourth triple-common portal is already closed by the
rooted-`K_4` common-core Corollary 1.4 in
`hadwiger_near_k7_nested_triangle_rooted_model.md`.  Among the remaining
choices, every failure of the displayed double partition makes the full
graph at most six-connected.  No seven-connected negative survived.

This is evidence for the five-set lemma, not its proof.  The rigorous new
content of this note is Lemmas 2.1, 3.1 and 3.2: they identify the exact
rooted model and prove that all separator obstructions of order at most
two are already excluded by the ambient hypotheses.
