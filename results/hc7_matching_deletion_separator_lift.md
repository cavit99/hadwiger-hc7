# Matching deletion: the exact separator budget

**Status:** proved and independently cold-audited.

This note records the separator law on the common deletion of several
split edges.  It is a graph-theoretic statement, independent of colouring
or of the particular `K_5` models from which the edges arose.

## 1. The separator budget

Let `F` be a matching in a graph `G`, and put `K=G-F`.  For a separation
`(A,B)` of `K`, write

\[
 S=A\cap B,\qquad L=A-B,\qquad R=B-A,
\]

and let

\[
 F(L,R)=\{uv\in F:u\in L,\ v\in R\}.
\]

### Theorem 1.1 (matching-deletion separator budget)

If `G` is `k`-connected and both `L` and `R` are nonempty, then

\[
                  |S|+|F(L,R)|\ge k.                 \tag{1.1}
\]

If equality holds, then for every `a in L` and `b in R` there are `k`
internally vertex-disjoint `a`--`b` paths in `G`, and every such family
of `k` paths has the following exact form:

1. `|S|` paths meet `S`, each in a different vertex of `S`;
2. `|F(L,R)|` paths avoid `S`, each uses a different edge of `F(L,R)`;
3. no path both meets `S` and uses an edge of `F(L,R)`, and no path uses
   two edges of `F(L,R)`.

#### Proof

By `k`-connectivity, the local form of Menger's theorem gives `k`
internally vertex-disjoint `a`--`b` paths in `G`.

Every `a`--`b` path which avoids `S` must use an edge of `F(L,R)`: after
all edges of `F` are deleted there is no edge of `K` from `L` to `R`.
In an internally vertex-disjoint family, at most `|S|` paths can meet
`S`.  Since `F` is a matching, at most `|F(L,R)|` further paths can avoid
`S`: two such paths cannot use the same crossing edge without sharing an
internal vertex, except when that edge is the single-edge path `ab`, in
which case it still accounts for only one path.  Hence every internally
disjoint family has order at most `|S|+|F(L,R)|`.  This proves (1.1).

If equality holds, a family of `k` paths must attain both upper bounds.
It therefore uses every boundary vertex once and every crossing matching
edge once.  A path consuming both kinds of resource, or two crossing
edges, would leave at most `k-1` paths after the remaining resources are
allocated.  This proves all three assertions.  \(\square\)

### Corollary 1.2

If `G` is `k`-connected and `F` is a matching of order `m`, then

\[
                         \kappa(G-F)\ge k-m.           \tag{1.2}
\]

For `k=7` and `m=3`, the graph `K=G-F` is four-connected.  Moreover,
every separation of `K` of order

* four is crossed by all three edges of `F`;
* five is crossed by at least two edges of `F`; and
* six is crossed by at least one edge of `F`.

Every exact four-separation is tight in Theorem 1.1, so its seven-path
families saturate its four boundary vertices and its three crossing rows.

#### Proof

If `G-F` had a separation of order below `k-m`, then (1.1) would give

\[
          k\le |S|+|F(L,R)|\le |S|+m<k,
\]

a contradiction.  The remaining assertions are the same inequality with
`k=7,m=3`.  \(\square\)

## 2. Literal lift of a tight deletion separation

The budget also gives an actual separator of the original graph; no
contracted or virtual boundary vertex is involved.

### Lemma 2.1 (literal lift)

Let `(A,B)` be a separation of `K=G-F`, and put `C=F(L,R)`.  Select one
endpoint of every edge in `C`, and call the selected set `X`.  Then

\[
                            S^+=S\cup X               \tag{2.1}
\]

has order `|S|+|C|`, and there is no edge of `G-S^+` between
`L-X` and `R-X`.

If both `L-X` and `R-X` are nonempty, `S^+` is therefore the boundary of
an actual separation of `G`.  In particular, every exact four-separation
of `G-F` for a three-edge matching has a literal order-seven lift: choose
the three endpoints so that at least one endpoint is left unselected in
each open shore.

#### Proof

