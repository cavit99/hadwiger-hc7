# Spanning rural quotient or a literal exchange obstruction

**Status:** proved and independently audited twice.
It repairs the nonspanning gap in the selected rural carrier without
assuming that absorbing leftover components preserves three-connectivity or
the captured-path property.  Those failures are retained as literal
outcomes.

## 1. Spanning three-part societies

Let `J` be a connected graph and let `x,y` be two distinguished vertices.
A **spanning two-pole triple** is a partition

\[
                     V(J)=K\mathbin{\dot\cup}X\mathbin{\dot\cup}Y       \tag{1.1}
\]

such that the three induced graphs on the parts are connected,
`x,y in K`, and `E_J(X,Y)=empty`.  Put

\[
 \begin{aligned}
 Q(K,X)&=N_K(X)-\{x,y\},\\
 P(K,Y)&=N_K(Y)-\{x,y\}.                            \tag{1.2}
 \end{aligned}
\]

The triple is **crossless** if the sets in (1.2) are disjoint and there
are no vertex-disjoint paths in `J[K]`, one joining `x` to `y` and the
other joining a member of `Q(K,X)` to a member of `P(K,Y)`.

Fix an allowed carrier set `Z subseteq V(J)` containing `x,y`, and consider
only triples with `K subseteq Z`.  We use the following exact exposure
hypothesis:

> If `C subseteq Z-\{x,y\}` is nonempty, then
> `|N_G(C)-V(J)|<=2`.                               \((\mathcal E)\)

In the exact-order-six Moser terminal shore after deleting `v,w`, take

\[
                    Z=V(J)-(U-\{x,y\})
                     =V(D_t)\cup\{t,x,y\},                       \tag{1.3}
\]

where `D_t` is the open shore and `t` its side terminal.  Every set in
`Z-\{x,y\}` consists only of open-shore vertices and possibly `t`.  Exact
shore anticompleteness and `N(v)=S` leave only `w` as an outside neighbour
of an open-shore vertex, while `t` can see `v` and the audited identities
`wt notin E(G)` and opposite-shore anticompleteness exclude any further
outside neighbour.  Hence all outside neighbours lie in `{v,w}`, and
`(E)` holds even for sets containing `t`.

## 2. The whole-shore theorem

### Theorem 2.1 (spanning rural quotient quadrichotomy)

Let `G` be seven-connected and let `J` be an induced connected subgraph
with an allowed carrier set `Z` satisfying `(E)`.  Fix disjoint connected
sets `X_0,Y_0` and the roots `x,y`.  Suppose at least one spanning
two-pole triple with `K subseteq Z` exists with

\[
 X_0\subseteq X,\qquad Y_0\subseteq Y,qquad
 |Q(K,X)|,|P(K,Y)|\ge3.                             \tag{2.1}
\]

Then every such spanning triple has at least one of the following outcomes.

1. **Low carrier cut.**  The carrier `J[K]` is not three-connected.
2. **Shared portal.**  There is a literal nonroot vertex in
   `Q(K,X) cap P(K,Y)`.
3. **Set-terminal cross.**  The carrier `J[K]` has vertex-disjoint paths,
   one joining `x` to `y` and the other joining a member of `Q(K,X)` to a
   member of `P(K,Y)`.
4. **Whole-shore rural quotient.**  The simple quotient

   \[
                 J/(X\mapsto\alpha,\;Y\mapsto\beta)             \tag{2.2}
   \]

   is planar.  More precisely it is a subgraph of a plane rib with frame
   `(x,alpha,y,beta)`.

The shared portal and the paths in outcomes 2--3 are literal.  They are not
shorthand for colour contacts or edges of a web completion.

#### Proof

Fix an eligible spanning triple.  If its carrier is not three-connected,
outcome 1 holds.  If its two portal sets meet, outcome 2 holds.  If it has
a set-terminal cross, outcome 3 holds.  Assume none of these outcomes
occurs.  The carrier is therefore three-connected and crossless.

Adjoin bookkeeping vertices `alpha,beta` to `J[K]`, with neighbourhoods
`Q=Q(K,X)` and `P=P(K,Y)`.  The block-terminal Two-Paths theorem applies:
crosslessness gives a same-vertex web completion with frame
`(x,alpha,y,beta)`.  Every member of `Q union P` is a rib vertex.  Every
component `D` of actual carrier vertices in a nonempty web cell has

\[
                         N_{J[K]}(D)=Delta,                        \tag{2.3}
\]

where `Delta` is its literal three-vertex gate, and `J[K]-D` is connected.
These are Theorem 3.1 and the connectivity paragraph of Lemma 5.1 in the
audited block-terminal theorem.

