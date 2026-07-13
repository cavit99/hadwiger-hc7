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

### Theorem 2.1 (spanning rural quotient trichotomy)

Let `G` be seven-connected and let `J` be an induced connected subgraph
with an allowed carrier set `Z` satisfying `(E)`.  Fix disjoint connected
sets `X_0,Y_0` and the roots `x,y`.  Suppose at least one spanning
two-pole triple with `K subseteq Z` exists with

\[
 X_0\subseteq X,\qquad Y_0\subseteq Y,qquad
 |Q(K,X)|,|P(K,Y)|\ge3.                             \tag{2.1}
\]

Then at least one of the following occurs.

1. **Low carrier cut.**  Among the crossless spanning triples with
   `K subseteq Z` satisfying (2.1), one with minimum `|K|` has a carrier
   `J[K]` which is not three-connected.
2. **Literal pole exchange.**  A spanning triple with `K subseteq Z`
   satisfying (2.1) has
   either
   * a shared nonroot portal in `Q(K,X) cap P(K,Y)`;
   * a set-terminal cross in `J[K]`; or
   * a nonempty proper connected set
     `D subseteq K-(\{x,y\} union Q(K,X) union P(K,Y))` with

     \[
       |N_{J[K]}(D)|=3,\qquad J[K-D]\text{ connected},           \tag{2.2}
     \]

     which has a neighbour in each of `X,Y` (a literal three-gate pole
     bridge).
3. **Whole-shore rural quotient.**  There is a spanning triple with
   `K subseteq Z` satisfying (2.1) such that the simple quotient

   \[
                 J/(X\mapsto\alpha,\;Y\mapsto\beta)             \tag{2.3}
   \]

   is planar.  More precisely it is a subgraph of a plane rib with frame
   `(x,alpha,y,beta)`.

Here outcome 2 records actual vertices and paths.  It is not shorthand for
a colour contact or for an edge of a web completion.

#### Proof

If no crossless spanning triple with `K subseteq Z` satisfies (2.1), every
available triple has either a shared portal or a set-terminal cross, and
outcome 2 holds.  Otherwise choose such a crossless triple with minimum
`|K|`.
If its carrier is not three-connected, outcome 1 holds.  Assume therefore
that the selected carrier is three-connected.

Adjoin bookkeeping vertices `alpha,beta` to `J[K]`, with neighbourhoods
`Q=Q(K,X)` and `P=P(K,Y)`.  The block-terminal Two-Paths theorem applies:
crosslessness gives a same-vertex web completion with frame
`(x,alpha,y,beta)`.  Every member of `Q union P` is a rib vertex.  Every
component `D` of actual carrier vertices in a nonempty web cell has

\[
                         N_{J[K]}(D)=Delta,                        \tag{2.4}
\]

where `Delta` is its literal three-vertex gate, and `J[K]-D` is connected.
These are Theorem 3.1 and the connectivity paragraph of Lemma 5.1 in the
audited block-terminal theorem.

We show that no such `D` exists.  Seven-connectivity and the three-gate
equation (2.4) give at
least four distinct neighbours of `D` outside `K`.  At most two lie
outside `J` by `(E)`.  Since (1.1) spans `J`, `D` has a literal
neighbour in `X union Y`.

If `D` sees both poles, it itself is the third bullet of outcome 2.  Thus,
after interchanging the poles if necessary, assume that `D` sees `X` and
does not see `Y`.  Define

\[
 K'=K-D,\qquad X'=X\cup D,\qquad Y'=Y.               \tag{2.5}
\]

The three new parts are induced and connected, span `J`, contain the same
fixed sets and roots, and `X'` remains anticomplete to `Y'`.  No old member
of `Q union P` belongs to a cell, so all old contacts survive; in
particular the two lower bounds in (2.1) still hold.

If the new portal sets meet, the first bullet of outcome 2 holds.  If the
new carrier has a set-terminal cross, the second bullet holds.  Otherwise
the triple (2.5) is another crossless triple satisfying (2.1), with a
strictly smaller carrier, contrary to the choice of `K`.  Hence the web
has no nonempty actual cell.

It remains to read the quotient.  All internal carrier edges lie in the
plane rib.  A quotient edge from `alpha` to a nonroot carrier vertex is
exactly an edge to a member of `Q`, and similarly for `beta,P`.  Quotient
edges from either pole to `x` or `y` are among the four outer-frame edges.
There is no `alpha-beta` edge because `X,Y` are anticomplete.  These are
all edges because (1.1) spans `J`.  Thus the simple quotient (2.3) is a
subgraph of the same plane rib, proving outcome 3. \(\square\)

The minimization is deliberately over all crossless spanning triples, not
only those with three-connected carrier.  Thus moving a cell to a pole
cannot hide a new low cut: if the smaller triple is still crossless it is
a valid smaller competitor, whether or not its carrier remains
three-connected.  Conversely, the initial passage to a spanning triple is
not claimed to preserve connectivity or crosslessness; those are outcomes
1 and 2.

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
normalization, which required the core to avoid the side terminal.  Thus the carrier
constructed in the second case of Lemma 3.1 lies in `Z`.  If the first
case occurs, a shortest path to `A union B` is a literal outside-carrier
pole connector.  It is **not automatically a valid core promotion**: the
path may run through the side terminal, and a separate label-faithful
assignment is required.  If the second case occurs, Theorem 2.1 applies
unless the absorption has exposed exactly the low cut or literal pole
exchange which it records.

## 4. What remains after the spanning repair

Outcome 3 is genuinely stronger than the earlier selected-core quotient:
every vertex of the closed shore `J` belongs to the carrier or one of the
two contracted poles.  It still does not say that the induced pole graphs
have local disk embeddings.  Apply the audited tree-pole rotation theorem
`hc7_exact7_tree_pole_rotation_exchange.md` to an edge-minimal connector
in each pole.  One then obtains either a
rotation-compatible connector or two literal disjoint carriers joining
alternating attachment occurrences.

Thus the exact remaining conversion is shared by outcomes 1--3.  It must
preserve the **attained decorated-state duty** of the current frame; an
unlabelled pole contact is not sufficient.  None of the literal exchange
certificates is silently identified with another:

\[
 \boxed{\begin{array}{c}
 \text{low cut, shared portal, set-terminal cross, bilateral three-gate,}\\
 \text{or alternating pole carriers}\\
 \Longrightarrow K_7,\text{ common state, or fixed pair.}
 \end{array}}
\]

No leftover shore component and no choice of web completion is hidden in
this formulation.
