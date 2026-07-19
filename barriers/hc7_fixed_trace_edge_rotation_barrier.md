# A fixed boundary response can rotate between repeated model contacts without descent

**Status:** written unbounded barrier; deterministic verifier included;
separate internal audit GREEN in
[`hc7_fixed_trace_edge_rotation_barrier_audit.md`](hc7_fixed_trace_edge_rotation_barrier_audit.md).
This is not a counterexample to `HC_7`.

The construction shows that the dynamic information currently available at
a repeated first-hit exposure still does not force a strict
response-preserving descent.  It simultaneously has seven-connectivity, an
actual seven-vertex separator with two boundary-full shores, one fixed
boundary partition attained after deleting any of several critical edges,
and a spanning labelled clique-minor model preserved after deleting either
of two repeated contact edges.  Nevertheless the selected partition does
not extend through the original opposite shore and the fixed-trace
list-critical subgraph never becomes smaller.

The construction contains an explicit `K_7`-minor model.  Thus it does not
refute a terminal-aware exchange theorem whose conclusions include a
`K_7` minor.  It proves that such a theorem must use `K_7`-minor exclusion
inside the exchange; it cannot first deduce descent or colour gluing from
the response and invoke minor exclusion only afterwards.

## 1. Construction

Fix an odd integer `n>=7`.  Let

\[
 S=K\mathbin{\dot\cup}J,\qquad
 K=\{k_0,k_1,k_2,k_3\},qquad
 J=\{j_0,j_1,j_2\},                                  \tag{1.1}
\]

where `G[S]` consists of the clique `K` and three isolated vertices `J`.
Let

\[
 R=r_0r_1\cdots r_{n-1}r_0                             \tag{1.2}
\]

be an induced odd cycle, and add one further vertex `a`.  Add every edge
between `R` and `S`, and every edge from `a` to `S`, but no edge from `a`
to `R`.  There are no other edges.  Equivalently,

\[
 V(G)=\{a\}\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(\{a\},R)=\varnothing.                     \tag{1.3}
\]

Thus `S` is an actual seven-vertex separator and its open shores are
`{a}` and `R`.

### Lemma 1.1

The graph `G` is seven-connected and seven-chromatic.

#### Proof

Delete at most six vertices.  At least one vertex of `S` survives.  Since
`n>=7`, at least one vertex of `R` also survives.  Every surviving vertex
of `R` is adjacent to every surviving vertex of `S`; every surviving
boundary vertex is adjacent to every surviving vertex of `R`; and `a`, if
it survives, is adjacent to every surviving boundary vertex.  The
remaining graph is therefore connected.  Deleting all seven vertices of
`S` separates `a` from `R`, so the connectivity is exactly seven.

The complete join between `S` and `R` forces disjoint colour sets on those
two subgraphs.  Since

\[
                         \chi(G[S])=4,qquad \chi(G[R])=3,
\]

at least seven colours are required.  Seven suffice, and `a` can reuse a
colour used on `R`.  Hence `chi(G)=7`. \(\square\)

## 2. One boundary partition on every critical edge deletion

Fix the following four-block partition of `S`:

\[
 \Sigma=\{k_0,j_0,j_1,j_2\}\mid\{k_1\}\mid\{k_2\}\mid\{k_3\}.
                                                               \tag{2.1}
\]

It is proper on `G[S]`.  Regard its four blocks as colours `0,1,2,3`.

### Theorem 2.1 (fixed-trace edge rotation)

For every cycle edge `e in E(G[R])`,

\[
                         \chi(G-e)=\chi(G/e)=6,          \tag{2.2}
\]

and `G-e` has a six-colouring whose exact equality partition on `S` is
`Sigma`.  In every such colouring the ends of `e` have one common colour.
However, `Sigma` does not extend to a six-colouring of the original closed
shore `G[R union S]`.

For the fixed colouring of `G[\{a\} union S]` obtained by giving `a` a
fifth colour, the induced lists on every vertex of `R` are the same
two-element set.  The entire odd cycle `G[R]` is the unique
vertex-minimal induced subgraph which is not colourable from those lists.
This remains the full fixed-trace critical subgraph regardless of which
cycle edge is deleted to obtain the response.  Thus moving the failed edge
around the cycle preserves the exact response but gives no strict
kernel-order descent.

#### Proof

