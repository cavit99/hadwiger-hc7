# A path normal form for one branch set of a `K_6`-minor model

**Status:** written proof; separate internal audit GREEN.

This note proves a local branch-set normalization.  It does not prove
`HC_7`, does not preserve the full valid defect-one configuration used by
the active programme, and does not produce a strict descent in the original
host graph.

## 1. Setup and the permitted re-selection

Let `G` be a finite graph.  Let

\[
                        B_1,B_2,B_3,B_4,B_5,L                 \tag{1.1}
\]

be pairwise disjoint nonempty connected vertex sets.  Assume that the five
sets `B_i` are pairwise adjacent and that `L` is adjacent to every `B_i`.
Thus (1.1) is a `K_6`-minor model with five named branch sets and one
distinguished branch set `L`.

At any stage of the following procedure, put

\[
 S_i=N_G(B_i)\cap L,
 \qquad
 P_L(x)=\{i\in\{1,\ldots,5\}:S_i=\{x\}\}.             \tag{1.2}
\]

The set `P_L(x)` records the named branch sets for which `x` is the unique
vertex of the current `L` having a neighbour in that branch set.  It records
unique *vertices of `L`*, not unique contact edges or unique neighbours
inside `B_i`.

Suppose `|L|>=2` and `x` is not a cutvertex of `G[L]`.  The following are
the only permitted elementary re-selections.

1. If `P_L(x)` is empty, replace `L` by `L-{x}` and leave every `B_i`
   unchanged.
2. If `P_L(x)={i}`, replace

   \[
                  (B_i,L)\quad\hbox{by}\quad
                  (B_i\cup\{x\},L-\{x\}),                 \tag{1.3}
   \]

   leaving the other four named branch sets unchanged.

Each operation preserves the names of the five branch sets; in the second
operation the branch set with name `i` is enlarged.  No assertion is made
that the enlarged set retains any additional role that `B_i` may have had
in a larger construction.

### Lemma 1.1 (legality of an elementary re-selection)

Each operation above produces another `K_6`-minor model satisfying the
same hypotheses as (1.1), and strictly decreases `|L|`.

#### Proof

Because `x` is not a cutvertex, `G[L-{x}]` is connected and nonempty.
Also, `x` has a neighbour in `L-{x}`: this follows from connectedness of
`G[L]` and `|L|>=2`.

If `P_L(x)` is empty, then for every `i` the nonempty set `S_i` contains a
vertex different from `x`.  Hence `L-{x}` remains adjacent to every `B_i`.

Suppose instead that `P_L(x)={i}`.  The equality `S_i={x}` implies that
`x` has a neighbour in `B_i`, so \(B_i\cup\{x\}\) is connected.  The edge from
`x` to `L-{x}` makes the enlarged `B_i` adjacent to the new distinguished
branch set.  For every `j!=i`, the fact that `j` is not in `P_L(x)` and
`S_j` is nonempty implies that `S_j` contains a vertex other than `x`.
Thus `L-{x}` remains adjacent to `B_j`.

All six sets remain pairwise disjoint.  Existing adjacencies among the five
named branch sets persist when one of them is enlarged.  This proves the
claim.

The proof does not require `x` to have only one neighbour in `B_i`, nor
does it require `x` to meet only one named branch set.  Multiple neighbours
in `B_i` cause no problem, and contacts from `x` to other `B_j` cause no
problem because those `B_j` retain a second contact vertex in `L-{x}`.
\(\square\)

Call a tuple **reduced** if neither elementary re-selection applies.
Repeated application of Lemma 1.1 terminates, since `|L|` decreases at
every step.

## 2. The path normal form

### Theorem 2.1 (five-support path normal form)

Starting from every tuple (1.1), a finite sequence of the permitted
elementary re-selections produces a reduced tuple in which one of the
following holds.

1. `L` is a singleton.
2. `G[L]` is an induced path.  If `s,t` are its two endpoints, then

   \[
                 |P_L(s)|\ge2,
                 \qquad |P_L(t)|\ge2,                       \tag{2.1}
   \]

   and the two sets `P_L(s),P_L(t)` are disjoint.  Consequently at most one
   of the five branch-set names lies outside their union.

The theorem does not require `G[L]` to be bipartite.  In particular, if
the initial distinguished branch set is induced and bipartite, the final
one is a singleton or an induced bipartite path.

#### Proof

Run the decreasing procedure until the tuple is reduced.  Suppose the
remaining `L` has at least two vertices.  If `x` is any non-cutvertex of
`G[L]`, reducedness and Lemma 1.1 imply

\[
                              |P_L(x)|\ge2.                  \tag{2.2}
\]

For distinct vertices `x,y` the sets `P_L(x)` and `P_L(y)` are disjoint:
one branch-set name `i` cannot satisfy both `S_i={x}` and `S_i={y}`.
There are only five names, so (2.2) implies that `G[L]` has at most two
non-cutvertices.

For completeness, every connected graph with at least two vertices has at
least two non-cutvertices, and it has exactly two if and only if it is a
path.  Indeed, the leaves of any spanning tree are non-cutvertices of the
ambient graph, because deleting a leaf leaves a connected spanning tree.
If a spanning tree is not a path it has at least three leaves.  If it is a
path but the ambient graph has an extra edge between nonconsecutive path
vertices, any path vertex strictly between the ends of that extra edge is
also a non-cutvertex.  Hence a connected graph with only two
non-cutvertices is exactly a path.

