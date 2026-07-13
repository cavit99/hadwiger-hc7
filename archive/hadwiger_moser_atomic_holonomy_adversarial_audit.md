# Adversarial audit: matching holonomy and the atomic star/XOR lock

## 1. Verdict on the three-state minimum-fragment collapse

The proof of Theorem 3.2 in `hadwiger_moser_matching_holonomy.md` is
mathematically sound, conditional on the already installed occurrence-level
Theorem 5.1 of `hadwiger_reserved_connector_rank_leaf.md` and the disk
curvature theorem.  In particular, the four points at which a hidden loss of
simultaneity might have occurred all survive audit.

1. **The faces are genuinely simultaneous.**  A failed normalized
   three-pair state gives a plane embedding of the same abstract
   three-connected graph (D).  Whitney uniqueness therefore lets us regard
   its portal face as a face of one fixed embedding.  Two such states omit
   different singleton labels and hence share five full portal classes.  The
   global seven-portal SDR supplies five distinct common facial vertices,
   whereas distinct faces of a three-connected plane graph meet in at most an
   edge.  The faces are equal.
2. **Three states give three different (C_5)-frames.**  After deleting the
   common pair (13), the five normalized matchings give exactly
   (05|24,05|46,06|24,06|25,25|46), without repetition.  Failure of every
   two-block packet for the state makes its displayed frame crossless.
3. **Curvature has the required relative boundary.**  Here the relative
   boundary (L=U\dot\cup\{w,a\}) in the curvature note is exactly
   (S=U\dot\cup\{1,3\}).  Since (D) is a component behind a seven-cut,
   every proper nonempty (A\subsetneq D) satisfies
   
   \[
   |N_D(A)-A|+|N_S(A)|\ge 7.
   \]
4. **Every curvature output contradicts global minimum-fragment choice.**
   A degree-seven output makes (N_G(x)) a seven-cut with singleton fragment
   ({x}); the anticomplete far shore remains after deleting (N_G(x)).
   In the triple-lock output, (D-x) is connected, the shield portal is
   (P_s={x}), and seven-connectivity forces
   
   \[
   N_G(D-x)={x}\cup(S-\{s\}).
   \]
   Thus (D-x) is a strictly smaller fragment behind an exact seven-cut.

There is one formal defect in the statement, not in the argument: an
arbitrary subset \(\mathcal F\) of the five labelled matchings does not by
itself have a "path outcome" or a "common-web branch."  The statement should
say that every member of \(\mathcal F\) is a transition state supplied by a
specified application of the matching-normalization theorem, and that the
listed packet/path alternatives refer to those applications.  With this
hypothesis made explicit, the proof is green.

## 2. Unused-colour symmetry sharpens the star/XOR lemma

The following refinement is exact and label-free.

### Lemma 2.1 (unused-colour invariant star/XOR classification)

Let \(R\subseteq\Omega\) be the colours used by a fixed boundary colouring,
put \(U=\Omega-R\), and assume \(|U|\ge2\).  Let nonempty
\(\mathcal A,\mathcal B\subseteq\Omega^2\) satisfy the hypotheses of Lemma
5.1 in `hadwiger_moser_atomic_interface_lock.md`.  Suppose in addition that
both relations are invariant under the diagonal action of every permutation
of \(U\) fixing \(R\) pointwise.  Then:

1. in the star case, the two coordinates of the singleton relation belong
   to \(R\);
2. in the XOR case, either all four values \(p,q,r,s\) in (5.2) belong to
   \(R\), or \(|U|=2\) and, after interchanging the two relations,
   
   \[
   \mathcal A={(u,u),(v,v)},
   \qquad
   \mathcal B={(u,v),(v,u)},
   \qquad U={u,v}.                         \tag{2.1}
   \]

#### Proof

If \(\mathcal A={(p,q)}\) is the singleton relation, invariance
fixes \((p,q)) under every permutation of \(U\).  Since \(|U|\ge2\), this
forces \(p,q\in R\).

Now suppose

\[
\mathcal A={(p,q),(r,s)},
\qquad
\mathcal B={(p,s),(r,q)},
\]

with \(p\ne r\) and \(q\ne s\).  If \(|U|\ge3\), any ordered pair with an
unused coordinate has an orbit of order at least three under
\(\operatorname{Sym}(U)\), whereas \(|\mathcal A|=|\mathcal B|=2\).
Consequently all four values lie in \(R\).

Let \(U={u,v}\) and let \(\tau\) interchange \(u,v\).  Invariance of
the two-point set \(\mathcal A\) says either that each of its two points is
fixed by \(\tau\), or that they are interchanged.  In the first case every
coordinate is in \(R\).  In the second case both coordinates of each point
are in \(U\), and the inequalities \(p\ne r,q\ne s\) leave precisely the
diagonal/off-diagonal pair (2.1), up to interchanging the relations. \(\square\)

For a boundary extension relation the invariance hypothesis is automatic:
apply the unused-colour permutation only inside the piece.  It fixes every
boundary colour, and an internal colour in (U) remains different from every
boundary colour.

For a normalized Moser state (13|J|K|r), exactly four colours occur on the
boundary.  Thus Lemma 2.1 reduces the unused-colour part of the XOR residue to
the single parity gadget (2.1).

## 3. Four anchors do not eliminate the parity gadget

