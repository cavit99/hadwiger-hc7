# Induced-cycle web descent and opposite-shore bridge composition

**Status:** written proof; internal audit pending.  This is an unbounded
structural theorem for actual full separations.  It reduces the exact
two-shore crossless bipartite-guard branch to a strict host separator or
a six-colouring, and gives an explicit `K_7` construction
when a crossed cycle is paired with a suitable pole-free bridge.  It does
not prove that every bounded interface supplies that bridge, and it does
not prove `HC_7`.

## 1. Setup and terminology

Let `G` be a seven-connected graph and let `S` be a separator.  Let `D`
be a component of `G-S` adjacent to every vertex of `S`.

Let `W subseteq S` induce a chordless cycle of order `m>=4`, and put

\[
                         Q=S-W.                         \tag{1.1}
\]

Form the **portal graph** `P(D,W)` from `G[D]` by adding
one artificial terminal `t_w` for every `w in W`.  Join `t_w` to exactly
the vertices of `N_D(w)`, and join consecutive artificial terminals
in the cyclic order of `G[W]`.

Call the portal tuple **crossed** if four terminals in alternating cyclic
order admit the corresponding two vertex-disjoint paths in `P(D,W)`.

We use Theorem 1.5 of Humeau--Pous, *On the Two Paths Theorem and the Two
Disjoint Paths Problem*, arXiv:2505.16431, in the same form already checked
in the [audit of the guarded cyclic-shore
theorem](../results/hc7_guarded_cycle_web_exchange_audit.md): a crossless
ordered terminal tuple has an edge-only completion, on the same vertex
set, to a web with that frame.  A web has a planar rib and may have a
clique inserted behind each facial triangle; vertices of such an inserted
clique have no neighbours in the web outside the clique and its facial
triangle.

## 2. Cross or a strictly smaller actual separator

### Theorem 2.1 (one-shore induced-cycle web descent)

Under the setup in Section 1, at least one of the following holds.

1. The portal tuple is crossed.  In that case `G[D union W]` contains a
   `W`-rooted `K_4` minor model.
2. There is a nonempty connected set `X subseteq D` whose full
   neighbourhood is an actual separator satisfying

   \[
             7\le |N_G(X)|\le |Q|+3
                    =|S|-m+3\le |S|-1.                \tag{2.1}
   \]
3. The graph `G[D union W]` has a plane embedding in a closed disc with
   the cycle `G[W]` as its boundary.

#### Proof

Suppose first that the portal tuple in `P(D,W)` is crossed.  The two paths
are terminal-clean.  Replace each artificial terminal at a path end by
its actual root in `W` and replace the incident artificial edge by the
corresponding portal edge.  Together with the four arcs of the chordless
cycle between the alternating roots, the two paths form a rooted
subdivision of `K_4`.  Splitting its subdivided edges at suitable edges
gives four disjoint pairwise adjacent connected branch sets, one at each
root.  This is outcome 1.

We may therefore assume that the portal tuple is crossless.  Complete
`P(D,W)` to a web on the same vertex set.

Suppose that an inserted facial clique contains an original vertex of
`D`, and let `X` be the set of all original shore vertices in that
clique.  The set `X` is nonempty and connected.  Inside `D union W`,
all of its neighbours outside `X` are represented by the at most three
vertices of the facial triangle.  Replace any artificial terminal among
those vertices by its corresponding actual root in `W`.  Vertices of `X`
may additionally have neighbours in `Q`, but they have no neighbours in
any other component of `G-S`.  Hence

\[
                         |N_G(X)|\le 3+|Q|.             \tag{2.2}
\]

The full neighbourhood `N_G(X)` separates `X` from every other component
of `G-S`.  Seven-connectivity gives the lower bound in (2.1), while
`m>=4` gives the strict upper bound `|Q|+3<=|S|-1`.  This is outcome 2.