The only edges of `G` from `L` to `R` belong to `C`, and the selection
deletes one endpoint of every such edge.  This proves the first assertion.

For the last assertion, all three edges cross by Corollary 1.2.  If an
open shore contains a vertex which is not an endpoint of `C`, it remains
nonempty for every selection.  If not, it consists of some or all of the
three pairwise distinct endpoints on that side.  Because there are three
crossing edges, choose endpoints from both sides, leaving at least one
unselected endpoint on each shore.  Thus both residual shores are
nonempty.  \(\square\)

## 3. Model-preserving choice for a split `K_5` support

Suppose an edge `xy in F(L,R)` is the two-vertex bag of a support-six
`K_5` model, let `Q` be its four singleton bags, and assume that no edge
of `F-{xy}` has both ends in `Q`.  Then `Q` remains a clique in `G-F`, so
all vertices of `Q-S` lie in at most one open shore.  The additional
assumption is automatic when the named model supports are pairwise
vertex-disjoint, which is the application below.

### Lemma 3.1 (preferred endpoint)

If `Q-S` is nonempty and lies in `L`, selecting `y in R` into the lifted
boundary makes the entire support `Q union {x,y}` lie in the left closed
shore.  Symmetrically, if `Q-S subseteq R`, select `x`.  If `Q subseteq S`,
either selection preserves the model in the closed shore containing the
unselected endpoint.

#### Proof

After `y` is moved into the boundary, `Q union {x,y}` is contained in
`L union S union {y}`.  The other cases are symmetric.  \(\square\)

Thus every crossing split model supplies a preferred endpoint choice for
the literal lift.  The only obstruction to obtaining an **actual**
model-preserving exact-seven handoff from an exact four-separation is that
all preferred choices delete an entire open shore.  This is now a sharply
defined exceptional geometry, rather than an unranked separator loss.

## 4. The exceptional geometry is impossible

The apparent exception in Section 3 disappears in the `HC_7` setting.
The only external input is the following theorem of Fabila-Monroy and
Wood: if four prescribed vertices in a four-connected graph do not root a
`K_4` minor, then the graph is planar and the four vertices lie on a
common face.

### Theorem 4.1 (model-preserving four-cut lift)

Let `G` be seven-connected and `K_7`-minor-free.  Let

\[
                        F=\{x_i y_i:1\le i\le3\}
\]

be a matching, where every `x_i y_i` is the two-vertex bag of a named
support-six `K_5` model with four singleton bags `Q_i`, and suppose these
three named supports are pairwise vertex-disjoint.  If `G-F` has an exact
four-separation, then `G` has an actual exact-seven separation which
contains each named support `Q_i union {x_i,y_i}` in one of its two closed
shores.

The separation has a literal model-side map.  After fixing one root in
each open shore, minimum open-shore order within that anchored side-map
class is therefore a well-founded rank under exact-seven uncrossing.

#### Proof

Let `(A,B)` be an exact four-separation of `G-F`, with boundary `S` and
open shores `L,R`.  Corollary 1.2 says that all three edges of `F` cross
the shores.  Relabel their ends so that `x_i in L` and `y_i in R`.

For each `i`, the clique `Q_i` has off-boundary vertices in at most one
shore.  Use Lemma 3.1 to select the endpoint opposite that shore; if
`Q_i subseteq S`, either choice is legal.  These three selected endpoints,
together with `S`, separate the two residual shores in `G` and preserve
every named model in a closed shore.  If both residual shores are
nonempty, this is the required exact-seven separation.

Suppose no legal choice leaves both shores nonempty.  Orient the
separation so that the selected endpoints exhaust `R`.  Then necessarily

\[
             R=\{y_1,y_2,y_3\},\qquad
             \varnothing\ne Q_i-S\subseteq L
             \quad(1\le i\le3).                     \tag{4.1}
\]

Indeed, the three crossing edges give three distinct endpoints in `R`,
so an exhausted shore contains exactly those endpoints.  If some
`Q_i subseteq S`, selecting `x_i` instead would leave `y_i` in `R` and
would still preserve that model, contrary to the assumed failure.

