# Minimal clean gates: a terminal-arm bypass theorem

## 1. Scope and the directed-sink correction

Use the notation of hadwiger_rooted_k24_clean_capture.md.  Thus

\[
  (T_1,T_2,T_3,T_4;C_1,C_2)
\]

is a clean rooted \(K_{2,4}\)-model, \(a,z\) avoid all six branch
sets, and

\[
  R=H-\bigcup_{i=1}^4T_i .
\]

After contracting \(C_1,C_2\), the auxiliary object must be a digraph:
ordinary edges are replaced by their two orientations and the two
contracted targets have outdegree zero.  A target appearing in a minimum
separator is therefore a target-reachability failure, not necessarily an
ordinary cutvertex after lifting.  The theorem below concerns only an
ordinary gate \(s\notin C_1\cup C_2\).

The clean-capture proof itself is valid.  Unit capacities force distinct
source and target ends, lifting restores two disjoint connected carriers,
and a shortest connector in the common undirected component has interior
outside both carriers.  Contracted terminal bags lift inside their
prescribed \(T_i\)'s, so all four terminal-terminal adjacencies and all old
contacts are retained.  Replacing one multiply rooted bag by two rooted
bags while dropping an uncontacted bag increases the contact count by one.

## 2. Innermost ordinary gates supply the missing root-side linkage

Let \(\mathcal C=C_1\cup C_2\).  Suppose \(s\notin
\{a,z\}\cup\mathcal C\) separates \(\{a,z\}\) from \(\mathcal C\) in
the undirected graph \(R\).  Let \(W_s\) be the union of the components
of \(R-s\) containing \(a\) or \(z\).  Choose \(s\) so that
\(|W_s|\) is minimum among **all** one-vertex
\(\{a,z\}\)-to-\(\mathcal C\) separators outside \(\mathcal C\),
allowing a source vertex itself to be a separator.  The lemma below
therefore applies when an innermost separator can be chosen internally.
A source separator is retained as a separate residual.

### Lemma 2.1 (root-side two-linkage)

Let \(p\notin V(R)\) have a neighbour in \(W_s\), and add \(p\), together
with all its edges to \(W_s\), to \(R[W_s\cup\{s\}]\).  Then this graph
contains two vertex-disjoint paths from the distinct sources \(a,z\) to
the distinct targets \(s,p\), in some order.

#### Proof

Both targets are individually reachable from \(\{a,z\}\): every
source-containing component of \(R-s\) has a neighbour at \(s\), and
\(p\) has a neighbour in a source-containing component.  If the required
linkage did not exist, vertex Menger would give a one-vertex separator
\(q\).

The separator is not \(s\), because a source reaches \(p\) inside its
component of \(R-s\).  It is not \(p\), because a source reaches \(s\)
inside \(W_s\cup\{s\}\).  Hence \(q\in W_s\) (an endpoint source is
allowed).  The vertex \(q\) separates the surviving source set from
\(s\).  Every source-to-\(\mathcal C\) path in \(R\) meets \(s\), and
its prefix up to its first visit to \(s\) lies in
\(W_s\cup\{s\}\).  Therefore \(q\) is itself an ordinary
\(\{a,z\}\)-to-\(\mathcal C\) separator.  Its root side is a nonempty
proper subset of \(W_s\): one of the two distinct sources survives
deletion of \(q\), while \(s\) is no longer reachable.  This contradicts
the choice of \(s\). \(\square\)

The exclusion of \(s\in\{a,z\}\) is substantive: Lemma 2.1 does not claim
that an innermost source separator has the same two-linkage.  The
minimization includes source separators precisely so that a separator
\(q=a\) or \(q=z\) arising in the proof still contradicts the minimality
of an internal \(s\).

## 3. A detachable terminal arm opens the gate

Retain the four prescribed terminal vertices \(t_i\in T_i\).  They
represent the original clique bags and, when that bag was contacted, its
old root is retained with \(t_i\).

### Definition 3.1 (detachable arm at a gate)

For \(i\in[4]\), a partition

\[
       T_i=A\mathbin{\dot\cup}B
\]

is a detachable arm (towards \(C_1\), say) if:

1. \(A,B\) are nonempty and connected, and \(E(A,B)\ne\varnothing\);
2. \(t_i\in B\);
3. some \(p\in A\) has a neighbour in \(W_s\);
4. \(E(A,C_1)\ne\varnothing\);
5. \(B\) is adjacent to \(C_2\) and to every \(T_j\), \(j\ne i\).

