# Criticality forces private columns between locally parallel portals

## 1. Anti-domination

### Lemma 1.1 (critical neighbourhood antichain)

Let `G` be vertex-critical with chromatic number `k`.  If `x,y` are
distinct nonadjacent vertices, then neither of the containments

\[
                         N(x)\subseteq N(y),\qquad
                         N(y)\subseteq N(x)                         \tag{1.1}
\]

can hold.

#### Proof

Suppose `N(x) subseteq N(y)`.  Properly `(k-1)`-colour `G-x`, which is
possible by vertex-criticality.  Give `x` the colour of `y`.  The two
vertices are nonadjacent, and every neighbour of `x` is a neighbour of
`y`, so no neighbour of `x` has that colour.  This extends the colouring
to `G`, a contradiction.  The other containment is symmetric. \(\square\)

### Corollary 1.2 (outside profiles are a Sperner family)

Let `U subseteq V(G)` and let `x_1,...,x_m in U` be pairwise nonadjacent
vertices with the same neighbourhood inside `U`:

\[
                 N(x_i)\cap U=N(x_j)\cap U
                 \quad(1\le i,j\le m).                         \tag{1.2}
\]

Then the outside-neighbour sets

\[
                         F_i=N(x_i)-U                            \tag{1.3}

\]

are pairwise incomparable under inclusion.  In particular, when `m>=2`,
they are nonempty and pairwise distinct.

#### Proof

An inclusion `F_i subseteq F_j`, together with (1.2), would give
`N(x_i) subseteq N(x_j)`, contrary to Lemma 1.1. \(\square\)

## 2. The three- and four-column consequences

### Theorem 2.1 (three locally parallel portals have an outside SDR)

Under Corollary 1.2, if `m=3`, there are distinct vertices

\[
                   y_i in N(x_i)-U\qquad(i=1,2,3).              \tag{2.1}

\]

Thus the three locally parallel portal vertices have three literal,
pairwise vertex-disjoint one-edge columns leaving `U`.

#### Proof

The three sets `F_1,F_2,F_3` form an antichain of nonempty sets.  Every
two of them have a union of order at least two: otherwise they would be
the same singleton.  Their total union has order at least three, because
the nonempty subsets of a set of order at most two have no three-element
antichain.  Hall's theorem therefore gives a system of distinct
representatives, proving (2.1). \(\square\)

The same argument has one further sharp case.

### Theorem 2.2 (four locally parallel portals have an outside SDR)

Under Corollary 1.2, if `m=4`, there are distinct vertices

\[
                   y_i\in N(x_i)-U\qquad(i=1,2,3,4).           \tag{2.2}
\]

#### Proof

Apply Hall's theorem to the four-set antichain.  Subfamilies of orders
one, two, and three have unions of at least the corresponding orders by
the proof of Theorem 2.1.  The union of all four sets has order at least
four: the largest antichain of subsets of a three-element set has order
three.  Thus every Hall inequality holds. \(\square\)

Order four is exact for this unconditional linear conclusion.  Five of
the six two-subsets of a four-element ground set form a five-set
antichain whose union has order four, so they have no system of distinct
representatives.

## 3. Gate-A application and limitation

In the two-star cross-lobe counterarchitecture of
`hadwiger_gate_a_combined_network_round.md`, each side of either
`K_{3,3}` block consists of three locally parallel, pairwise nonadjacent
portal vertices.  If the displayed local neighbourhoods were their full
neighbourhoods in a vertex-critical host, Lemma 1.1 would immediately
exclude the graph.  In any actual critical realization, Theorem 2.1
forces three distinct contacts leaving the local carrier network on each
such triple.

This does not yet prove that the contacts have the correct labels or lie
on the correct quotient shore.  It does, however, remove the static
counterarchitecture as a closed module: every capacity-three non-rural
block must export three private columns.  The remaining state-forcing
lemma may therefore be phrased more sharply:

> show that the private columns exported by two complementary
> missing-row blocks can be rerouted to the four labelled columns of the
> rooted-torso theorem, or else their endpoints give a common
> proper-minor boundary state across the exact seven-adhesion.

The conclusion uses vertex-criticality, not merely seven-connectivity or
maximality of the `Q`-full partition.