In `G`, a vertex `y_i` can have neighbours only among the four vertices
of `S`, the other two vertices of `R`, and its matching partner `x_i`:
all other `L`--`R` edges are absent from `G-F` and do not belong to `F`.
Since `G` is seven-connected, its minimum degree is at least seven.
Consequently all seven possible neighbours occur.  Thus `R` is a
triangle complete to `S`.

Put `H=G-R`.  Deleting three vertices from a seven-connected graph leaves
`H` four-connected.  If `H` contained a `K_4` minor rooted at the four
literal vertices of `S`, its four rooted bags together with the three
singleton bags in `R` would form a `K_7` model: `R` is a triangle and is
complete to every root.  Hence no such rooted minor exists.  The
Fabila-Monroy--Wood theorem therefore makes `H` planar.

The degree sum in `H` is now impossible.  The four vertices of `S` lose
exactly the three neighbours in `R`, so they have degree at least four in
`H`.  The three distinct vertices `x_i` lose only their corresponding
neighbour `y_i`, so they have degree at least six.  Every other vertex of
`H` has no neighbour in `R` and hence degree at least seven.  Writing
`n=|V(H)|` (so `n>=7`) gives

\[
 \sum_{v\in V(H)}d_H(v)
   \ge 4\cdot4+3\cdot6+7(n-7)=7n-15.                \tag{4.2}
\]

But a simple planar graph has degree sum at most `6n-12`, whereas
`7n-15>6n-12` for `n>=7`.  This contradiction eliminates (4.1), and the
literal model-preserving exact-seven lift always exists.  The final rank
statement is the standard anchored separation-submodularity argument:
retain the two roots and the side assignment of the three named supports,
and minimize one rooted open shore.  \(\square\)

## 5. Exact colouring signatures make the lift uniform

The preceding four-cut proof did not use contraction-criticality.  In a
strongly contraction-critical graph, the proper-minor colourings give a
more general lifting theorem.

Say that `(G,F)` has the **exact matching-signature property with `p`
colours** if, for every nonempty `D subseteq F`, the graph `G-F` has a
`p`-colouring in which the ends of an edge of `F` have the same colour
exactly for the edges in `D`.

If every proper minor of `G` is `p`-colourable and `F` is a matching,
this property is automatic: colour `G/D`, expand the contracted vertices,
and delete all edges of `F`.  The uncontracted matching edges remain
present in `G/D` and therefore have differently coloured ends.

### Theorem 5.1 (derangement lift)

Let `G` be `k`-connected and not `(k-1)`-colourable, let `F` be a
matching, and suppose `(G,F)` has the exact matching-signature property
with `k-1` colours.  Let `(A,B)` be a separation of `K=G-F`, and put

\[
             q=|F(L,R)|,\qquad |S|+q=k.               \tag{5.1}
\]

If `q>=2`, then **every** selection `X` of one endpoint of each edge in
`F(L,R)` leaves both `L-X` and `R-X` nonempty.  Consequently `S union X`
is the boundary of an actual exact-`k` separation of `G`.

#### Proof

Suppose, by symmetry, that `L-X` is empty.  Then `L=X` has exactly `q`
vertices.  Every `v in L` has possible neighbours only in

* the other `q-1` vertices of `L`;
* the `k-q` vertices of `S`; and
* its unique matching mate in `R`.

This is a total of `k` possible neighbours.  Since `delta(G)>=k`, every
such edge is present.  In particular, `L` is a clique complete to `S`.

Use the exact matching signature for the nonempty set `F(L,R)`.  In the
resulting `(k-1)`-colouring of `K`, the `q` vertices of the clique `L`
have distinct colours, their matching mates have the corresponding same
colours, and no vertex of `S` uses any of those `q` colours.  Because
`q>=2`, permute the colours on `L` by a fixed-point-free permutation.
Edges inside `L` and from `L` to `S` remain proper.  Every crossing
matching edge becomes proper.  No other edge from `L` to `R` exists, and
every noncrossing edge of `F` was already proper in the exact signature.
Thus the recolouring is a `(k-1)`-colouring of `G`, a contradiction.
\(\square\)

