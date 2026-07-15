# Independent audit: two named-edge disjoint cycles

**Verdict:** GREEN after three scope/wording corrections in the adjacent
theorem note.  The two mathematical conclusions are valid.  The audit
corrected the comparison with three linkages, made the definition of the
layer union exact, and restricted the claimed web closure to the
unrestricted common host.

## 1. Edge deletion and connectivity

Lemma 2.1 is correct.  If `X`, with `|X|<=k-2`, disconnects `J-xy`, then
neither end of `xy` lies in `X`; otherwise deleting `xy` has no effect on
`J-X`.  Adding the one edge `xy` can connect `J-xy-X` only if that graph
has exactly two components, one containing each end.

Both components have at least two vertices.  If the component containing
`x` were `{x}`, then every neighbour of `x` other than `y` would lie in
`X`, giving

\[
                     d_J(x)\le |X|+1\le k-1,
\]

contrary to the standard consequence `delta(J)>=k`.  Deleting
`X union {x}` from `J` then leaves the two nonempty anticomplete sets
`A-{x}` and `B`, contradicting `k`-connectivity.  No extra assumption on
the edge is used.

Apply the lemma first to `G-e` and then to `(G-e)-f`.  Since `e` and `f`
are distinct, `f` remains an edge after the first deletion.  Thus

\[
                    \kappa(G-\{e,f\})\ge 5.
\]

The disjointness of `e,f` is not needed for this connectivity calculation,
but is needed for four distinct named roots and is used transparently in
the endpoint description.

## 2. Nonplanarity

Seven-connectivity implies `delta(G)>=7` and `|V(G)|>=8`.  Deleting two
edges lowers the total degree sum by exactly four.  Hence, for
`H=G-{e,f}` and `n=|V(G)|`,

\[
                \sum_{v\in V(H)}d_H(v)
                =\sum_{v\in V(G)}d_G(v)-4
                \ge 7n-4.
\]

This is stronger than the planar simple-graph bound `6n-12`.  The source's
displayed endpoint count is therefore correct.  The condition `n>=3`
needed for the planar bound is automatic.

## 3. Jung's theorem

The cited result has exactly the required prescribed-terminal form.
Corollary 1 of Thomassen's *2-Linked Graphs* says that for four distinct
vertices `x1,x2,y1,y2` in a four-connected graph there is an
`(x1y1,x2y2)` linkage unless the graph is planar with a facial cycle
containing `x1,x2,y1,y2` in that cyclic order.  It is attributed there to
Jung.  In particular, every four-connected nonplanar graph is two-linked.

The graph `H` is five-connected and nonplanar, so the theorem applies to
the ordered pairs `(z,u)` and `(d,t)`.  Both named edges are absent from
`H`.  Each returned path therefore has length at least two, and adding its
corresponding edge produces a cycle.  Vertex-disjointness of the paths and
distinctness of all four ends make the two cycles vertex-disjoint.

## 4. Rooted `K_4`

Fabila-Monroy--Wood, Theorem 6, states exactly that, for four distinct
nominated vertices in a four-connected graph, either there is a rooted
`K_4` minor or the graph is planar with all four vertices on one face.
The nonplanarity of `H` excludes the second outcome, so the four branch
sets in Theorem 1.2 follow with their literal root labels.

The original phrase saying this is *strictly stronger* than all three
two-linkages was inaccurate under the present hypotheses.  The same
paper's Theorem 8 says that in a three-connected graph a rooted `K_4` at
four roots is equivalent to existence of all three pairings.  The adjacent
note now describes the rooted model correctly as one simultaneous
label-preserving certificate and as stronger than the single prescribed
linkage of Theorem 1.1.

## 5. Distinct twin-seam roots

In the frozen twin seam, `D` and `E` are distinct components of `A-Z`,
while `Z` is disjoint from both.  The old boundary `S` is disjoint from the
open lobes, and the displayed disjoint unions

\[
       \Omega_D=Z\mathbin{\dot\cup}T_D,
       \qquad
       \Omega_E=Z\mathbin{\dot\cup}T_E,
       \qquad T_D\cup T_E=S
\]

also imply \(Z\cap S=\varnothing\).  Thus

\[
                 z\in E,\quad d\in D,\quad
                 u\in S,\quad t\in Z
\]

are four distinct vertices.  The specialization to `e=zu` and `f=dt` is
valid.

## 6. Response-bundle facts

The four auxiliary claims in Section 5 are also correct.

1. In a colouring of `G-f`, a Kempe swap on a `gamma-epsilon` component
   containing `d` would restore `f` unless the component also contains
   `t`.  Hence every such layer has a `d-t` path.  Paths from two distinct
   layers can share away from the ends only vertices coloured `gamma`.
2. The present edge `e` has one fixed unordered endpoint-colour pair and
   hence lies in at most one of the five `gamma-epsilon` layers.  Four
   selected layer paths avoid it; all avoid the deleted edge `f`.
3. With `U` defined exactly as the union of all edges incident with a
   `gamma` vertex, Menger gives either two internally disjoint `d-t` paths
   or one internal separator `w`.  A separator common to all five layers
   has colour in every set `{gamma,epsilon}`, and therefore has colour
   `gamma`.
4. The graph `G-f` is six-connected.  It has six internally disjoint
   `d-t` paths; after discarding at most one through `w` and at most one
   further path using `e`, four remain.  Every `w`-avoiding path has an edge
   outside `U`, whose two ends are both non-`gamma`.

The exact definition of `U` matters in the last implication and has been
made explicit in the theorem note.

## 7. Exact consequence for the proof spine

The theorem eliminates only the unrestricted two-linkage/web obstruction
in the whole common deletion `G-{e,f}`.  It does not show that either path
lies in a named Kempe layer, one twin shore, an old packet, or a prescribed
model row.  The corrected scope language now records this boundary.

Nor does the rooted `K_4` immediately give a labelled carrier split or a
`K_7` model.  Its four bags may consume vertices from both lobes, both old
packets, and a regenerated `K_6` model, with no controlled disjointness or
row contacts.  Three additional branch sets for a `K_7` would have to be
pairwise adjacent, disjoint from the rooted core, and adjacent to every
rooted bag; none of those duties follows from the rooted theorem.

The adjacent two-apex icosahedron barrier gives a useful guardrail.  It is
seven-connected and `K_7`-minor-free, so after deleting any two disjoint
edges the present theorem still supplies the four-pole rooted `K_4`; the
host nevertheless has no `K_7`.  That example is not a twin-seam
counterexample and has a valid fixed pair, but it proves that the rooted
core alone cannot be promoted to a `K_7`.  A promotion in the active seam
must use the exact proper-minor states, labelled packet/row contacts, or a
coherent fixed-pair endgame.
