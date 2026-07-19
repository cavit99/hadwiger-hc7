# Independent audit: persistent-edge fixed-trace alignment

**Audited source:**
`results/hc7_persistent_edge_fixed_trace_alignment.md`.

**Source SHA-256:**
`a01a86295dc0b797ab19f63049e893ac97dbb712a22a3dad6de0b316b07b4cab`.

**Verdict:** **GREEN.**  The response-set dichotomy, the induced-kernel
conclusion, the spanning edge-minimal-kernel conclusion and the endpoint
colour equality are correct with their stated quantifiers.  Membership in
the response set preserves the exact labelled colouring of the boundary;
no permutation of colour names is used.

Relative to the frozen mathematical revision checked independently, the
hash above changes only because the source status line now links this audit.

## 1. Boundary lists and exact gluing

The partition

\[
                    V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D
\]

and the absence of `A-D` edges make the list definition exact.  A proper
colouring of `G[D]` from

\[
                  L_c(w)=[q]-c(N_G(w)\cap X)
\]

avoids every colour conflict across `D-X`, and therefore glues to the fixed
colouring `c` of `G[A union X]`.  Conversely, every colouring that glues to
`c` uses at each `w in D` a colour in `L_c(w)`.  No condition on neighbours
in `A` is missing because there are no `A-D` edges.

The response set \(\mathcal R_f(X)\) records functions on the labelled
vertices of `X`.  Thus

\[
                         \psi|_X=c|_X
\]

is literal equality of the two boundary colourings, including their colour
names.  It is stronger than equality of the induced equality partition and
stronger than equality up to a colour permutation.

## 2. The binary response alternative

The first split is exhaustive and exclusive because it is membership versus
nonmembership of the one fixed function `c|_X` in `mathcal R_f(X)`.  Under
membership, choose one proper `q`-colouring `psi` of `G-f` with that exact
trace.  For every `w in D`, properness excludes from `psi(w)` all colours
used by its boundary neighbours.  Exact trace equality then gives

\[
                           \psi(w)\in L_c(w).
\]

Consequently `psi|_D` is one fixed `L_c`-colouring of the entire spanning
graph `G[D]-f`.  This single colouring is the common witness used in both
kernel conclusions; no change of trace or recolouring is hidden between
them.

## 3. Induced noncolourable kernels

Let `K` be any induced non-`L_c`-colourable subgraph of `G[D]`.  If `f` is
not an edge of `K`, then every edge of `K` belongs to `G[D]-f`, so the
restriction of `psi|_D` colours `K` from its inherited lists.  This
contradicts the choice of `K`.

Hence every such `K` contains `f`.  Because `K` is induced in `G[D]` and
`f=uv` is an edge of `G[D]`, this is equivalent to saying that `K` contains
both endpoints `u,v`; an induced subgraph containing both endpoints cannot
omit their edge.  The proof does not infer inducedness from edge-minimality
and does not conflate an induced kernel with a spanning kernel.

The quantifier is universal over all induced noncolourable subgraphs, not
only one vertex-minimal choice.  It is also harmless if no such subgraph
exists: in that case the assertion is vacuous, as it should be.

## 4. Spanning edge-minimal kernels

Part 2b has a separate and valid quantifier.  Start with any induced
non-`L_c`-colourable subgraph and any spanning subgraph `F` of it which is
itself non-`L_c`-colourable and edge-minimal with that property.  If `F`
omitted `f`, then `F` would be a subgraph of `G[D]-f`, regardless of which
other edges of the induced host it omitted.  The restriction of `psi|_D`
would therefore colour `F`, a contradiction.

Thus `f in E(F)`.  Edge-minimality is not needed for this containment
argument; it records the intended list-critical application and does not
weaken or invalidate the proof.  In particular, the theorem does not call
`F` induced, and it does not infer that `F` contains every edge between its
vertices.

## 5. Endpoint colour equality

If `G` is not `q`-colourable, the endpoints of `f` have the same colour in
every proper `q`-colouring of `G-f`: distinct endpoint colours would permit
the deleted edge to be restored without changing any colour.  This argument
is independent of the boundary trace and therefore applies, in particular,
to every colouring whose trace is exactly `c|_X`.  Part 2c has the correct
universal quantifier.

## 6. Dependencies and trust boundary

The proof is self-contained once the displayed separation, fixed colouring
and colourability of `G-f` are assumed.  The cited boundary-list result
supplies the intended noncolourable fixed-trace kernel, while the cited
single-portal result supplies a model edge whose deletion preserves a
spanning labelled near-complete minor model.  Neither dependency is silently
used to strengthen Theorem 2.1.

The theorem applies only after the persistent edge has been located inside
`G[D]` and only if the deletion response contains the prescribed trace.
Alternative 1 is the exact negation of that last condition.  The response
set is the full set of boundary traces of the deletion minor `G-f`; the
theorem makes no assertion about traces of the contraction `G/f` or of
other proper minors.

Finally, the result aligns one deleted edge with one fixed boundary
colouring.  It does not identify colours with minor-model branch-set labels,
produce disjoint Kempe paths, synchronize the opposite shore, construct a
`K_7`-minor model, or yield a colour-compatible order-seven separation.
