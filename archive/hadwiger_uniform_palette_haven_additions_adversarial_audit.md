# Adversarial audit of the component-palette and artificial-source additions

## Verdict

**Theorem 4.0 is GREEN.  Theorem 2.2 is GREEN in every nonvacuous case
and in every use made by Theorem 4.0, but its literal statement needs a
one-line domain repair.**  No flaw was found in the directed Menger cut,
the artificial-colour accounting, the Rado transversal, or the
first-hit branch-set construction.

The literal exception is `X=V(H)`.  Then `H-X` has no component, while
Theorem 2.2 asserts that some component exists.  This can occur in the
stated setting: take `G=K_3`, `r=2`, let `v` be one vertex, and put
`X=V(H)`.  Here the free palette is empty, so the desired containment is
vacuous but there is no component in which to realize it.  Replace
"for every `X subseteq V(H)`" by either

* "for every `X` with `H-X` nonempty", or
* "if `[r]-c(X)` is nonempty, some component ...; if it is empty the
  conclusion is vacuous."

This does **not** affect Theorem 4.0: there `|X|<r` and the existing
`K_r` model forces `|V(H)|>=r`, so `H-X` is nonempty.

## 1. Independent component permutations (Theorem 2.2)

Let the components of `H-X` be `K_i`, let `F=[r]-c(X)`, and let
`P_i=c(N cap K_i) cap F`.  A separate permutation of `F` on each
component is legal:

1. it is a bijective recolouring on every internal edge;
2. components of `H-X` are pairwise anticomplete; and
3. every colour occurring on `X` is fixed, while no colour of `F`
   occurs on `X`.

If `a=max |P_i|`, every `P_i` can be injected into one fixed `a`-set
`Q subseteq F`, and each injection extends to a permutation of `F`.
The recoloured neighbourhood then uses at most `|c(X)|+a` colours.
Every proper `r`-colouring of `H` must use all `r` colours on `N`, or
the omitted colour extends to `v`.  Hence

`r <= |c(X)|+a <= |c(X)|+|F|=r`,

so `a=|F|`, and one original `P_i` was all of `F`.  Notice that the
proof does not merely show that the recoloured component carries the
palette: equality `|P_i|=|F|` proves this for the original colouring.

## 2. Failure of the adhesion outcome implies full palette in the model haven

For `|X|<r`, Theorem 2.2 supplies a component `K` carrying every free
colour.  If the model-haven component `M=beta_M(X)` omits a free colour,
then `K` and `M` are necessarily distinct and give outcome 1 of Theorem
4.0.  Therefore failure of outcome 1 indeed implies, with the correct
universal quantifier, that `beta_M(X)` carries every colour outside
`c(X)` for every `|X|<r`.

## 3. Directed Menger with endpoint cuts

Fix `J` of size `j`.  If `j` disjoint directed paths from the artificial
source set `S` to the target union do not exist, directed set-Menger
gives a vertex hitting set `Z` with `p=|Z|<j`.  It is legitimate for
`Z` to contain sources, neighbourhood vertices, or target vertices.
Writing

`C={gamma : s_gamma in Z}` and `X=Z cap V(H)`

accounts for every vertex of `Z`, so `|C|+|X|=p`.  At most `|X|<j`
of the `j` disjoint target bags meet `X`; choose a target bag `B_i`
disjoint from `X`.  It lies wholly in `beta_M(X)`.

Since `|C union c(X)|<=|C|+|X|=p<r`, choose
`gamma notin C union c(X)`.  Full palette alignment gives a vertex
`n_gamma in N cap beta_M(X)`.  Both `s_gamma` and `n_gamma` avoid `Z`.
The arc `s_gamma n_gamma`, followed by an undirected path inside the
model-haven component (using the two directed orientations of every
edge) to `B_i`, avoids `Z`.  This contradicts the hitting property.

Thus allowing endpoint vertices in the Menger cut creates no gap:
source deletions are paid for by `C`, and target deletions cannot hit all
`j` disjoint bags with fewer than `j` vertices.

## 4. Gammoid and Rado

Take the gammoid on ground set `V(H)` whose independent sets are those
linkable from the artificial sources in the directed auxiliary graph
(or reverse all arcs if using the sink-set convention for strict
gammoids).  The preceding argument proves

`rank(union_{i in J} B_i) >= |J|`

for every subfamily of the `r` bags.  These are exactly Rado's
matroid-transversal inequalities.  Rado therefore gives one distinct
representative from every bag and an `r`-linkage from `S` to those
representatives.  Because there are exactly `r` sources and `r`
vertex-disjoint paths, every artificial source is used.

Deleting each path's first artificial arc leaves disjoint paths whose
initial vertices are distinct vertices of `N`, one in each colour.
Zero-length residual paths are harmless when a chosen neighbourhood
vertex is already its representative.

## 5. First model hits

Truncate each residual path at its first vertex in the union of the old
model bags.  Before that vertex the path is disjoint from every old bag.
If the `r` first-hit labels are distinct, they exhaust the `r` bag
labels.  Adding each model-free prefix to its first-hit bag preserves:

* connectedness of that bag;
* pairwise disjointness of all bags; and
* every pre-existing interbag edge.

Each bag then contains a distinct neighbourhood root, yielding an
actual `N`-meeting `K_r` model.

If two first-hit labels coincide, path disjointness makes both roots
and both first-hit vertices distinct.  Adding the two prefixes to that
one bag gives exactly the asserted double-hit certificate.  No claim is
made that this second outcome alone is a cleaned `N`-meeting model.

## 6. Minor editorial repair

After inserting Theorem 2.2, the proof of the later exact-trace haven
still cites "Corollary 2.2".  There is no longer a Corollary 2.2.  It
may cite Theorem 2.2 directly (a component carrying every free colour
contains every free uniquely-coloured root) or Corollary 2.3.

Subject to the vacuous-component and citation repairs above, the two
new additions withstand this audit.
