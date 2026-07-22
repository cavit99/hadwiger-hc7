# A rejection-cut edge forces an alternating full-component cycle

**Status:** written proof; separately audited GREEN.  This theorem does not
prove `HC_7`.  It replaces one isolated opposite-shore
path by a canonical cyclic obstruction built from two fixed shore
extensions.

## 1. Setup

Let `G` be a finite graph, let `u` be a vertex, and put

\[
                         X=N_G(u),\qquad H=G[X].
\]

Assume that `G-N[u]` has exactly two components `C,D`.  Let `alpha,beta`
be two of five named boundary colours, and let

\[
                         W_0,\ldots,W_t                 \tag{1.1}
\]

be the connected components of `H[alpha,beta]`.  For
`T subseteq I={0,...,t}`, write `theta^T` for the boundary colouring
obtained from a proper five-colouring `theta` of `H` by interchanging
`alpha,beta` on exactly the sets `W_k` with `k in T`.
We freely identify a subset of `I` with its incidence vector in
`mathbf F_2^I`; vector addition is symmetric difference.

Fix `i in I`.  Suppose that

1. `theta` extends to a proper six-colouring `c_D` of `G[D union X]`;
2. `theta^{\{i\}}` extends to a proper six-colouring `c_C` of
   `G[C union X]`; and
3. no proper five-colouring of `H` extends through both `C` and `D`.

The third condition holds in the exact common-root residue: a common
labelled boundary colouring could be glued across the anticomplete
components and the sixth colour, absent from `X`, could be assigned to
`u`, contrary to `chi(G)=7`.

For a partition `mathcal P` of `I`, let

\[
 L(mathcal P)=\operatorname{span}_{\mathbf F_2}
       \{\mathbf 1_B:B in mathcal P\}\subseteq\mathbf F_2^I. \tag{1.2}
\]

Thus `L(mathcal P)` consists exactly of the unions of blocks of
`mathcal P`, represented by their incidence vectors.

## 2. The two full-component partitions

In the fixed colouring `c_D`, declare `k equivalent_D l` when `W_k` and
`W_l` lie in the same connected component of the subgraph induced by
colours `alpha,beta`.  This defines a partition `mathcal P_D` of `I`.
Define `mathcal P_C` analogously from the one fixed colouring `c_C`.
The underlying sets `W_k` are the same in the two definitions: swapping
the names `alpha,beta` on `W_i` does not change `H[alpha,beta]` or its
connected components.

### Lemma 2.1 (all block unions are switchable)

Every vector `p in L(mathcal P_D)` gives a boundary colouring `theta^p`
which extends through `D`.  Every vector `q in L(mathcal P_C)` gives a
boundary colouring

\[
                         theta^{e_i+q}                    \tag{2.1}
\]

which extends through `C`.

#### Proof

Each `W_k` is connected in `H[alpha,beta]`, so it lies wholly in one full
`alpha`--`beta` component of either shore colouring.  The intersection of
such a full component with `X` is therefore the union of the `W_k` in one
block of the corresponding partition.

Interchanging `alpha,beta` on one full two-colour component preserves
properness.  Distinct full components are disjoint, so any chosen union of
them can be interchanged simultaneously.  In `c_D` this changes the
boundary precisely on a union of blocks of `mathcal P_D`; in `c_C` it
changes the boundary, relative to `theta^{\{i\}}`, precisely on a union of
blocks of `mathcal P_C`.  This proves both assertions.  \(\square\)

### Lemma 2.2 (the two switch spaces are disjoint affine cosets)

Put `e_i=mathbf 1_{\{i\}}`.  Then

\[
 L(mathcal P_D)\cap\bigl(e_i+L(mathcal P_C)\bigr)=\varnothing, \tag{2.2}
\]

and hence

\[
                         e_i\notin
 L(mathcal P_D)+L(mathcal P_C).                         \tag{2.3}
\]

#### Proof