It remains that no inserted facial clique contains an original shore
vertex.  Thus every original vertex and edge of `D` lies in the planar
rib.  Delete the completion edges, delete the
artificial terminals, put the actual roots in their places, and replace
terminal--shore edges by the corresponding portal edges.  Because
`G[W]` is precisely the frame cycle, this gives a plane embedding of
`G[D union W]` in a closed disc with `G[W]` as its boundary.  This is
outcome 3. \(\square\)

### Corollary 2.2 (two-shore cross, descent, or colouring)

Suppose `G-S` has exactly two components `D_0,D_1`, both full to `S`, and
`G[Q]` is bipartite.  Then one of the following holds:

1. one component contains a `W`-rooted `K_4` model;
2. `G` has an actual separator satisfying (2.1); or
3. `G` is six-colourable.

#### Proof

Apply Theorem 2.1 to both components.  The first two outcomes give items
1 and 2.  Otherwise each `G[D_j union W]` has a disc embedding with the
same boundary cycle.  Reflect one disc and identify the boundary cycles.
There are no edges between the two components, so this gives a planar
embedding of

\[
                         G-Q=G[D_0\cup D_1\cup W].       \tag{2.3}
\]

Four-colour `G-Q` and colour the bipartite graph `G[Q]` with two fresh
colours.  This is a proper six-colouring of `G`, regardless of the edges
between `Q` and `G-Q`. \(\square\)

### Corollary 2.3 (structural residue from nonsplitness)

Assume that `G-S` has exactly two full components and that `G[S]` is
nonsplit.  Then one of the following holds.

1. `G[S]` is chordal and contains an induced `2K_2`;
2. `G[S]` has an induced cycle `W` for which `G[S-W]` is nonbipartite;
3. a shore contains a `W`-rooted `K_4` model for some induced cycle `W`;
4. `G` has an actual separator of order at most `|S|-1`; or
5. `G` is six-colourable.

#### Proof

If `G[S]` is chordal, it has no induced `C_4` or `C_5`.  The
Földes--Hammer forbidden-induced-subgraph characterization of split
graphs then says that its nonsplitness is witnessed by an induced
`2K_2`, giving outcome 1.

Otherwise take any induced cycle `W` of order at least four.  If
`G[S-W]` is nonbipartite, outcome 2 holds.  If it is bipartite, apply
Corollary 2.2.  Its three outcomes give respectively outcome 3, outcome
4, or outcome 5. \(\square\)

For `7<=|S|<=9`, outcome 2 is especially narrow.  If `|W|>=7`, it is
impossible because at most two vertices remain.  If `|W|=6`, it requires
the three remaining vertices to form a triangle.  More generally the
guard `S-W` must contain an odd cycle.  This observation is descriptive;
it is not a finite-case closure.

### Lemma 2.4 (cycle-complete guards are triangle-free)

Suppose additionally that

\[
             \overline K_2\vee G[S]
             \quad\hbox{has no }K_7\hbox{ minor}.       \tag{2.4}
\]

Let `U subseteq S-W` be the set of vertices complete to `W`.  Then
`G[U]` is triangle-free.

#### Proof

The cycle `G[W]` has a `K_3` minor.  If three vertices of `U` formed a
triangle, their singleton branch sets together with that cycle minor
would give a `K_6` minor in `G[S]`.  Either one of the two added universal
vertices in (2.4) would then complete it to a `K_7` minor, a
contradiction. \(\square\)

### Corollary 2.5 (dominating induced-cycle family)

Assume the hypotheses of Corollary 2.2 and (2.4), with
`7<=|S|<=9`.  If `|W|>=5` and every vertex of `S-W` is complete to `W`,
then one component contains a `W`-rooted `K_4` model, or `G` has an
actual separator of order at most `|S|-1`, or `G` is six-colourable.

#### Proof

Here `Q=U` has order at most four.  By Lemma 2.4 it is triangle-free, and
every triangle-free graph on at most four vertices is bipartite.  Apply
Corollary 2.2. \(\square\)

This closes the crossless/no-descent part of an infinite family in the
shore orders.  It is not a boundary census, and its crossed rooted-minor
outcome is composed with a pole-free bridge in the next section.

