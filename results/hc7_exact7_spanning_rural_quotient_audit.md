# Independent audit: spanning rural quotient quadrichotomy

Audited file: `results/hc7_exact7_spanning_rural_quotient.md`.

## Final verdict

**GREEN.**  The strengthened theorem is valid for each eligible spanning
triple.  Its key observation is exact: a web-cell component avoids the
roots and the whole pole-neighbour sets `Q,P`, so it has no edge to either
pole.  The exposure bound then gives at most five whole-graph neighbours,
contradicting seven-connectivity.  No carrier minimization, cell movement,
or bilateral-gate outcome is needed.

Component absorption, the allowed carrier set `Z`, side-terminal scope,
and quotient edge accounting also pass audit.  The theorem does not claim
that absorption preserves three-connectivity or the earlier universal
capture property; it tests low connectivity and a set-terminal cross
afresh.

One downstream limitation remains unchanged: a rotation-compatible
edge-minimal tree embeds only a selected connector inside a pole, not the
induced pole graph.  Thus the quadrichotomy is proved, but the final HC7
conversion still has an induced-pole branch in addition to the literal
low-cut/shared/cross/alternating-carrier certificates.

## 1. Per-triple alternatives

Fix any eligible spanning triple `(K,X,Y)`.  If `J[K]` is not
three-connected, outcome 1 holds.  If `Q cap P` is nonempty, outcome 2
holds.  If the specified two-linkage exists, outcome 3 holds.  Otherwise

\[
 J[K]\text{ is three-connected},\qquad Q\cap P=empty,
\]

and the augmented carrier with artificial terminals `alpha,beta` is
crossless.  The set-terminal Two Paths theorem therefore gives one web
with frame `(x,alpha,y,beta)`.

The geometric part of the audited block-terminal theorem applies directly:

* every vertex of `Q union P` and both roots lie on the rib; and
* every component `D` of actual carrier vertices in a nonempty cell has

  \[
       N_{J[K]}(D)=Delta,qquad |Delta|=3.
  \]

The cited connectedness of `J[K-D]` is also valid, though the strengthened
proof no longer needs it.

## 2. Why an actual cell is impossible

The cell component `D` contains neither root and no member of `Q union P`.
Because these are the **whole** nonroot pole-neighbour sets,

\[
 Q=N_K(X)-\{x,y\},\qquad
 P=N_K(Y)-\{x,y\},
\]

any edge from `D` to `X` would put its carrier end in `Q`, and any edge
from `D` to `Y` would put its carrier end in `P`.  Hence

\[
                         E_J(D,X\cup Y)=empty.       \tag{2.1}
\]

This is stronger than a one-pole or two-pole cell assignment: no such
literal pole contact can exist.

There is a nonempty far side.  The disjoint sets `Q,P` contain six distinct
rib vertices, while the gate has only three vertices, so at least one
marked carrier vertex lies outside `D union Delta`.  Thus `N_G(D)` is a
genuine separator.  Seven-connectivity gives

\[
                         |N_G(D)|\ge7.               \tag{2.2}
\]

On the other hand, exactly three neighbours of `D` lie in `K`; equation
(2.1) excludes every other neighbour in the spanning graph `J`; and the
uniform exposure hypothesis permits at most two neighbours outside `J`.
Therefore

\[
                         |N_G(D)|\le3+2=5,           \tag{2.3}
\]

a contradiction.  Consequently no nonempty actual web cell exists.

This count uses no completion edge.  The gate equality is a literal
neighbourhood statement inside the induced carrier.

## 3. Reading the planar quotient

Once all actual carrier vertices lie on the rib, every quotient edge is
accounted for.

* Carrier edges are literal rib edges.
* A pole--nonroot-carrier edge is represented by `alpha Q` or `beta P`.
* Pole--root edges are among the four outer-frame pairs.
* There is no pole--pole edge because `X,Y` are anticomplete.
* The triple spans `J`, so there is no fourth vertex class or leftover
  quotient edge.
* Internal pole edges become loops, and parallel copies may be suppressed
  in the stated simple quotient.

Thus outcome 4 is a literal planar simple quotient.  Completion-only edges
serve solely as the planar supergraph certificate.

## 4. Allowed carrier set and exposure

In the exact Moser shore,

\[
 Z=V(J)-(U-\{x,y\})=V(D_t)\cup\{t,x,y\}.
\]

The fixed frame pole `X_0=A union B` contains the other three vertices of
`U`, so component absorption cannot put them into `K`.  Every absorbed
carrier component consists of open-shore vertices and possibly the side
terminal `t`; hence `K subseteq Z`.

For any nonempty `C subseteq Z-{x,y}`, outside-shore neighbours lie only
among `v,w`: open-shore vertices can see `w`, and `t` can see `v`, while
the audited nonedge `wt` and opposite-shore anticompleteness exclude a
third outside neighbour.  The uniform bound `(E)` is therefore valid even
when the carrier contains `t`.

## 5. Component absorption and side-terminal scope

Lemma 3.1 is correct.  If `X_0,Y_0` occupy distinct components of
`J-V(K_0)`, every other component has an edge to connected `K_0`; their
union with `K_0` is connected.  The selected two pole components are
connected and anticomplete, and the three parts span `J`.  Old foreign
portals and old `L`-attachments remain in `K_0`, so both size-three lower
bounds survive.

Absorption can create a cutvertex or a new cross.  That causes no gap:
these are outcomes 1 and 3 of the per-triple theorem.  The proof never
asserts monotonicity of three-connectivity or universal capture.

The assignment of `t` is only topological.  A same-component
`X_0-Y_0` path may run through `t`, and an absorbed spanning part may
contain `t`; neither is automatically an eligible supported-core move.
The source correctly retains the first as a literal connector and requires
later label-faithful handling.

## 6. Trust boundary

The proved theorem is exactly

\[
\begin{array}{c}
\text{each eligible spanning triple with }|Q|,|P|\ge3\\
\Downarrow\\
\text{low carrier cut, shared portal, set-terminal cross,}\\
\text{or planar whole-shore two-pole quotient.}
\end{array}
\]

It closes the leftover-component assignment gap at the **quotient** level.
It does not embed either induced pole graph.

After outcome 4, the tree-pole theorem applied to an edge-minimal connector
returns either alternating literal carriers or a connector compatible with
the selected pole rotation.  In the compatible case, unused vertices and
extra edges of the induced pole remain unembedded.  Therefore a complete
downstream conversion must also handle

\[
 \text{rotation-compatible connector but non-disk-embedded induced pole},
\]

unless a separate spanning-pole disk theorem is supplied.  This limitation
does not affect the GREEN verdict for Theorem 2.1.
