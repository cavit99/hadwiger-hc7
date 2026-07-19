# Independent audit of the split-aligned joint-deletion theorem

**Verdict:** **GREEN** for the complete source file: Theorem 2.1,
Corollary 2.2, Propositions 3.1--3.3, and Corollaries 4.1--4.2 at the exact
source revision identified below.

**Audited source:** `results/hc7_split_aligned_joint_deletion.md`, SHA-256

```text
4aaff1e806bfbcd56c59b8e5d9647fc182104328c35439e3d3735559ab06f62b
```

After the GREEN audit of source revision
`568b711f83feeda676ef929e504852650ff4265f8d8ab2669ef2cf2f6dcfd677`,
the file was moved from `active/` to `results/` and only its status line
was changed to link this audit.  The mathematical statement and proof are
unchanged; the hash above pins the promoted source.

This is a separate internal mathematical audit, not external peer review.
The proof was reconstructed against the three cited GREEN inputs.  The audit
checked the spanning-tree split, every adjacency in the displayed `K_7`
model, both full-neighbourhood separations, the two deletion-capacity cases,
the closed-shore response orientation, the nested full-neighbourhood descent,
the minimum oriented interface, and both colouring corollaries.  No unproved
correspondence between palette colours and branch-set labels is used.

The cited dependency revisions are:

```text
2f413fa679fc7366920b9adbd1cdc9c419e7f2ff26c871ba8757ce2d8510c409  results/hc7_deficient_singleton_joint_persistence.md
d146edf7783d6f29750d634ac3d224da14bdd83dd91170011293ece177240d64  results/hc7_two_mark_branch_set_split.md
21b5fd5c523efb673ca11b0e604e0e81d173a5dbda677baa235efd8924d4b865  results/hc7_joint_persistent_incident_colour_fork.md
```

## 1. Hypotheses and neighbour multiplicities

The seven displayed branch sets partition `V(G)`.  Since `{x}` and `D` are
the sole nonadjacent pair of branch sets, `x` has no neighbour in `D`, has at
least one neighbour in every `U_i`, and has no neighbour outside the five
sets `U_i`.  Consequently

\[
 d_G(x)=\sum_{i=1}^5 |N_G(x)\cap U_i|.
\]

Seven-connectivity gives `d_G(x)>=7`, so some multiplicity `n_i` is at
least two.  These are exactly the hypotheses needed for the tree split and
for the subsequent deletion-capacity argument.  Spanningness and the
singleton condition are both essential and are stated explicitly.

## 2. The marked spanning-tree split

Fix `rho in M_i=N_G(x) cap U_i`.  In a spanning tree of `G[U_i]`, the
minimal subtree containing `M_i` is nontrivial.  Every leaf of that minimal
subtree is a terminal in `M_i`, and at most one leaf is `rho`; hence it has a
leaf `m in M_i-{rho}`.

Removing the edge of the minimal subtree incident with `m` from the full
spanning tree gives two nonempty connected vertex sets `Z,W`, joined by the
removed tree edge, with `m in Z` and `rho in W`.  The component on the
`m`-side contains no other vertex of the minimal terminal subtree.  Any
branches of the full tree attached on that side contain no terminal either.
Therefore

\[
 M_i\cap Z=\{m\},\qquad M_i-\{m\}\subseteq W.
\]

In particular, both `Z` and `W` are adjacent to the singleton `{x}`.  This
verifies the only delicate assertion in the tree split; no terminal is lost
in an unexamined branch of the spanning tree.

## 3. Explicit `K_7`-minor model

Suppose `Z` is adjacent to `D` and `W` is adjacent to each of the four
remaining common branch sets `V_1,...,V_4`.  The proposed seven branch sets
are

\[
 \{x\},\quad D\cup Z,\quad W,\quad V_1,V_2,V_3,V_4.
\]

They are disjoint and connected: `D union Z` is connected through a `DZ`
edge, while all other sets were already connected.  Their adjacencies are
exhaustively supplied as follows.

- `{x}` meets `D union Z` through `xm` and meets `W` through `x rho`.
- The removed tree edge joins `D union Z` to `W`.
- `D` supplies every adjacency from `D union Z` to a set `V_k`.
- The hypothesis on `W` supplies every `W-V_k` adjacency.
- The sets `V_k` are pairwise adjacent in the original labelled model.

