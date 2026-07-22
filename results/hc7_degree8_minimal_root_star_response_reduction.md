# Minimal aligned root-star deletions give a clean fan or a generic exact-seven restart

**Status:** written proof; separately audited GREEN in
[`hc7_degree8_minimal_root_star_response_reduction_audit.md`](hc7_degree8_minimal_root_star_response_reduction_audit.md).
This result does not prove `HC_7`.

## 1. Setting

Let `G` be a finite simple seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `X` have order eight, and suppose that the components of `G-X` are

\[
                         \{u\},E,F,                    \tag{1.2}
\]

each adjacent to every vertex of `X`.  Fix `x in X`, choose
`Q in {E,F}`, and let

\[
                         J=\{xv:v\in L\},\qquad
                         \varnothing\ne L\subseteq Q. \tag{1.3}
\]

Suppose that `d` is a proper six-colouring of `G-J`, with boundary trace
`tau=d|_X`, and that `J` is inclusion-minimal among its subsets having a
proper six-colouring with boundary trace `tau`.  Put

\[
                              \gamma=d(x).             \tag{1.4}
\]

This is exactly the multi-edge alternative in the
[degree-eight common-root star response](../results/hc7_degree8_common_root_star_response.md),
with one of its aligned colourings fixed.

## 2. What proper-minor criticality supplies

### Proposition 2.1 (all contraction signatures, but not the aligned trace)

Every edge of `J` is monochromatic under `d`, and `L` is independent.
For every nonempty `K subseteq J`, there is a proper six-colouring `c_K`
of `G-K` such that

1. every edge of `K` is monochromatic;
2. every edge of `J-K` is proper; and
3. if `K subsetneq J`, the equality partition induced by `c_K` on `X`
   differs from the equality partition of `tau`.

Moreover, the trace of `c_K` extends through the exterior component other
than `Q` and does not extend through the intact `Q`-side.

#### Proof

If some `xv in J` were proper under `d`, restoring it would give a
`tau`-aligned colouring after deleting the proper subset `J-{xv}`.  Hence
every edge is monochromatic.  All vertices of `L` consequently have colour
`gamma`; their mutual edges are present in `G-J`, so `L` is independent.

Contract the induced star with edge set `K` and six-colour the resulting
proper minor.  Expanding the contracted vertex gives a colouring of `G-K`
in which precisely the edges of `K` among the edges of `J` are
monochromatic.  If `K subsetneq J` and its boundary equality partition
were that of `tau`, a global palette permutation would make its boundary
trace literally `tau`, contrary to the inclusion-minimality of `J`.

The component other than `Q` is unchanged in `G-K`, so the new boundary
trace extends through it.  If it also extended through the intact `Q`-side,
that extension could replace the deleted-edge side of `c_K` and would give
a proper six-colouring of `G`.  This is impossible. \(\square\)

Thus proper-minor criticality gives a one-edge response for every member of
`J`, but minimality forces every such response into a different boundary-
partition fibre from `tau`.  It supplies no operation that transports one
of those responses back to `tau`.

## 3. Minimality supplies five paths at every deleted leaf

### Lemma 3.1 (aligned colour-indexed paths)

Fix `xv in J`.  For every colour `delta ne gamma`, the component containing
`v` in

\[
                    (G-J)[d^{-1}(\{\gamma,\delta\})]   \tag{3.1}
\]

meets `X`.  Consequently there is a `gamma`--`delta` path `P_delta`
from `v` to `X`, stopped at its first boundary vertex, whose internal
vertices lie in `Q`.  The five paths are pairwise edge-disjoint, and paths
belonging to different alternate colours meet only at `gamma`-coloured
vertices.

#### Proof

Let `K_delta` be the component in (3.1), and suppose that it misses `X`.
Interchange `gamma,delta` on `K_delta`.  Let

\[
 R=\{xw\in J:w\in V(K_delta)\}.
\]

The set `R` is nonempty because it contains `xv`.  The interchange fixes
`X`, changes every outer endpoint belonging to `R` away from the colour of
`x`, and preserves properness on `G-J`.  Restoring all edges of `R`
therefore gives a proper `tau`-aligned colouring of `G-(J-R)`.  This
contradicts minimality; if `R=J`, it instead directly six-colours `G`.
Hence `K_delta` meets `X`.

Take a shortest `v`--`X` path in `K_delta` and stop it at its first boundary
vertex.  Before that first visit it remains in the component `Q` of `G-X`.
Paths using distinct alternate colours can share only vertices of colour
`gamma`, and cannot share an edge. \(\square\)

## 4. The complete reduction

### Theorem 4.1 (clean aligned fan or strict generic exact-seven restart)

For every selected edge `xv in J`, at least one of the following holds.

