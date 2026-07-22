# Tight-pole edge localization at degree seven

**Status:** written proof; [separate internal audit **GREEN**](hc7_degree7_tight_pole_edge_localization_audit.md).
This theorem localizes the automatic degree-seven tight-pole transition in
either of two disjoint bichromatic components.  An order-seven localized
boundary gives a strict generic selected-response descent.  A larger
boundary, or two internally vertex-disjoint routes in each component,
remains nonterminal.  Nothing here proves `HC_7`.

## 1. Setup

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Let `u` have degree seven and put

\[
 S=N_G(u),\qquad C=G-N_G[u],\qquad A=G-u,
 \qquad H=G[S],\qquad F=\overline H.                 \tag{1.2}
\]

The audited degree-seven reduction makes `C` nonempty and connected.  It
also gives

\[
 \alpha(H)\le2,\qquad \chi(H)\le4,                  \tag{1.3}
\]

and the exact boundary matching languages

\[
 \begin{aligned}
  \mathcal M(A)&=\{\{e\}:e\in E(F)\},\\
  \mathcal M(G[N[u]])
     &=\{M:M\text{ is a matching of }F, |M|\ge2\}.
 \end{aligned}                                      \tag{1.4}
\]

Here a matching records the two-vertex colour classes on `S`; every
unmatched boundary vertex is a singleton colour class.  Equation (1.3)
implies that `F` has a matching

\[
                         \{e_0,e_1,e_2\}.             \tag{1.5}
\]

Indeed, a four-colouring of the seven-vertex graph `H` has three
two-vertex colour classes because every class has order at most two.

Fix a proper six-colouring `c` of `A` whose only repeated boundary pair is
`e_0`.  For `i=1,2`, write

\[
 e_i=x_i y_i,\qquad
 \alpha_i=c(x_i),\qquad \beta_i=c(y_i),              \tag{1.6}
\]

and let `K_i` be the component of

\[
             A[c^{-1}(\{\alpha_i,\beta_i\})]          \tag{1.7}
\]

containing `x_i`.

## 2. The pole transition is automatic

### Proposition 2.1

For each `i=1,2`, the component `K_i` also contains `y_i`, and

\[
 K_i\cap S=\{x_i,y_i\},\qquad K_i-S\subseteq C.       \tag{2.1}
\]

On the boundary, changing only `x_i` from `alpha_i` to `beta_i` is one
Kempe interchange.  It changes the matching from `\{e_0\}` to
`\{e_0,e_i\}` and is a tight-pole transition: its initial trace extends
through `A`, its final trace extends through `G[N[u]]`, and in the final
extension `u` has the colour `alpha_i` which disappeared from `S`.

In particular, the distance between the two exact-`e_0` extension
languages is one.  Shortening or reselecting such a transition cannot
remove the pole at degree seven.

#### Proof

The five vertices of `S-V(e_0)` have five distinct colours under `c`.
Thus the boundary `alpha_i`--`beta_i` graph consists of the two singleton
components `\{x_i\},\{y_i\}`.  If they belonged to different components
of the full bichromatic graph in `A`, interchanging the component of
`x_i` would give an `A`-colouring with matching `\{e_0,e_i\}`, contrary to
(1.4).  Hence `y_i` belongs to `K_i`, and (2.1) follows from the five
distinct singleton colours.

The same boundary interchange is therefore legal and has the asserted
two traces.  The second trace has five colour blocks, so (1.4) makes it
extend through `G[N[u]]`; explicitly, assign `u` the disappeared colour
`alpha_i`.  The two traces cannot coincide because the languages in (1.4)
are disjoint.

After deleting `u`, the final `alpha_i`--`beta_i` boundary graph has no
`alpha_i` vertex and has the nonadjacent vertices `x_i,y_i` as separate
`beta_i` components.  Thus the universal vertex `u` is the only such
two-colour connection in the opposite closed shore.  This is exactly the
tight-pole alternative of the pole-move normal form.  \(\square\)

The components `K_1,K_2` are vertex-disjoint because their two colour
pairs are disjoint.

## 3. A separating edge carries the exact response

