# A six-terminal crossing decoder for the exceptional `3+1` quotient

**Status:** written lemma with deterministic finite certificate checker;
independently audited in
[`hc7_disjoint_k6minus_six_terminal_crossing_decoder_audit.md`](hc7_disjoint_k6minus_six_terminal_crossing_decoder_audit.md).
This result compresses the two-web compatibility problem but does not close
it or prove `HC_7`.

## 1. Configuration

Use the normalized configuration from
[`hc7_disjoint_k6minus_support6_bridge_augmentation.md`](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md).
Thus

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\},
\]

the set \(\{a_0,a_1,a_2,a_3\}\) is a clique, `xy` is an edge,
`x` is adjacent to `a_0,a_1,a_2`, and `y` is adjacent to `a_3`.
The graph on `B` is `K_6` minus `pq`.  Six pairwise vertex-disjoint paths
join

\[
 a_i\!\mathbin{-}\!b_i\ (0\le i\le2),\quad
 a_3\!\mathbin{-}\!p,\quad x\!\mathbin{-}\!q,\quad
 y\!\mathbin{-}\!r.                                  \tag{1.1}
\]

Call two paths a **clean crossing** if they are vertex-disjoint, have four
distinct ends in `A union B`, and their interiors avoid `A union B` and all
six paths in (1.1).

Consider the cyclic order

\[
                         (a_3,y,x,q,r,p).               \tag{1.2}
\]

For indices `i<j<k<l`, a crossing type means paths joining the first and
third, and the second and fourth, terminals selected from (1.2).

## 2. Exact decoder

### Theorem 2.1 (six-terminal crossing decoder)

If a clean crossing of (1.2) has any type other than

\[
 (a_3x,yq),\qquad (a_3x,yr),\qquad (a_3x,yp),          \tag{2.1}
\]

then `G` contains a `K_7` minor.

For each of the three types in (2.1), the twelve-vertex endpoint quotient
contains no `K_7` minor.  More strongly, the fourteen-vertex bare graph in
which each crossing edge is replaced by a two-edge path with its own new
internal vertex also contains no `K_7` minor.  Hence a genuine pair of
clean paths of one of the types in (2.1) is not, by itself, a sufficient
minor certificate.  These finite negative graphs are not seven-connected;
they are barriers to the local crossing decoder, not counterexamples to the
host theorem.

#### Proof

Contract every path in (1.1) toward one end until one edge remains.  Do the
same to the two clean crossing paths.  The disjointness hypothesis makes
all eight contractions simultaneous and label-preserving.  Delete every
edge not listed in Section 1 or supplied by the crossing.  It is therefore
enough to exhibit a `K_7`-minor model in the resulting twelve-vertex graph.

The following table gives seven branch sets for all twelve positive
crossing types.  A concatenated string denotes one branch set; commas
separate branch sets.

| crossing edges | seven branch sets |
|---|---|
| `a3q, yr` | `b0, b1, b2, r, q, a3p, a0a1a2xy` |
| `a3q, yp` | `b0, b1, b2, r, p, a3q, a0a1a2xy` |
| `a3r, yp` | `b0, b1, b2, r, p, xyq, a0a1a2a3` |
| `a3q, xr` | `b0, b1, b2, r, q, a3yp, a0a1a2x` |
| `a3q, xp` | `b0, b1, b2, r, p, xq, a0a1a2a3y` |
| `a3r, xp` | `b0, b1, b2, r, p, xyq, a0a1a2a3` |
| `a3r, qp` | `b0, b1, b2, r, p, q, a0a1a2a3xy` |
| `yq, xr` | `b0, b1, b2, r, q, a3yp, a0a1a2x` |
| `yq, xp` | `b0, b1, b2, r, p, xq, a0a1a2a3y` |
| `yr, xp` | `b0, b1, b2, r, p, xq, a0a1a2a3y` |
| `yr, qp` | `b0, b1, b2, r, p, q, a0a1a2a3xy` |
| `xr, qp` | `b0, b1, b2, r, p, q, a0a1a2a3xy` |

Each row is checked directly: every displayed set is connected and every
two displayed sets are adjacent.  Replacing either added crossing edge by
its clean path lifts the model to `G`: put the internal vertices into one
incident branch set when the path is used, and ignore them otherwise.

There are exactly fifteen choices `i<j<k<l` in a six-term cyclic order.
The adjacent checker verifies that the table covers twelve of them and that
the other three are precisely (2.1).  It performs an exact exhaustive
connected-branch-set search on the twelve-vertex endpoint quotients.  For
the fourteen-vertex subdivided graphs it repeatedly uses the elementary
fact that, when `deg(v)<6`, a `K_7` model either avoids `v` or contains an
edge incident with `v` inside its branch set; deletion and the corresponding
edge contractions therefore give an exact recurrence down to the
twelve-vertex search.  All six negative checks return false.  This proves
both claims. \(\square\)

### Corollary 2.2 (one six-terminal web or one repaired-contact linkage)

Let `Sigma` be the union of the six paths in (1.1), let

\[
 T=\{a_3,y,x,q,r,p\},\qquad
 J=G-\bigl(((A\cup B)\cup V(\Sigma))-T\bigr).          \tag{2.2}
\]