1. **Clean aligned fan.**  There are five `v`--`X` paths preserving the
   five first edges of the paths in Lemma 3.1 and pairwise vertex-disjoint
   outside `{v} union X`.  Their boundary ends need not be distinct.
2. **Generic exact-seven restart.**  There are an integer
   `ell in {2,3,4,5}` and sets

   \[
      I\subseteq X,\quad |I|=\ell+1,\quad x\in I,
      \qquad Z\subseteq Q-\{v\},\quad |Z|=\ell-1,       \tag{4.1}
   \]

   together with a nonempty connected set
   `A subseteq Q-({v} union Z)` such that

   \[
      Y=N_G(A)=(X-I)\mathbin{\dot\cup}\{v\}
                    \mathbin{\dot\cup}Z,qquad |Y|=7. \tag{4.2}
   \]

   The restriction of `d` to `G[A union Y]` is proper in the original
   graph `G`.  Its exact `gamma`-class

   \[
                         B=d^{-1}(\gamma)\cap Y        \tag{4.3}
   \]

   contains `v` and at least one vertex of `Z`.

   In particular, choosing any edge `ya` from `Y` to `A` and any proper
   six-colouring of `G-ya` gives a generic exact-seven selected-response
   interface with

   \[
                              |A|<|Q|.                 \tag{4.4}
   \]

#### Proof

