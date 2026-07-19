# Independent audit: boundary-crossing persistent-edge reduction

**Verdict:** GREEN for the exact source revision identified below.

This is a separate internal mathematical audit.  It verifies the simultaneous
contraction colouring, the one-extra-colour list reduction, the orientation of
the two closed-shore extension sets, and the degree and separator conclusions.
It is not external peer review and does not close the surviving high-excess
shore-filling case.

## Audited revision

The audited file is
`results/hc7_boundary_crossing_persistent_edge_reduction.md`.

**Source SHA-256:**
`f57949ded3c17962004cbe1c7f1a36bb5ec9667cc79a901326b44234dfa41326`.

After the GREEN audit, the source was moved from `active/` to `results/`,
its dependency links were made local to that directory, and its status line
was changed to link this audit.  The mathematical statement and proof are
unchanged; this audit is repinned to the resulting source hash above.

## 1. Simultaneous contraction and the bypass alternative

The vertices `x,v,u` are distinct, the only edges among them are
`xv=g` and `vu=f`, and `xu` is absent because `x` and the branch set `B`
are the deficient pair of the labelled near-`K_7` model.  Contracting the
two-edge tree therefore produces a proper minor.  Expanding a six-colouring
of that minor gives all three vertices one colour and is proper on
`G-{g,f}`: after the two tree edges are deleted, the three expanded vertices
are independent, and every other host edge is represented by an edge
incident with the contracted vertex.

The hypotheses of the audited shared-interface bichromatic-bypass theorem
then hold with centre `v` and leaves `x,u`.  Its saturated alternative and
its two-component bypass alternative are quoted without strengthening.  In
the latter case its two individual Kempe switches really do give proper
six-colourings of `G-f` and `G-g`, respectively.

In the saturated alternative the simultaneous-contraction colouring need
not itself extend to `G-f`.  This causes no gap: `G-f` is independently a
proper minor and hence has a six-colouring, while deletion-persistence is a
model statement independent of which such colouring is selected.  Section
3 correctly starts afresh with an arbitrary proper six-colouring of `G-f`.

## 2. The unique extra boundary colour

Let `psi` be a proper six-colouring of `G-f` and put
`theta=psi(u)=psi(v)`.  The equality is forced: if the endpoints received
different colours, restoring `f` would six-colour `G`.

For every boundary neighbour `y` of `v` other than `u`, the edge `vy` is
still present in `G-f`.  Properness therefore gives
`psi(y) ne theta`.  Thus `u` is exactly the unique boundary neighbour of
`v` with colour `theta`, and in particular

\[
                    \theta\notin L(v).
\]

For each `z ne v` in `D`, no boundary edge incident with `z` was deleted,
so `psi(z)` avoids every colour on `N(z) cap X` and belongs to `L(z)`.
At `v`, `psi(v)=theta` belongs to precisely the enlarged list
`L(v) union {theta}`.  This verifies both the orientation and the
single-vertex nature of the one-extra-colour construction.

If `G[D]` were `L`-colourable, that colouring would glue to
`psi|G[A union X]`: the lists exclude all conflicts on edges from `D` to
`X`, `A` is anticomplete to `D`, and the colour assigned to `v` would avoid
`theta`, so the restored edge `uv` would also be proper.  This would
six-colour `G`.  Hence `G[D]` is not `L`-colourable.

A vertex-minimal induced non-`L`-colourable subgraph `K` is connected.  It
must contain `v`, since otherwise `psi|K` would colour it from `L`.  The
restriction `psi|K` is an `L^+`-colouring, so every hypothesis of the
audited one-extra-colour critical-kernel theorem is present.

## 3. The returned separation and extension orientation

For `S=N_G(V(K))`,

\[
 C=G[V(K)\cup S],\qquad O=G-V(K)
\]

