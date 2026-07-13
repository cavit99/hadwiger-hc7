# The minimum `C6+K1` atom promotes a singleton hub to a joint-edge warehouse

## 1. Scope and notation

Let `G` be a hypothetical proper-minor-minimal counterexample to
`HC_7`.  Let `S` be an exact seven-cut such that

\[
                  \overline{G[S]}=C_6\dot\cup K_1,
\]

and let `D,H` be the two full shores, with `D` chosen as a minimum
seven-fragment.  We use the already audited consequences recorded in
`hadwiger_c6_minimum_interface_square.md`:

* `D` is three-connected; and
* for every nonempty proper `C subset D`,
  \[
       |N_S(C)|+|N_D(C)-C|\ge 8.                 \tag{1.1}
  \]

The strict inequality over seven in (1.1) is exactly the exclusion of a
proper nested minimum fragment inside `D`.

Assume the singleton-hub outcome

\[
                  D=\{h\}\mathbin{\dot\cup}Y,   \tag{1.2}
\]

where `Y` is connected and full to `S`, and put

\[
                  P_h=N_S(h),\qquad p=|P_h|.
\]

The two-piece atlas and atomic surplus give

\[
                  p\le4,qquad |N_Y(h)|\ge8-p.   \tag{1.3}
\]

The point of this note is that the hub cannot remain a one-vertex
object.  It has an adjacent partner whose deletion also leaves a full
shore, and the edge between the two partners carries one exact
minor-transition state with two five-palette warehouses on the specified
shore.

## 2. A full-deletion neighbour always exists

### Theorem 2.1 (hub promotion)

There is a vertex

\[
                         w\in N_Y(h)              \tag{2.1}
\]

such that `D-w` is full to `S`.

#### Proof

Call `w in N_Y(h)` bad when `D-w` is not full.  Since `h` already
contacts every label in `P_h`, a bad vertex has a witness

\[
             s_w\in S-P_h,\qquad N_Y(s_w)=\{w\}. \tag{2.2}
\]

Distinct bad vertices have distinct witnesses: one boundary label cannot
have two different singleton portal sets.  Hence

\[
       |\{w\in N_Y(h):w\text{ is bad}\}|
          \le |S-P_h|=7-p.                        \tag{2.3}
\]

But (1.3) gives at least `8-p` neighbours of `h` in `Y`.  At least one
is not bad.  This is the required `w`.  QED.

This is a genuine use of the strict atomic surplus.  With only
seven-connectivity, (1.3) would have `7-p` on the right and every
internal neighbour of the hub could be the unique portal of a different
missing boundary label.

## 3. The promoted pair has only one boundary warehouse

Fix `w` as in Theorem 2.1 and put

\[
                       B=D-\{h,w\}.               \tag{3.1}
\]

### Theorem 3.1 (joint-edge one-hole core)

The following hold.

1. `B` is nonempty and connected, and both `h` and `w` have a neighbour
   in `B`.
2. `B` misses at most one boundary label:
   \[
                       |S-N_S(B)|\le1.             \tag{3.2}
   \]
3. If `lambda=S-N_S(B)`, then
   \[
                       \lambda\subseteq
                       N_S(h)\cap N_S(w).          \tag{3.3}
   \]
   Thus the sole possible missing label of the body is represented
   literally at both ends of the promoted edge.
4. The connected split
   \[
                  \{h,w\}\mid B                   \tag{3.4}
   \]
   covers `S`.  If its three-helper quotient is negative, the exact
   two-piece atlas says:
   * when `lambda=emptyset`, the defect of `\{h,w\}` contains one of
     the two prism triangles or the complement of an antipodal pair;
   * when `lambda=\{v\}`, either the same large-defect alternative
     holds or `v` is a cycle vertex and the defect of `\{h,w\}`
     contains `N_{C_6}(v)`.
5. The promoted vertex is itself a hub of the same kind:
   \[
        |N_S(w)|\le4,\qquad |N_{D-w}(w)|\ge4,
        \qquad D-w\text{ is full to }S.           \tag{3.5}
   \]

#### Proof

The shore has at least five vertices because `h` has at least four
distinct neighbours in `Y`.  Three-connectivity of `D` implies that
deleting `h,w` leaves a nonempty connected graph, and also that each of
`h,w` has a neighbour in it.  This proves item 1.

Apply (1.1) to `B`.  Its neighbours in `D-B` lie in the two-element set
`\{h,w\}`.  Therefore

\[
          8\le |N_S(B)|+|N_D(B)-B|
             \le |N_S(B)|+2,
\]

which proves (3.2).

