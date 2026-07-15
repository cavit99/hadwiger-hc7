# Audit: separating twin-seam response bundle

**Verdict:** GREEN for the precise formulation in
[`hc7_atomic_twin_seam_separating_response_bundle.md`](hc7_atomic_twin_seam_separating_response_bundle.md), with one essential
terminological qualification.  The Menger gate in Sections 4--5 is taken
in the **full union of the four non-`delta` two-colour layers**.  It is not
valid to replace that graph by the union of four arbitrarily selected lock
paths, nor by the five-layer union including the named `delta` layer.

The result is a useful response-local geometric certificate.  It is not a
labelled fifth bag, carrier, receiver, or terminal outcome.

## 1. The named complementary cycle is literal

Removing the bridge `f=dt` from the `alpha-beta` component `L` gives two
components, with `z` and `u` on opposite sides.  Its endpoints `d,t` are
also on opposite sides.  If `d` is on the `z`-side, concatenate a
`d-z` path in that side, the literal edge `e=zu`, and a `u-t` path in the
other side.  If `t` is on the `z`-side, use the symmetric concatenation.
The two component paths have disjoint vertex sets, so the concatenation is
simple and avoids `f`.

The side swap preserves the `alpha-beta` vertex set and every two-colour
edge internal to either component.  It gives `d,t` the common colour
`gamma` and gives the ends of `e` the colours `gamma,delta` in some order.
Thus the concatenation is a literal `gamma-delta` `d-t` path in `G-f`.
Adding `f` gives the claimed cycle.  This remains valid whichever endpoint
of `f` lies on the swapped side and whichever of `alpha,beta` is `gamma`.

All four vertices `d,t,z,u` are distinct in the frozen seam: they lie,
respectively, in `D`, `Z`, `E`, and `B_0`.  Hence `e` is genuinely an
internal edge of the path rather than an endpoint edge.

## 2. The other four locks coexist in the same response

The side-swapped colouring `psi` is proper on `G-f`, and `d,t` both have
colour `gamma`.  For every colour
`epsilon notin {gamma,delta}`, if their `gamma-epsilon` components were
different, swapping the component containing `d` would separate their
colours while preserving every edge of `G-f`.  Restoring `f` would then
six-colour `G`.  Therefore the required `d-t` path exists.

It cannot use `e`: the two ends of `e` have colours `gamma,delta`, whereas
the path uses only `gamma,epsilon`.  It cannot use `f`, which is deleted.
For two different alternate colours, an intersection vertex has colour in

