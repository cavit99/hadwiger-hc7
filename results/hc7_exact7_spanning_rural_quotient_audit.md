# Independent audit: spanning rural quotient

Audited file: `active/hc7_exact7_spanning_rural_quotient.md`.

## Final verdict

**GREEN, with one trust-boundary wording repair.**

The strengthened third exchange outcome is now the exact web-cell object
used in the proof: `D` is nonempty and proper, avoids the roots and all
marked portals, has a literal three-vertex carrier neighbourhood, leaves a
connected carrier, and sees both poles.  It cannot be witnessed vacuously
by the whole carrier.

The other earlier scope defects are also repaired:

* `x,y in K_0` is explicit in component absorption;
* the allowed carrier set
  `Z=V(J)-(U-{x,y})` prevents another literal `U`-vertex from drifting
  into the carrier;
* the exposure hypothesis is a uniform property of all subsets of `Z`;
* assignment of the side terminal is described as topological only;
* a same-component path is retained merely as a literal connector, not
  called a supported promotion; and
* the final paragraph explicitly requires preservation of the attained
  decorated-state duty.

No counterexample to the patched theorem was found.  The theorem does not
say that absorption preserves three-connectivity or universal capture; it
correctly makes their relevant failures into literal outcomes.

The sole remaining wording issue is the final boxed conversion.  Outcome
2 includes a shared portal, a set-terminal cross, and a bilateral literal
three-gate, none of which is automatically one of the “two alternating
literal carriers” returned by the tree-pole theorem.  Unless earlier
audited lemmas are cited to dispose of each of them, the box should list
all these certificates explicitly.

## 1. Spanning triples and the allowed carrier set

A spanning triple is a genuine partition into three nonempty connected
induced parts.  The roots stay in `K`, and anticompleteness of `X,Y` makes
their contractions legitimate distinct poles.

In the exact Moser side,

\[
 Z=V(J)-(U-\{x,y\})=V(D_t)\cup\{t,x,y\}.
\]

The original pair carrier `K_0` lies in `Z`.  The other three literal
vertices of `U` belong to the fixed frame blocks in
`X_0=A\cup B`; hence they remain in the component assigned to `X` and
cannot enter the absorbed carrier.  Every other component of
`J-V(K_0)` placed in `K` consists of open-shore vertices and possibly the
side terminal.  Thus the carrier produced by Lemma 3.1 really satisfies
`K subseteq Z`.

The exposure property is now independent of a drifting carrier:

\[
 C\subseteq Z-\{x,y\}
 \quad\Longrightarrow\quad
 |N_G(C)-V(J)|\le2.
\]

For open-shore vertices, exact shore anticompleteness leaves only the
deleted boundary vertex `w` outside `J`.  If `t` is present, it may also
see `v`; the audited nonedge `wt` and opposite-shore anticompleteness leave
no third outside neighbour.  Therefore `(E)` is valid for every carrier
eligible in the minimization, including one containing `t`.

## 2. Component absorption

Lemma 3.1 is literal and correct.

If `X_0,Y_0` lie in different components of `J-V(K_0)`, call those
components `X,Y`.  Every other component has an edge to connected `K_0`,
because distinct components of `J-V(K_0)` have no mutual edges and `J` is
connected.  Their union with `K_0` is therefore connected.  It contains
the roots, spans with `X,Y`, and the two poles are anticomplete.

The lower portal bounds survive.  Every old foreign portal in `K_0`
retains its edge to `X_0 subseteq X`, and every old marked attachment
retains its edge to `Y_0 subseteq Y`; none is moved out of `K`.

Absorption need not preserve three-connectivity.  For sharpness, take a
three-connected wheel carrier, attach two anticomplete singleton poles to
three disjoint nonroot carrier vertices each, and add another component
consisting of one leaf adjacent only to the wheel hub.  Lemma 3.1 must put
that leaf into the carrier, making the hub a cutvertex.  This is not a
counterexample: it lands exactly in outcome 1.

Likewise, adding absorbed ears can destroy the old universal-capture
property by creating new detours.  The proof never assumes otherwise.  It
recomputes `Q(K,X),P(K,Y)` and tests crosslessness in the enlarged induced
carrier.  A newly created cross is outcome 2; if none exists,
crosslessness itself is the exact input needed by the block-terminal web.

## 3. Minimization and the strengthened gated outcome

If no crossless eligible triple exists, every eligible triple has a shared
portal or a set-terminal cross, so outcome 2 holds.  Otherwise choose a
crossless eligible triple minimizing `|K|`.  If its carrier is not
three-connected, this is exactly outcome 1.

