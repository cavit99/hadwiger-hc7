# Repeated contacts and component defect

**Status:** written proof; separate internal audit GREEN in
[`hc7_repeated_contact_component_defect_audit.md`](hc7_repeated_contact_component_defect_audit.md).
This note determines exactly
what two literal edges between the same two selected connected subgraphs can
and cannot do to the component defect.  It is a local consequence of the
audited component-contact defect theorem.  It does not preserve a boundary
colouring and does not prove `HC_7`.

## 1. Setting

Let

\[
                         Q_1,Q_2,Q_3
\]

be pairwise disjoint connected subgraphs which are pairwise adjacent.  Let
the remaining selected connected subgraphs be partitioned into four labelled
families

\[
                  \mathcal L_1,\mathcal L_2,
                  \mathcal L_3,\mathcal L_4.
\]

Every selected subgraph is disjoint from the three `Q_i` and adjacent to
each of them.  Their component-contact graph `J` has one vertex for every
selected subgraph, with an edge exactly when the corresponding host
subgraphs are adjacent.  Put

\[
 \Delta(J)=\sum_{i<j}
   \operatorname{cc}\bigl(J[\mathcal L_i\cup\mathcal L_j]\bigr)
   -|V(J)|-2.                                           \tag{1.1}
\]

Assume that all four families are nonempty, that `J` has no `K_4` minor,
and that `Delta(J)=1`.  The audited component-contact theorem then says that
`J` is a two-tree.

## 2. Literal edge multiplicity is invisible

### Lemma 2.1

Let `L` and `W` be two selected connected subgraphs in different labelled
families.  Replacing one host edge between `L` and `W` by any positive
number of host edges between the same two subgraphs does not change `J` or
`Delta(J)`.

#### Proof

The component-contact graph records the existence of the adjacency
`L`--`W`, not its edge multiplicity.  None of its vertices, bichromatic
components, or edges changes.  Formula (1.1) is therefore unchanged.
\(\square\)

Thus two independent or incident edges between the same two selected
subgraphs do not by themselves lower the component defect.

## 3. Exact effect after separating one endpoint side

The repeated edges become useful only if a legitimate host operation
replaces one selected connected subgraph by two selected connected
subgraphs.

### Theorem 3.1

Let `L` be a vertex of `J` in `mathcal L_1`.  Suppose a legitimate
replacement produces two disjoint eligible connected subgraphs `L_1,L_2`
in the same labelled family, with no edge between them, and introduces no contact with an old
bichromatic component which did not contain `L`.  Let the new
component-contact graph be `J'`.

Suppose that one old selected subgraph `W in mathcal L_2` is adjacent to
both `L_1` and `L_2`.  For `i=2,3,4`, let `kappa_i` be the number of
components which replace the old component containing `L` in the
bichromatic contact graph on `mathcal L_1 union mathcal L_i`.
Then

