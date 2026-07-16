# Internal audit of endpoint-contact rigidity at the order-eight boundary

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_star_order_eight_endpoint_contacts.md`
- final file SHA-256: `638a828fea99872346a2a880a22a76b3dc3d4bd66484be395f300c528ff51909`

The only change after the independently audited mathematical revision was
the status line linking this audit; the theorem, hypotheses, and proof are
unchanged.

This is a separate internal mathematical audit, not external peer review.  It
checks the construction and adjacency of all seven proposed branch sets, the
passage from a cut in the reduced graph to a separator in the original graph,
the connectivity convention needed for the rooted-minor theorem, the exact
statement of Fabila-Monroy--Wood Theorem 6, and the use of the second
five-clique.  I also tried to falsify the statement by realizing the planar
alternative and by maximizing the overlap of that five-clique with the
deleted vertices.

## 1. Setup and distinctness

The five vertices of `L` are distinct.  The four endpoints of `e` and `f`
are distinct and lie outside `L`.  Hence the nominated vertices

\[
                         \ell_e,\ \ell_f,\ a,\ b
\]

are distinct.  The set `W` constructed in the proof contains the three
vertices of `R` and, in only one case, the other endpoint `b'` of `f`.
It is therefore disjoint from all four nominated vertices.

Collective adjacency of `f=bb'` to a vertex `r in R` says that at least one
of `br,b'r` is present.  Consequently the two nonneighbour sets `M(b)` and
`M(b')` are disjoint.  Since their total order is at most three, one has
order at most one, so the relabelling of `b,b'` used in the proof is valid.

## 2. The three row sets

If `M(b)` is empty, the three sets are the singleton vertices of `R`.  If
`M(b)={r_0}`, the exceptional set is `{r_0,b'}`.  It is connected because
`br_0` is absent and collective adjacency forces `b'r_0` to be present.
The other two sets are singleton vertices of `R`.  Thus the three sets are
connected and pairwise disjoint.

They are pairwise adjacent through the clique `R`.  Each one is adjacent
to every nominated vertex:

- `ell_e` and `ell_f` are adjacent to its vertex in `R`, since `L` is a
  clique;
- `a` is adjacent to its vertex in `R` by the endpoint-contact hypothesis;
- `b` is adjacent to every ordinary singleton row; in the exceptional row
  it is adjacent to `b'` through the edge `f`.

These checks include the exceptional row and account for every adjacency
claimed in display (2.4).

If `K=G-W` contains a rooted `K_4` model at the four nominated vertices,
its four branch sets are disjoint from the three row sets.  The preceding
adjacency checks make every row set adjacent to each rooted branch set, and
the clique `R` makes the row sets pairwise adjacent.  These are all twenty-
one adjacencies required for a `K_7`-minor model.  Thus the exclusion of the
rooted model in the `K_7`-minor-free branch is justified.

## 3. Separator and connectivity calculation

Let `X` be a vertex cut of `K` with

\[
                         |X|\le 7-|W|.
\]

Because `K=G-W` is induced and `X` is disjoint from `W`, deleting
`W union X` from `G` leaves exactly `K-X`.  Two distinct components of
`K-X` therefore give two nonempty open sides of an actual separation of
`G` of order at most seven.  Seven-connectivity excludes orders at most
six, and order seven is an allowed conclusion of Theorem 2.1.

In the branch with neither conclusion, `K` has no vertex cut of order at
most `7-|W|`.  It follows that `K` is `(8-|W|)`-connected, including the
required order condition on `K`: the five vertices of `L` and the four
distinct endpoints of `e,f` already give nine vertices in `G`.  Hence

- if `|W|=3`, then `|K|>=6>5=8-|W|`; and
- if `|W|=4`, then `|K|>=5>4=8-|W|`.

Thus the proof does not silently call a graph with too few vertices
four- or five-connected.  In both cases `K` is in particular
four-connected.

## 4. Rooted-minor theorem

Theorem 6 of R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*, states
that for four distinct nominated vertices in a four-connected graph,
either the graph has a `K_4` minor rooted at them, or it is planar and the
four vertices lie on a common face.  The proof invokes it with four
distinct roots and the four-connectivity established above.  Since the
rooted-minor alternative was already converted into a `K_7` model, the
planarity conclusion follows exactly as claimed.  The later argument needs
only planarity, so it does not make any unsupported use of the common-face
part.

## 5. The second five-clique and the planar contradiction

The five-clique `Y` is disjoint from `L`, hence from all three vertices of
`R`.  The only vertex of `W-R` that can occur is `b'`.  Therefore deleting
`W` removes at most one vertex of `Y`, and `K` contains at least four
vertices of `Y`; they induce a literal `K_4`.

In any plane embedding of a graph containing a literal `K_4`, every
component outside that clique lies in a triangular face of the embedded
clique and can attach to the rest only through the three vertices bounding
that face.  The fourth clique vertex remains on the other side.  Hence the
bounding triangle is a vertex cut whenever an outside component exists.
A four-connected planar graph containing a literal `K_4` consequently has
no vertex outside it and equals that `K_4`.

This last possibility is impossible here in two independent ways.  The
four-connectivity convention requires more than four vertices, and the
four nominated vertices would themselves be all vertices of `K` and hence
would form the excluded rooted `K_4`.  The contradiction is therefore
valid even when `Y` overlaps the endpoints of `e` or `f` as much as the
hypotheses permit.

## 6. Consequent endpoint incidence types

In the surviving branch, applying Theorem 2.1 to each endpoint shows that
each endpoint misses at least one vertex of `R`.  For either distinguished
edge, collective adjacency to every vertex of `R` makes the two endpoint
nonneighbour sets disjoint.  Two nonempty disjoint subsets of a three-set
have sizes `(1,1)` or `(1,2)`, up to exchanging the endpoints.  No further
incidence type is possible.

## 7. Falsification attempt and scope

The most permissive apparent counterexample would make `K` planar, retain
exactly four vertices of `Y`, and place all other vertices inside faces of
that `K_4`.  Every such placement creates the three-vertex cut described in
Section 5; adjoining `W` turns it into a separator of `G` of order at most
seven.  It is therefore either forbidden by seven-connectivity or is
precisely the theorem's order-seven outcome.  Concentrating all possible
overlap of `Y` in `b'` still leaves four clique vertices and does not evade
this argument.  No counterexample survives the stated hypotheses.

The theorem does **not** eliminate the remaining `(1,1)` and `(1,2)`
endpoint-contact patterns, close the complete order-eight case, or prove
`HC_7`.  This audit credits only the endpoint-contact dichotomy and its
incidence consequence.
