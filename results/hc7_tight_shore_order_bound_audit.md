# Independent audit of the tight-shore order bound

**Verdict:** GREEN for Theorem 1 and Corollary 2 at the exact source
revision identified below.

**Audited source:** `hc7_tight_shore_order_bound.md`, SHA-256

```text
88b7a9329c3a3a4170022cd1b0a54cef6305e22809d3cc932ccca9d24afc066f
```

The mathematical statement and proof are unchanged from the independently
checked revision; the new hash records only the source status-line update.

This is a separate internal mathematical audit, not external peer review.
It checks the internal-degree estimate, the low-degree singleton
separation, the opposite-shore contraction, every counted edge of the
minor, and the exact application of Mader's `K_7`-minor extremal bound.

## 1. Internal and whole-graph degree estimates

For every `v in R`, the list `A(v)` is a subset of a six-colour palette, so
the tightness equality gives

\[
                         d_{G[R]}(v)=|A(v)|\le6.
\]

Summing internal degrees yields `2e_R<=6r`, hence `e_R<=3r`.

If some vertex `v in R` has whole-graph degree at most eight,
seven-connectivity gives `7<=d_G(v)<=8`.  Since `E_G(L,R)=emptyset` and
`L` is nonempty, `N_G(v)` separates the singleton `{v}` from `L`.
Therefore the claimed order-seven or order-eight separation is literal and
has both open sides nonempty.

After excluding that outcome, every vertex of `R` has whole-graph degree at
least nine.  There are no `L-R` edges, so summing the whole-graph degrees
over `R` counts each `R`-edge twice and each `R-S` edge once:

\[
                    2e_R+e_{RS}\ge9r.
\]

No edge class is omitted from this equality.

## 2. Fullness of the contracted opposite-shore component

Choose a component `D` of the nonempty graph `G[L]`.  It has no neighbour
in another component of `G[L]`, and no vertex of `R` is adjacent to `L`;
therefore `N_G(D) subseteq S`.  The set `N_G(D)` separates `D` from the
nonempty shore `R`.  Seven-connectivity forces `|N_G(D)|>=7`, while
`|S|=7`, and hence

\[
                              N_G(D)=S.
\]

Contracting the connected set `D` to one vertex `ell` and deleting every
other vertex of `L` gives a minor `H`.  After suppressing loops and parallel
edges, `H` is simple and has exactly `r+8` vertices.  The contraction and
deletions do not disturb any edge inside `R` or between `R` and `S`, and
fullness of `D` leaves seven distinct `ell-S` edges.  Thus

\[
                         |E(H)|\ge e_R+e_{RS}+7.
\]

Using `e_{RS}>=9r-2e_R` and then `e_R<=3r` gives

\[
 |E(H)|\ge9r-e_R+7\ge6r+7.
\]

The inequality directions are correct: the upper bound on `e_R` supplies a
lower bound on `9r-e_R`.

## 3. Mader's bound and the order conclusion

The graph `H` is a minor of the `K_7`-minor-free graph `G`, so it is also
`K_7`-minor-free.  Its order is `r+8>=9`, within the range of Mader's exact
small-clique-minor theorem.  Therefore

\[
 |E(H)|\le5|V(H)|-15=5r+25.
\]

Combining the two estimates gives

\[
                         6r+7\le5r+25,
\]

and hence `r<=18`.  This proves the stated dichotomy.  Corollary 2 is a
direct specialization of the theorem to the all-tight shore-filling branch
of the already audited two-edge list-critical theorem; it introduces no
new inference.

## 4. Trust boundary

The result requires a literal order-seven separation
`V(G)=L dotcup S dotcup R`, seven-connectivity, `K_7`-minor exclusion, and
the equality `d_{G[R]}(v)=|A(v)|` at every shore vertex.  It needs neither
the number of colours used on `S` nor the Gallai-tree classification.

It proves only that the all-tight shore is bounded by eighteen vertices
unless a singleton-side order-seven or order-eight separation already
exists.  It does not eliminate the bounded residue, reduce order eight to
order seven, provide compatible boundary colourings, preserve a named
branch-set system, or construct a `K_7`-minor model.  It therefore does not
prove `HC_7`.
