# Five-connected planar cores exclude support-five `K_4` models

**Status:** proved and independently audited.

This closes the standardized terminal-contraction branch in
[`hc7_support_six_terminal_contraction_three_root_reduction.md`](hc7_support_six_terminal_contraction_three_root_reduction.md).
The alleged simultaneous three-root obstruction cannot occur: a
five-connected planar core contains no `K_4` model on at most five
vertices, rooted or otherwise.

More generally, it proves that a two-apex pair in a seven-connected split
contraction pulls back to a support-at-most-six `K_5` transversal.  This
includes both the nonsplit and split-row responses.

## 1. Two elementary lemmas

### Lemma 1.1 (one contraction loses at most one unit of connectivity)

If `F` is `k`-connected and `e=uv` is an edge of `F`, then the simple
graph `F/e` is `(k-1)`-connected.

#### Proof

Let `w` be the contracted vertex and let `X` be a set of at most `k-2`
vertices of `F/e`.

If `w` is not in `X`, then `F-X` is connected, and its image under the
contraction is `(F/e)-X`.

If `w` is in `X`, then `(F/e)-X` is naturally isomorphic to

\[
 F-\bigl((X-\{w\})\mathbin{\cup}\{u,v\}\bigr).
\]

The set deleted on the right has order `|X|+1`, which is at most `k-1`,
so this graph is connected.  Thus deleting at most `k-2` vertices from
`F/e` never disconnects it.  \(\square\)

### Lemma 1.2 (a planar `K_4` has a separating triangle)

Let `F` be a planar graph containing a literal `K_4`.  If `F` has a
vertex outside that `K_4`, then `F` is not four-connected.

#### Proof

Restrict a plane drawing of `F` to the displayed `K_4`.  Its four
triangles bound the four regions of the sphere cut out by that drawing.
Every component of the graph outside the `K_4` lies in one of those
regions, and all its neighbours on the `K_4` lie in the boundary triangle
of that region.  Deleting that triangle separates the component from the
fourth vertex of the `K_4`.  \(\square\)

## 2. Support-five exclusion

### Theorem 2.1

Let `J` be a five-connected planar graph.  Then `J` has no `K_4` minor
model whose total support has order at most five.

#### Proof

By the standard convention for vertex connectivity, `|V(J)|>=6`.

A `K_4` model supported on four vertices is a literal `K_4`.  This is
impossible by Lemma 1.2 because `J` is four-connected and has vertices
outside the displayed clique.

Suppose instead that a model is supported on five vertices.  Its four
nonempty branch sets have size multiset

\[
                         (2,1,1,1).
\]

The two-vertex branch set is an edge `uv`.  Contract it.  The other three
singleton branch sets together with the contracted image of `uv` form a
literal `K_4` in `J/uv`.  Lemma 1.1 says that `J/uv` is four-connected;
it is planar and has at least five vertices.  This contradicts Lemma 1.2.
\(\square\)

The theorem is independent of how an external vertex meets the four
branch sets.  In particular, no external vertex can have a rooted `K_4`
model of support at most five in `J`.

## 3. Two-apex contraction pullback

### Theorem 3.1

Let `xy` be an edge of a graph `G`, let `H=G/xy`, and write `z` for the
contracted vertex.  Suppose `H` is seven-connected and `R` is a two-vertex
set such that `H-R` is planar.

1. If `z notin R`, then `R` meets every `K_5` model in `G` supported on
   at most six vertices.
2. If `R={z,r}`, then each of

\[
                       \{x,y\},\qquad \{x,r\},\qquad \{y,r\}
\]

meets every `K_5` model in `G` supported on at most six vertices.

#### Proof

Put `J=H-R`.  Deleting two vertices from a seven-connected graph leaves a
five-connected graph, so `J` is five-connected as well as planar.

First suppose `z notin R`, and let `M` be a `K_5` model of support at most
six in `G-R`.  If `x,y` are not in distinct branch sets of `M`, contracting
`xy` preserves five disjoint branch sets and produces a `K_5` model in the
planar graph `J`, a contradiction.

It remains to consider a split-row model, with `x` and `y` in distinct
branch sets.  Contracting the literal edge `xy` merges exactly those two
branch sets.  Together with the other three branch sets, their merged image
is a `K_4` model in `J`.  Its support has order at most five, because the
contraction identifies two support vertices.  This contradicts Theorem
2.1.  Thus no such `M` exists, proving item 1.

Now let `R={z,r}`.  Fix `q in \{x,y,r\}` and put
`P=\{x,y,r\}-\{q\}`.  The graph `G-P` consists of `J` together with the
single vertex `q`.  Suppose it has a `K_5` model `M` of support at most six.
The model must use `q`, since `J` is planar.

If the branch set containing `q` is the singleton `\{q\}`, deleting that
branch set leaves a `K_4` model in `J` supported on at most five vertices,
contrary to Theorem 2.1.  Otherwise the support bound and the five nonempty
branch sets force the bag-size multiset `(2,1,1,1,1)`, with `q` in the
two-vertex bag.  The other four bags are singleton vertices of `J` and form
a literal `K_4`, again contrary to Theorem 2.1.  Hence `P` is a transversal.
Applying this to all three choices of `q` proves item 2.  \(\square\)

### Corollary 3.2 (terminal three-root branch)

Under Proposition 2.1 of
[`hc7_support_six_terminal_contraction_three_root_reduction.md`](hc7_support_six_terminal_contraction_three_root_reduction.md),
all three pairs among `x,y,r` meet every support-at-most-six `K_5` model.

#### Proof

There `R={z,r}` and `H-R=G-\{x,y,r\}` is five-connected and
`K_5`-minor-free.  Wagner's four-connected theorem makes this remainder
planar, so Theorem 3.1(2) applies.  \(\square\)

## 4. Exact implication and trust boundary

This is a literal common two-vertex transversal outcome, not a `K_7`
construction.  It discharges every seven-connected contraction branch in
which the contracted graph has a planar two-apex pair.  A five-connected
`K_5`-minor-free remainder is planar by Wagner's theorem and is therefore
included.

The proof does **not** address:

* a remainder of connectivity only four;
* rooted `K_4` models using six or more vertices;
* the neutral nonterminal branch of the contraction pullback; or
* the exact-seven-separation branch when the contraction is not
  seven-connected.

No enumeration, embedding uniqueness, or rooted-minor characterization is
used.

## 5. Sharpness checks

Both numerical hypotheses in Theorem 2.1 are tight.

* Four-connectivity is insufficient.  In the octahedral graph, the edge
  bag `\{0,1\}` and singleton bags `\{2\},\{4\},\{5\}` form a `K_4`
  model on five vertices (in the standard NetworkX labelling).
* Support six is possible in a five-connected planar graph.  In the
  icosahedral graph, the connected bag `\{0,8,2\}` and singleton bags
  `\{1\},\{5\},\{6\}` form a `K_4` model on six vertices.

These examples are sanity checks only; the proof of the theorem is
structural and does not depend on their computation.