We show directly that no such `D` exists.  Every member of `Q union P` is
a rib vertex, while `D` lies inside a nonempty cell; moreover `D` contains
neither root.  Since `Q` and `P` are the **whole** nonroot pole-neighbour
sets, it follows from their definitions that

\[
                         E_J(D,X\cup Y)=\varnothing.             \tag{2.4}
\]

The six distinct vertices of the disjoint sets `Q,P` cannot all lie in
the three-vertex gate `Delta`.  Hence some carrier vertex lies beyond
`D union Delta`, so `N_G(D)` is a genuine separator.  Seven-connectivity
and (2.3) give `|N_G(D)|>=7`, with exactly three neighbours inside `K`.
But (2.4), spanning (1.1), and `(E)` leave at most two further neighbours,
all outside `J`.  Thus `|N_G(D)|<=5`, a contradiction.  Therefore the web
has no nonempty actual cell.

It remains to read the quotient.  All internal carrier edges lie in the
plane rib.  A quotient edge from `alpha` to a nonroot carrier vertex is
exactly an edge to a member of `Q`, and similarly for `beta,P`.  Quotient
edges from either pole to `x` or `y` are among the four outer-frame edges.
There is no `alpha-beta` edge because `X,Y` are anticomplete.  These are
all edges because (1.1) spans `J`.  Thus the simple quotient (2.2) is a
subgraph of the same plane rib, proving outcome 4. \(\square\)

No connectivity or captured-path property is inherited from an earlier
carrier.  They are tested afresh on the chosen spanning triple: low
connectivity is outcome 1 and a new detour is outcome 3.

## 3. Obtaining a spanning triple from the selected core

### Lemma 3.1 (component absorption)

Let `K_0,X_0,Y_0` be disjoint connected subgraphs of a connected graph
`J`, with `x,y in K_0` and `X_0,Y_0` disjoint from `K_0`.

* If `X_0,Y_0` lie in the same component of `J-V(K_0)`, that component
  contains an `X_0-Y_0` path avoiding `K_0`.
* Otherwise let `X,Y` be their two distinct components of
  `J-V(K_0)`, and put

  \[
                  K=V(J)-(X\cup Y).                              \tag{3.1}
  \]

  Then `(K,X,Y)` is a spanning two-pole triple.  Moreover every vertex
  added to `K_0` lies in a component of `J-V(K_0)` different from `X,Y`;
  each such component has a neighbour in `K_0`, so `J[K]` is connected.

#### Proof

The first assertion is the definition of a component.  In the second
case, different components of `J-V(K_0)` are anticomplete, so `X,Y` are
connected and anticomplete.  Since `J` is connected, every other component
of `J-V(K_0)` has an edge to `K_0`.  Their union with the connected set
`K_0` is therefore connected, and (3.1) spans `J`. \(\square\)

In the exact-six cell take `X_0=A union B`, `Y_0=L`, and `Z` as in (1.3).
All literal
vertices of `U` already lie in `K_0 union A union B`, so absorbing the
other components does not add a new `U`-vertex to the pair trace of `K`.
The side terminal may be assigned topologically to one of the three
spanning parts; it is not a vertex of the adhesion `T=U union \{w\}`.
This assignment is not asserted to preserve the earlier supported-core
normalization, which required the core to avoid the side terminal.  The
carrier constructed in the second case of Lemma 3.1 nevertheless lies in
`Z`.  If the first
case occurs, a shortest path to `A union B` is a literal outside-carrier
pole connector.  It is **not automatically a valid core promotion**: the
path may run through the side terminal, and a separate label-faithful
assignment is required.  If the second case occurs, Theorem 2.1 gives
exactly a low cut, a shared portal, a set-terminal cross, or the planar
whole-shore quotient.

## 4. What remains after the spanning repair

Outcome 4 is genuinely stronger than the earlier selected-core quotient:
every vertex of the closed shore `J` belongs to the carrier or one of the
two contracted poles.  It still does not say that the induced pole graphs
have local disk embeddings.  Apply the audited tree-pole rotation theorem
`hc7_exact7_tree_pole_rotation_exchange.md` to an edge-minimal connector
in each pole.  One then obtains either a
rotation-compatible connector or two literal disjoint carriers joining
alternating attachment occurrences.

Thus the exact remaining conversion is shared by outcomes 1--4.  It must
preserve the **attained decorated-state duty** of the current frame; an
unlabelled pole contact is not sufficient.  None of the literal exchange
certificates is silently identified with another:

\[
 \boxed{\begin{array}{c}
 \text{low cut, shared portal, set-terminal cross,}\\
 \text{or alternating pole carriers}\\
 \Longrightarrow K_7,\text{ common state, or fixed pair.}
 \end{array}}
\]

No leftover shore component and no choice of web completion is hidden in
this formulation.
