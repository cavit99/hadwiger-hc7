# Audit: exact deficiency-rotation edge

## Verdict

**GREEN for Theorems 1--5 after adding the literal old-donor row
contacts; the final rotation-web composition target remains unproved.**
Every involution statement concerns a single connected gate.

* The exact involution theorem and its anti-potential corollary are
  **GREEN**.
* The rooted two-carrier completion is **GREEN**; its theorem statement
  explicitly includes fixed `X-Z` and `W-Z` attachment roots.
* The one-versus-one statement is **GREEN** only as a rooted Two-Paths
  reduction.  The former unique-pinch claim has been retracted: an
  alternating cycle is a 2-connected counterexample.
* The one-versus-two statement is **GREEN** solely as an unrooted capacity
  equivalence.  Rooting introduces an additional web obstruction.

## Checks

1. The added hypothesis `E(U,F_i) nonempty` for every fixed row is
   necessary: it makes `U,F_1,...,F_5` the advertised old foreign clique
   model and ensures that every row missed by `W` is met through `Z`.
   In the inverse model the donor is `X union Z`.  Since `X` misses
   exactly `D` and meets every other fixed row, removing `Z` loses exactly
   `D`; no additional missing row is hidden.  Since `Z` monopolized every
   row in `E` in the forward donor, it meets every current target.  The
   same literal cut edges restore `U=W union Z`.  Reversibility is exact.
   A two-piece concentrated rotation has no connected `Z` and is outside
   this theorem.
2. The involution immediately disproves any claim that one state-only
   potential strictly decreases along every legal rotation.  A potential
   may orient an edge using extra global choices, but termination then
   requires a separate proof that the trichotomy always returns a forward
   edge.  No such assertion is made.
3. For two-carrier completion, demand contacts alone do not guarantee that
   the two sides also contain the correct centre attachments.  The theorem
   therefore records the rooted carrier version as the safe statement.
   Every future citation must include these roots or separately prove the
   required side allocation.
4. With rooted carriers, the seven proposed bags are connected, disjoint,
   and pairwise adjacent: each enlarged centre repairs its own missing
   rows, their cut edge joins them, and the five fixed rows remain a
   clique.
5. In the one-versus-two unrooted statement, deleting a chosen singleton
   `D`-portal gives the exact necessary and sufficient condition for an
   unrooted opposite carrier.  Two-connectivity forces the displayed
   singleton portal exception, yielding `|P_d|<=2`.  This conclusion is
   not inferred merely from the absence of a target minor.
6. The last section correctly treats the absence of a `K_7^-` **minor**,
   not merely absence of a chosen `K_7^-` model.  Every order-one deficient
   rotation is itself such a minor, so both ends of every surviving edge
   have order two.
7. The robust-demand theorem uses the same rooted partition as Theorem 2.
   Covering three of the four demand occurrences leaves at most one absent
   pair among seven otherwise pairwise adjacent bags, which is a literal
   `K_7^-` model.  Repeated labels in `D cap E` are treated as demand
   occurrences on different enlarged centre bags, so the count remains
   valid.
8. The rotation-web composition target remains unproved.  The note narrows
   the composition gap to a global cycle/coherence theorem; it does not
   claim `HC_7`.
