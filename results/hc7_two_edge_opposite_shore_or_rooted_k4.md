# Two independent critical edges: opposite-shore separation or a rooted four-terminal model

**Status:** written proof; separate internal audit GREEN in
[`hc7_two_edge_opposite_shore_or_rooted_k4_audit.md`](hc7_two_edge_opposite_shore_or_rooted_k4_audit.md).
This note
isolates exactly what the universal absence of the fourth edge-response
signature gives for the two independent owner-contact edges in the
concentrated three-owner setting.  It proves an order-seven placement when
the common deletion loses two units of connectivity.  Otherwise it returns
an endpoint-rooted `K_4` model, whose label-preserving absorption is a
separate, presently unproved step.  It does not prove `HC_7`.

## 1. The matching-deletion host

Let `G` be seven-connected and satisfy

\[
 \chi(G)=7,
 \qquad \chi(M)\le 6\quad\hbox{for every proper minor }M\hbox{ of }G.
\tag{1.1}
\]

Let

\[
                         e=ab,\qquad f=cd
\tag{1.2}
\]

be vertex-disjoint edges and put `H=G-{e,f}`, where both operations are
edge deletions.

### Lemma 1.1 (exact response and connectivity bounds)

The graph `H` has the three edge-equality signatures

\[
 ({\rm equal},{\rm equal}),\qquad
 ({\rm equal},{\rm proper}),\qquad
 ({\rm proper},{\rm equal}),
\tag{1.3}
\]

and has no six-colouring with signature
`(proper,proper)`.  Moreover,

\[
                         \chi(H)\in\{5,6\},
                         \qquad \kappa(H)\ge5.
\tag{1.4}
\]

#### Proof

Contracting any nonempty subset of the matching `{e,f}`, six-colouring
the resulting proper minor, and expanding the contracted edges gives the
three signatures in (1.3).  A six-colouring proper on both deleted edges
would remain proper after restoring them and would six-colour `G`.

The graph `H` is a proper minor and hence is six-colourable.  If it were
four-colourable, recolour one end of `e` with a new fifth colour and one end
of `f` with a new sixth colour.  Restoring `e,f` would then give a proper
six-colouring of `G`.  Thus `chi(H)>=5`.

Finally, let `(L,T,R)` be a separation of `H` with both open sides
nonempty.  Seven internally disjoint paths in `G` between fixed vertices
of `L,R` must either meet `T` or use one of the two deleted matching edges
from one open side to the other.  Hence

\[
 |T|+|\{g\in\{e,f\}:g\text{ crosses }(L,T,R)\}|\ge7.
\]

The second term is at most two, so `|T|>=5`.  This proves (1.4). \(\square\)

## 2. Exact placement fork

### Theorem 2.1

At least one of the following holds.

1. `G` has an actual order-seven separation for which `e` belongs only to
   one closed shore and `f` belongs only to the other closed shore.
2. `H` contains a `K_4`-minor model rooted at `a,b,c,d`.

More precisely, outcome 1 holds whenever `kappa(H)=5`; outcome 2 holds
whenever `kappa(H)>=6`.

#### Proof

Suppose first that `kappa(H)=5`, and let `(L,T,R)` be an order-five
separation.  Equality in the separator budget from Lemma 1.1 forces both
deleted edges to cross between `L` and `R`.  Orient their ends as

\[
       a,c\in L,\qquad b,d\in R,
\]

after interchanging endpoint names if necessary.  Put

\[
                            S^*=T\cup\{b,c\}.
\tag{2.1}
\]

Every edge of `G-S^*` between the residual `L`- and `R`-sides would be an
edge of `H-T`, except possibly `e` or `f`.  The edge `e=ab` has its
`R`-end `b` in `S^*`, and `f=cd` has its `L`-end `c` there.  Thus no such
edge remains.  The residual sides are nonempty because they contain `a`
and `d`, respectively.  Hence `S^*` is an actual seven-vertex separator.
The edge `e` is contained in the closed `L`-shore and not in the closed
`R`-shore, while `f` has the opposite placement.  This is outcome 1.

If `kappa(H)>=6`, Jung's two-linkage theorem makes `H` two-linked.  Hence
all three pairings of the four nominated vertices `a,b,c,d` have disjoint
linkages.  The rooted-`K_4` characterization for a three-connected graph
(Fabila-Monroy--Wood, Theorem 8) gives a `K_4`-minor model rooted at those
four vertices.  This is outcome 2. \(\square\)

