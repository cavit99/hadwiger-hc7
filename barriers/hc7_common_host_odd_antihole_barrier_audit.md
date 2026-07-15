# Audit: common-host odd-antihole barrier

**Verdict:** GREEN.  The construction and all uniform claims for
\(q\ge3\) are valid.  The deterministic \(q=6\) probe reproduces every
advertised colouring, connectivity, model, contraction, and transversal
certificate.  The family is a mechanism barrier only: it is excluded both
by \(K_7\)-minor-freeness and by strong contraction-criticality.

**Audited sources and SHA-256 hashes:**

* `barriers/hc7_common_host_odd_antihole_barrier.md` —
  `7765c3eefb01970b4a1b7e1e88913d874d622225410fe1be0067ebcf2a3a775c`;
* `active/hc7_common_host_odd_antihole_probe.py` —
  `bcd42e63f10fb310e9090016baa2a43df200a6ce97f4e52e76beae26d0f1e3a1`.

**Probe replay:** `python3 active/hc7_common_host_odd_antihole_probe.py`
completed successfully and printed its GREEN certificate.

## 1. Uniform graph and chromatic number

In \(G_q=\overline{C_{2q+1}}\), an independent set is a clique of the
cycle, hence has order at most two.  Therefore

\[
                   \chi(G_q)\ge
                   \left\lceil\frac{2q+1}{2}\right\rceil=q+1.
\]

Pairing consecutive cycle vertices and leaving one singleton gives the
matching upper bound.  Deleting any vertex leaves
\(\overline{P_{2q}}\), whose independence number is two and whose path
vertices pair into \(q\) independent pairs.  Thus every vertex deletion
has chromatic number \(q\), and `G_q` is \((q+1)\)-vertex-critical.

The named pairs

\[
                         e=1(2q),
\qquad                    f=0(2q-1)
\]

are four distinct vertices and are edges of the complement, while
`01`, `0(2q)`, and `(2q-1)(2q)` are cycle edges and hence cross-nonedges.

Deleting `e` makes \(\{2q,0,1\}\) independent and deleting `f` makes
\(\{2q-1,2q,0\}\) independent.  The displayed pair partitions cover all
remaining vertices and are valid \(q\)-colourings of `G_q-e` and `G_q-f`,
and hence of `H_q`.

The nonedge graph of `H_q` is the cycle plus the two named chords.  A
triangle must use one chord.  The endpoints of `e` have only `0` as a
common neighbour there; the endpoints of `f` have only `2q` as a common
neighbour.  Consequently its only triangles are

\[
                         T_e=\{2q,0,1\},
\qquad                    T_f=\{2q-1,2q,0\}.
\]

These are exactly the independent triples of `H_q`, and they intersect.
A \((q-1)\)-colouring of \(2q+1\) vertices with classes of order at most
three would need at least three size-three classes: with at most two, it
covers at most \(2(q-1)+2=2q\) vertices.  Three disjoint independent
triples do not exist.  Hence \(\chi(H_q)=q\).  Since each one-edge
restoration contains `H_q` and has the displayed \(q\)-colouring,

\[
              \chi(H_q)=\chi(H_q+e)=\chi(H_q+f)=q.
\]

The universal opposite response signatures follow immediately.  In any
\(q\)-colouring of `H_q+e=G_q-f`, edge `e` is proper; if `f` were also
proper, the colouring would extend to `G_q`, contradicting
\(\chi(G_q)=q+1\).  The symmetric statement holds for `H_q+f`.

## 2. Equal/equal state and double contraction

Suppose a \(q\)-colouring of `H_q` made both named pairs equal.  The two
pair classes cannot coincide because that would be an independent set of
order four, while \(\alpha(H_q)=3\).  The `e`-class cannot add its only
possible third vertex `0`, because `0` is already in the distinct
`f`-class.  Symmetrically, the `f`-class cannot add its only possible third
vertex `2q`.  Both classes therefore have order exactly two.

Removing their four vertices leaves \(2q-3\) vertices and \(q-2\) colours.
Neither of the only independent triples survives, so each remaining class
has order at most two and the colours cover at most \(2q-4\) vertices.
This contradiction proves absence of the equal/equal state.

For two vertex-disjoint edges, the following equivalence is exact:

\[
G_q/e/f\text{ is }q\text{-colourable}
\quad\Longleftrightarrow\quad
H_q\text{ has a }q\text{-colouring equal on both pairs}.
\]

Expansion from the contracted graph is proper because every edge of
`H_q` maps to an edge between distinct contraction classes.  Conversely,
identifying each equal-coloured pair preserves properness: every neighbour
of either endpoint already avoids the common colour; a common neighbour
still has a different colour after parallel edges merge, and loops from
the contracted named edges are discarded.  Cross-edges between the pairs
ensure the two contracted images receive different colours whenever such
an equal/equal colouring exists.