The universal quantifier over endpoint selections is important.  It lets
one choose the endpoint required to preserve each named split model; the
resulting lift cannot accidentally erase a shore.

## 6. The weighted separation order

For a separation `(A,B)` of `K=G-F`, define

\[
       \lambda_F(A,B)=|A\cap B|+|F(A-B,B-A)|.          \tag{6.1}
\]

### Theorem 6.1 (submodularity)

The function `lambda_F` is submodular on the separation lattice.  Thus,
for separations `(A,B)` and `(C,D)`,

\[
 \lambda_F(A,B)+\lambda_F(C,D)
 \ge
 \lambda_F(A\cap C,B\cup D)+
 \lambda_F(A\cup C,B\cap D).                         \tag{6.2}
\]

#### Proof

Subdivide every edge `e in F` once, with new vertex `w_e`, and call the
resulting graph `K^*`.  A separation of `K` extends to a separation of
`K^*` whose boundary has minimum possible order `lambda_F`: put `w_e` in
the boundary exactly when the ends of `e` lie in opposite open shores;
otherwise it can be put on a compatible closed side without enlarging the
boundary.

Take minimum-order extensions in `K^*` of the two separations in (6.2).
Ordinary separation order is submodular.  Their meet and join restrict on
`V(K)` to the meet and join displayed in (6.2), while their orders are at
least the minimum extension orders of those restrictions.  Inequality
(6.2) follows.  \(\square\)

Theorem 1.1 says that `lambda_F>=k` on every actual separation when `G`
is `k`-connected.  Consequently two oriented exact-`lambda_F=k`
separations which preserve the same literal roots and named-model side
map uncross to two more exact weighted separations of order `k`.  Their
intersected rooted open shore is a proper subset whenever the original
oriented shores are nonnested.  Rooted open-shore order is therefore a
genuine well-founded rank on this weighted handoff class.

## 7. Consequence for three disjoint split models

Let `G` now be a hypothetical minor-minimal `HC_7` counterexample, and
let `F` be the three split edges of three pairwise vertex-disjoint
support-six `K_5` models.  Put `K=G-F`.

* `K` is four-connected by Corollary 1.2.
* Every exact four-separation of `K` has weighted order seven and all
  three split rows cross it.
* Choose for each row the endpoint opposite the shore containing its
  singleton `K_4`.  Theorem 5.1 says that this particular choice gives an
  actual exact-seven separation of `G`, and all three named models lie in
  declared closed shores.
* The weighted submodularity theorem gives the anchored strict rank.

Hence the entire `kappa(K)=4` branch returns an accepted, ranked,
model-preserving exact-seven handoff.  If that handoff is absent, then

\[
                             \kappa(K)\ge5.            \tag{7.1}
\]

In the latter branch, `K-Q_i` is connected for every singleton clique
`Q_i`.  It therefore contains an `x_i`--`y_i` path avoiding `Q_i`.
That path, as one connected branch bag, together with the four singleton
bags of `Q_i`, regenerates the named `K_5` model entirely inside the one
common deletion graph `K`.

Combined with the punctured-cube chromatic fork, the unresolved kernel is
now exactly a five-connected graph `K` with `chi(K) in {5,6}`, carrying
all seven non-all-proper matching signatures and three regenerated labelled
`K_5` models.  The regenerated path bags need not be disjoint; composing
them, rather than extracting another unranked separator, is the next gap.

## 8. Trust boundary

The weighted order is the first global rank in this route which retains
both separator geometry and the split-edge cost.  The exact-signature
theorem closes every weighted-order-seven lift with at least two crossing
rows.  It does not turn the seven punctured-cube signatures into the
missing all-proper signature in the five-connected residue.

For a single crossing row (`q=1`), a model-preserving preferred endpoint
can still erase a singleton shore; no colour derangement exists.  This is
the isolated one-row lock already represented by the noncontractible
split-edge handoff.  It is not a reason to reopen general portal or Moser
casework.
