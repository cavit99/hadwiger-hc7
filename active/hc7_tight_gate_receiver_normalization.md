# Tight-gate packet analysis and receiver localization

**Status:** split audited. Lemma 2.1, the packet-vector arithmetic and
Theorem 4.1 are GREEN. The claimed accepted `S3` and ranked `S4`
normalizations are RED; see the adjacent audit.

This note records the promotion-safe receiver data for the audited tight
bypass-lobe transition. It uses only packets which are genuinely full to
the new boundary. In particular, it never treats either old `S`-full
packet as `Omega`-full.

The conclusion is an exact certificate trichotomy. A new `(1,3)` cell
closes, a new `(1,2)` cell has a named contraction on its actual packet-one
shore which returns a nonreflectable state intact on the packet-two shore,
and a new `(1,1)` cell has a named state, a one-step packet-sum drop and
five literal receiver lock/crossing alternatives. The latter two
certificates are not yet recognized recursive receivers.

## 1. Audited entry

Use the tight lobe supplied by
`../results/hc7_shortest_thin_lock_tight_bypass_transition.md`.  Write

\[
 V(G)=D\mathbin{\dot\cup}\Omega\mathbin{\dot\cup}B,
 \qquad |\Omega|=7,                                    \tag{1.1}
\]

where `D` is the selected component off the shortest thin spine,
`Omega=N_G(D)`, `B` contains the old rich shore, and `|D|<|A|`.  Both
open shores are nonempty and anticomplete.  Every component of
`G-Omega` is `Omega`-full.

Let `nu_D,nu_B` be the maximum numbers of pairwise vertex-disjoint
connected `Omega`-full packets in the two open shores.  The exact-seven
packet theorem gives, up to orientation,

\[
                  (\nu_D,\nu_B)\in
                  \{(1,1),(1,2),(1,3)\}.               \tag{1.2}
\]

Choose the named boundary edge

\[
                         f=dq,qquad d\in D, q\in\Omega, \tag{1.3}
\]

from the transition theorem, and contract it toward the literal label
`q`.  Let `c_f` be a six-colouring of `G/f`, expanded to a colouring of
`G-f` with `c_f(d)=c_f(q)`, and let `Pi_f` be its exact partition of
`Omega`.  The restriction to `G[B\cup\Omega]` is intact, while the same
state is attained on the other side by the named `f`-contraction.  The
audited demand inequality is

\[
                         d_H(\Pi_f)>\nu_B,
                  \qquad H=G[\Omega].                  \tag{1.4}
\]

If `f` is the separating first-entry edge of a second compulsory lock,
`c_f` may be chosen to be the explicit Kempe-swapped colouring in the
transition theorem.  It then retains the proved fixed-state toggle on the
old literals in the new boundary.

## 2. Regeneration on the actual packet-one shore

The orientation of (1.2) need not put the packet-one shore at `D`.
The following symmetric form of the demand argument repairs that issue.

### Lemma 2.1 (packet-one-side regeneration)

Suppose an actual exact-seven separation

\[
                         V(G)=L\dot\cup\Omega\dot\cup R \tag{2.1}
\]

has `nu_L=1` and `nu_R=q>=1`.  Then `L` is connected and
`Omega`-full.  For any boundary edge `g=xy`, with `x in L` and
`y in Omega`, contract `g` toward the literal label `y`.  Every exact
boundary state `Pi_g` returned by a six-colouring of `G/g` satisfies

\[
                         d_H(\Pi_g)>q                   \tag{2.2}
\]

in a `K_7`-minor-free non-six-colourable graph.  The state is intact on
the packet-`q` closed shore and is attained by the named contraction on
the packet-one side.

#### Proof

Every component of `G-Omega` is `Omega`-full.  If `L` had two components,
they would be two disjoint full packets, contrary to `nu_L=1`.  Thus `L`
is connected and full, and a boundary edge `g` exists.

The contraction preserves all seven boundary labels and lies wholly in
the closed `L`-side.  A six-colouring of `G/g` therefore restricts intact
to `G[R\cup\Omega]` and gives the same exact state on the named contracted
`L`-side.