are induced subgraphs with intersection `G[S]`, their union contains every
edge of `G`, and there is no edge between their open sides.  The `C`-side
is nonempty because it contains `K`; the `O`-side is nonempty because the
nonempty set `A` is anticomplete to `D`, hence disjoint from both `K` and
`S`.  Thus this is an actual separation.

Since `v in K` and `uv` is an edge, `u in S`.  The only edge on which
`psi|C` can fail to be proper is `f=uv`; all other edges occur in `G-f`.
Meanwhile `v` is absent from `O`, so `psi|O` is proper.  Both restrictions
induce the same equality partition `Pi` on the literal boundary `S`.
Consequently

\[
 \Pi\in\operatorname{Ext}(C-f,S)\cap\operatorname{Ext}(O,S).
\]

If `Pi` belonged to `Ext(C,S)`, the colours on its distinct blocks could be
permuted to agree with the corresponding block colours of `psi|O`; the two
colourings would then glue to a six-colouring of `G`.  Hence
`Pi notin Ext(C,S)`, with exactly the orientation claimed in (3.6).

The full neighbourhood `S` separates `K` from `A`, so seven-connectivity
gives `|S|>=7`.  If `K` is a proper induced subgraph of `G[D]`, then its
vertex set is a proper subset of `D`; thus the component-order descent is
strict.  The edge `uv` still crosses the new boundary, and neither the
model nor the graph has been altered, so the labelled model remains in
`G-f`.  The source correctly warns that the positions of all seven branch
sets relative to this new separation are not thereby preserved.

## 4. Shore-filling degree calculation

When `K=G[D]`, there are no residual vertices of `D` outside the kernel.
Writing `q(z)` for the number of distinct boundary colours and `rho(z)`
for the number of repeated boundary-colour occurrences gives

\[
 |L(z)|=6-q(z),\qquad
 |N(z)\cap X|=q(z)+\rho(z).
\]

Therefore

\[
 d_G(z)=d_{G[D]}(z)+|N(z)\cap X|
       =6+\varepsilon(z)+\rho(z),
\]

which verifies (4.2).  Vertex-minimality and the `L^+`-colouring established
above justify applying the full one-extra-colour trichotomy to
`G[D],L,v`.

If `epsilon(z)+rho(z)<=2`, the identity gives `d_G(z)<=8`, while
seven-connectivity gives `d_G(z)>=7`.  The set `N_G(z)` separates the
singleton `z` from the nonempty set `A`, because `A` is anticomplete to
`D`.  It is therefore the boundary of an actual order-seven or order-eight
separation.  When `|D|>1`, the singleton side is strictly smaller than the
old connected side.

If all such descents are excluded, the exact identity forces
`epsilon(z)+rho(z)>=3` and hence `d_G(z)>=9` for every `z in D`.  A tight
vertex has `epsilon(z)=0`, so it has at least three repeated boundary-colour
occurrences, exactly as stated.

Finally, if `D={v}`, non-`L`-colourability of the singleton forces
`L(v)=emptyset`, hence `q(v)=6` and `epsilon(v)=0`.  Since `|X|=8`,
`rho(v)<=2`, so the low-degree separator conclusion always applies.  The
singleton-shore conclusion is therefore also valid.

## 5. Trust boundary

At the audited hash the source proves:

1. a valid simultaneous-contraction saturation-or-bypass alternative at
   the critical edge and the deletion-persistent boundary edge;
2. a strict full-neighbourhood descent whenever the one-extra-colour kernel
   is a proper part of the old shore;
3. the exact opposite-shore extension orientation for the returned boundary
   partition; and
4. an order-seven/order-eight singleton-side separation or the stated
   shore-filling high-excess normal form.

It does **not** prove that the returned boundary has order exactly seven,
that both closed shores admit a common boundary partition, that the strict
descent preserves useful placements of all model labels, that the persistent
edge lies in a prescribed list-critical kernel, or that `G` contains a
`K_7` minor.  No unresolved gap remains inside the stated reduction at the
audited source revision.
