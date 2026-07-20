# A terminal edge of a minimal compound separator need not retain the selected response

**Status:** explicit finite barrier to an intermediate inference;
[separately audited GREEN](hc7_order8_compound_separator_terminal_edge_barrier_audit.md), with deterministic verifier in
[`hc7_order8_compound_separator_terminal_edge_barrier_verify.py`](hc7_order8_compound_separator_terminal_edge_barrier_verify.py).
This is not a counterexample to `HC_7`.

## 1. Inference refuted

The following static conclusion is false.

> Let
> \[
> S=\{d,e\}\mathbin{\dot\cup}X\mathbin{\dot\cup}Y,
> \qquad |X|=|Y|=3,
> \]
> and let a connected open shore `R` have an adjacent connected partition
> `R=Q_0 dotcup Q_1`, where both parts are adjacent to every literal vertex
> of `S`.  Suppose the closed shore realizes
> \[
> X\mid Y\mid\{d\}\mid\{e\}
> \]
> but rejects
> \[
> X\mid Y\mid\{d,e\}.
> \]
> Assume that, inside each `Q_i`, the root-connecting subgraphs, the
> `X`-connecting sets and the `Y`-connecting sets are pairwise
> cross-intersecting.  Choose an inclusion-minimal connected
> `X`-support `A subseteq Q_0` and an inclusion-minimal connected
> `Y`-support `B subseteq Q_1` so that `A union B` meets every connected
> subgraph adjacent to both roots.  Then deleting a terminal edge of `A`
> makes the rejected merged-root partition extend through the shore.

Here a set `F` connects `X` when `G[X union F]` is connected and contains
an edge, and similarly for `Y`.  The example below satisfies the displayed
geometric and colouring hypotheses, but its terminal edge does not retain
the selected response.

The barrier does **not** refute a host theorem which also uses
seven-chromaticity, universal proper-minor six-colourability, and the
complete response language at the terminal edge.  It proves that those
global hypotheses must establish response retention; support minimality and
`K_7`-minor exclusion do not establish it.

## 2. Construction

Number the boundary and open-shore vertices by

```text
d=0, e=1, X={2,3,4}, Y={5,6,7},
Q0={8,9,12}, Q1={10,11}.
```

The edge set is

```text
(0,3) (0,6) (0,8) (0,9) (0,10)
(1,3) (1,4) (1,5) (1,6) (1,9) (1,11)
(2,11) (2,12)
(3,5) (3,6) (3,8) (3,10)
(4,5) (4,9) (4,11)
(5,9) (5,10) (5,11)
(6,8) (6,9) (6,10) (6,11)
(7,8) (7,11)
(8,9) (8,10) (8,11) (8,12)
(9,10) (9,11) (10,11).
```

Both `Q_0` and `Q_1` are connected, an edge joins them, and each is
adjacent to all eight boundary vertices.

For the split-root trace, fix boundary colours

```text
X=0, Y=1, d=2, e=3.
```

It extends by assigning colours

```text
(8,9,10,11,12)=(3,4,5,2,1).
```

Exhaustive six-colour search shows that the merged-root trace

```text
X=0, Y=1, d=e=2
```

does not extend.

## 3. The minimal compound separator

The inclusion-minimal root-connecting sets are

```text
{9}, {8,11}, {10,11}.
```

The inclusion-minimal `X`-connecting sets are

```text
{8,11}, {10,11}, {8,9,12},
```

and the inclusion-minimal `Y`-connecting sets are

```text
{11}, {8,9}, {8,10}.
```

Inside `Q_0`, take

\[
                       A=\{8,9,12\}.
\]

It is an inclusion-minimal connected `X`-support: the three boundary
vertices `2,3,4` attach respectively through `12,8,9`.  Inside `Q_1`, take

\[
                       B=\{11\},
\]

which connects all of `Y`.  The union

\[
                       K=A\mathbin{\dot\cup}B
                        =\{8,9,11,12\}
\]

meets every root-connecting set.  Thus it is exactly the proposed compound
root separator.  Direct enumeration also verifies, separately in each
`Q_i`, that each of the root, `X` and `Y` support families
cross-intersects each of the other two families.  There is no disjoint
choice of one root connector, one `X`-support and one `Y`-support.

The vertex `12` is a leaf of `G[A]`, and

\[
                            f=8\,12
\]

is its terminal support edge.  Nevertheless, deleting `f` still does not
make the merged-root boundary trace extend.  The four vertices
`8,9,10,11` continue to induce a clique, and each continues to see the
three boundary colours used on `X`, `Y` and the merged root block.  Hence
they would require four colours from the remaining three; the exhaustive
checker verifies the same conclusion directly.

## 4. Minor exclusion

The verifier checks a tree decomposition of width five for the whole
thirteen-vertex boundaried graph.  Therefore it has no `K_7` minor.  It
also checks a width-two decomposition of the boundary graph, which in
particular excludes a boundary `K_5` minor.

The new vertex `12` lies in the leaf bag `{2,8,12}` attached to the old
width-five decomposition.  Thus the certificate is not relying on an
unverified minor search.

## 5. Exact consequence for the live proof step

For an internal edge `f` of the split-response shore, contraction-criticality
only guarantees a six-colouring of `G-f`.  Its boundary partition lies in
the extension language of the intact opposite shore and is rejected by the
intact operated shore.  It need not be the previously selected merged-root
partition.  The compound-separator minimality is purely incidence data and
does not relate that new partition to the selected one.

Therefore a valid terminal-edge theorem needs an additional, genuinely
dynamic conclusion, for example

\[
 \Pi_{\rm merged}\in
 \operatorname{Ext}(G[(R\cup S)]-f,S),
\]

or a proof that a different operation-specific partition already gives one
of the declared terminal outcomes.  Without such a response-retention
statement, the five endpoint bichromatic locks are indexed only by palette
colours and cannot be assigned to the five inherited branch-set labels.

## 6. Trust boundary

The construction supplies one closed shore only.  It is not asserted to
extend to a seven-connected, seven-chromatic, contraction-critical host,
nor to carry an opposite merged-only shore.  It consequently does not
refute the active host-level disjunction allowing an explicit `K_7` model,
a compatible order-seven separation, or a strict labelled descent.

It refutes exactly the missing shortcut: minimal compound-separator
geometry, pairwise cross-intersection and `K_7`-minor exclusion do not make
a terminal support edge preserve the selected colouring response.