If (2.2) failed, exact packet reflection using `q` full packets in `R`
would give either a literal `K_7` model or an intact colouring of
`G[L\cup\Omega]` with exact state `Pi_g`.  The first outcome is excluded.
The second aligns and glues with the intact `R`-side restriction of the
`G/g` colouring, producing a six-colouring of `G`.  This too is excluded.
Hence (2.2) holds.  \(\square\)

This lemma regenerates a state.  If `L` is not the old lobe `D`, the new
state need not be related to the fixed colouring of `G-zu`; no such
relation is used below.

## 3. Complete packet-vector analysis

### Theorem 3.1 (tight-gate certificate trichotomy)

The tight cell (1.1) has exactly one of the following outcomes.

1. **Closed `(1,3)`.**  If its packet vector is `(1,3)` in either
   orientation, then `G` has a literal `K_7` model or is six-colourable.
2. **Regenerated high-demand `(1,2)` certificate.** If its vector is
   `(1,2)`, orient
   the shores as `L,M` with
   \[
                         \nu_L=1,\qquad \nu_M=2.        \tag{3.1}
   \]
   There is a named boundary-edge contraction `g` in the closed `L`-side
   whose six-colouring returns an exact state `Pi_g` intact on
   `G[M\cup\Omega]`, and
   \[
                         d_H(\Pi_g)\ge3.                \tag{3.2}
   \]
   If `L=D`, the actual packet-one shore is the strict lobe, but the
   returned state is arbitrary high-demand rather than an accepted paired
   state. If `L=B`, the packet-one shore is not the strict lobe and no
   decreasing active-shore rank has been proved.
3. **State-labelled `(1,1)` certificate.** If
   `nu_D=nu_B=1`, the named state `Pi_f` satisfies
   \[
                         d_H(\Pi_f)\ge2,                \tag{3.3}
   \]
   is intact on the `B`-side and attained by the named `f`-contraction on
   the `D`-side, and the packet-sum value drops from the old atomic value
   three to
   \[
                         \nu_D+\nu_B=2.                 \tag{3.4}
   \]
   In addition, the state has the five receiver lock/crossing alternatives
   proved in Theorem 4.1 below. These data do not yet define a
   well-founded `S4` rank.

The literal boundary replacement is explicit throughout:

\[
       S=T_D\mathbin{\dot\cup}(S-T_D)
       \quad\longmapsto\quad
       \Omega=T_D\mathbin{\dot\cup}Z_D.                \tag{3.5}
\]

The labels in `T_D` are retained identically and the gate set `Z_D`
replaces the omitted old labels.  Formula (3.5) is a literal set
substitution, not a palette identification or a claimed pairing between
`S-T_D` and `Z_D`.

#### Proof

Outcome 1 is the audited adaptive `(1,3)` packet-reflection theorem,
which is symmetric in the orientation of the two shores.

For a `(1,2)` vector, use Lemma 2.1 with `q=2` on the shore which actually
has packet number one.  It produces the named state and gives
`d_H(Pi_g)>2`, which is (3.2).  The packet-one shore is connected and
full, while the other shore contains the two required disjoint full
packets. This is a regenerated high-demand exact-seven certificate. The
strict inclusion `D subsetneq A` is part of the audited tight-lobe
construction, but it supplies an active-shore decrease only when the
packet-one shore is `D`.

For `(1,1)`, inequalities (3.3) and (3.4) are (1.4) and arithmetic.  The
state and named-operation assertions are exactly the audited transition
certificate.  The receiver alternatives are established next.  Finally,
(3.5) is the definition `Omega=Z_D union T_D`, with both unions literal
and disjoint.  \(\square\)

The boundary clique bounds specialize to

\[
 \omega(H)\le
 \begin{cases}
  4,&(\nu_D,\nu_B)=(1,1),\\
  3,&\{\nu_D,\nu_B\}=\{1,2\},\\
  2,&\{\nu_D,\nu_B\}=\{1,3\}.
 \end{cases}                                             \tag{3.6}
\]

