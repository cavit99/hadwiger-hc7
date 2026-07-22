# Independent two-defect bags do not force a `K_7` minor

**Status:** explicit computer-assisted barrier to an intermediate
strengthening.  This graph is not a counterexample to `HC_7`.

## 1. The false strengthening

The audited four-bag completion theorem uses one missed set for both bags
on each shore.  The following seemingly useful relaxation is false.

> **Independent-defect four-bag claim (false).**  Let `H` be a graph on an
> eight-set `S` such that
> \[
>  \alpha(H)\le3,
>  \qquad K_4\not\preccurlyeq H-Z
>       \quad\text{for every two-set }Z\subseteq S.
> \]
> Let `u` be complete to `S`.  Suppose there are four pairwise disjoint
> connected sets
> \[
>                 A_E^0,A_E^1,A_F^0,A_F^1
> \]
> outside `S union {u}`, with the two same-shore pairs adjacent.  If each
> set `A_Q^i` is adjacent to all but at most two vertices of `S`, with its
> missed set allowed to depend independently on both `Q` and `i`, then the
> graph contains a `K_7` minor.

The common missed set within each shore cannot be dropped on the strength
of these hypotheses alone.

## 2. A thirteen-vertex counterexample

Put `S={0,1,...,7}` and let

\[
       H=G[S]=K_3[\{0,3,6\}]\mathbin{\dot\cup}
               K_3[\{1,4,7\}]\mathbin{\dot\cup}K_2[\{2,5\}].
\tag{2.1}
\]

Its graph6 code is

```text
GCOcaO
```

Thus `alpha(H)=3`.  Every component of `H` has order at most three, so no
vertex deletion can leave a `K_4` minor; in particular the required
two-vertex-deletion condition holds.

Add five vertices

\[
                    u,e_0,e_1,f_0,f_1.
\]

Join `u` to every vertex of `S`, add only the two same-shore edges
`e_0e_1,f_0f_1` among the four bag vertices, and give the singleton bags
the exact missed sets

\[
\begin{array}{c|c}
\text{bag}&\text{missed boundary set}\\ \hline
\{e_0\}&\{3,7\}\\
\{e_1\}&\{0,5\}\\
\{f_0\}&\{1,7\}\\
\{f_1\}&\{1,6\}.
\end{array}
\tag{2.2}
\]

There are no other edges.  The four singleton bags are connected,
pairwise disjoint, disjoint from `S union {u}`, and each sees exactly six
boundary vertices.  The two required same-shore adjacencies are literal.

The adjacent deterministic verifier exhausts all edge contractions of this
connected graph down to seven vertices.  None yields `K_7`; hence the graph
has no `K_7` minor.  It also checks directly that no certificate of the
four-anchor plus two-singleton form used by the positive theorem exists.

## 3. Exact scope

The example proves that four individually near-full bags are insufficient.
A valid completion theorem needs either

- one common missed set of order at most two for the two bags in each
  shore, as in the promoted theorem; or
- additional host geometry strong enough to couple their different
  defects.

The graph is not seven-connected, seven-chromatic, or minor-minimal, and it
does not carry the aligned Kempe-operation responses, the two literal full
shores, or the confined-lobe provenance of the live degree-eight branch.
It therefore does not refute a host-level theorem which uses those omitted
hypotheses to force common defects.  It only rules out replacing that step
by the independent-defect four-bag claim above.

## Verifier

Run

```text
python3 barriers/hc7_degree8_independent_two_defect_four_bag_barrier_verify.py
```
