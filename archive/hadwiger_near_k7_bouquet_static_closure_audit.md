# Audit: static closure of the exact-seven bouquets

## Verdict

**GREEN**, conditional only on the already stated one-complex
normalization and dark-lobe exactness.  The result closes the Hall-rank
branch for four distinct fixed off-torso lobes.  It does not close a
shared-lobe collision or an attachment occurrence which belongs to no
full SDR.

## Checks

1. In both normalizations the six literal labels contain
   `J=K_6-{ab,ac}`: the `K_7^vee` boundary is exact, and the denser
   `K_7^-` boundary contains it after deleting an unused singleton edge.
2. A dark lobe is connected, has two distinct torso poles, and contacts
   all five literal rows other than its unique miss.  These are exactly
   the inputs used; no pole--pole or pole--literal edge is assumed.
3. Lemma 2.1 handles repeated marks by enlarging their distinct set to
   order three.  Avoiding singleton bags at the enlarged set is stronger
   than required.  In every displayed partition the only bag containing
   `a` also contains a universal `r_i`; all other vertices lie in the
   clique `J-a`.
4. The two-pole and all-three-pair constructions use disjoint poles in
   different branch bags.  Every claimed bag adjacency is a literal
   pole--lobe contact.
5. In the four-helper frame the unique possible `x`-missing lobe is put
   in `P`, while `A_2,B_1,B_2` see `x`; hence `Q` is connected and the
   two `x` cross-edges are literal.
6. The spent-pair proof covers both possible support orders omitted in
   the first draft:
   * four distinct missed rows (`|M|=4`); and
   * three distinct missed rows with triangle-free unmissed triple.
   In the four-distinct case `A_2` is chosen to miss a neutral `r_i`, so
   it sees the spent vertex `a`; this is necessary for connectivity of
   `Q`.
7. The two triangle-free triples have exactly the advertised two orbits
   under `b<->c` and permutations of the three universal `r_i`.
8. `near_k7_four_bouquet_verify.py` independently constructs and replays
   seven branch bags for all 1296 missed-row profiles of the sole
   `(2,2,0)` portal multiplicity.  It checks disjointness, connectedness,
   and all 21 bag adjacencies from the weakest literal quotient.

## Exact consequence

Corollary 9.2 of the active-root note had only two Hall-deficient
geometries.  Both now give `K_7`, so four distinct fixed dark lobes have
portal rank four.  Corollary 2.4 then supplies the full active product
whenever the common pool/reserve hypotheses are present.

The remaining one-torso residue is not a bouquet.  It is exactly one of:

* two desired extension roles still using one shared connected lobe; or
* a named attachment occurrence unused by every full SDR.

Those are role/occurrence failures, not Hall capacity failures, and still
require the bilateral exact-seven or active-occurrence exchange.
