# Audit: common edge-deletion chromatic fork

**Verdict:** GREEN.  The recolouring, chromatic, `HC_6`, absorption,
minimal two-edge response signature, and twin-seam steps are valid.  The
new Corollary 3.1 proves existence of both opposite states and in fact a
universal equality condition for every colouring of either one-edge
restoration.  It proves no boundary-state or labelled-row allocation.

**Audited source:**
`results/hc7_common_edge_deletion_k6_fork.md`.

**Source SHA-256:**
`b3c0b1c6972963b2e282f92242aafb11e211351d43585f09492c7f1a3ecc2785`.

## 1. One-spare-colour lemma

Let `c` be a `q`-colouring of
\(H=G-\{ab,cd\}\), where the two deleted edges are vertex-disjoint.

If \(c(a)\ne c(b)\), the restored edge `ab` is already proper.  Recolouring
one endpoint of `cd` with one fresh colour makes `cd` proper and cannot
spoil any other edge: the recoloured vertex is the only vertex with the
new colour.  Thus `G` would be \((q+1)\)-colourable.  The hypothesis
\(\chi(G)>q+1\) therefore forces \(c(a)=c(b)\).  The symmetric argument
forces \(c(c)=c(d)\).

Now let a cross-edge be absent, say `ac`.  Recolour `a,c` with the same
fresh colour.  This is legal because `ac` is absent.  The four endpoints
are distinct, so:

* `ab` and `cd` become proper against the old palette;
* every other edge from `a` or `c` to an unchanged vertex is proper; and
* even if another cross-edge such as `ad` or `bc` is present, its unchanged
  endpoint has an old colour.

This again gives a \((q+1)\)-colouring, a contradiction.  Applying the
same argument to each of the four possible cross-pairs proves that all
four cross-edges are present.  Together with `ab,cd`, they are exactly the
six edges on four distinct vertices, hence induce a literal \(K_4\).

The lemma does not identify colours with model bags and is valid for every
\(q\ge1\).

## 2. Exact chromatic fork

Strong seven-contraction-criticality means

\[
\chi(G)=7,
\qquad
\text{every proper minor of }G\text{ is six-colourable}.
\]

Deleting the two distinct edges gives a proper minor `H`, so
\(\chi(H)\le6\).

For the lower bound, suppose `H` were four-colourable.  Recolour one
endpoint of `e` with a fresh fifth colour and one endpoint of `f` with a
distinct fresh sixth colour.  Vertex-disjointness ensures that these are
two different vertices and that the other endpoint of each restored edge
retains an old colour.  All unchanged incident edges remain proper, and a
possible edge between the two recoloured vertices has ends of colours five
and six.  This six-colours `G`, a contradiction.  Hence

\[
                         5\le\chi(H)\le6.
\]

If \(\chi(H)=5\), Lemma 1.1 applies with \(q=5\), since
\(\chi(G)=7>6\), and forces the endpoint \(K_4\).  This is a one-way
implication only; the source does not claim its converse.  Consequently,
if even one cross-edge is absent, \(\chi(H)\ne5\) and the exact bounds
force \(\chi(H)=6\).

## 3. Use of `HC_6`

The known parameter-six case of Hadwiger says that every graph with no
\(K_6\) minor is five-colourable.  Its contrapositive applies to
\(\chi(H)=6\) and yields a \(K_6\) minor in `H`.  No rooted version of
`HC_6`, and no assertion about which model bag contains an endpoint, is
used or obtained.

Thus the precise unconditional fork is:

1. the four endpoints induce a literal \(K_4\) in `G`; or
2. \(\chi(H)=6\) and `H` contains a \(K_6\) minor.

The alternatives need not be exclusive: an endpoint \(K_4\) may coexist
with \(\chi(H)=6\).

## 4. Spanning absorption

Let \((M_1,\ldots,M_6)\) be any \(K_6\) model in a connected graph `H`.
If its union is not spanning, connectedness supplies an edge from some
component `C` of the unused graph to a bag, say `M_i`.  Replace `M_i` by
\(M_i\cup C\).  The replacement is connected, remains disjoint from the
other five bags, and retains every old inter-bag edge.  Repeating this
operation strictly increases the model union and terminates with a
spanning model.

More generally, in disconnected `H` the same argument produces a model
spanning the connected component that originally contained the model, not
a model spanning all of `H`.  This is why connectedness is essential to
the final “spanning `H`” conclusion and why the normalized wording above
is the exact safe one.