The definition with \(C_1,C_2\) interchanged is also allowed.

### Theorem 3.2 (minimal-gate terminal-arm bypass)

Assume that \(R\) has one undirected component containing
\(a,z,C_1,C_2\), that \(s\) is an innermost ordinary gate, and that from
\(s\) there is a path to \(C_2\) in \(R-C_1\) whose interior lies outside
\(W_s\).  If some \(T_i\) has a detachable arm towards \(C_1\), then the
clean model can be changed into a doubly rooted \(K_{2,4}+e\)-model.
After lifting to the contact-maximal \(K_6\)-model, this increases the
number of contacted bags.

#### Proof

Let \(p\in A\) be as in Definition 3.1.  By Lemma 2.1 there are disjoint
paths \(P_p,P_s\) from \(a,z\), in some order, to \(p,s\), respectively,
inside \(W_s\cup\{s,p\}\).  Let \(Q\) be an \(s\)-to-\(C_2\) path in
\(R-C_1\) with interior outside \(W_s\).

Form two disjoint connected sets

\[
  A^*=P_p\cup A\cup C_1,\qquad
  Z^*=P_s\cup Q\cup C_2.
\]

They are disjoint: the root-side paths are disjoint; \(A\subseteq T_i\)
is outside \(R\); and the interior of \(Q\) lies on the far side of
\(s\) and avoids \(C_1\).  Each set is adjacent to every \(T_j\),
\(j\ne i\), through its original free carrier.  Replace \(T_i\) by
\(B\).  The set \(B\) sees \(Z^*\) through its retained adjacency to
\(C_2\), sees \(A^*\) through an \(A\)-\(B\) edge, and retains its
adjacencies to all other terminal bags.  It is connected and still
contains \(t_i\).

It remains only to make \(A^*,Z^*\) adjacent.  Both meet the common
undirected component of \(R\).  A shortest path in that component between
the two sets has interior outside their union.  Absorb its internal
vertices into one of them.  This does not meet any terminal branch set,
because all \(T_j\) were deleted in the definition of \(R\).

The resulting two rooted sets, \(B\), and the other three \(T_j\)'s are
six pairwise adjacent branch sets.  They contain \(a,z\) separately and
retain all four prescribed terminals.  This is the required model.
\(\square\)

### Corollary 3.3 (the exact ordinary-gate residue is a locked core)

In a surviving contact lock, suppose an innermost separator is an
internal ordinary gate, and assume neither sink target-reachability
failure occurs.  Then every attachment
from its root side to a multiply hit terminal carrier lies in a carrier
with no detachable arm in either direction.

In particular, Lemma 5.1 of hadwiger_rooted_k24_clean_capture.md does
more than produce portal multiplicity.  Outside a tight seven-cut, it
produces at least six actual attachments, but every repeated carrier must
be a simultaneous locked Steiner core for:

* its prescribed terminal;
* its three other terminal adjacencies;
* both free-carrier adjacencies; and
* all root-side attachment vertices.

Any pendant region containing a root-side attachment and only one
free-carrier charge is eliminated by Theorem 3.2.

### Theorem 3.4 (source-gate terminal-arm bypass)

The same conclusion holds when the innermost separator is a source, say
\(s=a\), provided the attachment \(p\in A\) has a neighbour in the
component \(W\) of \(R-a\) containing the other source \(z\), and there
is an \(a\)-to-\(C_2\) path in \(R-C_1\) whose interior avoids \(W\).

#### Proof

Join \(z\) to \(p\) inside \(W\cup\{p\}\), and use the given path from
\(a\) to \(C_2\).  These two paths are disjoint because the latter has
interior outside \(W\).  Now repeat the construction in Theorem 3.2:
absorb \(A\) and \(C_1\) into the \(z\)-carrier, retain \(B\) as
\(T_i\), and use a shortest connector in \(R\) to make the two rooted
carriers adjacent. \(\square\)

Thus a source gate is not a new unlocked geometry.  It survives only
when all attachments from the component of the other root lie in the
same locked terminal/free-carrier cores already described above.

## 4. What an edge-critical Kempe detour can rigorously repair

The following records the exact safe use of the five detours around an
edge.  It avoids the invalid assumption that an arbitrary Kempe path
misses the reserved branch sets.

### Lemma 4.1 (one-charge Kempe repair)

