# Audit of the large-boundary singleton-response descent

**Audited file:** `hc7_large_boundary_singleton_response_descent.md`
**Audited SHA-256:**
`bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97`
**Audit date:** 2026-07-20
**Verdict:** **GREEN.**  The strict extremal bound, every numerical case in
the boundary-order argument, the singleton response, the
complementary-component transfer, and the paired shore-filling endpoint are
correct at the audited revision.

The promoted source differs from the originally audited revision
`ffd2dbc0b648d0921899aea13ffca9915a3478944cb4f5cc0ad4fa44b33958e2`
only in its status header and link to this audit; its theorem statements and
proof are unchanged.

Two scope repairs were made before this verdict.  Section 3 now states the
general conclusion `|B|<=9` and obtains equality only in the live enlarged
boundary where `|B|>=9`.  It also explicitly continues under the hypotheses
of Corollary 2.2, so its uses of seven-connectivity, `K_7`-minor exclusion
and proper-minor six-colourability are licensed.

## 1. Strict Mader bound

Mader's bound gives

\[
                         |E(G)|\le 5|V(G)|-15
\]

for the seven-connected graph under consideration.  If equality held,
Jorgensen's classification leaves the following cases.

- `K_{2,2,2,3}` has connectivity six.
- A nontrivial five-clique sum has a separator of order five.
- A single edge-maximal two-apex graph is six-colourable: delete an apex
  set of order at most two, four-colour the planar remainder, and use two
  fresh colours on the apex vertices.

The first two contradict seven-connectivity and the third contradicts
seven-chromaticity.  Equality is therefore impossible, and integrality
gives `|E(G)|<=5|V(G)|-16`.  This is a valid strengthening of the already
audited equality-classification consequence; it uses chromaticity to rule
out the single two-apex summand, where the earlier eight-connectivity
argument used a degree bound.

## 2. Boundary-order arithmetic

Put `b=|B|`, `n=|V(G)|` and `s=n-b=|A|+|D|`.  Under the contrary assumption
that every shore vertex has degree at least `b`, the degree sum is at least

\[
                 b(n-b)+7b.
\]

Together with the strict Mader bound this gives

\[
                 b(n-b)+7b\le 10n-32.                 \tag{A.1}
\]

The three numerical ranges are all handled correctly.

- For `b=10`, (A.1) reads `10n-30<=10n-32`, an immediate contradiction.
- For `b=11`, it reads `11n-44<=10n-32`, hence `n<=12`; the two nonempty
  shores instead give `n>=13`.
- For `b>=12`, rearrangement gives

  \[
  (b-10)n\le b^2-7b-32=(b-10)(b+3)-2.
  \]

  Thus `n<b+3`, so `n<=b+2`.  Since both shores are nonempty, equality
  holds and each shore is a singleton.  The `K_5`-minor-free boundary is
  four-colourable by the established `t=5` case of Hadwiger's conjecture;
  the two anticomplete singleton shores may share a fifth fresh colour.
  This contradicts seven-chromaticity.

Consequently some shore vertex has degree below `b`, while
seven-connectivity gives degree at least seven.  Theorem 2.1 follows.

## 3. Singleton-side response

For a selected vertex `v` in, say, `A`, the nonempty opposite shore `D` is
outside `N_G[v]`.  Hence `N_G(v)` is the boundary of a nontrivial separation
with order `d_G(v)<b`.

For any incident edge `vx`, `G-vx` is a proper minor and has a proper
six-colouring.  Its endpoints must receive one colour, since otherwise the
edge could be restored.  Restriction gives colourings of `G-v` and of
`G[N_G[v]]-vx`.  If the induced equality partition on `N_G(v)` extended
through the intact singleton side, a permutation of colour names would
align the two boundary colourings and glue them to a six-colouring of `G`.
Thus the intact singleton side rejects the partition.  Degree seven gives
an exact order-seven response, and degrees from eight through `b-1` give
the claimed strict boundary-order response.

## 4. Exact-block consequence and component transfer

Corollary 2.2 gives only `|B|<=9` in the general exact-block setting.  The
live enlarged boundary has

\[
 B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |S|=8,\quad |W|\ge2,
\]

so `|B|=7+|W|>=9`.  Therefore the surviving live case has exactly
`|B|=9` and `|W|=2`.  No equality claim is made for smaller unrelated
boundaries.

If a selected list-critical subgraph `K_A` is proper, any component `R` of
`G[A-V(K_A)]` is nonempty and strictly smaller than `A`.  The graph `G-R`
is a proper minor and has a six-colouring.  Its trace on the literal full
neighbourhood `N_G(R)` cannot extend through the intact graph on
`R union N_G(R)`, since such an extension would glue directly to the
colouring of `G-R`.  Moreover `N_G(R)` separates `R` from the nonempty
opposite shore, so seven-connectivity gives `|N_G(R)|>=7`.

This validates the corrected direct transfer.  In particular, the proof
does not use a colouring obtained by deleting all complementary components;
such a colouring would not automatically colour `G-R`.  The current proof
uses the proper minor `G-R` itself.

## 5. Spanning paired kernels

If both list-critical subgraphs span their shores, then each shore is
vertex-minimal non-list-colourable for the same fixed boundary colouring
`phi`.  For arbitrary `a in A` and `z in D`, list-colour `A-a` and `D-z`
and glue both colourings to `phi`.  The shores are anticomplete, so this is
a proper six-colouring of `G-{a,z}`.

Every colour appears in the neighbourhood of each deleted vertex.  A
colour excluded from the vertex's list already appears on a boundary
neighbour.  A colour in the list must appear on an internal neighbour in
every colouring of the vertex-deleted shore; otherwise the deleted vertex
could be restored.  Thus the simultaneous saturation assertion is exact.

For `v` in a spanning shore `Z`, let `q(v)` be the number of distinct
boundary-neighbour colours.  Then

\[
 |L_Z(v)|=6-q(v),\qquad
 \varepsilon_Z(v)=d_{G[Z]}(v)-|L_Z(v)|,
\]

and

\[
 \rho_Z(v)=|N_G(v)\cap B|-q(v).
\]

Since there are no edges to the opposite shore,

\[
 d_G(v)=d_{G[Z]}(v)+|N_G(v)\cap B|
       =6+\varepsilon_Z(v)+\rho_Z(v).
\]

List-criticality gives `epsilon_Z(v)>=0`.  At the nine-vertex boundary,
degrees seven and eight would respectively give an exact order-seven
response or a strict boundary-order response by the singleton argument.
Outside those exits every shore degree is at least nine, and hence

\[
                 \varepsilon_Z(v)+\rho_Z(v)\ge3.
\]

Finally, the standard degree-choosability argument applies to the vertices
with `epsilon_Z(v)=0`: colour the complement of a block of tight vertices,
delete the colours used by external neighbours from their lists, and note
that the residual lists have size at least the degree inside the block.  A
block which were neither complete nor an odd cycle would be
degree-choosable and would extend the colouring, contradicting criticality.
The tight-vertex subgraph is therefore a Gallai forest.  For a tight vertex
the preceding inequality reduces to `rho_Z(v)>=3`, as claimed.

## 6. Trust boundary

The audited result does not close the order-nine spanning endpoint.  A
proper-kernel transfer changes the trace and may return a boundary of
arbitrarily large order; it preserves neither the singleton block nor
minor-model labels.  The spanning endpoint supplies simultaneous saturated
deletion colourings and repeated boundary-colour incidences, but it does
not convert palette colours into distinct literal branch-set contacts.
