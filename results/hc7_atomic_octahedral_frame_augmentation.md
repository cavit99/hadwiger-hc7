# The atomic octahedral frame needs only one adjacency augmentation

**Status:** written proof; separate internal audit GREEN.

The hard nonbranch atomic collision has an exact eight-bag quotient.  This
note identifies its smallest valid completion operation and eliminates two
natural counterexample families.  It does not prove that eight-connectivity
forces that operation.

## 1. The extremal quotient

Let

\[
 J=K_8-\{xe,ab,cd\}=K_2\vee K_{2,2,2},              \tag{1.1}
\]

where `f,g` are the two vertices in the complete factor and the three
parts of the octahedral factor are `{x,e},{a,b},{c,d}`.

### Lemma 1.1 (one absent edge is enough)

The graph `J` has no `K_7` minor.  Adding any one of `xe,ab,cd`
creates an explicit `K_7` minor.

#### Proof

The clique number of `J` is five: a clique contains at most one endpoint
of each of the three absent edges, together with `f,g`.  A `K_7`-minor
model on eight vertices would have either seven singleton branch sets or
six singleton branch sets and one branch set of order two.  The former
requires a `K_7` subgraph and the latter requires the six singleton
vertices to form a `K_6` subgraph.  Neither exists.

After adding `xe`, use

\[
 \{x\},\ \{e\},\ \{a,c\},\ \{b\},\ \{d\},\ \{f\},\ \{g\}.
                                                               \tag{1.2}
\]

The merged set repairs both `ab` and `cd`: it meets `b` through
`cb` and `d` through `ad`.  Every other adjacency is present.
After adding `ab`, use

\[
 \{x\},\ \{a\},\ \{b\},\ \{c,e\},\ \{d\},\ \{f\},\ \{g\};
                                                               \tag{1.3}
\]

the merged set meets `{d}` through the edge `ed`, repairing the absent
`cd` adjacency.
Interchanging `ab` and `cd` gives the third case.  \(\square\)

The graph has 25 edges, equal to Mader's extremal value
`5|V(J)|-15` for a `K_7`-minor-free graph on eight vertices.  Lemma
1.1 gives the label-preserving fact needed here; density alone would not
identify its three critical nonedges.

## 2. Exact landing from an atomic collision

In the disjoint-demand case of the
[atomic rounding theorem](hc7_atomic_weak_k7_immersion_rounding.md), suppose
the collision vertex `x` misses the clean bag `D_e` and meets the other
two clean bags `D_f,D_g`.  If the host has no `K_7` minor, Corollary 3.6
there says that the two route-defect pairs are genuinely anticomplete.
Proposition 3.7 then gives a spanning common-frame partition

\[
 \{x\},\ D'_e,\ D'_a,D'_b,D'_c,D'_d,D'_f,D'_g
 \qquad\text{where }D'_e=\{v_e\}.                       \tag{2.1}
\]

whose bag-adjacency graph is exactly `J`.

Consequently a model-compatible reallocation which produces another
eight-bag partition with all the old labelled adjacencies and any one of

\[
 E_G(\{x\},D'_e)\ne\varnothing,\qquad
 E_G(D'_a,D'_b)\ne\varnothing,\qquad
 E_G(D'_c,D'_d)\ne\varnothing                            \tag{2.2}
\]

is immediately terminal by Lemma 1.1.  A constructive proof should
therefore seek one ownership-preserving missing-pair augmentation.  Asking
for three independent repairs or generic three-linkedness is unnecessarily
strong.

## 3. Clean paths and the canonical three-subgraph reduction

Write

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},
                                                        \tag{3.1}
\]

on vertices `a,b,c,d,e,f,g,x`.  Let `T` be a subdivision of `H_0`
whose branch vertices retain these labels, and write `T_{uv}` for the
subdivided route corresponding to an edge `uv` of `H_0`.
In the disjoint-demand atomic collision, the union of the immersion routes
is exactly such a subdivision: split each of the two colliding routes at
`x`, and retain every other route unchanged.

### Lemma 3.1 (a `T`-clean path closes the model)

If `G` contains an `a`--`b` path `Q` whose internal vertices avoid
`V(T)`, then `G` contains a `K_7` minor.

#### Proof

Split the internal vertices of `Q` across one edge of `Q`, putting the
initial segment with `a` and the terminal segment with `b`; call the two
connected sets `A` and `B`.  They are disjoint and adjacent.  Put `c`,
the whole route `T_{cx}`, and all internal vertices of `T_{xd}` into a
third connected set `C_x`, and initially take the four remaining sets to
be `{d},{e},{f},{g}`.

For every other route of `T`, assign all its internal vertices to one of
the branch sets containing one of its ends.  Each assignment attaches a
path at its chosen end, so all seven sets remain connected; the last edge
of the route supplies the adjacency to the set at the other end.  The
routes are internally disjoint, and `Q-V(T)` is disjoint from all of them,
so the seven sets are disjoint.  The path `Q` supplies the formerly absent
`ab` adjacency, while `T_{xd}` supplies the formerly absent `cd`
adjacency between `C_x` and the set containing `d`.  Every other pair is
joined by its route in `T`.  Thus these sets form a `K_7`-minor model.
\(\square\)