Thus every one of the 21 required branch-set adjacencies is present, and the
displayed family is an explicit `K_7`-minor model.

## 4. Full-neighbourhood separation alternatives

If the explicit model is unavailable, the two cases in the proof are
exhaustive.

- If `Z` is anticomplete to `D`, then `D` is disjoint from
  `Z union N_G(Z)`.  Hence `N_G(Z)` separates the nonempty connected side
  `Z` from a nonempty opposite side containing `D`.
- Otherwise `Z` meets `D`, so failure of the explicit model means that `W`
  is anticomplete to some `V_k`.  Then `N_G(W)` separates the nonempty
  connected side `W` from a nonempty opposite side containing `V_k`.

In either case the selected set `L` is nonempty, proper, and connected, and
`S=N_G(L)` is the literal full boundary of an actual separation.  Since
`a in L` is adjacent to `x`, the vertex `x` belongs to `S`.  The proof does
not claim an upper bound on `|S|`; seven-connectivity supplies only
`|S|>=7`.

## 5. Joint deletion capacity in both multiplicity cases

When `n_i>=3`, the split has one `x`-neighbour `m` in `Z` and at least two
in `W`.

- For `L=Z`, delete `xm` and one edge from `x` to `M_i cap W`, retaining a
  second edge to `M_i cap W`.
- For `L=W`, delete one edge from `x` to `M_i cap W` and delete `xm`, again
  retaining another edge to `M_i cap W`.

Thus one deleted outer end lies in `L`, the other lies outside `L`, and the
required `x-U_i` adjacency survives.  No other model adjacency is affected.

When `n_i=2`, the degree identity gives

\[
 \sum_{j\ne i}n_j\ge5.
\]

Among four positive integers, one is therefore at least two.  Choose the
second deleted edge in that branch set `U_j`, retaining another `x-U_j`
edge.  The member of `M_i` opposite `L` retains the `x-U_i` adjacency.
Again the two outer ends lie on opposite sides of `L`, and the same labelled
near-complete model survives after both deletions.  These constructions
agree exactly with the audited deficient-singleton capacity criterion.

## 6. Parameter-uniform corollary

Corollary 2.2 uses the same proof with `t-2` common branch sets.  In a
spanning labelled `K_t`-minus-one-edge model with singleton endpoint `{x}`,
minor exclusion makes `x` anticomplete to the deficient branch set and the
model requires a positive multiplicity at every common label.  Therefore

\[
 \sum_{i=1}^{t-2}n_i=d_G(x)\ge t.
\]

Some `n_i` is at least two.  The minimal-terminal-subtree split then has
exactly the same two separator alternatives; in the remaining case the
sets

\[
 \{x\},\quad D\cup Z,\quad W,
 \quad V_1,\ldots,V_{t-3}
\]

are `t` disjoint connected pairwise adjacent branch sets.  The adjacency
verification in Section 3 is independent of the number of untouched common
branch sets.

If `n_i>=3`, the same-bag deletion leaves one `x-U_i` edge.  If `n_i=2`,
then

\[
 \sum_{j\ne i}n_j\ge t-2
\]

over exactly `t-3` positive summands.  Since `t>=4`, at least one of them is
at least two, and the second-bag deletion again preserves both required
singleton adjacencies.  Finally, a full neighbourhood separating two
nonempty sides has order at least `t` in a `t`-connected graph.  Thus the
parameter-uniform corollary introduces no unproved colouring or
label-allocation assumption.

## 7. Closed-shore response orientation

Let `C=G[L union S]` and `O=G-L`.  Since `S=N_G(L)`, these induced graphs
cover every vertex and edge of `G`, meet exactly in `G[S]`, and have no edge
between their open sides.

The edge `e=xa` lies in `C` and not in `O`.  If `b notin S`, then
`b notin L union S`, so `f=xb` lies in `O` and not in `C`.  A colouring of
`G-e` restricts to the unchanged graph `O`.  If the same equality partition
on `S` extended through `C`, a permutation of the six colour names would
align the two boundary colourings and glue them to a six-colouring of `G`.
This is impossible.  Therefore

