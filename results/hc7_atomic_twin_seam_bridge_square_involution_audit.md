# Independent audit: twin-seam bridge-square involution

**Verdict:** the cited inputs are individually GREEN, but they do not yet
prove either decoder in the active double-lock target.  The separating
bridge response has an additional exact symmetry: its reverse lock forms
an involutive four-state square.  In the counterexample-derived twin seam
that entire square is crossed on both boundaries.  Consequently a second
side swap cannot itself be the missing state convergence or a strict
ranked move.

This note proves that square and identifies the one composition statement
which is still absent.  It does not assert that the double-lock theorem is
false.

**Audited source:**
`results/hc7_atomic_twin_seam_bridge_square_involution.md`.

**Source SHA-256:**
`f3da93603f86c5207b74463097e2f7bd305a400bc200869e25b9d4ca239a785a`.

## 1. Requirements of the active theorem

The target has three acceptable outputs.

1. **Common state.**  The two intact closed sides must induce the same
   literal equality partition on one actual seven-boundary.  Equality only
   on the common five-set, or equality between two colourings intact on the
   same side, is insufficient.
2. **Terminal.**  The proof must display seven literal branch sets, or a
   fixed pair `P` for which `G-P` is `K_5`-minor-free.  The latter is a
   genuine terminal because known `HC_5` four-colours `G-P`, and two fresh
   colours on `P` six-colour `G`.
3. **Strict handoff.**  The output must specify an actual receiver, its
   literal boundary map, exact packet vector, attained state, intact
   opposite side, and a previously defined well-founded rank which strictly
   decreases.  A naked `(1,1)` receiver, a one-/two-hole model, or an actual
   separator is not such an output.

The two constructive branches additionally require:

* in the separating case, allocation of the response bundle to literal
  old-boundary or regenerated-model duties; and
* in the bypass case, promotion of the rooted four-pole core from three
  forced boundary incidences to the fourth incidence or exact state needed
  for closure.

## 2. Exact bridge-response square

### Lemma 2.1 (complementary bridge swaps form a square)

Let `e=zu` and `f=dt` be vertex-disjoint edges of a graph `G`.  Let `phi`
be a proper colouring of `G-e` with

\[
                         \phi(z)=\phi(u)=\alpha .
\]

For `beta ne alpha`, let `K` be the `alpha,beta` component of `G-e`
containing `z,u`.  Suppose `f` is a bridge of `K` separating `z` from
`u`.  Write

\[
                         K-f=X\mathbin{\dot\cup}Y,
                \qquad z\in X,\quad u\in Y,
\]

where `X,Y` denote the vertex sets of the two components.  For a set `U`
of `alpha,beta` vertices, write `phi^U` for the colouring obtained by
interchanging `alpha,beta` on `U`.

Then:

1. `phi^X` and `phi^Y` are proper colourings of `G-f`; the ends of `f`
   have equal colours, so both descend to `G/f`.
2. `phi` and `phi^K` are proper colourings of `G-e`; the ends of `e`
   have equal colours, so both descend to `G/e`.
3. In either of the two `G-f` colourings, the `alpha,beta` component
   containing the four named vertices is exactly

   \[
                              (K-f)+e,                 \tag{2.1}
   \]

   and `e` is a bridge whose two sides are `X,Y`.
4. The legal bridge swaps form the four-cycle

   \[
   \begin{array}{ccc}
       \phi & \longleftrightarrow & \phi^X\\
       \updownarrow && \updownarrow\\
       \phi^Y & \longleftrightarrow & \phi^K,
   \end{array}                                        \tag{2.2}
   \]

   where the opposite pair `phi,phi^K` consists of the two `G/e`
   responses, and the other opposite pair `phi^X,phi^Y` consists of the
   two `G/f` responses.  Every displayed move is its own inverse.

### Proof

The bridge `f` is the only `alpha,beta` edge between `X` and `Y` in
`G-e`.  Exactly one endpoint of `f` lies in each side.  Swapping either
side therefore makes the ends of `f` equal.  It also changes exactly one
of `z,u`, making `e` proper.  No other edge becomes monochromatic: an
`alpha,beta` edge leaving one side would contradict the definition of the
component or the bridge, while an edge to a vertex of another colour
remains proper.  This proves item 1.

Swapping the whole Kempe component `K` is an ordinary Kempe exchange in
`G-e`.  Both `z,u` are swapped and remain equal.  This proves item 2.

All four colourings have the same set of `alpha,beta` vertices.  Passing
from `G-e` to `G-f` deletes the sole edge `f` between `X,Y` and restores
`e`, whose ends lie one in each side.  No other `alpha,beta` component can
join this one.  Hence (2.1) is the whole component, and `e` is its bridge.

Finally, symmetric difference of swap sets gives

\[
 (\phi^X)^X=\phi,
 \qquad (\phi^X)^Y=\phi^K,
 \qquad (\phi^Y)^Y=\phi,
 \qquad (\phi^Y)^X=\phi^K.
\]

