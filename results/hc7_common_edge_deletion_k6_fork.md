# Common edge-deletion chromatic fork and `K_6` regeneration

**Status:** proved and independently audited.  This is a uniform
common-host theorem for two disjoint named edges.  In the atomic twin seam
it upgrades the previously known rooted `K_4` and dominating `K_5`
substrates to a spanning `K_6` model.  It does not yet split a labelled row
or prove the double-lock exchange.

## 1. One-spare-colour lemma

### Lemma 1.1

Let `q>=1`, let `G` be a graph with `chi(G)>q+1`, and let

\[
                       e=ab,\qquad f=cd
\]

be vertex-disjoint edges.  If the common edge-deletion graph

\[
                       H=G-\{e,f\}                     \tag{1.1}
\]

is `q`-colourable, then the four endpoints induce a literal `K_4` in `G`.

### Proof

Fix a `q`-colouring `c` of `H`.  If `c(a) ne c(b)`, then `e` is already
proper; recolouring one endpoint of `f` with one fresh colour gives a
`(q+1)`-colouring of `G`.  This contradicts `chi(G)>q+1`.  Hence
`c(a)=c(b)`, and symmetrically `c(c)=c(d)`.

Now suppose some cross-edge is absent, say `ac notin E(G)`.  Recolour both
`a` and `c` with the same fresh colour, leaving every other vertex as in
`c`.  The restored edges `ab` and `cd` are proper.  Every other edge
incident with `a` or `c` has its other endpoint in one of the old `q`
colours, and `ac` is absent.  Thus this is again a `(q+1)`-colouring of
`G`, a contradiction.

All four edges between `{a,b}` and `{c,d}` are therefore present.  Together
with `ab` and `cd`, they induce the literal `K_4`.  \(\square\)

The proof uses one common spare colour, not a palette-to-model
identification.  It is valid for arbitrary graphs and every `q`.

## 2. Exact `HC_7` consequence

### Theorem 2.1 (common-deletion `K_6` fork)

Let `G` be a strongly seven-contraction-critical graph, and let `e,f` be
vertex-disjoint edges.  Put `H=G-{e,f}`, with edge deletion understood.
Then

\[
                         5\leq\chi(H)\leq6.             \tag{2.1}
\]

and at least one of the following holds:

1. the four endpoints of `e,f` induce a literal `K_4` in `G`; or
2. `chi(H)=6`, so `H` contains a `K_6` minor; when `H` is connected this
   can be enlarged to a spanning `K_6` model.

In particular, if `H` is connected and any cross-edge between the two
endpoint pairs is absent, `H` has a spanning `K_6` model.

### Proof

The upper bound in (2.1) follows because `H` is a proper minor of `G`.
The lower bound is the independently proved common-deletion bound: a
four-colouring of `H`, followed by assigning distinct fresh fifth and
sixth colours to one endpoint of `e` and one endpoint of `f`, would
six-colour `G`.

If `chi(H)=5`, apply Lemma 1.1 with `q=5`; the endpoint set is a literal
`K_4`.  Hence absence of one cross-edge forces `chi(H)=6`.  Hadwiger's
Conjecture for parameter six, which is known, gives a `K_6` minor in `H`.
If `H` is connected, repeatedly absorb each component outside the current
model union into an adjacent bag.  This preserves all six pairwise bag
adjacencies and terminates with a spanning model.  \(\square\)

## 3. Minimal two-edge obstruction signature

### Corollary 3.1

Under the hypotheses of Theorem 2.1, suppose that a cross-edge between the
endpoint pairs is absent and that `H` is connected.  Then

\[
 \chi(H)=\chi(H+e)=\chi(H+f)=6,
 \qquad \chi(H+e+f)=7.                                \tag{3.1}
\]

Moreover, the following exact response signatures hold.

1. Every six-colouring of `H+e`, restricted to `H`, makes `e` proper and
   makes the ends of `f` equal; such a colouring exists.
2. Every six-colouring of `H+f`, restricted to `H`, makes `f` proper and
   makes the ends of `e` equal; such a colouring exists.
3. No six-colouring of `H` makes both `e` and `f` proper.

Equivalently, the two one-edge restorations supply the opposite states
`(proper,equal)` and `(equal,proper)`, while the state
`(proper,proper)` is forbidden.  This corollary alone does not exclude the
state `(equal,equal)`; the stronger audited
[double-contraction theorem](hc7_common_host_double_contraction_lock_allocation.md)
proves that it exists by colouring `G/e/f`.

### Proof

Theorem 2.1 gives `chi(H)=6`.  Each of `H+e=G-f` and `H+f=G-e` is a proper
minor of `G`, so both are six-colourable; since each contains `H`, both
have chromatic number exactly six.  Finally `H+e+f=G` has chromatic number
seven.

Restrict any six-colouring of `H+e` to `H`.  The ends of `e` have different
colours.  If the ends of `f` also had different colours, the same colouring
would extend to `G`, a contradiction.  Existence follows from the exact
chromatic equality in (3.1).  This proves the first signature; the second
is symmetric.  A six-colouring of `H` in which both deleted edges are
proper would itself be a six-colouring of `G`, proving the third.
\(\square\)

Identifying the equal pair in the first response gives a six-colouring of
`G/f`; identifying the equal pair in the second gives one of `G/e`.
Thus the signatures can be chosen as the two named contraction responses,
not merely as colourings of unrelated proper subgraphs.

This is a graph-global state coupling: it refers only to the two literal
edges in their common host.  It does not identify either state with a
boundary equality partition or a row of the spanning `K_6` model.

## 4. Twin-seam corollary

Use the frozen atomic notation

\[
                         e=zu,\qquad f=dt,
\]

where `z in E` and `d in D`, with `D,E` distinct components of `A-Z`.
Then `zd` is absent.  The graph `G-{e,f}` is connected (indeed, deleting
two edges from the seven-connected host cannot disconnect it).  Theorem
2.1 therefore gives a spanning common-host model

\[
                         \mathcal M=(M_1,\ldots,M_6)    \tag{4.1}
\]

in `G-{e,f}`.

This model is common to the separating and bypass branches and is
independent of the selected response colouring.  The literal remaining
problem is:

> Extremize (4.1) relative to the four named endpoints and the opposite
> response signatures in Corollary 3.1.  Either one
> restored edge splits a multiply hit row into two adjacent connected
> pieces which both retain all five foreign-row duties, giving `K_7`; the
> two operation responses reproduce one exact state; a fixed pair is
> exposed; or an actual smaller globally ranked `(1,2)` seven-cell is
> returned.

No conclusion currently guarantees that split.  The four endpoints can
occupy four distinct rows, and distinct first hits can lie in one
unsplittable row.  Thus (4.1) is a stronger uniform substrate, not a hidden
completion of the target theorem.