## 3. Composing a crossed cycle with a pole-free bridge

The crossed outcome of Theorem 2.1 becomes terminal when the opposite
shore supplies two adjacent connected branch sets that both see the four
rooted bags.  A pole-free path gives exactly those two sets when its ends
are complete to the cycle.

### Theorem 3.1 (opposite-shore path-splitting composition)

Retain `G,S,W,Q` from Section 1.  Let `D_0,D_1` be distinct components of
`G-S`, and let `u in D_1` be adjacent to every vertex of `S`.  Suppose
that:

1. `G[D_0 union W]` contains a `W`-rooted `K_4` minor model
   `M_1,M_2,M_3,M_4`;
2. `P` is an `a`--`b` path, for distinct `a,b in S`, whose internal
   vertices lie in `D_1-{u}`; and
3. some edge `e` of `P` separates it into two nonempty subpaths
   `P_a,P_b` such that each subpath is adjacent to every `M_i`.

Then `G` contains a `K_7` minor.

#### Proof

The subpaths `P_a,P_b` are disjoint, connected, and adjacent through
`e`.  Each is adjacent to all four rooted bags by hypothesis.  Each
`M_i` contains a root `w_i in W`, so the singleton `{u}` is adjacent to
every `M_i`.  It is adjacent to `P_a,P_b` through `a,b`, respectively.
Thus

\[
             M_1,M_2,M_3,M_4,P_a,P_b,\{u\}             \tag{3.1}
\]

are seven disjoint connected pairwise adjacent branch sets. \(\square\)

### Corollary 3.2 (cycle-complete ends)

The path-splitting hypothesis of Theorem 3.1 holds if `a,b in S-W` and
each of `a,b` is complete to `W`.

#### Proof

Choose any edge of `P` for the split.  The subpath containing `a` is
adjacent to each `M_i` through the edge from `a` to the root in `M_i`;
the same holds at `b`. \(\square\)

### Corollary 3.3 (application to the bounded anti-neighbourhood frame)

In the bounded-interface setup, orient `D_0` as the component `C` of
`G-N[u]` and `D_1` as the component of `G-S` containing `u`.  If an
induced boundary cycle `W` has a crossed `C`-portal tuple and one of the
pole-free paths forced by the exact-block Kempe reduction lies in
`D_1-{u}`, has both ends in `S-W`, and both ends are complete to `W`,
then `G` has a `K_7` minor.

This is an explicit composition, not an identification of a colour class
with a branch set.  The remaining obstruction is correspondingly exact:
a crossed `C`-tuple can survive only if every available opposite-shore
pole-free bridge fails the two cycle-completeness duties (or has an end on
the cycle).  Handling that distributed-contact failure requires more than
the abstract equality partition of its ends.

## 4. Scope

Theorem 2.1 is uniform in the shore order and in the cycle length.  Its
separator outcome is measured in the original host graph,
not in a web completion, and strictly reduces the boundary order.  The
planar outcome closes whenever the omitted boundary graph is bipartite.

The one-shore theorem allows arbitrarily many open components.  The
six-colouring conclusion in Corollary 2.2 assumes exactly two: with
additional full components, two disc embeddings do not cover `G-Q`, and
one must instead use a multishore minor or colouring-composition theorem.
Theorem 3.1 also does not assert that the forced pole-free bridge has
cycle-complete ends.  Those are the two precise limits of the present
result.

No completion edge of a web is used as an edge of `G`.  In the crossed
outcome, every path edge belongs to the portal graph and every artificial
terminal incidence is replaced by its literal portal edge.  In the planar
outcome, all completion edges are deleted before terminals are replaced
by boundary roots.  The gluing conclusion uses the induced frame cycle
and exactly two open components; it is not asserted for a virtual frame
or for a third shore.

Finally, the smaller separator in (2.1) is an actual host separator, but
the theorem does not show that it retains the low-degree pole, the named
edge-deletion response, or the exact-block colouring data of the original
bounded interface.  It is therefore a strict separator-order reduction,
not yet a recursive instance of the full bounded-interface theorem.
