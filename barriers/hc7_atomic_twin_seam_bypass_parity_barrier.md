# Barrier: a nonseparating lock has no two-colour contraction exchange

**Status:** proved elementary obstruction, with an executable literal
twin-shell certificate.  This does not falsify the terminal-disjunctive
double-lock theorem.  It rules out the most direct proposed mechanism for
its complementary bypass branch.

## 1. Exact obstruction

Let `e=zu` and `f=dt` be disjoint edges.  Let `phi` be a proper colouring
of `G-e` with

\[
                         \phi(z)=\phi(u)=\alpha,
\]

and suppose `f` lies in the `alpha,beta` lock containing `z,u`.  Put

\[
 H=G-\{e,f\},\qquad
 L=H[\phi^{-1}(\{\alpha,\beta\})].
\]

Assume that deleting `f` does not separate `z` from `u`; equivalently,
`z,u` lie in one component of `L`.  Then no sequence of Kempe exchanges
confined to the colours `alpha,beta` in `H` can produce a colouring which
simultaneously

1. restores the edge `e`, and
2. identifies the ends of `f` and hence descends to `G/f`.

Indeed, any sequence of exchanges on the `alpha,beta` components of `H`
has the same net effect as swapping a union of those components.  Since
`z,u` lie in one component, they are either both swapped or both left
fixed.  They therefore retain equal colours.  Restoring `e` is impossible,
regardless of what happens at `d,t`.  A global palette permutation also
preserves this equality and does not alter the conclusion.  \(\square\)

This is the exact opposite of the separating bridge square.  In that
branch a bridge side contains precisely one of `z,u` and precisely one of
`d,t`, so one two-colour swap couples the two named operations.  In the
bypass branch, the same component relation is an invariant forbidding that
coupling.

## 2. Literal crossed-response shell

The adjacent verifier
[`../active/hc7_atomic_twin_seam_bypass_parity_probe.py`](../active/hc7_atomic_twin_seam_bypass_parity_probe.py)
realizes the obstruction with the full literal twin notation.

Use

\[
 Z=\{t,q\},\quad D=\{d,d_1\},\quad E=\{z,e_1\},
\]

\[
 I=\{i_1,i_2,i_3\},\quad A_0=\{a_1,a_2\},
 \quad B_0=\{u,b\}.
\]

The lobe supports are exactly

\[
 T_D=I\mathbin{\dot\cup}A_0,
 \qquad T_E=I\mathbin{\dot\cup}B_0,
\]

the gates have old-boundary contacts only in `I`, and `zu` is the unique
edge from the displayed thin graph to `u`.  The old seven-boundary is a
connected bipartite tree.  Two adjacent singleton vertices are both full
to it.

One six-colouring `phi` of `G-e` has the literal paths

```text
z-t-d-a1-u       through f=td,
z-b-u            avoiding f.
```

All their vertices use the two colours `0,1`; hence the response-matched
lock contains `e`'s two ends and `f`, while `L-f` still connects all four
named ends.  A second six-colouring `psi` of `G-f` satisfies

\[
                   \psi(d)=\psi(t),\qquad
                   \psi(z)\ne\psi(u),
\]

and therefore descends to `G/f`.  Nevertheless its exact partitions
differ from those of `phi` on both

\[
                 \Omega_D=Z\cup I\cup A_0,
       \qquad    \Omega_E=Z\cup I\cup B_0.
\]

Thus the bypass and a crossed response genuinely coexist, while the
response cannot be generated from the displayed lock by any two-colour
component exchange.

The certificate intentionally has connectivity four and contains a
literal `K_7` minor after the two full packets are added.  It is therefore
closed by the allowed terminal outcome and is not a counterexample to any
full-kernel statement.  Its role is narrower: it proves that the bypass
branch cannot imitate the separating bridge swap, even when all literal
twin labels and both crossed states are present.

## 3. Consequence for the active theorem

The following prospective sublemma is false:

> A response-matched `f`-bypass in the `e`-lock can be converted, by
> exchanges within that lock, into a boundary-state transition between
> the `e`- and `f`-contraction responses.

The nonseparable decoder must instead use information outside the selected
two-colour component.  Under the currently audited spine, the only precise
possibilities are:

1. couple an independently chosen `G/f` response to the rooted
   `K_4(z,u,d,t)` in `G-{e,f}` and attach an exclusive literal duty;
2. use a third-colour or internal-edge response to reproduce one exact
   state on complementary closed sides;
3. exhibit the literal `K_7` or fixed pair; or
4. return an actual member of the globally ranked family `F_12(G)` whose
   open packet-one shore is strictly smaller.

An `(1,1)` twin, an arbitrary near model, or a receiver ranked only after
it is produced remains invalid.  In particular, the bypass itself supplies
no strict `S1/S4` handoff.

### 3.1 A stronger positive common-host substrate

There is one uniform replacement for the failed two-colour exchange.  In
the full counterexample kernel put

\[
                              H=G-\{e,f\}.
\]

Then `chi(H)>=5`.  Indeed, from a colouring of `H` with at most four
colours, recolour one endpoint of `e` with a fifth fresh colour and one
endpoint of the vertex-disjoint edge `f` with a sixth fresh colour.  Both
deleted edges and every incident edge are then proper, giving a
six-colouring of `G`.

Consequently the
[Dominating 4-Colour Theorem](https://arxiv.org/abs/2605.10112)
supplies a dominating `K_5` model directly in the **common deletion**
`H`.  It may be normalized as

\[
                    (T_1,T_2,T_3,\{v\},\{w\}),
\]

where `T_3` is a path and the last three parts induce a cycle.  This
strictly strengthens the previously used common-host rooted `K_4` as an
unlabelled allocation substrate: it gives five ordered pairwise adjacent
bags in the graph where both named responses live.

It is not yet the decoder.  The five bags may consume both old packets and
both lobes, and they need not all meet the literal old boundary.  Thus the
two full packets cannot simply be appended.  The exact positive bypass
problem can now be narrowed to a state-labelled pullback of this dominating
five-bag model: make all five bags duty-bearing without consuming the two
packet reserves, reproduce a complementary-side exact state, or read a
fixed pair from the normalized terminal cycle.  This is a graph-global
allocation problem rather than another two-colour swap.

## 4. Verification

Run

```text
PYTHONPATH=active/runtime/deps python3 \
  active/hc7_atomic_twin_seam_bypass_parity_probe.py
```

The script checks both proper-minor colourings, the nonseparating lock,
the exact lobe supports and unique portal, the connected bipartite old
boundary, both full packets, mismatch of both exact twin states, and the
declared terminal `K_7` minor.
