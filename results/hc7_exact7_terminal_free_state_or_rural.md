# Side-terminal-free state-or-rural theorem

**Status:** proved and independently audited.  This removes the
endpoint-transfer and side-terminal defects which
prevented an arbitrary spanning set-terminal cross from being used as a
supported decoration rotation.

## 1. Exact terminal-free shore

Work in one side of the exact-order-six Moser cell.  Let `D_t` be its
connected open shore, `t` its side terminal, and

\[
                         J^\circ=G[D_t\cup U].                    \tag{1.1}
\]

Thus `v,w,t` are omitted.  The graph `J^circ` is connected because every
member of `U` belongs to `N(D_t)`.  Put

\[
                         Z=V(D_t)\cup\{x,y\}.                    \tag{1.2}
\]

For every nonempty `C subseteq Z-\{x,y\}`, exact shore anticompleteness
and `N(v)=S` give

\[
                         N_G(C)-V(J^\circ)\subseteq\{w,t\}.      \tag{1.3}
\]

Hence the exposure hypothesis of the audited spanning-rural theorem holds.

Let `K_0,A,B` be the supported pair-carrier core: `K_0` has trace
`{x,y}`, while the traces of `A,B` partition `U-\{x,y\}`.  Let `L` be
one connected locked region, put `W=\{w\}\cup L`, and assume that `W`
supports the pair-carrier decoration; in particular `w` is adjacent to
`L` and `\{w,x,y\}` is independent.  Also assume

\[
 E(L,A\cup B)=empty,\qquad
 |(N(L)\cap K_0)-\{x,y\}|\ge3,\qquad
 |N(A\cup B)\cap(K_0-\{x,y\})|\ge3.               \tag{1.4}
\]

The exact five-attachment/three-bypass branch supplies these inherited
non-root bounds.

## 2. A labelled partition of the target pole

### Lemma 2.1 (endpoint-faithful target partition)

Let `X` be a connected graph containing disjoint connected adjacent sets
`A,B`.  For every `u in X`, there is a partition

\[
                         V(X)=A'\mathbin{\dot\cup}B'             \tag{2.1}
\]

into connected adjacent sets with `A subseteq A'`, `B subseteq B'`; in
particular `u` belongs to one named side.  If all adhesion vertices of `X`
already belong to `A union B`, the two traces are unchanged.

#### Proof

Contract `A` and `B` separately, retain one literal edge between the two
contracted vertices, and choose a spanning tree containing that edge.
Delete the edge.  Its two tree components lift to connected sets `A',B'`
covering `X` and containing the corresponding original block.  The vertex
`u` lies in one of them.  The retained literal edge has one end in each
lifted set, so `A'` and `B'` remain adjacent.  No adhesion vertex changes
side because every such vertex was already in one of the two fixed blocks.
\(\square\)

## 3. Uniform state-or-rural conclusion

### Theorem 3.1 (terminal-free endpoint transfer)

Under the hypotheses of Section 1, at least one of the following occurs.

1. **State-faithful promotion.**  A connected enlargement `W'` of the
   original decorated set `W`, with the same adhesion trace `{w}`, has
   literal contact with two named core blocks.  Hence an admissible
   rank-two state is attained, or the corresponding literal
   boundary-incompatibility certificate occurs.
2. **Exact named rotation.**  There is a trace-preserving core on this
   side in which every contact supplied by the enlarged locked region
   `Y` has moved from the pair carrier to one named target block.  A
   direct `w`--carrier edge may survive, but the same named supported
   state is attained whenever its unchanged trace is admissible.
3. **Low carrier cut.**  The component-absorbed spanning pair carrier has
   a cut of order at most two.
4. **Terminal-free rural page.**  There is a spanning partition

   \[
                   V(J^\circ)=K\mathbin{\dot\cup}X
                                      \mathbin{\dot\cup}Y       \tag{3.1}
   \]

   such that `K,X,Y` are connected, `X,Y` are anticomplete, `K` has trace
   `{x,y}`, and the simple quotient obtained by contracting `X,Y` is a
   planar rib with frame `(x,alpha,y,beta)`.

