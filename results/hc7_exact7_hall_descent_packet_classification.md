# Packet classification after a prescribed-portal Hall descent

**Status:** proved and independently audited.

This note identifies exactly when the two old full packets survive a
prescribed-portal exact-seven descent.  The incidence classification is
label-free.  Its two non-two-packet residues are a compulsory portal and
one alternating six-cycle incidence; the prescribed portal edge turns the
six-cycle residue into a labelled near-clique model.

## 1. Literal setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,
\]

be an actual separation.  Assume that `R` contains disjoint connected
`S`-full packets `P,Q` joined by a literal edge.  No connectedness of the
whole open shore `R` is assumed.

Suppose the prescribed-portal Hall argument returns a nonempty set
`U subseteq S`, a retained literal `s in S-U`, a prescribed portal edge
`sz`, a prescribed vertex `z in L`, and

\[
       Y=N_{L-\{z\}}(U),\qquad X=N_L(U)=Y\cup\{z\},
       \qquad |Y|=|U|-1,\quad |X|=|U|\le3.              \tag{1.1}
\]

Assume that `U` is inclusion-minimal deficient in the forced matching
problem.  Equivalently, every nonempty proper `W subsetneq U` satisfies

\[
                         |N_Y(W)|\ge |W|.               \tag{1.2}
\]

Finally assume that `C=L-X` is nonempty, connected, and full to the new
boundary defined below.  (In the counterexample application, fullness
follows because `G` is seven-connected and `C` is a component behind an
actual boundary of order seven.)  Put

\[
                         \Omega=(S-U)\cup X,
                         \qquad O=R\cup U.              \tag{1.3}
\]

The exact-seven descent says that `C` is one open shore behind `Omega`;
the other open shore is literally `O`.  There is no `R-X` edge because
there was no `R-L` edge in the old separation.

Call `T subseteq U` **X-dominating** when every vertex of `X` has a
neighbour in `T`.

## 2. Packet traces are exactly the incidence obstruction

### Lemma 2.1 (trace criterion)

The shore `O` contains two disjoint adjacent `Omega`-full packets if and
only if `U` contains two disjoint `X`-dominating sets.

#### Proof

Let `K subseteq O` be any `Omega`-full packet.  For every `x in X`, the
packet `K` must contain a neighbour of `x`.  Since `x` has no neighbour in
`R`, this neighbour lies in `K cap U`.  Thus `K cap U` is `X`-dominating.
Consequently two disjoint full packets have disjoint `X`-dominating traces.

Conversely, let `T_P,T_Q subseteq U` be disjoint `X`-dominating sets.
Then

\[
                              P'=P\cup T_P,
                         \qquad Q'=Q\cup T_Q             \tag{2.1}
\]

are disjoint.  They are connected because every member of `U` has a
neighbour in each of the old `S`-full packets `P,Q`.  They contact every
literal of `S-U` through `P,Q`, respectively, and contact every member of
`X` through their dominating traces.  Hence both are `Omega`-full.  The
old literal `P-Q` edge makes them adjacent.  \(\square\)

The connected set `P union U` is `Omega`-full: `P` supplies all retained
old-boundary contacts, every member of `U` attaches to `P`, and `U`
dominates `X=N_L(U)`.  Therefore, whenever the two-trace condition fails,
the `Omega`-packet number of the whole opposite shore is exactly one, not
zero.  Extra components of `R` cause no problem.

## 3. Exact Hall-incidence classification

### Theorem 3.1 (two packets, compulsory portal, or alternating six-cycle)

Under the setup of Section 1, exactly one of the following holds.

1. **Two-packet pull-through.**  The shore `O` contains two disjoint
   adjacent `Omega`-full packets.
2. **Compulsory portal.**  The prescribed vertex `z` has a unique neighbour
   `u_* in U`.  Every `Omega`-full packet in `O` contains `u_*`, and hence
   the `Omega`-packet number of `O` is one.
3. **Alternating three-gate.**  `|U|=|X|=3`, every vertex of `X` has degree
   two into `U`, and the three missing incidences form a perfect matching.
   Equivalently, the bipartite graph `G[U,X]` is a six-cycle.  Every
   `Omega`-full packet in `O` contains at least two members of `U`, and
   hence the `Omega`-packet number of `O` is one.

#### Proof

Put `k=|U|=|X|`.  Inclusion-minimality gives (1.2).

If `k=1`, then `Y` is empty and `z` has exactly one neighbour in `U`.
Outcome 2 holds.

Let `k=2`, say `U={u_1,u_2}` and `Y={y}`.  Applying (1.2) to each
singleton of `U` shows that `y` is adjacent to both `u_1,u_2`.  If `z` is
also adjacent to both, the two singletons `{u_1},{u_2}` are disjoint
`X`-dominating sets, and Lemma 2.1 gives outcome 1.  Otherwise `z` has a
unique neighbour `u_*`, and outcome 2 holds.

It remains that `k=3`; write `Y={y_1,y_2}`.  Equation (1.2), applied to
the one- and two-subsets of `U`, implies

\[
       d_U(y_1),d_U(y_2)\ge2,\qquad d_Y(u)\ge1
       \quad\hbox{for every }u\in U.                    \tag{3.1}
\]

Two disjoint `X`-dominating subsets of a three-set exist precisely when
there is a vertex `u_0 in U` such that

\[
             u_0\in N_U(y_1)\cap N_U(y_2)\cap N_U(z),
             \qquad d_U(z)\ge2.                         \tag{3.2}
\]

