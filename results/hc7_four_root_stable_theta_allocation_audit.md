# Audit: stable-theta allocation for the four-root degree-eight disk

**Audited source:** `results/hc7_four_root_stable_theta_allocation.md`
**Audited SHA-256:** `f5fb47f4e9e9e2857addbb3d7f5be54c7818bd32f264b07eccc729f671bbfa62`
**Verdict:** **GREEN** — the theorem and proof are valid for arbitrary
overlap between `U` and `C`.

## Checks

1. **External input.** Wollan, *SIAM Journal on Discrete Mathematics* **24**
   (2010), Theorem 1.1, quotes Tutte's theorem in the required form. For the
   union of four internally disjoint `r`--`v` paths, choose `{r,v}` as the
   branch vertices; the four paths are precisely the segments. Common
   endpoint pairs are allowed, each indexed endpoint pair is preserved, and
   every bridge, including a trivial unused edge, is made 2-stable.
2. **Roots, overlaps, and selected neighbours.** Four-connectivity supplies
   four internally disjoint `r`--`v` paths. Since `d_J(r)=4` and `d_J(v)=5`,
   their first edges exhaust `rU`, while their last edges select four
   distinct vertices of `C`. Each path contains exactly one root. If
   \(u\in U\cap C\) and `P_i` begins with `ru`, then an unused edge `uv`
   would be a bridge whose attachments lie on `P_i`, contradicting
   2-stability. Hence `uv` belongs to `P_i`; simplicity and the endpoint
   order force `P_i=r-u-v`, so `u=c_i`. Thus every overlap is selected and
   the fifth neighbour `c_*` is outside `U`. This also covers the extreme
   case \(|U\cap C|=4\), where the corresponding `A_i` are singleton roots.
3. **Unused neighbour.** If `c_*` lay internally on a selected path, the
   unused edge `vc_*` would be a bridge with both attachments on that one
   path, contradicting 2-stability. Thus `c_*` lies in a component `K`
   outside the path union.
4. **Plane bridge localization.** The path union is a plane subdivision of
   four parallel `r`--`v` edges. A connected component outside it lies in
   one complementary sector, whose boundary consists of two consecutive
   paths. The edge `vc_*` selects that sector. Since `r` has no neighbour
   outside the path union and `v` is common to every path, 2-stability forces
   an attachment strictly inside each boundary path; otherwise all
   attachments lie on one path. Hence `K` remains adjacent to both path
   interiors after deleting `r,v`.
5. **Five-set construction.** Removing `r,v` from the four paths leaves
   four nonempty connected pairwise disjoint sets, each containing its
   distinct root and selected neighbour, possibly the same vertex. The
   outer facial boundary is the literal cycle `u_0u_1u_2u_3u_0`; three
   consecutive boundary edges give `A_0A_1,A_1A_2,A_2A_3`, and the two
   off-endpoint attachments of `K` give `A_3X,XA_0`. This proves the
   asserted cyclic allocation.

## Adversarial check and trust boundary

A planar counterexample would have to put the `c_*` bridge across two
complementary sectors or attach it effectively to only one path.
Connectedness and planarity exclude the first; 2-stability excludes the
second. Common endpoints do not witness stability because both lie on every
segment. The proof does not establish the remaining contacts from the three
omitted boundary vertices or the disjoint reserved host component, exactly
as its trust boundary records.
