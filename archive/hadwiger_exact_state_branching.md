# Exact-state branching over a bounded attachment support

## 1. Audit of the minimum-separator depth theorem

The general theorem in `hadwiger_minimum_separator_state_depth.md` is
sound.

The points most vulnerable to a hidden gap all check out.

1. If two order-`k` adhesions overlap in `R`, deleting `R` from a
   k-connected graph leaves a `(k-|R|)`-connected graph.  Set-Menger
   gives the remaining paths, and every shared root is represented by
   a trivial path.
2. The nesting inclusions used to confine paths are correct:

\[
 S-R\subseteq O'-I',\qquad S'-R\subseteq I-O.
\]

   A minimal retained path cannot leave the annulus without meeting one
   of its terminal adhesions internally.
3. Consecutive open annuli are disjoint.  A later adhesion vertex lying
   in an earlier outer side already lies in the intervening adhesion,
   which the linkage interior avoids.  Hence propagated paths
   concatenate without unintended intersections.
4. Contracted inner root edges need not reproduce the outer root graph.
   Equality of extension families, not rooted-graph isomorphism, is
   exactly what the pumping proof requires.
5. Propagating labels through the consecutive linkages removes any
   extra factor of `k!`.

Thus the depth bounds `2^N(r,k)`, and `1024` for the actual
`K_2 join C_5` boundary, are valid.

## 2. Branching is an irredundant constraint system

There is a comparably exact theorem for parallel children, provided
their total attachment support is bounded.

Let `X` be a vertex set and let `D_1,...,D_m` be pairwise disjoint,
pairwise anticomplete nonempty vertex sets in a graph `G`, such that

\[
 N_G(D_i)\subseteq X\qquad(1\le i\le m).           \tag{2.1}
\]

Put

\[
 H=G-\bigcup_{i=1}^m D_i.
\]

For equality states on `X`, define

\[
 {\cal F}_0={\cal E}_r(H,X),\qquad
 {\cal F}_i={\cal E}_r(G[D_i\cup X],X).            \tag{2.2}
\]

Vertices of `X` with no neighbour in a child cause no problem; they
are simply isolated roots on that child side.

### Theorem 2.1 (private-state branching bound)

If `G` is r-minor-critical, then

\[
 m\le N(r,|X|)=
 \sum_{q=1}^{\min(r,|X|)} {|X|\brace q}.           \tag{2.3}
\]

More sharply, `m` is at most the number of proper equality states of
`G[X]`.

#### Proof

By (2.1), a colouring of `G` is exactly a colouring of the common
support which extends to the torso and to every child.  Thus

\[
 G\text{ is }r\text{-colourable}
 \Longleftrightarrow
 {\cal F}_0\cap\bigcap_{i=1}^m{\cal F}_i
 \ne\varnothing.                                  \tag{2.4}
\]

The intersection in (2.4) is empty.  Delete all vertices of one child
`D_i`.  This is a proper minor, so it has an r-colouring.  Its state
`phi_i` on `X` satisfies

\[
 \phi_i\in {\cal F}_0
       \cap\bigcap_{j\ne i}{\cal F}_j,
 \qquad
 \phi_i\notin{\cal F}_i.                          \tag{2.5}
\]

The last nonmembership follows because otherwise the child extension
would combine with the colouring of the deletion and colour `G`.

The private witnesses in (2.5) are pairwise distinct.  If
`phi_i=phi_j` for `i ne j`, the witness for `j` belongs to `F_i`, while
the witness for `i` does not, a contradiction.  Hence the m children
inject into the equality-state universe on `X`, proving (2.3).
\(\square\)

This argument is stronger than pigeonholing child extension *families*:
minor-criticality gives one private state per essential branch, so the
bound is the number of states, not the number of subsets of states.

## 3. Consequences

### Corollary 3.1 (one adhesion)

If all incomparable child regions are pairwise anticomplete components
behind one order-`k` adhesion `S` (so every child has all its neighbours
in `S`), then there are at most `N(r,k)` children.  No connectivity,
planarity, or defect assumption is needed beyond minor-criticality.

### Corollary 3.2 (HC7 exact boundary)

If the common support is a `K_2 join C_5` adhesion in the HC7 cell,
there are only ten proper equality states.  Hence

\[
 m\le10.                                           \tag{3.1}
\]

The defect-star and defect--Helly theorems can be much sharper in a
specified low-defect atlas, but (3.1) is uniform and requires no atlas.

### Corollary 3.3 (branching-or-large-support)

Let `D_1,...,D_m` be incomparable anticomplete child regions and put

\[
 X=\bigcup_i N_G(D_i).
\]

