# Independent audit: universal-pair three-core elimination

**Verdict:** GREEN.

The proof of `hc7_universal_pair_three_core_elimination.md` was checked
independently.  Every branch-set and connectivity step is valid.

## Checks

1. Since the three `K_5`-model supports are pairwise vertex-disjoint, the
   two vertices `p,q` meet at most two supports.  Hence one model support,
   and therefore its literal singleton `K_4` core `Q`, avoids both.

2. Writing `R=Q\cap S` and `K=Q-S`, the clique `K` lies wholly in one
   component of `G-S`; otherwise it would contain an edge between the two
   anticomplete shores.

3. For `r=|K|=4-|R|`, deleting the forbidden set
   `D_0=R\cup{p,q}` leaves an `r`-connected graph, since

   \[
       r+|D_0|=(4-|R|)+(|R|+2)=6\le 7.
   \]

   The target set `S-(R\cup{p,q})` has at least `r` vertices.  The fan
   lemma therefore gives disjoint paths from every vertex of `K` to
   distinct targets while avoiding `D_0`.  First-`S` truncation keeps all
   internal vertices in the shore containing `K`.

4. The four resulting bags remain pairwise adjacent because they retain
   their distinct roots in the literal clique `Q`.  They meet four
   distinct boundary vertices outside `p,q`.

5. The bags `{p}`, `{q}`, and the opposite full shore are disjoint from
   the four rooted bags and pairwise adjacent to them.  Universality of
   `p,q` in `G[S]` and boundary-fullness of the opposite shore supply all
   required edges.  Thus the seven bags form a literal `K_7` model.

The case `K=\varnothing` is immediate by the same seven bags, without the
fan.  No split edge or unused fifth branch bag is needed.

## Consequence

The unique order-nine five-chromatic boundary `K_2\vee C_7` from the
two-full-shore absorption theorem cannot occur in the three-model
minimal-bad-contraction residue.  Hence every surviving expanded boundary
of order eight or nine in that residue is four-colourable.
