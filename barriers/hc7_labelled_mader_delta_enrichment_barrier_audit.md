# Independent audit of the labelled Mader delta-matroid enrichment barrier

**Audited file:** `hc7_labelled_mader_delta_enrichment_barrier.md`
**Audited SHA-256:**
`27bc1eea766fcbe91f5c6e44016296d0f0f6d2c601cbb2cafae443209455fd2c`
**Verdict:** **GREEN** — the stated counterexamples and persistence claims
are correct at this revision.

The independently audited mathematical revision had SHA-256
`11d385911c1610c066258eaa65aa2609fe387167cbb76244cab9d47732252b27`.
The current revision differs only in its opening status paragraph, which
now records this GREEN audit; no proposition or proof step changed.

## Scope of the verdict

The note proves a limitation of endpoint-only Mader delta-matroid methods
and of the explicitly defined static enrichments.  It does not refute a
witness-coupled representation, an exchange theorem using the host graph,
or any statement under all the hypotheses of a minimal counterexample to
`HC_7`.  Those exclusions are stated correctly in the audited note.

## Independent reconstruction of the common representation

The only implicit algebraic step in Proposition 2.1 is valid.  Over the
rational-function field in nonzero indeterminates `alpha,beta`, order the
relevant ground elements as

\[
                    x,y,z,b_1,b_2
\]

and use the skew-symmetric matrix

\[
M=\begin{pmatrix}
0&0&0&1&0\\
0&0&0&0&1\\
0&0&0&\alpha&\beta\\
-1&0&-\alpha&0&0\\
0&-1&-\beta&0&0
\end{pmatrix}.
\]

The four vertices of `Q` may be added as zero rows and columns: they are
loops of the endpoint delta-matroid because every route from one of them to
`B` passes through another terminal.

The restriction omitting `z` has exactly the nonempty feasible sets

\[
 \{x,b_1\},\quad \{y,b_2\},\quad \{x,y,b_1,b_2\},
\]

which are precisely the endpoint sets in the split network.  The
restriction omitting `x,y` has the nonempty feasible sets

\[
                    \{z,b_1\},\quad \{z,b_2\},
\]

which are precisely the endpoint sets after contracting `xy`.  Relevant
principal determinants are

\[
\det M[\{x,y,b_1,b_2\}]=1,
\quad
\det M[\{z,b_1\}]=\alpha^2,
\quad
\det M[\{y,z,b_1,b_2\}]=\alpha^2,
\]

whereas the determinants for `\{y,b_1\}` and `\{b_1,b_2\}` vanish.
Thus the asserted mixed feasible set exists, and it lies in neither legal
graph restriction.  This also independently verifies every row of (2.6).

## Graph-theoretic checks

1. The four singleton sets `q_1,...,q_4` and the connected set `\{x,y\}`
   form a labelled `K_5`-minor model.  Contracting `xy` gives the claimed
   `K_5` subgraph, while deleting `xy` leaves the replacement path
   `x-u-y`.
2. In the split Mader network the only nonempty Mader paths are the edges
   `xb_1` and `yb_2`.  Every proposed alternative through `u` or `Q`
   either has endpoints in one terminal part or has an internal terminal.
   Hence the path-feasibility calculation used in Proposition 2.1 is
   exhaustive.
3. For the two retained feasible sets `F,C`, their symmetric difference is
   exactly `\{x,y,z,b_2\}`.  At the element `x`, the four candidates in
   (2.6) exhaust the symmetric-exchange axiom; only the mixed, illegal
   candidate is feasible.  Corollary 2.2 follows.
4. Taking three disjoint copies leaves the failed exchange wholly in one
   factor, so Proposition 3.1 is correct.  No connectivity or `HC_7`
   property is claimed for this graph.

## Operations and information-loss checks

- A fixed twist conjugates every exchange candidate by the same symmetric
  difference and therefore preserves the failure.
- In a direct sum with a disjoint auxiliary system, attaching the same
  auxiliary feasible set to both compared sets removes all auxiliary
  elements from their symmetric difference.  The failed exchange is
  unchanged.  A delta-sum on disjoint ground sets has the same setwise
  effect because symmetric difference equals union there.
- Deleting an edge internal to `Q`, or deleting the edges of `x-u-y`, does
  not change any Mader path endpoint set.  It does change the designated
  clique or replacement-path datum.  Hence a construction that is solely a
  function of the endpoint delta-matroid cannot recover that datum.
- On the terminal four-cycle, the full endpoint set is feasible, but no
  two vertex-disjoint paths realize the prescribed opposite pairing.  The
  parity obstruction in Proposition 5.1 is therefore correct.

## Trust boundary

The audit verifies the finite constructions, the common linear
representation, and the operations explicitly named in the theorem.  The
phrase “auxiliary systems that do not themselves contain the missing host
information” must retain its stated static meaning: an auxiliary object
chosen from additional host data, or a multimatroid/polynomial whose
feasibility couples endpoint choices to actual path witnesses, is outside
the counterexample.  Likewise, the audit makes no novelty claim relative
to the cited delta-matroid literature.