The first two outcomes are fully label-faithful at the level of the
attained boundary state and avoid the side terminal `t`; outcome 4 contains
every vertex of `J^circ` (and deliberately contains neither `w` nor `t`).

#### Proof

First inspect the components of `J^circ-V(K_0)` containing
`A union B` and `L`.

If they are the same component, choose a shortest `(A union B)-L` path in
that component.  Its interior avoids all three core blocks and `L`.  It
also contains no vertex of `U`: every member of `U` already lies in one of
the three core traces.  Absorb the path, except its final vertex in `L`,
into the target block at its first end.  This preserves the target trace
and gives it a literal edge to `L`, while `L` retains its old contact with
`K_0`.  This is outcome 1 (subject only to the already-audited
admissibility check on the unchanged target trace).

Assume the two components are distinct and call them `X,Y`, respectively.
Absorb every other component of `J^circ-V(K_0)` into `K`; the component-
absorption lemma makes `(K,X,Y)` a spanning two-pole triple.  No additional
root of `U` enters `K`, and the old contacts in (1.4) give

\[
                         |Q(K,X)|,|P(K,Y)|\ge3.                  \tag{3.2}
\]

Apply the audited spanning-rural quadrichotomy using (1.2)--(1.3).  Its
low-connectivity outcome is outcome 3 here, and its planar outcome is
outcome 4.

Suppose it returns a shared portal `q in Q(K,X) cap P(K,Y)`.  Apply
Lemma 2.1 to `X`, choosing the side containing an `X`-neighbour of `q` as
the named target `A'`.  Put

\[
                         L'=Y,\qquad W'=\{w\}\cup Y.             \tag{3.3}
\]

The set `W'` is connected because `Y` contains `L`, and it avoids `t` by
construction.  Its carrier-neighbour set is the whole set `P(K,Y)`, so
`q` is simultaneously a marked attachment and a literal portal to `A'`.
The audited three-connected pair-carrier peel applies (unless outcome 3
already holds), giving contact with both the retained pair block and
`A'`.  This is outcome 1.

We may now assume that the shared-portal outcome is absent, so `Q(K,X)`
and `P(K,Y)` are disjoint.  Finally suppose the quadrichotomy returns an
`x-y | q-p` set-terminal cross.  Partition `X` by Lemma 2.1 so that the
`X`-neighbour of `q` lies in a named target `A'`, and again use (3.3).  Now

\[
                         p\in P(K,Y)=N(Y)\cap K                  \tag{3.4}
\]

is an **actual attachment of the chosen locked region `L'=Y`**, not merely
an endpoint seeing `Y-L`.  Disjointness of the two portal sets also gives
`q notin P(K,Y)`, as required by the local cross theorem.  The spanning
carrier and both target blocks avoid `t`.  Therefore the audited
set-terminal cross-rotation theorem applies with `L'`: it gives either the
label-faithful peel of outcome 1 or the exact named rotation of all
`Y`-based contacts in outcome 2.  This exhausts the quadrichotomy.
\(\square\)

## 4. Remaining exact gap

The endpoint-transfer and side-terminal duties are no longer gaps **at the
level of the attained decorated state** in the shared-portal or
set-terminal-cross branches.  A literal endpoint at the originally chosen
subregion `L` need not exist; replacing `L` by its whole component `Y` is
the trace-preserving normalization.  A survivor on this route is now
confined to:

* a literal carrier cut of order at most two; or
* a planar two-pole quotient spanning the entire side after deletion of
  its one side terminal.

For the second branch, the audited tree-pole theorem converts a failed
connector rotation to two alternating literal carriers, and the audited
rooted-`K_4` refinement converts the distinct-end case to a rooted
`K_4` subdivision.  What remains is induced-pole expansion (plus
reinsertion of `t`) or conversion of that rooted duty object/collision to
the bilateral state, `K_7`, or fixed-pair outcome.
