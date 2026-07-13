# Lifting a partial-2-tree carrier adhesion

## 1. Label-free setup

Let `Q={q_1,q_2,q_3}` be a triangle in a seven-connected graph `G`, and
put `H=G-Q`.  Let

\[
              \mathcal P=(\{a\},\{b\},\{c\},D_1,\ldots,D_m) \tag{1.1}
\]

be a partition of `H` into connected `Q`-full sets, maximal by number of
parts.  Thus every part contains a neighbour of each `q_i`.  Let `R` be
the simple quotient.

In the `K_7`-free branch, the `Q`-full quotient theorem gives

\[
                          R\text{ is }K_4\text{-minor-free}.   \tag{1.2}
\]

Hence `R` is a partial 2-tree.  Every quotient separator of order at most
two contains a nonsingleton `Q`-indecomposable carrier: a part which has
no connected bipartition into two `Q`-full sides.

The purpose of this note is to distinguish an actual small separator from
a separator which only exists after contracting an arbitrarily large
carrier.

## 2. A tree carrier has one universal rainbow gate

The next lemma is independent of `Q` and of the number of terminal sets.

### Lemma 2.1 (Helly gate for an indecomposable tree)

Let `T` be a finite tree and let `P_1,...,P_s` be nonempty vertex sets.
Call a connected subgraph **rainbow** if it meets every `P_i`.  Exactly
one of the following holds.

1. `T` contains two vertex-disjoint rainbow connected subgraphs.  They
   extend to a connected adjacent bipartition of `T` whose two sides are
   rainbow.
2. There is a vertex `x in T` which belongs to every rainbow connected
   subgraph of `T`.

#### Proof

If two disjoint rainbow subtrees exist, contract them, take a spanning
tree, and delete an edge on the path between the contraction vertices.
Lifting gives the bipartition in outcome 1.

Suppose no two rainbow subtrees are disjoint.  The family of all
inclusion-minimal rainbow subtrees is finite and pairwise intersecting.
Subtrees of a tree have the Helly property, so one vertex `x` belongs to
all of them.  Every rainbow connected subgraph contains an
inclusion-minimal rainbow subtree and therefore contains `x`.  This is
outcome 2.  QED.

### Corollary 2.2 (`Q`-indecomposable tree gate)

If a `Q`-full carrier `D` is a tree and is indecomposable in the maximal
partition, then there is a vertex `x_D` meeting every connected
`Q`-full subgraph of `D`.  In particular every component of `D-x_D`
misses at least one of the three neutral portal classes.

## 3. Exact lifting of a quotient cut

Let `S` be a quotient separator of order at most two.  Bipartition **all**
components of `R-S` into two nonempty families `mathcal L,mathcal R`, and
write `L,R` for the respective unions in `H` of all parts indexed by
those families.  Each of `L,R` may have several components; this causes
no problem because the portal sets below are their full unions.

Let `U` be the union of all nonsingleton carrier parts indexed by `S`,
including every edge between those parts.  Define its left and right
portal sets

\[
 L_U=N_U(L),\qquad R_U=N_U(R).                      \tag{3.1}
\]

Singleton vertices of `S` are retained literally.

### Lemma 3.1 (faithful gate lift)

Let `Z subseteq U` separate all of `L_U` from all of `R_U` in the
combined carrier graph `H[U]`.  Let `S_0` be the set of singleton
quotient vertices in `S`.  Then

\[
                              Q\cup S_0\cup Z                \tag{3.2}
\]

separates `L` from `R` in `G`.

#### Proof

Delete `Q` and `S_0`.  Any remaining `L-R` path projects to a quotient
walk using only nonsingleton vertices of `S` between its last visit to a
component in `mathcal L` and first visit to one in `mathcal R`.  There is
no third unassigned quotient component through which it can detour.  That subpath is contained in the combined
carrier graph `H[U]`, begins in `L_U`, and ends in `R_U`.  It cannot avoid
`Z`.  QED.

In particular, if

\[
                              |S_0|+|Z|\le3,                \tag{3.3}
\]

then (3.2) is an actual cut of order at most six, contradicting
seven-connectivity.

Separate gates chosen independently inside two carriers are insufficient:
a path may alternate `L-D-E-R` without crossing either carrier from its
own left portal set to its own right portal set.  The combined-network
hypothesis in Lemma 3.1 is essential.

### Theorem 3.2 (one tree-carrier cut or straddling dark component)

