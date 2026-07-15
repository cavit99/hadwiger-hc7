# Full packets force a rooted connected minor

**Status:** proved and independently audited.

This is a uniform bridge from packet capacity to rooted-minor structure.
It supplies an existential labelled connected core for a packet-rich
closed shore without merging any literal boundary vertices.  It does not
make that core canonical, and it does not assert that the core is
nonplanar or contains the three duty-correct carriers required for
exact-state reflection.

## 1. Root connectivity supplied by packets

Let `J` be a finite graph and let `S subseteq V(J)`.  A connected subgraph
`P subseteq J-S` is **`S`-full** when every literal vertex of `S` has a
neighbour in `P`.

An **`S`-separator** is a set `X subseteq V(J)` such that at least two
components of `J-X` contain vertices of `S`.  Write `kappa_J(S)` for the
largest integer at most `|S|-1` such that every `S`-separator has at least
that order.  Put `H=J[S]` and `r=kappa_H(S)`.  Thus `r=0` when the literal
boundary is disconnected, `r>=1` when it is connected, and `r>=2` when it
is two-connected.

### Theorem 1.1 (packet-to-root-connectivity)

If `J-S` contains `q>=1` pairwise vertex-disjoint connected `S`-full
packets, then

\[
                 \kappa_J(S)\ge \min\{q+r,|S|-1\}.       \tag{1.1}
\]

### Proof

Let `X` be any `S`-separator of `J`.  It must meet every packet.  Indeed,
if a packet `P` were disjoint from `X`, it would remain connected in
`J-X`, and every surviving root `s in S-X` would retain an edge to `P`.
All surviving roots would lie in one component, a contradiction.  Since
the packets are disjoint and lie outside `S`,

\[
                            |X-S|\ge q.                  \tag{1.2}
\]

Moreover, `X cap S` is an `S`-separator of `H`: roots in different
components of `J-X` cannot be joined by a path in the subgraph
`H-(X cap S)`.  Hence `|X cap S|>=r`.  If `H` has no `S`-separator, the
same observation says that `J` has none either, and the conclusion is
immediate.  Otherwise

\[
                |X|=|X-S|+|X\cap S|\ge q+r.             \tag{1.3}
\]

Applying the defining cap `|S|-1` proves (1.1). \(\square\)

Both summands are necessary.  If `S` is independent, then `r=0`; taking
exactly `q` independent vertices adjacent to every root gives singleton
full packets, and deleting all of them separates the roots.  When `H` is
connected, `r>=1` recovers the earlier `q+1` bound.

## 2. Rooted-minor corollary

Boehme--Harant--Kriesell--Mohr--Schmidt prove the following theorem for
`k in {1,2,3,4}`: if `kappa_J(S)>=k`, then `J` has a `k`-connected
`S`-minor; for `k<=3` it has a `k`-connected **topological** `S`-minor.
Here an `S`-minor is obtained by `S`-legal contractions and has a minor
certificate in which every bag contains at most one literal vertex of `S`
and all vertices of `S` are retained.

### Corollary 2.1 (the packet hierarchy)

Under Theorem 1.1, put

\[
                k=\min\{q+r,4,|S|-1\}.
\]

Then `J` has a `k`-connected `S`-minor.  If `k<=3`, it may be chosen as a
topological `S`-minor.  In particular, for a connected literal
seven-boundary:

* one full packet gives a 2-connected topological `S`-minor;
* two disjoint full packets give a 3-connected topological `S`-minor; and
* three disjoint full packets give a 4-connected `S`-minor.

If the literal seven-boundary is two-connected, then already two disjoint
full packets give a 4-connected `S`-minor.

### Proof

The value of `k` is at most four and Theorem 1.1 gives
`kappa_J(S)>=k`.  Apply Theorem 3 of the cited paper, using its topological
conclusion when `k<=3`. \(\square\)

Primary source: T. Boehme, J. Harant, M. Kriesell, S. Mohr and
J. M. Schmidt, *Rooted Minors and Locally Spanning Subgraphs*, Journal of
Graph Theory 105 (2024), 209--229, doi:10.1002/jgt.23012, Theorem 3.

## 3. Exact `HC_7` specialization

For an actual oriented exact-seven `(1,2)` separation

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad (\nu_L^S,\nu_R^S)=(1,2),             \tag{3.1}
\]

assume, as in the active connected-boundary cell, that `G[S]` is
connected.  Choose two disjoint connected `S`-full packets in `R` and put

\[
                            J=G[R\cup S].                 \tag{3.2}
\]

Corollary 2.1 gives a 3-connected topological `S`-minor wholly inside the
rich closed shore.  All seven boundary labels survive as distinct vertices
of its subdivision.  Thus arbitrary portal multiplicities admit an
existential reduction to a labelled 3-connected core before applying a
rooted linkage or web theorem.  The core is not canonical and need not be
disjoint from either packet.

In the two-connected-boundary subcell, the same two packets instead give a
4-connected `S`-minor.  This stronger minor need not be topological, and
the reservation and state-selection limitations below still apply.

This is compatible with the global thin-shore rank: the construction does
not change the packet-one shore `L`.  It is also compatible with a
shore-confined minor operation in the following limited sense: every
`S`-legal contraction used by the rooted-minor certificate lies in
`R union S` and does not merge two literal boundary labels.

If the certificate uses a genuine deletion or contraction, perform it in
`G` while leaving `G[L union S]` untouched.  In a minor-minimal `HC_7`
counterexample the resulting proper minor has a six-colouring.  Its
restriction to `G[L union S]` is proper and therefore induces an exact
partition of the literal boundary while the rooted core exists on the
other side.  This couples the core to **some** legal returned state.  It
does not force the previously attained paired-triangle state, nor does it
make the colour blocks into connected, correctly labelled carriers.

## 4. Trust boundary

The theorem does **not** close the `(1,2)` state problem.

1. A 3-connected rooted torso may be planar.  Its four-terminal failures
   are precisely web/rural phenomena rather than contradictions.
2. Even in a nonplanar core, a rooted `K_4` model selected at four boundary
   vertices may use the other three literal boundary vertices internally.
   The cited theorem does not reserve them for packet bags.  This failure
   occurs already in the edge-minimal four-connected graph
   `K_1 join K_{3,3}` when all seven vertices are declared roots: it is
   nonplanar, but a `K_4` model avoiding three roots would have four
   singleton branch sets, whereas the graph has clique number three.
3. Nor does the theorem reserve the full packets.  Let `J[S]=P_7` and add
   three independent vertices, each adjacent to every root.  They are
   three disjoint singleton full packets and Theorem 1.1 gives
   `kappa_J(S)>=4`, but deleting their interiors leaves only `P_7`, so no
   rooted `K_4` can be built while keeping all three packets disjoint for
   the packet lift.
4. A genuine confined certificate does give the weak state--geometry
   coupling described above.  If the certificate is the identity, however,
   no proper operation has occurred.  More importantly in either case,
   rooted-minor minimality does not select a canonical core, a prescribed
   returned partition, or a transition-compatible packet duty.
5. Three-connectivity does not imply that an arbitrary demand-three
   partition of `S` is knitted.  A stateful carrier-or-rural dichotomy is
   still required.

The precise next uniform target is therefore: after fixing one labelled
3-connected core supplied by (3.2), turn the actual attained demand-three
state into three duty carriers or into one rural order compatible with the
opposite proper-minor response.  The result here supplies a domain on which
that theorem may operate; it is neither a canonical global state nor that
theorem itself.
