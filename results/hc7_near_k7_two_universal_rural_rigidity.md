# Two-universal rigidity: the join architecture is exactly rural

## Status

This is a short structural lemma for the exact path-capacity
falsification gate.  It proves that the standard unbounded static family
`K_2 \vee H` cannot falsify a `K_7`-or-two-apex conclusion: under the
ambient seven-connectivity and `K_7`-minor exclusion hypotheses, its
remainder `H` is forced to be planar.

It does **not** prove the path-capacity exchange theorem for arbitrary
coherent carriers.  In particular it uses two literal adjacent universal
vertices, much more than row support by at most three crossing pieces.

## Theorem 1 (exact two-universal characterization)

Let `a,b` be adjacent vertices and let `H` be a graph disjoint from them.
Put

\[
                       G=K_2\vee H,
\]

where `K_2=G[{a,b}]`.  Then:

1. `G` is `K_7`-minor-free if and only if `H` is `K_5`-minor-free;
2. `G` is seven-connected if and only if `H` is five-connected.

Consequently, if `G` is seven-connected and `K_7`-minor-free, then `H`
is planar and `{a,b}` is one global two-apex pair.

### Proof

If `H` has a `K_5` model, its five bags together with the singleton bags
`{a}` and `{b}` form a `K_7` model in `G`.

Conversely, suppose `G` has a `K_7` model.  At most two branch bags of
the model contain `a` or `b`.  Delete those bags.  At least five pairwise
adjacent connected branch bags remain, and they lie wholly in `H`.
They form a `K_5` model in `H`.  This proves assertion 1.

If `G` is seven-connected, then `|V(G)|>=8`, so `|V(H)|>=6`.  If `H`
has a separator `S` of order at most four, then
`S union {a,b}` is a separator of `G` of order at most six.  Hence
seven-connectivity of `G` implies five-connectivity of `H`; the order
condition is automatic as well, since `|H|<=5` would give `|G|<=7`,
which is not seven-connected under the standard convention.

For the converse, assume `H` is five-connected and delete at most six
vertices from `G`.  If at least one of `a,b` remains, that universal
vertex joins all remaining vertices.  If both are deleted, at most four
vertices of `H` were also deleted, and the remaining graph is connected
by five-connectivity of `H`.  Thus `G` is seven-connected, proving
assertion 2.

Under the two ambient hypotheses, assertions 1 and 2 say that `H` is a
five-connected `K_5`-minor-free graph.  The 4-connected case of Wagner's
`K_5`-minor structure theorem says that every 4-connected
`K_5`-minor-free graph is planar.  Therefore `H` is planar.  Deleting
the fixed pair `{a,b}` from `G` leaves precisely `H`, so the pair is a
global two-apex certificate.  \(\square\)

## Sharpness and implication for the capacity bottleneck

Conversely, every five-connected planar `H` gives a seven-connected,
`K_7`-minor-free graph `K_2\vee H`: the preceding proof supplies both
claims.  Thus the geodesic-icosahedral and ordinary icosahedral join
examples are not isolated.  They are the full two-universal rural
architecture.

The proof also identifies the exact point at which this architecture is
too rigid to challenge the proposed path-capacity dichotomy.  The two
apex vertices do not arise from a local choice of a deficient row at
each path cut; they are literal universal vertices, so every local rural
piece already uses the same fixed pair.  Any genuine static
counterarchitecture must therefore abandon at least one of the two
features:

* literal universality of the common pair; or
* one common pair across all pieces.

The second option is precisely the incompatible-rural-gluing problem.
The known `K_{3,3,3}` example realizes it only at connectivity six.  The
present theorem explains why the connectivity deficit cannot be repaired
by replacing that architecture with two literal adjacent universal
vertices: the remainder is then forced to be planar.

There is also no escape by replacing the universal edge with a larger
universal carrier, even a disconnected one.

### Proposition 2 (a third universal vertex forces `K_7`)

Let `H` be five-connected and let `R` be any graph of order at least
three.  Then `R\vee H` contains a `K_7` minor.

#### Proof

Choose distinct vertices `r_1,r_2,r_3` of `R` and distinct vertices
`h_1,h_2` of `H`.  The graph `H-{h_1,h_2}` is three-connected.  Every
three-connected graph contains a `K_4` minor, so let
`Q_1,Q_2,Q_3,Q_4` be a `K_4` model in `H-{h_1,h_2}`.

Now use the seven bags

\[
       \{r_1,h_1\},\quad \{r_2,h_2\},\quad \{r_3\},\quad
       Q_1,Q_2,Q_3,Q_4.
\]

The first two bags are connected through the join edges `r_1h_1` and
`r_2h_2`.  The first three bags are pairwise adjacent: use the join
edges `r_1h_2`, `h_1r_3`, and `h_2r_3`.  They are each adjacent to every
`Q_i` through their `R`-vertex, and the four `Q_i` are pairwise adjacent.
These are the branch sets of a `K_7` model.  \(\square\)

Thus, over a five-connected remainder, the entire universal vertex set
of a `K_7`-minor-free graph has order at most two.  If its two vertices
are adjacent, they are exactly the universal pair of Theorem 1 and the
remainder is planar.  This mixed-bag model is the precise reason that an
unbounded universal replacement of the two apex vertices cannot furnish
the desired non-two-apex counterarchitecture.

Finally, the capacity hypothesis alone is much weaker than the theorem's
universal-pair hypothesis.  A row supported by at most three crossing
pieces does not bound the number of vertices in those pieces and does
not give a separator of order at most three.  Therefore this lemma closes
the canonical join family but cannot be cited as a proof of the general
capacity-state web exchange.