\[
 \{\gamma,\epsilon\}\cap\{\gamma,\epsilon'\}=\{\gamma\}.
\]

No disjointness follows from this observation.

## 3. The exact Menger graph and the palette of its cutvertex

Let `U` contain **all** edges of `G-f` whose colour pair is
`{gamma,epsilon}` for one of the four colours outside
`{gamma,delta}`.  The endpoints `d,t` are nonadjacent in `U`, since the
host is simple and their only edge `f` has been deleted.

Vertex Menger in `U` gives either two internally disjoint `d-t` paths or
an internal one-vertex `d-t` separator `w`.  Each of the four full
`gamma-epsilon` components containing `d,t` contains a `d-t` path.  Hence
such a separator belongs to all four components.  Its colour belongs to
the intersection of their four palettes and is therefore `gamma`.
Moreover every `d-t` path in each component contains `w`, since each is a
path in `U`.

The use of the full layer union is indispensable.  For example, select
the path

```text
d(gamma)-a(epsilon)-w(gamma)-b(epsilon)-t(gamma)
```

but add the same-layer detour

```text
a(epsilon)-x(gamma)-c(epsilon)-t(gamma).
```

The selected path goes through `w`, while
`d-a-x-c-t` avoids `w`, leaves the selected-path union only through
`gamma-epsilon` edges, and uses neither `delta` nor a mixed non-`gamma`
edge.  Thus Sections 4--5 would be false if “union” meant only the chosen
paths.  The detour is included in the full graph `U`, where it correctly
forces the rank-two outcome instead.

The `delta` layer is deliberately excluded from `U`.  Including it changes
the dichotomy because the named path through `e` can itself bypass a gate,
and it also changes the escape-edge classification below.

## 4. Seven-connectivity gives four genuine mixed escapes

Seven-connectivity implies that `G-d` is six-connected and that
`|N_G(d)-{t}|>=6`.  The fan lemma in `G-d`, from `t` to six distinct
members of `N_G(d)-{t}`, followed by the six corresponding incident edges
at `d`, gives six pairwise internally vertex-disjoint `d-t` paths in
`G-f`.

The seam makes `z,u` distinct from `d,t`, so at most one of these six paths
uses the internal edge `e=zu`.  At most one contains the internal vertex
`w`.  Deleting those at most two paths leaves at least four pairwise
internally disjoint paths avoiding both `e` and `w`.  This counting remains
valid if `w` equals `z` or `u`; then the two discarded classes overlap and
the bound only improves.

Since `U-w` contains no `d-t` path, each of the four paths has an edge not
in `U`.  In the proper colouring `psi`, an edge outside `U` is either

* incident with a `delta`-coloured vertex; or
* has both ends coloured differently from `gamma`.

Indeed every edge from `gamma` to any of the four remaining colours is,
by definition, in `U`, and a `gamma-gamma` edge cannot occur.  As `d,t`
have colour `gamma`, every `delta` vertex on such a path is internal.  This
proves the four mixed escape channels exactly as stated.

An equivalent direct proof of the path count is that the local
`d-t` connectivity of `G-f` is at least six and loses at most one on
deleting `w`; among five resulting paths at most one uses `e`.  The fan
proof in the source avoids any ambiguity about adjacent-terminal Menger.

## 5. The double-contraction saturation fork is state-preserving

The four named vertices of `e=zu` and `f=dt` are distinct.  A colouring
`c` of `G/e/f`, lifted to `G-{e,f}`, therefore satisfies

\[
                 c(z)=c(u),\qquad c(d)=c(t),
\]

and is proper on every other original edge.

Suppose first that an alternate colour is absent from
`N_G(z)-{u}`.  Recolouring only `z` with that colour restores `e` and
gives a colouring `c_f` of `G-f`.  Similarly, freedom at `d` means that
recolouring only `d` restores `f` and gives a colouring `c_e` of `G-e`.
The two alternate colours need not be the same.

Neither recoloured vertex belongs to either twin boundary:

\[
 z\in E,\quad d\in D,
 \qquad z,d\notin\Omega_D\cup\Omega_E.
\]

Consequently `c_f` and `c_e` retain literally the same boundary colours,
not merely the same equality partition.

The closed-side assignment in the source is correct and essential.  On
`Omega_D`:

* use `c_e` on `D union Omega_D`; its only missing edge `e` has both ends
  outside that closed side, while `f` has been restored; and
* use `c_f` on `B_D union Omega_D`; its only missing edge `f` has its
  `D`-end outside that closed side, while `e` has been restored.

The two restrictions agree with `c` on every vertex of `Omega_D`, and
`N_G(D)=Omega_D` excludes an edge between the open shores.  They therefore
glue to a six-colouring of `G`.

The symmetric assignment on `Omega_E` is also correct:

* `c_f` colours `E union Omega_E`, which contains `e` but excludes the
  `D`-end of the deleted edge `f`; and
* `c_e` colours `B_E union Omega_E`, which contains `f` but excludes the
  `E`-end of the deleted edge `e`.

Again the boundary colours agree literally.  Either twin view alone is
enough to contradict simultaneous freedom.

Negating simultaneous freedom has exactly the claimed form.  The current
colour of `z` is the colour of `u`; failure to recolour `z` means that each
of the other five colours occurs in `N_G(z)-{u}`.  Likewise failure at `d`
means that all five alternate colours occur in `N_G(d)-{t}`.  Hence every
double-contraction colouring makes at least one of `z,d` five-colour
saturated relative to its named mate.

This conclusion is palette saturation only.  The five witnesses can be
repeated, lie in arbitrary twin regions, and do not inherit the five
boundary or model labels.

## 6. Exact edge cases and trust boundary

The following possibilities do not invalidate the result:

* `gamma` may be either `alpha` or `beta`;
* either `d` or `t` may lie in the swapped component `X`;
* the common gate `w` may be a boundary vertex, a lobe vertex, `z`, or
  `u`;
* the four lock components and their paths may overlap arbitrarily at
  `gamma` vertices;
* a mixed escape may traverse several twin shores and may meet either old
  full packet.

The last two points are also the exact limitation.  Neither Menger path is
localized to a prescribed twin shore.  A rank-two path pair shares the
literal endpoints `d,t` and has no automatic split into disjoint labelled
branch sets.  In the gate outcome, `w` is only a separator of the palette
layer graph `U`, not a vertex cut of `G`; the four escapes carry no old
boundary-duty labels.  Consequently the bundle does **not** yet give a
labelled fifth bag, an adaptive carrier return, a strict receiver, a
fixed-pair terminal, or a `K_7` model.

Its genuine value is narrower: one named contraction response now has a
literal cycle through `e,f` and either two internally disjoint
non-`delta` lock-layer routes, or one common `gamma` palette gate bypassed
by four pairwise internally disjoint mixed-colour channels.  A decoder
must next combine that certificate with the two literal twin boundary maps
or with a second named proper-minor response.  Palette membership alone
cannot assign the channels to model rows.
