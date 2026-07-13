# A portal-choice-invariant attained-duty gate core

**Status:** proved and independently audited.  This strengthens the
selected-witness Helly gate in the exact-seven `(1,2)` cell.  It uses the
point--tree Koenig theorem to obtain one subtree meeting **every** attainable
duty hull in a fixed full packet, and then identifies the only way that
transversal can fail to be a single literal vertex.  It does not yet turn
the resulting core into an adhesion or an apex pair.

## 1. Cross-intersecting subtree families

Let `T` be a finite tree and let

\[
                 \mathcal H_1,\mathcal H_2,\mathcal H_3
\]

be nonempty finite families of nonempty subtrees of `T`.  Call them
**cross-intersecting** when

\[
 K\cap L\ne\varnothing
 \quad\text{for all }K\in\mathcal H_i, L\in\mathcal H_j, i\ne j.
 \tag{1.1}
\]

### Theorem 1.1 (dominant hull and minimal gate core)

For three cross-intersecting families as above, there is a subtree
`K_0` belonging to one of the three families which meets every member of
all three families.

Moreover, let `R\subseteq K_0` be an inclusion-minimal subtree meeting
every member of all three families.  Exactly one of the following holds.

1. `R={g}` is one literal vertex, and every subtree in every family
   contains `g`.
2. `R` has at least two leaves.  There is one index `j` such that:

   * for every leaf `r` of `R`, some `L_r\in\mathcal H_j` satisfies
     `L_r\cap R=\{r\}`;
   * the subtrees `L_r`, over the leaves of `R`, are pairwise disjoint; and
   * every member of either family `\mathcal H_i` with `i\ne j` contains
     all of `R`.

#### Proof

Form a point--tree hypergraph `\mathcal A` on the disjoint ground set

\[
                         \{1,2,3\}\mathbin{\dot\cup}V(T)
\]

whose hyperedges are

\[
                    \{i\}\cup V(K),
       \qquad i\in\{1,2,3\},\quad K\in\mathcal H_i.       \tag{1.2}
\]

Two hyperedges with the same point `i` meet at `i`, while two hyperedges
with different points meet in `T` by (1.1).  Thus the matching number of
`\mathcal A` is one.

The point--tree Koenig theorem of Aharoni--Berger--Ziv says that

\[
                          \sigma(\mathcal A)\le\nu(\mathcal A)=1, \tag{1.3}
\]

where a covering member counted by `sigma` is either one point `{i}` or
the vertex set of one of the subtrees occurring in (1.2).  No singleton
`{i}` covers `mathcal A`, because each of the other two families is
nonempty.  Hence (1.3) supplies some occurring subtree `K_0` whose vertex
set meets every hyperedge, equivalently every member of every
`mathcal H_i`.  This proves the first assertion.

Choose an inclusion-minimal subtree `R\subseteq K_0` with the same
transversal property.  If it is a singleton, outcome 1 holds.  Assume
instead that `R` has at least two vertices.  For each leaf `r` of `R`, the
proper subtree `R-r` fails to hit every member, so there is a subtree
`L_r` in one of the three families such that

\[
                              L_r\cap R=\{r\}.          \tag{1.4}
\]

For distinct leaves `r,s`, the subtrees `L_r,L_s` are disjoint.  Otherwise
their union would be a connected subgraph of the tree containing `r,s`,
and hence would contain the unique `r-s` path.  That path lies in `R`,
contradicting (1.4) at its first edge (and also when `R` is the single
edge `rs`).  By cross-intersection, pairwise disjoint leaf witnesses must
all belong to one family; call it `\mathcal H_j`.

Let `K\in\mathcal H_i` with `i\ne j`.  Cross-intersection makes `K` meet
every `L_r`.  Choose `x_r in K cap L_r` for each leaf `r`.  For any two
leaves `r,s`, the unique `x_r-x_s` path enters `R` at `r`, contains the
whole path `rRs`, and leaves at `s`, because of (1.4).  Since `K` is a
subtree containing `x_r,x_s`, it contains `rRs`.  The union of the paths
between the leaves of a nontrivial tree is the whole tree, so `R\subseteq K`.
This proves every clause of outcome 2.  \(\square\)

The only external input is Theorem 2.1 of R. Aharoni, E. Berger and
R. Ziv, *A tree version of Koenig's theorem*, Combinatorica 22 (2002),
335--343; arXiv:math/9912134.  The application uses its literal
point--tree hypergraph definition and the inequality `sigma<=nu`.

## 2. Attainable duty hulls in one full packet

Retain an attained demand-three state `Pi` in an actual exact-seven
`(1,2)` adhesion, with duties `D_1,D_2,D_3`, and let `P` be either of the
two disjoint full packets.  Fix an arbitrary spanning tree `T` of `P`.

For each `i`, let `\mathcal H_i(T)` consist of all minimal subtrees

\[
             T[\{p(s):s\in D_i\}],                    \tag{2.1}
\]

over every duty-specific choice

\[
                  p(s)\in V(P)\cap N_G(s),\qquad s\in D_i. \tag{2.2}
\]

These are the **attainable duty hulls** in `T`.  The family is nonempty
because `P` is full to every literal boundary vertex.  A hull is a literal
connected carrier funding its displayed duty.

### Corollary 2.1 (choice-invariant packet gate core)

If the attained state does not reflect across the rich shore, then the
three families `\mathcal H_i(T)` are cross-intersecting.  Consequently they
have a gate core `R` satisfying Theorem 1.1.  Thus either:

1. one literal packet vertex lies in every attainable hull of every duty;
   or
2. one exceptional duty `j` has pairwise disjoint leaf-witness hulls, while
   every attainable hull of each of the other two duties contains the same
   whole subtree `R`.

#### Proof

If `K\in\mathcal H_i(T)` and `L\in\mathcal H_j(T)` were disjoint for
`i\ne j`, they would be two disjoint duty-correct subtrees of the same
packet tree.  Cutting their unique joining path gives adjacent connected
carriers for those two duties.  The other full packet funds the third duty,
so the audited attained-duty tree-split theorem reflects `Pi`, contrary to
hypothesis.  Hence (1.1) holds, and Theorem 1.1 applies.  \(\square\)

## 3. Exact scope

This result removes the quantifier defect of a gate obtained from one
selected witness triple.  The core `R` is chosen only after considering all
literal portal choices in one fixed spanning tree, and outcome 1 is a true
portal-choice-invariant vertex obstruction.

Outcome 2 is not yet a separator theorem.  In particular:

* `R` may have arbitrary order;
* the exceptional-duty leaf hulls need not be adjacent;
* a leaf of `R` may itself be a required portal, so deleting that leaf from
  its witness hull need not preserve the duty; and
* changing the spanning tree can change `R`.

The next admissible gate-descent step must exploit the leaf witnesses with
Perfect--Pym endpoint-preserving augmentation or a proper-minor state
transition.  It must either split a leaf witness from a nonexceptional duty
carrier, or make the gate core invariant under packet-tree rotations.  No
such conclusion is asserted here.