\[
 Resp(e,S)\subseteq Ext(O,S)-Ext(C,S).
\]

The symmetric argument gives the stated inclusion for `Resp(f,S)`.  The two
set differences are disjoint.  Equality partitions, rather than named
colour assignments, are sufficient for the gluing argument because the
bijection between used boundary colours extends to a permutation of the
six-colour palette.

If `b in S`, both ends of `f` lie in the common boundary.  Deleting `f`
changes the boundary graph in both closed shores, so the unchanged-shore
argument is genuinely unavailable.  The theorem correctly records this as
the boundary-pinch alternative rather than applying the clean orientation
illegitimately.

## 8. Nonadjacent outer ends

When `ab` is absent, contracting the two-edge star on `x,a,b` and expanding
a minor colouring gives the exact trace

\[
 \kappa(x)=\kappa(a)=\kappa(b)=\alpha,
 \qquad N_G(x)\cap\kappa^{-1}(\alpha)=\{a,b\}.
\]

The cited incident-edge fork then yields either an edge saturated for all
five alternate colours or the named two-component bypass.

If `xa` is saturated, orient each bichromatic path from `a in L` to
`x in S`.  Its first vertex outside `L` lies in `N_G(L)=S`, and all earlier
internal vertices lie in `L`.  Two paths with distinct alternate colours
can share a first-entry vertex only if that vertex has the common colour
`alpha`.

If `xb` is saturated, let `R_b` be the component of `G-S` containing `b`.
The clean placement puts `b` in such an open component and puts `x` in `S`.
Orienting each bichromatic path from `b` to `x`, its first vertex outside
`R_b` belongs to `S`, since every edge leaving a component of `G-S` enters
`S`.  The preceding internal vertices lie in `R_b`, and the same palette-
intersection argument proves the stated collision rule.  Thus both possible
saturated orientations have a literal first-entry interpretation, although
neither conclusion identifies those entries with five distinct branch-set
labels.

In the bypass case, the path starts in `L`, ends at
`b notin L union S`, and avoids `x`, so its first exit lies in `S-{x}`.
The component containing `a` gives a colouring of `G-f`, while the component
containing `b` gives a colouring of `G-e`, exactly as in the cited GREEN
bypass theorem.  Their boundary partitions lie in the two opposite set
differences above and hence are distinct.  No stronger label assignment is
inferred.

## 9. Adjacent outer ends

When `ab` is an edge, every colouring of the common-deletion graph has
exactly one of the two signatures `(equal,proper)` and `(proper,equal)`.
Both classes are nonempty by the two one-edge contractions.  A colouring in
the first class restores `f` and is a colouring of `G-e`; a colouring in the
second restores `e` and is a colouring of `G-f`.  Proposition 3.1 therefore
places their boundary equality partitions in the two opposite, disjoint
extension differences exactly as stated.

If the two classes occupy different Kempe-reconfiguration components, the
source stops.  Otherwise a first transition between them is one interchange
on the connected bichromatic subgraph supplied by the cited critical-
triangle theorem.  If that subgraph avoided `S`, the two colourings would
agree on every boundary vertex and induce the same equality partition,
contradicting the disjoint extension differences.  Thus it meets `S`.
Likewise, an interchange which only permuted whole boundary colour blocks
would preserve the equality partition and is excluded.  The transition
therefore changes the complete labelled equality partition on `S`.

The remaining saturation, separation, and dominating-core conclusions are
quoted without strengthening from the GREEN incident-edge theorem.  In
particular, agreement of the two responses on the full neighbourhood of a
nondominating transition component is not claimed to colour both original
closed shores.

## 10. Trust boundary

The audited theorem proves a host-level alignment of two choices which were
previously independent: the connected branch-set split and a common
model-preserving deletion of two incident edges.  In the clean placement it
also locates the two one-edge response languages on opposite closed shores
and gives literal first-entry information.

It does **not** prove any of the following:

1. that the second deleted edge avoids the new boundary;
2. that the two critical-triangle response classes share a Kempe component;
3. that first hits are injectively assigned to the five named common branch
   sets;
