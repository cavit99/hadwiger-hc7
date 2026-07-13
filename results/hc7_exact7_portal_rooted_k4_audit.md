# Independent audit: exact-seven portal matching and rooted-`K_4` exchange

## Verdict

**GREEN.**  The Hall separator, literal seven-bag lift, transversal-matroid
transport, and facial propagation are all valid with overlapping portal
sets and also when the thin shore has order five or six.  The result does
not close the cofacial rural outcome and does not turn that outcome into an
apex set.

## 1. Hall deficiency and the separator

Let the portal bipartite graph have sides `S` and `V(C)`, with `|S|=k`,
and let its maximum matching have order `m`.  The standard deficiency
identity on the `S` side is

\[
 m=\min_{A\subseteq S}\bigl(k-|A|+|N_C(A)|\bigr).
\]

Thus the set `A` used in (1.3) exists even when `|C|<k`; this is not an
implicit assumption that the matching is trying to saturate `S`.  The
proposed separator

\[
 X=(S-A)\cup N_C(A)
\]

has literal order `m`.  The strict inequality
`m<min{k,|C|}` implies `C-N_C(A)` is nonempty: if
`N_C(A)=V(C)`, then (1.3) gives `m>=|C|`.

After deleting `X`, a vertex of `C-N_C(A)` cannot leave through `A`
because it is not in `N_C(A)`, cannot leave through `S-A` because those
vertices are deleted, and cannot leave through another open-shore
component or the opposite open shore by the definition of an actual
separation and of `C`.  The opposite open shore is nonempty and disjoint
from `X`.  Hence `X` is a genuine separator of order `m<k`, contradicting
`k`-connectivity.  Both the formula and the two sides of the separation
are therefore correct.

In particular, for `k=7` and `|L|=5` or `6`, the conclusion is a matching
which saturates every vertex of `L`, of order five or six.  Nothing in the
later rank-four argument requires seven distinct portal vertices.

## 2. Literal `K_7` lift

The seven bags in (2.1) are disjoint because the four rooted bags lie in
`L`, the three packets lie in `R`, and all seven boundary anchors are
distinct.  They are connected because `x_i t_i` is an edge and every
full packet contacts its own anchor.

All 21 clique adjacencies are present:

* the six pairs among the first four bags come from the rooted `K_4`;
* for each pair of packet bags, `P_j` contacts the other bag's literal
  anchor `r_{j'}` (three pairs);
* for each of the twelve mixed pairs, `P_j` contacts the literal vertex
  `t_i` in the rooted bag.

This is label-preserving and does not identify a colour with a model bag.

## 3. Transversal matroid, truncation, and overlap

The sets `Z_s=N_L(s)` present a transversal matroid on the actual portal
vertices.  An independent set is exactly a set of distinct portal
vertices admitting distinct literal labels.  Theorem 1.1 makes its rank
`min{7,|L|}`, hence at least five when `L` is four-connected; truncating
to rank four is legitimate.

Every basis of the truncation is a four-element partial transversal and
therefore has four distinct representing labels, exactly what Lemma 2.1
needs.  A portal vertex belonging to several `Z_s` remains just one
ground element, is a nonloop, and extends to a basis of the rank-four
truncation.  Thus overlapping portal sets create neither duplicate roots
nor an unrepresented portal.  This also verifies the two smallest live
orders, `|L|=5,6`.

The basis graph is connected under one-element exchanges.  Consecutive
bases share three actual vertices, not merely three labels, which is the
correct overlap needed for face propagation.

## 4. Rooted model and facial propagation

For every rank-four basis, absence of the literal lift excludes a rooted
`K_4` in `L`.  The Fabila-Monroy--Wood rooted-`K_4` theorem at its valid
strength then makes `L` planar and puts that basis on a face.  Since `L`
is four-connected, it is three-connected, so its plane embedding is
unique up to reflection.  Distinct faces of a three-connected simple
plane graph share at most two vertices.  Faces assigned to consecutive
bases share the three common basis vertices and hence are the same.
Connectivity of the basis graph gives one face `F` for all bases.

Every actual portal is a nonloop and extends to such a basis, so every
vertex of `N_L(S)` lies on `F`.  This proves precisely the stated
cofacial conclusion.  It does not claim that all vertices of `L` lie on
`F`, that the seven labels have distinct portals on `F`, or that adding
the literal boundary preserves planarity.

## 5. Corollary and overlap with existing notes

In a target-free `(1,3)` cell, Theorem 3.1 implies that a nonplanar or
noncofacial thin shore is not four-connected and therefore has a
separator of order at most three.  The separate audited
`hc7_exact7_thin_shore_exchange` theorem closes cutvertices and all
2-cuts with at least three lobes, so the assertion that every surviving
2-cut has exactly two lobes is correctly imported rather than reproved.

The ingredients overlap with two earlier repository results:

* `archive/hadwiger_full_deletion_propagation.md`, Lemma 5.1, already
  proved the portal matching when `|C|>=k`; Theorem 1.1 here is the clean
  sharp extension to all component orders.
* `results/hc7_near_k7_active_root_face_exchange.md`, especially
  Theorem 2.3, already proved the transversal-matroid/basis-exchange
  facial-coherence mechanism for four named portal families.  The new
  note applies the same mechanism to the rank-four truncation of all
  seven literal portal labels and combines it with the three-full-packet
  lift.

Accordingly the reusable new package is the exact-seven combination,
not a new proof of the general rooted-`K_4` or matroid facts.

## 6. Trust boundary

The conclusion needs all of the following:

1. an actual order-seven adhesion with a nonempty opposite shore, for
   the Hall separator;
2. three disjoint literal `S`-full packets in the opposite shore, for
   the seven-bag lift; and
3. four-connectivity of the thin shore, for the rooted-`K_4` dichotomy
   and unique facial propagation.

Dropping (2) leaves only a rooted `K_4`, not a `K_7`; dropping (3) permits
different bases to be trapped behind low-order separators.  The final
cofacial rural page remains an open structural cell.
