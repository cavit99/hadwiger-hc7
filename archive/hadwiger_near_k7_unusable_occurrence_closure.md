# Static closure of an unusable dark-lobe occurrence

## 1. Outcome

This note removes the second of the two residues left by Corollary 9.3
of `hadwiger_near_k7_active_root_face_exchange.md`.

Let the six literal singleton labels contain

\[
        J=K_6-\{ab,ac\}.
\]

Let `D_0,D_1,D_2,D_3` be four distinct dark off-torso lobes in the
one-complex shell.  For each `i`, its actual torso attachment set

\[
                         P_i=N_W(D_i)
\]

has order two, and `D_i` sees every vertex of `J` except possibly its
one named missed row.  Suppose the portal family has rank four.  Then
**every named incidence** `x in P_i` occurs in an SDR with `D_i`
assigned to `x`, unless `G` already contains a `K_7` minor.

Thus an attachment occurrence which belongs to no role-respecting full
SDR is not a live near-`K_7` counterarchitecture.  The proof is static;
it uses neither a virtual torso edge nor a proper-minor colour state.

## 2. The incidence Hall witness

### Lemma 2.1 (a forbidden incidence has one of two forms)

Let `P_0,P_1,P_2,P_3` be two-element sets with an SDR.  Fix
`x in P_0`.  If no SDR assigns `x` to `P_0`, then, after renumbering
`P_1,P_2,P_3`, one of the following holds.

1. `P_1=P_2={x,y}` for some `y ne x`.
2. For three distinct elements `x,y,z`, the multiset
   `(P_1,P_2,P_3)` is either
   \[
                  (xy,xz,yz)                                      \tag{2.1}
   \]
   or
   \[
                  (xy,yz,yz),                                     \tag{2.2}
   \]
   up to interchanging `y,z`.

Here `uv` abbreviates the set `{u,v}`.

#### Proof

Force `P_0` to use `x`, delete `x`, and apply Hall's theorem to the
remaining three sets.  Choose an inclusion-minimal nonempty witness
`I subseteq {1,2,3}`.  Put

\[
       U=\bigcup_{i\in I}P_i,
       \qquad
       U'=\bigcup_{i\in I}(P_i-\{x\}).
\]

The forced system fails, so `|U'|<=|I|-1`.  The original four-set
family has an SDR, and hence its subfamily indexed by `I` has an SDR;
therefore `|U|>=|I|`.  Since `U subseteq U' union {x}`, equality holds:

\[
                       |U|=|I|,
       \qquad          |U'|=|I|-1,
       \qquad          x\in U.                                  \tag{2.3}
\]

A one-set witness is impossible because a two-element set remains
nonempty after deleting `x`.  Hence `|I|` is two or three.

If `|I|=2`, equation (2.3) says that two two-element sets have union of
order two containing `x`; they are both `{x,y}`.  This is outcome 1.

Suppose `|I|=3`.  Then `U={x,y,z}` and `U'={y,z}`.  The only possible
two-element sets are `xy,xz,yz`.  Minimality of `I` forbids two copies
of `xy`, because after deleting `x` those two sets would have union
`{y}`; similarly it forbids two copies of `xz`.  If all three types
occur we obtain (2.1).  Otherwise the only repeated type is `yz`, and
the third set is `xy` or `xz`, which is (2.2) after interchanging
`y,z`.  QED.

## 3. Every witness contains three almost-complete clique bags

We use Lemma 2.2 of
`hadwiger_near_k7_bouquet_static_closure.md`: three disjoint connected,
pairwise adjacent sets which each see all six literal labels except
possibly one marked label, together with `J`, contain a `K_7` minor.

### Theorem 3.1 (unusable-occurrence closure)

In the setting of Section 1, if an incidence `x in P_0` is not used by
any full role-respecting SDR, then `G` contains a `K_7` minor.

#### Proof

Apply Lemma 2.1.

In outcome 1, write `P_1=P_2={x,y}` and take

\[
       H_0=D_0\cup\{x\},
       \qquad H_1=D_1\cup\{y\},
       \qquad H_2=D_2.                                           \tag{3.1}
\]

The three sets are connected and disjoint.  They are pairwise adjacent:
`H_0H_1` and `H_0H_2` use the actual attachment edges from `x` to
`D_1,D_2`, while `H_1H_2` uses the actual attachment edge from `y` to
`D_2`.

For (2.1), denote the corresponding lobes by
`D_{xy},D_{xz},D_{yz}` and take

\[
       H_x=D_{xy}\cup\{x\},
       \qquad H_z=D_{xz}\cup\{z\},
       \qquad H_y=D_{yz}\cup\{y\}.                              \tag{3.2}
\]

The three cross-adjacencies use, respectively, the unused endpoint of
each of the portal pairs `xy,xz,yz`.

For (2.2), with lobes `D_{xy},D_{yz},D'_{yz}`, take

\[
       H_y=D_{xy}\cup\{y\},
       \qquad H_z=D_{yz}\cup\{z\},
       \qquad H'=D'_{yz}.                                        \tag{3.3}
\]

Here `H_yH_z` and `H_yH'` use the `y`-attachments of the two `yz`
lobes, and `H_zH'` uses the `z`-attachment of `D'_{yz}`.

In every case the displayed three bags contain three different lobes.
Consequently they are disjoint, and each sees every literal singleton
of `J` except possibly the one row missed by its own lobe.  The
three-lobe triangle completion now gives a literal `K_7` model.  QED.

### Corollary 3.2 (both poles occur as active-face roots)

In a `K_7`-minor-free one-complex shell, let four distinct fixed dark
lobes supply the four private extension roles.  Then every actual pole
incidence of every one of the four lobes belongs to a full
role-respecting SDR.  Hence the fixed-extension facial-coherence theorem
places both actual attachment **vertices** of every selected lobe on its
one active face.

This conclusion concerns actual torso vertices and the combinatorial
incidences of actual lobe--torso edges.  It does not prescribe the side
of the face on which such an edge is embedded, does not turn a virtual
torso edge into a literal edge, and does not assert that the interior of
a nonrural lobe can be drawn in the face.  Those embedding issues belong
to the remaining shared-lobe collision, not to SDR occurrence coverage.

## 4. Remaining residue

Together with the Hall-bouquet closure, Theorem 3.1 leaves only one
active-root capacity failure in the one-torso branch:

> two desired private extension roles are forced to use the same
> connected lobe (or the same indispensable reserve carrier).

Ordinary portal rank and occurrence coverage are now complete for every
four-tuple of **distinct** dark lobes.  Closing the remaining residue
requires a genuine carrier-splitting or exact-seven operation-state
exchange; it cannot be attributed to Hall deficiency.
