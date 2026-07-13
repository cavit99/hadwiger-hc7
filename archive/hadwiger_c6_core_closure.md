# Complete closure of the \(C_6\dot\cup K_1\) full-shore core

> **Retraction notice.** Theorem 1.1 is not established. The
> orientation-free SPQR step in Section 4 assumes that reflecting a leaf
> preserves the face containing four portal classes. This is false.
> The explicit rank-two/rank-two counterexample and corrected dependency
> boundary are in `hadwiger_c6_closure_spotcheck_counteraudit.md`.
> The three-connected branch and the elimination of an already-present
> cycle-type S-leaf remain valid; the arbitrary nontrivial SPQR-tree
> residue is open.

## 1. Theorem

### Theorem 1.1

There is no seven-connected, \(K_7\)-minor-free, non-six-colourable graph
which satisfies

\[
       \alpha(G[N(x)])\le d_G(x)-5\quad\text{for every }x\in V(G),
\]

and has boundary

\[
 S=\{c_0,\ldots,c_5,z\},\qquad
 \overline{G[S]}=c_0c_1\cdots c_5c_0\ \dot\cup\ K_1,
\]

and two anticomplete connected components \(D_1,D_2\) of \(G-S\), each
full to \(S\).  In particular, the conclusion applies when \(G\) is
seven-contraction-critical: non-six-colourability and the displayed local
inequality are then automatic, by Dirac's theorem.

Equivalently, inside the counterexample-derived two-full-shore equality
cell, the sole six-edge boundary type left by the relaxed-frame atlas,
\(C_6\dot\cup K_1\), is eliminated.  This is not asserted for arbitrary
seven-connected minimum-degree-seven graphs.

## 2. Previously audited inputs

We use the following results, each with its own proof and verifier.

1. **Frame ownership.**  Every one of the six complementary frames is
   crossed in exactly one shore; opposite frames have the same owner.
   Hence one shore \(D\) owns at least two opposite frame pairs.
2. **Linkage exclusions.**  Neither shore has an antipodal two-linkage
   \(e_i\mid e_{i+3}\), or a nonidentity even-to-odd three-linkage.
3. **Internal locks.**  A nonsingleton shore is two-connected, every
   shore two-cut has exactly two components, and a shore-degree-two
   vertex has the exact lock

   \[
   S-N_S(x)=N_{C_6}(v_x),\qquad S-N_S(D-x)=\{v_x\}.       \tag{2.1}
   \]

4. **Portal transversal.**  The six portal sets of the high-owner shore
   have an SDR.  Hall's theorem reduces failure to orders four or five,
   and the complete order-four/order-five certificates eliminate those
   finite cases.
5. **Bare webs.**  For each antipodal demand, the generalized Two Paths
   Theorem gives a same-vertex web completion.  Seven-connectivity kills
   every clique inserted behind a facial triangle, so the shore is
   planar and the four full portal sets lie on one face after deleting
   the artificial frame terminals.

These are proved in

* `hadwiger_c6_opposite_crossing_dichotomy.md`,
* `hadwiger_c6_three_linkage_exclusion.md`,
* `hadwiger_c6_two_piece_locks.md`,
* `hadwiger_c6_portal_multiplicity_closure.md`, and
* `hadwiger_c6_simultaneous_prism_web.md`.

## 3. Three-connected shores

If the high-owner shore \(D\) is three-connected, Whitney uniqueness
synchronizes the three bare-web embeddings.  Their portal faces either
coincide or form the three faces of a subdivided triangular prism.
Seven-connectivity and minimum degree eliminate the prism alternative,
so all six portal sets lie on one face.

The exact circular obstruction theorem then applies.  An SDR has one of
six cyclic orders forced by the three antipodal exclusions.  Facial arcs
realize exactly one opposite frame pair in each order, while high
ownership requires two.  The full disk rule, including collapsed portal
occurrences, makes a second pair impossible.  Thus \(D\) is not
three-connected.  This is Theorem 1.1 of
`hadwiger_c6_threeconnected_highowner_closure.md` and Theorem 1.1 of
`hadwiger_circular_obstruction_frame_theorem.md`.

## 4. Orientation-free SPQR leaf reduction

Take a leaf edge of a nontrivial reduced SPQR decomposition of \(D\).
Use any one of the three bare four-web embeddings.  Reflecting one side
of the leaf separation reverses one contiguous block of the four
alternating portal representatives.  A block containing exactly two
representatives destroys alternation.  Since this holds for every SDR,
the basis-intersection interval property of the four-set transversal
matroid implies that one of the two separation interiors has portal rank
at most one.

