# The global pair--`K_5` contact rank has a terminal sink

## Status

This is a rigorous barrier to using the following tuple as a self-contained
well-founded invariant:

\[
 (p,q,\mathcal M)\longmapsto
 \bigl(c_{pq}(\mathcal M),u_{pq}(\mathcal M),-|\mathcal M|\bigr),
\]

where `pq` is an edge, `M` is a `K_5` model in `G-{p,q}`,
`c` counts bags contacted by both poles, and `u` counts bags contacted by
at least one pole.  Here

\[
             |\mathcal M|:=\left|\bigcup_{B\in\mathcal M}V(B)\right|
\]

is the total number of model vertices, not the constant number of bags.

The example is the standard seven-connected `K_7`-minor-free graph

\[
                         G=K_2\vee I,
\]

where `I` is the icosahedron.  Among every pair for which a `K_5` model
exists, the exact global optimum is `(4,5,-8)`.  It is attained both when
one selected pole is a universal apex and when neither selected pole is an
apex.  No strict improvement exists.  Nevertheless, the terminal pair is
the *other* pair: deleting the two universal apices leaves the planar
icosahedron.

The dependency-free exhaustive checker is
`hc7_global_pair_k5_contact_rank_barrier_verify.py`.

This graph is six-colourable, not a hypothetical `HC_7` counterexample.
Consequently it does not refute a theorem using the full force of
seven-contraction-criticality.  It proves that the proposed numerical rank
does not itself supply the missing global invariant: at a maximum, the
remaining task is a sink-classification theorem which must recover a hidden
fixed pair from data not recorded by the rank.

## 1. Why the setup is valid in a hypothetical counterexample

Let `G` be a minimal `HC_7` counterexample.  For any two vertices `p,q`,

\[
             \chi(G-\{p,q\})\geq \chi(G)-2=5.
\]

Known `HC_5` therefore gives a `K_5` minor in `G-{p,q}`.  In particular
this holds for every adjacent pair.  If all five bags of such a model are
contacted by both ends of `pq`, then the five bags together with the
singletons `{p},{q}` are a literal `K_7` model.  Thus in a `K_7`-minor-free
graph

\[
                         c_{pq}(\mathcal M)\leq4.          \tag{1.1}
\]

Of course `u<=5`.  Hence `(4,5)` is the largest possible contact profile.

There is a basic logical point.  If `(p,q,M)` is chosen *globally*
lexicographically maximal, strict improvement is already impossible by
definition.  A theorem asserting

\[
 \text{`K_7`, fixed-pair terminal, or strict improvement}              \tag{1.2}
\]

therefore reduces at the chosen triple to `K_7` or a fixed-pair terminal.
In a hypothetical counterexample either conclusion is the final
contradiction.  Thus proving (1.2) at the global maximum is already the
whole missing `HC_7` theorem, not merely the construction of a rank.

## 2. The exact static sink

Label the universal vertices `a,b`.  The graph `G=K_2 vee I` is
seven-connected: the icosahedron is five-connected, and adjoining two
universal adjacent vertices raises connectivity by two.

It has no `K_7` minor.  In any putative seven-bag model, delete the at most
two bags containing `a,b`.  At least five pairwise adjacent connected bags
remain wholly in `I`, giving a `K_5` minor in the planar graph `I`, a
contradiction.

The adjacent pair `a,b` is not eligible: `G-{a,b}=I` is planar and hence
has no `K_5` minor.  It is exactly the fixed-pair terminal.

Every other edge is eligible and has one of two types: apex--icosahedron
or icosahedron--icosahedron.  For either type the checker proves:

* no `K_5` model of total order at most seven has profile `(4,5)`;
* a `K_5` model of total order eight does have profile `(4,5)`.

The search covers every one of the 54 eligible edges, rather than relying
only on symmetry.  It enumerates every connected candidate bag of the
necessary orders and every disjoint pairwise-adjacent five-tuple.

For example, with the conventional icosahedron labels from the checker,
for `(p,q)=(a,0)` the five bags are

\[
 \{1\},\ \{2\},\ \{b\},\ \{3,T\},\ \{5,6,7\};             \tag{2.1}
\]

for `(p,q)=(0,1)` they are

\[
 \{2\},\ \{a\},\ \{b\},\ \{3,T\},\ \{5,6,7\}.       \tag{2.2}
\]

In both cases four bags meet both poles and all five meet at least one.
By (1.1), trivial `u<=5`, and the exhaustive order-seven exclusion, these
models have the global lexicographic value `(4,5,-8)`.

## 3. Consequence for the proof programme

The rank is useful only as a **bounded normalization**.  It proves that one
may work in the sharp defect-one profile `(4,5)` if that profile can first
be reached.  It does not orient the equality moves which remain there and
does not identify the terminal pair.

Moreover the sharp profile is not a new structural state.  If the unique
noncommon bag is, say, contacted by `q` but not `p`, then

\[
 \{p\},\{q\},B_0,B_1,B_2,B_3,B_4
\]

are seven pairwise adjacent bags except for the single pair
`{p},B_0`.  Thus `(4,5)` is exactly a labelled `K_7^-` model.  The proposed
rank therefore hands the proof directly to the already known one-hole
near-`K_7` rotation problem; it does not rank that problem.

The icosahedral sink records the exact missing data.  The two apex bags are
common-contact singleton bags in some optimal models, but the numerical
tuple neither distinguishes them from the other common-contact bags nor
distinguishes the two eligible pole types.  Regenerating a model at a new
pair can stay on the same value until one happens to test `{a,b}`, where no
model exists and the terminal is exposed.

Therefore a viable version must augment the state with a finite,
label-faithful equality-transition object and prove one of:

1. every sink strongly connected component has one common terminal pair;
2. a proper-minor response collides with an equality class and glues a
   six-colouring; or
3. a rooted-model exchange leaves the equality class and creates `K_7`.

That is the same global confluence/sink-coherence gap already exposed by
the near-`K_7` rotation triangle.  The bare three-coordinate contact rank
does not solve it.

## Trust boundary

The example retains seven-connectivity and exact `K_7` exclusion.  Every
minor is also six-colourable: the class of two-apex graphs is minor-closed,
and deleting its two surviving apex images leaves a planar graph, so the
Four-Colour Theorem plus two fresh colours applies.  It does **not** have
chromatic number seven, and hence
does not satisfy the saturation consequences of seven-contraction-
criticality.  Full criticality could still rule out the sink, but doing so
requires a new palette-to-labelled-carrier theorem not encoded in this
potential.