Use the five paths from Lemma 3.1 and repeat the vertex-capacitated Menger
argument of the
[prescribed-spoke reduction](../results/hc7_order8_prescribed_spoke_reduction.md#theorem-31-clean-first-edge-fan-or-a-coloured-order-seven-separation).
For completeness, call a path direct when it has one edge, let `ell` be the
number of non-direct paths.  If `ell<=1`, the original five paths already
give item 1, so the separator branch has `ell in {2,3,4,5}`.  Choose
`I subseteq X` of order `ell+1` containing `x` and all non-direct path ends
while avoiding all direct ends.  The edge `xv` is absent from `G-J`, so no
direct end is `x`.

In the original graph `G[(Q-{v}) union I]`, either the non-direct first
neighbours have
`ell` paths to `I`, disjoint outside `I`, or a set
`Z subseteq Q-{v}` of order at most `ell-1` meets all such paths.  The first
outcome, after prepending the prescribed first edges, is item 1.
These rerouted paths are allowed to use other edges of `J`; the packing
outcome is a statement about literal path geometry in `G`.

In the second outcome, let `A` be a component of
`G[Q-({v} union Z)]` containing a surviving first neighbour.  It has no
neighbour in `I`, and hence

\[
                 N_G(A)\subseteq (X-I)\cup\{v\}\cup Z.
\]

Another component of `G-X` lies outside this set, so this is an actual
separation.  Seven-connectivity forces equality and order seven, proving
(4.1)--(4.2).  Every original non-direct path tail meets `Z`; since there
are `ell` tails and `|Z|=ell-1`, one vertex of `Z` lies on two paths with
different alternate colours and therefore has colour `gamma`.  The vertex
`v` also has colour `gamma`, proving (4.3).

It remains to check a point absent from the one-edge version of the
argument.  Although the Menger paths were allowed to use other edges of
`J`, the cut is computed in the original graph.  Hence `A` has no neighbour
in `I`.  Moreover, although `d` was defined on the common deletion `G-J`,
none of the missing edges has both ends in `A union Y`: every missing edge
is incident with `x`, while `x in I` and (4.2) places `I` outside
`A union Y`.  Thus the displayed restriction of `d` is proper in the
original graph.

Finally, `A` is a proper subset of `Q` because `v notin A`.  The edge
`ya` exists by `Y=N_G(A)`, and proper-minor criticality supplies a
six-colouring of `G-ya`; its ends are monochromatic, since otherwise it
would colour `G`.  This is the asserted generic exact-seven response and
proves (4.4). \(\square\)

### Corollary 4.2 (the surviving multi-edge residue)

Either a strict generic exact-seven restart exists, or every edge of `J`
has a clean five-path fan whose prescribed first edges come from the same
aligned colouring `d`.  The fans are obtained separately and are not
asserted to be mutually disjoint.

In the exact-seven outcome, the block `B` in (4.3) is also an exact colour
class in some colouring of the opposite closed shore.  If `G[Y-B]` is a
clique, the two closed shores have one common equality partition and glue
to six-colour `G`; hence every live exact-seven output has a nonedge in
`G[Y-B]`.

#### Proof

Apply Theorem 4.1 to every member of `J`.  For the final assertion, contract
a spanning tree of the connected set `A union B` and colour the resulting
proper minor.  Restrict to the opposite closed shore and expand the
contraction image only over the independent set `B`.  Every vertex of
`Y-B` has a neighbour in `A`, so it was adjacent to the contraction image
and avoids its colour.  Thus `B`, and no other boundary vertex, receives
that colour: it is an exact boundary block.  If `G[Y-B]` is a clique, that
exact-block equality partition is unique up to palette names, so it agrees
with the partition induced by `d` and the two shore colourings glue.
\(\square\)

### Corollary 4.3 (a shore-confined clean prescribed six-fan)

For every `xv in J`, there are six `v`--`X` paths in `G[Q union X]`
which share only `v`, have six distinct ends in `X`, and meet `X` only at
their ends.  One path is the edge `vx`; the other five preserve the five
colour-indexed first edges supplied by Lemma 3.1.  No assertion is made
about the colours of their rerouted boundary ends.

#### Proof

Fix `xv in J`.  Among the five paths from Lemma 3.1, let `D subseteq X`
be the set of ends of the direct one-edge paths, put `h=|D|`, and let `S`
be the set of first neighbours of the other `ell=5-h` paths.  The direct
ends are distinct, avoid `x`, and the vertices of `S` are distinct.

If `ell=0`, the five direct paths together with `vx` have the required
form.  Suppose `ell>=1`, put

\[
                         T=X-(D union \{x\}),
\]

and seek `ell` pairwise vertex-disjoint `S`--`T` paths with distinct ends
in the graph `G[(Q-{v}) union T]`.  If they did not exist, the vertex-set
form of Menger's theorem would give a set `Z` of order at most `ell-1`
separating the surviving sources from the surviving terminals.  Some
source survives.  Its component `A` after deleting `Z` contains no member
of `T-Z` and satisfies

\[
                 N_G(A) subseteq \{v\} union D union \{x\} union Z.
\]

The right side has order at most

\[
                         1+h+1+(\ell-1)=6.
\]

Another component of `G-X` lies outside `A` and its displayed
neighbourhood, contradicting seven-connectivity.  Thus the linkage exists.
Prepend the prescribed edges from `v`, retain the `h` direct paths, and add
`vx`.  The linkage avoids `D union {x}`, so the six resulting paths have
distinct boundary ends and are otherwise disjoint.  Their open interiors
lie in `Q`.  \(\square\)

## 5. Sharp quantifier obstruction and the missing hypothesis

For `J={e_1,e_2}`, the proved information has the following form after all
colourings are restricted to the common deletion host:

\[
\begin{array}{c|c|c}
 \text{operation}&(e_1,e_2)\text{ signature}&
                    \text{boundary partition}\\ \hline
 G-e_1&(\mathrm{equal},\mathrm{proper})&\Pi_1\ne\Pi_\tau\\
 G-e_2&(\mathrm{proper},\mathrm{equal})&\Pi_2\ne\Pi_\tau\\
 G-\{e_1,e_2\}&(\mathrm{equal},\mathrm{equal})&\Pi_\tau.
\end{array}                                             \tag{5.1}
\]

The all-proper signature is forbidden because it would colour `G`.
Table (5.1) satisfies both inclusion-minimality and every response supplied
by proper-minor criticality.  There is no valid quantifier exchange from

\[
 \forall e\in J\ \exists\text{ a colouring of }G-e
\]

to a colouring of some `G-e` having the separately prescribed partition
`Pi_tau`.  The existing
[single-edge response-alignment barrier](../barriers/hc7_degree7_single_edge_response_alignment_barrier.md)
realizes this exact response-table obstruction at boundary-partition level.
It is not asserted to realize the full hypothetical `HC_7` host.

The logically smallest extra hypothesis for a singleton aligned response is

\[
       \exists e\in J:\quad
       \Pi_\tau\in\operatorname{Resp}(e,X),            \tag{5.2}
\]

where `Resp(e,X)` denotes the boundary equality partitions induced by
proper six-colourings of `G-e`.  A usable structural version of (5.2) is a
response-transport theorem: for some singleton contraction response, a
boundary Kempe path to `tau` must lift through the same one-edge-deletion
graph.  Boundary Kempe connectivity alone is insufficient; the lifts, and
therefore the operation provenance, must be retained.

Absent such a transport theorem, Theorem 4.1 is the strongest direct
consequence of minimality: it spends the aligned common-deletion colouring
to obtain either a literal smaller response shore or a family of clean
fans, but it does not manufacture a singleton aligned response, a common
complete partition, or a `K_7`-minor model.

The decrease in (4.4) is a generic exact-seven response-shore decrease.  It
is not claimed to preserve the selected anti-neighbourhood component or the
labels required by the primary same-host anti-neighbourhood descent.

## Dependencies

- [degree-eight common-root star response](../results/hc7_degree8_common_root_star_response.md)
- [prescribed-spoke fan or exact-seven separation](../results/hc7_order8_prescribed_spoke_reduction.md)
- [generic exact-seven selected-response restart](../results/hc7_generic_exact7_response_restart.md)
