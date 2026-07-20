# Five-colour boundary transitions between two full shores

**Status:** written proof; separate internal audit pending.

This note records a general consequence of combining a five-colour Kempe
equivalence theorem with minor-minimality.  Its useful feature is that the
sixth colour remains absent from the boundary throughout the transition.
The conclusion is a pair of operation-specific bichromatic obstruction paths,
not a clique-minor model or a colour-gluing theorem.

## 1. Setup and extension sets

Let

\[
                 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
                 \tag{1.1}
\]

where `A` and `D` are nonempty and anticomplete.  Write `[6]={1,...,6}`.
Assume that each of the two closed sides `G[A\cup B]` and `G[D\cup B]`
has a proper six-colouring whose restriction to `B` avoids colour `6`.

Let `Col_5(B)` denote the proper colourings of `G[B]` with the labelled
palette `[5]`; a colouring need not use every colour.  Define

\[
\begin{aligned}
 \mathcal E_A={}&\{c\in Col_5(B):c\text{ extends to a proper
 six-colouring of }G[A\cup B]\},\\
 \mathcal E_D={}&\{c\in Col_5(B):c\text{ extends to a proper
 six-colouring of }G[D\cup B]\}.
                                                        \tag{1.2}
\end{aligned}
\]

Thus both extension sets are nonempty.  If `G` is not six-colourable, they
are disjoint: two closed-side colourings with the same labelled restriction
to `B` glue because `A` and `D` are anticomplete.

The **five-colour Kempe graph** `\mathcal K_5(B)` has vertex set
`Col_5(B)`.  Two colourings are adjacent when one is obtained from the other
by interchanging two colours on one connected component of the subgraph of
`G[B]` induced by those colours.

## 2. Producing the five-colour boundary responses

The next lemma explains when the nonemptiness assumption in Section 1 is
automatic.

### Lemma 2.1 (opposite-shore contraction)

Suppose `A` and `D` are connected, each is adjacent to every vertex of `B`,
every proper minor of `G` is six-colourable, and

\[
                         |A|\ge2,\qquad |D|\ge2.       \tag{2.1}
\]

Then both extension sets in (1.2) are nonempty.
Moreover, after requiring the contracted shore vertex to have colour `6`,
`\mathcal E_A` is exactly the set of boundary traces of six-colourings of
`G/D`, and symmetrically for `\mathcal E_D` and `G/A`.

#### Proof

Contract a spanning tree of `D` to one vertex `d`.  This is a proper minor,
so it has a six-colouring.  The vertex `d` is adjacent to every vertex of
`B`; hence its colour is absent from `B`.  Rename that colour `6` and restrict
the colouring to `G[A\cup B]`.  This gives an element of `\mathcal E_A`.
Contracting `A` and arguing symmetrically gives an element of
`\mathcal E_D`.

Conversely, take any six-colouring of `G[A\cup B]` counted by
`\mathcal E_A`.  Giving the contracted image of `D` colour `6` extends it
to `G/D`: that vertex has no neighbour in `A`, and every one of its
neighbours in `B` avoids colour `6`.  This proves the exact trace assertion;
the other shore is symmetric.  \(\square\)

The order assumptions in (2.1) are deliberate.  Contracting a singleton
shore does not produce a proper minor, so minor-minimality alone does not
justify this particular construction in that case.

## 3. The shortest-transition theorem

We use the following theorem of Las Vergnas and Meyniel: all labelled proper
five-colourings of a `K_5`-minor-free graph are Kempe equivalent.  Equivalently,
`\mathcal K_5(B)` is connected whenever `G[B]` has no `K_5` minor.

### Theorem 3.1 (opposite-shore five-colour transition)

Assume the setup of Section 1, suppose `G` is not six-colourable, and suppose
`G[B]` has no `K_5` minor.  Choose a shortest path

\[
              c_0,c_1,\ldots,c_m                           \tag{3.1}
\]

in `\mathcal K_5(B)` with `c_0\in\mathcal E_A` and
`c_m\in\mathcal E_D`, minimizing over both endpoints.  Then:

1. `m\ge1`;
2. `c_i\notin\mathcal E_A` for every `i>0`, and
   `c_i\notin\mathcal E_D` for every `i<m`;
3. the first boundary interchange is obstructed by a bichromatic path whose
   internal vertices lie in `A`; and
4. the last boundary interchange, read in reverse, is obstructed by a
   bichromatic path whose internal vertices lie in `D`.

More explicitly, suppose `c_1` is obtained from `c_0` by interchanging
colours `alpha,beta` on a component `K` of the corresponding two-colour
subgraph of `G[B]`.  For every six-colouring `\widehat c_0` of
`G[A\cup B]` extending `c_0`, the full `alpha`--`beta` component containing
`K` also meets a different `alpha`--`beta` component of `G[B]`.  Consequently
it contains a path with one end in `K`, the other end in that different
boundary component, and nonempty interior contained in `A`.

