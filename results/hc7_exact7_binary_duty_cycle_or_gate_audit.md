# Hostile independent audit: binary-duty cycle or gate

Audited file:

* `results/hc7_exact7_binary_duty_cycle_or_gate.md`.

## Verdict

**GREEN after the explicit attainment, same-shore-packet, and tiny-order
scope repairs.**

The substantive graph theory is sound:

* Theorem 1.1 is GREEN.  The Humeau--Pous web theorem is used with its
  exact same-vertex, edge-completion conclusion; four-connectivity removes
  every inserted clique; deletion of completion edges keeps the frame
  terminals cofacial; Whitney uniqueness and the facial-intersection lemma
  synchronize the three frames; and the resulting word is exactly
  `A B D A B D`.
* Corollary 2.1 is GREEN as an **internal separator of the actual shore
  component**.  The small set `X` is a vertex cut of `C`, not a cut of
  `G`; the actual global separation boundary for a lobe `K` is
  `N_G(K)=N_C(K) union N_S(K)`.
* Corollaries 2.2 and 2.3 are GREEN.  The source now says explicitly that
  the completing full packet lies in the same open shore as `C`, is
  vertex-disjoint from `C union S`, and that `Pi` was returned by a legal
  proper-minor operation on the opposite shore.  Their exact order-seven
  descent is literal.
* Lemma 3.1 is GREEN.  Its Hall separator is valid for every nonempty
  subfamily and the hypothesis `|C|>=m` is exactly what guarantees a
  surviving vertex of `C`.
* Corollary 3.2 is GREEN under its now-explicit attained-state hypothesis.
  It concludes only that the two rich components cannot both be
  four-connected.  The former unsupported inference from this fact to an
  internal cut in an arbitrarily tiny component has been removed.

Those qualifications are part of the current source, not merely audit
recommendations.

The Moser conclusion is strategically redundant: the already GREEN
`results/hc7_exact7_moser_two_component_closure.md` closes the entire
two-component pure-Moser branch.  The reusable new content is Theorem 1.1
and the exact gate/descent package, not another Moser closure.

## 1. Exact Two Paths/web audit

For the tuple

\[
                         (a_0,b_0,a_1,b_1),
\]

a crossing in the sense of Humeau--Pous is precisely a pair of
vertex-disjoint `a_0-a_1` and `b_0-b_1` paths.  Thus the missing `A,B`
linkage makes the tuple crossless.  Theorem 1.5 of Humeau--Pous says that
adding edges, but no vertices, completes `J` to a web with this frame.

In their Definition 1.2, every clique-cell vertex has neighbours only in
its own clique and the supporting rib triangle `T`.  A frame has four
distinct rib vertices, so at least one frame vertex is outside `T`.  If a
cell were nonempty, deleting `T` would disconnect one of its vertices from
that frame vertex already in the spanning edge-subgraph `J`.  This
contradicts four-connectivity.  Because the completion is same-vertex,
there is no possibility that a nonempty cell consists only of newly added
vertices.  Hence every vertex of `J` is a rib vertex and `J` is planar.

Deleting completion edges only merges faces.  All four frame vertices
remain incident with the merged outer face.  Four-connectivity implies
two-connectivity, so its boundary is a cycle, and the inherited cyclic
order is `a_0,b_0,a_1,b_1`.  This justifies `F_AB`; the same argument gives
`F_AD,F_BD`.

The nonadjacency step is correct.  If `a_0a_1` were an edge,
four-connectivity makes `J-{a_0,a_1}` connected, so it contains a
`b_0-b_1` path disjoint from that edge.  This is the forbidden linkage.
The same applies to `B,D`.

Whitney uniqueness should technically be described as uniqueness of the
spherical embedding (a plane embedding still has a choice of outer face),
but this is editorial only.  In a three-connected plane graph, two
distinct facial cycles intersect in at most one edge.  Therefore two such
cycles cannot both contain the same nonadjacent pair.  It follows that

\[
                         F_{AB}=F_{AD}=F_{BD}.
\]

On this common cycle every two duty pairs alternate.  Between the two
`A` occurrences there is one `B` and one `D` on either arc; alternation of
`B,D` forces the same order on both arcs.  This gives `A B D A B D` up to
the stated symmetries.  No planarity or terminal-independence hypothesis
has been smuggled into the web theorem.

## 2. Corollary 2.1: what is and is not an actual separator

If `C` is not four-connected, its six distinct terminals ensure
`|C|>=6`, so a cut `X` of order at most three genuinely leaves at least
two sides.  For a component `K` of `C-X`, componenthood of `C` in the
open shore gives

\[
 N_G(K)=N_C(K)\mathbin{\dot\cup}N_S(K),
 \qquad N_C(K)\subseteq X.
\]

The old opposite open shore is nonempty and anticomplete to `K`, so
`N_G(K)` is a literal separator of `G`.  Seven-connectivity gives

\[
 7\le |N_G(K)|\le |X|+|N_S(K)|,
\]

which is exactly the support bound in (2.1).

The terminology must remain precise: `X` is an actual cut inside `C`, but
it need not separate `K` from the rest of `G`, because `K` still contacts
literal vertices of `S`.  No later step in the note treats `X` alone as a
global adhesion, so the proof is safe.

## 3. Exact three-gate certificate and descent

Let `C` be three-connected and `X` a three-cut.  Every component `K` of
`C-X` meets every member of `X`: otherwise the other two members of `X`
separate `K` from another component.  Hence