König's theorem gives a one-vertex cover of its portal incidences.  If
the cover is a boundary label, the interior is separated in \(G\) by
\(p,q,z\), the two omitted labels, and that label.  If the cover is a
shore vertex \(x\), every component after deleting \(x\) is separated by
\(p,q,z,x\) and the two omitted labels.  Both cuts have order at most
six.  Seven-connectivity therefore forces the low-rank interior to be
the singleton \(\{x\}\).  It has shore neighbours exactly \(p,q\) and
the exact lock (2.1).

This conclusion is deliberately orientation-free.  The earlier claim
that the singleton must always lie on the selected leaf-node side is
false for a canonical R--P--S decomposition and is not used.

Since \(d_G(x)=7\), Dirac's inequality gives
\(\alpha(N_G(x))\le2\).  Both \(p,q\) miss the unique portal label
\(v_x\), so \(pq\in E(D)\).  Hence the separation has the three
\(p\)-\(q\) bridges

\[
 pxq,\qquad pq,\qquad\text{the complementary bridge}.
\]

Canonical SPQR reduction introduces a P-node for these parallel bridges
and an S-node leaf whose real path is \(pxq\).  Thus every nontrivial
SPQR tree would contain a cycle-type leaf.

## 5. Elimination of a cycle-type leaf

Let the S-leaf have real path \(px_1\cdots x_rq\).

If \(r\ge2\), then at \(x_1\) the vertices
\(p,x_2,v_{x_1}\) are pairwise nonadjacent: the first two are
nonadjacent in the chordless S-torso, and both miss the unique portal
label of \(x_1\).  They form an independent triple in \(N_G(x_1)\),
contrary to Dirac.  Hence \(r=1\); write \(x=x_1\).  The same argument
forces \(pq\in E(D)\).

Normalize \(v_x=c_0\), let \(B\) be the other component of
\(D-\{p,q\}\), and put

\[
 A=\{c_2,c_4\},\qquad T=\{c_3\}.
\]

The exact connected-split atlas leaves only cut rows of type
\(A\) or \(T\), with an optional \(z\)-contact.  A seven-fan from the
degree-seven vertex \(x\) to \(S\) uses the five direct boundary edges
and gives two internally disjoint arms through \(p,q\) to \(c_1,c_5\),
one each.  If either cut vertex is broad (type \(A\)), these arms lift
one of the explicit models

\[
\begin{array}{c}
\{p,c_0,c_2\},\ \{q,x,c_4\},\
\{c_1\},\{c_3\},\{c_5\},\{z\},H,\\[1mm]
\text{or}\qquad
\{p,c_0,c_4\},\ \{q,x,c_2\},\
\{c_1\},\{c_3\},\{c_5\},\{z\},H,
\end{array}                                        \tag{5.1}
\]

after swapping \(p,q\) if needed.  These are \(K_7\)-models.

It remains only that both cut vertices are thin:

\[
 N_S(p),N_S(q)\in\bigl\{\{c_3\},\{c_3,z\}\bigr\},\qquad
 \{c_1,c_2,c_4,c_5\}\subseteq N_S(B).             \tag{5.2}
\]

Apply the bare web for the absent antipodal linkage
\(c_0c_1\mid c_3c_4\).  It embeds

\[
 J=G[D\cup\{c_0,c_1,c_3,c_4\}]
\]

with its four terminals cofacial.  Contract \(B\) to \(b\) and add a
cofacial apex \(r\).  The augmented quotient contains a subdivision of
\(K_{3,3}\) with sides

\[
 \{x,b,c_3\},\qquad\{p,q,c_4\},
\]

where the ninth edge is the path \(c_3rc_4\).  The other eight edges are
\(xp,xq,xc_4,bp,bq,bc_4,c_3p,c_3q\).  This contradicts planarity.

The complete leaf proof and exact certificates are in
`hadwiger_c6_spqr_cycle_leaf.md`.

## 6. Conclusion and audit boundary

A high-owner shore is impossible when three-connected by Section 3.  If
it is not three-connected, Section 4 forces an S-leaf and Section 5
eliminates that leaf.  This proves Theorem 1.1.

The proof does **not** use the retracted assertion that all actual SPQR
leaf sides are singletons, nor the conditional monotone rope path.  Its
only computer-assisted finite inputs are the archived portal bases and
the exact one-ear contact frontier; all unbounded geometry is handled by
the bare-web, transversal-rank, fan, and Kuratowski arguments.