If `v` belonged to the intersection in (2.2), Lemma 2.1 would give a
`D`-extension and a `C`-extension of the same *labelled* boundary
colouring `theta^v`.  The two exterior components are anticomplete, so the
extensions glue on `X`.  The boundary uses only the five named colours;
give `u` the sixth colour.  This is a proper six-colouring of `G`, contrary
to hypothesis 3.  Thus (2.2) holds.

Over `mathbf F_2`, an equality `e_i=p+q` with
`p in L(mathcal P_D)` and `q in L(mathcal P_C)` is equivalent to
`p=e_i+q`, which would put `p` in the intersection (2.2).  This proves
(2.3).  \(\square\)

## 3. The alternating-cycle theorem

Form a bipartite multigraph `Gamma=Gamma(mathcal P_D,mathcal P_C)` as
follows.  Its two vertex classes are the blocks of `mathcal P_D` and the
blocks of `mathcal P_C`.  For each `k in I`, put one edge, also labelled
`k`, between the two blocks which contain `k`.  Parallel edges are retained.

### Theorem 3.1 (affine incompatibility is exactly a cyclic edge)

Under the setup of Section 1, the edge `i` of `Gamma` lies on a cycle.
Here two parallel edges count as a cycle of length two.

Equivalently, if edge `i` were a bridge, the two fixed extensions would
explicitly produce one common labelled boundary colouring and hence a
proper six-colouring of `G`.

#### Proof

Work over `mathbf F_2` and index the coordinates by the edge set `I` of
`Gamma`.  The incidence row of a `mathcal P_D`-vertex is the block vector
`mathbf 1_B`; the same is true for a `mathcal P_C`-vertex.  Consequently
the row space of the unoriented incidence matrix of `Gamma` is exactly

\[
                         L(mathcal P_D)+L(mathcal P_C). \tag{3.1}
\]

The incidence row space of a finite multigraph over `mathbf F_2` is its
cut space.  A one-edge vector `e_i` belongs to the cut space if and only if
edge `i` is a bridge.  Indeed, if `i` is a bridge, the vertex set of one
component of `Gamma-i` has cut exactly `{i}`.  Conversely, if a vertex set
has cut exactly `{i}`, the ends of `i` lie on opposite sides and no other
edge crosses, so deleting `i` disconnects them.  This argument also covers
parallel edges: neither member of a parallel pair is a bridge.

Lemma 2.2 says that `e_i` is not in the row space (3.1).  Thus `i` is not
a bridge.  Every nonbridge edge of a finite multigraph lies on a cycle,
with a parallel pair giving the possible two-edge cycle.  \(\square\)

### Corollary 3.2 (literal two-shore ownership)

Choose a shortest cycle of `Gamma` containing `i`.  For a block `B` of
`mathcal P_D`, let `K_B^D` be the full `alpha`--`beta` component of
`c_D` represented by `B`; define `K_Q^C` analogously for a block `Q` of
`mathcal P_C`.  The cycle yields a cyclically ordered family of connected
subgraphs

\[
 K_{B_1}^D,K_{Q_1}^C,K_{B_2}^D,K_{Q_2}^C,\ldots,
 K_{B_m}^D,K_{Q_m}^C,                                  \tag{3.2}
\]

with all of the following literal properties.

1. Every `D`-component in (3.2) comes from the one fixed colouring `c_D`,
   and every `C`-component comes from the one fixed colouring `c_C`.
2. The part of `K_B^D` outside `X` lies in `D`, and the part of `K_Q^C`
   outside `X` lies in `C`.  Each selected component has a nonempty part
   outside `X`.
3. Distinct selected components on the same shore are vertex-disjoint and
   anticomplete.
4. Consecutive components in (3.2) meet in at least the connected boundary
   component `W_k` labelling their cycle edge.
5. Nonconsecutive selected components are vertex-disjoint and anticomplete.

