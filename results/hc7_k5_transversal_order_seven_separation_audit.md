# Audit of the two-vertex-transversal separation theorem

**Audit verdict:** GREEN.

**Audited source:** `hc7_k5_transversal_order_seven_separation.md`

**Audited SHA-256:**
`2aa8024d6b0d1b6a6b0c8a22e5ef1e7183ffdab29157f442dbe8844dacb4a038`

**Audit scope:** independent line-by-line check of the equivalence in the
hypothesis, the small-order cases, the connectivity conventions, the use of
Wagner's characterization, the planar-degree contradiction, and the final
construction of an actual order-seven separation.  The source was not edited
during this audit.

The exact promoted revision was rechecked on 2026-07-16 after its status
header was updated.  The theorem and proof remain exactly within the scope
of the audit below.

## Interpretation fixed by the statement

The phrase *two-vertex transversal* and the notation `P={p,q}` are read as
asserting that `p` and `q` are distinct, so `|P|=2`.  This is the interpretation
used in the proof's order calculations.  Connectivity is the standard vertex
connectivity convention: a `k`-connected graph has more than `k` vertices and
has no vertex cut of order less than `k`.

## Detailed check

1. **Transversal equivalence.** A `K_5`-minor model whose vertex-union avoids
   `P` is exactly a `K_5`-minor model in the induced subgraph `G-P`.  Thus “`P`
   meets the vertex-union of every model” is equivalent to “`G-P` has no
   `K_5` minor.”  No branch-set information is lost in either direction.

2. **Connectivity after deleting `P`.** Put `H=G-P`.  If deleting at most four
   vertices `X` disconnects `H`, then deleting `X\cup P` disconnects `G`, and
   `|X\cup P|\le6`.  This contradicts seven-connectivity.  Also
   `|V(G)|\ge8`, hence `|V(H)|\ge6`; these facts establish five-connectivity
   under the convention above.

3. **The six-vertex edge case.** If `|V(H)|=6`, five-connectivity forces every
   vertex to have degree five, so `H=K_6`.  That graph contains `K_5` as a
   subgraph and hence as a minor.  Therefore the hypothesis forces
   `|V(H)|\ge7`.  This also ensures that six-connectivity is a meaningful
   possibility in the following contradiction.

4. **Wagner consequence.** The cited modern formulation is exact: Theorem 1.2
   of Norin's survey states that the `K_5`-minor-free graphs are precisely the
   graphs obtained from planar graphs and `V_8` by `0`-, `1`-, `2`-, and
   `3`-clique-sums.  A nontrivial such sum exposes a vertex separator of order
   at most three.  Hence a four-connected graph in this class cannot have a
   nontrivial final sum.  Its remaining basic piece is planar or is `V_8`;
   the latter is only three-connected.  Consequently every four-connected
   `K_5`-minor-free graph is planar, exactly as used.  The theorem number,
   chapter DOI, original Wagner bibliographic data, and the statement quoted
   in the source all agree with the publisher's record.

5. **Excluding six-connectivity.** If `H` were six-connected, then it would be
   four-connected and therefore planar by the preceding consequence.  It
   would also satisfy `\delta(H)\ge6`.  For a finite simple planar graph on
   at least three vertices, `|E(H)|\le3|V(H)|-6`, so its average degree is
   strictly less than six and some vertex has degree at most five.  This is a
   valid contradiction.

6. **Existence of an exact five-cut.** The already proved facts say that `H`
   is five-connected, has at least seven vertices, and is not six-connected.
   Thus a vertex cut of order at most five exists, while none of order at most
   four exists.  Hence there is a cut `X` with `|X|=5`.  (The `K_5`-minor-free
   hypothesis also rules out a complete graph of the relevant order, so no
   complete-graph convention creates an exception.)

7. **Lifting the cut.** If `C` is one component of `H-X` and `D` is the union
   of the other components, then both are nonempty and no edge joins `C` to
   `D`.  With

   \[
      A=C\cup X\cup P,
      \qquad B=D\cup X\cup P,
   \]

   one has `A\cup B=V(G)`, no edge between `A-B=C` and `B-A=D`, and both open
   sides nonempty.  Moreover `A\cap B=X\cup P`; since `X\subseteq V(H)` is
   disjoint from `P`, its order is `5+2=7`, and it contains `P`.  This is an
   actual separation in the stated sense.

## Dependency and scope assessment

The result uses one established structural input, the four-connected
consequence of Wagner's `K_5`-minor-free decomposition.  All remaining steps
are elementary.  It converts the existence of a two-vertex transversal into
an order-seven separation, but it does **not** select a side, preserve an
attained boundary colouring, preserve labels of a pre-existing minor model,
or make either open side connected.  No stronger conclusion was used or
verified.
