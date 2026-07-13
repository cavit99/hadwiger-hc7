# Two colourful portal sets: exact model-or-capacity theorem

## Status

This note records a target-slot/Rado formulation of the contact problem
for a **pre-existing** clique model.  The cleaner unit-bag formulation in
`hadwiger_unit_bag_linkage_and_rotation.md` supersedes it when whole model
bags are to have capacity one; the present version remains useful when
individual boundary slots must be retained.

The theorem is deliberately phrased as an exact dichotomy.  Either all
bags of the model can be made to meet both portal sets, or a specified
subfamily of bags has a strict model-relative linkage-capacity defect.
The defect is witnessed by an explicit separator in an auxiliary network.

No claim is made that this separator is automatically colour-gluable in
the ambient contraction-critical graph.  Proving that additional step is
precisely the remaining uniform obstruction.

## 1. The one-set contact theorem

Let `K` be a graph and let

\[
                     \mathcal B=(B_1,\ldots,B_m)
\]

be pairwise disjoint connected sets.  (For the application they are the
bags of a `K_m`-model.)  Put `B=union_i B_i`.

Fix a portal set `X subseteq V(K)`.  A bag already meeting `X` is called
`X`-hit.  For every bag which is not `X`-hit, create one target slot
`t_{i,v}` for each vertex `v in B_i` having a neighbour outside `B`.
Form a directed network `D_X(mathcal B)` as follows:

* retain the vertices of `K-B` and replace each edge among them by the two
  opposite arcs;
* add the target slots as sinks;
* for every edge `yv` with `y outside B` and `v in B_i`, add the arc
  `y t_{i,v}`;
* use `X-B` as the source set.

For a set `I` of non-`X`-hit bag indices, let `A_I` be the union of the
target slots belonging to those bags, and define

\[
 \rho_X(I)=\max\{\text{number of vertex-disjoint directed paths from
 distinct sources in }X-B\text{ to distinct vertices of }A_I\}.
                                                        \tag{1.1}
\]

The target slots have capacity one, as do all ordinary vertices.

### Theorem 1.1 (root all bags, or expose a capacity defect)

Exactly one of the following alternatives holds.

1. The bags can be enlarged, preserving disjointness, connectedness and
   all old bag adjacencies, so that every enlarged bag meets `X`.
2. There is a nonempty set `I` of non-`X`-hit bags such that

   \[
                              \rho_X(I)<|I|.            \tag{1.2}
   \]

   Equivalently, by directed vertex-Menger, fewer than `|I|` vertices or
   target slots meet every model-avoiding path from `X-B` to the external
   boundary of the bags indexed by `I`.

#### Proof

The subsets of target slots which can be linked from `X-B` by
vertex-disjoint paths are the independent sets of a strict gammoid.  Its
rank on `A_I` is exactly `rho_X(I)`.

