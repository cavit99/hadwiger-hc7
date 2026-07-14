# Atomic near-full two-carrier state exchange

**Status:** proved and independently audited.

This theorem closes every pair of adjacent near-full carriers rooted at the
compulsory vertex `z`; the carriers need not span the thin shore.  In
particular it closes the entire clean-edge branch of the rooted path/`Y`
bridge-hull milestone.  The same-parity two-list obstruction is not a live
residue: in the connected bipartite frontier, one named proper-minor
response returns a demand-at-most-two state; in the exceptional frontier,
the untouched boundary triangle gives a literal `K_7` model.

## 1. Setup

Use the atomic exact-seven separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where:

1. `G` is seven-connected, `K_7`-minor-free, is not six-colourable, and
   every proper minor is six-colourable;
2. there is no `A-R` edge;
3. `A` is connected and `S`-full;
4. `zu` is the unique `A-u` edge; and
5. `R` contains two disjoint adjacent connected `S`-full packets.

Suppose `X,Y subseteq A` are vertex-disjoint, nonempty, connected and
adjacent, with `z in X`, and

\[
                 |N_S(X)|\ge6,\qquad |N_S(Y)|\ge6.       \tag{1.1}
\]

No spanning assumption `X union Y=A` is made.  Fix one literal `X-Y` edge.

## 2. The theorem

### Theorem 2.1 (near-full rooted carriers close)

Under the setup above, the two carriers cannot occur in a hypothetical
counterexample.  More precisely:

1. if `G[S]` is connected and bipartite, the two rich packets and one
   named contraction supported by `X,Y` six-colour `G`; and
2. if `G[S]=K_{1,3} dotunion K_3`, either the audited two-carrier list
   state six-colours `G`, or the carriers and the literal triangle give a
   literal `K_7` model.

#### Proof

Give every vertex of the audited bipartite frontier `F` its literal list
of contacts with `X,Y`.  The support bounds leave at most one vertex absent
from each carrier.  The carrier `X` contains `z` and therefore contacts
`u`, while `Y` cannot contact `u` because `zu` is the unique `A-u` edge.
Thus `Y` has singleton defect `{u}`; the defect of `X` is empty or a
different singleton.  In particular every list is nonempty.

The audited exact two-list theorem closes unless the two defects are
distinct vertices in the same bipartition side of the same component of
`F`.  Assume this sole obstruction occurs.  Since `z in X` and `zu` is the
unique `A-u` edge, the carrier `Y` misses `u`.  Hence its singleton defect
is exactly `u`.  Write the other defect as `p`; thus

\[
       S-N_S(X)=\{p\},\qquad S-N_S(Y)=\{u\},            \tag{2.1}
\]

where `p,u` lie in the same bipartition side of one component of `F`.

First suppose `H=G[S]` is connected and bipartite.  Write its bipartition
as

\[
                         S=I\mathbin{\dot\cup}J,
                 \qquad p,u in I.                      \tag{2.2}
\]

Both `I-{p}` and `J` are nonempty: the first contains `u`, while the
connected boundary has a nonempty opposite class.  The literal sets

\[
          Z_X=X\cup(I-\{p\}),\qquad Z_Y=Y\cup J          \tag{2.3}
\]

are disjoint and connected.  Indeed, `X` contacts every member of
`I-{p}`, and `Y` contacts every member of `J` because its only defect is
`u in I`.  They are adjacent through the fixed literal `X-Y` edge.

Contract a spanning tree of each set in (2.3).  This is a proper minor:
both sets contain thin-shore vertices and the nonempty rich shore remains
untouched.  Let `x,y` be the two contracted representatives, and take a
proper six-colouring of the minor.  The edge `xy` gives different colours,
and (2.1) gives a literal `p-Y` edge, so `p` has a colour different from
`y`.  There is no `p-X` edge and no edge from `p` to `I-{p}`, because
`p in I` and `I` is independent.  Thus `p` is nonadjacent to `x` in the
minor.

Restrict the minor colouring to `G[R union S]`, expanding the colour of
`x` over `I-{p}` and the colour of `y` over `J`.  Its exact equality
partition on `S` is therefore one of

\[
                         I\mid J,
        \qquad (I-\{p\})\mid\{p\}\mid J.               \tag{2.4}
\]

In the first case there are two blocks.  In the second there are three
blocks and `{p}` is a literal singleton block.  Hence in both cases the
packet demand of the returned partition is at most two.