If a label `s` is absent from `B`, fullness of `D-h` forces `w` to
contact `s`, while fullness of `D-w` forces `h` to contact `s`.  This is
(3.3), and it also proves coverage in item 4.  Contracting the opposite
full shore `H`, the pair `\{h,w\}`, and `B` gives exactly the quotient
of the audited 28-row two-piece atlas.  Read the rows whose second
defect has order zero or one.  With an empty second defect only the
empty-coordinate triangle/antipodal-complement rows occur.  With second
defect `\{v\}`, those rows may still be enlarged by `v`, and the only
additional maximal row is `N_{C_6}(v)\mid\{v\}`.  This proves item 4.

Finally apply the singleton/full-body row of the same atlas to
`\{w\}\mid(D-w)`.  It gives `|N_S(w)|\le4`.  Atomic surplus for the
proper singleton `\{w\}` then gives

\[
                 |N_{D-w}(w)|\ge8-|N_S(w)|\ge4,
\]

which proves item 5.
QED.

The theorem converts the former alpha-hub language into a literal
two-vertex core.  It also removes the unbounded alpha warehouse: the
body opposite the core has at most one missing boundary portal, and
that portal has two specified representatives, namely `h,w`.

### Theorem 3.2 (the joint edge is the singleton side of a rooted `K_4`)

There is a connected adjacent bipartition

\[
                         B=B_1\dot\cup B_2         \tag{3.6}
\]

such that each `B_i` is adjacent to both `h` and `w`.  Consequently

\[
                         \{h\},\ \{w\},\ B_1,\ B_2 \tag{3.7}
\]

is a `K_4`-model with the two promoted endpoints as prescribed singleton
bags.  Moreover `B_1 union B_2` contacts all but at most one vertex of
`S`, and that exceptional vertex, if present, contacts both singleton
bags.

#### Proof

There are two internally vertex-disjoint `h-w` paths in `D-hw`.
Indeed, `D-h` is two-connected and `h` has at least two neighbours other
than `w`.  The two-fan lemma in `D-h`, from `w` to
`N_D(h)-\{w\}`, gives two internally disjoint paths with distinct ends;
prepend to their ends the two corresponding edges from `h`.

The interiors of the two paths are disjoint connected subgraphs of `B`,
each adjacent to both `h,w`.  If those interiors are not adjacent, join them by a shortest
path in the connected graph `B` and split the internal vertices of that
path between its two ends.  We obtain disjoint connected adjacent cores,
each still adjacent to `h,w`.

Extend the two cores to a connected bipartition of all of `B` by
Lemma 1.1 of `hadwiger_atomic_portal_order_operation_states.md` (or by
contracting the cores in a spanning tree and deleting one edge on the
path between them).  All six adjacencies in (3.7) are now present.  The
last assertion is exactly (3.2)--(3.3).  QED.

Thus the singleton branch already supplies a nontrivial rooted-model
principle: it canonically contains a `K_4` whose two prescribed singleton
bags are precisely the endpoints of the critical operation.  The
remaining allocation problem is only to distribute the almost-full
boundary contacts of `B_1 union B_2` between those two body bags while
retaining two additional boundary branch sets.

That allocation is not static.  The final row printed by
`c6_square_static_probe.py` replaces the four helper square by a helper
`K_4`, makes the last two helpers together miss only boundary label `0`,
and makes both singleton helpers contact `0`.  The resulting quotient
still has no `K_7` model.  Thus Theorem 4.1's operation state, rather than
the rooted `K_4` alone, is indispensable.

### Theorem 3.3 (hub graph: cycle or an exact portal star)

Define the full-deletion hub set

\[
             \mathcal H=\{u\in D:D-u\text{ is full to }S\}. \tag{3.8}
\]

Then the induced graph `D[mathcal H]` has minimum degree at least one.
Moreover, if `u` is a leaf of this graph and `p_u=|N_S(u)|`, then

\[
                  d_D(u)=8-p_u,                  \tag{3.9}
\]

and the `7-p_u` neighbours of `u` outside `mathcal H` are in bijection
with `S-N_S(u)`: for each such boundary label `s` there is one vertex
`y_s` satisfying

\[
             N_D(s)=\{y_s\},\qquad uy_s\in E(G). \tag{3.10}
\]

Consequently every component of `D[mathcal H]` contains either a cycle
or a leaf carrying the exact portal star (3.9)--(3.10).

#### Proof

Fix `u in mathcal H` and put `p_u=|N_S(u)|`.  The singleton/full-body
atlas gives `p_u<=4`, and strict atomic surplus at `\{u\}` gives

\[
                         d_D(u)\ge8-p_u.          \tag{3.11}
\]

If a neighbour `y` of `u` is not in `mathcal H`, the same argument as
in Theorem 2.1 gives a witness