## 5. Minimal two-edge obstruction signature

Assume a cross-edge is absent.  The audited fork gives \(\chi(H)=6\);
connectedness is not needed for this chromatic conclusion.  The two
one-edge restorations satisfy

\[
                         H+e=G-f,
\qquad                    H+f=G-e.
\]

Each is a proper minor of `G`, because it is obtained by deleting the
other literal edge.  Strong contraction-criticality therefore makes each
at most six-colourable.  Since each contains the six-chromatic graph `H`,
monotonicity under edge addition gives the reverse inequality.  Hence

\[
             \chi(H)=\chi(H+e)=\chi(H+f)=6,
\qquad       \chi(H+e+f)=\chi(G)=7.
\]

All four equalities in (3.1) are therefore exact.

Take any six-colouring of `H+e`.  The ends of `e` differ because `e` is an
edge in that host.  The ends of `f` must be equal: if they differed, the
same assignment would remain proper after restoring `f` and would
six-colour `G`.  Thus every six-colouring of `H+e`, not merely one chosen
colouring, restricts to state `(proper,equal)` on `H`.  Existence follows
because `H+e` is six-colourable.  Symmetrically, every six-colouring of
`H+f` restricts to `(equal,proper)`, and at least one such colouring
exists.

Conversely, any six-colouring of `H` with state `(proper,proper)` would
already be a six-colouring of `G`; hence that state is impossible.  This
fork argument alone does not decide `(equal,equal)`.  The source now
correctly points to the separately audited simultaneous contraction
theorem, which proves existence of that state from `G/e/f`.

The equality at the absent edge also means the first colouring descends to
a colouring of `G/f`, and the second descends to a colouring of `G/e`.
This is a legitimate contraction response: identifying equal-coloured
ends cannot create a monochromatic edge.  More explicitly, every neighbour
of either endpoint has colour different from their common colour already
in the edge-deletion host.  A common neighbour is adjacent to both ends and
still has a different colour; after identification it creates only one
proper incident edge.  Loops are discarded and parallel edges merged, so
neither causes a colouring obstruction.  Conversely, every six-colouring
of `G/f` expands to a colouring of `H+e` and hence has the
`(proper,equal)` signature; every six-colouring of `G/e` has the opposite
signature.  Thus universality holds for the two-bit edge signature of all
contraction responses.  What the corollary neither claims nor proves is
palette agreement between two preselected responses, Kempe reachability,
or realization of a prescribed boundary equality partition.

The connectedness hypothesis in Corollary 3.1 is harmless but stronger
than needed for (3.1) and the three state clauses; it is retained because
the surrounding theorem also uses it to obtain a spanning \(K_6\) model.

## 6. Twin-seam specialization

In the frozen seam, `z` lies in the component `E` of `A-Z` and `d` lies in
the distinct component `D`.  An edge `zd` would join these two components
inside `G[A-Z]`; therefore `zd` is absent.  It is one of the four
cross-edges between the endpoint pairs \(\{z,u\}\) and \(\{d,t\}\).

The four endpoints are distinct: `z,d` lie in distinct components of
`A-Z`, `u` lies in the old boundary, and `t` lies in the gate set `Z`.
Hence the named edges `zu,dt` satisfy the vertex-disjoint hypothesis.

The host `G` is seven-connected, so its edge-connectivity is at least
seven.  Deleting only `e,f` cannot disconnect it.  Equivalently, the
standard inequality \(\kappa(G)\le\lambda(G)\) gives
\(\lambda(G)\ge7\).  Thus the common deletion `H` is connected.

Since `zd` is absent, the non-\(K_4\) side of the fork applies:
\(\chi(H)=6\), known `HC_6` supplies a \(K_6\) model, and the absorption
argument makes it spanning in `H`.

## 7. Exact scope

The theorem gives one spanning six-bag model in the common deletion host,
independent of the separating/bypass choice and of any response colouring.
The new corollary separately gives two opposite literal edge states in
that same host.  It does **not** show:

* which bags contain or contact `z,u,d,t`;
* that two named endpoints occupy one splittable bag;
* that either restored edge can split a row while retaining all five
  foreign-row adjacencies;
* that two proper-minor colourings return a common exact state; or
* that a fixed pair or strict exact-seven handoff exists.

Accordingly the final paragraph of the source is a correctly stated open
allocation problem, not a consequence of the chromatic fork.