When `m=1`, the cycle consists of two parallel coordinate edges.  Thus one
fixed full two-colour component in each shore contains the same two
distinct boundary components: this is the bilateral two-shore outcome.
When `m>=2`, (3.2) is a genuine alternating cyclic intersection
certificate.

#### Proof

Items 1 and 2 follow from construction, except for nonemptiness outside
`X`.  A selected block has two distinct incident cycle edges and hence
contains at least two distinct sets `W_k`.  Those sets are different
components of `H[alpha,beta]`; they cannot be joined inside `H`.  Their
full shore component must therefore use a vertex of the corresponding
exterior component.

Distinct full two-colour components of one fixed colouring are disjoint.
An edge between them would join them in the induced two-colour subgraph,
so they are anticomplete.  This proves item 3.

For a `D`-block `B` and a `C`-block `Q`, the intersection of the associated
full components lies in `X`, because `C,D` are disjoint and anticomplete.
More precisely,

\[
 K_B^D\cap K_Q^C
       =\bigcup\{W_k:k in B\cap Q\}.                    \tag{3.3}
\]

Thus every cycle edge supplies the intersection in item 4.

A shortest cycle containing `i` has no edge joining two nonconsecutive
cycle vertices: such a chord, together with the one of the two cycle arcs
which contains `i`, would give a shorter cycle containing `i`.  By (3.3),
nonconsecutive opposite-shore components are therefore disjoint.  They are
also anticomplete.  Indeed, there is no edge from `C` to `D`.  An edge with
both ends in `X` lies in `H[alpha,beta]`, so its ends belong to one `W_k`,
forcing `k in B cap Q`.  If one end lies in `D` and the other in `X`, that
edge belongs to the `alpha`--`beta` subgraph of `c_D`, again forcing the
boundary end's coordinate into `B cap Q`; the case with one end in `C` is
symmetric in `c_C`.  Each possibility contradicts the absence of a chord
between the selected blocks.  Combined with item 3, this proves item 5.
The description of the parallel-edge case is immediate.  \(\square\)

## 4. Application to the synchronized flip-cube fork

At the cube vertex `S` in the synchronized fork, put `theta=phi_S`, let
`E=r(S)`, and let `F` be the other exterior component.  For each of the two
rejector-changing coordinates `k in {i,j}`, the colouring `theta` extends
through `F` and `theta^{\{k\}}` extends through `E`.  Fix the `F`-extension
once and for all.  Theorem 3.1 then gives an alternating component cycle
through coordinate `k`, using that same fixed `F`-extension and one fixed
`E`-extension of `theta^{\{k\}}`.

Thus the two-coordinate fork cannot end in an isolated opposite-shore
path.  For either coordinate, failure of a common labelled boundary
colouring is certified by a closed alternating sequence of full
two-colour components.  The two cycles for `i` and `j` may use different
`E`-extensions and must not be combined without a further synchronization
argument.

## Exact trust boundary

The theorem is unbounded and exact.  It uses only two fixed shore
extensions for each selected coordinate, keeps literal `C`/`D` ownership,
and treats the parallel-edge bilateral case explicitly.  It is stronger
than listing separately chosen support paths: affine incompatibility forces
the supports to close into an alternating component cycle.

The cyclic family is an intersection certificate, not yet a clique-minor
model.  Consecutive full components overlap on literal boundary subgraphs,
and a path inside one full component between its two selected boundary
components may pass through additional boundary components.  No disjoint
branch-set allocation is inferred from (3.2).

Seven-connectivity has not yet been spent.  The next valid host theorem
must analyse bridges attached to this entire shortest alternating cycle.
Crossing attachments should yield a rooted linkage or an explicit
`K_7`-minor model; a noncrossing attachment system should yield one
coherent web/disc structure or a bounded response-preserving separation.
Applying Menger separately to one displayed path would discard the cyclic
invariant proved here and is not a valid completion.

## Input

- the exact two-full-component common-root exchange;
- the synchronized antipodal flip-cube fork.