\[
                 \Delta(J')=\kappa_2+\kappa_3+\kappa_4-3. \tag{3.1}
\]

Consequently:

1. `Delta(J')=0` exactly when

   \[
                          \kappa_2=\kappa_3=\kappa_4=1, \tag{3.2}
   \]

   and in that case the host contains a `K_7` minor;
2. the replacement preserves defect one exactly when

   \[
             \{\kappa_2,\kappa_3,\kappa_4\}=\{1,1,2\}; \tag{3.3}
   \]

3. the two repeated contacts put `L_1,L_2` in one component counted by
   `kappa_2`, but do not imply `kappa_2=1`: components left behind when
   `L` is removed from its old bichromatic component may remain separate.

#### Proof

In the bichromatic graph on the first two labelled families, the two new
vertices lie in one component because they are both adjacent to `W`.
There may nevertheless be further components counted by `kappa_2`: after
the old vertex `L` is deleted, a component of the old bichromatic component
may have no contact with either replacement vertex.  Thus the repeated
edges do not determine `kappa_2`.

With `s=2`, Proposition 4.2 of the component-contact defect theorem gives

\[
 \begin{aligned}
 \Delta(J')-\Delta(J)
   &=\kappa_2+\kappa_3+\kappa_4-2-2\\
   &=\kappa_2+\kappa_3+\kappa_4-4.
 \end{aligned}
\]

Since `Delta(J)=1`, this is (3.1).  All three `kappa_i` are at least one.  Hence
the only way to obtain defect zero is `(1,1,1)`, and the only way to retain
defect one is a permutation of `(1,1,2)`.  In the defect-zero case, the
component-contact theorem gives a `K_4` minor in `J'`.  Replacing its four
quotient branch sets by their represented connected host subgraphs and
adjoining `Q_1,Q_2,Q_3` gives seven disjoint connected pairwise adjacent
branch sets, hence a `K_7` minor. \(\square\)

### Corollary 3.2 (independent and incident repeated edges)

Suppose `e=x_1y_1` and `f=x_2y_2` join `L` to `W`.

* If the edges are independent, a replacement which puts `x_1,x_2` in
  different new subgraphs of `L`, or puts `y_1,y_2` in different new
  subgraphs of `W`, puts those two replacement subgraphs in one component
  of the corresponding bichromatic contact graph.
* If the edges are incident, only the side containing their two distinct
  ends can be separated in this way.  Separating the side containing the
  common end does not turn the two edges into contacts of two different
  selected subgraphs.

This does not by itself make the relevant replacement number one.  It does
so under the additional **full old-contact retention** hypothesis that
every component left after deleting the old selected vertex from its old
bichromatic component has a neighbour in one of the two replacement
subgraphs.  Under that additional hypothesis, the repeated-contact label
has `kappa=1`; Theorem 3.1 then gives a `K_7` minor when the other two
replacement numbers are both one, and preserves defect one exactly when
those other two numbers are one and two in either order.

## 4. The fixed-trace edge deletions do not lower the defect

### Proposition 4.1

Keep the defect-one hypotheses of Section 1.  Let `e,f` be two distinct
host edges between the same selected subgraphs `L,W` in different labelled
families.  Assume deleting either one leaves the selected subgraphs
connected and eligible.

1. The component-contact graph and its defect are unchanged in `G-e` and
   in `G-f`.
2. In the common deletion `G-{e,f}`, the defect remains one if another
   `L`--`W` edge survives.  If no such edge survives, the component-contact
   graph is `J-LW` and its defect is two.

#### Proof

After either single deletion, the companion edge still represents the
same `L`--`W` adjacency, so Lemma 2.1 applies.

For the common deletion, a third edge again leaves `J` unchanged.  Otherwise
the only quotient change is deletion of the edge `LW`.  In a two-tree every
bichromatic induced subgraph is a forest.  Hence `LW` is a bridge of the
bichromatic graph containing it, its deletion increases that pair's
component count by one, and all other terms in (1.1) are unchanged.  The
defect therefore rises from one to two. \(\square\)

Accordingly, none of the three edge-deletion hosts in the fixed-trace
two-edge fork lowers component defect while the old selected subgraphs are
retained.  The fork contributes useful colouring information, but a defect
decrease must come from a new eligible component, a genuine split, or a
different component selection.  Contracting one of the edges merges two
different labels and is not itself an operation within the same
four-labelled component-contact graph.

## 5. Exact trust boundary

The theorem assumes that the two replacement subgraphs are already valid
members of the same component selection: they retain all three anchor
contacts and whatever valid-cut property is required in the colour-matched
path application.  It does not prove that deleting or contracting either
repeated edge creates such a replacement.  It also does not infer a common
boundary colouring, identify palette colours with the four labels, or use
the fixed-trace two-edge alternatives.

The result isolates the missing dynamic assertion.  A proper-minor response
must do more than preserve two literal edges: it must control every fragment
left in the three old bichromatic components, not merely connect the two new
endpoint pieces.  It must force all three replacement numbers to one, or
else turn the unique value two in the defect-preserving pattern (3.3) into
an order-seven colour-compatible separation.

## 6. Dependency

- [component-contact defect and two-tree equality](../results/hc7_component_contact_defect_theorem.md)
