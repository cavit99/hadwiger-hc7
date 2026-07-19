# Exact completion with two connected subgraphs and six outside branch sets

**Status:** written proof; separate internal audit GREEN in
[`hc7_five_contact_completion_classification_audit.md`](hc7_five_contact_completion_classification_audit.md).
This theorem corrects the tempting but false assertion that five outside
contacts always suffice in the reserved-component configuration.  It
classifies the exact two quotient obstructions and shows that repairing any
one of their three missing adjacencies gives an explicit `K_7`-minor model.
It does not force such a repair and does not prove `HC_7`.

## 1. Setting

Let

\[
                 \mathcal Q=\{X,Y,D,F_1,F_2,F_3\}       \tag{1.1}
\]

be six pairwise disjoint connected branch sets.  Every two members of
`\mathcal Q` are adjacent except possibly `X,Y`.  Let `A,R` be two further
disjoint connected subgraphs, disjoint from `\mathcal Q` and adjacent to
one another.

Assume that `A` is adjacent to every member of `\mathcal Q` except possibly
one member `a`, and that `R` is adjacent to every member except possibly one
member `b`.  The symbol `perp` below means that the corresponding connected
subgraph is adjacent to all six members.  Assume throughout that

\[
                     a\in\{X,Y,F_1,F_2,F_3\};            \tag{1.2}
\]

as holds in the reserved-component application; the branch set `D` is not
an omitted owner.

## 2. Exact eight-object classification

### Theorem 2.1

The eight displayed connected sets contain a `K_7`-minor model unless all
three of `X-Y`, `A-a`, and `R-b` are genuine missing adjacencies and, up to
interchanging `X,Y` or relabelling `F_1,F_2,F_3`, one of the following
holds.

1. **Crossed polar misses:**

   \[
                       (a,b)=(X,Y)\quad\hbox{or}\quad(Y,X).  \tag{2.1}
   \]

   The quotient on the eight connected sets is `K_8` with the three edges
   of a four-vertex path deleted.
2. **Distinct universal misses:** for some `i`,

   \[
               a=F_i,qquad
               b\in\{D,F_j:j\ne i\}.                    \tag{2.2}
   \]

   The quotient is `K_8` with three independent edges deleted.

In either exceptional quotient, adding a connected path whose interior is
disjoint from all eight displayed connected sets, or an additional
branch-set adjacency, which repairs any one of the three missing
adjacencies produces a `K_7`-minor model.

#### Proof

If `X-Y` is present, the six outside branch sets form a `K_6` model.  When
`A,R` miss the same member, discard that member; when they miss two distinct
members, merge those two adjacent branch sets.  If either connected
subgraph has no miss, discard the member missed by the other, or discard an
arbitrary outside member when neither has a miss.  In every case the five
remaining outside bags are adjacent to both `A,R`.  Thus assume that
`X-Y` is absent.

If `A` has no missed member and `R` misses `b`, discard `b` when
`b\in\{X,Y\}`; when `b\in\{D,F_1,F_2,F_3\}`, merge `X` with `b`.  If `R`
has no miss, the case table below applies with `b=perp`.  We may therefore
write `a,b` for genuine misses when describing the sharp exceptions.

First suppose `a=X`.  If `b` is `perp` or `X`, discard `X`; the other five
outside branch sets form a clique model adjacent to both `A` and `R`.  If
`b` is one of `D,F_1,F_2,F_3`, merge the adjacent branch sets `X` and `b`.
The merged set is adjacent to `Y` through `b`, is adjacent to `A` through
`b`, and is adjacent to `R` through `X`.  It and the other four outside
sets form the required `K_5` model.  The only unclosed case is `b=Y`.
The case `a=Y` is symmetric.

Now let `a=F_i`.  If `b` is `perp`, `F_i`, or `X`, merge `X` with `F_i`.
The merged set is adjacent to `Y` through `F_i`, while `A` contacts it
through `X` and `R` contacts it through at least one of `X,F_i`.  If
`b=Y`, use `Y\cup F_i` symmetrically.  These mergers again give five
pairwise adjacent outside branch sets, each adjacent to `A` and `R`.
The only remaining choices are exactly (2.2).

In every closed case, the five resulting outside branch sets together with

\[
                              A,\ R                       \tag{2.3}
\]

are seven pairwise disjoint connected sets with all pairwise adjacencies.
Thus they are an explicit `K_7`-minor model.

It remains to verify sharpness at the quotient level.  In case (2.2), the
missing edges are

\[
                            XY,\quad AF_i,\quad Rb,       \tag{2.4}
\]