Assume it is three-connected.  Adjoin the two bookkeeping terminals.  The
set-terminal Two Paths theorem gives one web with frame
`(x,alpha,y,beta)`.  The geometric portion of the audited block-terminal
proof uses only this crosslessness and three-connectivity to show:

* every member of `Q union P`, as well as `x,y`, lies on the rib;
* a component `D` of actual carrier vertices in a nonempty cell avoids
  `\{x,y\} union Q union P`;
* `N_{J[K]}(D)` is exactly its literal three-vertex gate; and
* `J[K-D]` is connected.

The six distinct marked vertices give a carrier vertex outside
`D union N_{J[K]}(D)`, so `N_G(D)` is a genuine separator.  Seven-
connectivity yields at least seven neighbours.  Exactly three are in the
carrier and at most two are outside `J` by `(E)`, so at least two lie in

\[
                         V(J)-K=X\cup Y.
\]

If `D` sees both poles, it satisfies every clause of the strengthened
third bullet of outcome 2.  This is a nonvacuous literal certificate.

If it sees only `X`, move it to `X`.  The new pole is connected, remains
anticomplete to `Y`, and retains `X_0`; the retained carrier is connected,
contains the roots, and remains inside `Z`.  All old marked portals lie on
the rib rather than in `D`, so the lower bounds survive.  A new shared
portal or cross is an outcome; otherwise this is a smaller crossless
eligible triple, contradicting minimality.  No preservation of
threeconnectivity is needed for this contradiction.

Thus every actual cell is evacuated unless one of the literal outcomes has
already occurred.

## 4. Planar quotient and completion-edge discipline

When no actual cell remains, every actual edge of the augmented carrier is
contained in the planar web/rib certificate.  Completion-only facial-gate
edges are not used as host edges.

The quotient edge list is exhaustive because the triple spans `J`:

* internal carrier edges stay in the rib;
* a pole--nonroot-carrier edge is exactly an edge represented by
  `alpha Q` or `beta P`;
* pole--root edges are among the four outer-frame pairs;
* `X,Y` contribute no pole--pole edge because they are anticomplete;
* internal pole edges become loops; and
* parallel copies may be suppressed in the stated simple quotient.

Hence the quotient in outcome 3 is literally planar.  This is stronger
than the earlier selected-core quotient because every vertex of `J` has
been assigned to the carrier or a pole.  It still does not embed the
induced pole graphs; the tree-pole theorem addresses only selected
connectors and correctly leaves induced-pole rotation as further work.

## 5. Side terminal and labelled scope

The side terminal `t` may occur in any one of the three parts for purposes
of the abstract spanning partition and planar contraction.  This does not
preserve the earlier supported-core normalization, whose named core blocks
avoided `t`.  The source now says this explicitly.

In the same-component branch of Lemma 3.1, an
`X_0-Y_0` path avoiding `K_0` is literal.  If it runs through `t`, it cannot
automatically be absorbed into `A` or `B` and called the earlier supported
rank promotion.  The source now retains only the connector and requires a
separate label-faithful assignment.

Similarly, a set-terminal cross in the enlarged spanning carrier need not
already be the old labelled peel.  Its `Q` endpoint may see a vertex of
`X-X_0` rather than a specified original block, and its `P` endpoint may
contact `Y-Y_0` rather than the fixed region `L`.  Outcome 2 correctly
records actual paths only.  Any later conversion must establish the named
endpoint duty, exactly as the attained-duty caveat in Section 4 requires.

## 6. Trust boundary

The proved structural implication is

\[
\begin{array}{c}
\text{eligible spanning triple with }|Q|,|P|\ge3\\
\Downarrow\\
\text{minimum-carrier cut, shared portal, set-terminal cross,}\\
\text{bilateral literal three-gate, or planar spanning quotient.}
\end{array}
\]

This is a genuine infinite-family theorem and closes the nonspanning
carrier-assignment gap at quotient level.  It does not yet convert all its
literal obstruction outcomes into a `K_7`, common state, or fixed pair.

For precision, replace the final box by

\[
\boxed{\begin{array}{c}
\text{low cut, shared portal, set-terminal cross, bilateral three-gate,}\\
\text{or alternating pole carriers}\\
\Longrightarrow K_7,\text{ common state, or fixed pair,}
\end{array}}
\]

unless separate audited citations already discharge the first three
exchange certificates.  With that wording, the file's scope is exact.