Assume `S` contains exactly one nonsingleton carrier `D`; its possible
other member is a singleton.  Assume `D` is a tree and is
`Q`-indecomposable, and choose its Helly gate `x_D` from Corollary 2.2.
At least one of the following holds.

1. A carrier has a connected `Q`-full bipartition, contradicting
   maximality of (1.1).
2. The set

   \[
                              Q\cup S_0\cup\{x_D\}           \tag{3.4}
   \]

   is an actual cut of order at most five.
3. A component `K` of `D-x_D` meets both `N_D(L)` and `N_D(R)`.
   The component `K` misses at least one neutral portal
   class.

#### Proof

Outcome 1 is the first outcome of Lemma 2.1.  Otherwise the carrier has
the displayed gate and all its gate components are non-rainbow.  If no
component of `D-x_D` meets both portal sides, then `{x_D}` separates
the combined carrier portal sets.  Lemma 3.1 makes (3.4) an actual cut.
There is at most one additional singleton in the quotient separator, so

\[
                         |(3.4)|\le3+1+1=5.
\]

If the small-cut conclusion fails, the straddling component exists.  It is
not `Q`-full by Corollary 2.2, proving outcome 3.  QED.

This theorem is a complete carrier-adhesion lift for a one-carrier
quotient cut.  With two carrier vertices, Lemma 3.1 remains valid only
after their union and cross-edges are treated as one carrier network.  A
component of that union after deleting the two Helly gates can alternate
between carriers and need not be dark to one common label.

### Theorem 3.3 (arbitrary one-carrier state split or straddling lobe)

Assume `S` contains exactly one nonsingleton carrier `D`; its possible
other member is a singleton.  Let

\[
 P_i=N_D(q_i)\qquad(i=1,2,3)
\]

be the three nonempty neutral portal classes.  At least one of the
following holds.

1. `D` contains disjoint adjacent connected shores with portal rows
   `P_1P_2|P_2P_3` or `P_1P_3|P_2P_3`.
2. There is an actual separation of `G` of order at most six between the
   two selected quotient sides `L,R`.
3. There are vertices `z_2,z_3` (possibly equal) and a component `K` of
   `D-{z_2,z_3}` such that `K` meets both `N_D(L)` and `N_D(R)`, while
   `K` meets at most one of `P_1,P_2,P_3`.

In a seven-connected graph outcome 2 is impossible.  Thus failure of a
typed state-shore split has one exact residue: a straddling portal-dark
lobe behind a gate of order at most two.

#### Proof

Apply Theorem 2.1 of `hadwiger_state_shore_or_two_gate.md` to
`(P_1,P_2,P_3)`.  Its first two outcomes are outcome 1 here.  Otherwise
it supplies `Z={z_2,z_3}` of order at most two.  Corollary 2.3 of that
note says that every component of `D-Z` meets at most one neutral portal
class.

If one such component meets both carrier incidence sets
`N_D(L),N_D(R)`, it is the set `K` in outcome 3.  If none does, every
`N_D(L)`--`N_D(R)` path in `D` meets `Z`; hence `Z` separates the two
incidence sets in the combined carrier graph (which here is just `D`).
Lemma 3.1 then makes

\[
                       Q\cup S_0\cup Z
\]

an actual separator between `L,R`.  Its order is at most
`3+1+2=6`, proving outcome 2. \(\square\)

The theorem strictly extends Theorem 3.2 beyond tree carriers.  It does
not solve a two-carrier quotient cut: there a path may alternate between
the carriers and avoid both gates as individual left--right separators.

### Theorem 3.4 (two-carrier combined-gate trichotomy)

Assume the quotient separator consists of two nonsingleton carriers
`D,E`.  Suppose neither carrier has either typed state-shore split from
Theorem 3.3.  Let `Z_D,Z_E` be their respective two-gates and put

\[
                   U=D\cup E,\qquad Z=Z_D\cup Z_E,              \tag{3.5}
\]

where `U` includes every edge between the carriers.  Then at least one of
the following holds.

1. A component of `H[U]-Z` meets both combined incidence sets
   `L_U=N_U(L)` and `R_U=N_U(R)`.
2. `Q union Z` is an actual separator between `L` and `R`, of order at
   most seven.

If `G` is seven-connected and outcome 2 holds, then necessarily

\[
                         |Z_D|=|Z_E|=2,                         \tag{3.6}
\]

and `Q union Z` is an exact order-seven adhesion.  Thus every smaller or
degenerate pair of carrier gates forces the combined straddling outcome.

#### Proof