It follows that `G[L]` is a path and that its endpoints are precisely its
two non-cutvertices.  Equation (2.1) follows from (2.2), and disjointness
was proved above.  Two disjoint subsets of a five-element set, each of
order at least two, leave at most one unused name.  \(\square\)

## 3. Why absorption is necessary

The conclusion is false if the five named branch sets must remain fixed
and the only allowed operation is to replace `L` by a connected proper
subset.

Let `B_i={b_i}` for `1<=i<=5`, and let `b_1,...,b_5` induce a `K_5`.
Let

\[
                         L=\{x_1,x_2,x_3,x_4\}
\]

induce the chordless cycle

\[
                         x_1x_2x_3x_4x_1.
\]

Add the contact edges

\[
               x_1b_1,\quad x_2b_2,\quad x_3b_3,
               \quad x_4b_4,\quad x_4b_5,                  \tag{3.1}
\]

and no other edge between `L` and the five singleton branch sets.  The set
`L` is connected, induced, bipartite, and adjacent to all five named
branch sets.  Every connected vertex set adjacent to all five fixed
singletons must contain all four `x_i`, because the contacts in (3.1) are
unique.  Thus `L` is inclusion-minimal when the `B_i` are fixed, but
`G[L]` is a cycle rather than a path.

The elementary absorption in (1.3) is exactly what invalidates this
example as an obstruction to Theorem 2.1.

## 4. What the normal form says about splitting the path

The endpoint conclusion is an obstruction to the most direct branch-set
split; it is not by itself a `K_7` construction.

Suppose the reduced `L` is the path

\[
                          v_0v_1\cdots v_r,\qquad r\ge1.
\]

For every edge `v_kv_{k+1}`, the right shore
`{v_{k+1},...,v_r}` is nonadjacent to every `B_i` with
`i in P_L(v_0)`, because `v_0` is the unique vertex of all of `L` meeting
such a `B_i`.  Symmetrically, the left shore is nonadjacent to every
`B_i` with `i in P_L(v_r)`.  Each missed family has at least two names.

Consequently no edge split of this reduced path makes both path shores
adjacent to all five named branch sets.  The seven sets formed by the two
path shores and `B_1,...,B_5` therefore do not automatically form a
`K_7`-minor model.  A positive application needs a new path or connected
subgraph outside the displayed `K_6` model which replaces at least one of
these private contacts while preserving the named branch sets.

## 5. Conditional separator consequence in the defect-one setup

There is one direct host-level conclusion when the starting tuple comes
from the conditional defect-one setup in the active `HC_7` programme.
Let `L_0` be the selected component represented by a simplicial vertex of
the two-tree component-contact graph.  Since all four protected labels are
represented, that contact graph has a selected vertex other than the
vertices representing `L_0` and its two neighbours.  Let `W` be the
corresponding connected subgraph.  Simplicial degree two implies that
`W` is anticomplete to `L_0`.

### Proposition 5.1 (raw full-neighbourhood separations)

For every nonempty connected vertex set `Y` contained in `L_0`,

\[
                  \bigl(Y\cup N_G(Y),\;V(G)-Y\bigr)          \tag{5.1}
\]

is an actual separation with two nonempty open sides.  If `G` is
seven-connected, then

\[
                              |N_G(Y)|\ge7.                   \tag{5.2}
\]

#### Proof

The first open side contains `Y`.  The subgraph `W` is nonempty, disjoint
from `Y`, and has no edge to `Y`; hence it lies in the second open side
`V(G)-(Y\cup N_G(Y))`.  The intersection of the two closed sides in (5.1)
is exactly `N_G(Y)`.  Seven-connectivity gives (5.2).  \(\square\)

This applies in particular to every prefix and suffix of a path returned
by Theorem 2.1, because that path remains a subset of the original `L_0`.
It supplies an exact order-seven separation only if a separate argument
proves `|N_G(Y)|<=7`.  It supplies no six-colourings of the two closed
shores and no common equality partition on the separator.

## 6. Exact trust boundary for the active `HC_7` programme

Theorem 2.1 is a normalization of a local `K_6`-minor model.  It is not a
legal descent among the valid defect-one configurations in the original
host graph.

1. Even in the deletion case, `L-{x}` need not be a component of the fixed
   graph `G[K-V(P)]`: the vertex `x` remains in the original `G` and can
   reconnect it to the rest of the old component.
2. In the absorption case, the enlarged `B_i` contains a vertex taken from
   the protected component which supplied `L`.  If `B_i` was one of the
   path-side sets, the singleton `{z}`, or one of the two neighbouring
   selected components, this re-selection need not preserve its path,
   pole, protected-label, valid-cut, or component role.
3. Minimizing `|L|` over full valid defect-one configurations therefore
   does not imply reducedness under the elementary operations of Section 1:
   those operations need not return another full valid configuration.
4. Seven-connectivity gives only the lower bound (5.2).  The proper-minor
   six-colourings supplied by contraction-criticality do not identify their
   five exposed colours with the five named branch sets, and hence do not
   repair the private endpoint contacts or align two shore colourings.

To turn this normal form into a strict defect-one descent, one still needs
an operation-specific reconstruction theorem.  It must replace the named
contacts lost at an endpoint, reconstruct the complete path/cut and
component data in the original `G`, and either decrease the chosen literal
component, construct a `K_7`-minor model, or return an order-seven
separation with compatible boundary colourings.