Call an edge `h` of `K_i` an `x_i`--`y_i` **separating edge** if `x_i`
and `y_i` lie in different components of `K_i-h`.

### Theorem 3.1 (prescribed-response edge localization)

Let `h=pq` be an `x_i`--`y_i` separating edge.  Orient its ends so that
`p` and `x_i` lie in one component `X` of `K_i-h`, while `q` and `y_i`
lie in the other component `Y`.

There is a proper six-colouring `c_h` of both `G-h` and `G/h` such that

1. its exact matching on the original boundary `S` is `\{e_0,e_i\}`;
2. `c_h(p)=c_h(q)`; and
3. for each of the other five colours `theta`, the vertices `p,q` lie in
   one `c_h(p)`--`theta` component of `G-h`.

For the old pair of colours there is a literal lock route

\[
              p\;K_i[X]\;x_i\;u\;y_i\;K_i[Y]\;q.    \tag{3.1}
\]

Thus the edge response retains the particular tight-pole operation, not
merely an uncontrolled boundary matching of order two or three.

#### Proof

Interchange `alpha_i,beta_i` on `X` and leave `c` unchanged elsewhere in
`A`.  Since `K_i` is a full bichromatic component and `h` is its only edge
between `X,Y`, this is a proper colouring of `A-h`.  Only `x_i` changes on
`S`, from `alpha_i` to `beta_i`.  Hence its boundary matching is exactly
`\{e_0,e_i\}`, and `alpha_i` is absent from `S`.  Give `u` colour
`alpha_i`.  This produces a proper six-colouring `c_h` of `G-h`.

Exactly one end of `h` was interchanged, so `c_h(p)=c_h(q)`.  The colouring
therefore descends to `G/h`.  If `p,q` lay in different components for
their common colour and some other colour `theta`, interchange the
component containing `p`.  The ends of `h` would then have different
colours, allowing `h` to be restored and giving a six-colouring of `G`, a
contradiction.  This proves all five locks.

Both `X` and `Y` are connected in the old two-colour graph.  After the
interchange, paths from `p` to `x_i` in `X` and from `y_i` to `q` in `Y`,
together with the edges `x_i u,u y_i`, give the walk (3.1).  It contains a
simple `p`--`q` path in the old pair of colours.  \(\square\)

The general five-lock theorem for an edge meeting `C` is already known.
The added content here is the prescribed matching `\{e_0,e_i\}` and its
identification with the automatic tight-pole move.

## 4. A bridge gives a smaller literal side

### Theorem 4.1 (rank-smaller bridge side)

If `K_i` has an `x_i`--`y_i` separating edge, there is such an edge `h`
and a component `W` of `K_i-h` satisfying

\[
 |W|<|C|,\qquad
 V(G)-(W\cup N_G(W))\ne\varnothing.                  \tag{4.1}
\]

Consequently `N_G(W)` is the boundary of an actual separation and

\[
                            |N_G(W)|\ge7.              \tag{4.2}
\]

If equality holds in (4.2), the separation, the crossing edge `h`, and
the colouring from Theorem 3.1 form a generic exact-seven selected-response
interface whose connected operated shore is `W`.  This is a strict
same-host descent from the original component `C`.

#### Proof

First, `|C|\ne1`.  If `C=\{v\}`, seven-connectivity and `N(v)\subseteq S`
give `N(v)=S`.  In a six-colouring of the proper minor `G-v`, the colour of
`u` is absent from `S`; assigning that same colour to the nonadjacent
vertex `v` would six-colour `G`.

Put `n=|C|\ge2`.  Since `K_i\cap S=\{x_i,y_i\}`,

\[
                              |K_i|\le n+2.             \tag{4.3}
\]

For `n\ge3`, the smaller component of `K_i-h` has order at most
`floor((n+2)/2)<n`.  If `n=2`, only an equal `2+2` split needs attention.
The connected bipartite graph `K_i` then has four vertices, a separating
edge, and nonadjacent roots of opposite colours.  It is the alternating
path `x_i-C-C-y_i`; an end edge has a singleton root side.  Thus in every
case a separating edge has a side `W` with `|W|<n` and exactly one of the
two boundary roots.