Then at least one of the following holds:

1. `G` contains a `K_7` minor;
2. for some `z in {q,r,p}`, the graph `J` contains vertex-disjoint paths
   from `a_3` to `x` and from `y` to `z`; or
3. `J` has a same-vertex web completion whose frame has cyclic order
   \((a_3,y,x,q,r,p)\).

#### Proof

A crossing of the displayed six-terminal tuple in `J` consists of two
vertex-disjoint paths whose interiors avoid every terminal.  By the
definition of `J`, their interiors also avoid `A union B` and all six paths
in (1.1).  They are therefore a clean crossing.  Theorem 2.1 says that a
crossing either gives outcome 1 or has one of the three forms in outcome 2.
If the tuple is crossless, the Generalised Two Paths Theorem supplies the
same-vertex web completion in outcome 3. \(\square\)

The completion edges in outcome 3 are not edges of `G`.  The point of the
corollary is that it replaces two independently completed four-terminal
graphs by one literal six-terminal test; it does not turn the resulting
six-web into a host separation.

## 3. Consequence for the two-web route

The two four-terminal web certificates leave their common exterior
vertices uncoordinated because their completion edges need not be host
edges.  Theorem 2.1 gives a label-preserving way to replace them by one
six-terminal test: every clean crossed outcome either already gives a
`K_7` minor or includes an `a_3`--`x` path, which repairs the unique missing
contact between the singleton `a_3` and the three-neighbour endpoint `x`
of the two-vertex branch set.

What remains is not a generic web-composition problem.  One must show that
this repaired contact yields a strictly better labelled `K_5` model (or a
proper-minor colouring contradiction), or else prove that all such
`a_3`--`x` paths are intercepted by a bounded literal separator.  The
present theorem proves neither statement.

It is also important that the common path from `y` to `r` cannot itself be
used as the composition path in the recursive Humeau--Pous theorem: `y`
and `r` are consecutive vertices of each four-terminal frame, whereas the
host-side composition theorem starts from a literal path joining
nonconsecutive frame vertices and satisfying additional side-connectivity
hypotheses.

### Proposition 3.1 (what stable rerouting supplies literally)

The six paths in (1.1) may first be rerouted, with all twelve ends fixed,
so that every bridge of their union has attachments on at least two of the
six paths.  Let `C` be a nontrivial bridge, meaning a component outside the
union of the six rerouted paths, and write

\[
             N_\Sigma(C)=N_G(C)\cap\bigcup_{i=0}^5V(P_i).
\]

Then:

1. \(|N_\Sigma(C)|\ge7\);
2. if \(|N_\Sigma(C)|=7\), this set is the boundary of an actual
   order-seven separation with open shore `C`; and
3. in a `K_7`-minor-free graph, `C` cannot have both an attachment in
   \(P_5-y\) and an attachment in \(P_i-b_i\) for any
   \(i\in\{0,1,2\}\).

#### Proof

Tutte's stable-bridges theorem, in the fixed-end path-system formulation,
applies because `G` is seven-connected and there are six paths.  It gives
the first sentence while preserving every label.

The component `C` has no neighbour outside its skeleton attachment set.
If that set had order at most six, deleting it would separate `C` from the
twelve distinct skeleton ends, not all of which can belong to a set of
order at most six.  This contradicts seven-connectivity and proves item 1.
If its order is seven, the same observation gives the separation

\[
 \bigl(V(C)\cup N_\Sigma(C),\;V(G)\setminus V(C)\bigr). \tag{3.1}
\]

Its far open shore is nonempty because the skeleton has twelve distinct
ends.  This proves item 2.

For item 3, suppose `u` is an attachment in `P_5-y` and `v` is an
attachment in `P_i-b_i`.  A shortest `u`--`v` path through the connected
component `C` has all internal vertices in `C`.  It is therefore a clean
augmenting path of the kind used in Theorem 2.1 of the bridge-augmentation
note, which gives a `K_7` minor. \(\square\)

This proposition is deliberately endpoint-sensitive: attachments at `y`
or at one of `b_0,b_1,b_2` do not satisfy item 3.  It also does not turn an
attachment set of order at least eight into a bounded separation.  A
2-stable bridge can still have all its routes through one internal vertex;
stability alone does not manufacture the two vertex-disjoint crossed paths
needed by the earlier crossed-cycle theorem.

## 4. Verification

Run from the repository root:

```sh
python3 results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.py
```

The checker uses only the Python standard library.  It verifies every
positive branch-set certificate and independently performs the exact
negative searches.  No unbounded conclusion is inferred from those finite
negative examples.

Stable rerouting in Proposition 3.1 uses Tutte's theorem in the formulation
of P. Wollan, *Bridges in Highly Connected Graphs*, SIAM Journal on
Discrete Mathematics 24 (2010), 1731--1741,
[Theorem 1.1](https://doi.org/10.1137/070710214).

Corollary 2.2 uses S. Humeau and D. Pous, *On the Two Paths Theorem and the
Two Disjoint Paths Problem*,
[Theorem 1.5](https://arxiv.org/abs/2505.16431).