Therefore the absent equal/equal state is equivalent to
\(G_q/e/f\) not being \(q\)-colourable.  This is the precise point at
which the family violates strong contraction-criticality.

## 3. Connectivity and uniform models

Every vertex of `G_q` has degree \(2q-2\), so
\(\kappa(G_q)\le2q-2\).  After deleting at most \(2q-3\) vertices, at
least four remain.  If the induced complement were disconnected with
nonempty sides `A,B`, every `A-B` pair would be a cycle edge.  Cycle degree
two forces \(|A|,|B|\le2\); four remaining vertices would then force a
\(K_{2,2}\) subgraph of a cycle of order at least seven, impossible.
Thus \(\kappa(G_q)=2q-2\).

The spanning \(K_q\) model is valid.  The \(q-1\) even singletons
`2,4,...,2q-2` form a clique.  In the remaining bag, vertex `3` is adjacent
to every other member even after the two named deletions, so the bag is
connected; its vertex `0` contacts every singleton.

For the \(K_{q+1}\) model in `H_q`, the \(q\) even singletons
`0,2,...,2q-2` form a clique.  The remaining bag
`{1,3,...,2q-1,2q}` is connected through vertex `3`.  It contacts singleton
`0` through `3`, and its vertex `2q` contacts every other even singleton.
Neither deleted edge is needed.  Hence `H_q` already contains the target
\(K_{q+1}\) minor.

Deleting two cycle vertices leaves one or two paths with \(2q-1\) vertices
in total.  The sum of their independence numbers is at least \(q\), so an
independent set of order \(q\) in the residual cycle becomes a literal
\(K_q\) in `G_q` after the selected vertex pair is deleted.

Finally, `03` is an edge of `G_q`.  The cycle-nonneighbour sets of `0` and
`3` are disjoint, so their contracted image is universal.  The set

\[
                         \{1,4,6,\ldots,2q\}
\]

has order \(q\), contains no consecutive cycle vertices, and is a literal
clique.  Together with the contracted image it gives a literal
\(K_{q+1}\) in `G_q/03`.  Thus `G_q` is vertex-critical but is not strongly
\((q+1)\)-contraction-critical.

## 4. Deterministic \(q=6\) probe

The probe constructs the complement of `C_13` directly and checks:

* both named edges and the three advertised cross-nonedges;
* the two explicit six-colourings;
* non-six-colourability of `G`, exact six-chromaticity of `H`, and the exact
  list of its two independent triples;
* absence of an equal/equal six-colouring of `H`;
* non-six-colourability after the simultaneous named contraction;
* connectivity after every deletion of fewer than ten vertices and an
  explicit ten-vertex cut, hence \(\kappa(G)=10\);
* a literal \(K_6\) after every two-vertex deletion, ruling out every
  two-vertex \(K_5\)-transversal;
* the spanning \(K_6\) model with the four named endpoints in four distinct
  bags;
* the explicit \(K_7\) model already in `H`; and
* the literal \(K_7\) in `G/03`.

The union-find equality constraints and DSATUR search operate on the
correct quotient graphs.  The model checker verifies spanning coverage,
bag disjointness, connectivity, and all inter-bag adjacencies.  Replaying
the unmodified script produced the output below.  One bookkeeping detail:
the script directly checks only the lower statement that `G` is not
six-colourable; its printed equality `chi(G)=7` combines that check with
the explicit seven-colouring proved analytically in Section 1 rather than
validating a seven-colour partition in code.  This does not affect the
certificate, but it is the exact division between computation and proof.

The replay produced:

```text
GREEN common_host_odd_antihole q=6
chi(G)=7; chi(H)=chi(G-e)=chi(G-f)=6
kappa(G)=10; simultaneous_equal_equal=false; chi(G/e/f)>6
spanning_K6_named_rows=4; fixed_pair_K5_transversal=none
K7_model_in_H=true; K7_subgraph_in_G_contract_03=true
```

## 5. Exact barrier scope

The family rigorously shows that the following data, even together, do not
force a simultaneous named double-contraction state, a multiply-hit named
row in every spanning model, or a fixed two-vertex \(K_5\)-transversal:

* connectivity above seven;
* vertex-criticality;
* universal opposite one-edge deletion signatures;
* a connected exactly six-chromatic common host; and
* a spanning common-host \(K_6\) model.

It does **not** refute the desired `HC_7` exchange theorem.  For \(q=6\),
`H` already has a \(K_7\) model, so the literal terminal outcome holds.
The family is also excluded from the minimal-counterexample kernel by both
\(K_7\)-minor-freeness and strong contraction-criticality: the named
double contraction is not six-colourable, and `G/03` supplies a second
failure.

Accordingly the construction refutes attempts to *derive* the named
double-contraction response from high connectivity, vertex-criticality,
the two deletion responses, and one arbitrary spanning model.  It does not
refute arguments that explicitly use the guaranteed named contraction
response, model reselection, carrier-edge contraction responses, or the
literal \(K_7\) alternative.