Let `Q` be the other component of `K_i-h`, and orient `h=pq` with
`p\in W,q\in Q`.  If `Q` has a vertex other than `q`, that vertex has no
neighbour in `W`: any such edge would be another edge of the full induced
two-colour component joining the bridge sides.  It therefore lies outside
`W\cup N(W)`.  If `Q=\{q\}`, then `q` is the other boundary root.  Replace
`W` by `\{q\}` and interchange the names of the two roots.  The first root
lies outside `N[q]` because `e_i` is a boundary nonedge.  This proves
(4.1).

The nonempty set `N(W)` separates `W` from a nonempty far side, so
seven-connectivity gives (4.2).

Suppose `|N(W)|=7`, and put

\[
 T=N(W),\qquad R=V(G)-(W\cup T).                       \tag{4.4}
\]

Then `W` is connected, `R` is nonempty, `T=N(W)`, and the selected edge
`h` joins `W` to `T`.  Reorient the names in Theorem 3.1 so that the
component interchanged there is `W`.  Its colouring `c_h` is proper on
the unchanged opposite closed shore `G[R\cup T]`.  Its exact partition on
`T` cannot also extend through the intact closed shore `G[W\cup T]`, since
the two colourings could then be aligned on `T` and glued to six-colour
`G`.  Hence (4.4), `h`, and `c_h` satisfy the definition of a generic
exact-seven selected-response interface.  Finally `|W|<|C|`, so the
descent is strict on literal vertices of the unchanged host.  \(\square\)

If `|N(W)|\ge8`, Theorem 4.1 gives a response-preserving
positive-excess separator but no recursive descent.  An upper bound on
this literal neighbourhood does not follow from the bridge geometry.

### Theorem 4.2 (articulation-side localization)

For each `i=1,2`, at least one of the following holds.

1. `K_i` contains two internally vertex-disjoint `x_i`--`y_i` paths.
2. There is an internal articulation vertex `v` and a component `W` of
   `K_i-v` containing exactly one of `x_i,y_i` such that

   \[
     |W|<|C|,\qquad
     V(G)-(W\cup N_G(W))\ne\varnothing,
     \qquad |N_G(W)|\ge7.                              \tag{4.5}
   \]

In outcome 2, choose any edge `at` with `a\in W` and `t\in N_G(W)`.
Every six-colouring of the proper minor `G-at` is intact on the opposite
closed shore and its complete equality partition on `N_G(W)` is rejected
by the intact `W`-shore.  If `|N_G(W)|=7`, this is a strict generic
exact-seven selected-response descent.  If `|N_G(W)|\ge8`, it is only a
response-bearing positive-excess separation.

#### Proof

Apply the vertex form of Menger's theorem inside `K_i`.  Failure of outcome
1 gives a vertex `v\notin\{x_i,y_i\}` such that the two roots lie in
different components `X,Y` of `K_i-v`.  By (4.3),

\[
 \min\{|X|,|Y|\}
 \le \left\lfloor\frac{|K_i|-1}{2}\right\rfloor
 \le \left\lfloor\frac{|C|+1}{2}\right\rfloor
 <|C|,                                                   \tag{4.6}
\]

where the last inequality uses `|C|\ge2`, proved in Theorem 4.1.  Let `W`
be the smaller root component.

The other root component is anticomplete to `W` in the full graph `G`.
Indeed, both sets lie in the induced `alpha_i`--`beta_i` graph, so any
edge between them would also be an edge of `K_i-v` and would join the two
components.  It follows that the other root component lies outside
`W\cup N_G(W)`.  Thus `N_G(W)` is an actual separation boundary, and
seven-connectivity proves the last inequality in (4.5).

Choose a crossing edge `at`.  The graph `G-at` is a proper minor and has a
six-colouring `d`.  Put `T=N_G(W)` and
`R=V(G)-(W\cup T)`.  The edge `at` is absent from the unchanged opposite
closed shore `G[R\cup T]`, so `d` restricts to a proper colouring there.
If the complete equality partition induced by `d` on `T` extended through
the intact closed shore `G[W\cup T]`, the two colourings could be aligned
on `T` and glued to six-colour `G`.  Hence the intact `W`-shore rejects
that partition.  When `|T|=7`, all clauses of a generic exact-seven
selected-response interface hold and (4.6) makes the descent strict.  The
same argument records a selected response but gives no recursion when
`|T|\ge8`.  \(\square\)

