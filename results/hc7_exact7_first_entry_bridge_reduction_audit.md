# Independent audit: exact-seven first-entry bridge reduction

**Verdict:** **GREEN under the exact stated hypotheses.**  The prefix
component is literal, its full neighbourhood is computed correctly, the
support-at-least-five branch is exactly within the audited defect-two
carrier theorem, and seven-connectivity gives three distinct packet
attachments in the survivor.

**Audited source:**
`results/hc7_exact7_first_entry_bridge_reduction.md`.

**Source SHA-256:**
`edb821588975da2590d0f355d17ddbc16c2bf00abc12d8565c62176da4fcc540`.

This differs from the line-by-line audited revision
`718735c0625b18940c3a87f360c170d9018206fa4d64633ca0a7dd2caf65fe16`
only by correction of a repository-relative dependency link after the
dependency was promoted from `active/` to `results/`; the theorem statement
and proof are unchanged.

## 1. Hypotheses used

The proof assumes an actual order-seven separation in a seven-connected,
strongly seven-contraction-critical, `K_7`-minor-free graph; a boundary
graph belonging to the ten hard orbits in the defect-two carrier theorem;
two disjoint `S`-full connected subgraphs on one open side; and an
`r-z` path whose internal vertices lie on that side and which meets their
union.

The opposite open side need not be connected.  The source correctly
derives an `S`-full connected component there: the neighbourhood of any
component is contained in the seven-set `S`, and the other open side makes
the cut genuine, so seven-connectivity forces equality.

## 2. Prefix component and neighbourhood

In the non-direct case, the internal vertices before the first hit form a
nonempty connected path segment in
`R-(P_1 union P_2)`.  They therefore lie in one component `K` of that
graph.  The first path edge gives `r in N_S(K)`, while the last pre-entry
edge gives an attachment to the selected union.

Because there is no edge between the open shores and `K` is a component
after deleting precisely the two selected subgraphs, every neighbour of
`K` lies either in `S` or at a distinct attachment vertex of
`P_1 union P_2`.  Conversely every vertex counted in those two sets is a
neighbour.  Thus the displayed equality

\[
 N_G(K)=T_K\mathbin{\dot\cup}A_K
\]

is exact, not merely an upper bound.

## 3. The two numerical branches

If `|T_K|>=5`, the connected set `K` is a third carrier of boundary defect
at most two, disjoint from the two full carriers.  Theorem 2.2 of the
audited connected-rich carrier exchange applies because the source also
has the required opposite full component and one of the ten hard boundary
graphs.  Its adaptive quantifier order chooses the independent contraction
block before the returned state and reflects every returned state.  This
gives the claimed six-colouring outcome.

Otherwise `|T_K|<=4`.  The exact neighbourhood separates `K` from the
nonempty opposite shore.  Seven-connectivity gives

\[
 |T_K|+|A_K|\ge7,
\]

and hence `|A_K|>=3`.  These are three distinct literal attachment
vertices, not three paths or three boundary labels.

## 4. Trust boundary

The theorem does not handle a direct first entry.  In the surviving
non-direct case it does not distribute the three attachments between the
two selected subgraphs, reroute either subgraph, preserve a pre-existing
minor model, or return a common boundary partition.  Lexicographic
minimality supplies none of those statements.  The GREEN verdict therefore
certifies the reduction to a support-at-most-four three-attachment bridge,
not closure of that bridge or `HC_7`.
