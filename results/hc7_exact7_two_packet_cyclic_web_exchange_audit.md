# Independent hostile audit: two-packet cyclic-web exchange

Audited files:

* `hc7_exact7_two_packet_cyclic_web_exchange.md`;
* `hc7_exact7_two_packet_cyclic_web_exchange_verify.py`.

## Verdict

**GREEN after two scope corrections and one labelled-adjacency correction.**
The final theorem is a valid state-specific infinite-family closure.  It
does not close the homologous matching cylinder, the two-component rural-web
outcome, or the general exact-seven `(1,2)` cell.

The corrections made during audit were material:

1. a transverse path supplies only two of the three representative
   adjacencies, so Theorem 2.1 now names the required literal block edge for
   each offset;
2. the three-attachment proof in Corollary 3.2 is now direct and no longer
   invokes a theorem whose audit is restricted to the ten hard boundary
   orbits; and
3. the two-component cutvertex conclusion is now proved directly in the
   paired-triangle state instead of citing that same restricted theorem.

## 1. The five transverse offsets

After rotating the first endpoint to `p_0`, the five displayed rows are
literal, pairwise vertex-disjoint carrier triples.  They fund

\[
 B_0=\{s_0,s_3\},\qquad B_1=\{s_1,s_4\},\qquad
 B_2=\{s_2,s_5\}.
\]

For offsets `1,2,3,4,5`, the carrier adjacency pairs supplied by cycle
edges are respectively

\[
 \{02,12\},\quad \{01,02\},\quad \{01,02\},\quad
 \{01,02\},\quad \{01,12\}.
\]

Thus the missing representative edges are exactly

\[
 M_1=01,\qquad M_2=M_3=M_4=12,\qquad M_5=02,
\]

as stated.  Rotation merely relabels the three antipodal blocks.  The five
rows explicitly include both orientations, so no unrecorded reversal
assumption remains.

If a cycle gap used for a geometric adjacency is subdivided, its open
subpath can be split across one chosen edge and appended to the carriers at
its two ends.  The two required gaps in every row are distinct.  Hence both
carrier adjacencies survive arbitrary subdivisions as literal edges between
disjoint connected branch sets; they are not quotient edges.

## 2. Exact contraction and colour gluing

Each carrier `X_r` meets portals for both literals in `B_r`, so
`X_r union B_r` is connected.  The carriers and boundary blocks are
pairwise disjoint.  The two geometric adjacencies plus the named literal
block edge make the three representatives pairwise adjacent.  Since `c`
has a boundary neighbour in every `B_r`, all three also see `{c}`.

Contracting the three representatives is a proper minor: each contains
rich-shore vertices and the nonempty thin shore is untouched.  In a
six-colouring of that minor, pulling back only on the untouched thin closed
shore gives precisely the four equality blocks of `Pi`; the representative
clique prevents any two blocks from sharing a colour.  The original
thin-shore operation gives the same exact partition on the rich closed
shore.  A bijection between the four used boundary colours extends to a
permutation of the six-colour palette, and the two colourings glue because
the open shores are anticomplete.

No palette colour is silently identified with a packet or literal label.

## 3. Cross-packet components and portal purity

For Corollary 3.1, if a connected subgraph has attachments on both cycles
and at least three distinct selected attachments, some cross-side pair has
different literal indices.  A shortest path through the subgraph between
such attachments is clean and transverse.  Pairwise block adjacency makes
the offset-specific hypothesis of Theorem 2.1 automatic.

For Corollary 3.2, let `K` be a component outside the two cycles.  If it had
at most two cycle-attachment vertices, then

\[
 N_G(K)\subseteq S\cup A_K.
\]

The nonempty thin shore makes this a genuine cut, so seven-connectivity
gives `|N_S(K)| >= 5`.  At most two of the six `s_i` are missed; therefore
one of the three disjoint pairs `B_r` is wholly contacted.  Funding that
block with `K` and the other two with the full cycles produces the exact
representative clique and reflects `Pi`.  Thus every such component has at
least three attachments.  Portal purity then makes every component meeting
both cycles subject to Corollary 3.1.  If all complementary components are
one-sided, connectedness of `R` forces a direct cycle edge; every surviving
direct edge is homologous by Theorem 2.1.

The argument genuinely uses the stated portal-pure hypotheses.  It makes no
claim for a component attached at unselected cycle vertices or for a direct
cycle edge with an unselected endpoint.

## 4. The two-component branch

The note correctly does not route through `S` when the cycles lie in
different rich components.  Under pairwise block adjacency, two disjoint
duty carriers in one component and the other full component give the three
representatives directly.

The cutvertex conclusion is also state-specific.  If a rich component `K`
has cutvertex `w`, choosing a lobe `D` gives adjacent connected carriers
`X=D` and `Y=K-D`.  Seven-connectivity gives each at least six boundary
contacts.  Each therefore forbids at most one of the three disjoint blocks,
so two distinct allowed blocks can be assigned to `X,Y`; the other full
rich component funds the third.  This proves cutvertex-freeness here without
using the hard-orbit finite theorem.  It does not prove two-connectivity or
link the two rich components internally.

## 5. Finite verifier and sharpness boundary

A fresh run of

```text
python3 results/hc7_exact7_two_packet_cyclic_web_exchange_verify.py
```

terminates with

```text
CERTIFIED transverse carrier core and homologous-cylinder barrier
```

The verifier exhausts all connected vertex subsets of the two unsubdivided
six-cycles.  It checks every cross-edge offset, the two required geometric
adjacencies for each normalized row, and every subset of the six homologous
rungs.  No homologous-rung subset admits three disjoint duty carriers.

That last result is sharpness only for the static carrier core.  The
homologous cylinder is not asserted to be a contraction-critical graph, an
HC7 counterexample, or immune to a separate state-transition argument.
