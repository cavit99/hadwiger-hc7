# Tight-gate local orientation shell

**Status:** explicit barrier to local packet-orientation and state-shape
claims. It is not an `HC_7` counterexample.

## Construction

Let

\[
 \Omega=\{0,1,\ldots,6\},\qquad
 H=G[\Omega]=\overline{C_7}.
\]

Take `D={d_1,d_2}` with edge `d_1d_2`, make both `d_i` complete to
`Omega`, take `B={b}` complete to `Omega`, and put no edge between `D`
and `B`. Then

\[
                 V(G)=D\mathbin{\dot\cup}\Omega
                        \mathbin{\dot\cup}B
\]

is an actual order-seven separation. The graph is seven-connected and
has packet vector

\[
                         (\nu_D,\nu_B)=(2,1).
\]

Contract `f=d_1 0` toward the literal boundary label `0`. The following
is a proper six-colouring of `G/f`:

\[
 \{d_1,0\},\quad \{1,2\},\quad \{3,4\},\quad
 \{5\},\quad \{6\},\quad \{d_2,b\}.
\]

Its exact boundary partition is

\[
 \Pi=\{\{0\},\{1,2\},\{3,4\},\{5\},\{6\}\}.
\]

The singleton set is `{0,5,6}` and has clique number two in
`overline(C_7)`, so

\[
                         d_H(\Pi)=5-2=3>\nu_B.
\]

Thus a tight actual seven-cell, a named boundary contraction, high demand
and seven-connectivity do not imply that the marked lobe is packet-one or
that the returned state is paired.

## Separating-entry extension

The same failure can be embedded in the fixed-state Kempe transition.
Add vertices `h,u` to `B`, keep `b` boundary-full, make `bhu` a triangle,
put `q=0,z=6,r=5`, join `h` to `Omega-{z,r}` and `u` to
`Omega-{q,r}`, and take `e=zu`, `f=d_1q`. Extending the displayed
colouring by `h=5,u=1`, then swapping colours `1,5` on `{z,d_1}`, gives
a colouring of `G-e` whose `1-5` lock is

\[
                         z-d_1-f-q-h-u.
\]

The edge `f` is a separating first entry. Swapping back restores `e`,
equalizes `f`, and yields the same colouring of `G/f`. Hence even the
audited separating-entry toggle does not orient the packet vector or
normalize the state.

## Trust boundary

The ten-vertex shell is six-colourable and contains a literal `K_7`
minor, for example with bags

\[
 \{0,3\},\{d_2\},\{2,4\},\{1\},\{5\},\{b,6\},\{d_1\}.
\]

Therefore it does not refute a theorem using `K_7`-minor-freeness or the
full universal proper-minor response of a hypothetical counterexample.
It proves that those hypotheses must be used explicitly; local packet
bookkeeping, high demand and one named Kempe toggle are insufficient.
