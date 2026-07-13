# Audit: singleton one-hole rooted exchange

## Verdict

**GREEN after explicitly handling the reverse-avoidable orientation**,
subject to the stated spanning/all-neighbours hypothesis.  The theorem
is a valid label-preserving reduction to `K_7`, an actual adhesion, or a
`K_7^-`/`K_7^vee` deficiency rotation.  It is not a proof that rotations
terminate.

## Checks

1. Since `a` is anticomplete to `B` and all of its neighbours lie in the
   displayed foreign bags, its at least seven neighbours lie across five
   neutral donors.  Each neutral donor has a root because `aU_i` is a
   prescribed model edge.  Hence a two-root donor exists.
2. A component outside a retained row core has connected complement and
   no monopoly among the five old foreign rows.  If it meets `B`, moving
   it into `B` preserves every old row adjacency, and the cut edge
   supplies the new `B-U` adjacency.  The two selected roots supply the
   two required edges at `a`.  The seven bags in (1.4) are therefore a
   literal `K_7` model.
3. If such a component or canonical gate misses `B`, `B` is a whole
   connected far bag outside the set and its open neighbourhood.  The
   separator is actual, not a quotient cut.  Seven-connectivity and
   exact-order fullness are invoked correctly.
4. Unavoidability is directional.  After `s` is unavoidable relative to
   protected `r`, the corrected proof first tests the reverse orientation.
   If `r` is avoidable relative to protected `s`, the same monopoly-free
   transfer-or-separator proof applies with the roots reversed.  Only if
   both orientations are unavoidable do the two canonical gates exist;
   they are disjoint, so their nonempty monopoly sets are disjoint.  Five
   labels force one monopoly order at most two.  No claim is made that it
   is zero.
5. In the rotation branch, `A'={a} union Z` is connected; it meets `B`
   through `Z` and every other neutral row through `a`.  The remaining
   five old foreign rows are still pairwise adjacent.  The residual
   centre meets `A'` through a literal cut edge and can lose precisely
   the rows monopolized by `Z`.  Thus monopoly order one/two gives the
   advertised labelled near model.
6. The hypothesis about all neighbours of `a` is essential.  A
   nonspanning model may have unused `a`-neighbours, and those cannot be
   counted as roots in the five displayed donors.  Whole-component
   spanning transport must precede the theorem.
7. Corollary 2 correctly stops at the common composition gap.  A proper
   subbag centre is not by itself a well-founded global descent because
   the old centre is enlarged into a foreign bag.