\[
       s_y\in S-N_S(u),\qquad N_{D-u}(s_y)=\{y\}.
\]

Different non-hub neighbours have different witnesses.  There are at
most `7-p_u` of them.  Equation (3.11) therefore leaves at least one
neighbour of `u` in `mathcal H`.

If `u` has exactly one hub neighbour, both counts are tight: it has
exactly `7-p_u` non-hub neighbours and equality holds in (3.11).  The
witness injection is then a bijection.  Since `u` itself misses every
label in `S-N_S(u)`, the equation for the portal set strengthens to
`N_D(s_y)=\{y\}`, proving (3.9)--(3.10).  The final graph-theoretic
alternative is immediate for a finite graph of minimum degree one.  QED.

This converts indefinite hub promotion into two uniform objects: a cycle
of full-deletion operation edges, or one exact finite portal star.  It
does not assert that operation states on a hub cycle repeat; that is a
state-holonomy question, not a consequence of finiteness alone.

### Corollary 3.4 (the leaf is an exact degree-eight cell)

Every leaf `u` in Theorem 3.3 has degree exactly eight in `G`, and if
`w` is its unique neighbour in `mathcal H`, then

\[
 N_G(u)=N_S(u)\mathbin{\dot\cup}\{w\}
          \mathbin{\dot\cup}\{y_s:s\in S-N_S(u)\}. \tag{3.12}
\]

Each `y_s` is the unique `D`-portal of its displayed boundary label.

#### Proof

Equation (3.9) gives

\[
                 d_G(u)=|N_S(u)|+d_D(u)=8.
\]

The bijection and the unique additional hub neighbour give the disjoint
decomposition (3.12).  QED.

Thus the terminal portal star is not a new unbounded family: it feeds
directly into the exact degree-eight neighbourhood programme, with more
root information than an arbitrary degree-eight vertex.

## 4. The specified-side operation state

### Theorem 4.1 (joint-edge palette warehouse)

Let `c` be a six-colouring of `G-hw`, and put

\[
                         \alpha=c(h)=c(w).         \tag{4.1}
\]

For every colour `beta ne alpha`:

1. the `alpha/beta` component containing `h` also contains `w`;
2. each of `h,w` has a `beta`-coloured neighbour; and
3. all such neighbours lie in the specified closed shore `D union S`.

Consequently each endpoint has five distinct, colour-labelled portal
vertices in `D union S`.  If `Pi` is the equality partition induced by
`c` on `S`, then

\[
  \Pi\in {\cal E}_6(D-hw,S)\cap {\cal E}_6(H,S),
  \qquad
  \Pi\notin {\cal E}_6(D,S).                     \tag{4.2}
\]

If a boundary-faithful proper-minor operation supported in the opposite
shore induces the same state `Pi`, crossed splicing six-colours `G`.

#### Proof

Restoring `hw` would colour `G` unless its ends have one colour, proving
(4.1).  If, for some `beta`, the two endpoint bichromatic components
were different, interchange `alpha,beta` on the component containing
`h`.  This separates the colours of `h,w`, permits restoration of the
edge, and six-colours `G`, a contradiction.  Hence the component is
common.  Its first edge at each endpoint gives the asserted
`beta`-neighbour.  Distinct colours give distinct neighbours.

The open shores `D` and `H` are anticomplete.  A neighbour of a vertex
of `D` therefore lies in `D union S`, proving the specified-side claim.

The two memberships in (4.2) are restrictions of `c`.  If `Pi` extended
over the unoperated `D`, align its colour names with the restriction on
`H` and glue; this would colour `G`.  The final assertion is the standard
boundary-faithful crossed splice.  QED.

This is stronger than the collective two-leaf star lock: the operation
is on an actual edge, so **both** endpoints support **every** non-alpha
palette, and all ten labelled incidences are on the named shore.

## 5. Audit of the interface-square invocation

The square alternative in
`hadwiger_c6_minimum_interface_square.md` does not yet satisfy the
hypotheses of `hadwiger_double_interface_contraction_exchange.md`.
That theorem assumes that the *complete* interface is exactly two
independent edges.  Lemma 2.2 of the square note proves only that two
independent edges exist and that four connected pieces have a `C_4`
in their adjacency skeleton.  Extra interface edges are not deleted or
excluded.

Indeed extra edges are unavoidable in the minimum atom.  Since `D` is
three-connected, it is three-edge-connected; every connected bipartition
has at least three interface edges.  Thus a matching of order two never
forms the complete interface here.

The distinction is used essentially in the proof of the double-interface
theorem.  With exactly `x_1y_1,x_2y_2` at the interface, failure to glue
two side extensions says their terminal pairs agree in at least one of
the two coordinates.  An extra edge can be the sole monochromatic
obstruction even when both selected coordinates disagree.  The
cross-intersecting star/XOR classification then has no premise.