If no component of `H[U]-Z` meets both `L_U,R_U`, every path between
those two incidence sets meets `Z`.  Lemma 3.1, applied to the **combined**
carrier graph, makes `Q union Z` an actual separator.  Since each gate has
order at most two, its order is at most `3+4=7`.

Seven-connectivity excludes order at most six.  The carrier parts are
disjoint, so `Z_D,Z_E` are automatically disjoint.  Equality can therefore
hold only when both gate sets have order two, which is precisely (3.6).  The two
alternatives are exhaustive. \(\square\)

Unlike the one-carrier residue, a straddling component in outcome 1 need
not be dark to a common neutral label: it may alternate between a
`q_i`-dark lobe of `D` and a differently dark lobe of `E`.  Treating the
two carriers separately at this point would be invalid.  The theorem
isolates the exact remaining full-adhesion state: combined alternation, or
four distinct gates on one literal seven-vertex cut.

The theorem also identifies why a quotient two-cut need not lift directly:
a dark
component can pass through the universal rainbow gate from the left shore
to the right shore without itself being `Q`-full.

## 4. General carriers and the exact bridge-stabilization lemma

The block tree and every chain of 2-separations can now be removed before
the bridge-stabilization step.  By the torso--Helly theorem in
`hadwiger_rainbow_torso_helly_core.md`, a `Q`-indecomposable carrier has
one bag `B` of its Tutte decomposition which meets every connected
`Q`-full subgraph.  The adhesion is at most two, every component outside
`B` is `Q`-dark, and it has at most two neighbours in `B`.  The torso on
`B` is one of:

1. an order-at-most-two gate;
2. a cycle; or
3. a 3-connected torso.

In the first case, Lemma 3.1 lifts the gate to a cut whenever no dark
lobe straddles the two quotient shores.  In the other cases, every portal
and shore incidence outside the torso is represented by a named dark
lobe on an adhesion of order at most two.  Thus the unproved exchange
below may be confined to one cycle or 3-connected torso.  Virtual torso
edges must still be expanded through their named lobes, and for a
two-carrier quotient cut the two carriers plus their cross-edges remain
one combined network; individual torso gates do not lift independently.

For a general carrier `D`, choose a tree `W` minimal subject to meeting
the three neutral portal classes.  Every leaf of `W` is essential for a
portal class, so `W` has at most three leaves.  Components of `D-W` are
`W`-bridges.  A bridge meeting all three portal classes gives two disjoint
rainbow carriers (`W` and the bridge) and contradicts maximality.  Thus
every off-core bridge is dark to at least one label.

The exact missing label-free theorem is:

> **Carrier bridge-stabilization lemma.**  Let `D` be connected, with
> three nonempty portal sets and two external incidence sets `L_D,R_D`.
> Let `W` be a minimal rainbow tree.  Assume every off-core bridge is
> dark, and every bridge which straddles the left and right incidence
> systems has the attachment surplus forced by seven-connectivity.  Then
> one of the following holds:
>
> 1. `D` has two disjoint connected rainbow subgraphs;
> 2. some set `Z_D` of the size allowed by (3.3) separates all of `L_D`
>    from all of `R_D`; or
> 3. the `W`-bridges admit a common noncrossing disk embedding in which
>    one fixed neutral portal class lies on the outer face.

Outcome 1 refines the maximal `Q`-full partition.  Outcome 2 lifts by
Lemma 3.1 to a literal cut of order at most six.  Outcome 3 is the local
rural state needed for a coherent apex pair.

The bridge-overlap step is the only unproved part: one must show using
actual attachment vertices that crossing straddling bridges produce two
disjoint rainbow subgraphs while preserving all three portal classes.
Ordinary quotient crossing is insufficient because it forgets whether an
essential portal leaf is consumed by the rerouting.

## 5. Coherent rural assembly: exact hypothesis

The local rural outcome becomes a global two-apex conclusion under the
following explicit compatibility condition.  Choose one neutral vertex
`q_k`.  Suppose

1. `R` has an outerplane embedding;
2. every carrier has a disk embedding compatible with the cyclic order
   induced by that outerplane embedding; and
3. every neighbour of `q_k` in each carrier lies on the corresponding
   outer boundary.

Substitute the carrier disks into the outerplane quotient and place
`q_k` in the outer face.  This gives a plane drawing of

\[
                         G-(Q-\{q_k\}),              \tag{5.1}
\]

so the other two neutral vertices are a coherent global apex pair.

The outerplane hypothesis is essential: a partial 2-tree need not be
outerplanar.  Thus `K_4`-minor-freeness of the `Q`-full quotient alone
does not justify a two-apex conclusion.
