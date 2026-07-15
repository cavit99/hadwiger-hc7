# Independent audit: shortest thin-lock tight-lobe transition

**Verdict:** GREEN.

**Audited theorem hash:**
`d74224f2d8bff549e65e38cab1fa8083814e3277a4dfe6f6c86d22c24724f8e0`.

## 1. Scope of the audit

The audit checked the separation, retained-label contraction, packet
reflection, Kempe toggle, coverage of all first lobe entries, and the exact
scope of the conclusion in
`hc7_shortest_thin_lock_tight_bypass_transition.md`.

The first draft was RED for two reasons:

1. it considered only entries through a spine attachment, omitting a path
   entering a lobe from an old boundary vertex; and
2. it called the smaller seven-cell a recursive descent without proving a
   packet orientation or an accepted receiving state.

The final theorem repairs both defects.  It permits any boundary edge
`dq` with `q in Omega_D` and calls the conclusion only a strict set-size
transition certificate carrying a named one-sided state.

## 2. Separation and budget

For a component `D` of `A-A_P`, its full host neighbourhood is exactly

\[
 N_G(D)=Z_D\mathbin{\dot\cup}T_D.
\]

This set separates nonempty `D` from the nonempty rich shore.  Hence
seven-connectivity gives `|Z_D|+|T_D|>=7`.  Connectedness of `A` gives
`Z_D` nonempty, and the uniqueness of `zu` gives `u notin T_D`.

At equality, `Omega_D=N_G(D)` is a literal order-seven separator.  The
opposite open side contains the old rich shore, so both open sides are
nonempty and anticomplete.  Every component of `G-Omega_D` is
`Omega_D`-full: its neighbourhood lies in a seven-set and separates it
from another nonempty component, so seven-connectivity forces equality.

## 3. Named contraction and demand inequality

For any literal boundary edge `f=dq`, contracting toward the boundary
endpoint `q` preserves all seven literal `Omega_D` labels.  The operation
is proper.  A six-colouring of `G/f` restricts intact to the opposite
closed shore and gives the same exact partition on the named contracted
lobe side.

If that partition had packet demand at most the opposite packet capacity,
exact packet reflection on the opposite side would give either a literal
`K_7` or an intact lobe-side colouring with the same exact partition.  In
the latter case it aligns with the intact opposite-side restriction and
the two colourings glue.  Both alternatives contradict the frozen
counterexample.  Therefore the strict demand inequality in the theorem is
valid.  No adjacency among the reflecting packets is used.

## 4. First-entry Kempe transfer

Let a second compulsory lock first enter `D` through `f=dq`.  Since
`N_G(D)=Omega_D`, every first visit has exactly this form, including an
entry from an old boundary vertex in `T_D`.

If `f` is not separating in the bichromatic lock, deleting it leaves a
literal same-lock bypass.  If it is separating, swap the two colours on
the component containing `z`.  The vertex `z` changes colour while `u`
does not, so `zu` can be restored.  Exactly one endpoint of `f` swaps, so
the endpoints become equal and the colouring descends to `G/f`.  The old
boundary toggle is exactly the intersection of that component with `S`.
For a tight lobe, choosing the partition induced by this particular
colouring couples the named lobe state to the fixed original colouring.

## 5. Exact conclusion

The theorem proves a smaller actual seven-cell with a named one-sided
contracted state, and in the separating-entry branch an explicit
fixed-state transition.  It does **not** prove:

- that the lobe is the packet-one shore;
- that the opposite shore contains two full packets;
- that the returned state is an accepted paired `S3` state; or
- that a `(1,1)` cell has a ranked `S4` receiver.

The theorem and README now state these as the next receiver obligation.
No mathematical defect remains in the promoted local result.
