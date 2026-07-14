# A capacity transition at a support-four three-gate

**Status:** proved and independently audited.

This note strengthens the state-free part of the support-four three-cut
transition.  It explains the explicit `K_7` in the packet-collapse barrier,
closes every multi-lobe packet-collapse geometry by a reusable matching
principle, and isolates one exact two-lobe obstruction.  It does **not**
claim that the old equality state survives the descended boundary.

## 1. Literal setup

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
             \qquad |S|=7,                              \tag{1.1}
\]

be an actual separation in a seven-connected graph.  Assume:

1. `G[L]` is three-connected;
2. `P,Q subseteq R` are disjoint connected `S`-full packets joined by a
   literal edge; and
3. `H=G[S]` contains a spanning non-path tree, or is
   `K_{1,3} dotcup K_3`.

The third item is the audited connected-rich width-two boundary conclusion.
Let

\[
                         T=\{t_1,t_2,t_3\}              \tag{1.2}
\]

be a three-cut of `G[L]`, and call the components of `G[L]-T` the
**lobes**.  Every lobe meets every member of `T`.  If

\[
                         A(D)=N_S(D),                   \tag{1.3}
\]

then seven-connectivity gives `|A(D)|>=4` for every lobe.  The whole shore
`L` is `S`-full.

Fix a lobe `D_0` with

\[
                         A=A(D_0),\qquad |A|=4,         \tag{1.4}
\]

and put

\[
                         B=S-A,\qquad
                         \Omega=T\cup A.                \tag{1.5}
\]

The audited three-cut descent says that `Omega=N_G(D_0)` is an actual
seven-boundary and that `D_0` is a connected `Omega`-full shore strictly
smaller than `L`.

## 2. Why the packet-collapse barrier contains `K_7`

The following elementary lift is the reusable form of the barrier's
seven displayed bags.

### Lemma 2.1 (three-row outer-`K_4` lift)

Let `K_1,K_2,K_3` be pairwise disjoint connected sets which are pairwise
adjacent.  Let `W_1,...,W_4` be four further pairwise disjoint connected
sets, pairwise adjacent and disjoint from the `K_i`.  If

\[
                         E(K_i,W_j)\ne\varnothing
             \qquad(1\le i\le3,\ 1\le j\le4),          \tag{2.1}
\]

then these seven sets are a literal `K_7` model.

#### Proof

The `K_i` form a triangle, the `W_j` form a clique of order four, and
(2.1) supplies every cross adjacency.  All seven sets are connected and
pairwise disjoint.  \(\square\)

In the verified fourteen-vertex packet-collapse barrier, take

\[
 K_1=\{x,z_1\},\quad K_2=\{y,z_2\},\quad K_3=\{z_3\},   \tag{2.2}
\]

and

\[
 \{b_1\},\quad \{b_2\},\quad
 \{b_3,a_2,q\},\quad \{a_3,a_1,p\}.                  \tag{2.3}
\]

The lobe-to-gate edges make (2.2) a triangle.  The two boundary triangles,
the crossed boundary edges, packet fullness, and the literal `p-q` edge
make (2.3) a `K_4`.  Directly from the advertised portal lists, every bag
in (2.3) meets every bag in (2.2).  Lemma 2.1 therefore gives exactly the
displayed literal `K_7`; the failure of packet pullback in that example is
paid for by a rooted minor, not by an equality-state transition.

## 3. The gate-capacity graph

For every lobe `D` and gate vertex `t in T`, call `D` and `{t}`
**resources**, and define their supports by

\[
             \sigma(D)=A(D),\qquad \sigma(t)=N_S(t).    \tag{3.1}
\]

Construct a simple graph `C_T` as follows.

* Its real vertices are all lobes and the three literal gate vertices.
* For every lobe `D` with `|sigma(D)|>=5`, add one private dummy vertex
  `d_D` and the edge `D d_D`.
* For a lobe `D` and a distinct real resource `Z`, add `DZ` exactly when

  \[
                         |\sigma(D)\cup\sigma(Z)|\ge5. \tag{3.2}
  \]

