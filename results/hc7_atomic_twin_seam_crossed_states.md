# Atomic twin-seam crossed states

**Status:** proved and independently audited.

## 1. Setup

Use outcome 2 of the
[literal two-gate normal form](hc7_atomic_literal_two_gate_transition.md).
Thus `A-Z` has components `D,E`, where `Z={p,q}`, `z in E`, and

\[
 |T_D|=|T_E|=5,
 \qquad T_D\cup T_E=S,
 \qquad |T_D\cap T_E|=3,
\]

with `T_D=N_S(D)`, `T_E=N_S(E)`, and

\[
 \Omega_D=Z\mathbin{\dot\cup}T_D=N_G(D),
 \qquad
 \Omega_E=Z\mathbin{\dot\cup}T_E=N_G(E).              \tag{1.1}
\]

Put

\[
 I=T_D\cap T_E,\quad
 A_0=T_D-T_E,\quad
 B_0=T_E-T_D,\quad
 K=Z\cup I.                                            \tag{1.2}
\]

Then

\[
 |K|=5,qquad
 \Omega_D=K\mathbin{\dot\cup}A_0,qquad
 \Omega_E=K\mathbin{\dot\cup}B_0,                    \tag{1.3}
\]

where `|A_0|=|B_0|=2` and `u in B_0`.  Let

\[
 B_D=V(G)-(D\cup\Omega_D),qquad
 B_E=V(G)-(E\cup\Omega_E).                             \tag{1.4}
\]

For a boundary `Omega` and an open shore `X`, write
`nu_X^Omega` for the maximum number of pairwise disjoint connected
`Omega`-full packets in `X`.  Superscripts are suppressed below because
the boundary is determined by the subscript `D` or `E`.

Put `e=zu`.  Fix a six-colouring `phi` of `G/e`, expanded to a colouring
of `G-e` by giving `z,u` the same colour.  For an edge

\[
                         f=dt,qquad d\in D, t\in Z,   \tag{1.5}
\]

let `c_f` be any six-colouring of `G/f`, with the contracted image named
by the literal gate `t`.  Expand it to a colouring of `G-f` by giving `d`
the colour of `t`.

Let

\[
 \Pi_D^\phi,\Pi_E^\phi,\Pi_D^f,\Pi_E^f               \tag{1.6}
\]

be the exact equality partitions induced by the indicated colouring on
`Omega_D` or `Omega_E`, respectively.  Put
`H_D=G[Omega_D]` and `H_E=G[Omega_E]`.

## 2. Crossed-state theorem

### Theorem 2.1

For every edge `f` in (1.5) and every six-colouring `c_f` of `G/f`,

\[
             \Pi_D^\phi\ne\Pi_D^f,
             \qquad
             \Pi_E^\phi\ne\Pi_E^f.                   \tag{2.1}
\]

Moreover,

\[
 d_{H_D}(\Pi_D^\phi)>\nu_D,
 \qquad
 d_{H_D}(\Pi_D^f)>\nu_{B_D},                          \tag{2.2}
\]

and

\[
 d_{H_E}(\Pi_E^\phi)>\nu_{B_E},
 \qquad
 d_{H_E}(\Pi_E^f)>\nu_E.                              \tag{2.3}
\]

Here every packet number is taken relative to the boundary occurring in
the same formula.

### Proof

The colouring `phi` is proper on `G[D union Omega_D]`: both endpoints
`z,u` of its deleted edge lie outside that closed side.  It is also proper
on `G[B_E union Omega_E]`, because that closed side excludes `z`.

The expanded colouring `c_f` is proper on
`G[B_D union Omega_D]` and on `G[E union Omega_E]`, because both closed
sides exclude `d`.  Contracting `f` may add edges incident with `t`; this
does not make either closed side graph-isomorphic to its image in `G/f`,
but the restrictions remain proper colourings of the original subgraphs.

If `Pi_D^phi=Pi_D^f`, permute the six colours of `c_f` so that the two
boundary colourings agree block by block.  Glue `phi` on
`D union Omega_D` to `c_f` on `B_D union Omega_D`.  Formula (1.1) says
there is no edge between the two open shores, and the edge `zu` lies on
the `c_f` side.  The result is a six-colouring of `G`, a contradiction.

If `Pi_E^phi=Pi_E^f`, perform the same palette alignment and glue `phi`
on `B_E union Omega_E` to `c_f` on `E union Omega_E`.  Again `zu` lies
on the `c_f` side.  This gives the same contradiction and proves (2.1).

For (2.2), suppose first that
`d_HD(Pi_D^phi)<=nu_D`.  Exact packet reflection with packets in `D`
manufactures either a literal `K_7` or a colouring of the opposite closed
shore with exact boundary state `Pi_D^phi`.  The first outcome contradicts
the kernel and the second glues to `phi` on the `D`-closed side.  Thus the
first inequality is strict.  The same argument applied to `c_f`, whose
colour-intact closed side is `B_D`, gives the second inequality in (2.2).

On `Omega_E`, the colour-intact side of `phi` is `B_E` and that of `c_f`
is `E`.  Exact reflection in those same open shores gives (2.3).  Notice
that the packets are always taken from the shore already carrying the
colour-intact restriction: their contraction constructs the matching
colouring on the opposite closed shore.  \(\square\)

## 3. Packet-aligned handoff

### Corollary 3.1 (packet-aligned named handoff)

For each of the two twin boundaries, its actual packet-one shore selects a
named operation from `{e,f}` whose returned state has demand strictly larger
than the packet number of the opposite shore.

More explicitly, at `Omega_D`:

* if `D` is the packet-one shore, use the boundary-edge contraction `f`
  and the state `Pi_D^f`, whose demand exceeds `nu_B_D`;
* if `B_D` is the packet-one shore, use the internal contraction `e` and
  the state `Pi_D^phi`, whose demand exceeds `nu_D`.

At `Omega_E`:

* if `E` is the packet-one shore, use the boundary-edge contraction `e`
  and the state `Pi_E^phi`, whose demand exceeds `nu_B_E`;
* if `B_E` is the packet-one shore, use the boundary-edge contraction `f`
  and the state `Pi_E^f`, whose demand exceeds `nu_E`.

Thus a `(1,3)` orientation is terminal by adaptive reflection; a `(1,2)`
orientation has a named returned state of demand at least three, intact on
the packet-two closed shore; and a `(1,1)` orientation has a named state of
demand at least two.  Every boundary label is retained literally.

### Proof

The four choices are exactly the four colour-intact restrictions used in
the proof of Theorem 2.1.  In each case the chosen operation lies in the
closed packet-one side, while its colouring is proper on the opposite
closed side.  The relevant strict inequality is therefore the corresponding
one of (2.2)--(2.3).  The packet-vector consequences are immediate.  \(\square\)

## 4. Exact scope

The theorem couples one fixed `G/e` colouring to **every** response to a
literal `D`-gate contraction, simultaneously on two overlapping actual
seven-boundaries.  It is stronger than a naked receiver certificate.

It is not yet state localization.  The restrictions of `phi` and `c_f`
to the common five-set `K` may induce different partitions.  Consequently
(2.1) does not say that the change occurs in `A_0` or `B_0`, and (2.2)--
(2.3) do not by themselves produce a common state, a rooted model, or an
accepted recursive handoff.  Corollary 3.1 normalizes the local operation,
orientation and demand, but supplies no globally noncycling rank.  The
missing operation is a literal
`K`-alignment or a proof that failure of such alignment yields the terminal
model/handoff.
