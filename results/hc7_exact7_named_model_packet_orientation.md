# Named small models orient an exact-seven packet cell

**Status:** proved and independently cold-audited.

This note records the exact conclusion available from a named
support-at-most-six `K_5` model at a literal seven-separator.  It does not
close the resulting packet-`(1,1)` cell and it does not claim a strict
recursive descent.

## 1. Setup

Let `G` be a seven-connected graph and let `S` be a seven-set such that
`G-S` has at least two components.  Every component of `G-S` is then
`S`-full: its neighbourhood is a subset of `S`, and seven-connectivity
forces that neighbourhood to have order at least seven.

A named `K_5` model `M=(B_1,...,B_5)` is **owned by** a component `C` of
`G-S` if

\[
 V(M)\subseteq S\cup C,\qquad V(M)\not\subseteq S.
\]

This is exactly the ownership returned by the audited split-edge
separator handoff: every named model has all of its off-boundary vertices
in one component.

A connected subgraph of `G-S` is an `S`-full packet if it has a neighbour
at every literal vertex of `S`.

## 2. Boundary exclusion

### Lemma 2.1

If `G` has no `K_7` minor, no `K_5` model supported on at most six
vertices is contained in `S`.

### Proof

Suppose that `B_1,...,B_5` is such a model and put
`W=V(B_1) union ... union V(B_5) subseteq S`.  Choose
`x in S-W`, which is possible because `|W|<=6<|S|`, and choose two
distinct components `C,D` of `G-S`.

The seven sets

\[
                B_1,\ldots,B_5,\quad C\cup\{x\},\quad D
\]

are disjoint and connected.  The first five are pairwise adjacent.  Both
`C` and `D` are `S`-full, so they are adjacent to every `B_i`.
Moreover, `C union {x}` is connected and is adjacent to `D` through an
edge from `x` to `D`.  These are the branch sets of a `K_7` minor, a
contradiction.  \(\square\)

## 3. A branch-faithful fan to the boundary

### Lemma 3.1 (five-root fan)

Let `M=(B_1,...,B_5)` be a `K_5` model supported on at most six vertices
and owned by a component `C` of `G-S`.  There are disjoint connected
subgraphs

\[
                         R_1,\ldots,R_5\subseteq G[S\cup C]
\]

with all of the following properties.

1. The `R_i` are pairwise adjacent.
2. Each `R_i` contains the whole corresponding branch bag `B_i`.
3. The five `R_i` meet five distinct vertices of `S`.
4. Their union contains at most six vertices of `S`.

### Proof

Choose one representative `a_i in B_i` from every branch bag and put
`A={a_1,...,a_5}`.  Since the total support has order at most six, the
set

\[
 D=V(M)-A
\]

has order at most one.  Put `A_S=A cap S`, `A_0=A-S`, and
`r=|A_0|=5-|A_S|`.  Delete `D union A_S`.  The remaining graph is at
least

\[
                 7-|D|-|A_S|\ \ge\ r
\]

connected.  The target set

\[
                 S_0=S-(D\cup A)
\]

has order at least `7-|A_S|-|D|>=r`.  The set version of Menger's
theorem therefore gives `r` disjoint `A_0`--`S_0` paths, using every
vertex of `A_0` and distinct vertices of `S_0`.

Truncate each path at its first vertex of `S`.  Its interior then lies in
`C`: it starts at a vertex of `C`, and leaving `C` requires first meeting
`S`.  For every `a_i in A_S`, use the zero-length path `{a_i}`.  The five
paths are disjoint and have five distinct ends in `S`.

Finally, if `D={d}`, adjoin `d` to the path starting at the representative
of the unique two-vertex branch bag.  The two vertices of that bag are
adjacent, so the enlarged path remains connected.  Call the resulting
five subgraphs `R_1,...,R_5`.  They contain the five original branch bags
and hence are pairwise adjacent.  The truncated paths contain no boundary
vertices except their five ends; the only possible additional boundary
vertex is `d`.  Thus their union meets at most six vertices of `S`.
\(\square\)

## 4. Opposite packet absorption

### Theorem 4.1 (named-model packet orientation)

Let `G` be seven-connected and `K_7`-minor-free.  Suppose a named
support-at-most-six `K_5` model is owned by a component `C` of `G-S`.
Then the union of all other components of `G-S` does not contain two
vertex-disjoint `S`-full packets.

Consequently:

1. `G-S` has exactly two components;
2. the component different from `C` has packet number exactly one; and
3. if named small models are owned on both sides, then both components
   have packet number one.

### Proof

Apply Lemma 3.1 and obtain the five rooted bags `R_1,...,R_5`.  Suppose
that the opposite open side contains disjoint `S`-full packets `P,Q`.
By item 4 of Lemma 3.1, choose

\[
                x\in S-\bigcup_{i=1}^5 V(R_i).
\]

The seven sets

\[
                   R_1,\ldots,R_5,\quad P\cup\{x\},\quad Q
\]

are disjoint and connected.  Both packets are adjacent to every `R_i`
through the distinct boundary root contained in `R_i`.  The set
`P union {x}` is connected because `P` is `S`-full, and it is adjacent to
`Q` because `Q` has a neighbour of `x`.  Hence the seven displayed sets
form a `K_7` model, a contradiction.

Every component of `G-S` is itself an `S`-full packet.  Since at least two
components exist, the preceding paragraph implies that there can be only
one component other than `C`.  That component has packet number at least
one and at most one, proving items 1 and 2.  If another named model is
owned by the other component, repeat the argument with the roles of the
components reversed to obtain item 3.  \(\square\)

### Corollary 4.2 (three named models)

Suppose three named small models from the split-edge separator handoff are
all preserved and none lies in `S`.

* There are exactly two open components.
* If the ownership distribution is `2+1`, then the exact-seven cell has
  packet vector `(1,1)`.
* The unique-side named model gives a literal orientation of a `2+1`
  cell.  This orientation is label-preserving, but no strict decrease of
  shore order follows from the present theorem.

Pairwise disjointness of the three named supports is not needed for these
conclusions.  When it is present, a global two-vertex transversal is
already impossible because two vertices cannot meet three pairwise
disjoint supports.

## 5. Trust boundary

The theorem eliminates every opposite two-packet outcome and every
three-or-more-component exact-seven handoff carrying a named small model.
It does not eliminate either of the following residues:

* all three named models are owned by one component, while only the other
  component is known to be packet-one; or
* the `2+1` distribution with packet vector `(1,1)`.

In particular, ownership distribution alone does not produce a nested
separator, preserve a colouring state, or prove that a returned handoff
is strictly smaller.  Any recursive use must retain an immutable named
model (or a private pair) and separately prove literal containment of its
new owner shore.