Apply exact packet reflection to this *actual returned state* using the
two disjoint full packets in `R`.  It produces a proper colouring of the
intact thin closed shore with exactly the same boundary partition.  Align
the colours of corresponding blocks and glue the two closed-shore
colourings over `S`.  This six-colours `G`, a contradiction.

Now suppose

\[
                         H=K_{1,3}\mathbin{\dot\cup}K_3.
\]

Retain one triangle vertex as in the audited clique-OCT theorem, so that
`F=K_{1,3} dotunion K_2` and `u in V(F)`.  Two distinct vertices in the
`K_2` component lie in opposite bipartition sides, and its components may
be oriented independently of the claw.  Therefore the obstructing pair
`p,u` in (2.1) must consist of two claw leaves.  In particular neither is
a triangle vertex.

Let the literal triangle be `k_1k_2k_3`.  Form the five disjoint connected
sets

\[
          X\cup\{u\},\quad Y\cup\{p\},
          \quad\{k_1\},\quad\{k_2\},\quad\{k_3\}.       \tag{2.5}
\]

The first set is connected because `X` misses only `p`; the second is
connected because `Y` misses only `u`.  They are adjacent through the
fixed literal `X-Y` edge.
Both carriers contact all three triangle vertices, and the three
singletons form a clique.  Thus (2.5) is an `S`-rooted literal `K_5`
model in `G[A union S]`.

Let `P_1,P_2 subseteq R` be the two disjoint adjacent `S`-full packets.
They are adjacent to every bag in (2.5) through the literal boundary
vertex contained in that bag.  Consequently

\[
                    P_1,P_2\quad\hbox{and the five bags in (2.5)}
\]

form a literal `K_7` model, contrary to the setup.  This completes both
frontier forms.  \(\square\)

## 3. Consequences

### Corollary 3.1 (every clean core edge closes)

Every clean edge of the audited rooted path/`Y` core closes the atomic
cell.

#### Proof

The audited clean-edge split supplies disjoint adjacent connected carriers
partitioning `A`, each with boundary support at least six.  Name the side
containing `z` as `X` and apply Theorem 2.1.  \(\square\)

### Corollary 3.2 (the nonsingleton atomic shore is two-connected)

In the frozen minimal-counterexample kernel, every nonsingleton atomic
thin shore `A` has at least three vertices and is two-connected.

#### Proof

The independently audited root-deletion normalization proves that `A-z`
is connected, so `z` is not a cutvertex.

Suppose some `v ne z` is a cutvertex.  Let `D` be a component of `A-v`
not containing `z`, and put

\[
                         Y=D,\qquad X=A-D.              \tag{3.1}
\]

The set `Y` is connected.  Every component of `A-v` is adjacent to `v`
because `A` is connected; hence `X`, which contains `v` and all the other
components, is connected.  The two sets are adjacent and `z in X`.

For every component `K` of `A-v`, all of its neighbours outside `K` lie
in `S union {v}`.  The nonempty old rich shore lies beyond this set, so
seven-connectivity gives

\[
                             |N_S(K)|\ge6.              \tag{3.2}
\]

Apply (3.2) to `D` to get `|N_S(Y)|>=6`, and to any other component of
`A-v` (in particular the one containing `z`) to get
`|N_S(X)|>=6`.  Theorem 2.1 is a contradiction.  Thus `A` has no
cutvertex.

It remains to exclude `|A|=2`.  Write `A={z,a}`.  The root-deletion
normalization makes `{a}` `W`-full, so its support has order six.  The
minimal-counterexample kernel has minimum degree at least seven.  Since
`z` has no rich-shore neighbour and only the one possible neighbour `a`
inside `A`, it has at least six neighbours in `S`.  The adjacent singleton
carriers `{z},{a}` therefore satisfy Theorem 2.1, again a contradiction.
Consequently `|A|>=3`; connectedness and absence of a cutvertex say exactly
that `A` is two-connected.  \(\square\)

### Bridge-hull consequence

The crossed-defect certificate in the earlier clean-edge audit is now
closed rather than residual.  Therefore every surviving edge of the
rooted path/`Y` core is crossed by a literal `T`-bridge.  Moreover the
ambient thin shore is two-connected, so a bridge-hull induction may use
ordinary two-vertex linkage inside `A`; only label/state preservation
remains open.

The proof also identifies the correct use of a named proper-minor response:
one does not ask an arbitrary colouring of `G/h` to select the desired
orientation.  Instead, the literal defect pair determines the connected
contractions (2.3); the returned colour of the sole uncontracted literal
`p` adaptively selects one of the two low-demand states in (2.4).  Both
states are reflectable, so no palette-to-label identification is made.
