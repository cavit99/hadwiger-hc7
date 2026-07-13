# Clique palette recycling and colourful common neighbourhoods

The triangle/four-colour argument is an instance of a general elementary
recolouring lemma.  Only its rooted-minor endpoint depends on Strong
Hadwiger.

## Theorem 1 (clique palette recycling)

Let (G) contain a clique

\[
   Q=\{q_1,\ldots,q_r\},\qquad r\ge2,
\]

and put (H=G-Q).  Suppose (H) is (k)-colourable, and let

\[
   X=\bigcap_{i=1}^{r}N_H(q_i)
\]

be the common neighbourhood of (Q) in (H).  Then at least one of the
following holds:

1. (G) is ((k+r-1))-colourable;
2. every proper (k)-colouring of (H) uses all (k) colours on (X).

#### Proof

Suppose (2) fails.  Choose a proper (k)-colouring of (H) and rename an
absent colour on (X) as colour (0).  Let (Z) be its colour class.
Thus (Z) is independent and no vertex of (Z) is adjacent to all of
(Q).

Introduce (r-1) fresh colours (f_2,\ldots,f_r).  For each
(u\in Z\cap N(q_1)), choose an index (j(u)\in\{2,\ldots,r\}) such that
(u\notin N(q_{j(u)})), and recolour (u) with (f_{j(u)}).  Such an
index exists because (u\notin X).  The recolouring is proper: all changed
vertices belonged to the independent set (Z), and the new colours were
absent from (H).

Now colour (q_1) with (0), and colour (q_j) with (f_j) for
(2\le j\le r).  The clique (Q) gets distinct colours.  Every old
colour-zero neighbour of (q_1) was recoloured, and a vertex recoloured
(f_j) was chosen to miss (q_j).  This is a proper colouring of (G)
with (k+r-1) colours.  \(\square\)

## Corollary 2 (Strong-Hadwiger endpoint)

Under the hypotheses of Theorem 1, suppose the Strong Hadwiger statement
is known for (k): whenever a (k)-colourable graph has a set (X) which
takes all (k) colours in every (k)-colouring, it has an
(X)-rooted (K_k)-minor.  Then

\[
   \chi(G)\le k+r-1
   \quad\hbox{or}\quad
   K_{k+r}\preccurlyeq G.
\]

Indeed, in outcome (2), the (k) rooted branch sets are each adjacent to
all (r) singleton vertices of (Q), so together they form a
(K_{k+r})-model.

For (k=4), Strong Hadwiger is the theorem of Martinsson--Steiner.  Taking
(r=3) gives

\[
   \chi(G-T)\le4
   \quad\Longrightarrow\quad
   \chi(G)\le6\ \text{ or }\ K_7\preccurlyeq G,
\]

the exact endpoint used in the near-(K_7) planar-frame branch.

## Corollary 3 (uniform critical saturation)

Let (G) be a graph with

\[
   \chi(G)>k+r-1
\]

and let (Q\cong K_r) be such that (G-Q) is (k)-colourable.  Then the
common neighbourhood (X) of (Q) is (k)-colourful in (G-Q): it sees
all (k) colours in every proper (k)-colouring.

This conclusion is unconditional and label-free.  It identifies precisely
which model-meeting statement would finish the corresponding clique
extension at larger (k), without assuming that statement as a routine
linkage lemma.