There are no gate-gate edges.  A lobe-lobe edge is of course inserted only
once.  Dummy vertices have degree one.

### Lemma 3.1 (capacity matching gives a near-full carrier split)

If `C_T` has a matching of order two, then the real resources can be
partitioned into two classes whose unions `X,Y subseteq L` are connected
and adjacent, and satisfy

\[
        |N_S(X)|,|N_S(Y)|\ge5,
        \qquad N_S(X)\cup N_S(Y)=S.                    \tag{3.3}
\]

Consequently, under the setup of Section 1, a matching of order two gives
a literal labelled `K_7^vee` model.

Conversely, such a resource partition gives a matching of order two
provided **each resource class contains a lobe**.

#### Proof

Suppose first that `e_X,e_Y` are disjoint capacity edges.  Put the real
endpoints of `e_X` on one side and those of `e_Y` on the other; ignore a
dummy endpoint.  Each side already contains a lobe.  Each capacity edge
certifies support at least five on its side, either directly by (3.2) or
through a private dummy edge.

Give each side a gate vertex.  This is always possible: a capacity edge
uses at most one gate, the two edges use at most two of the three distinct
gates, and a side which already contains a gate needs no extra one.  Assign
all remaining real resources arbitrarily.  Every lobe meets every gate,
so each side is connected.  A lobe on either side meets a gate on the
other, giving a literal `X-Y` edge.  The two sides partition `L`, and `L`
is `S`-full, proving (3.3).

Conversely, suppose there is such a resource partition and each class
contains a lobe.  On either side choose a lobe `D`.  If
`|sigma(D)|>=5`, its private dummy edge witnesses capacity.  Otherwise
`|sigma(D)|=4`; since the union of the supports on that side has order at
least five, some other real resource `Z` on the same side has a support
element outside `sigma(D)`, and `DZ` is a capacity edge.  The two witnesses
are disjoint because the resource sides are disjoint (and dummies are
private), giving a matching of order two.

Finally, `X,Y,P,Q` satisfy every hypothesis of the audited two-defect
anchored near-model theorem: `X-Y` and `P-Q` are literal, `P,Q` are full,
the two thin supports have order at least five and cover `S`, and the
boundary has the required non-path tree or exceptional form.  That theorem
returns a literal labelled `K_7^vee`.  \(\square\)

Thus the barrier itself has a second, coarser explanation.  Its two lobes
have complementary four-supports, and two different gate vertices augment
the two lobes.  Those two disjoint capacity edges invoke Lemma 3.1.  The
explicit model in Section 2 is stronger (`K_7` rather than `K_7^vee`) and
records the precise rooted mechanism.

### Lemma 3.2 (the exact matching obstruction)

If `C_T` has no matching of order two, then its non-isolated part is a
star or a triangle.  It is not empty.

#### Proof

If `C_T` had no edge, no lobe would have support at least five.  Any two
lobe supports, both of order four, would be equal, since otherwise their
union would have order at least five.  Every gate support would be
contained in this common four-set.  The union of all resource supports
would then have order four, contrary to `S`-fullness of `L`.

A nonempty simple graph of matching number one is a star or a triangle.
Indeed, fix an edge `uv`.  Every edge meets it.  If all edges meet `u` or
all meet `v`, the graph is a star.  Otherwise there are edges `ux` and
`vy` with `x ne v` and `y ne u`.  They cannot be disjoint, so `x=y=w`.
Every further edge must meet all three edges of the triangle `uvw`, and
hence belongs to that triangle.  \(\square\)

This is a literal **matching** obstruction: all lobe-based, two-resource
witnesses for raising a four-support to five pass through one compulsory
lobe/gate, or through the three resources of one odd capacity triangle.
A gate-only carrier of support at least five is not encoded by `C_T`;
accordingly this statement is not a converse characterization of every
near-full carrier split.

## 4. Packet pullback at the descended boundary

Call a sibling lobe `J ne D_0` **self-full** when

\[
                         A\subseteq A(J).               \tag{4.1}
\]

For a non-self-full sibling put