Unlike Theorem 4.1, Theorem 4.2 need not preserve `e_0`, `e_i`, or the old
palette: its selected response comes from an arbitrary colouring of the
new crossing-edge deletion.  Its gain is the stronger route geometry in
the only case without a smaller response-bearing separator.

## 5. Two disjoint layers give a response square

### Corollary 5.1 (punctured response square)

Suppose both `K_1,K_2` contain separating edges `h_1,h_2`.  Choose for
each edge the side containing `x_i` as in Theorem 3.1.  Then the two
component interchanges commute and give

1. a six-colouring of `G-h_1` with boundary matching `\{e_0,e_1\}`;
2. a six-colouring of `G-h_2` with boundary matching `\{e_0,e_2\}`; and
3. a six-colouring of `G-\{h_1,h_2\}` with boundary matching
   `\{e_0,e_1,e_2\}`, in which both deleted endpoint pairs are
   monochromatic.

These are the three nonzero corners of a response square.  The missing
corner in which both intact edges are proper would be a six-colouring of
`G`.  No five-lock conclusion is asserted in the double-deletion colouring.

#### Proof

The two colour pairs, components and selected edges are disjoint.  Either
single interchange is exactly Theorem 3.1 and leaves the other layer
unchanged.  After both interchanges, both original singleton pairs have
merged.  Either disappeared colour may be assigned to `u`, giving the
third colouring.  Exactly one end of each `h_i` was interchanged, so both
deleted endpoint pairs are monochromatic.  \(\square\)

## 6. Exact residual

By Theorem 4.2, each `K_i` has exactly the following alternative:

1. it contains two internally vertex-disjoint literal `x_i`--`y_i`
   paths; or
2. an internal articulation exposes a rank-smaller connected side `W_i`
   carrying a selected crossing-edge response.

The two layers remain vertex-disjoint.  After excluding strict order-seven
descent, every side in outcome 2 has

\[
                             |N(W_i)|\ge8.              \tag{6.1}
\]

When the articulation is witnessed more strongly by a separating edge,
Theorems 3.1 and 4.1 retain the exact matching `\{e_0,e_i\}`; if both
layers have such edges, their exact single- and double-operation responses
coexist as in Corollary 5.1.  Thus the degree-seven tight-pole branch is
reduced to the following literal host-level obstruction:

> two vertex-disjoint bichromatic layers, each with either two
> internally vertex-disjoint root-to-root routes or a smaller connected
> side of boundary order at least eight; in the two-separating-edge case
> the prescribed matching responses form the punctured square above.

This is not a terminal outcome.  The two routes have no proved contacts to
the other rooted branch sets, and a boundary of order at least eight is not
a bounded exact-seven restart.  Closing the residue requires further use
of the global `K_7`-minor exclusion or operation-specific proper-minor
responses.

## 7. Dependencies and novelty boundary

- [connected degree-seven anti-neighbourhood](hc7_degree7_anti_neighbourhood_connectivity.md)
- [exact matching languages and disjoint Kempe bridges](hc7_degree7_matching_bridge_bundle.md)
- [degree-seven off-pole edge responses](hc7_degree7_one_spoke_bridge_corollaries.md)
- [last-pole move normal form](hc7_bounded_interface_pole_move_normal_form.md)
- [generic exact-seven selected-response restart](hc7_generic_exact7_response_restart.md)
- [atomic bichromatic-bridge localization](hc7_atomic_bichromatic_bridge_state_localization.md)

The component swap, five locks, generic restart, and commuting disjoint
palette swaps are established mechanisms.  The specialized conclusions
proved here are that the degree-seven tight-pole transition is automatic,
an internal articulation exposes a smaller literal side, a separating edge
retains the exact matching `\{e_0,e_i\}`, and two such edges retain the
exact triple matching under double deletion.
