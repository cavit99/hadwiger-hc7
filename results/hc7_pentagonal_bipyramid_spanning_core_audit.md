# Independent audit of the pentagonal-bipyramid spanning-core theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_pentagonal_bipyramid_spanning_core.md`](hc7_pentagonal_bipyramid_spanning_core.md)

**Audited SHA-256:**
`1eaa30dc1b8fa6e2865fbe36d5c80e988fb1f069edd6a661e1a280fb0cd37967`

This is an internal mathematical audit, not external peer review.  The
source proves an unbounded host-level normalization in the exceptional
pentagonal-bipyramid column case.  It does not prove the remaining rooted
model or boundary-colouring conclusion and does not prove `HC_7`.

## 1. Hypotheses and fixed branch sets

The source assumes a seven-connected, seven-chromatic, `K_7`-minor-free
graph whose every proper minor is six-colourable.  The two fixed root branch
sets are

\[
 R_0=G[\{v,p\}],\qquad R_1=G[\{w\}],
\]

and are connected and adjacent because `vp,pw` are edges.  They are
disjoint from seven pairwise disjoint connected columns, each adjacent to
both roots.  Hence any `K_5` model in a column-contact graph lifts with
`R_0,R_1` to an explicit `K_7` model.  This is the only lifting fact used in
the maximality argument.

## 2. Maximal-coverage absorption

The class of admissible enlargements is nonempty and finite, so maximizing
the total column order is legitimate.  Let `Z` be a component outside the
two roots and all seven maximal columns.

If `Z` met no column, its full neighbourhood would be contained in the
three root vertices, contradicting seven-connectivity.  Thus its set `A` of
contacted column labels is nonempty.

If `A` contains nonadjacent labels `i,j`, a path through the connected set
`Z` joins `L_i` to `L_j` with internal vertices outside every old branch
set.  Absorbing the path into `L_i` preserves disjointness, connectedness,
both root contacts and all old contacts, and adds `ij`.  It may add further
contacts if internal vertices have other column neighbours, but this causes
no problem: the new contact graph still contains `J+ij`.  Edge-maximality
of the pentagonal bipyramid then supplies a `K_5` minor and hence the
forbidden `K_7` lift.

Therefore `A` is a clique.  Absorbing all of `Z` into any contacted column
`L_i` creates no new column-contact edge: every label newly met by `Z`
belongs to `A` and is already adjacent to `i`.  The enlargement retains all
fixed subgraphs originally contained in `L_i` and strictly increases the
maximized total order.  This contradiction proves that the roots and seven
columns span `G`.

The proof does not assume that an outside component avoids the roots; root
contacts are harmless when it is absorbed into a column.

## 3. Connectivity and chromatic properties of the core

After deleting `v,p,w`, the induced graph `F` is partitioned by the seven
nonempty columns, so it has at least seven vertices.

If at most three vertices separated `F`, adjoining `v,p,w` to that set
would separate `G` with order at most six.  Hence `F` is four-connected.

If `F` were four-colourable, use four colours on `F`, one new common colour
on the nonadjacent vertices `v,w`, and a sixth colour on `p`.  This is a
proper six-colouring of `G`, so `chi(F)>=5`.  Vertex deletion makes `F` a
proper minor, hence `chi(F)<=6`.  The Four Colour Theorem then correctly
implies that `F` is nonplanar.

Likewise `G-{v,w}` is a six-colourable proper minor.  A five-colouring of it
would extend by assigning one fresh common sixth colour to the nonadjacent
vertices `v,w`.  Therefore its chromatic number is exactly six.

## 4. Four-cuts lift to full order-seven boundaries

If `X` is a four-vertex cut of `F`, then

\[
                       S_X=X\cup\{v,p,w\}
\]

has order seven and `G-S_X=F-X` has at least two components.  For any such
component `C`, all its outside neighbours lie in `S_X`.  If it missed one
literal vertex of `S_X`, then its full neighbourhood would have order at
most six and would separate `C` from another component, contradicting
seven-connectivity.  Hence every component of `G-S_X` is adjacent to every
vertex of `S_X`, and `S_X` is a full actual order-seven boundary.

This conclusion is deliberately nonterminal.  It does not supply matching
boundary equality partitions on two closed shores and therefore does not,
by itself, six-colour `G`.

## 5. Kelmans--Seymour branch

Four-connectivity of `F`, its order at least seven, and the absence of a
four-vertex cut imply that `F` is five-connected.  The source has already
proved that `F` is nonplanar.  The Kelmans--Seymour theorem applies at
exactly this scope: every five-connected nonplanar graph contains a
subdivision of `K_5`.  The cited final paper by He, Wang and Yu proves this
statement (arXiv:1612.07189; JCTB 144 (2020), 309--358).

The resulting subdivision is unlabelled.  Its five branch sets need not
each retain adjacency to both fixed roots after being selected inside `F`.
The source therefore correctly stops at the existence of a subdivision and
does not claim a `K_7` model.

## 6. Trust boundary and verdict

The source establishes the following exact dichotomy for the spanning
core:

1. a four-cut gives a full actual order-seven separation, without a common
   shore-colouring partition; or
2. the five-connected nonplanar core contains an unlabelled subdivision of
   `K_5`, without the required simultaneous root contacts.

Every branch-set, connectivity, colouring and theorem-scope inference is
valid at the audited hash.  The two missing label/colour conclusions are
stated rather than assumed.  **GREEN.**
