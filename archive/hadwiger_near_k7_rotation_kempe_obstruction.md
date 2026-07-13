# Rotation repair at a locked near-\(K_7\) bag: the exact Kempe obstruction

## 1. Scope and conclusion

Consider the alternating port cross returned by the tree interval criterion
in `hadwiger_near_k7_port_labeled_split_2apex.md`.  If its central tree
edge is \(xy\), deletion-criticality supplies five bichromatic
\(x\)-\(y\) detours, one for each colour other than the common colour of
\(x,y\).

Those five detours do **not**, by themselves, repair the prescribed portal
rotation.  The missing information is not the number of detours, nor even
their local disjointness.  It is an alignment between colour labels and the
port labels of the fixed near-clique model.  This note proves three precise
facts.

1. Contracting the model bags and taking an edge-deletion colouring do not
   commute.  Thus the five secondary colours cannot be identified with the
   five reserved branch sets without an additional lemma.
2. There is a treewidth-two graph with seven internally disjoint
   \(x\)-\(y\) detours and all five required bichromatic detours.  Hence
   even local linkage of order seven plus the complete Kempe conclusion
   does not force a rooted \(K_4\), a port cross repair, or any nonplanar
   structure.
3. A genuinely clean detour segment *does* give a \(K_7\)-model by an
   explicit two-bag peel.  Therefore the correct target is a
   **bag-aligned clean-segment-or-adhesion lemma**, not a statement merely
   counting Kempe paths.

The graph in Section 3 is deliberately only a counterexample to the
proposed *local inference*.  It is not seven-contraction-critical.  Asking
for such a counterexample while also requiring it to be \(K_7\)-minor-free
would ask for a counterexample to \(HC_7\) itself.

## 2. The noncommutation obstruction

Let \(G\) be seven-critical, let \(xy\in E(G)\), and let
\(c\) be a six-colouring of \(G-xy\).  The standard edge-deletion witness
gives

\[
 c(x)=c(y)=0                                                   \tag{2.1}
\]

and, for every \(i\in\{1,\ldots,5\}\), an \(x\)-\(y\) path in the
subgraph induced by colours \(\{0,i\}\).  Otherwise switching the
\(i\)-coloured component meeting one endpoint separates their colours and
extends to a six-colouring of \(G\).

Now fix a near-\(K_7\) model \(\mathcal M\).  Its branch sets need not be
monochromatic in \(c\).  In fact, the following elementary obstruction is
the source of the gap.

### Proposition 2.1 (colouring and model contraction do not commute)

Let \(\mu\) contract a connected branch set \(B\) of \(\mathcal M\).

* A colouring of \(G-xy\) descends through \(\mu\) only if all vertices
  identified by \(\mu\) have one colour.
* A colouring of \((G/\mu)-xy\) need not lift to a colouring of
  \(G-xy\).
* Even if \((G/\mu)-xy\) is six-colourable, edge-criticality of \(xy\) in
  \(G\) says nothing about the colours of its endpoints in that proper
  minor.

Consequently, the five colours in (2.1) do not canonically label the five
other branch sets of \(\mathcal M\).

#### Proof

The first assertion is the definition of a colouring after vertex
identification: the new contracted vertex would otherwise need two
different colours.  For the second, a colour assigned to the contracted
vertex need not extend to a proper colouring of the nontrivial connected
graph \(B\), and its external neighbours can forbid all available
extensions.  For the third, seven-criticality says that each **proper
subgraph** of \(G\) is six-colourable and that \(G\) is not.  It neither
makes a fixed edge critical in every proper minor nor prescribes equality
of the endpoints in all colourings of such a minor.  \(\square\)

Thus an \(\{0,i\}\)-path can enter and leave one reserved bag several
times, meet several reserved bags, or miss the bag informally assigned
label \(i\).  None of those behaviours contradicts the Kempe witness.

## 3. Seven detours can live in treewidth two

Let \(F\) have terminals \(x,y\) and seven internally vertex-disjoint
length-four paths between them.  For \(i=1,\ldots,5\), write the first five
paths as

\[
 x-a_i-b_i-c_i-y.                                             \tag{3.1}
\]

Write the last two as

\[
 x-r_j-s_j-t_j-y,\qquad j=1,2.                               \tag{3.2}
\]

There are no other edges.  Let \(F^+=F+xy\).

### Proposition 3.1 (the seven-detour theta obstruction)

The following hold.

1. \(\kappa_F(x,y)=7\).
2. \(F^+\) has treewidth at most two, and hence has no \(K_4\)-minor.
3. \(F\) has a proper six-colouring in which \(x,y\) have colour zero
   and, for each \(i\in\{1,\ldots,5\}\), (3.1) is an
   \(x\)-\(y\) path using exactly colours \(\{0,i\}\).

#### Proof

The seven displayed paths are internally disjoint.  Conversely, deleting
one internal vertex from each separates \(x\) from \(y\); Menger's theorem
gives (1).

For (2), use the root bag \(\{x,y\}\).  For every path
\(x-u-v-w-y\), attach the chain of bags

\[
 \{x,y,u\},\quad \{y,u,v\},\quad \{y,v,w\}                  \tag{3.3}
\]

to the root, with consecutive bags joined in the displayed order.  Every
edge of \(F^+\) is covered and the bags containing any fixed vertex form a
connected subtree.  The largest bag has order three.

For (3), put