In particular, if the displayed copy of `H_0` is literal rather than
subdivided and `G` is eight-connected, delete `c,d,e,f,g,x`.  The
remaining graph is connected, so it contains an `a`--`b` path whose
interior avoids the other six vertices.  Lemma 3.1 then gives a `K_7`
minor.  Hence the unresolved case must genuinely exploit the internal
vertices of the provenance routes.

There is also a canonical way to expose exactly where that exploitation
can occur.  Put

\[
\begin{aligned}
 P_e={}&\{e\}\cup\!\bigcup_{r\in\{a,b,c,d,f,g\}}\!\operatorname{int}(T_{er}),\\
 P_f={}&\{f\}\cup\!\bigcup_{r\in\{a,b,c,d,g\}}\!\operatorname{int}(T_{fr}),\\
 P_g={}&\{g\}\cup\!\bigcup_{r\in\{a,b,c,d\}}\!\operatorname{int}(T_{gr}),
                                                        \tag{3.2}
\end{aligned}
\]

and let `L=G-(P_e\cup P_f\cup P_g)`.  The three sets are disjoint and
connected.  They are pairwise adjacent, and each is adjacent to every one
of the literal roots `a,b,c,d`.  The graph `L` contains the subdivided
wheel with rim `a,c,b,d,a` and hub `x`.

### Theorem 3.2 (rooted-`K_4` dichotomy)

If `L` is four-connected, then either `G` contains a `K_7` minor, or `L`
has a planar embedding in which `a,b,c,d` lie on one face.

#### Proof

The rooted-`K_4` theorem of Fabila-Monroy and Wood, Theorem 6 of
[*Rooted `K_4`-Minors*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i2p64/pdf/),
Electron. J. Combin. **20**(2) (2013), Paper 64, says that a
four-connected graph either has a `K_4`-minor model whose four branch
sets contain the prescribed vertices `a,b,c,d`, respectively, or has the
stated planar cofacial embedding.  In the former case, add
`P_e,P_f,P_g`.  These three sets are pairwise adjacent and each meets all
four rooted branch sets through its edge to the corresponding literal
root.  The resulting seven branch sets form a `K_7` model.  \(\square\)

### Corollary 3.3 (five paths through three support sets)

Suppose that `G` is eight-connected and `L` is not four-connected.  Then
there are a set `S\subseteq V(L)`, `|S|\le3`, and a component `U` of
`L-S` such that, for `W=V(L)-(U\cup S)`, at least five paths from `U` to
`W` are pairwise internally disjoint and have all internal vertices in
`P_e\cup P_f\cup P_g`.

#### Proof

The graph `L` contains the five distinct branch vertices of the displayed
subdivided wheel.  Since it is not four-connected, there is a set `S`,
`|S|\le3`, such that `L-S` is disconnected; take `S=\varnothing` if `L`
itself is disconnected.  Choose a component `U` of `L-S`, put
`W=V(L)-(U\cup S)`, and choose `u\in U` and `w\in W`.  There is no
`L`-edge between `U` and `W`, so `u,w` are nonadjacent.  Eight-connectivity
and Menger's theorem give eight internally disjoint `u`--`w` paths in
`G`.  At most `|S|` of them meet `S` internally, so at least five avoid
`S`.  On each such path, take the subpath from the last vertex in `U`
before its first vertex in `W` to that first vertex in `W`.  Its internal
vertices lie outside `L`, hence in `P_e\cup P_f\cup P_g`.  The chosen
subpaths inherit internal disjointness.  \(\square\)

Corollary 3.3 deliberately makes no label-allocation claim: all five
paths can first meet the same support set, and splitting that set can lose
its connection to a literal root.  Decoding these paths, or the bridge
attachment intervals in the planar cofacial outcome of Theorem 3.2, into
one ownership-preserving missing-pair augmentation is the remaining
structural step.  Counting five paths by itself does not perform that
decoding.

## 4. Complete substitutions cannot be obstructions

Call a graph a **complete substitution of `J`** if each vertex `z` of
`J` is replaced by a nonempty connected bag `B_z`, every two bags
corresponding to an edge of `J` are made complete to one another, and
the three antipodal bag pairs are anticomplete.

### Theorem 4.1

Every complete substitution of `J` in which some bag has more than one
vertex contains a `K_7` minor.

#### Proof

A nontrivial connected bag contains an edge `uv`.

First suppose that the bag is `B_f` or `B_g`, say `B_f`.  Use
`{u},{v}`, the connected bag `B_g`, and any `K_4`-minor model in the
octahedral six-bag substitution.  Such a model already exists in the
quotient; for example the four quotient branch sets

\[
                   \{x,a\},\quad\{e,c\},\quad\{b\},\quad\{d\}
                                                               \tag{4.1}
\]