The static issue is real.  The invariant finder
`c6_square_static_probe.py` exhibits `C_4` helper quotients with an
opposite full helper and no `K_7` model even after a boundary label is
duplicated across the two grouped sides.  This is not a counterexample to
the minimum-atom theorem (the quotient forgets all internal portal
placement), but it proves that a bare square skeleton and a repeated
label are not a static closure.

The correct dynamic object is therefore a multi-interface realization,
not the two-edge XOR cell.  The abstract obstruction in
`hadwiger_multi_interface_hypercube_obstruction.md` shows that deletion
and simultaneous-contraction states alone can absorb every cube direction
once three interface constraints are present.  A proof must use the
placement of those constraints in the four connected square pieces.

## 6. Exact remaining axiom

The singleton-hub branch is now reduced to the joint-edge core of
Theorems 3.1--4.1:

* both endpoint deletions leave full bodies;
* the residual body has defect at most one;
* that one defect, when present, has portals at both endpoints;
* both endpoints carry all five non-alpha palettes on the specified
  shore; and
* the operation state is accepted by the opposite full shore and rejected
  by the original shore.

What is not supplied by any current lemma is a map from these five
**palette labels** to the five labels of a rooted `K_5` model.  Model-bag
warehouses and the palette warehouse in Theorem 4.1 live in different
coordinate systems.  Neither connectivity nor equality-state novelty
identifies them.

The exact missing principle can be stated without Moser labels.

> **Joint-edge rooted exchange.**  In a minimum `k`-fragment behind an
> exact `k`-cut, suppose an edge `uv` has both deletion bodies full, the
> body `D-\{u,v\}` has boundary defect at most one, and every colouring
> of `G-uv` gives the two endpoint-complete `(k-2)`-palette warehouse on
> the specified shore.  Then either a target rooted clique model exists,
> an opposite faithful operation has the same boundary state, or a proper
> nested exact `k`-cut occurs.

For `k=7`, Theorems 2.1--4.1 prove every hypothesis of this principle in
the singleton-hub residue.  The square residue requires the corresponding
geometric hypercube-realization exchange.  Proving either conclusion from
abstract state spectra is impossible; the portal placement must be used.

## 7. Later closure of the hub-leaf alternative

The degree-eight programme now eliminates the leaf outcome of Theorem
3.3 completely.  The transport theorem sends such a leaf to one or two
exterior components.  The sole-exterior case is closed by the audited
eight-boundary theorem in
`hadwiger_transported_degree8_leaf_closure.md`; with two components, the
four-clique locked state closes by
`hadwiger_transported_locked_relay_exchange.md`, and the sole antipodal
row closes by `hadwiger_transported_antipodal_relay_exchange.md`.

### Corollary 7.1 (the full-deletion hub graph has minimum degree two)

In a hypothetical proper-minor-minimal `HC_7` counterexample satisfying
the minimum `C_6 dotunion K_1` atom hypotheses, every vertex of
`D[mathcal H]` has degree at least two.

#### Proof

Theorem 3.3 gives minimum degree at least one.  A vertex of degree one is
the tight degree-eight leaf of Corollary 3.4.  The three transported
closure theorems cited above cover all of its possible exterior-component
and old-boundary rows and give a `K_7` minor.  Hence no such leaf occurs.
QED.

Thus the singleton-hub branch no longer has a terminal portal-star cell.
Its remaining object is a cycle/core of faithful full-deletion edges; the
missing assertion is operation-state holonomy on that core, together with
the palette-to-model alignment already identified in Section 6.

## 8. Full-deletion propagation supersedes the hub dichotomy

The later minimum-fragment argument in
`hadwiger_full_deletion_propagation.md` strengthens Corollary 7.1 all the
way to

\[
                         \mathcal H=V(D).
\]

Indeed, let `C` be a component of `D[mathcal H]` and put
`X=N_D(C)-C`.  Every `x in X` is a nonhub, so some old boundary label has
`x` as its unique portal in `D`; these labels are distinct and none meets
`C`.  Hence

\[
       |N_S(C)|+|X|\le 7,
\]

whereas strict atomic surplus gives at least eight for every nonempty
proper connected subset of the minimum shore.  Thus `C=D`.

Consequently the leaf/cycle alternatives of Theorem 3.3 are no longer the
terminal structure of this branch: every vertex deletion leaves the shore
full, every boundary portal class has at least two members, and the
joint-edge palette warehouse applies to every edge of the three-connected
shore.  The transported degree-eight results remain valid independent
theorems, but the live minimum-atom problem is now the uniform all-edge
rooted exchange problem stated in the propagation note.
