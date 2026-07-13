# Barrier: connectivity and Dirac do not force the bipartition carriers

## Status

**Verified counterexample to the proposed auxiliary lemma.**  This is not a
counterexample to `HC_7`: the graph below deliberately contains a `K_7` and
is not contraction-critical.  It proves that seven-connectivity, the exact
packet vector `(1,2)`, a bipartite boundary, and even all literal Dirac
neighbourhood inequalities do **not** by themselves force the two thin-shore
bipartition carriers.

The missing input must use `K_7`-minor-freeness or genuine proper-minor state
transitions, rather than another consequence of connectivity or the static
Dirac inequality.

## 1. Construction

Let the literal boundary be

\[
 S=\{s_0,\ldots,s_6\},\qquad G[S]=s_0s_1\cdots s_6=P_7,
\]

with natural bipartition

\[
 I=\{s_0,s_2,s_4,s_6\},\qquad J=\{s_1,s_3,s_5\}.
\]

The thin open shore `L` is the icosahedral graph with one vertex deleted.
Its five former neighbours occur in cyclic order on the boundary of the
new outer face.  Every vertex of `L` contacts `s_0,s_1,s_2`.  Four
successive outer-face vertices receive, in cyclic order, one additional
contact to

\[
                         s_4,s_3,s_6,s_5.                 \tag{1.1}
\]

No other thin-shore contacts are present.

The rich open shore is a `K_6` on vertices `r_0,...,r_5`.  Vertices
`r_0,r_1` contact every member of `S`; each other `r_i` contacts
`S-\{s_0\}`.  There are no edges between the open shores.

## 2. Exact verified properties

The deterministic verifier checks:

1. `G` is seven-connected;
2. the thin and rich packet numbers are exactly `1` and `2`;
3. for every literal vertex `x` of `G`,

   \[
              \alpha(G[N(x)])\le d_G(x)-5,               \tag{2.1}
   \]

   which is precisely Dirac's neighbourhood inequality at parameter seven;
4. no two disjoint connected subgraphs of `L` contact `I` and `J`,
   respectively.

The last assertion also has a direct proof.  Since only the first and third
special outer vertices contact `s_4,s_6`, every `I`-carrier contains those
two vertices.  Every `J`-carrier contains the alternating second and fourth
vertices, the unique portals for `s_3,s_5`.  A path in each carrier would
therefore give two vertex-disjoint paths joining alternating vertices on the
boundary of a planar disc, contrary to the Jordan curve theorem.

The common contacts `s_0,s_1,s_2` do not alter this crossing obstruction.
They make the rooted cut inequalities strong: the punctured icosahedron is
four-connected, and every thin vertex has at least three boundary contacts.

## 3. Trust boundary

The graph is intentionally outside the hypothetical-counterexample class.
Indeed the rich `K_6` together with (for example) `s_1` is a literal `K_7`.
Thus this barrier does not refute a theorem which retains
`K_7`-minor-freeness and strong contraction-criticality.

What it refutes is the tempting proof step

\[
 \text{seven-connectivity + packet }(1,2)+\text{Dirac}
 \Longrightarrow \text{two thin bipartition carriers}.  \tag{3.1}
\]

The negative certificate is exactly a planar crossed-frame web.  Any proof
of the bipartite boundary cell must therefore show that this web is
incompatible with proper-minor colouring transitions or else convert it,
using `K_7`-minor-freeness, into a safe equality state.

## 4. Reproduction

Run

```text
active/runtime/venv/bin/python \
  barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier_verify.py
```

The expected output begins

```text
VERIFIED
vertices 24 edges 121
node_connectivity 7
packet_vector (1, 2)
```