There is a symmetric statement for the last move and every extension of
`c_m` through `D`.  If `m=1`, the two paths obstruct the same pair of colours
and the same operated boundary component, one through each open shore.  The
other boundary components reached by the two paths need not be the same.
Their interiors are vertex-disjoint because `A` and `D` are disjoint.

#### Proof

The Las Vergnas--Meyniel theorem makes `\mathcal K_5(B)` connected, so a
path (3.1) exists.  The extension sets are disjoint, and therefore `m\ge1`.
If some `c_i` with `i>0` belonged to `\mathcal E_A`, then the suffix
`c_i,\ldots,c_m` would contradict the minimality of `m`.  The symmetric
prefix argument proves assertion 2.

Fix a six-colouring `\widehat c_0` of `G[A\cup B]` extending `c_0`, and let
`L` be the full `alpha`--`beta` component in this closed side that contains
`K`.  If

\[
                              L\cap B=K,                \tag{3.2}
\]

then interchanging `alpha,beta` on `L` gives a six-colouring of
`G[A\cup B]` whose boundary restriction is exactly `c_1`.  This would put
`c_1` in `\mathcal E_A`, contrary to assertion 2.  Thus `L` meets a second
component of the boundary two-colour subgraph.

Take a shortest path in `L` from `K` to a boundary vertex outside `K`,
stopping at the first such vertex.  Its other end lies in a different
boundary two-colour component.  All internal vertices avoid `B` and hence
lie in `A`.  The interior is nonempty, because distinct components of the
boundary two-colour subgraph have no edge between them.  This proves the
first obstruction statement.

For the last move, start with a six-colouring of `G[D\cup B]` extending
`c_m` and apply the same argument to the reverse interchange from `c_m` to
`c_{m-1}`.  If its full two-colour component met no other boundary
component, the reverse interchange would put `c_{m-1}` in
`\mathcal E_D`, again contradicting assertion 2.  The resulting shortest
path has nonempty interior in `D`.

When `m=1`, the first move and the reverse of the last move interchange the
same two colours on the same vertex set `K`.  The component partition of the
boundary two-colour subgraph is unchanged when the two colour names are
interchanged on one component.  Hence the two obstruction paths concern the
same boundary move.  \(\square\)

### Corollary 3.2 (minor-minimal two-full-shore form)

Let (1.1) hold.  Suppose:

- `A,D` are connected and anticomplete;
- every vertex of `B` has a neighbour in each of `A,D`;
- `|A|,|D|\ge2`;
- `G` is not six-colourable but every proper minor of `G` is
  six-colourable; and
- `G[B]` has no `K_5` minor.

Then all conclusions of Theorem 3.1 hold.

#### Proof

Lemma 2.1 supplies the two nonempty five-colour boundary extension sets;
Theorem 3.1 applies.  \(\square\)

## 4. Exact trust boundary

The theorem provides an unbounded, five-palette transition and literal
two-colour paths in the two open shores.  It does **not** prove any of the
following.

1. The distance `m` between the extension sets is one.
2. The other boundary components reached by the two obstruction paths are
   equal, disjoint, or attached to prescribed clique-minor branch sets.
3. Either obstruction path is boundary-full, or has a neighbourhood of
   order seven.
4. The two paths produce a `K_7`-minor model, a common boundary colouring,
   or a strict recursive descent.
5. The contraction construction in Lemma 2.1 works for a singleton open
   shore.  Such a case needs a separate response construction or must be
   excluded by an additional argument.

For `m\ge2`, every internal boundary colouring is rejected by both closed
sides, but this fact alone gives no compatible colouring partition.  The
first and last obstruction paths may also use different colour pairs under
different boundary colourings, so they are not automatically a simultaneous
linkage certificate.

The theorem is a five-palette specialization of the general shortest
boundary-distance mechanism recorded in
[`hc7_two_shore_kempe_list_dichotomy.md`](../results/hc7_two_shore_kempe_list_dichotomy.md).
Its new input is that `K_5`-minor-freeness connects the full unbounded
five-colouring space while keeping the sixth colour off `B` throughout.

## 5. External input

In the current two-full-shore application, the hypothesis that `G[B]` is
`K_5`-minor-free is supplied by
[`hc7_double_cone_vertex_deletion_equivalence.md`](../results/hc7_double_cone_vertex_deletion_equivalence.md),
Corollary 3, when the designated boundary vertex has two adjacent boundary
neighbours.

M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger Conjecture*,
Journal of Combinatorial Theory, Series B **31**(1) (1981), 95--104,
doi:10.1016/S0095-8956(81)80014-7.  The main result used here is that the
proper five-colourings of every `K_5`-minor-free graph form one Kempe
equivalence class.  Colourings are labelled maps into a five-colour palette;
surjectivity onto all five colours is not required.  This is the paper's
main theorem as stated in its publisher abstract; no unverified theorem
number is assigned here.  The corresponding assertion for arbitrary
`K_t`-minor-free graphs and `t` colours was posed there as a conjecture, not
proved.
