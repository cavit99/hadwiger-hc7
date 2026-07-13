# The degree-nine exact seven-cut: a parity state obstruction

## 1. Scope

**Subsequent status.**  This note remains a valid warning against an
abstract colouring-state gluing argument, but its cut is no longer a
live case.  `hadwiger_degree9_exact_cut_ordered_spine.md` eliminates the
entire exact-cut outcome of Theorem 4.6 by retaining the labelled carrier
edges.  Nothing below should therefore be read as a remaining obstruction
to the current degree-nine programme.

Retain the exact-cut outcome of
`hadwiger_degree9_protected_portal_peel.md`, Theorem 4.6.  Its adhesion is

\[
 X=\{q,h,1,2,3,4,6\}.
\]

The edges on \(X-\{q\}\) forced by the pure Moser spindle are

\[
 h1,h2,h3,h4,12,16,26,34.                       \tag{1.1}
\]

The edges from \(q\) to the other six adhesion vertices are not fixed by
the portal-bottleneck argument.  In this note they may be arbitrary.

The conclusion is negative but exact.  Full-shore trace contractions and
the one-step boundary-transition axiom do **not**, as abstract colouring
state data, force this adhesion to glue.  There is a particularly simple
obstruction: parity of the number of equality blocks.  Therefore an
elimination of this exact cut must use the seven-connected internal shore
geometry (or a rooted model inside it), not only its collection of exact
traces.

This is not a counterexample to \(HC_7\).  Section 5 records precisely
which counterexample hypotheses are and are not reproduced.

## 2. Two disjoint trace-complete state families

For a graph \(J\) on \(X\), let \({\cal P}_6(J)\) be the set of partitions
of \(X\) into at most six nonempty independent blocks.  These are exactly
the equality partitions of proper six-colourings of \(J\).  Put

\[
 \begin{aligned}
  {\cal P}_{\rm ev}(J)&=\{\Pi\in{\cal P}_6(J):|\Pi|\text{ is even}\},\\
  {\cal P}_{\rm odd}(J)&=\{\Pi\in{\cal P}_6(J):|\Pi|\text{ is odd}\}.
 \end{aligned}                                                   \tag{2.1}
\]

### Theorem 2.1 (parity trace completeness)

Let \(J\) contain exactly the fixed edges (1.1) among
\(X-\{q\}\), and give \(q\) an arbitrary neighbourhood in
\(X-\{q\}\).  Then the two families in (2.1) are disjoint, and each has
the following property:

> For every nonempty independent set \(I\subseteq X\), the family
> contains a partition having \(I\) as one of its blocks.

Both families also contain a state using at most five blocks.

#### Proof

Let \(Y=X-\{q\}\).  The graph forced by (1.1) has
\(\alpha(J[Y])=2\) and clique number three.  Consequently
\(\alpha(J)\le3\).

First let \(|I|=2\).  The partition consisting of \(I\) and the five
remaining singletons has six blocks.  The five vertices outside \(I\)
do not induce a clique: a clique in \(J\) has order at most four, since
deleting \(q\) leaves clique number three.  Merge a nonadjacent pair
outside \(I\).  This gives a proper five-block partition with the same
distinguished block \(I\).  Thus both parities occur.

Now let \(|I|=3\).  Then \(q\in I\), because
\(\alpha(J[Y])=2\).  The four vertices outside \(I\) lie in \(Y\),
which has no four-clique.  The partition consisting of \(I\) and four
singletons has five blocks; merging a nonadjacent pair outside \(I\)
gives four blocks.  Again both parities occur.

It remains to treat \(I=\{x\}\).  In every row below, \(ab\) denotes
the independent pair \(\{a,b\}\).  The two displayed pairs are
vertex-disjoint and avoid \(x\):

\[
\begin{array}{c|c}
x&\text{two fixed nonedges outside }x\\ \hline
q&13,24\\
h&13,24\\
1&23,46\\
2&13,46\\
3&h6,14\\
4&h6,13\\
6&13,24
\end{array}                                                     \tag{2.2}
\]

Starting from seven singleton blocks, merge the first pair in the row.
This gives a proper six-block partition in which \(\{x\}\) is a block.
Merge the second pair as well to obtain a proper five-block partition
with the same singleton block.  This proves the trace assertion.

Finally,

\[
 \{13,24,h6,\{q\}\}                                      \tag{2.3}
\]

is a proper four-block state and

\[
 \{13,24,\{h\},\{6\},\{q\}\}                         \tag{2.4}
\]

is a proper five-block state, independently of the \(q\)-edges.  Hence
both parity families contain a state using at most five blocks.  Their
disjointness is immediate from (2.1). \(\square\)

The exhaustive verifier `exact7_state_probe.py` independently enumerates
all 877 set partitions for each of the \(2^6=64\) possible
\(q\)-neighbourhoods.  It checks every independent trace and obtains
64/64 successful parity pairs.

### Corollary 2.2

The connected-shore exact-trace lemma, even applied to every independent
set on this adhesion and on both sides, cannot imply that the two side
partition families intersect.  Nor does the weaker fact obtained by
contracting a full shore alone (existence of a state on at most five
blocks), because (2.3)--(2.4) supply such a state in both disjoint
families.

## 3. Actual graph gadgets with two full connected shores

The obstruction is not merely a formal pair of set systems.

### Proposition 3.1 (full-shore realization)

For either \(\epsilon\in\{\mathrm{ev},\mathrm{odd}\}\), there is a
finite graph \(H_\epsilon\) containing \(J\) induced on \(X\) such that

1. a labelled six-colouring of \(X\) extends to \(H_\epsilon\) exactly
   when its equality partition belongs to
   \({\cal P}_\epsilon(J)\); and
