# A root-connecting subgraph and two disjoint boundary-block carriers force the split-root response

**Status:** written proof; separate internal re-audit GREEN in
[`hc7_order8_root_connector_reflection_audit.md`](hc7_order8_root_connector_reflection_audit.md).
This is an unbounded two-shore colouring theorem.  It does not prove
`HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing.                            \tag{1.1}
\]

Assume that every proper minor of `G` is six-colourable.  Let `d,e` be
distinct nonadjacent vertices of `G[S]`, and let

\[
                         S-\{d,e\}=X\mathbin{\dot\cup}Y             \tag{1.2}
\]

be a bipartition of `G[S - {d,e}]`, where `X,Y` are nonempty.  Assume that

1. there is an edge between `X` and `Y`; and
2. each of `d,e` has a neighbour in each of `X,Y`.

For a nonempty independent boundary block \(Z\subseteq S\) and a vertex
set `F` disjoint from `S`, call `F` a **boundary-block carrier for `Z`** if
`G[Z union F]` is connected and contains an edge.  The carrier `F` need
not induce a connected subgraph: vertices of `Z` may join several of its
components inside the contracted block.

## 2. Root-connector reflection theorem

### Theorem 2.1

Suppose that `D` is a nonempty connected subgraph of `G[R]` and that
\(F_X,F_Y\subseteq R\) are vertex sets such that

\[
                         V(D),\qquad F_X,\qquad F_Y                \tag{2.1}
\]

are pairwise disjoint, `D` has a neighbour at both `d,e`, `F_X` is a
boundary-block carrier for `X`, and `F_Y` is a boundary-block carrier for
`Y`.  Then the closed shore `G[L union S]` has a proper six-colouring
inducing the exact boundary equality partition

\[
                            X\mid Y\mid\{d\}\mid\{e\}.             \tag{2.2}
\]

Consequently, if the opposite closed shore `G[R union S]` also has a
proper six-colouring inducing (2.2), then `G` is six-colourable.

#### Proof

In `G`, simultaneously contract spanning trees of the following three
pairwise disjoint connected sets:

\[
                  V(D)\cup\{d\},\qquad F_X\cup X,
                  \qquad F_Y\cup Y.                                \tag{2.3}
\]

Each displayed set is connected and contains an edge: `D` has a neighbour
at `d`, and the two boundary-block-carrier hypotheses give exactly those
properties for `F_X union X` and `F_Y union Y`.  The result is therefore a
proper minor of `G`.

Let the three contraction images be `Z_d,Z_X,Z_Y`, and leave `e`
uncontracted.  These four objects form a `K_4`:

* `Z_d` is adjacent to `e` through an edge from `D` to `e`;
* `Z_d` is adjacent to `Z_X,Z_Y` through the assumed neighbours of `d`
  in `X,Y`;
* `e` is adjacent to `Z_X,Z_Y` through its assumed neighbours in `X,Y`;
  and
* `Z_X` is adjacent to `Z_Y` through an edge between `X,Y`.

Six-colour the proper minor.  Keep its colouring on `L union {e}` and
pull the colours of `Z_d,Z_X,Z_Y` back to `d,X,Y`, respectively.  The
four boundary blocks in (2.2) are independent, and the displayed `K_4`
forces them to receive four distinct colours.  Every edge from `L` to a
contracted boundary vertex was represented by an edge to the corresponding
contraction image.  The pulled-back colouring is therefore proper and
induces exactly (2.2).

If the other closed shore also realizes (2.2), permute its six colour
names to align the four block colours.  The open shores are anticomplete,
so the two colourings glue to a proper six-colouring of `G`. \(\square\)

The proof does not require `D,F_X,F_Y` to lie in different components of
`G-S`, nor does it require either carrier to be connected before its
boundary block is adjoined.  In particular, `D` may be a single common
neighbour of `d,e`; it need not split into two connected pieces carrying
the two root contacts.

## 3. Exact connector/carrier entanglement

Suppose the closed `R`-shore realizes (2.2), whereas the closed `L`-shore
does not.

### Corollary 3.1 (exact connector/carrier entanglement)

For every connected subgraph `D` of `G[R]` having a neighbour at both
`d,e`, there are no disjoint sets

\[
                        F_X,F_Y\subseteq R-V(D)                    \tag{3.1}
\]

such that `F_X` is a boundary-block carrier for `X` and `F_Y` is a
boundary-block carrier for `Y`.

#### Proof

Such `D,F_X,F_Y` would satisfy Theorem 2.1 and make the closed `L`-shore
realize (2.2), contrary to the hypothesis. \(\square\)

This is the exact obstruction to applying the root-connector contraction
inside a connected open shore.  Taking `D={q}` gives the common-neighbour
case.

## 4. Consequences for two full connected subgraphs

Assume additionally that `R` contains two disjoint connected subgraphs
`Q_0,Q_1`, each adjacent to every literal vertex of `S`.

### Corollary 4.1 (external common root neighbour)

Every common neighbour of `d,e` in `R` belongs to `Q_0 union Q_1`.

#### Proof

If a common neighbour `q` lies outside `Q_0 union Q_1`, apply Theorem 2.1
with `F_X=V(Q_0)` and `F_Y=V(Q_1)`.  Boundary fullness and connectivity
make these boundary-block carriers.  The theorem makes the closed
`L`-shore realize (2.2), contrary to the hypothesis. \(\square\)

### Corollary 4.2 (class-component incidence at an internal common neighbour)

Let `q in Q_i` be adjacent to both `d,e`, and put `j=1-i`.  Let
\(\mathcal K_i(q)\) be the components of

\[
                         G[V(Q_i)-\{q\}].                           \tag{4.1}
\]

For \(Z\in\{X,Y\}\), form the bipartite incidence graph
\(\mathcal I_Z(q)\) with parts \(Z\) and \(\mathcal K_i(q)\), where
`zK` is an edge exactly when `z` has a neighbour in `K`.  No connected
component of \(\mathcal I_Z(q)\) contains every vertex of `Z` together
with a member of \(\mathcal K_i(q)\).

Equivalently, there is no boundary-block carrier for `Z` contained in
`V(Q_i)-{q}`.

#### Proof

Suppose a connected component of \(\mathcal I_X(q)\) contains all of `X`
and at least one member of \(\mathcal K_i(q)\).  Let `A` be the set of
members of \(\mathcal K_i(q)\) in that incidence component and put

\[
                         F_X=\bigcup_{K\in A}V(K).                  \tag{4.2}
\]

Because every `K` is connected and the incidence component is connected,
`G[X union F_X]` is connected.  It contains an edge because the incidence
component contains vertices on both sides.  Thus `F_X` is a boundary-block
carrier for `X`.  Boundary fullness and connectivity make `V(Q_j)` a
boundary-block carrier for `Y`.  The three sets

\[
                         \{q\},\qquad F_X,\qquad V(Q_j)
\]

are pairwise disjoint, so Theorem 2.1 gives the forbidden split response
on the closed `L`-shore.  Interchanging `X,Y` proves the displayed
incidence conclusion for both classes.

For completeness, suppose that
\(F_Z\subseteq V(Q_i)-\{q\}\) is a boundary-block carrier for `Z`.
Project each path in the connected graph `G[Z union F_Z]` to the incidence
graph by replacing every maximal subpath in
\(V(Q_i)-\{q\}\) with the member of \(\mathcal K_i(q)\) containing it.
This shows that all vertices of `Z` lie in one component of
\(\mathcal I_Z(q)\).  Because `Z` is independent and the carrier block is
nontrivial, that component also contains a member of
\(\mathcal K_i(q)\).  Hence the two formulations are indeed equivalent.
\(\square\)

### Corollary 4.3 (a nonseparating common neighbour)

If \(G[V(Q_i)-\{q\}]\) has at most one component, then `q` is the unique
`Q_i`-neighbour of some vertex of `X` and the unique `Q_i`-neighbour of
some vertex of `Y`.

#### Proof

Fix \(Z\in\{X,Y\}\).  If \(G[V(Q_i)-\{q\}]\) is empty, boundary fullness
immediately makes `q` the unique `Q_i`-neighbour of every vertex of `Z`.
Otherwise let `K` be its unique component.  If every vertex of `Z` had a
neighbour in `K`, then the component of \(\mathcal I_Z(q)\) containing
`K` would contain all of `Z`, contrary to Corollary 4.2.  Some `z in Z`
therefore has no neighbour in `K`.  Boundary fullness gives a neighbour of
`z` in `Q_i`, and the only remaining vertex is `q`.  Thus `q` is its unique
`Q_i`-neighbour.  Apply this once for each class. \(\square\)

Thus a common root neighbour does not by itself close an actual
two-component interface only when it is inseparable from the two named
boundary-block carriers in this precise incidence sense.  This is a
literal cutvertex/contact obstruction, not a failure caused by the two
carriers lying in one connected open shore.

## 5. Application to opposite boundary responses

In the setting of the audited
[opposite-response theorem](hc7_order8_independent_oct_opposite_response.md),
orient the responses so that the closed shore containing `Q_0,Q_1`
realizes (2.2) and the opposite closed shore realizes only

\[
                             X\mid Y\mid\{d,e\}.                    \tag{5.1}
\]

Corollaries 3.1 and 4.1--4.3 apply verbatim.  Hence every surviving common
`d,e`-neighbour lies inside one of the two named boundary-full connected
subgraphs, and the class-component incidence graph after its deletion has
no relevant connected component spanning either bipartition class.  All
other common-neighbour configurations already give a common split-root
response and a six-colouring of `G`.

## 6. Exact gain and trust boundary

The theorem generalizes the common-neighbour contraction used in the
audited completion of the three-component two-cut residue.  It removes
both the unnecessary requirement that the root connector split into two
connected pieces and the unnecessary requirement that each open-side
carrier be connected before its boundary block is adjoined.  It applies to
connected open shores, uses literal vertices and contacts, and never
identifies a palette colour with a named subgraph.

It does not eliminate the incidence-entangled cutvertex configuration in
Corollary 4.2, split a named boundary-full subgraph through its common
neighbour, or produce an order-seven separation from that configuration.
Those are the exact remaining host-level obligations in this branch.

## 7. Dependencies

- six-colourability of every proper minor of `G`;
- the opposite-response theorem only for the application in Section 5.
