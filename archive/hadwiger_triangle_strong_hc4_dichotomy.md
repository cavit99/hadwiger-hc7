# A triangle over a four-colourable core

## 1. General clique-extension lemma

We use the proved four-colour case of Holroyd's Strong Hadwiger
Conjecture (Martinsson--Steiner): if a graph (H) is four-colourable and
every proper four-colouring of (H) uses all four colours on a set
(X\subseteq V(H)), then (H) has an (X)-rooted (K_4)-minor, meaning
that each of the four branch sets contains a vertex of (X).

### Theorem 1.1 (strong-Hadwiger clique extension)

Fix integers (k\ge2) and (m\ge1), and assume Holroyd's Strong
Hadwiger Conjecture holds for (k).  Let (G) contain a clique

\[
                         T=\{q_1,\ldots,q_m\},
\]

and put (J=G-T).  If (J) is (k)-colourable, then either

\[
             \chi(G)\le k+m-1
             \qquad\hbox{or}\qquad
             G\succeq K_{k+m}.
\]

#### Proof

Let (X=\bigcap_{i=1}^m N_J(q_i)).  If every proper (k)-colouring of
(J) uses all (k) colours on (X), Strong Hadwiger gives an
(X)-rooted (K_k)-minor.  Its (k) bags, together with the (m)
singleton bags of (T), form a (K_{k+m})-model.

Otherwise choose a proper (k)-colouring of (J) with one colour,
renamed (0), absent from (X), and let (Z) be its colour-(0) class.
Introduce (m-1) new colours, one for each of
(q_2,\ldots,q_m).  For every (u\in Z\cap N(q_1)), choose an index
(j\ge2) for which (u\notin N(q_j)), and recolour (u) with the new
colour assigned to (q_j).  Such an index exists because (Z\cap X)
is empty.  The recolouring is proper: (Z) is independent and all the
new colours were absent from (J).

Now colour (q_1) with (0), and colour (q_2,\ldots,q_m) with their
pairwise distinct new colours.  Every old colour-(0) neighbour of
(q_1) was recoloured, and a vertex receiving the new colour of (q_j)
was chosen to miss (q_j).  The clique (T) also has distinct colours.
This is a proper (k+m-1)-colouring of (G).  \(\square\)

## 2. The four-colour/triangle specialization

### Theorem 2.1 (triangle/core dichotomy)

Let (G) contain a triangle

\[
                    T=\{q_1,q_2,q_3\},
\]

and put (J=G-T).  If (J) is four-colourable, then at least one of
the following holds:

1. (G) is six-colourable;
2. (G) contains a (K_7)-minor.

No connectivity, planarity, or cofaciality hypothesis is required.

### Proof

Let

\[
 X=N_J(q_1)\cap N_J(q_2)\cap N_J(q_3)
\]

be the common neighbourhood of the triangle in (J).

Suppose first that every proper four-colouring of (J) uses all four
colours on (X).  The strong four-colour theorem gives four pairwise
disjoint, pairwise adjacent connected branch sets in (J), each meeting
(X).  Every one of these branch sets is adjacent to every vertex of
(T).  Together with the three singleton branch sets
({q_1},{q_2},{q_3}), they form a (K_7)-model in (G).

Otherwise choose a proper four-colouring

\[
             c:V(J)\longrightarrow\{0,1,2,3\}
\]

for which one colour, renamed (0), is absent from (X).  Put

\[
                         Z=c^{-1}(0).
\]

The set (Z) is independent, and no vertex of (Z) is adjacent to all
three vertices of (T).  Introduce two new colours (4,5).  Recolour
each vertex (u\in Z\cap N(q_1)) as follows:

* if (u\notin N(q_2)), give (u) colour (4);
* otherwise give (u) colour (5).

The second rule is safe because such a vertex sees (q_1,q_2), but is
not in (X), and therefore misses (q_3).  All recoloured vertices came
from the independent set (Z), and colours (4,5) were previously
unused on (J), so the recolouring remains proper.

Finally give (q_1,q_2,q_3) the colours (0,4,5), respectively.  Their
triangle is properly coloured.  Every old colour-(0) neighbour of
(q_1) was recoloured; every new colour-(4) vertex was chosen to miss
(q_2); and every new colour-(5) vertex was proved to miss (q_3).
Thus no edge between (T) and (J) is monochromatic.  This is a proper
six-colouring of (G).  \(\square\)

## 3. Consequences for (HC_7)

### Corollary 2.1

In a seven-chromatic (K_7)-minor-free graph, deleting any triangle
leaves a graph of chromatic number at least five.  In particular, it
cannot leave a planar graph.

### Corollary 2.2

The planar-frame outcome of Theorem 2.10 in
`hadwiger_near_k7_two_complex_bag_round.md` is impossible in a
hypothetical counterexample to (HC_7).  This follows from Theorem 2.1
directly; the stronger cofacial conclusion is not needed for colouring.

## 4. Significance

The theorem turns a rooted-minor saturation statement into an exact
colour-or-minor dichotomy.  It is a reusable near-clique mechanism:

\[
 \text{triangle}+\text{four-colourable remainder}
 \quad\Longrightarrow\quad
 \text{six colours or }K_7.
\]

For the near-(K_7) split-versus-two-apex programme, it means that any
structural argument which makes the complement of one triangle
four-colourable already finishes the (HC_7) counterexample; it need not
identify the two apex vertices individually.