4. that the returned full neighbourhood has order exactly seven;
5. that one complete equality partition extends through both original
   closed shores;
6. that a strict label-preserving full-neighbourhood descent exists; or
7. that `HC_7` is proved.

These limitations are stated accurately in the source.  No gap remains
inside the theorem, parameter-uniform corollary, three propositions, or two
colouring corollaries at the audited source hash.

## 11. Response-preserving nested descent

Assume the clean placement, so `b` lies outside `L union S`.  Since
`S=N_G(L)`, the connected set `L` is a component of `G-S`.  Let `R_b` be
the distinct component containing `b` and put `S_b=N_G(R_b)`.

Every edge leaving a component of `G-S` enters `S`; hence

\[
                              S_b\subseteq S.
\]

The edge `xb` has one end in `R_b`, so `x in S_b`.  The set `L` is disjoint
from both `R_b` and `S_b` and remains nonempty after `S_b` is deleted.
Consequently `R_b` and a side containing `L` are distinct nonempty open
sides of the full-neighbourhood separation with boundary `S_b`.  If
`S_b` is not all of `S`, this boundary has strictly smaller cardinality;
seven-connectivity gives only the lower bound `|S_b|>=7`.

For

\[
 C_b=G[R_b\cup S_b],\qquad O_b=G-R_b,
\]

the edge `f=xb` belongs to `C_b` and not to `O_b`.  The edge `e=xa`
belongs to `O_b` and not to `C_b`, because `a in L` and
`L cap (R_b union S_b)` is empty.  Thus a colouring of `G-f` restricts to
the unchanged graph `O_b`.  Were its equality partition on `S_b` also in
`Ext(C_b,S_b)`, a colour permutation would align the two boundary
colourings and glue them to a six-colouring of `G`.  This proves

\[
 Resp(f,S_b)\subseteq Ext(O_b,S_b)\setminus Ext(C_b,S_b).
\]

The identical argument with the two sides and the edges interchanged gives
the asserted orientation for `Resp(e,S_b)`.  The operation has not changed
either deleted edge or the global graph `G-{e,f}`; therefore the labelled
near-complete model already present in that graph remains present.  Nothing
in this argument asserts that the new boundary respects the old branch-set
partition.

## 12. Minimum oriented interface

The initial boundary `S` is oriented for `(e,f)`: it contains `x`, while
`a in L` and `b in R_b` lie in distinct components of `G-S`.  Hence a
minimum-order oriented vertex set `T` exists.  Let `A_T,B_T` be the
components of `G-T` containing `a,b`, respectively.

Because `A_T` is a component of `G-T`, its full neighbourhood is contained
in `T`.  The edge `xa` puts `x` in `N_G(A_T)`.  If this inclusion were
proper, then deleting `N_G(A_T)` would leave the connected set `A_T` as a
component.  The vertex `b` is outside `T`, hence outside the subset
`N_G(A_T)`, and it is not in `A_T`.  Therefore `N_G(A_T)` would itself be
an oriented set of smaller order, contrary to the choice of `T`.  Thus

\[
                         N_G(A_T)=T.
\]

The symmetric argument using `xb` gives `N_G(B_T)=T`.  This proves that
both named endpoint components are adjacent to every literal vertex of one
common interface; it does not assert that any other component is full to
that interface.

For the `A_T`-side, `e` is present only in `G[A_T union T]`, whereas `f`
is present only in the unchanged opposite graph `G-A_T`.  A colouring of
`G-e` restricts to that unchanged opposite graph, and extension of its
boundary partition through the original `A_T`-side would glue to a
six-colouring of `G`.  This gives the first line of (3.6).  Replacing
`A_T,e` by `B_T,f` gives the second.  The two orientations therefore
survive minimization without requiring that `T` be a subset of `S`.

Since the two endpoint components are nonempty, `T` is an actual separator;
seven-connectivity yields `|T|>=7` and no upper bound.  The same named edges
remain jointly model-preserving because the labelled model is a global
model in the unchanged graph `G-{e,f}`.  The proof does **not** claim that
`T` preserves individual branch sets, supplies a common full boundary
partition, has order exactly seven, or already closes the clean branch.