The same identities read in the opposite direction are the two legal
`f`-bridge swaps from the `G/e` responses.  This proves (2.2).  \(\square\)

### Corollary 2.2 (the twin square is fully crossed)

In the frozen twin seam, let `Pi_Omega(c)` be the exact partition induced
by a colouring `c` on either `Omega=Omega_D` or `Omega_E`.  For each

\[
 a\in\{\phi,\phi^K\},
 \qquad b\in\{\phi^X,\phi^Y\},
\]

one has

\[
                         \Pi_\Omega(a)\ne\Pi_\Omega(b). \tag{2.3}
\]

### Proof

Both members of the first set descend to `G/e`, and both members of the
second set descend to `G/f` with the literal gate label retained.  Apply
the audited crossed-state theorem first with `phi` and then with `phi^K`;
that theorem quantifies over every colouring of `G/f` and over either twin
boundary.  This gives all eight inequalities in (2.3).  \(\square\)

### Consequence

The response-matched reverse `e`-lock in the separating branch is not an
independent descent mechanism.  It returns either the original `G/e`
state or its whole-component Kempe mate, and every cross-minor comparison
inside the square remains mismatched on both twins.  Moreover no scalar
rank can strictly decrease under all four legal side swaps, because every
move is reversible.

A proof can still orient one move using data external to the square.  It
must use, for example, a third palette response, a literal boundary duty,
a labelled row split, or an actual globally ranked `(1,2)` separation.

## 3. What the current inputs do and do not compose

| Input | Exact proved contribution | Missing composition |
|---|---|---|
| Crossed exact states | Every `G/e`--`G/f` comparison mismatches on both twins; four packet-demand inequalities | No localization to the exclusive labels or common state |
| Packet transfer | Unless terminal `(1,3)` or strict lobe-oriented `(1,2)`, both twin vectors are `(1,1)` | No rank for the remaining `(1,1)` cell |
| Global thin-shore minimum | Excludes a smaller actual oriented `(1,2)` packet-one shore when the source was chosen globally | Does not rank `(1,1)`, near-model rotations, or an arbitrary separator; its upstream applicability must be preserved |
| Separating response bundle | One literal cycle through `e,f`; four further bypasses; rank-two layers or one palette gate with four mixed escapes; double-contraction saturation | No boundary-duty or model-row labels on those paths |
| Two-named-edge rooted `K_4` | A literal rooted core at `z,u,d,t`; at least three bags meet `Omega_E` | No fourth incidence and no disjoint reserve for the old packets/lobes |
| Compulsory-edge regeneration | A spanning `K_6` model avoiding `z,u`; exact contact thresholds | The two first hits may lie in one row and palette colours do not name rows |
| Two-pole trichotomy | Contact six closes; contact five/four gives one-/two-hole models; a same-row split gives `K_7` or an actual separator | Contact five/four is unranked; the residual row-duty lock is exactly the missing decoder |

Thus no pair of existing theorems silently closes the target.  The rooted
`K_4` may consume both old packets and both lobes, while the regenerated
`K_6` is chosen independently.  There is no proved disjointness or
label-preserving map between their bags.  The response paths likewise may
cross every region and concentrate in one regenerated row.

## 4. Exact missing implication

The most economical new statement is not another path-existence theorem.
It is the following allocation/confluence lemma.

> **State-labelled allocation lemma (missing).**  In the simultaneous
> `(1,1)/(1,1)` twin seam, one response outside the involutive bridge
> square, together with either the separating bundle or the rooted
> four-pole core, must do one of the following:
>
> 1. attach a literal exclusive boundary duty to a carrier disjoint from
>    the other required bags;
> 2. split a multiply hit regenerated row while retaining all five foreign
>    duties;
> 3. reproduce one exact state on complementary closed sides; or
> 4. produce an actual oriented `(1,2)` receiver with a strictly smaller
>    packet-one shore (or another explicitly defined quotient rank).

Items 1--2 give the literal terminal model, item 3 gives the common-state
colouring, and item 4 is the only currently available noncycling exact-
seven descent.  Merely swapping the reverse bridge, maximizing numerical
row contact, or naming a new `(1,1)` receiver cannot establish this lemma.

## 5. Audit conclusion

The active double-lock theorem is still a genuine theorem-strength gap.
Its separating branch cannot be completed by the two response-matched
bridge swaps alone: Lemma 2.1 proves that they are an exact involution, and
Corollary 2.2 proves that the resulting square is fully crossed.  The
nonseparating branch has a literal rooted `K_4`, but no current theorem
promotes its forced three-boundary incidence to the fourth labelled duty.

Accordingly the next proof attempt should target the state-labelled
allocation lemma above.  Any claimed strict `S1/S4` output must instantiate
its rank explicitly; otherwise the completion claim is not auditable.
