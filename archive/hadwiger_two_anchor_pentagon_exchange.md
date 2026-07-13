# Two-anchor pentagon exchange: common state or a rooted triangle

## 1. Setting

Let \(G\) be a hypothetical \(7\)-contraction-critical,
\(K_7\)-minor-free graph. Let \(v\) have degree seven, put
\[
 N=N_G(v),
\]
and assume
\[
                 G-N[v]=C_1\mathbin{\dot\cup}C_2,
\tag{1.1}
\]
where both exterior components are full to \(N\).

Fix an independent pair \(I\subseteq N\), put \(U=N-I\), and assume

\[
                         \overline{G[U]}\cong C_5. \tag{1.2}
\]

This is label-free; in the pure-Moser normalization one takes
\(I=\{1,3\}\).

For an edge \(J\) of the missing cycle (1.2), the three vertices of
\(U-J\) induce a two-edge path in \(\overline{G[U]}\). Denote its two
edges by \(K_J^1,K_J^2\).

## 2. One input edge

### Lemma 2.1 (matching state or double support)

Fix distinct \(h,k\in\{1,2\}\) and an edge \(J\) of the missing
\(C_5\). Contract the two disjoint connected sets

\[
                         \{v\}\cup I,\qquad C_h\cup J.
\tag{2.1}
\]

Then \(G-(\{v\}\cup C_h)\) has a six-colouring whose state on \(N\)
has \(I,J\) as exact, distinctly coloured blocks. In that colouring,
one of the following holds.

1. The state on \(N\) is
   \[
                         I\mid J\mid K\mid\{r\},   \tag{2.2}
   \]
   where \(K\in\{K_J^1,K_J^2\}\).
2. For each \(\ell\in\{1,2\}\), there is a path joining the ends of
   \(K_J^\ell\) whose interior lies in \(C_k\). Both paths occur in
   the same colouring.

#### Proof

The two contraction sets in (2.1) are adjacent, through the edges from
\(v\) to the two vertices of \(J\). Their images therefore receive
distinct colours. Fullness makes every boundary vertex outside \(I\)
adjacent to the first image and every boundary vertex outside \(J\)
adjacent to the second. Expanding only \(I,J\) and deleting the two
anchor interiors gives exact, distinct traces for those blocks on the
remaining side \(N\cup C_k\).

The three vertices of \(U-J\) avoid both anchor colours. If two of them
share a colour, they form a nonedge \(K_J^\ell\), because a colour
class is independent, and (2.2) holds.

Suppose the three colours are distinct. For
\(K_J^\ell=xy\), consider the two-colour subgraph on the colours of
\(x,y\). If \(x,y\) lie in different components, swap the two colours
on the component containing \(x\). No other boundary vertex has either
colour, so this merges exactly \(x,y\) and gives (2.2).

If no such swap works for either \(\ell\), both endpoint pairs lie in
their corresponding two-colour components. Choose a shortest path for
each. Its interior avoids \(N\), because its two endpoint colours occur
on no other boundary vertex. The only graph remaining outside \(N\) is
\(C_k\), so both path interiors lie in \(C_k\). This is outcome 2.
\(\square\)

### Corollary 2.2 (the support outcome is a rooted triangle)

In outcome 2, \(G[C_k\cup(U-J)]\) contains a
\((U-J)\)-rooted \(K_3\)-model.

#### Proof

Write the complementary missing path as \(x-y-z\). The two supplied
paths make a connected subgraph containing \(x,y,z\). The edge \(xz\)
is present in \(G[U]\), since \(xz\) is not an edge of the missing
path. Take an inclusion-minimal tree in the connected union spanning
\(x,y,z\). Assign its unique branch region to the \(y\)-bag and its
two terminal arms to the \(x\)- and \(z\)-bags. The two tree edges make
the \(y\)-bag adjacent to the other two, and the boundary edge \(xz\)
makes those two adjacent. This is the rooted triangle. \(\square\)

## 3. The five-state incidence cycle

The matchings of order three in \(\overline{G[N]}\) containing \(I\)
form five states. Each missing-cycle edge \(J\) belongs to exactly two
of them, according to the choice
\(K\in\{K_J^1,K_J^2\}\). The resulting incidence graph between input
edges \(J\) and matching states is a \(10\)-cycle; equivalently, the
five matching states themselves form a \(C_5\), with \(J\) represented
by the edge joining its two possible normalized states.

### Theorem 3.1 (bilateral pentagon exchange)

At least one application of Lemma 2.1, over the two choices of target
shore and the five edges \(J\), has the double-support outcome 2.
Consequently one exterior shore contains the rooted triangle of
Corollary 2.2 in a two-anchor exact-trace colouring.

#### Proof

Suppose every application normalizes to a matching state. For
\(i=1,2\), let \(\mathcal A_i\) be the matching states which extend to
\(G[N\cup C_i]\).

For each input edge \(J\), anchor the opposite shore and apply Lemma
2.1 with target \(C_i\). The resulting state is one of the two matching
states incident with \(J\), and belongs to \(\mathcal A_i\). Hence
\(\mathcal A_i\) is a vertex cover of the five-cycle of matching
states. Therefore
\[
                         |\mathcal A_i|\ge3.
\]

Two subsets of a five-element set, each of order at least three,
intersect. Choose
\[
                         \Pi\in\mathcal A_1\cap\mathcal A_2.
\]
Colour the two exterior sides with exact state \(\Pi\), permute colours
so corresponding blocks agree, and glue across \(N\). The state
\(\Pi\) has four blocks on \(N\), so at least one colour of the
six-colour palette is absent from \(N\); assign it to \(v\). This
six-colours \(G\), a contradiction. \(\square\)

## 4. What this closes and what remains

The theorem proves a genuine capacity--state exchange in the smallest
two-exterior equality cell:

\[
 \boxed{\text{common exact matching state}\quad\text{or}\quad
        \text{one-shore rooted triangle}.}
\]

The common-state outcome is impossible by colouring, so the rooted
triangle is forced. It is stronger than an arbitrary missing-edge path:
two incident missing edges are packaged simultaneously in one shore and
one colouring.

For the pure-Moser contact lock, the unresolved step is to combine this
rooted triangle on \(U-J\) with:

* the opposite full-shore carrier for \(J\); and
* a connector for the fixed pair \(I\),

while keeping the six branch sets disjoint. This is precisely the
reserved-connector problem, now with the other three unique roots already
packaged as a rooted \(K_3\). No five-way transition family remains in
this branch.
