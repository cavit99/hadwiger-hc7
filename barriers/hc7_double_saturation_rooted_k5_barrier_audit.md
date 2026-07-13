# Independent audit: double-saturation rooted-`K_5` barrier

## Verdict

**GREEN.**  The construction, chromatic assertions, rooted-model
exclusion, and `K_7`-minor exclusion are correct.  The accompanying
verifier also returns GREEN under the workspace NetworkX runtime.

## Checks

1. In `H=K_6-03`, the vertices `1,2,4,5` form a `K_4` complete to both
   `0` and `3`.  A five-colouring therefore assigns four distinct colours
   to the `K_4` and the fifth colour to both nonadjacent vertices `0,3`.
   The sets `S=V(H)-{3}` and `T=V(H)-{0}` each induce `K_5`, so each is
   five-colour-saturating.
2. Put `I=S cap T={1,2,4,5}`.  Every branch set meeting both roots either
   contains a vertex of `I`, or contains both exclusive vertices `0,3`.
   Since `0,3` are nonadjacent and every `0-3` path in `H` has an internal
   vertex in `I`, the latter kind also contains a vertex of `I`.  Five
   disjoint doubly rooted bags would therefore require five distinct
   vertices of the four-element set `I`, impossible.
3. The graph `Q` is `K_8` minus the complementary path with edges
   `s3,30,0w`.  The six vertices `s,w,1,2,4,5` form a literal `K_6`.
   The displayed colour classes `{0,w}`, `{3,s}`, and four singleton
   classes are proper, so `chi(Q)=6`.
4. A seven-bag minor model in an eight-vertex graph uses either seven
   vertices as singleton bags or all eight vertices with one two-vertex
   bag.  The first case would be a `K_7` subgraph, but the largest clique
   has order six (equivalently, deleting one vertex does not cover all
   three complementary-path edges).
5. In the all-eight-vertex case, the two-vertex bag must cover every edge
   of the complementary path so that the six singleton bags are pairwise
   adjacent.  The only size-two covers are `{3,0}`, `{s,0}`, and `{3,w}`.
   The first is disconnected in `Q`; `{s,0}` is anticomplete to the
   singleton `3`; and `{3,w}` is anticomplete to the singleton `0`.
   Hence none produces a `K_7` model.
6. The verifier exhausts all five-bag models supported on arbitrary
   subsets of `H`, checks the displayed six-colouring, computes maximum
   clique order six, and tests every possible connected two-vertex bag
   for an eight-vertex `K_7` model.  It prints:

   `GREEN: double saturation without a doubly rooted K5 verified`.

The example is deliberately only six-chromatic and is not claimed to be
seven-connected or contraction-critical.  It refutes saturation alone,
not a future theorem using the full proof-spine hypotheses.
