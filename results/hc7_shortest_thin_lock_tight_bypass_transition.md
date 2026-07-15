# Shortest thin lock: tight bypass-lobe state transition

**Status:** proved and independently audited.

This note proves the first literal transition available after anchoring the
compulsory-lock decoder at a shortest thin lock.  It does not assert that
every second lock enters a tight lobe.  It says exactly what happens when
its first off-spine entry does: the lobe is a strictly smaller actual
seven-shore, a named contraction attains an exact one-sided state there,
and a separating lock entry transports the fixed `G-zu` state by an
explicit Kempe swap.  The resulting cell is not yet a legitimate recursive
receiver: its packet orientation and attained state remain to be
normalized.

## 1. Frozen setup and the thin spine

Use the frozen atomic separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where `G` is seven-connected, strongly seven-contraction-critical and
`K_7`-minor-free, there is no `A-R` edge, `A` is connected and `S`-full,
`R` contains two disjoint adjacent `S`-full packets, and `e=zu` is the
unique `A-u` edge.  Retain the nonsingleton atomic normalization, so
`A-z` is connected and `A` is two-connected.

Fix a proper six-colouring `phi` of `G-e`, with

\[
                         \phi(z)=\phi(u)=\alpha .       \tag{1.1}
\]

Let `delta` be a thin lock colour, and choose a shortest literal
`alpha-delta` `z-u` path

\[
                         P\subseteq G[A\cup S]-e .      \tag{1.2}
\]

Put `A_P=V(P)\cap A`.  Thus `z in A_P`.  For a component `D` of
`A-A_P`, define its spine attachments and old-boundary support by

\[
             Z_D=N_A(D)\subseteq A_P,
             \qquad T_D=N_S(D)\subseteq S.             \tag{1.3}
\]

The equality in (1.3) uses that `D` is a component of `A-A_P`.

## 2. Tight off-spine lobes

### Lemma 2.1 (relative budget and strictness)

Every component `D` in (1.3) satisfies

\[
                         |Z_D|+|T_D|\ge7.               \tag{2.1}
\]

Moreover `D` is a nonempty proper subset of `A`, `Z_D` is nonempty, and
`u notin T_D`.

#### Proof

There is no `A-R` edge, and the definition of `Z_D,T_D` gives

\[
                         N_G(D)=Z_D\mathbin{\dot\cup}T_D.
\]

This neighbourhood separates the nonempty set `D` from the nonempty rich
shore, so seven-connectivity gives (2.1).  The set `A_P` contains `z`, so
`D` is proper; connectedness of `A` gives `Z_D ne emptyset`.  Finally the
only `A-u` edge is `zu`, and `z notin D`, whence `u notin T_D`.  \(\square\)

Call `D` **tight** when equality holds in (2.1), and put

\[
                         \Omega_D=Z_D\mathbin{\dot\cup}T_D. \tag{2.2}
\]

### Theorem 2.2 (named one-sided state on a tight bypass lobe)

Let `D` be tight.  Then

\[
 V(G)=D\mathbin{\dot\cup}\Omega_D\mathbin{\dot\cup}B,
 \qquad B=V(G)-(D\cup\Omega_D),                         \tag{2.3}
\]

is an actual order-seven separation with both open shores nonempty, and
the selected lobe satisfies `|D|<|A|`.

Choose any literal boundary edge `f=dq`, where `d in D` and
`q in Omega_D`, and contract `f` toward the labelled vertex `q`.  A
six-colouring of the proper minor `G/f` induces an exact partition
`Pi_f` of the seven literal vertices of `Omega_D` such that

1. `G[B\cup\Omega_D]` is coloured intact with exact state `Pi_f`; and
2. `G[D\cup\Omega_D]/f` is coloured by the same minor colouring, with
   the literal label `q` retained.

Let `nu_B` be the maximum number of pairwise disjoint
`Omega_D`-full packets in `B`, and put `H_D=G[Omega_D]`.  In a
hypothetical counterexample every such returned state satisfies

\[
                         d_{H_D}(\Pi_f)>\nu_B.          \tag{2.4}
\]

Thus the transition is not merely an unlabelled seven-cut: it has a named
minor operation, one intact `B`-side state, the same named contracted
`D`-side state, and a strict decrease `|D|<|A|`.  This is a set-size
transition certificate, not yet a recursive descent.

#### Proof

By tightness and Lemma 2.1, `Omega_D=N_G(D)` has order seven.  Hence there
is no `D-B` edge.  The set `B` contains the old rich shore `R`, so it is
nonempty.  This proves that (2.3) is an actual order-seven separation;
strictness follows from `D subsetneq A`.

Such a boundary edge exists because `Z_D` is nonempty.  Contracting `dq`
and retaining `q` preserves all seven literal labels of `Omega_D` and is
a proper minor.  Strong contraction-criticality gives a six-colouring.
The contraction lies wholly in the closed `D`-side, so restriction to
`G[B\cup\Omega_D]` is intact.  Restriction to the other side is precisely
the named contracted colouring.  Both restrictions give the same exact
literal partition `Pi_f`.

Every component of `G-Omega_D` is `Omega_D`-full.  Indeed its
neighbourhood is contained in the seven-set `Omega_D` and separates it
from a different nonempty component; seven-connectivity forces equality.
In particular `nu_B>=1`.

Suppose (2.4) failed.  Apply exact packet reflection to `Pi_f` using
`nu_B` disjoint full packets in `B`.  It gives either a literal `K_7`
model, excluded by hypothesis, or an intact colouring of
`G[D\cup\Omega_D]` with exact boundary state `Pi_f`.  Align this colouring
with the intact restriction of the `G/f` colouring on
`G[B\cup\Omega_D]`.  The open shores are anticomplete, so the two
colourings glue to a six-colouring of `G`, a contradiction.  Therefore
(2.4) holds.  \(\square\)