In the setting of Theorem 3.2, suppose
\(T_i=A\dot\cup B\) satisfies items 1--4 of Definition 3.1 and all of
item 5 except for adjacency to one retained carrier \(K\), where

\[
 K\in\{C_2\}\cup\{T_j:j\ne i\}.
\]

Let \(xy\in E(A,B)\), with \(x\in A,y\in B\), and color \(G-xy\) with
six colors.  First fix the two root-side paths, the far-side
\(s\)-to-\(C_2\) path, and a connector between the two prospective
rooted carriers as in the proof of Theorem 3.2.  If one of the five
\(x\)-\(y\) bichromatic Kempe detours contains a \(B\)-to-\(K\)
subpath whose interior avoids

\[
 A\cup C_1\cup C_2\cup\bigcup_{j=1}^4T_j
\]

and avoids all four fixed paths (the two root-side paths, the far-side
path, and the connector), then the contact lock opens.

#### Proof

Stop the displayed subpath at its first vertex in \(K\), and absorb its
interior into \(B\).  The enlarged \(B\) is connected, remains disjoint
from every other branch set and from the already fixed bypass
certificate, and now is adjacent to \(K\).  Replay the proof of Theorem
3.2 with those fixed paths.
\(\square\)

Thus every surviving one-charge arm has a concrete five-color blocking
certificate: for every interface edge and every non-edge color, the
corresponding detour either never supplies the missing carrier or meets a
reserved branch set (or a root-linkage path) before it can do so.  This is
strictly stronger than the former undifferentiated locked-tree state, but
it is not yet a proof that one of the five detours is clean.

## 5. A sink target failure reduces to the same terminal-arm lock

Suppose the contracted carrier \(C_1\) is the sink obstruction.  In
lifted language, every admissible root-to-\(C_2\) path meets \(C_1\).
Let \(U\) be the union of the components of \(R-C_1\) containing \(a\)
or \(z\).  Stop every path on first entering \(C_1\).

### Lemma 5.1 (carrier target plus one terminal attachment)

Let \(p\notin R\) have a neighbour in \(U\).  Then either:

1. there are two disjoint paths from \(a,z\) to the two distinct targets
   \(C_1,p\), one path ending in each; or
2. a one-vertex gate \(q\in U\), possibly one of the sources \(a,z\),
   separates the surviving source set from both free carriers and has
   root shore properly contained in \(U\).

#### Proof

Contract \(C_1\) to a directed capacity-one sink \(c_1\), make \(p\) a
second capacity-one sink, and work in the root-side graph induced by
\(U\cup C_1\cup\{p\}\).  Both targets are individually reachable.
If two disjoint paths do not exist, Menger gives a one-vertex separator
\(q\).  It cannot be either sink: after deleting one target, the other is
still reachable.  Hence \(q\in U\).

The vertex \(q\) separates the surviving sources from \(C_1\).  Since
every admissible path to \(C_2\) meets \(C_1\), it also separates the
sources from \(C_2\).  Its reachable root shore is a nonempty proper
subset of \(U\), as in Lemma 2.1. \(\square\)

### Theorem 5.2 (sink-gate terminal-arm bypass)

Suppose \(T_i=A\dot\cup B\), where \(A,B\) are connected and adjacent,
\(t_i\in B\), some \(p\in A\) has a neighbour in \(U\),
\(A\) is adjacent to the inaccessible carrier \(C_2\), and \(B\) is
adjacent to \(C_1\) and every \(T_j\), \(j\ne i\).  Then either a smaller
one-vertex gate exists (possibly a source gate), or the clean model can
be changed into a doubly rooted \(K_{2,4}+e\)-model.

#### Proof

Apply Lemma 5.1.  In its first outcome, let \(P_1,P_p\) be the disjoint
root paths ending at \(C_1,p\).  Form

\[
  A^*=P_1\cup C_1,\qquad
  Z^*=P_p\cup A\cup C_2,
\]

stopping \(P_1\) at first entry into \(C_1\).  These sets are disjoint
and connected.  Replace \(T_i\) by \(B\).  The residue \(B\) sees
\(A^*\) through its retained \(C_1\)-adjacency, sees \(Z^*\) through
an \(A\)-\(B\) edge, and retains all three other terminal adjacencies.
The two rooted sets see the other terminal bags through \(C_1,C_2\).
Finally make \(A^*,Z^*\) adjacent with a shortest connector in their
common undirected component of \(R\), exactly as in Theorem 3.2.
\(\square\)

