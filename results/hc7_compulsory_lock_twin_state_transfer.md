# Twin-boundary transfer of a lifted compulsory-lock state

**Status:** proved and independently audited.

This note records the strongest literal handoff obtained directly from the
compulsory-edge lock-state lift.  It creates an actual exact-seven cell,
transports a named legal state to it, and forces its packet vector to be
`(1,1)`.  Thus the atomic `(1,2)` branch has a label-faithful S4 handoff;
closing the receiving `(1,1)` programme remains a separate global task.

## 1. Setup

Use the nonsingleton frozen atomic setup

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |W|=6,
\]

with no `A-R` edge.  Assume:

1. `G` is seven-connected and `K_7`-minor-free, is not six-colourable,
   and every proper minor of `G` is six-colourable;
2. `A` and `R` are connected, `A` is `S`-full, and `R` contains two
   disjoint adjacent `S`-full packets; the oriented packet vector is
   `nu_A=1,nu_R=2`;
3. `e=zu`, with `z in A`, is the unique `A-u` edge and is a bridge of
   `G-W`; and
4. `|A|>=2`; and
5. the atomic boundary frontier `G[S]` is either connected bipartite or
   `K_{1,3} dotunion K_3` (with the audited retained-triangle convention
   in the second case).

Fix the data of the audited compulsory-edge lock-state lift.  Thus `phi` is
a six-colouring of `G-e`, `f` is a rich-internal or boundary--rich bridge
of one compulsory two-colour lock, and swapping the `z`-side of that lock
gives a colouring `psi` of `G-f`.  The ends of `f` have the same colour in
`psi`, so `psi` descends to `G/f`, retaining a literal boundary label when
`f` is boundary--rich.

Put

\[
       \Omega=W\mathbin{\dot\cup}\{z\},\qquad
       C=A-z,\qquad B=R\cup\{u\}.                       \tag{1.1}
\]

Let `Pi_Omega` be the exact equality partition of `Omega` under `psi`.

## 2. The literal twin cell

### Theorem 2.1 (stateful twin-boundary transfer)

The decomposition

\[
                 V(G)=C\mathbin{\dot\cup}\Omega
                         \mathbin{\dot\cup}B             \tag{2.1}
\]

is an actual order-seven separation with both open shores nonempty,
connected, and `Omega`-full.  Moreover:

1. the maximum number `nu_B` of disjoint `Omega`-full packets in `B` is
   exactly one;
2. `psi` restricts to an intact six-colouring of the closed shore
   \(G[C\cup\Omega]\) with exact boundary state `Pi_Omega`; and
3. contracting the named edge `f` in the opposite closed shore gives a
   proper minor coloured by `psi` with the same exact labelled boundary
   state `Pi_Omega`.  If `f` has one end in `Omega`, that literal boundary
   label is retained under the contraction; and
4. if `Pi'` is the exact state of the old boundary `S` under `psi`, then
   `Pi_Omega` is obtained by the literal root substitution
   \[
      u\longmapsto z:
      \quad u\text{ is deleted from its }\alpha\text{-block and }z
      \text{ is inserted into the }\beta\text{-block},                \tag{2.2}
   \]
   where `alpha=phi(u)=phi(z)` and `beta` is the lock colour.  Empty
   blocks are discarded and a missing `beta`-block is created.

Thus a single legal `G-e` state produces a literal state-labelled twin
seven-cell, rather than merely an unlabelled `(1,1)` or near-model
interface.

#### Proof

The audited root-deletion normalization says that `C=A-z` is nonempty,
connected, and `W`-full.  Since `A` is connected and `C` is nonempty, `z`
has a neighbour in `C`.  Hence `C` is `Omega`-full.

The set `B` is connected: `R` is connected and an old `S`-full packet in
`R` has a neighbour at `u`.  It is `Omega`-full because its `R` part meets
every member of `W`, while the edge `uz` supplies its contact with `z`.
There is no `C-B` edge: there is no `A-R` edge, and uniqueness of the
`A-u` edge excludes every edge from `C` to `u`.  Equation (2.1) is
therefore an actual order-seven separation.