They follow from the exact-seven packet theorem and are not needed for the
certificate trichotomy.

## 4. Receiver localization in the `(1,1)` case

Retain `c_f` as a colouring of `G-f`, and put

\[
                         \gamma=c_f(d)=c_f(q).          \tag{4.1}
\]

For a colour `eta ne gamma`, let `K_eta^D` be the
`gamma-eta` component containing `d` in

\[
                         G[D\cup\Omega]-f.              \tag{4.2}
\]

### Theorem 4.1 (internal receiver lock or opposite crossing)

For every `eta ne gamma`, at least one of the following holds.

1. `q in K_eta^D`; hence the `f`-Kempe lock for `eta` is already connected
   inside the named contracted shore.
2. There is a literal `gamma-eta` path with distinct ends in `Omega`, all
   internal vertices in `B`, and with its ends respectively in
   \[
           U_eta=K_eta^D\cap\Omega
           \quad\hbox{and}\quad \Omega-U_eta.          \tag{4.3}
   \]

If neither displayed outcome occurs, the two closed shores attain one
common exact state and `G` is six-colourable.

#### Proof

First note the global compulsory lock at `f`.  In the colouring `c_f` of
`G-f`, the vertices `d,q` have the same colour.  If their
`gamma-eta` components in the full graph `G-f` were different, swapping
the component containing `d` would give them different colours and permit
restoration of `f`, six-colouring `G`.  Thus they lie in one full
`gamma-eta` component.

Suppose `q notin K_eta^D`.  Swap `gamma,eta` on `K_eta^D` in the closed
`D`-side.  This changes `d` and leaves `q` fixed, so it restores `f` and
gives an intact colouring of `G[D\cup\Omega]`.  Its boundary change from
`Pi_f` is exactly the toggle of `U_eta`.

Consider the `gamma-eta` components of the intact opposite closed shore
`G[B\cup\Omega]` under `c_f`.  If no such component meets both `U_eta`
and `Omega-U_eta`, swap every component which meets `U_eta`.  This toggles
exactly the same literal boundary set.  The two intact closed-shore
colourings then have the same exact boundary state, align, and glue to a
six-colouring of `G`.

In a counterexample some opposite component therefore meets both boundary
sets.  A shortest path in it between them has no internal boundary vertex,
so all internal vertices lie in `B`.  This is item 2.  Item 1 is the
remaining case, and the alternatives are exhaustive.  \(\square\)

When `f` was a separating first-entry edge of the second original lock,
the colouring `c_f` in this theorem may be the explicit swapped colouring
coupled to `phi`.  Hence the five receiver alternatives, the exact new
state and the old-boundary toggle coexist in one legal transition.

## 5. Exact scope

The theorem analyzes every packet vector of the tight-gate certificate:

* `(1,3)` is terminally closed;
* `(1,2)` is reoriented using a packet proved full to `Omega`, not an old
  packet, and receives a named state of demand at least three on its
  intact packet-two side; and
* `(1,1)` carries a named state of demand at least two, a literal boundary
  substitution, a one-step packet-sum drop and five receiver
  lock/crossing alternatives.

This does **not** close the tight-gate receiver demanded by the
shortest-lock programme. In the orientation where the regenerated
packet-one shore is `B`, that shore is not the strict lobe and the state
need not be related to the original fixed colouring `phi`. Even in the
other orientation, demand at least three does not place the state in the
accepted paired/attained-duty language. In `(1,1)`, packet-sum `3 -> 2`
is not a rank until later transitions are proved unable to reverse it.

The exact next theorem must spend `K_7`-minor-freeness or the universal
proper-minor response: convert the regenerated high-demand state to a
demand-at-most-two state or literal terminal, or resolve the `(1,1)`
lock/crossing system with a rank which cannot cycle.

No conclusion here applies to a boundary-excess lobe, a same-lock bypass,
or a spine-confined/rich excursion.  Those remain the geometric branches
for the crossing/web decoder.