Indeed, under (3.2), the sets `{u_0}` and `U-{u_0}` both dominate `X`;
the second one does so by (3.1) and `d_U(z)>=2`.  Conversely, among two
disjoint nonempty subsets of a three-set one is a singleton, say `{u_0}`.
Its domination makes `u_0` common to all three neighbourhoods, and the
other dominating set shows that every member of `X`, in particular `z`,
has a neighbour outside `u_0`.

If `d_U(z)=1`, outcome 2 holds.  Suppose therefore that `d_U(z)>=2`.  If
`d_U(z)=3`, the two sets `N_U(y_1),N_U(y_2)`, each of order at least two
in a three-set, have a common member; (3.2) holds.  If `d_U(z)=2` and
(3.2) fails, then

\[
 N_U(y_1)\cap N_U(y_2)=\{m\},\qquad m\notin N_U(z).     \tag{3.3}
\]

Both `y_i` therefore have degree exactly two and miss distinct members of
`U`; the vertex `z` misses their unique common neighbour `m`.  Thus all
three vertices of `X` have degree two and their three missed neighbours
are distinct.  This is exactly a bipartite six-cycle, giving outcome 3.
In every other case (3.2) holds, and Lemma 2.1 gives outcome 1.

Finally, in outcome 2 every `X`-dominating trace contains the unique
neighbour of `z`.  In outcome 3, no singleton of `U` dominates `X`, so
every dominating trace has order at least two; two such subsets of a
three-set intersect.  Lemma 2.1 and fullness of `O` now give packet number
exactly one in both cases.  \(\square\)

## 4. The alternating cycle is already a labelled near model

The packet classification did not use the prescribed edge `sz`.  That edge
closes its only non-star obstruction.

### Lemma 4.1 (alternating Hall cycle handoff)

In outcome 3 of Theorem 3.1, `G` contains a literal labelled `K_7^vee`
model.

#### Proof

The bipartite six-cycle on `U union X` has a perfect matching.  Let

\[
                         A_1,A_2,A_3                    \tag{4.1}
\]

be its three matching edges, regarded as two-vertex connected branch
sets.  Contracting alternate edges of a six-cycle leaves a triangle, so
the three `A_i` are pairwise adjacent.  Let `A_z` denote the one which
contains `z`.

Here `|U|=3`, so the retained old-boundary set `S-U` has order four.
Choose

\[
                         r in (S-U)-\{s\}.              \tag{4.2}
\]

Use the six rim bags

\[
                         C\cup\{r\},\quad P,\quad Q,
                         \quad A_1,A_2,A_3.             \tag{4.3}
\]

They form a literal `K_6` model.  Indeed:

* `C union {r}` is connected because `C` is `Omega`-full;
* `P-Q` is literal, and both old packets meet `r`, so both meet
  `C union {r}`;
* each `A_i` contains one member of `U` and one member of `X`, hence meets
  both `P,Q` through its old boundary literal and meets `C` through its
  new gate; and
* the three `A_i` are pairwise adjacent by the remaining edges of the
  six-cycle.

The seventh bag is the singleton `{s}`.  It meets `P,Q` by old
`S`-fullness, meets `C union {r}` because `C` is full to the retained
literal `s in Omega`, and meets `A_z` through the prescribed literal edge
`sz`.  Thus `{s}` has at least four neighbours on the `K_6` rim.  Its at
most two missing rim adjacencies share the endpoint `{s}`, so the seven
bags form a literal labelled `K_7^vee` model.  \(\square\)

No boundary edge other than the prescribed edge `sz` is used.

### Corollary 4.2 (composition after the Hall descent)

In the counterexample kernel, a prescribed-portal descent has one of the
following outputs:

1. the descended opposite shore contains two disjoint adjacent
   `Omega`-full packets;
2. `G` contains a literal labelled `K_7^vee` model; or
3. `z` has a unique neighbour `u_* in U`, and every `Omega`-full packet
   in the opposite shore contains `u_*`.

In outcome 1, the exact-seven packet theorem orients the descendant as
`(1,2)` or `(1,3)` with `C` on the packet-thin side; adaptive reflection
closes `(1,3)`.  Thus every surviving outcome 1 is a strict-shore-order
`(1,2)` descendant.  No equality state is asserted to survive.

#### Proof

Theorem 3.1 gives the three packet-incidence alternatives.  Lemma 4.1
turns its alternating outcome into item 2.  The compulsory outcome is item
3.  In the two-packet outcome, `C` is one `Omega`-full packet and the
opposite shore contains at least two.  The exact-seven packet theorem
therefore makes the two packet numbers `(1,2)` or `(1,3)` in this
orientation, and the audited adaptive-reflection theorem eliminates the
latter.  \(\square\)

## 5. Consequence and trust boundary

The prescribed-portal descent therefore preserves the rich two-packet
side except in two canonical ways:

* a one-portal bottleneck, which includes every `|U|=1` residue and the
  degree-one `z` residues for `|U|=2,3`; or
* the label-free alternating word on three old literals and three new
  gates, represented by `G[U,X]=C_6`; the prescribed edge closes this
  second packet obstruction by Lemma 4.1.

Both are sharp at the packet level.  In the compulsory case every full
packet must contain `u_*`; in the alternating case every full packet must
spend at least two of the three old literals.  Thus no rearrangement inside
the old connected rich shore can create two disjoint new full packets
without using additional colouring-state or labelled-model information.

The only surviving packet-number-one residue is therefore the compulsory
portal.  The theorem does **not** assert that this residue reflects an
equality state, contains `K_7^vee`, or supplies a fixed apex pair.  Strong
contraction-criticality is not used.  The remaining composition obligation
is exact: exploit the canonical literal `u_*` which belongs to every full
packet on the new opposite shore.