Every `Omega`-full packet contained in `B` must contain a neighbour of
`z`.  Inside `B`, the only such neighbour is `u`: there is no `A-R` edge
and `zu` is the displayed bridge.  Hence two disjoint `Omega`-full packets
in `B` cannot exist.  Since `B` itself is a connected `Omega`-full packet,
`nu_B=1`.

The edge `f` is rich-internal or boundary--rich in the old separation.  It
therefore has an end in `R` and is not an edge of \(G[C\cup\Omega]\).
Consequently the proper colouring `psi` of `G-f` restricts to an intact
colouring of that closed shore, with exact boundary partition `Pi_Omega`.

Both ends of `f` receive the same colour in `psi`, so `psi` descends to
`G/f`.  The edge lies in the opposite closed shore \(G[B\cup\Omega]\):
a former boundary end in `W` lies in `Omega`, while a former boundary end
at `u` now lies in `B`.  In the first case contract the rich end into the
literal vertex of `W`; otherwise the contraction is wholly off `Omega`.
In every case the seven labels of `Omega` survive and have exact partition
`Pi_Omega`.

Finally, the lock swap leaves `u` with colour `alpha` and changes `z` to
`beta`; every member of `W` has the same colour whether it is viewed in
`S` or in `Omega`.  This is exactly the substitution (2.2), and proves all
assertions.  \(\square\)

## 3. Capacity consequence

Let `H_Omega=G[Omega]`, and let `nu_C` be the maximum number of pairwise
disjoint `Omega`-full packets in `C`.

### Lemma 3.1 (the deleted-root shore is packet-thin)

In a hypothetical counterexample,

\[
                              \nu_C=1.                  \tag{3.1}
\]

#### Proof

The connected `Omega`-full shore `C` itself is one packet, so
`nu_C>=1`.  Suppose it contains disjoint `Omega`-full packets `D_1,D_2`.
Set

\[
                         X=D_1\cup\{z\},\qquad Y=D_2.
\]

Both sets lie in the old thin shore `A`, are nonempty, connected and
disjoint.  They are adjacent because `D_2` has a neighbour at the literal
vertex `z`.  The carrier `X` contains `z`, meets all of `W` through `D_1`,
and meets `u` through `zu`; hence it is old-`S`-full.  The carrier `Y`
meets every member of `W` and misses only `u`, because `zu` is the unique
old `A-u` edge.  Therefore

\[
                        |N_S(X)|=7,\qquad |N_S(Y)|=6.
\]

These are exactly the disjoint adjacent near-full rooted carriers excluded
by the audited atomic near-full two-carrier state-exchange theorem.  Its
connected-bipartite branch six-colours `G`; in the exceptional
`K_{1,3} dotunion K_3` frontier it six-colours `G` or gives a literal
`K_7`.  Both contradict the frozen setup.  Thus `nu_C=1`.  \(\square\)

### Corollary 3.2 (the transferred state outruns both capacities)

In a `K_7`-minor-free hypothetical counterexample,

\[
                    d_{H_\Omega}(\Pi_\Omega)\ge2.       \tag{3.2}
\]

In particular, `nu_C` cannot by itself reflect the transferred state.

#### Proof

Suppose instead that the packet demand is at most one.  Apply the audited
exact packet-reflection lemma using the full packet `C`.  It either
displays a literal `K_7` model, or produces an intact
colouring of the opposite closed shore \(G[B\cup\Omega]\) whose exact
boundary partition is `Pi_Omega`.

The first outcome is excluded by hypothesis.  In the second, align its
palette on `Omega` with the intact colouring
\(\psi|G[C\cup\Omega]\) from Theorem 2.1.  There is no `C-B` edge, so the
two colourings glue to a six-colouring of `G`, a contradiction.  This
proves (3.2).  \(\square\)

The twin cell therefore has exact packet vector `(1,1)`, and its legally
attained root-substitution state has demand at least two.

## 4. Receiver-side lock localization

Let `r` be an end of `f` in \(R\subseteq B\), and let `q` be its other end.
Write `gamma=psi(r)=psi(q)`.  For every colour `delta != gamma`, let
`K_delta^B` be the `gamma-delta` component containing `r` in

\[
                         G[B\cup\Omega]-f.             \tag{4.1}
\]

### Theorem 4.1 (internal lock or opposite-shore crossing)

For every `delta != gamma`, at least one of the following holds:

1. `q in K_delta^B`; thus the `f`-Kempe lock for `delta` is already
   connected inside the receiving closed shore; or
2. there is a `gamma-delta` path with distinct ends in `Omega`, all
   internal vertices in `C`, whose ends lie respectively in
   \[
                     T_delta=K_delta^B\cap\Omega
       \quad\hbox{and}\quad \Omega-T_delta.            \tag{4.2}
   \]

If neither outcome can be certified for some `delta`, the two closed
shores have a common exact state and `G` is six-colourable.

#### Proof

Suppose `q notin K_delta^B`.  Swap `gamma,delta` on `K_delta^B` in the
right closed shore.  The swap preserves every edge other than `f`, and it
changes `r` while leaving `q` unchanged, so it restores `f`.  We obtain an
intact proper colouring of \(G[B\cup\Omega]\) which toggles exactly the
boundary set `T_delta` relative to `psi`.

Consider the `gamma-delta` components of the intact left closed shore
\(G[C\cup\Omega]\) under `psi`.  If `T_delta` is a union of their boundary
traces, swap precisely those components meeting `T_delta`.  This toggles
exactly the same literal boundary vertices as the right-side swap.  The
two intact closed-shore colourings then have the same exact boundary
state; align their palettes and glue, six-colouring `G`.

In a hypothetical counterexample, `T_delta` is therefore not a union of
left component traces.  Some left `gamma-delta` component meets both
`T_delta` and its complement.  A shortest path in that component between
the two boundary sets has no internal boundary vertex, and hence all of
its internal vertices lie in `C`.  This is outcome 2.  If instead
`q in K_delta^B`, outcome 1 holds.  The alternatives exhaust every
`delta`.  \(\square\)

Thus the exact receiver obstruction is not an abstract palette issue.  It
is a five-colour mixture of literal locks internal to \(B\cup\Omega\) and
literal boundary-to-boundary crossings through `C`; any missing member of
that mixture gives a common-state colouring.

## 5. Handoff scope

The construction closes the local legality and packet-orientation gaps.
Relative to the exact-seven packet hierarchy, the packet-sum rank drops
strictly:

\[
                 \nu_A+\nu_R=1+2=3
                 \quad\longrightarrow\quad
                 \nu_C+\nu_B=1+1=2.                   \tag{5.1}
\]

The handoff is normalized by the literal map `u -> z`, the exact state
`Pi_Omega`, and the named `f`-contraction on the receiving right closed
shore.  It is therefore substantially stronger than an unspecified
`(1,1)` adhesion.

It does not close the global receiver:

* exchanging `u` and `z` recovers the old twin geometry.  Root exchange
  is an involution, so shore order alone supplies no decreasing rank;
* `Pi_Omega` is the actual state returned by the lock swap.  Nothing in
  the construction makes it the recursive paired `2+2+2+1` state.
* The right closed shore has `Pi_Omega` only after the named contraction
  of `f`; it is not an intact extension.  Removing that last contraction
  is exactly the state-lifting problem, not a palette relabelling.

Thus Theorem 2.1 and Lemma 3.1 discharge the atomic branch into the
labelled S4 stratum with the strict packet-sum drop (5.1).  They do not
prove HC7, because the current proof spine has no theorem resolving every
state-labelled `(1,1)` cell.  The next global theorem must be a
**twin-state receiver**: it must reflect `Pi_Omega`, produce a literal
`K_7`/fixed-pair terminal, or supply a further normalized S1 transition
with a rank which cannot cycle back through the involutive root exchange.

### Corollary 5.1 (exact surviving compulsory-lock branch)

If the active proof remains in the atomic `(1,2)` stratum after every
normalized S4 handoff has been delegated, then for every legal colouring
of `G-zu` and every alternate colour, its compulsory `z-u` lock has no
`z-u`-separating bridge which is rich-internal or boundary--rich.

Indeed, any such bridge is the edge `f` in the setup above and triggers
the state-labelled `(1,1)` handoff.  This corollary makes no stronger
vertex-disjointness claim: a surviving lock may still have a separating
edge wholly in the old thin shore.  The exact remaining local branch is
therefore the **all-five-locks rich-edge-nonseparable branch**, together
with the global S4 receiver for the handed-off cells.
