# Independent audit of repeated contacts and component defect

**Verdict:** **GREEN** at the exact source revision recorded below.  The
split formula now counts residual fragments in all three affected
bichromatic contact graphs.  Repeated literal contacts connect the two new
pieces but are correctly no longer claimed to eliminate orphan fragments.

This is a separate internal mathematical audit, not external peer review.

## Audited revision

```text
1e1e67661628b700997ad3c0a847260a7ad213840d32587cebfc98a519ccd9f4  results/hc7_repeated_contact_component_defect.md
```

The only change from the audited `88d82551...` revision is the source's
status line and link to this audit; no mathematical content changed.

The previous draft failed audit because a common neighbour of the two
replacement vertices need not connect every component left after deleting
the old quotient vertex.  The audited revision repairs that issue by
retaining the full replacement number `kappa_2`.

## 1. Multiplicity and the defect-one starting point

Under the hypotheses of Section 1, the audited component-contact theorem
applies: four nonempty parts, `K_4`-minor exclusion and defect one make `J`
a two-tree.  The defect depends only on the simple component-contact graph.
Changing the positive number of host edges witnessing one fixed quotient
adjacency changes neither a quotient vertex nor any bichromatic component,
so Lemma 2.1 is correct.

## 2. Exact split formula

Replacing one selected quotient vertex by two nonadjacent vertices raises
the total selected-vertex count by one.  For each of the three other parts,
the old bichromatic component containing the replaced vertex is replaced by
`kappa_i` components, so its component count changes by `kappa_i-1`.
Consequently

\[
\begin{aligned}
 \Delta(J')-\Delta(J)
   &=\sum_{i=2}^4(\kappa_i-1)-1\\
   &=\kappa_2+\kappa_3+\kappa_4-4.
\end{aligned}
\]

Since `Delta(J)=1`, this gives exactly

\[
              \Delta(J')=\kappa_2+\kappa_3+\kappa_4-3.
\]

Every replacement number is at least one.  Thus the new defect is zero
exactly for `(1,1,1)`, and is one exactly when the multiset is
`{1,1,2}`.  In the zero case the promoted component-contact theorem gives a
`K_4` minor in `J'`; lifting its four branch sets and adjoining the three
anchors gives the asserted explicit `K_7`-minor model in the host.

The common old neighbour `W` places the two new vertices in one of the
components counted by `kappa_2`.  It does not imply `kappa_2=1`, because
other fragments of the old component may have lost their only contact with
the replaced vertex.  This is now stated explicitly and matches the exact
formula.

## 3. Independent and incident repeated edges

For independent edges, separating their two ends on either endpoint side
gives two new subgraphs each adjacent to the unchanged opposite selected
subgraph.  They therefore lie in one new bichromatic component.  For
incident edges, only the side containing the two distinct ends can be split
this way; the common end cannot belong to two disjoint replacement
subgraphs.

The additional full old-contact retention condition in Corollary 3.2 is
exactly sufficient for replacement number one.  Every residual component
then attaches to one of the replacement vertices, while the replacement
vertices are connected through their common neighbour.  The corollary does
not claim that repeated contacts alone supply this retention.

## 4. Single and common edge deletions

After either one of two repeated host edges is deleted, the other still
witnesses the same quotient adjacency.  The contact graph and defect remain
unchanged.  After deleting both, a third edge again leaves them unchanged.
If no third edge survives, the quotient operation is exactly deletion of
the one edge `LW`.

Every bichromatic induced subgraph of the defect-one two-tree is a forest.
Thus `LW` is a bridge in its bichromatic forest, and deleting it increases
exactly one pairwise component count by one.  The defect rises from one to
two.  Proposition 4.1 and its conclusion that none of these edge-deletion
hosts lowers the old defect are therefore correct.

## 5. Trust boundary

The theorem starts only after a valid host operation has produced two
eligible connected replacement subgraphs retaining the three anchor
contacts and the application-specific cut data.  It does not produce that
split, preserve a selected boundary colouring, identify colours with
labels, or turn the unique replacement number two into a compatible
order-seven separation.  Those obligations are accurately retained as the
dynamic frontier.

No unresolved gap remains in the stated local defect calculus.
