# The bilateral exact-eight gate: a three-choice critical-core dichotomy

## 1. Setting

Let `G` be `K_7`-minor-free and let `X` be an eight-vertex adhesion with
two anticomplete connected shores full to `X`.  This includes the forced
exact-eight descendant of the minimum `C6+K1` atom.  Assume the established
case `HC_5`.

## 2. The three-choice dichotomy

### Theorem 2.1

At least one of the following structural branches is available; under
the failure of outcome 1, outcomes 2 and 3 are mutually exclusive.

1. Some vertex `x in X` can be reserved while `G[X-x]` contains a `K_5`
   model; then `G` contains a `K_7` minor.
2. `chi(G[X])<=4`.
3. `chi(G[X])=5`; then all of the following hold:
   * `G[X]` is 5-vertex-critical;
   * every `K_5` model in `G[X]` spans all eight vertices;
   * `G[X]` is the join of one universal vertex and a 4-critical
     seven-vertex graph.

Thus in a target-free gate, failure of all three cut-vertex reserve
choices is not an unstructured local obstruction.  It is either a
four-colour boundary-state gate or a coherent critical join core.

### Proof

The full-shore reserve lift proves outcome 1 whenever some `G[X-x]`
contains a `K_5` model.  Assume this never occurs.  Then

\[
                         \eta(G[X-x])\le4
                         \qquad(x\in X).              \tag{2.1}
\]

By `HC_5`, every graph in (2.1) is four-colourable.  Adding one vertex
raises chromatic number by at most one, so

\[
                         \chi(G[X])\le5.              \tag{2.2}
\]

If the left side is at most four, outcome 2 holds.  Suppose it is five.
Every vertex deletion is then at most four-colourable, so `G[X]` is
5-vertex-critical.  `HC_5` supplies a `K_5` model in `G[X]`; (2.1) says
that no vertex can be unused by such a model.  Hence every `K_5` model
spans `X`.

Gallai's small-critical-graph theorem says that a `k`-critical graph on
at most `2k-2` vertices is a nontrivial join of two smaller critical
graphs.  Apply it with `k=5` and `|X|=8`.  The chromatic numbers of the
two factors split as `1+4` or `2+3`.  A 1-critical graph is one vertex,
a 2-critical graph is `K_2`, and a 3-critical graph is an odd cycle.
The `2+3` split has `2+odd` vertices and therefore cannot have order
eight.  The split is consequently `1+4`: one factor is a single
universal vertex and the other is a 4-critical graph on seven vertices.
This is outcome 3.  QED.

## 3. Interaction with proper-minor states

Outcome 2 is the genuine colour-gluing branch: a fixed four-colouring of
the eight-vertex adhesion must fail to extend compatibly across the two
full shores, even though every internal edge deletion supplies an
endpoint-complete six-colour transition.  Outcome 3 is the coherent
near-clique branch: after contracting the two shores, the quotient is a
two-shore expansion of a universal vertex joined to a seven-vertex
4-critical core.

The remaining three-choice exchange theorem may therefore be stated
without defect labels:

> In the four-colour branch, opposite endpoint-complete proper-minor
> transitions either share a boundary partition and glue, or force a
> labelled rerouting which creates the reserve-core model of outcome 1.

The theorem above does not prove this last transition statement.  It
does prove that no third chromatic/rooted-model branch is hidden in the
simultaneous reserve failure.

### Later elimination of outcome 3

Lemma 1.1 of `hadwiger_exact8_critical_core_elimination.md` checks the
seven 4-critical graphs on seven vertices and proves that every one has a
vertex deletion containing a `K_4` minor.  In outcome 3, adjoining the
universal vertex would therefore give a `K_5` minor in some `X-x`,
contrary to the reserve obstruction.  Hence outcome 3 is empty and every
target-free bilateral exact-eight adhesion lies in the four-colour
state-gluing branch.
