# Audit: degree-free hub core and row-five path absorption

## Verdict

**GREEN** for Theorem 0.1 of
`hadwiger_degree9_hub_rainbow_rooted_k4.md` and Theorem 2.1 of
`hadwiger_degree9_row5_two_path_exchange.md`.

The degree-free theorem depends on the proved four-color case of Holroyd's
Strong Hadwiger Conjecture.  The row-five theorem depends on the previously
audited interface-capacity linkage and the 87-state two-six-contact packing
certificate.  Subject to those stated inputs, all contractions, expansions,
cuts, and model lifts are valid.

## 1. Degree-free hub theorem

The simultaneous stars are disjoint and connected, and their contraction
images are adjacent through \(vh\), so their colors \(\alpha,\beta\) are
different.  Deleting the centers before expansion restores only the two
independent leaf sets.  Every external edge was represented at a contracted
image, so the expansion colors \(G-\{v,h\}\) properly.

The degree-seven center has only two neighbors besides \(h\) and the four
common leaves.  Its residual list therefore has order at least two in every
six-coloring of the simultaneous contraction.  If the hub residual list
were nonempty, the two lists would have distinct representatives.  Hence
all six colors occur on \(W\cup E\), and all four colors outside
\(\{\alpha,\beta\}\) occur on \(E\).  This proves \(|E|\ge4\).

Let \(J\) be the union of those four color classes and
\(X=E\cap V(J)\).  If a four-coloring of \(J\) omitted one of its four
colors on \(X\), combining it with the untouched \(\alpha,\beta\) classes
would give another six-coloring of the contraction in which that color is
absent from \(E\).  Reapplying the preceding residual-list argument to this
new coloring gives the contradiction.  Thus \(X\) is four-saturating.

This last sentence is the only wording clarification needed in the source:
the proof should say explicitly that the residual-list conclusion holds for
**every** coloring of the contraction.  It should not be read as claiming
that equation (0.1) for one fixed coloring is itself invariant under
recoloring.

Strong HC4 gives an \(X\)-rooted \(K_4\)-model in \(J\).  The two
contracted images have colors \(\alpha,\beta\), so the model avoids both.
It therefore lifts without expanding either star, lies in
\(G-(\{v,h\}\cup W)\), and every bag meets a root in \(E\subseteq N(h)\).
Adding \(\{h\}\) gives the claimed \(K_5\)-model.

## 2. Row-five path absorption

The interface-capacity theorem supplies two vertex-disjoint paths
\(L_1,L_2\), one from each missing label \(d_1,d_2\), with distinct
terminal vertices in \(N_Q(P)\).  After deleting \(d_h\), the remainder
\(W_h\) of one path is connected.  Its terminal has an edge to \(P\), so
\(A_h=P\cup W_h\) is connected and contacts the original five-row set
together with \(d_h\).

The other path is disjoint, so it lies in a unique component \(K_k\) of
\(Q-W_h\).  This component contacts \(d_k\), and its terminal has an edge
to \(P\subseteq A_h\).

If \(K_k\) has at least six boundary contacts, \(A_h,K_k\) each have six
contacts and their rows cover the exact seven-set \(F\).  The audited
four-piece packing lemma therefore yields the \(N\)-meeting \(K_6\).

Otherwise every neighbor of \(K_k\) lies in

\[
 N_F(K_k)\cup N_{A_h}(K_k).
\]

Distinct components of \(Q-W_h\) are anticomplete; the original shore is
an exact component with external neighborhood \(F\); and \(P\cup W_h\)
contains every remaining internal neighbor.  Thus the displayed set is
exactly \(N_G(K_k)\), not merely a superset.  It is a genuine separator,
with the other exterior components and \(v\) on the far side.
Seven-connectivity gives order at least seven.  Equality is the stated
exact cut; strict inequality gives

\[
 |N_{A_h}(K_k)|\ge 8-|N_F(K_k)|,
\]

including three attachments in the row-five case.

The counterarchitecture verifier was run successfully and reports:

```text
two_label_paths=True distinct_interface_vertices=True
treewidth_at_most=4 hence_no_K6_minor=True
```

It correctly demonstrates that the two-path linkage alone is insufficient;
ambient connectivity after absorption is the new input.

## 3. Additional hub-lock extension

The newly appended Lemma 4.3, Corollary 4.4, Lemma 5.1, and Theorem 5.2 in
`hadwiger_degree9_hub_portal_lock.md` are also **GREEN**.

* The alternate seven bags in Lemma 4.3 are connected and disjoint.  The
  vertex \(6\) supplies both singleton contacts for \(D\cup R_0\), while
  the assumed \(U-R_5\) edge, \(UD\), and old rooted-model contacts supply
  every remaining adjacency.
* In Corollary 4.4, every component of \(L_6-6\) has an edge to \(6\), so
  the complement of the root component is connected and adjacent to it.
* Seven-connectivity makes the graph left after deleting the six displayed
  vertices connected.  Hence every component outside the rooted model can
  be absorbed into one neighboring bag, proving the spanning assertion.
* In Theorem 5.2, spanning and the component definition give the exact
  neighborhood containment.  The vertex \(v\) is not adjacent to the root
  component, so it remains on the far side and the neighborhood is a real
  separator.  If the protected portal set has order one, its union with the
  six displayed vertices has order seven; seven-connectivity forces equality
  and hence an exact seven-cut.  Otherwise there are at least two protected
  portals, exactly as claimed.
