# Barrier: ordinary `H`-Wege does not enforce indivisible split bags

## Status

The construction below is a hand-checkable counterexample to the clean
packing/cut version of the proposed indivisible-bundle theorem.  It is
seven-connected and contains three pairwise disjoint, normalized
support-six `K_5` models, but its maximum bag-injective model-good path
packing has order four.  Consequently it has no cut of order at most six
and no seven-path certificate.

The exact construction and scope are separately internally audited GREEN
in the adjacent audit.

The graph deliberately contains a `K_7` minor.  Thus it is **not**
a counterexample to an `HC_7` statement retaining `K_7`-minor-freeness or a
`K_7`-minor outcome.  Its purpose is sharper: it shows that standard
Mader--Robertson--Seymour--Thomas `H`-Wege, followed by exact lifting of
three contracted split bags, cannot by itself prove the desired
bag-injective packing.  In the example the exact dual certificate lifts to
an order-seven separator, not to a cut of order at most six.

## 1. Construction

Let

\[
 S=\{x_1,y_1,x_2,y_2,x_3,y_3,w\}
\]

and let

\[
 Q_i=\{a_i,b_i,c_i,d_i\}\qquad(i=1,2,3)
\]

be three further pairwise disjoint four-sets.  Define `G_*` as follows.

1. Each `Q_i` induces a `K_4`.
2. The only edges inside `S` are `x_i y_i` for `i=1,2,3`.
3. There are no edges between distinct `Q_i,Q_j`.
4. Every vertex of `S` is adjacent to every vertex of every `Q_i`, except
   that

   \[
                  x_i a_i,\ y_i b_i\notin E(G_*)
                  \qquad(i=1,2,3).
   \]

For each `i`, take the four singleton bags in `Q_i` and the edge-bag
`x_i y_i`.  These form a support-six `K_5` model `M_i`.  Its two defect
sets are exactly

\[
                         D_{x_i}=\{a_i\},\qquad
                         D_{y_i}=\{b_i\}.
\]

In particular both defects are nonempty and disjoint, so this is the
normalized `(1,1,2)` split type rather than a redundant enlargement of a
literal `K_5`.  The three model supports are pairwise disjoint.

## 2. Exact connectivity

### Lemma 2.1

`G_*` is seven-connected.

### Proof

Let `R` have order at most six.  At least one vertex of `S-R` remains.
Among the twelve vertices in the three sets `Q_i`, at least six remain, so
some `Q_k-R` has order at least two.  Every vertex of `S` has at most one
nonneighbor in `Q_k`; hence every vertex of `S-R` has a neighbor in the
clique `Q_k-R`.  Thus `G_*[(S\cup Q_k)-R]` is connected.

Consider any nonempty `Q_i-R`.  It is a clique.  If it had no edge to
`S-R`, then, since each of its vertices has at most one nonneighbor in
`S`, the set `S-R` would have to be a singleton, say `{s}`, and
`Q_i-R` would have to be the unique singleton nonadjacent to `s`.  But
leaving only `s` in `S` already uses all six deletions, leaving all four
vertices of `Q_i`; this is impossible.  Hence every nonempty `Q_i-R`
attaches to the connected subgraph containing `S-R`.  Therefore `G_*-R`
is connected.

On the other hand, deleting all seven vertices of `S` separates the three
cliques `Q_i`.  Hence `kappa(G_*)=7`.  \(\square\)

## 3. The bag-injective packing number is four

A **model-good path** has ends in two distinct model supports and has no
internal vertex in any of the three supports.  A family is
**bag-injective** when no two ends at the same model belong to the same
branch bag.

### Lemma 3.1

The maximum number of pairwise vertex-disjoint, bag-injective model-good
paths in `G_*` is four.

### Proof

The union of the three model supports is `V(G_*)-{w}`.  Hence a
model-good path has no internal vertex or has the single internal vertex
`w`.  At most one member of a vertex-disjoint family can use `w`.