\[
 c(x)=c(y)=c(b_i)=0,\qquad c(a_i)=c(c_i)=i.                  \tag{3.4}
\]

On each of the two remaining paths use the sequence of colours
\(0,1,2,1,0\).  Adjacent vertices get different colours, and every path
in (3.1) is the asserted bichromatic detour.  \(\square\)

The four prescribed port occurrences at a locked edge may be attached to
the two terminal sides and declared to occur in any alternating cyclic
order in the **contracted** quotient.  Proposition 3.1 is unaffected: the
five Kempe detours and even local \(x\)-\(y\) connectivity seven coexist
with a planar, treewidth-two detour graph.  Hence those data do not decide
whether an expansion society is rural.

This does not refute a theorem whose alternative is a small adhesion:
the theta graph visibly has small global separators.  It refutes the
specific inference

\[
 \text{five edge-critical Kempe detours}
 \Longrightarrow
 \text{a label-preserving rotation repair or rooted clique}.             \tag{3.5}
\]

Any valid repair theorem must use global minor-criticality to align a
detour with the fixed bags, or else return the adhesion on which that
alignment fails.

## 4. What a clean segment really proves

The following is the exact positive certificate.  It is stated without
colour labels.

### Theorem 4.1 (bag-aligned clean-segment peel)

Let

\[
 (\{a\},\{c\},\{q_1\},\{q_2\},\{q_3\},D,E)                 \tag{4.1}
\]

be a \(K_7^-\)-model whose only missing model adjacency is \(ac\).
Suppose

\[
 D=P\mathbin{\dot\cup}R,\qquad E=Z\mathbin{\dot\cup}W    \tag{4.2}
\]

are partitions into nonempty connected sets satisfying:

1. \(P\) is adjacent to \(R,a,c\);
2. \(R\) is adjacent to \(Z\);
3. \(Z\) is adjacent to \(W\);
4. \(R\cup Z\) is adjacent to each of \(c,q_1,q_2,q_3\);
5. \(W\) is adjacent to each of \(c,q_1,q_2,q_3\); and
6. \(W\) is adjacent to \(P\) or to \(a\).

Then \(G\) has a \(K_7\)-minor.

#### Proof

Use the seven branch sets

\[
 \{a\}\cup P,\quad \{c\},\quad
 \{q_1\},\{q_2\},\{q_3\},\quad R\cup Z,\quad W.           \tag{4.3}
\]

They are connected and disjoint.  The first branch set meets \(c\) via
\(P\), repairing the deficient pair.  It meets \(R\cup Z\) via \(PR\)
and meets \(W\) by condition 6.  Conditions 4 and 5 supply all contacts
from the last two branch sets to the four remaining singletons, and
\(ZW\) joins the last two branch sets.  All other singleton adjacencies
already occur in (4.1).  \(\square\)

In the rotation application, \(P,R\) are the two sides of the locked
tree edge.  A detour is **clean and bag-aligned** precisely when one of
its segments can be assigned to \(Z\) while the residue of the opposite
bag can be assigned to \(W\) and the six conditions remain true.  The
theorem then repairs the model; no further Kempe argument is needed.

### Corollary 4.2 (exact charge left by a failed clean segment)

Retain (4.1)--(4.2), assume conditions 1--3, and suppose no \(K_7\)-minor
exists.  For every proposed segment \(Z\) with \(Z,W=E-Z\) nonempty and
connected, at least one of the following holds:

* \(R\cup Z\) loses a port in \(\{c,q_1,q_2,q_3\}\);
* \(W\) loses a port in \(\{c,q_1,q_2,q_3\}\); or
* \(W\) is anticomplete to \(P\cup\{a\}\).

In particular, when \(R\) already retains all four ports, every failed
segment is charged either to a portal class trapped wholly in \(Z\) or to
the last cross-contact from \(W\) to \(P\cup\{a\}\).

#### Proof

If none of the three failures occurs, conditions 4--6 of Theorem 4.1 all
hold, which gives a \(K_7\)-minor.  \(\square\)

This corollary identifies the finite state that a contraction-critical
exchange must change.  It also explains why a path count alone stops:
five detours can be charged injectively to five indispensable portals of
a minimal five-terminal Steiner tree.  There is no sixth coloured detour
available for a pigeonhole argument.  Seven-connectivity supplies more
uncoloured routes, but Proposition 2.1 shows that they have no automatic
colour-state alignment.

## 5. Corrected rotation-repair target

The next lemma must explicitly retain both the coloring state and the
port state.

> **Bag-aligned rotation exchange.**  Let \(xy\) be the edge of a
> lexicographically minimal locked tree bag whose sides support an
> alternating port cross.  In a seven-contraction-critical host, either
> (i) one edge-deletion witness has a clean segment satisfying Theorem
> 4.1, (ii) the detours and the fixed bags directly give a rooted
> \(K_4\) and hence a \(K_7\)-minor, or (iii) the first unavoidable
> charged ports in Corollary 4.2 lie on two carriers whose lifted boundary
> is a colour-gluable adhesion.

The lexicographic minimality must range jointly over the model, its portal
cores, and the chosen edge-deletion witness.  Minimality of the model
alone cannot control where a bichromatic path first meets a reserved bag.

This target is narrow enough to be meaningful and strong enough to finish
the alternating-cross outcome of the near-\(K_7\) route.  Proposition 3.1
shows exactly what the proof must use beyond the five standard Kempe
paths: a minor-critical exchange rule that couples colour classes to
prescribed bag portals.
