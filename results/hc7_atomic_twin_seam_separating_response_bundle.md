# Separating twin seam: the exact response bundle

**Status:** proved and independently audited.  It strengthens the
separating-edge input, but it is not the separating-edge decoder.

## 1. Setup

Use the notation of
`../results/hc7_atomic_twin_seam_separating_gate_bridge.md`.  Thus

\[
 e=zu,
 \qquad f=dt\quad(d\in D,\ t\in Z),
\]

`phi` is a six-colouring of `G-e`, the vertices `z,u` have common colour
`alpha`, and `L` is the `alpha-beta` component containing them.  Assume
that `f` is a bridge of `L`.  Let `X` be the `z`-component of `L-f`, and
swap `alpha,beta` on `X`.  Denote the resulting six-colouring of `G-f` by
`psi`, and put

\[
                         \gamma=\psi(d)=\psi(t).
\tag{1.1}
\]

Let `delta` be the other member of `{alpha,beta}`.  In particular
`{gamma,delta}={alpha,beta}`.

## 2. The complementary named-edge cycle

### Lemma 2.1

The `gamma-delta` graph of `psi` contains a literal `d-t` path `Q_0`
which contains `e` and avoids `f`.  Consequently `Q_0+f` is a literal
cycle containing both named edges `e,f`.

### Proof

The bridge `f` has one end in `X` and one in the other component of
`L-f`.  The vertices `z,u` are in those two components respectively.
If `d in X`, take a path in `L[X]` from `d` to `z`, then the edge `zu`,
then a path in the other component from `u` to `t`.  If `t in X`, use
the symmetric path from `d` to `u`, then `uz`, then from `z` to `t`.
The two component paths are disjoint and the resulting path is simple.

Swapping on `X` preserves the two-colour vertex set and every two-colour
edge within either component.  It makes `e` proper and its ends receive
the two colours `gamma,delta`.  Hence the displayed path is a
`gamma-delta` path for `psi`.  Adding `f`, whose ends are the two ends of
the path, gives the asserted cycle.  \(\square\)

## 3. Four further response-matched bypasses

### Lemma 3.1 (four-colour bypass bundle)

For each of the four palette colours

\[
                 \epsilon\notin\{\gamma,\delta\},
\]

the `gamma-epsilon` graph of `psi` contains a literal `d-t` path
`Q_epsilon`.  Every such path avoids both `e` and `f`.  For distinct
colours `epsilon,epsilon'`, the two paths can intersect away from `d,t`
only at vertices coloured `gamma`.

### Proof

The edge `f` is absent under `psi` and its ends have common colour
`gamma`.  If the `gamma-epsilon` component containing `d` did not contain
`t`, swapping that component would make the colours of `d,t` different.
Restoring `f` would then give a six-colouring of `G`, contrary to the
counterexample hypothesis.  Thus a `d-t` path exists.

The path avoids `f` because it lies in `G-f`.  It avoids `e` because the
ends of `e` have colours `gamma,delta`, and `delta ne epsilon`.  Finally,
a vertex common to a `gamma-epsilon` path and a
`gamma-epsilon'` path has colour in