\[
                           N_C(K)=X.                    \tag{A.1}
\]

If distinct lobes `K,K'` contain complete, distinctly named duties
`B_i,B_j`, then for any `x in X` the carriers `K` and `K' union {x}` are
connected, disjoint, and adjacent.  After adjoining their boundary blocks,
the literal `B_i-B_j` edge supplies any needed representative adjacency;
an `S`-full packet in the same shore and disjoint from `C union S` funds
the third duty; and the
neighbours from `c` make the four state representatives a clique.  This is
the standard exact reflection because `Pi` is attained on the opposite
shore.  Both hypotheses are literal in the current statement.

For a dutyless lobe, seven-connectivity and (A.1) give
`|N_S(K)|>=4`.  Avoiding a complete one of the three disjoint pairs permits
at most one member of each pair.  Thus four boundary neighbours are possible
only as

\[
 N_S(K)=\{c\}\cup\{\hbox{one member of each }B_i\}.
\]

There is no hidden fifth vertex: the seven boundary vertices are exactly
the three pairs plus `c`.  Consequently

\[
 \Omega_K=X\cup N_S(K)=N_G(K),\qquad |\Omega_K|=7.
\]

Every literal member of `Omega_K` has a neighbour in connected `K`, so
`K` is `Omega_K`-full.  Deleting `Omega_K` leaves both `K` and the old
opposite open shore, proving that this is a genuine exact-seven
separation.

The reuse of the packet-packing theorem in Corollary 2.3 is exact.  Every
component of the new opposite open shore is `Omega_K`-full, since missing
one boundary vertex would leave a neighbour set of order at most six while
`K` remains on the other side.  The packing vectors are therefore, up to
orientation, `(1,1),(1,2),(1,3)`, and the audited adaptive theorem closes
`(1,3)`.  Because `X` is a cut, another component of `C-X` exists, so the
new shore `K` is strictly smaller than `C`.  The note correctly does not
claim that the binary attained state survives this descent.

## 4. Portal matching

Let `A subseteq S`, `|A|=m`, and consider its bipartite incidence with
`C`.  If a nonempty `B subseteq A` violated Hall, then

\[
 |N_C(B)|\le |B|-1<|B|\le m\le |C|,
\]

so `C-N_C(B)` is nonempty.  The set

\[
                         N_C(B)\cup(S-B)
\]

has order at most six.  A component of `C-N_C(B)` has no edge to the
surviving boundary set `B`, and componenthood of `C` excludes every
open-shore escape.  The nonempty opposite shore remains.  This is a valid
separator contradiction.  Hall therefore gives distinct portals for any
prescribed `m<=7` boundary vertices.  The statement is also already a
standard consequence of the frozen exact-seven shore machinery, so it
need not be advertised as a separate novelty.

## 5. Conditional Moser composition

Assume now all frozen counterexample hypotheses, the actual `(1,2)`
separation, the Moser boundary, the two rich exterior components `C_1,C_2`,
the disjoint thin full packet `T`, **and** a legal thin-shore operation
which returns exactly

\[
                         23\mid14\mid05\mid6.           \tag{A.2}
\]

Under these hypotheses the proof is correct.

If a four-connected `C_i` has order five, it is `K_5`.  Five distinct
portal matches enlarge its singleton clique bags; `C_{3-i}` and `T`, each
with one remaining distinct boundary anchor, give the last two bags.
Fullness supplies all cross-adjacencies, including adjacency of those last
two bags through either one's contact to the other's anchor.  This is a
literal `K_7`.

Otherwise both four-connected components have order at least six, so Hall
selects six distinct duty portals in each.  A two-duty linkage in either
component reflects (A.2).  If all three linkage pairs fail, Theorem 1.1
gives an alternating cycle in each component.  The audited cyclic-duty
theorem leaves only the exceptional literal orbit

\[
                         2,4,5,3,1,0.
\]

There is no orientation mismatch here.  The two exceptional flip vectors
`011` and `100` differ by a rotation of three; reversal and rotation of
each cycle may be chosen independently.  The Moser automorphism used to
merge some of the nonexceptional orbits is not needed to align the two
exceptional cycles.  Hence the audited cyclic-packet completion applies
with `C_1,C_2,T` and returns a literal `K_7`.

What does **not** follow is automatic attainment of (A.2).  Fullness of a
thin packet, or the star-contraction trace lemma by itself, does not force
that particular three-pair equality state.  The current Section 3 preamble
and corollary repeat the legal-attainment hypothesis and therefore avoid
that unconditional reading.

The draft formerly inferred an internal cut from the mere fact that one
component is not four-connected.  This was unsafe for components of order
at most four and could not invoke Corollary 2.1 without six terminals.  The
current Corollary 3.2 has deleted that inference and now states only its
proved four-connectivity exclusion.

## 6. Falsification boundary

No counterexample was found to Theorem 1.1 or to the exact gate descent.
The expected sharp obstruction at connectivity three is real: a web with a
nonempty clique inserted in a facial triangle is three-connected,
crossless for its frame, and nonplanar.  Thus four-connectivity is doing
essential work, and the theorem cannot be weakened by simply deleting it.

The only hostile failures located were ones of quantifier/scope, not
geometry: treating the fixed Moser partition (A.2) as automatically
attained, allowing the completing packet to overlap the lobe component, or
inferring a cut inside a tiny component would each overstate the result.
All three have been repaired in the current source.