If `m>N(r,k)`, then `|X|>k`.  In particular, more than ten HC7 child
regions cannot all attach through one common support inducing the
specific `K_2 join C_5` boundary.  For an arbitrary seven-vertex
support the corresponding crude bound is `N(6,7)=876`, not ten.

This is the exact finite-boundary branching alternative: unbounded
branching must continually introduce new attachment vertices in the
torso.

## 4. Why rail contractions do not automatically give a branch bound

There is a tempting but invalid shortcut here.  Even if the child
boundaries can be carried to one ordered set `X` by disjoint rail
trees, contracting those trees produces a **proper minor** of `G`.
When `G` is r-minor-critical that minor is r-colourable; it is not
r-minor-critical, so Theorem 2.1 cannot be applied to it.  Moreover,
contracting a rail forces all its vertices to have one colour, whereas
colourings of the original rail need not do so.  Thus rail contraction
does not in general preserve the extension relation needed for the
private-state argument.

The precise valid substitute is the following factorization statement.

### Proposition 4.1 (exact common-root factorization)

Suppose the original graph, without any contraction, has a common root
set `X` and extension families `F_0,F_1,...,F_m` such that

\[
 G\text{ is r-colourable}
 \Longleftrightarrow F_0\cap\bigcap_iF_i\ne\varnothing,
\]

and, after deleting child `i`, its colourability is equivalent to
`F_0 intersection (intersection over j not equal i of F_j)` being
nonempty.  If every child deletion is a proper minor and `G` is
r-minor-critical, then `m` is at most the number of equality states on
`X`.

#### Proof

Choose from each child deletion a state in all factors except `F_i`.
It cannot lie in `F_i`, and the resulting private witnesses are
pairwise distinct exactly as in (2.5). \(\square\)

Consequently a rail-star theorem requires an additional proof that the
**original** colour-extension relation factors through the transported
root states.  Separate child-to-parent linkages do not give this:
linkages may overlap in the torso, and even simultaneous disjoint rails
can carry nonconstant colour sequences.  If a proposed rail contraction
really preserves the complete extension relation, then that proper
minor is still non-r-colourable and already contradicts
minor-criticality; no separate branching theorem is needed.

## 5. Why distinct-support branching is genuinely different

Connectivity alone does not bound the number of incomparable minimum
cuts with distinct adhesions.

### Example 5.1 (bounded-degree clique-tree branching)

For every `k>=3`, start with copies of `K_{k+1}` indexed by a binary
tree of arbitrarily large order and maximum degree at most three.  Glue
bags along distinct `K_k` facets according to the tree, using no facet
for two tree edges.  The result is a k-tree and is k-connected.  Each
used facet separates precisely the two sides of its tree edge, while
the leaf sides give arbitrarily many pairwise incomparable child
separations.  Thus every displayed separator produces only two
components, certainly no more than k, and the rooted leaf pieces can
all be isomorphic.

Thus neither k-connectivity, bounded component count at each adhesion,
nor repetition of an abstract rooted piece type bounds branching when
the root sets themselves move through an unbounded torso.

At the state level the same obstruction is familiar from minimally
unsatisfiable bounded-arity systems.  An odd cycle of two-colour
inequality constraints has arbitrarily many identical binary
constraints; deleting any one makes the system satisfiable.  What
prevents the private-state injection from bounding their number is that
the union of their variable supports grows with the cycle.

These examples are not asserted to be Hadwiger counterexamples or
r-minor-critical graphs.  They falsify the purely structural inference
that bounded cut order plus bounded local state type controls branching.
Minor-critical contractions, the planar portal geometry, or a bounded
common support must still be used.

## 6. Relation with the defect-star theorem

The private-state theorem and the existing defect-star theorem control
different branching mechanisms.

* Theorem 2.1 controls arbitrary exact colour constraints when all
  branches attach through a bounded common support.
* The defect-star theorem controls branches produced by deleting a
  small internal cut from one full shore.  Connectivity bounds each
  leaf defect, fullness makes the total defect intersection empty, and
  the bad quotient atlas bounds the resulting star number.

For a laminar hierarchy, the combined rigorous alternative is:

1. a root-to-leaf chain has length below the exact-state depth bound;
2. a node with all children supported on one k-frame has at most
   `N(r,k)` children (ten for `K_2 join C_5`);
3. a low-defect internal split has branching bounded by its defect-star
   number; or
4. the child adhesions use more than k torso vertices, producing a
   distributed-portal configuration not controlled by finite boundary
   states alone.

Outcome 4 is the precise remaining branching gap.  Calling it a
routine common-state or Helly argument would be incorrect.