\[
             \{\gamma,\epsilon\}\cap
             \{\gamma,\epsilon'\}=\{\gamma\}.
\]

This proves all claims.  \(\square\)

The separating bridge therefore does not merely return the two boundary
mismatch paths.  The same named response contains a five-rung bypass
bundle: one rung through `e` and four colour-distinct rungs avoiding both
named edges.

## 4. Rank two or one common palette gate

For the four colours in Lemma 3.1, let `C_epsilon` be the
`gamma-epsilon` component containing `d,t`.  Let `U` be the spanning
subgraph of `G-f` whose edges are **all** edges joining a `gamma`-coloured
vertex to a vertex of one of those four colours.  Equivalently,

\[
 U=\bigcup_{\epsilon\notin\{\gamma,\delta\}}
     (G-f)[\psi^{-1}(\{\gamma,\epsilon\})].
\tag{4.1}
\]

This full union is important: a path may switch from one alternate colour
to another at a `gamma` vertex.

### Theorem 4.1 (exact lock-layer dichotomy)

Exactly one of the following structural alternatives is forced.

1. `U` contains two internally vertex-disjoint literal `d-t` paths.
2. There is a vertex `w notin {d,t}`, coloured `gamma`, such that
   `U-w` has no `d-t` path.  In fact `w` lies on every `d-t` path in
   every one of the four components `C_epsilon`.

### Proof

Apply the vertex form of Menger's theorem in `U`.  The vertices `d,t`
are nonadjacent there, because the simple edge `dt=f` was deleted.  If
there are not two internally disjoint paths, one internal vertex `w`
separates them.

Each `C_epsilon` itself contains a `d-t` path.  Therefore `w` belongs to
every `C_epsilon`; otherwise that component supplies a path avoiding
`w`.  Its colour consequently lies in

\[
        \bigcap_{\epsilon\notin\{\gamma,\delta\}}
        \{\gamma,\epsilon\}=\{\gamma\}.
\]

The same argument says that every `d-t` path in every layer contains
`w`.  \(\square\)

## 5. What seven-connectivity adds in the gate outcome

### Lemma 5.1 (four disjoint mixed escape channels)

Assume outcome 2 of Theorem 4.1.  Then `G-f` contains four internally
vertex-disjoint `d-t` paths, all avoiding `{e,w}`, such that each path
either contains a `delta`-coloured internal vertex or contains an edge
whose two ends both have colours different from `gamma`.

### Proof

Since `G` is seven-connected, `G-d` is six-connected and
`d_G(d)>=7`.  Apply the fan lemma in `G-d` from `t` to six distinct
vertices of `N_G(d)-{t}`.  Adding the six incident edges at `d` gives six
internally vertex-disjoint `d-t` paths in `G-f`.

At most one of the six paths contains the internal edge `e`, and at most
one contains the internal vertex `w`.  Hence at least four avoid both.
None is a path in `U-w`, by Theorem 4.1.  A proper-colouring edge belongs
to `U` exactly when it joins a `gamma` vertex to a vertex whose colour is
one of the four colours outside `{gamma,delta}`.  Thus a path leaving `U`
must use a `delta` vertex or an edge with neither end coloured `gamma`.
The four witnesses are mutually disjoint because their parent paths are
internally disjoint.  \(\square\)

This is the exact contribution of ordinary seven-connectivity.  It does
not turn the palette gate `w` into a graph separator; instead it forces
four disjoint paths which escape the lock layers through mixed-colour
geometry.

## 6. The common double-contraction chamber

The bridge response is not the only exact coupling of `e,f`.  Their common
double contraction gives a second, state-preserving fork.

### Lemma 6.1 (twin double-contraction saturation fork)

Let `c` be any six-colouring of `G/e/f`, lifted to `G-{e,f}`.  If `z` can
be recoloured to restore `e` and `d` can be recoloured to restore `f`, then
`G` is six-colourable.  Consequently every such `c` satisfies

\[
 \boxed{
 z\text{ sees all five alternate colours outside }u
 \quad\text{or}\quad
 d\text{ sees all five alternate colours outside }t.}
\tag{6.1}
\]

### Proof

The lifted colouring has `c(z)=c(u)` and `c(d)=c(t)`.  If `z` is free,
recolour only `z` and restore `e`; this gives a colouring `c_f` of `G-f`.
If `d` is free, recolour only `d` and restore `f`; this gives a colouring
`c_e` of `G-e`.

Neither recolouring changes a literal vertex of `Omega_D` or `Omega_E`.
On `Omega_D`, use `c_e` on the `D`-closed side and `c_f` on the
`B_D`-closed side.  Their boundary restrictions both equal that of `c`,
so they glue and colour `G`.  Equally, on `Omega_E`, use `c_f` on the
`E`-closed side and `c_e` on the `B_E`-closed side.  Thus simultaneous
freedom is impossible.  Negating it gives (6.1).  \(\square\)

This is stronger than comparing independently selected edge responses:
one double-contraction state is preserved on both twin boundaries.  Its
output is nevertheless palette saturation, not five labelled contacts.

## 7. Why the two mismatch paths themselves cannot be the decoder

Put `K=Omega_D intersect Omega_E`.  Since

\[
                  D\cup\Omega_D\subseteq B_E\cup\Omega_E,
\]

any `t-r` path with internal vertices in `D` and with `r in K` is
simultaneously eligible as both mismatch paths of the separating-gate
theorem.  In particular the theorem permits

\[
                              P_D=P_E.                 \tag{7.1}
\]

Thus path multiplicity alone supplies no fork, no second carrier and no
strict receiver.  The smallest form is the literal path `t-d-c` with
`c in K`; it is realized by the current bounded falsification shell.

The palette-gate alternative is also a genuine local mechanism.  For four
distinct alternate colours, take vertices `d,t,w` of colour `gamma` and,
for each `epsilon`, vertices `a_epsilon,b_epsilon` of colour `epsilon`,
with paths

\[
                   d-a_\epsilon-w-b_\epsilon-t.
\tag{7.2}
\]

Every one-colour lock layer is forced through `w`.  Arbitrarily many
internally disjoint mixed bypasses may be added as paths

\[
                    d-r_i-s_i-t,
\]

where `r_i,s_i` receive two distinct non-`gamma` colours.  These raise
the literal local `d-t` connectivity without creating a path in any one
lock layer which avoids `w`.  Hence neither high connectivity nor the
four Kempe locks alone eliminates the gate.

## 8. Exact remaining decoding obligation

The separating branch has now reached a sharper non-enumerative fork:

* decode two internally disjoint response-matched lock-layer paths together
  with the twin boundary maps; or
* decode one common `gamma` gate together with the four disjoint mixed
  escape channels of Lemma 5.1.

The second branch is the precise countermechanism to a path-only decoder.
Any valid completion must use the literal twin duties or a second named
proper-minor response to label the mixed channels.  Calling `w` a small
separator, or assigning its palette sectors directly to model rows, would
be invalid.