\[
                         E(J)=A(J)\cap B.               \tag{4.2}
\]

Every such exit set is nonempty: `|A(J)|>=4`, while `J` misses a member
of the four-set `A`.

### Lemma 4.1 (exit matching)

The open shore opposite `D_0` behind `Omega` contains two disjoint
connected `Omega`-full packets unless one of the following holds.

1. `D_0` has exactly one sibling lobe.
2. There are at least two siblings, all are non-self-full, and for one
   `b in B`,

   \[
                         E(J)=\{b\}
              \quad\hbox{for every sibling }J.          \tag{4.3}
   \]

#### Proof

A self-full sibling is itself an `Omega`-full packet: it contacts `A` by
(4.1) and every gate vertex by three-connectivity.  If `J` is non-self-full
and `b in E(J)`, then for `F in {P,Q}` the set

\[
                         F\cup\{b\}\cup J              \tag{4.4}
\]

is connected and `Omega`-full.  The old packet supplies all contacts to
`A`, while the lobe supplies all contacts to `T`.

Two self-full siblings give two packets.  One self-full sibling and any
other sibling give two packets, using (4.4) for the latter when needed.
Two non-self-full siblings with distinct representatives in their exit
sets give the two disjoint packets

\[
 P\cup\{b_1\}\cup J_1,
 \qquad Q\cup\{b_2\}\cup J_2.                          \tag{4.5}
\]

For a family of at least two nonempty subsets of the three-set `B`, failure
to choose distinct representatives from two distinct members means that
every member is the same singleton.  This proves the dichotomy.  \(\square\)

### Lemma 4.2 (the common-exit obstruction has capacity two)

Outcome 2 of Lemma 4.1 forces a literal labelled `K_7^vee` model.

#### Proof

Choose two distinct siblings `J_1,J_2`.  Since they are non-self-full,
have support at least four, and meet `B` exactly in `{b}`, there are
`a_1,a_2 in A` such that

\[
                         A(J_i)=(A-\{a_i\})\cup\{b\}.
                                                               \tag{4.6}
\]

In particular `D_0J_1` is a capacity edge, because their support union is
`A union {b}`.

Choose `b' in B-{b}`.  The whole shore `L` is `S`-full.  No lobe contacts
`b'`: `D_0` has support exactly `A`, and (4.3) excludes `b'` from every
sibling.  Hence some gate vertex `t in T` contacts `b'`.  The pair
`J_2,t` is a capacity edge, since `A(J_2)` has order four and `b'` lies
outside it.  The edges

\[
                         D_0J_1,\qquad J_2t            \tag{4.7}
\]

are disjoint.  Lemma 3.1 gives the claimed near model.  \(\square\)

## 5. Combined transition and exact residue

### Theorem 5.1 (support-four capacity transition)

Under the setup of Section 1, at least one of the following holds.

1. `G` contains a literal labelled `K_7^vee` model.
2. At the strict descended boundary `Omega`, the open shore opposite
   `D_0` contains two disjoint connected `Omega`-full packets.
3. `G[L]-T` has exactly two lobes, and the capacity graph `C_T` has
   matching number one; its non-isolated part is a star or a triangle.

#### Proof

Apply Lemma 4.1.  Its generic outcome is item 2.  Its common-exit outcome
is item 1 by Lemma 4.2.  In its one-sibling outcome, Lemma 3.1 gives item
1 whenever `C_T` has a two-edge matching.  Otherwise Lemma 3.2 gives item
3.  \(\square\)

In the hypothetical-counterexample kernel, item 2 has packet vector, with
the strictly smaller `D_0`-shore first,

\[
                              (1,2)\quad\hbox{or}\quad(1,3). \tag{5.1}
\]

The audited adaptive-reflection theorem eliminates `(1,3)`.  Thus every
surviving item-2 descent is a strict packet-vector `(1,2)` transition.
This statement is deliberately state-free: it does not assert a common
demand-two state or pull the old paired state to `Omega`.

The two-lobe obstruction in item 3 has a completely explicit support
form.  Write `E` for the sibling lobe and `C=A(E)`.

