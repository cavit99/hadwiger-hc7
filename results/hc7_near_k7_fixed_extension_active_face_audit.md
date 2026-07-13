# Audit: fixed private extensions force one face

## Verdict

**GREEN AS PATCHED.**  The theorem is a correct transversal-matroid
upgrade of the active-root face theorem.  It proves that root choice and
root rotation are exhausted once four fixed disjoint private extensions
and their common completion data exist.  It does not prove that those
extensions exist.

## Checks

1. The feasible four-sets are exactly the bases of the rank-four
   transversal matroid on the portal sets `P_i=N_W(E_i)`.  The existence
   of one feasible set is precisely the assertion that the matroid has
   rank four.
2. The basis graph is connected by one-element exchange.  Consecutive
   bases share three actual torso vertices, which is the exact overlap
   needed by the facial-coherence theorem.  A reassignment of the same
   four roots to the fixed extensions does not change the underlying
   rooted set and introduces no gap.
3. For a saturating matching `p_i in P_i`, the sets
   `E_i union {p_i}` are connected, pairwise disjoint and meet `W` only
   in their distinct named roots.  The assumed fixed pool/reserve contacts
   therefore satisfy the literal hypotheses of the biportal completion.
4. If one feasible root set has a rooted `K_4`, the completion gives a
   labelled `K_7`.  If none does, the active-root face theorem puts all
   vertices occurring in feasible bases on one face.  In the
   four-connected case that theorem first forces `W` planar; in the
   planar three-connected case the embedding is already fixed.
5. The corollary has been qualified to conflicts inside the same page
   `W`.  Leaving that page is a separate gate/three-separator event and
   is not a rotation change covered by this theorem.

## Exact frontier

An unusable portal vertex which belongs to no feasible basis is not put
on the common face.  This is correct: it is a Hall/capacity obstruction,
not an alternative root choice.  The remaining work is therefore exactly
one of:

* rank below four for the private-extension portal family;
* two state coordinates sharing one extension lobe;
* loss of a pool/reserve contact; or
* departure through a named gate/three-separator.

The theorem makes no state-intersection claim in these cases.

