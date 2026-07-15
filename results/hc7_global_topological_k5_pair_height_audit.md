# Audit of the global topological-`K_5` pair height

## Verdict

**GREEN for the proved normalization; OPEN and `HC_7`-strength for the
exchange target.**  Propositions 2.1, 3.1 and 4.1 in
[`hc7_global_topological_k5_pair_height.md`](hc7_global_topological_k5_pair_height.md)
are correct.  The parameter has an exact terminal and its first finite rung
has genuine path geometry, but no monotone pair exchange has been proved.
Thus `theta` is not presently a well-founded global invariant.

The audit checked the stated uses of connectivity, the Four-Colour Theorem,
Kelmans--Seymour and Wagner, as well as every possible host chord in the
six-vertex subdivision.

## 1. Definition and connectivity after deleting the pair

For a fixed pair `P`, the minimum defining `theta_G(P)` exists whenever
`G-P` contains a `TK_5`, because `G` is finite.  The infinity convention is
unambiguous, and the maximum over the finitely many pairs exists.

If `G` is seven-connected, then `G-P` is five-connected.  Indeed, a separator
of order at most four in `G-P`, together with the two vertices of `P`, would
be a separator of order at most six in `G`.  There is no small-order
exception: a seven-connected graph has at least eight vertices, so `G-P` has
at least six vertices, the minimum order on which five-connectivity is
defined.

## 2. Terminal equivalence

The three implications in Proposition 2.1 are exact.

* A planar graph cannot contain a subdivision of nonplanar `K_5`, so
  planarity implies `theta_G(P)=infinity`.
* The Kelmans--Seymour theorem states that every five-connected nonplanar
  graph contains a `TK_5`.  Applied to `G-P`, its contrapositive proves that
  `theta_G(P)=infinity` implies planarity.
* Planarity excludes every `K_5` minor.  Conversely, `G-P` is
  five-connected and hence four-connected; Wagner's four-connected theorem
  says that every four-connected `K_5`-minor-free graph is planar.

Therefore

\[
 \theta_G(P)=\infty
 \quad\Longleftrightarrow\quad
 G-P\text{ is planar}
 \quad\Longleftrightarrow\quad
 G-P\text{ is `K_5`-minor-free}.
\]

This verifies that infinity is exactly the fixed-pair terminal used in the
proof spine, not merely a topological-minor surrogate for it.  The published
Kelmans--Seymour proof cited in the theorem file directly supports the first
equivalence; Wagner's theorem supports the second.

## 3. Hypothetical minimal counterexample

In a minor-minimal counterexample to `HC_7`, `chi(G)=7`: every vertex
deletion is six-colourable, while `G` itself is not.  Deleting two vertices
can lower chromatic number by at most two, so for every pair `P`,

\[
                         \chi(G-P)\ge5.
\]

The Four-Colour Theorem then makes `G-P` nonplanar.  Since `G-P` is
five-connected, Kelmans--Seymour supplies a `TK_5`; hence every value
`theta_G(P)` is finite.

The independently audited literal-`K_5` transversal theorem applies because
the hypothetical counterexample is seven-connected and `K_7`-minor-free.
It returns a set of order at most two meeting every literal `K_5`; enlarging
it if necessary gives a two-set `P_0` with the same property.  A `TK_5` on
exactly five vertices has no internal subdivision vertices and is precisely
a literal `K_5`.  Consequently the shortest `TK_5` in `G-P_0` has at least
six vertices.  This proves `Theta_5(G)>=6`.

The maximizing pair need not be unique.  The corrected theorem statement
claims only that any selected maximizer is graph-global and independent of
local models or colourings, which is valid.

## 4. Six-vertex subdivision and all possible host chords

A subdivision of `K_5` has five branch vertices and ten internally
vertex-disjoint branch-to-branch paths.  If its total order is six, exactly
one path contains one internal vertex and the remaining nine paths are
single edges.  Thus, after naming the exceptional path `a-w-b`, the
subdivision contains every edge among `a,b,c,d,e` except `ab`.

The subdivision need not be induced.  The possible extra host edges relevant
to the displayed six vertices are:

1. the chord `ab`; and
2. one or more of `wc,wd,we`.

There are no other missing branch-vertex edges.  If `ab` were present, the
five branch vertices would induce a literal `K_5` disjoint from `P`, contrary
to the hypothesis that `P` meets every literal `K_5`.  Hence `ab` is absent.

Use `{a,w}` as the connected two-vertex bag and
`Q={b,c,d,e}` as the four singleton bags.  The set `Q` is a clique.  The
edge-bag contacts `b` through `wb` and contacts `c,d,e` through `a`, so this
is a valid `K_5` minor model.  Relative to `Q`,

\[
 D_a=\{b\},\qquad D_w\subseteq\{c,d,e\}.
\]

The extra edges `wc,wd,we` are accounted for exactly by membership outside
`D_w`; they do not invalidate the calculation.  If `D_w` were empty, then
`Q union {w}` would be a literal `K_5` disjoint from `P`.  Thus
`1<=|D_w|<=3`, giving

\[
 (1,1,2),\qquad(1,2,1),\qquad(1,3,0).
\]

The fourth general support-six type `(2,2,0)` cannot arise from this chosen
six-vertex `TK_5` orientation because one endpoint of its unique subdivided
edge necessarily misses exactly the other branch endpoint and no additional
member of `Q`.  This proves Proposition 4.1 with arbitrary host chords, not
only for an induced subdivision.

## 5. Strategic audit: `theta` versus `mu`

The parameter is more operational than `mu` in one limited and useful sense:
a minimizing witness is a labelled system of ten paths, so bridge
reroutings, segment shortening and exchanges involving the deleted pair can
be formulated literally.  An arbitrary minimum-support minor model need not
have that path structure.

It is **not** currently more powerful as a progress measure.  A strict
increase from `P` to `P'` requires proving that every `TK_5` smaller than the
new threshold is absent from `G-P'`.  Local construction or rerouting of one
subdivision cannot prove this.  Moreover, a small `K_5` minor need not be a
`TK_5` on the same support.  Numerically `mu(P)<=theta(P)` when both are
finite, but a lower bound on `theta(P)` gives no corresponding lower bound on
`mu(P)` and therefore does not advance the existing support-transversal
height by itself.

At a pair maximizing `theta`, the proposed exchange theorem has only its
literal `K_7` or infinite-pair outcomes.  Either outcome closes the
hypothetical counterexample.  The exchange target is therefore deliberately
`HC_7`-strength, as the theorem file states; it is not a proved intermediate
lemma disguised as a potential argument.

The accurate strategic conclusion is:

* `theta` supplies a valid global normalization and a more structured finite
  witness than `mu`;
* it does not yet supply a well-founded invariant or composition theorem;
* its value should be tested at the three support-six topological types, and
  demoted if the proper-minor states cannot be coupled to the selected pair
  and to the exclusion of **all** smaller subdivisions.

No claim stronger than this is promoted.
