# Exact-seven forced-path completion

## 1. Boundary theorem

Let `F` be a triangle-free graph on the literal seven-set `S`, and let

\[
                 \Lambda(s)\subseteq\{1,2,3\}
\]

be nonempty raw lists satisfying

\[
              |\Lambda(s)|\le2\quad(s\in S),
 \qquad |\{s:q\in\Lambda(s)\}|\ge4\quad(q=1,2,3).       \tag{1.1}
\]

Form the carrier auxiliary graph `Q(F,Lambda)` by adjoining a triangle
`c_1c_2c_3` and the incidence edge `sc_q` exactly when
`q in Lambda(s)`.  An **anchored `K_4`** is a `K_4` model in `Q` with four
bags using exactly four vertices of `S`, one per bag.

Perform singleton propagation: if `Lambda(x)={q}`, assign `q` to `x`,
delete `x`, and remove `q` from every remaining neighbour list.  Stop when
a list becomes empty or no singleton remains.

### Theorem 1.1 (anchored model or forced conflict)

At least one of the following conclusions holds:

1. `(F,Lambda)` is list-colourable;
2. `Q(F,Lambda)` contains an anchored `K_4`; or
3. singleton propagation reaches an empty list.

Equivalently, if the raw state is uncolourable and has no anchored `K_4`,
then propagation must end in a literal forced conflict; it cannot stabilize
at an uncolourable pair-list bicycle.

#### Proof

Suppose the state is uncolourable, has no anchored `K_4`, and propagation
does not reach an empty list.  Singleton propagation preserves
colourability in both directions.  Its stable residual `(H,L)` is therefore
uncolourable.  Every residual list has order at least two, while propagation
only deletes colours from raw lists of order at most two.  Hence every
residual list is a pair and is equal to its original raw list.

Apply the audited triangle-free three-palette critical-core classification
to `(H,L)`.  After vertex and edge deletion and list enlargement it contains
one of `T1`--`T10`.  At a displayed pair-list vertex, the residual and raw
list is that exact pair.  At a displayed full-list vertex, the residual/raw
list is one of its three pair subsets.

The raw support bound (1.1) eliminates five template types.

* `T1` has five pair-list vertices all using the same two colours.  Only the
  two vertices of `S` outside the core can contain the third colour, so its
  raw support is at most two.
* `T3` uses all seven vertices and only two colours.
* `T7,T8,T9` use all seven vertices.  Replacing every displayed full list
  by an arbitrary pair leaves some palette colour with support at most
  three, as verified in the audited critical-core census.

For `T2,T4,T5,T6`, the explicit anchored bags from the audited pair-bicycle
completion use only displayed pair incidences and retained boundary edges.
For `T10`, the same anchored bags work for all three pair refinements of its
one displayed full list, and avoid that refined vertex.  Thus each remaining
template gives an anchored `K_4` in the original raw auxiliary graph: core
edge deletion and list enlargement only discarded extra original data, and
every incidence used by the displayed bags is an exact raw pair incidence.

This contradicts the assumption that no anchored `K_4` exists.  Therefore
the stable residual cannot be uncolourable.  If it were colourable, reversing
the conflict-free propagation assignments would colour the raw instance,
also a contradiction.  Propagation must reach an empty list. `square`

The theorem is not the false assertion that an equal-singleton boundary edge
must already be present.  For example, on the path `0-1-2`, the lists

\[
 \{1\},\{1,2\},\{2\},\{1,3\},\{1,3\},\{2,3\},\{2,3\}
\]

have support `(4,4,4)`, are uncolourable, and have no equal-singleton edge;
the conflict is transported through the middle pair-list vertex.

## 2. Exact forcing certificate

The conflict in Theorem 1.1 has a canonical implication-path certificate.
For every vertex `v` and every `q in Lambda(v)`, make an assignment-literal
node `(v,q)`.  For every singleton `v` with list `{q}`, make a source
`sigma_v` and an arc

\[
                         \sigma_v\longrightarrow(v,q). \tag{2.1}
\]

For every boundary edge `uv` and common colour `q`:

* if `v` has pair list `{q,r}`, add `(u,q) -> (v,r)`;
* if `v` has singleton list `{q}`, add `(u,q) -> bot`;
* add the symmetric implications with `u,v` interchanged.

### Lemma 2.1 (forced-path certificate)

Singleton propagation reaches an empty list if and only if its forcing
digraph contains either

