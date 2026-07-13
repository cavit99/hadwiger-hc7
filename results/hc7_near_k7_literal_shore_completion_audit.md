# Independent audit: literal shore completions

## Verdict

**GREEN.**  The uniform missing-star theorem, both branch-set lemmas, the
exact three-piece capacity dual, and the path-cut specializations in
`hc7_near_k7_literal_shore_completion.md` are valid in their stated
sufficient scope.

## Checks

1. In Theorem 0, the `m+1` carrier shores form a clique model, the
   `t-1-m` retained foreign bags form a clique model, and every cross-pair
   is explicitly present.  The two family sizes sum to `t`; none of the
   globally missed foreign bags is used.  This proves the uniform
   missing-star completion, including `m=0` and `m=t-1`.
2. In the one-missing branch the retained foreign bags are
   `E,U_1,...,U_4`.  They are five connected pairwise adjacent bags;
   both `X,Y` see all five and see each other.  Together these are seven
   disjoint clique bags.  The other twin is correctly omitted.
3. In the both-missing branch, the three proposed shores form a triangle
   model by hypothesis, the four neutral bags form a `K_4` model, and all
   twelve cross contacts are stated explicitly.  No contact to `B` or
   `C` is used.
4. For a path cut `L | R`, every assigned crossing piece has an
   attachment to its assigned side, so adjoining any family of such
   pieces preserves connectedness.  The two families are disjoint, old
   exterior components are disjoint, and the two path sides are
   disjoint; hence the constructed shores are disjoint.  The literal
   path edge across the cut supplies their adjacency.
5. The left shore already sees `U_1,U_2` at `p_0`; its coverage triple
   supplies `E,U_3,U_4`.  Symmetrically the right shore sees `U_3,U_4`
   at `p_m` and its coverage triple supplies `E,U_1,U_2`.  Thus Lemma 1
   applies with actual model-label edges, not palette colours.

## Exact capacity dual

Let `S={k_1,k_2,k_3}`, allowing repetitions.  If the representatives
meet all three left demand sets and no right demand set is contained in
`S`, then assigning `S` left and every other crossing piece right gives
the required disjoint covers.  Conversely, from any disjoint covering
families choose one representative for each left demand inside the left
family.  Every right demand has a representative in the disjoint right
family and therefore is not contained in `S`.  This proves both
directions of Lemma 3.

The quantified concentration conclusion remains correct when a left
demand set is empty: there is then no representative triple, so its
universal formulation is vacuous, while the capacity state indeed
fails.  The useful four-support corollary assumes all six demand sets
have order at least four, so representatives exist and no right support
set can lie in a set of at most three representatives.  The symmetric
argument is identical.

## Both-missing bridge triangle

In Lemma 4, “other crossing pieces” excludes `K_0` and the two families
are disjoint.  Hence `X,Y,Z=K_0` are vertex-disjoint.  The path cut edge
joins `X,Y`; crossing attachments of `K_0` join `Z` to each.  Endpoint
portals plus (1.6) give all four neutral rows to `X,Y`, while `K_0` has
all four by hypothesis.  Thus the three shores are pairwise adjacent,
each is full to `U_1,...,U_4`, and Lemma 2 gives the seven literal branch
bags.

The set-packing condition is only sufficient.  Failure of this particular
two-bin assignment is not claimed to exclude every possible `K_7` model;
it is correctly identified as the residue for a later bridge/web
exchange theorem.
