# Adversarial audit: atomic surplus and rooted-state kernels

## Verdict

**GREEN for Theorems 2.1, 3.1, 4.1 and 5.1 after two scope repairs in
the source note.**  The minimum-fragment inequality, the global use of a
rooted operation, equality-partition gluing, fixed-root labelled-minor
well-quasi-ordering, finiteness of state-minimal kernels, and the
private-state component bound are all valid.

The original draft made two statements stronger than its proof:

1. it said that \(N_G(X)\) separates \(X\) from \(Y\), although it may
   delete all of \(Y\); the untouched far side is instead any other
   component of \(G-S\);
2. it passed from a globally minimum fragment to the two-full-shore
   cyclic-hull setting without requiring the cut defining that fragment
   to have exactly two components.

Both are now corrected in `hadwiger_exact_cut_atomic_kernel.md`.  The
second correction is substantive: an atomic cut with at least three
components remains outside the two-shore cyclic-hull theorem.

## 1. Minimum-fragment theorem

Let \(D\) be a minimum fragment behind a \(k\)-cut \(S\), and let
\(D=X\dot\cup Y\) be a nontrivial connected split.  Because different
components of \(G-S\) are anticomplete,

\[
N_G(X)=N_S(X)\dot\cup N_Y(X).
\]

There is an original component \(D'\ne D\) of \(G-S\), and \(D'\) is
disjoint from this neighbourhood.  Hence \(N_G(X)\) separates \(X\)
from \(D'\), so it has order at least \(k\).  If it has order exactly
\(k\), then \(X\) is itself a component behind a \(k\)-cut and
\(|X|<|D|\), contradicting minimum-fragment choice.  Integrality gives
the asserted lower bound \(k+1\).  The same proof works for \(Y\).

The proof does not need a vertex of \(Y-N_Y(X)\).  Indeed, in
\(K_k\vee(K_2\dot\cup K_2)\), the central \(K_k\) is a \(k\)-cut and
either \(K_2\) is a minimum fragment.  Splitting one such edge into its
two endpoints gives \(Y=N_Y(X)\).  This is an explicit counterexample
to the discarded wording, but not to the corrected theorem: the
neighbourhood has order \(k+1\).

The no-descent corollary is valid only when the local theorem's tight
outcome is exactly the neighbourhood of a proper connected part of the
chosen minimum fragment.  It does not exclude an unrelated exact cut
elsewhere.

Finally, minimum-fragment choice does not force a two-component cut.
The graph \(K_k\vee\overline{K_3}\) is \(k\)-connected and its only
order-\(k\) separating set is the central \(K_k\); deletion leaves three
full singleton components.  Thus no argument based only on Theorem 2.1
may replace an atomic multi-component cut by the two-shore cyclic-hull
configuration.

## 2. Rooted operations really are global minor operations

For a component \(C\) of \(G-S\), every non-root vertex in
\(H=G[S\cup C]\) has no neighbour in another component of \(G-S\).
Consequently:

* deleting an internal vertex or edge affects no other side;
* contracting an internal branch set changes no adjacency between two
  untouched sides;
* contracting a branch set containing root \(s\) preserves every old
  edge from \(s\) to every other component, because the labelled root
  remains in that branch set;
* a new root-root edge not in \(J=G[S]\) can be deleted, while every
  edge of \(J\) is already present between the two root branch sets and
  can be retained.

Every proper rooted operation reduces the vertex count or the simple
edge count globally, so the resulting graph is a proper minor of \(G\).
There is therefore no hidden replacement step in Theorem 3.1.

This fails if one merely substitutes an abstract state-equivalent
gadget.  For example, with two nonadjacent roots and palette two, paths
of lengths two and four induce the same endpoint-equality state, but the
longer path is not a minor of the shorter one.  State equivalence
preserves a colouring question under gluing; it does not make the
substitution a minor operation to which minor-criticality applies.

## 3. Equality partitions are exactly enough for colour gluing

Suppose two proper \(r\)-colourings induce the same labelled equality
partition \(\Pi\) on \(S\).  Distinct blocks of \(\Pi\) receive distinct
colours in each colouring.  The bijection taking the colour of each
block in the first colouring to the colour of that block in the second
extends to a permutation of the \(r\)-colour palette.  After applying
it, the two colourings agree pointwise on \(S\), so they glue.

Labels cannot be forgotten.  With three pairwise nonadjacent roots and
palette two, one boundaried bipartite gadget can force the partition
\(12|3\), while another can force \(13|2\): use internally subdivided
paths of prescribed parity between the roots.  Both partitions have
the same unlabelled block sizes \(2+1\), but they are not compatible.

Nor is preservation of just one state enough.  For two nonadjacent
roots and palette two, a length-two path admits only the `same` state,
whereas two isolated roots admit `same` and `different`.  An opposite
odd path admits only `different`.  Thus the two possible first sides
share the state `same`, but only the isolated-root side glues to the
odd-path side.  The full labelled extension family in (3.1) is the
correct invariant.

In fact Theorem 3.1 gives slightly more than inequality of the two state
families.  Colour the global proper minor obtained from any proper
rooted minor \(H'\).  Its boundary state is realized by \(H'\) and by
every untouched side; it cannot be realized by \(H\), or it would colour
\(G\).  Hence every proper rooted operation exposes at least one genuinely
new compatible state, though it may also destroy old states.

## 4. Fixed-root labelled-minor WQO

Use a finite antichain of vertex labels: one unique label for each root
and one common non-root label.  In the labelled Graph Minor Theorem's
branch-set relation, a target root labelled \(i\) must have in its branch
set the unique source vertex labelled \(i\).  All target roots occur and
branch sets are disjoint, so no source root can be deleted, put in a
non-root branch set, or swallowed by another root branch set.  Non-root
vertices may still be absorbed into root branch sets, exactly as the
rooted relation permits.

Restricting to graphs whose induced root graph is the fixed graph \(J\)
does not destroy comparability.  If two members of this subclass are
comparable in the labelled relation, every edge of \(J\) already joins
the corresponding source roots and survives between their branch sets;
surplus root edges created by contractions may be deleted.  Thus the
comparison is an allowed \(S\)-rooted minor with root graph exactly
\(J\).

For each extension family \(\mathcal F\), its rooted-minor-minimal
members form an antichain.  Labelled WQO makes this set finite.  There
are finitely many labelled equality partitions of \(S\), hence finitely
many possible families \(\mathcal F\), so their union is finite.  By
Theorem 3.1 every component side in an \(r\)-minor-critical graph is one
of these minimal members.  Theorem 4.1 follows.

This is only an existence result.  It supplies neither a usable bound
nor a finite certificate that has been enumerated.  Indeed, ordinary
unlabelled Graph Minor WQO already implies that for fixed \(r\) there
are only finitely many globally \(r\)-minor-critical graphs; the rooted
argument adds the exact side-state interpretation but does not make the
bound constructive.

## 5. Private-state component bound

Let \(\mathcal F_i\) be the state family of component \(C_i\).  Their
total intersection is empty, since \(G\) is not \(r\)-colourable.  After
deleting \(C_i\), minor-criticality gives

\[
\phi_i\in\bigcap_{j\ne i}\mathcal F_j.
\]

If \(\phi_i\in\mathcal F_i\), it lies in the total intersection, so
\(\phi_i\notin\mathcal F_i\).  If \(i\ne j\) and
\(\phi_i=\phi_j\), then the first witness lies in \(\mathcal F_j\),
whereas the second does not, a contradiction.  Hence the private states
are pairwise distinct and the number of components is at most
\(|\Omega_r(J)|\).  For one component the empty intersection is the
universe \(\Omega_r(J)\), as now stated in the source note.

Combining this injection with the finite size of every rooted-state
kernel proves (5.1) and Corollary 5.2.

## 6. Exact remaining scope

The audited results prove a non-effective finite bound for a fixed
palette and fixed boundary, and they remove nested neighbourhood cuts
inside a chosen minimum fragment.  They do **not**:

1. colour the final surplus torso;
2. enumerate the finite kernels;
3. convert an atomic cut with at least three components into a two-shore
   cut;
4. show that every exact cut exposed by an unrelated construction is
   nested inside the chosen fragment; or
5. prove HC7 or the general Hadwiger conjecture.

Within these boundaries, the four displayed theorems are sound.