1. a directed path from a singleton source to `bot`; or
2. directed paths, starting at singleton sources which may coincide, to
   both `(v,a)` and `(v,b)` for one pair-list vertex
   `Lambda(v)={a,b}`.

#### Proof

When a vertex is forced to colour `q`, every neighbour whose pair list is
`{q,r}` is forced to `r`; this is exactly one implication arc.  A neighbour
already forced to the singleton colour `q` gives `bot`.  If two forcing
chains assign the two different choices at one pair vertex, the deletions
which caused those assignments remove both colours from its list.  Thus
either displayed directed configuration produces precisely a propagation
conflict.

Conversely, trace the first empty list backward through the propagation
steps.  If it is a singleton conflict, the predecessor chain ends at `bot`.
If both colours were removed from a former pair list, trace the two removing
assignments backward.  Every noninitial forced assignment has a predecessor
across the boundary edge which removed its other colour, and the finite trace
ends at raw singleton sources.  This gives the two directed paths in item 2.
`square`

The paths may share vertices and need not project to one simple boundary
path.  The exact negative object is a one- or two-source **forced unit
bicycle**, not necessarily an odd cycle or an equal-singleton edge.

## 3. Literal `HC_7` consequence

In an exact-seven spanning three-carrier state, an anchored `K_4` in `Q`
lifts by replacing `c_q` with its actual carrier.  The four anchored bags,
together with the three opposite `S`-full packet bags, form a literal `K_7`
by the audited `6+12+3` adjacency count.  A full raw list also gives the
same literal lift directly.  A colourable raw state six-colours `G` by the
audited spanning-triangle list-state theorem.

Consequently, in every canonical crossed-chain state of a hypothetical
counterexample:

* no raw list is full;
* some raw list is singleton; and
* the forcing digraph contains one of the two explicit certificates in
  Lemma 2.1.

This closes the residual pair-bicycle branch.  The remaining obstruction is
now dynamic: a forced unit bicycle must survive every literal block transfer.

## 4. The two allocations at one cut

Use the canonical crossed cut from the audited block-chain list exchange.
The fixed carriers away from the cutvertex `z` determine a base contact list
`M(s)`.  Allocating `z` to the left carrier adds colour `j`; allocating it
to the right carrier adds colour `k`.  Thus, for

\[
                          Z=N_S(z),
\]

the lists agree outside `Z`, while for `s in Z`

\[
              \Lambda^{\rm L}(s)=M(s)\cup\{j\},
       \qquad \Lambda^{\rm R}(s)=M(s)\cup\{k\}.         \tag{4.1}

Both states are nonempty, have no full list, and have support at least four
per colour.  Write `i` for the fixed carrier colour.

### Proposition 4.1 (five literal switch types)

For every `s in Z`, the ordered pair
`(Lambda^L(s),Lambda^R(s))` is one of

\[
 (ij,ik),\quad (j,k),\quad (j,jk),\quad (jk,k),
                         \quad(jk,jk).                  \tag{4.2}

The first type occurs exactly when `i in M(s)`; the other four occur when
`i notin M(s)`.

#### Proof

If `i in M(s)`, then a `k` already in `M(s)` would make the left list full,
and a `j` already in `M(s)` would make the right list full.  Hence
`M(s)={i}`, giving `(ij,ik)`.

If `i notin M(s)`, then `M(s)` is one of
`emptyset,{j},{k},{j,k}`.  Substitution in (4.1) gives the last four types
in the displayed order. `square`

Thus a cut transfer changes the forcing digraph only at the literal portal
set `Z`, by the five explicit switch operations (4.2).  In a target-free
host both allocations have forced unit bicycles by Theorem 1.1.  If a
certificate changes, its first changed literal lies in `Z`; if it does not,
the same literal forcing certificate persists across the cut.

## 5. Exact remaining step

The proof has reduced the crossed block-chain state problem to one named
operation-state lemma:

> **Forced-bicycle transport.**  Along the monotone block-chain sweep, a
> sequence of switch sets `Z` of the five types (4.2) cannot carry a forced
> unit bicycle through every state unless the persistent certificate is
> governed by one fixed literal two-vertex endgame.

The first alternative to target is concrete.  At a cut where the certificate
changes, splice the last unchanged implication path on one allocation to the
first changed path through `Z` on the other.  The required output is either
four literal anchored carriers (hence `K_7`) or the same independent equality
blocks in the two proper-minor states (hence a six-colouring).

This note proves the forced-path interface and the exact five switch types;
it does not yet prove that final transport lemma or infer a `K_5`-minor-free
remainder from a persistent boundary certificate.