A path with no internal vertex is an edge between distinct model supports.
There are no edges between distinct `Q_i,Q_j`, and the only edges inside
`S` join the two vertices of one model.  Therefore every such good edge has
an end in one of the three split bags `x_i y_i`.  Bag-injectivity permits
at most one path end in each split bag.  Thus there are at most three
one-edge members, plus at most one member through `w`, giving an upper
bound of four.

The bound is attained, for example, by

\[
 x_1c_2,\qquad x_2c_3,\qquad x_3c_1,\qquad a_1wa_2.
\]

Their vertices are disjoint and their ends use distinct bags at every
model.  \(\square\)

Combining Lemmas 2.1 and 3.1 shows that the two clean outcomes

* seven bag-injective good paths; or
* an actual cut of order at most six

are not exhaustive, even for the exact normalized split models arising in
the support-six programme.

## 4. What ordinary `H`-Wege actually returns

Contract each `x_i y_i` to `z_i`, obtaining `H`.  Then

\[
                       L_i=Q_i\cup\{z_i\}
\]

is a literal `K_5`, and the three `L_i` are disjoint.  Give each `z_i`
weight two and all other vertices weight one.  The set

\[
                         T=\{z_1,z_2,z_3,w\}
\]

separates the three `Q_i`.  Its ordinary order is four and its lifted
weight is seven.  It is therefore exactly the `(4,3)` anchored-separator
collision from the parallel-contraction law.

There is an explicit Robertson--Seymour--Thomas form of the Mader
certificate.  Set `W=T`; for every vertex `q` in
`Q_1 union Q_2 union Q_3`, take one cell

\[
                            Y_q=X_q=\{q\}.
\]

Then

\[
             |W|+\sum_q\left\lfloor |X_q|/2\right\rfloor=4<7.
\]

The off-boundary condition is vacuous because every `Y_q-X_q` is empty,
and `H-W` contains no good path between distinct `L_i`.  Thus this is a
literal `H`-Wege obstruction of value four.  Expanding the three bundle
vertices replaces `W` by `S`, an order-seven separator.  It does not
produce a separator of order at most six.

This also explains why neither natural **scalar** capacity convention
repairs the issue.  Charging each `z_i` one unit makes the dual set have
cost four but loses the lifted connectivity.  Charging it two units gives
the correct cost seven but no
longer forces a **bag-injective** seven-path primal solution: two units may
be used by two different paths.  The obstruction is a genuine indivisible
three-bundle bottleneck.

## 5. The collision is already a direct minor certificate

The example contains a `K_7` minor, so the obstruction is harmless once an
explicit `K_7`-minor construction is allowed.  The seven branch sets

\[
 \{a_1\},\{b_1\},\{c_1\},\{d_1\},
 \{x_2,c_2\},\{x_3,a_2\},\{w,b_2\}
\]

are connected and pairwise adjacent.  The last three are pairwise adjacent
through the clique `Q_2`, and their `S` vertices are complete to `Q_1`.

Thus the correct research target cannot insist that every successful
composition be represented by seven bag-injective good paths.  A viable
theorem must return at least one of:

1. a bag-injective path packing;
2. an explicit `K_7`-minor model obtained by decoding a bundle bottleneck;
3. an anchored quotient separator whose lift is an exact-seven (or larger)
   labelled handoff; or
4. an actual cut of order at most six.

Standard `H`-Wege supplies the quotient partition in item 3, but does not
perform items 2 or 3's label-preserving HC7 handoff.  That additional
decoder is the substantive missing theorem.

## 6. Trust boundary

The construction proves only the following negative statement:

> Seven-connectivity plus three private normalized split models does not
> force seven bag-injective model-good paths, and ordinary `H`-Wege plus
> exact bundle expansion does not force a cut of order at most six.

It does not refute any statement which assumes `K_7`-minor-freeness, and it
does not produce a counterexample to `HC_7`.  Rather, it proves that
`K_7`-minor-freeness or a direct-minor collision decoder must be used
essentially before the indivisible-bundle route can progress.