The parity gadget is not merely an abstract relation.  It has a
seven-connected local realization satisfying every numerical and Kempe-anchor
conclusion currently available at the atomic interface.

Take the Moser boundary (S={0,\ldots,6}), and use the boundary state

\[
13\mid05\mid24\mid\{6\},                         \tag{3.1}
\]

with used colours (0,1,2,3) and unused colours (u,v).  Let

\[
X=x_1-z-x_2,
\qquad
Y=y_1y_2,
\]

and put in the two interface edges (x_1y_1,x_2y_2).  Join every vertex of
(X) to (S-\{1\}), and every vertex of (Y) to (S-\{2\}).  Finally add
an opposite helper shore (H=K_{1,4}), with every vertex complete to (S).

Because every one of (S-\{1\}) and (S-\{2\}) contains all four colours
used in (3.1), every extension of (3.1) over (X) colours its vertices only
with (u,v).  The even path forces

\[
(c(x_1),c(x_2))\in{(u,u),(v,v)}.
\]

The edge (y_1y_2) forces

\[
(c(y_1),c(y_2))\in{(u,v),(v,u)}.
\]

Hence (3.1) extends after deletion of either interface edge, but not before
deletion.  In the (x_1y_1)-deletion colouring, the sole internal
(u/v)-detour uses the retained interface edge, while for each of the four
used boundary colours γ the (u/γ)-components at (x_1,y_1) are
distinct and directly anchored at (S).  The symmetric assertion holds for
the other deletion.  Thus the lower bound of four anchored colours is met
with equality and produces no exchange.

The graph is seven-connected.  Indeed, after deleting at most six vertices,
some boundary vertex survives.  If a surviving boundary vertex is outside
{1,2}, it is adjacent to every surviving shore vertex and both helper
vertices.  If only vertices from {1,2} survive on the boundary, at
least five boundary vertices were deleted, so at most one nonboundary vertex
was deleted.  Vertex 2 joins the whole (X)-side, vertex 1 joins the whole
(Y)-side, and the two intact interface edges join the sides; the helper
shore meets both.  If only one of 1,2 survives, all six deleted vertices are
boundary vertices and the same conclusion follows through the intact
interface.  Deleting all seven boundary vertices disconnects the graph, so
its connectivity is exactly seven.

Moreover (D=X\cup Y) is a minimum fragment in this graph.  It has order
five and boundary exactly (S).  Every connected proper subset of the
five-cycle (D=x_1zx_2y_2y_1x_1) has external neighbourhood of order at
least eight: a subset contained in one row sees six boundary vertices and at
least two cycle neighbours, while a mixed subset sees all seven boundary
vertices and at least one cycle neighbour.  A proper connected subset of the
full helper shore already sees all seven boundary vertices and at least one
shore neighbour.  Finally, the verifier checks directly that no connected
set of order below five anywhere in the graph has external neighbourhood of
order seven.  Hence no smaller fragment lies behind a seven-cut.

The dependency-free verifier is
`moser_atomic_xor_local_probe.py`.  This construction is **not** claimed to
be (K_7)-minor-free or six-minor-critical.  Its role is sharper: it proves
that seven-connectivity, minimum-fragment choice, the near-full rows, the
atomic equalities, unused colour symmetry, and the four-anchor conclusion do
not by themselves rule out XOR.  Any final elimination must use an additional
global input, in particular (K_7)-minor exclusion and the packet-deficient
geometry of the opposite accepting shore.

In fact the local minor-transition hypothesis can also be saturated.  The
five vertices of (D) induce the odd cycle

\[
x_1zx_2y_2y_1x_1,
\]

and every one of them sees all four colours used on the boundary.  Thus its
local list is exactly ({u,v}).  Deleting any edge turns this cycle into a
bipartite path, and contracting any edge turns it into a bipartite four-cycle.
Consequently the same exact boundary state extends every one-edge deletion
and every one-edge contraction internal to (D).  The parity cycle is the
literal fixed-state critical kernel, not just a witness for the two interface
deletions.

What the construction cannot satisfy is (K_7)-minor exclusion.  The verifier
checks the following explicit seven branch sets (with helper-star vertices
numbered 12 through 16):

\[
\{0,15\}\mid\{1,10\}\mid\{2,4,12\}\mid\{3\}
\mid\{5,16\}\mid\{6,7,8,9,11,14\}\mid\{13\}.
\]

They are disjoint, connected, and pairwise adjacent.  Hence even the full
fixed-state one-step transition condition does not kill XOR; the remaining
proof must use packet deficiency of the opposite accepting shore together
with (K_7)-minor exclusion.

## 4. Exact next target

After Lemma 2.1, the atomic residue has only three genuinely different
forms:

1. a star whose rigid terminal colours are boundary-used;
2. an XOR using four boundary-used colours;
3. the pure two-unused-colour parity gadget (2.1).

The third is saturated by the four anchored colours.  Therefore a proposed
"anchors alone imply a split" lemma is false.  The viable next statement is
a **parity-transition lemma**: in a minimum (K_7)-minor-free
six-minor-critical shore, an internal deletion or contraction cannot preserve
the diagonal/off-diagonal relation (2.1) while preserving both almost-full
portal rows.  Proving this would use precisely the global hypothesis absent
from the construction above and would close the hardest XOR branch without
further Moser-labelled enumeration.