2. \(H_\epsilon-X\) is connected and has neighbourhood exactly \(X\).

#### Proof

The relation consisting of the labelled colourings in
\({\cal P}_\epsilon(J)\) is closed under every permutation of the six
colours.  The realization theorem of Dvořák and Swart (Theorem 3 in
*A note on extendable sets of colorings and rooted minors*, arXiv:
2504.07764) therefore gives a finite graph \(R_\epsilon\) whose exact
boundary extension relation is this relation.  Add the edges of \(J\)
on \(X\).  This does not remove an intended colouring because every
member of the relation is proper on \(J\), and it cannot add a colouring.
There is no unwanted boundary edge: Theorem 2.1 gives, for every nonedge
of \(J\), an intended colouring in which its ends are equal.

It remains to make the open interior connected and full without changing
the relation.  Add a new vertex \(c\), and for every \(x\in X\) add a
vertex \(l_x\) and the path \(x l_x c\).  For every component \(C\) of
\(R_\epsilon-X\), choose \(u_C\in C\), add a vertex \(m_C\), and add
the path \(c m_C u_C\).  Call the resulting graph \(H_\epsilon\).

Any colouring of \(R_\epsilon\) extends over the new vertices: choose
the colour of \(c\) arbitrarily, choose \(l_x\) different from the at
most two colours on \(c,x\), and choose \(m_C\) different from the at
most two colours on \(c,u_C\).  Conversely, restriction to
\(R_\epsilon\) shows that no new boundary colouring is admitted.  The
new interior is connected, and every boundary vertex has its neighbour
\(l_x\). \(\square\)

Take disjoint copies of the two open interiors and identify their copies
of \(X\).  The resulting graph has a seven-vertex separator and two
connected shores, each full to the separator, but is not six-colourable:
any six-colouring would induce a partition in the empty intersection
\({\cal P}_{\rm ev}(J)\cap{\cal P}_{\rm odd}(J)\).

This construction is only a gluing counterarchitecture.  The harmless
paths used to connect the realizers are deliberately redundant, so the
resulting graph is not minor-critical.

## 4. Actual gadgets satisfying every internal one-step transition

The proper-minor transition axiom alone also does not remove the parity
obstruction.

### Proposition 4.1 (internally minor-critical parity pair)

There are finite boundaried graphs \(M_{\rm ev},M_{\rm odd}\), each
containing \(J\) on \(X\), with exact extension relations
\({\cal P}_{\rm ev}(J)\) and \({\cal P}_{\rm odd}(J)\), respectively,
such that the following holds.  If their open interiors are made
disjoint and the copies of \(X\) are identified, then deletion of any
open-side vertex, or deletion or contraction of any edge whose two ends
lie in one open side, makes the union six-colourable.

#### Proof

Start with arbitrary finite realizers supplied by Proposition 3.1 before
the harmless connectivity augmentation.  On each side, repeatedly delete
an interior vertex or an edge with two interior ends whenever that
deletion leaves the exact same boundary extension relation.  Finiteness
gives a deletion-minimal realizer \(M_\epsilon\).

Deleting an interior vertex or edge cannot destroy a boundary extension,
so minimality says every such deletion admits a new boundary colouring.
Since \(M_\epsilon\) already admits **every** proper colouring of parity
\(\epsilon\), every new state has the opposite parity.  It therefore
extends over \(M_{1-\epsilon}\).

For an internal edge \(uv\), let \(f\) be a new opposite-parity boundary
colouring extending to \(M_\epsilon-uv\).  In every such extension,
\(u\) and \(v\) have the same colour; otherwise the same colouring would
extend to \(M_\epsilon\).  Identifying \(u,v\) therefore gives a proper
colouring of \(M_\epsilon/uv\) with the same boundary colouring \(f\).
Thus both deletion and contraction of \(uv\) create a state accepted by
the opposite side.

After any displayed operation, choose the same labelled boundary
colouring \(f\) on the two sides and glue the extensions.  The open
interiors are disjoint and no edge joins them, so there is no overlap or
cross-edge issue. \(\square\)

Proposition 4.1 reproduces exactly the internal one-step compatibility
asserted by the minimal-incompatible-states theorem.  It does not claim
compatibility after operations meeting \(X\), which that theorem likewise
does not supply for a fixed unchanged adhesion.

## 5. Trust boundary and the remaining positive target

The constructions prove the following sharp negative conclusion.

* Full connected shores plus every independent exact trace do not force
  gluing (Proposition 3.1).
* Every internal deletion/contraction transition plus every independent
  exact trace does not force gluing (Proposition 4.1 and Theorem 2.1).

They do **not** produce one graph having all of the following jointly:

1. seven-connectivity;
2. one connected full component on each prescribed side;
3. the internal one-step transition property;
4. no \(K_7\)-minor.

That joint package is exactly where a genuine \(HC_7\) theorem may live.
In particular, the note does not disprove a theorem using the portal
placement inside the full component, nor a theorem using seven-connectivity
to force a rooted clique partition.

The correct next exact-adhesion target is therefore geometric rather than
state-only:

> **Parity-breaking full-shore lemma.**  In the degree-nine Moser
> adhesion (1.1), if both open sides contain a full connected component,
> the whole graph is seven-connected and internally minor-critical, then
> at least one side admits two proper six-colour boundary states whose
> equality-block counts have opposite parity in a way compatible with the
> opposite side; equivalently, the two extension families cannot be
> separated by the parity cut (2.1).

Proving this lemma requires a portal/linkage argument inside a full shore.
No argument using only the exact traces or only the abstract one-step
transition sets can prove it, by the audited constructions above.