### Lemma 5.2 (two-lobe star/triangle normal form)

In item 3 at least one of the following holds, after naming a star centre.
The two lobe-centred descriptions may both apply when the non-isolated
capacity graph consists of the single edge `D_0E`; no disjointness of the
four displayed normal forms is claimed.

1. **Gate star.**  `C=A`, both have order four, one gate is the unique
   resource which contacts `S-A`, and every other gate support is contained
   in `A`.
2. **`D_0`-star.**  `|C|=4`, `A union C=S`, and every gate support is
   contained in `C`.
3. **`E`-star.**  `A union C=S`, and every gate support is contained in
   `A` (here `|C|` may exceed four).
4. **Capacity triangle.**  `|C|=4`, `A ne C`, the non-isolated capacity
   graph is the triangle on `D_0,E,t` for one gate `t`, and every other
   gate support is contained in `A cap C`.

#### Proof

There are only the two lobe vertices `D_0,E`.  A capacity triangle cannot
contain two gates because gate-gate edges do not exist, and cannot contain
a dummy because dummies have degree one.  Hence it is exactly
`D_0,E,t`.  Neither lobe then has a dummy, so both supports have order
four; the lobe-lobe edge gives `A ne C`.  A different gate has no capacity
edge to either lobe, so its support lies in `A cap C`.  This is item 4.

Now suppose the capacity graph is a star.  Its centre is a real resource:
a dummy has degree one and, for a one-edge star, the real lobe endpoint may
be chosen as centre.

If the centre is a gate `t`, the lobe-lobe edge is absent, so `A=C`.
Neither lobe has a dummy, and every other gate has support inside `A`.
Since all resource supports cover `S`, the one gate `t` carries every
member of `S-A`.  This is item 1.

If the centre is `D_0`, the lobe `E` cannot have a dummy edge, so `|C|=4`.
Every gate support is contained in `C`, since otherwise it would make an
`E`-gate capacity edge not incident with the centre.  The lobe-lobe edge
must be present; without it, `A=C` and then no capacity edge or support
outside `A` could exist.  Fullness now gives `A union C=S`, proving item 2.

Finally let the centre be `E`.  Every gate support lies in `A`, since an
element outside `A` would give a `D_0`-gate edge.  The lobe-lobe edge is
present, and fullness gives `A union C=S`.  The private dummy of `E` is
allowed, so `C` may have order at least five.  This is item 3.  \(\square\)

### Lemma 5.3 (the gate-centred star is a forbidden five-cut)

Under the seven-connectivity hypothesis, item 1 of Lemma 5.2 cannot occur.

#### Proof

In the gate-star form both lobes have the common four-support `A`.  One
gate `t` is the unique resource which contacts `S-A`; every other lobe or
gate has all its boundary contacts in `A`.  Therefore

\[
                              A\cup\{t\}                \tag{5.2}
\]

separates the nonempty set `L-{t}` from the nonempty old shore `R`.
Indeed there is no `L-R` edge, and after deleting (5.2) no surviving
vertex of `L` has a neighbour in `S-A`.  The displayed separator has
order five, contradicting seven-connectivity.  \(\square\)

## 6. Trust boundary

The theorem closes an infinite family: every support-four three-cut with
at least three lobes either gives a labelled near model or gives a strict
packet-vector descent.  The only residue not disposed of by the
matching-and-exit proof is one two-lobe gate whose capacity matching graph
has one of the lobe-centred star or triangle support patterns in Lemma 5.2;
Lemma 5.3 removes the gate-centred star.  This does not assert that every
remaining star/triangle lacks some other carrier split or near model.

What remains is genuinely dynamic.  In item 2 the returned packet vector
does not by itself reproduce a legally attained low-demand or paired state.
In item 3 there may be only one `Omega`-full packet on the opposite shore.
A complete transition must therefore use a proper-minor colouring response
to either select a common state in item 2 or break the compulsory
star/triangle resource in item 3.  Neither assertion follows from fullness,
seven-connectivity, or the old attained state alone.