Thus an entire free carrier may be the directed target obstruction, but
it does not create a new unlocked geometry.  A detachable terminal arm
towards the inaccessible carrier either opens it or exposes a strictly
closer one-vertex gate.  Iterating internal ordinary gates terminates
either in an opened model, in a source gate (which still needs the
additional hypotheses of Theorem 3.4), or in the same simultaneous
locked terminal core.  The source outcome cannot be silently called an
ordinary cutvertex.  The icosahedral architecture is sharp because its
relevant terminal carrier has no such detachable arm.

## 6. Net status

The clean-capture lemma is sound after the directed-sink clarification.
Theorem 3.2 completely eliminates the nonlocked ordinary-gate family and
Lemma 4.1 gives an actual Kempe-to-branch rerouting for every clean
one-charge detour.  The exact remaining local branches are:

1. absence of a clean rooted \(K_{2,4}\) packing;
2. a terminal locked core in which every repeated root-side attachment
   fails Definition 3.1 and all five one-charge detours are blocked;
3. a free-carrier sink target-reachability failure whose every terminal
   attachment is in the same locked core; or
4. a source gate with the same locked-core obstruction; or
5. a tight seven-cut from the equality case of the gate attachment count.

No claim here eliminates these five atomic states.

## 7. The no-clean-packing branch has the same clique-bridge invariant

The following applies to any prescribed rooted minor, not only
\(K_{2,4}\).

### Lemma 7.1 (maximal rooted-minor-free bridge attachment)

Let \(W\) be a graph with prescribed terminals, edge-maximal on its
vertex set subject to containing no prescribed rooted \(F\)-minor.  Let
\(X\) be a connected graph disjoint from \(W\), containing no prescribed
terminal, whose vertices are usable in branch-set rerouting.  If
\(W\cup X\) still has no prescribed rooted \(F\)-minor, then

\[
                         N_W(X)\text{ is a clique}. \tag{7.1}
\]

#### Proof

Suppose \(u,w\in N_W(X)\) are nonadjacent.  Edge-maximality gives a
prescribed rooted \(F\)-model in \(W+uw\).  If the model does not use
the new edge for either branch-set connectivity or a required
branch-set adjacency, it already exists in \(W\), a contradiction.

Choose a \(u\)-to-\(w\) path with interior in \(X\).  If \(u,w\) lie in
one branch set of the model, absorb the path interior into that branch
set.  If they lie in two branch sets and \(uw\) supplies their
adjacency, split the path at one edge and absorb its two halves into the
two branch sets.  In both cases all other branch sets and all prescribed
terminal placements are unchanged.  This lifts the rooted \(F\)-model
to \(W\cup X\), a contradiction. \(\square\)

### Corollary 7.2 (application to no clean rooted \(K_{2,4}\))

Suppose the usable four-terminal quotient is contained in an
edge-maximal rooted-\(K_{2,4}\)-free core \(W\) whose edges are all
realized in the host (or have pairwise compatible branch-avoiding
replacement paths).  Then every connected usable bridge \(X\) for which
\(W\cup X\) remains rooted-\(K_{2,4}\)-free attaches on a clique.  In a
\(K_7\)-minor-free host the clique has order at most six.

This count is initially a count of quotient objects.  If none of its
vertices is a contracted terminal carrier, it lifts to an actual
separator of order at most six and contradicts seven-connectivity.  If a
contracted terminal occurs, its lift may be a large branch bag and cannot
be charged as one actual cut vertex.  That alternative is precisely a
reserved-carrier attachment and must be handled by the portal peel; it is
not a small separator merely because it is one quotient vertex.

Under the realization hypothesis, the no-clean-packing residue has the
same exact form as the gate residue:

* a rooted-minor obstruction core on all usable vertices; and
* every bridge not already behind an actual cut of order at most six has
  an attachment charged to a genuinely reserved carrier, not material
  that may be absorbed for free.

An arbitrary abstract edge-maximal completion does **not** satisfy the
realization hypothesis: a rooted model created after adding \(X\) may
also use older artificial completion edges, which need not lift to the
host.  Thus Lemma 7.1 is an exact bridge tool, but it does not by itself
classify or eliminate the nonplanar no-clean-packing core.  The missing
step is a completion whose added edges have compatible realizations, or a
direct rooted-minor obstruction theorem on the original usable graph.