which are pairwise vertex-disjoint.  A `K_7` model in an eight-vertex
quotient either omits one vertex and uses seven singleton bags, or uses all
eight vertices and has exactly one two-vertex connected bag.  Omitting one
vertex leaves at least two edges of (2.4).  Contracting one present edge can
cover the endpoints of at most two edges of the matching (2.4), so the
third remains.  Hence this quotient has no `K_7` minor.

In case (2.1), the missing-edge graph is the path

\[
                              A-X-Y-R                     \tag{2.5}
\]

or its reverse.  Deleting one vertex leaves a missing edge.  The only
two-vertex covers of the three edges of (2.5) are

\[
                         \{X,Y\},\quad\{A,Y\},\quad\{X,R\}. \tag{2.6}
\]

The first pair is nonadjacent and cannot be one connected branch set.  The
set `A\cup Y` has no edge to `X`, and `X\cup R` has no edge to `Y`.
Thus no possible two-vertex branch set yields `K_7`.

Finally, in the matching case (2.4), repairing any one missing edge leaves
two independent missing edges.  Contract an edge joining one endpoint of
the first to one endpoint of the second; the displayed quotient has all
four such cross-edges, and the merged bag covers both remaining misses.  In
the path case (2.5), repairing the middle edge permits contraction of the
present edge `A-R`; repairing an end edge permits deletion of the shared
internal vertex of the other two missing edges.  Each operation gives seven
pairwise adjacent connected bags. \(\square\)

## 3. Three-owner consequence

### Corollary 3.1

In the three-owner reserved-component setting, choose the omitted owner

\[
                         a=R_0\in I-\{X,Y\}.             \tag{3.1}
\]

Thus `a=F_i` for some `i`.  If a connected residual subgraph `R` is
adjacent to the linkage union and to at least five outside branch sets,
then it gives a `K_7` minor except when its unique missed label is

\[
                         b\in\{D,F_j:j\ne i\}.           \tag{3.2}
\]

In the exceptional case the quotient is `K_8-3K_2`, with missing
adjacencies

\[
                             X-Y,\quad A-F_i,\quad R-b.  \tag{3.3}

Repairing any one of the three by an additional branch-set edge or by a
path internally disjoint from the eight displayed sets is terminal.

#### Proof

Apply Theorem 2.1.  The choice (3.1) excludes the crossed polar cases, and
(2.2) is precisely (3.2). \(\square\)

## 4. Residual bridge count

### Corollary 4.1

Retain the literal order-eight boundary

\[
 S=\{k_1,k_2,s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.     \tag{4.1}
\]

Let `P=P_1\cup P_2` be a two-owner linkage, with `P\cap C` nonempty, and let
`R` be a component of `C-V(P)`.  If `R` contacts at most four
of the six outside branch sets, then:

1. `R` has at least one neighbour in `P\cap C`; and
2. either `N_G(R)` is an actual order-seven boundary, or `R` has at least
   two distinct neighbours in `P\cap C`.

If `R` contacts five outside branch sets, the same count permits one
linkage attachment at an order-eight full neighbourhood; no second
attachment or order-seven conclusion follows from connectivity alone.

#### Proof

Every neighbour of `R` outside `C` belongs to the eight-set `S`, and among
those vertices at most the two `k_i` and four outside representatives can
occur.  Since `R` is a component after deleting `P\cap C`, all its other
neighbours in `C` lie on `P\cap C`.  Connectedness of `C` gives at least
one such neighbour.  Hence one attachment gives

\[
                             |N_G(R)|\le 6+1=7.          \tag{4.2}
\]

The set `N_G(R)` separates nonempty `R` from the linkage and the opposite
component behind `S`.  Seven-connectivity makes (4.2) equality and returns
an actual order-seven separation.  If that outcome is absent, the
neighbourhood has order at least eight and therefore contains at least two
distinct linkage attachments.

With five outside contacts, the corresponding bound is `5+2+1=8`, proving
the final warning. \(\square\)

## 5. Trust boundary

Raw contact count is not the correct completion invariant.  In the sharp
survivor a residual may meet five of the six outside branch sets and still
fail to complete `K_7`, because merging its missed label with the omitted
owner leaves the independent missing pair `X-Y`.

The operation-specific next theorem must therefore repair one of the three
literal gaps in (3.3), increase the number of outside bags simultaneously
usable by the linkage union and the residual, or return a compatible exact
order-seven separation.  This theorem provides the exact quotient target;
it does not produce the required response path or boundary colouring.