### Remark 2.2 (the nonplanar strengthening)

Lemma 1.1 makes `H` at least five-chromatic, hence nonplanar by the Four
Colour Theorem.  Jung's stronger formulation that every four-connected
nonplanar graph is two-linked therefore in fact gives the rooted `K_4`
model throughout the setting, including the order-five-separator branch.
The useful extra conclusion of the latter branch is the literal
opposite-shore placement in (2.1), not merely rooted linkage.

## 3. A third-edge probe

Let `h=xy` be an edge vertex-disjoint from `e,f` and put

\[
                         J=G-\{e,f,h\}.
\tag{3.1}
\]

### Proposition 3.1

The common host `J` realizes every one of the seven equality signatures on
`(e,f,h)` except `(proper,proper,proper)`.  It has connectivity at least
four.  If `kappa(J)=4`, then `G` has an actual order-seven separation
placing `e` and `f` on opposite closed shores.

#### Proof

For every nonempty subset of the three-edge matching, contract precisely
those edges, six-colour the proper minor, expand, and delete all three
edges.  Since the edges are independent, the resulting signature is exact.
The all-proper signature would six-colour `G`.

The matching-deletion separator budget gives `kappa(J)>=7-3=4`.  At an
order-four separation equality forces all three deleted edges to cross.
Choose the endpoint of `e` on one open side and the endpoint of `f` on the
other open side, together with either endpoint of `h`, and add these three
vertices to the four-vertex boundary.  The unchosen ends of `e,f` remain
on opposite open sides, so both are nonempty.  The chosen seven vertices
delete every restored crossing edge, and `e,f` lie on opposite closed
shores exactly as in Theorem 2.1. \(\square\)

Thus a third proper-minor response helps only if the third edge deletion
exposes the sharp four-vertex cut.  When `J` remains five-connected, its
new `(proper,proper,equal)` response merely replaces the forbidden
two-edge signature by a monochromatic third edge; it does not identify a
branch-set label or synchronize a boundary partition.

## 4. Exact failed implication in the concentrated three-owner setting

For the owner-contact edges

\[
       e=a_1s_1,\qquad f=a_2s_2
\]

from the audited three-owner concentration theorem, Theorem 2.1 leaves
only the following implication unproved:

> **Label-preserving rooted-model absorption.**  Given an endpoint-rooted
> `K_4` model in `G-{e,f}`, either choose its four branch sets so that they
> can replace the portions of the donor and the two owner branch sets
> while three named completing branch sets remain connected, disjoint and
> adjacent to all four; or use the first unavoidable intersection with a
> completing branch set to obtain a strict donor reduction or an actual
> order-seven separation preserving the two selected edge responses.

Ordinary rooted linkage does not prove this statement.  Its four branch
sets may traverse any of the five inherited common branch sets, and
contracting them can destroy the retained donor root, the prescribed
first-hit labels, or the selected boundary partition.  The third-edge
response in Proposition 3.1 supplies no additional literal avoidance.

Consequently the universal absence of `(proper,proper)` has been fully
spent at the purely edge-response level: it gives the exact signature
cube, separator budgets, and endpoint-rooted `K_4`; the next implication
is genuinely a label-preserving rooted-minor extraction theorem.  Treating
the unlabelled rooted `K_4` as though it already supplied the three
reserved completing branch sets is the first invalid inference.

In fact, the placement fork itself is connectivity-driven: the prohibition
of `(proper,proper)` certifies nonextendability but contributes no literal
location for either edge.  Thus it cannot be promoted to a shore-placement
principle without precisely the additional label-preserving implication
displayed above.

## 5. Dependencies and trust boundary

* the matching-deletion separator budget;
* Jung's two-linkage theorem, quoted in Stephens--Ye, *Connectivity for
  Kite-Linked Graphs*, Theorem 1.1, and the stronger four-connected
  nonplanar formulation recorded in their introduction;
* Fabila-Monroy--Wood, Theorem 8; and
* the three exact contraction signatures for independent edges.

The theorem is uniform and literal.  It does not prove the
label-preserving absorption statement in Section 4, a common boundary
partition, or `HC_7`.