The exact-seven packet theorem applies to (2.3).  Consequently its packet
vector is, up to orientation, one of `(1,1)`, `(1,2)`, `(1,3)`, and

\[
 \omega(H_D)\le 6-(\nu_D+\nu_B),                       \tag{2.5}
\]

where `nu_D` is the packet number in the lobe.  These are receiving
constraints, not a claim that `Pi_f` is the old paired-triangle state.

## 3. Coupling a second compulsory lock to the transition

Fix a second colour `epsilon ne alpha,delta`, and let `K_epsilon` be the
`alpha-epsilon` component of `G-e` containing `z,u`.  Let `Q` be a
literal `z-u` path in `K_epsilon`; if `epsilon` is represented initially
by a rich quotient route, choose internal paths in every contracted thin
component to obtain this literal lift.

Suppose `Q` first enters a component `D` of `A-A_P` through a literal
boundary edge

\[
                         f=dq,\qquad d\in D,\ q\in\Omega_D. \tag{3.1}
\]

### Lemma 3.1 (first entry edge: bypass or fixed-state transfer)

Exactly one of the following two structural alternatives holds.

1. `K_epsilon-f` still contains a `z-u` path.  Thus the second lock has a
   literal bypass of the named first attachment edge `f`.
2. `f` separates `z` from `u` in `K_epsilon`.  If `X` is the component
   of `K_epsilon-f` containing `z`, swapping `alpha,epsilon` on `X`
   produces a proper six-colouring `psi` of both `G-f` and `G/f`.

In item 2 the boundary change is exact: every old literal `s in S`
is toggled if and only if `s in X`, and every other old boundary colour is
unchanged.  If `D` is tight, take `Pi_f` in Theorem 2.2 to be the
partition supplied by this particular `psi`.  On the retained old labels
`T_D subseteq S` it is related to `phi` by

\[
 \psi(s)=
 \begin{cases}
  \text{the opposite member of }\{\alpha,\epsilon\},&s in T_D\cap X,\\
  \phi(s),&s in T_D-X.
 \end{cases}                                             \tag{3.2}
\]

The new gate labels `Z_D` retain their literal vertices and their actual
colours under `psi`; no palette-to-old-label identification is imposed.

#### Proof

Because `f` lies on the chosen `z-u` path `Q`, deleting it either leaves
`z,u` connected in `K_epsilon` or separates them.  This is precisely the
displayed dichotomy.

In the second case swap the two colours on the `z`-component `X`.  All
edges except possibly `e,f` remain proper.  The vertex `z` changes colour
while `u` does not, so restoring `e=zu` is proper.  Originally the ends
of `f` had the two distinct colours; exactly one belongs to `X`, so they
have the same colour after the swap.  Hence `psi` colours `G-f` and
descends to `G/f`.  Its boundary toggle is exactly `X\cap S`, proving
(3.2).

If `D` is tight, `f` is an allowed named contraction in Theorem 2.2.
It lies in the lobe closed side, so the restrictions of this particular
minor colouring are exactly the two restrictions asserted there.  The
literal description of the retained old and gate labels is immediate.
\(\square\)

### Corollary 3.2 (the exact residual after the first bypass test)

For every second lock path `Q`, one of the following occurs at the first
off-spine component it visits and its first boundary edge into that
component:

1. a tight component gives the smaller actual seven-cell and named
   one-sided contracted state of Theorem 2.2; if its entrance edge is
   separating in the lock, the state is coupled to the fixed colouring
   `phi` by Lemma 3.1;
2. the entrance edge has a literal same-lock bypass; or
3. the entered component has strict boundary excess
   \[
                    |Z_D|+|T_D|\ge8.                  \tag{3.3}
   \]

If a second lock never visits an off-spine component, then it is confined,
on the thin side, to `A_P\cup S`; rich excursions may still occur through
`R`.  Boundary excess, a same-lock bypass, and spine-confined/rich
excursion are the precise unresolved geometric branches.  In the tight
case the additional unresolved issue is the receiver: neither quotient
edge-disjointness nor shortestness of `P` determines the packet orientation
or the returned state.

## 4. Scope

This theorem isolates an infinite **tight first-entry** family by a strict
set-size transition carrying a named one-sided state; it is not finite
shore-order casework.  It also records the strongest legal fixed-state
conclusion from a separating thin-lock entry.

It does **not** close that family.  To turn the certificate into a valid
receiver one must additionally prove at least one of the following:

1. `D` is the packet-one shore, the opposite shore has at least two full
   packets, and the attained state is an accepted `S3` state;
2. the new cell has a normalized ranked `(1,1)` `S4` handoff; or
3. the packet vector is `(1,3)`, where the audited closure applies.

None of these follows merely from `|D|<|A|` or from Theorem 2.2.

It does not prove that an arbitrary rich quotient route enters an
off-spine component of `A`, that a used component is tight, or that a
nonseparating bypass is vertex-disjoint from `P`.  In particular a common
`alpha` articulation on `P`, with every off-spine component satisfying
(3.3), survives.  A complete decoder must now spend either at least one
unit of boundary excess in (3.3), or the ordered bridge geometry of the
spine-confined/rich excursion, to obtain adjacent duty carriers or a
stateful web seam.

The shortestness of `P` is not used in the transition proof itself; the
statement remains valid for any literal thin lock path.  Shortestness is
retained because it is needed by the surrounding decoder.