Deleting one edge from the odd cycle makes it a bipartite path.  Colour
that path with two new colours `4,5`, retain the four colours of (2.1), and
give `a` either colour `4` or `5`.  This six-colours `G-e` and induces
exactly `Sigma` on `S`.  The deleted edge joins the two ends of an
even-length path, so those ends have one common colour.

Contracting a cycle edge turns `R` into an even cycle, which is also
bipartite.  The same four-plus-two palette six-colours `G/e`.  Neither
proper minor is five-colourable: the boundary clique requires four
colours, and the path or even cycle has an edge and is complete to `S`, so
it requires two further colours.  This proves (2.2).

In the original closed shore, `R` is an odd cycle complete to `S`.
Any colouring inducing `Sigma` uses four distinct colours on `S`, none of
which can occur on `R`; the odd cycle needs three further colours.  Hence
`Sigma` has no six-colour extension through that shore.

The fixed colouring of the other closed shore uses four colours on `S`.
Every cycle vertex is adjacent to all of `S`, so its available list is
exactly the remaining two colours.  The odd cycle is not colourable from
those lists, whereas every proper induced subgraph is a disjoint union of
paths and is two-colourable.  This proves the minimal-kernel assertion.
\(\square\)

## 3. Two repeated contacts preserving one spanning model

Choose the nonincident cycle edges

\[
                  e=r_{n-1}r_0,qquad e'=r_3r_4.        \tag{3.1}
\]

Deleting them splits `R` into the two nonempty connected paths

\[
                  D=\{r_0,r_1,r_2,r_3\},qquad
                  U=\{r_4,\ldots,r_{n-1}\}.            \tag{3.2}
\]

Put

\[
                  B=\{a,j_0,j_1,j_2\}.                 \tag{3.3}
\]

### Proposition 3.1 (model-preserving repeated contact)

The seven connected sets

\[
             B,\quad D,\quad U,\quad
             \{k_0\},\{k_1\},\{k_2\},\{k_3\}         \tag{3.4}
\]

partition `V(G)` and are pairwise adjacent.  They are therefore a spanning
labelled `K_7`-minor model.  The two distinct `D`--`U` edges are exactly
`e,e'`; deleting either one leaves the other and preserves the same
spanning model.  Both edge deletions attain the same fixed boundary
partition `Sigma`, but neither produces a smaller fixed-trace critical
subgraph or an extension of `Sigma` through both closed shores.

#### Proof

The set `B` is connected through the star with centre `a`.  The sets
`D,U` are paths.  The four singleton sets are pairwise adjacent.  Every
cycle vertex is adjacent to every vertex of `S`, so `D` and `U` are
adjacent to the four singleton sets and to `B` through the vertices of
`J`.  The vertex `a` supplies all adjacencies from `B` to the four
singletons.  Finally, (3.1) are the two edges between the paths in (3.2).
This proves the model and its persistence after either deletion.  The
remaining assertions are Theorem 2.1. \(\square\)

## 4. Exact consequence

This family has all of the following simultaneously:

1. seven-connectivity and chromatic number seven;
2. an actual order-seven separation with two connected boundary-full open
   shores;
3. one exact boundary partition attained after deleting either of two
   repeated literal model-contact edges;
4. critical-edge Kempe saturation at either deleted edge;
5. a fixed-trace vertex-minimal obstruction which fills the same shore for
   every choice of the failed edge; and
6. no extension of the selected partition through both original closed
   shores.

Therefore fixed-trace attainment, repeated exposure and
model-preserving edge rotation do not by themselves increase a labelled
first-hit rank, shorten the response kernel, or synchronize the two shore
colourings.  The example exits only through its explicit `K_7` model.

It does not satisfy `K_7`-minor exclusion and, because that model contracts
to a proper `K_7` minor, it is not minor-minimal among seven-chromatic
graphs.  These are not incidental omissions: in a genuine hypothetical
counterexample they are the remaining hypotheses which must turn a
repeated exposure into an explicit `K_7` model, a label-preserving split,
or a colour-compatible separator.  Pure fixed-trace list dynamics cannot
do so.

## 5. Verification

The deterministic verifier checks the smallest member `n=7`:

```text
python3 barriers/hc7_fixed_trace_edge_rotation_barrier_verify.py
```

Expected output:

```text
GREEN fixed-trace edge-rotation barrier
G: vertices=15 edges=69 connectivity=7 chromatic_number=7
both edge deletions and contractions: chromatic_number=6, exact Sigma
spanning K7 model survives either repeated D-U contact deletion
fixed-trace critical kernel: entire C7 for every deleted cycle edge
```