Partition the target slots according to their bags.  Rado's transversal
theorem (the matroidal form of Hall's theorem) says that one can select
one target slot from every non-`X`-hit bag so that the selected set is
independent in the gammoid if and only if

\[
                              \rho_X(I)\ge |I|           \tag{1.3}
\]

for every subfamily `I`.

If (1.3) fails, (1.2) is the promised certificate.  Directed Menger gives
the stated separator form of the same rank defect.

If (1.3) holds, take the disjoint linkage to a transversal of target
slots.  Replace each terminal arc `y t_{i,v}` by the edge `yv`.  We
obtain pairwise vertex-disjoint paths, one from `X-B` to every previously
unhit `B_i`, whose internal vertices avoid all old bags.  Trim paths, if
necessary, so that no unused source is internal to a path.  Absorb each
path into its terminal bag.  The enlarged bags are connected and
pairwise disjoint; every old interbag edge remains; and each bag now meets
`X`.  This is alternative 1.  \(\square\)

### Remark 1.2 (why the partition condition is necessary)

Ordinary Menger from `X` to `B` is insufficient.  It may send many paths
to one bag and none to another.  The inequalities (1.3), one for every
subfamily of labelled bags, are the exact Hall-type conditions enforcing
one contact per bag.

## 2. The simultaneous two-set theorem

### Theorem 2.1 (biportal model or a named capacity cut)

Let `mathcal B=(B_1,...,B_m)` be a clique model in `K`, and let
`X,Y subseteq V(K)`.  Then one of the following holds.

1. There is a `K_m`-model `mathcal B'` obtained from `mathcal B` by
   disjoint path absorption such that every bag of `mathcal B'` meets
   both `X` and `Y`.
2. For one of the two portal sets, at one of the two successive absorption
   stages, there is a nonempty labelled subfamily `I` whose auxiliary
   rank satisfies `rho(I)<|I|`; a separator of order `rho(I)` in the
   corresponding target-slot network certifies the failure.

#### Proof

Apply Theorem 1.1 first to `X`.  If it returns a defect, we are in
alternative 2.  Otherwise obtain an `X`-hit clique model.  Apply Theorem
1.1 to `Y` using these enlarged bags.  Absorbing the second linkage never
removes the existing `X` vertices, so success gives alternative 1; failure
gives the named second-stage defect.  \(\square\)

This theorem uses neither colourfulness nor a colouring theorem.  In the
bipartite-compression application, one first obtains an unrooted
`K_{r-2}`-model in the `(r-2)`-slice (for example from an already proved
lower-parameter ordinary Hadwiger theorem) and applies Theorem 2.1 to the
two parity portal sets.

## 3. The separator alternative is genuinely necessary

For every `q>=2`, let `J` be the disjoint union of two copies `L,R` of
`K_q`, let `X=V(L)`, and let `Y=V(R)`.  Then:

* `J` is `q`-colourable;
* both `X` and `Y` are `q`-colourful;
* `J` has no `K_{q+1}` minor;
* there is no `K_q`-model every bag of which meets both `X` and `Y`.

The last assertion is immediate because no connected set meets both
components.  If a connected example is preferred, join the two cliques
by one bridge.  Every connected set meeting both sides then contains that
bridge, so two such sets cannot be disjoint; again no biportal `K_q`
model exists for `q>=2`, and the bridge is the capacity defect.

By Proposition 2.2 of
`hadwiger_uniform_bipartite_compression_barrier.md`, either example occurs
as the two parity portal sets in the common `(r-2)`-slice of an exact
induced-edge contraction, with `r=q+2`.  Therefore simultaneous
colourfulness and common contraction origin do not eliminate the
separator outcome.

## 4. Exact remaining gluing problem

In a hypothetical minor-critical Hadwiger counterexample, Theorem 2.1
reduces the rooted step to the following concrete task.

> **Capacity-cut gluing problem.**  Given a labelled subfamily `I` of
> clique-model bags and a target-slot separator of order `<|I|`, prove
> that the separator lifts to an ambient separation whose boundary
> colourings can be aligned, or use the omitted colour classes and the
> opposite parity side to augment the model.

The auxiliary separator is not automatically a separator of the whole
host: paths may run through the contracted bipartite bag, through the two
omitted colour classes, or through other clique bags which the target-slot
network treats as forbidden.  Any proof which silently identifies the
two separators is invalid.

Thus Theorem 2.1 gives an exact, label-preserving uniform dichotomy, but
the transition from a model-relative capacity cut to a colour-gluable
ambient adhesion remains the substantive missing lemma.

## 5. Audit boundaries

1. Target slots are sinks; paths are not allowed to travel through one
   old model bag on their way to another.
2. Bags already meeting the current portal set are removed from the
   transversal demand.  Their vertices are not silently reused as paths
   to other bags.
3. Rado's theorem, not ordinary Hall or ordinary Menger alone, enforces
   one endpoint in each labelled bag.
4. Absorbed paths avoid all old bags except their own terminal bag, so
   branch-set disjointness is preserved.
5. The second absorption stage is performed relative to the already
   enlarged first-stage bags.
6. The separator certificate is model-relative.  No colour-gluing claim
   is made without a separate ambient lifting argument.
