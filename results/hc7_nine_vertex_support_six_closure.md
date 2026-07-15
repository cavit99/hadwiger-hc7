# Nine-vertex closure for exact six-vertex `K_5` supports

**Status:** computer-assisted theorem; exhaustive certificate supplied and
independently replayed.  This closes every support-six obstruction whose
union is contained in nine vertices.  It does not prove the global
support-six transversal theorem.

## 1. Statement

An **exact six-support** in a graph `J` is a six-set which is the union of
the five branch sets of a `K_5` model and in which all six vertices are used.
Equivalently, its branch-bag sizes are `(2,1,1,1,1)`.

Let `E_6(J,X)` be the family of exact six-supports contained in a set
`X subseteq V(J)`.

### Theorem 1.1 (nine-vertex support closure)

Let `G` be a seven-connected graph and let `X subseteq V(G)` have order
nine.  If

\[
                         \tau(E_6(G,X))>2,              \tag{1.1}
\]

then `G` contains a `K_7` minor.

The theorem uses seven-connectivity only to eliminate one uniquely
determined local exception.

## 2. The finite local classification

### Lemma 2.1 (nine-vertex classification)

Let `J` be a graph on nine vertices.  If the exact six-supports of `J`
have transversal number greater than two, then either

1. `J` has a `K_7` minor; or
2. `J` is isomorphic to the complement of the nine-cycle.

Moreover, in the second case there are twenty-seven exact six-supports.

### Certificate

The script

[`active/hc7_support_six_nine_vertex_classifier.py`](../active/hc7_support_six_nine_vertex_classifier.py)

is a solver-free exhaustive certificate.  It invokes `geng` from
nauty/Traces to generate all unlabelled nine-vertex graphs with between
nineteen and thirty-six edges.  For every generated graph it:

1. enumerates all six-subsets and tests the unique possible spanning
   `K_5` branch-size pattern `(2,1,1,1,1)`;
2. tests every two-set against the resulting support family;
3. enumerates every partition of every seven-, eight-, or nine-subset into
   seven nonempty connected pairwise adjacent bags; and
4. retains precisely the graphs satisfying (1.1) and having no `K_7`
   minor.

Exactly `120314` unlabelled graphs are generated.  The retained list has
one entry:

\[
          \texttt{HUzvvx\}},\qquad |E(J)|=27,qquad |E_6(J,V(J))|=27.
                                                               \tag{2.1}
\]

The graph6 string in (2.1) is independently decoded by the script as
`complement(C_9)`.  No graph library, SAT solver, or heuristic minor test
is used.

It remains only to justify the lower edge cutoff.  Every exact six-support
contains at least eleven edges: six edges of its singleton `K_4`, the edge
inside its two-vertex bag, and at least one edge from that bag to each of
the four singleton bags.  For every pair `P subseteq V(J)`, condition
(1.1) supplies an exact support disjoint from `P`, so

\[
                            e(J-P)\ge11.                \tag{2.2}
\]

On summing (2.2) over all thirty-six pairs, every edge is counted
`binom(7,2)=21` times.  Hence

\[
             21e(J)=\sum_{|P|=2}e(J-P)\ge36\cdot11,
\]

and therefore `e(J)>=19`.  Thus the generation range is exhaustive.

## 3. The exceptional graph is universally seven-rooted

Label the vertices of `C_9` cyclically by `0,1,...,8` and put

\[
                              J=\overline{C_9}.         \tag{3.1}
\]

### Lemma 3.1 (rooted exception)

For every seven-set `N subseteq V(J)`, the graph `J` has a `K_6` model
every branch bag of which meets `N`.

### Proof

The dihedral group of the cycle has four orbits on the omitted pair,
according to cyclic distance `1,2,3,4`.  Representatives and six branch
bags are as follows:

\[
\begin{array}{c|l}
V(J)-N & \text{branch bags}\\ \hline
\{0,1\}&015,\ 2,\ 37,\ 4,\ 6,\ 8,\\
\{0,2\}&025,\ 1,\ 37,\ 4,\ 6,\ 8,\\
\{0,3\}&015,\ 2,\ 37,\ 4,\ 6,\ 8,\\
\{0,4\}&025,\ 1,\ 3,\ 47,\ 6,\ 8.
\end{array}                                               \tag{3.2}
\]

Here, for example, `015` denotes the bag `{0,1,5}`.  In the complement
of the cycle every displayed bag is connected, every two displayed bags
are adjacent, and every bag contains a vertex of `N`.  These twenty-one
adjacency checks, and all thirty-six literal choices of `N`, are also
verified by the certificate script.  Dihedral symmetry proves the claim.
\(\square\)

## 4. Proof of Theorem 1.1

Apply Lemma 2.1 to `J=G[X]`.  The first outcome is terminal.  In the
second, `G[X]` is `complement(C_9)`.

The graph `G-X` is nonempty: otherwise `G=G[X]` would be only
six-connected.  Let `C` be a component of `G-X`.  If `N_G(C)=X`, it has
nine neighbours in `X`; otherwise `N_G(C)` is a vertex cut, so
seven-connectivity gives

\[
                              |N_G(C)|\ge7.             \tag{4.1}
\]

Choose a seven-set `N subseteq N_G(C)`.  By Lemma 3.1, `G[X]` contains
an `N`-meeting `K_6` model.  Its six branch bags, together with the
connected seventh bag `C`, form a `K_7` model: every old bag contains a
vertex of `N` and is therefore adjacent to `C`.  This proves the theorem.
\(\square\)

## 5. Consequences for the active frontier

1. The complements of the lines of `AG(2,3)` cannot be a live
   graph-realized obstruction inside a hypothetical counterexample.
2. The thirteen-block pair-cover design is likewise only an abstract
   set-system barrier; every genuine realization meeting its stated
   support condition is already terminal.
3. Any remaining support-six family of transversal number greater than
   two in a seven-connected `K_7`-minor-free graph has union of order at
   least ten.

The third conclusion is the new extraction threshold.  It replaces both
nine-point designs by a single reusable rooted-model principle.
