# The connectivity-only near-`K_7` augmentation is open-problem strength

**Status:** barrier to an intermediate proof strategy; written reduction;
separate internal audit GREEN.  This is not a counterexample to the
proposed implication and is not a counterexample to `HC_7`.

## 1. Proposed implication

Consider the following tempting completion theorem.

> **Connectivity-only augmentation claim.** Every eight-connected graph
> containing a `K_7`-minus-one-edge minor contains a `K_7` minor.

The claim would close the one-deficient-branch-set case after an
order-seven separation has been excluded.  The reduction below shows that
it is not an appropriately local next lemma: it implies a major open
`K_6`-minor conjecture.

## 2. Hardness reduction

### Proposition 2.1

If the connectivity-only augmentation claim is true, then every
seven-connected graph contains a `K_6` minor.

#### Proof

Let `F` be an arbitrary seven-connected graph.  Then `|V(F)| >= 8`,
`delta(F) >= 7`, and `F` is nonplanar.  By Theorem 1.3 of Lo, every
four-connected nonplanar graph of minimum degree at least five contains a
`K_6`-minus-one-edge minor.  Hence `F` contains such a model.

Form the join

\[
                         G=K_1\vee F,
\]

and call the new universal vertex `a`.  The graph `G` is
eight-connected: after deleting at most seven vertices, either `a`
remains and joins all remaining vertices, or `a` is deleted and at most
six vertices have been deleted from the seven-connected graph `F`.

The singleton branch set `{a}`, together with the `K_6`-minus-one-edge
model in `F`, is a `K_7`-minus-one-edge model in `G`.  The proposed
augmentation claim would therefore give a `K_7` model in `G`.

At most one branch set of this model contains `a`.  If no branch set
contains `a`, then all seven lie in `F` and any six of them form a `K_6`
model there.  Otherwise, delete the unique branch set containing `a`.
The remaining six branch sets again lie in `F` and are pairwise adjacent.
Thus `F` contains a `K_6` minor.  Since `F` was arbitrary, every
seven-connected graph contains a `K_6` minor.  \(\square\)

## 3. Why this is a barrier

The conclusion of Proposition 2.1 is Conjecture 1.6 in the authors'
26 June 2024 revision of Chudnovsky--Scott--Seymour--Spirkl and is open.
Their Conjecture 1.4 is the stronger minimum-degree assertion that every
nonempty graph of minimum degree at least seven contains a `K_6` minor.

Accordingly, the connectivity-only augmentation claim must not be used as
an unproved bridge in the current `HC_7` programme.  A viable replacement
has to retain the additional hypotheses available in a hypothetical
minor-minimal counterexample, especially the proper-minor six-colourings,
the connected two-colour star, the rooted-model maximality, and the
colour-matched repair path.

The reduction does not show that the augmentation claim is false.  It
shows that proving it in this generality would settle an independently
important open problem and hence would merely replace the current gap by
another theorem-strength gap.

## 4. Primary sources

- O.-H. S. Lo,
  [*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973),
  Theorem 1.3: every four-connected nonplanar graph of minimum degree at
  least five contains a `K_6`-minus-one-edge minor.
- M. Chudnovsky, A. Scott, P. Seymour and S. Spirkl,
  [*Bipartite graphs with no `K_6` minor*](https://doi.org/10.1016/j.jctb.2023.08.005),
  Journal of Combinatorial Theory, Series B 164 (2024), 68--104;
  [authors' 26 June 2024 revision](https://web.math.princeton.edu/~pds/papers/bipK6/paper.pdf),
  Conjecture 1.6: every seven-connected graph contains a `K_6` minor,
  and Conjecture 1.4: every nonempty graph of minimum degree at least
  seven contains a `K_6` minor.