are pairwise adjacent and connected.  Completeness between allowed bag
pairs makes `{u},{v},B_g` pairwise adjacent and adjacent to all four
lifted branch sets.  These seven sets give a `K_7` model.

Now suppose that `uv` lies in one of the six octahedral bags, say
`B_x`.  The four bags belonging to the other two antipodal pairs induce
a complete substitution of a four-cycle.  They contain a `K_3` minor;
with the displayed labels one may use

\[
                         B_a\cup B_c,\quad B_b,\quad B_d. \tag{4.2}
\]

Both `u` and `v` are adjacent to every set in (4.2), and the two
complete-factor bags `B_f,B_g` are adjacent to all five of these branch
sets and to one another.  Thus

\[
             \{u\},\ \{v\},\ B_a\cup B_c,\ B_b,\ B_d,\ B_f,\ B_g
                                                               \tag{4.3}
\]

is a `K_7` model.  The other five octahedral bags are symmetric.
\(\square\)

Thus a counterexample cannot be a clique or lexicographic blow-up of the
octahedral frame.  It must use sparse, vertex-specific cross-bag contacts.

## 5. The icosahedral barrier example has no small monotone augmentation

Let `I` be the icosahedral graph and `G_0=K_2\vee I`.  Thus
`|V(G_0)|=14` and `|E(G_0)|=55`.

### Theorem 5.1

Let `H` be an eight-connected simple graph containing `G_0` as a
subgraph on fourteen designated vertices.  If

\[
                      1\le |V(H)-V(G_0)|\le7,          \tag{5.1}
\]

then `H` contains a `K_7` minor.

#### Proof

Put `r=|V(H)-V(G_0)|` and let `W` be the new vertex set.  Every vertex
of `W` has degree at least eight.  If `m_W` is the number of edges with
at least one endpoint in `W`, then

\[
 \begin{aligned}
 m_W
 &=\sum_{w\in W}d_H(w)-|E(H[W])|\\
 &\ge8r-\binom r2.                                    \tag{5.2}
 \end{aligned}
\]

Hence

\[
                 |E(H)|\ge55+8r-\binom r2.             \tag{5.3}
\]

The separately audited
[eight-connected extremal lemma](hc7_eight_connected_order_bound.md#lemma-21)
says that an eight-connected `K_7`-minor-free graph on `n` vertices has
at most `5n-16` edges.  For `n=14+r`, the difference between the lower
bound in (5.3) and that upper bound is

\[
                  1+3r-\binom r2,                       \tag{5.4}
\]

which is positive for every integer `1\le r\le7`.  Therefore `H`
cannot be `K_7`-minor-free.  \(\square\)

This is a monotone-augmentation result: all edges of `G_0` must be
retained.  It implies that a counterexample obtained only by adjoining
vertices to the sharp fourteen-vertex host must use at least eight new
vertices.
It does not exclude a smaller graph obtained by deleting or rewiring old
edges.

For comparison, the separately audited order-sixteen exclusion in the
same note shows that an arbitrary eight-connected `K_7`-minor-free graph
has at least seventeen vertices.  At order seventeen, Lemma 2.1 of that
note and minimum degree eight give 68 or 69 edges; in the first case the
graph is eight-regular, while in the second its total degree excess over
eight is two.  This is the first sharp general search window, but it does
not encode the spanning `J`-model.

## 6. Exact remaining inference

The positive theorem still needed for the atomic configuration is:

> In an eight-connected host with a spanning `J`-model chosen under a
> declared ownership-minimal potential, either reallocate the bags to
> realize one of the three pairs in (2.2), or return a vertex cut of order
> at most seven.

This statement is stronger than ordinary linkage because every path and
branch-set split must preserve the other seven named bags.  Conversely, a
generic claim that every eight-connected graph containing a
`K_7`-minus-one-edge minor contains `K_7` is too broad: the audited
[augmentation-hardness reduction](../barriers/hc7_eight_connected_near_k7_augmentation_hardness.md)
shows that it would imply the open assertion that every seven-connected
graph contains a `K_6` minor.

The closest primary structural input is Hayashi, Theorem 1.2(5) and
Theorem 1.3 of
[*Linking four vertices in graphs of large connectivity*](https://doi.org/10.1016/j.jctb.2021.12.007),
J. Combin. Theory Ser. B **154** (2022), 136--174.  The former gives, for
a six-connected graph and four prescribed vertices, a rooted
`K_4`-subdivision or a discoid decomposition; the latter guarantees the
rooted subdivision in every seven-connected graph.  Those theorems do not
preserve the three pre-existing connected support sets or the bag
ownership of a spanning model.  The missing implication is therefore an
ownership-preserving bridge-attachment theorem, not another application
of unlabelled linkedness.

Theorems 4.1 and 5.1 rule out broad structured falsifiers, while Lemma 3.1
and Theorem 3.2 isolate the route-interior and planar cofacial cases.  They
do not prove this remaining inference, the single-collision terminal
disjunction, or `HC_7`.
