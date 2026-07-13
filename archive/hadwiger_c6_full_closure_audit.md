# Independent audit and repair of the (C_6\dot\cup K_1) closure

> **Retraction notice.** The proposed repair is incomplete. Its
> rank-four leaf argument assumes that a portal-cofacial face is
> preserved by an SPQR reflection. The counterexample in
> `c6_rank_four_leaf_counterexample.py` has a cofacial alternating
> portal set, no prescribed linkage, and portal ranks \((2,2)\) across
> the SPQR edge. See
> `hadwiger_c6_closure_spotcheck_counteraudit.md`.

## 1. Verdict

The path classification stated as Theorem 6.1 in
`hadwiger_circular_obstruction_frame_theorem.md` is **false as written**.
The local cycle-leaf elimination in
`hadwiger_c6_spqr_cycle_leaf.md`, including its bare-web and
(K_{3,3}) argument, is sound.  Replacing the false orientation step by
the orientation-free singleton-to-S-leaf lemma below repairs the logical
chain and removes both the R-leaf and two-node loopholes.

The repair does not need the SPQR tree to be a path and does not use the
(L/M/R) transition analysis.

## 2. Precise flaw in the old path theorem

The rank-four flip argument says that for a leaf separation
({p,q}), **one** of its two interiors has portal transversal rank at
most one.  Seven-connectivity then makes that low-rank interior a
singleton.  It does not identify which orientation is low-rank.

The assertion that the complement of a leaf cannot have one-vertex
interior when its SPQR subtree has at least two nodes is false.  Take
three (p)-(q) bridges:

1. a real edge (pq);
2. a singleton ear (pyq); and
3. a nontrivial three-connected (p)-(q) bridge.

The reduced canonical tree is

[
 R-P-S.
]

For the R-leaf edge, the complementary (P+S) subtree has interior
({y}).  Thus the rank argument may select the complement, while the
actual R-leaf remains nontrivial.  This directly refutes the proof of
the old Theorem 6.1 and its claim that every actual leaf is singleton.

## 3. Audited orientation-free rank conclusion

The part of the rank argument needed below is valid.

Fix one forbidden antipodal linkage and its four full portal classes.
The bare-web theorem gives a plane embedding of (D) in which all four
classes lie on one facial cycle.  They have a four-element SDR by
restriction of the audited six-element SDR.

Flip a canonical SPQR leaf through its separation pair.  The internal
representatives on its exposed facial arc form a contiguous block.  A
four-point alternating order remains alternating after a block reversal
only when the block has size (0,1,3), or (4), never size (2).
The images of the four-class SDRs are bases of a rank-four transversal
matroid, and their intersection sizes with the leaf interior form an
integer interval.  Therefore one side of the separation has portal
rank at most one for the four represented classes.

If its incidences are covered by one represented boundary label, its
neighbourhood is contained in

[
 {p,q,z}cup{	ext{two omitted labels}}
             cup{	ext{one represented label}},                 	ag{3.1}
]

of order at most six.  If they are covered by one shore vertex (x),
then every component after deleting (x) has neighbourhood contained
in

[
 {p,q,z,x}cup{	ext{two omitted labels}},                      	ag{3.2}
]

again of order at most six.  Seven-connectivity excludes (3.1) and
excludes (3.2) unless the selected interior is the singleton
({x}).  Hence:

> **Orientation-free leaf conclusion.**  For every canonical leaf edge,
> at least one of its two interiors is a singleton degree-two shore
> vertex.

This is all that should be cited from the SPQR rank step.

## 4. Singleton side forces an actual S-leaf

### Lemma 4.1 (orientation-free singleton-to-S-leaf)

Let a proper two-separation of (D) have separator ({p,q}) and one
interior ({x}).  Under the audited degree-two portal lock and Dirac
neighbourhood bound:

1. (pqin E(D)); and
2. the canonical SPQR tree has a leaf S-node whose real path is
   (pxq).

### Proof

Two-connectivity gives

[
 N_D(x)={p,q}.
]

The exact degree-two lock supplies a label (v_x) with

[
 S-N_S(x)=N_{C_6}(v_x),qquad
 S-N_S(D-x)={v_x}.                               	ag{4.1}
]

Thus (x) has five boundary neighbours and two shore neighbours, so
(d_G(x)=7), while (p,qin D-x) both miss (v_x).  If (pq) were
absent, then (p,q,v_x) would be an independent triple in (N_G(x)),
contrary to

[
 alpha(G[N(x)])le d_G(x)-5=2.
]

Hence (pq) is an edge.

The separation pair now has three distinct (p)-(q) bridges: the
ear (pxq), the real edge (pq), and the nonempty complementary side.
In a reduced SPQR decomposition these are represented by a P-node.  Its
ear edge is virtual and is adjacent to the S-node with skeleton triangle
(pxq); the other two real edges of that S-node are (px,xq).  This
S-node has only that one virtual edge, so it is a leaf. (square)

The proof is independent of whether ({x}) was the originally named
leaf side or its complement.  In particular it handles the explicit
(R-P-S) counterexample to the old path argument.

## 5. Audit of the cycle-leaf web elimination

The following four points in Sections 6--7 of
`hadwiger_c6_spqr_cycle_leaf.md` survive adversarial checking.

### 5.1 Terminal-essentiality

Put

[
 J=G[Dcup{c_0,c_1,c_3,c_4}].
]

If a component (C) of (J-X), (|X|le3), contains none of the four
listed terminals, then (Csubseteq D), even when it contains (p) or
(q).  The only possible neighbours omitted from (J) are
(c_2,c_5,z); the opposite shore is anticomplete to (D), and the
original degree-seven apex has no neighbour in (D).  Hence

[
 N_G(C)subseteq Xcup{c_2,c_5,z},qquad |N_G(C)|le6.             	ag{5.1}
]

This separates (C) from the opposite shore and contradicts
seven-connectivity.  Thus the terminal-essentiality assertion (6.2) is
correct.

### 5.2 Exact Two Paths/web consequence

The no-linkage hypothesis in (J) is exactly the absence of the
antipodal (e_0\mid e_3) linkage: neither path can use an endpoint of
the other internally, and (c_2,c_5,z) are absent from (J).

Apply the cited same-vertex web form of the Two Paths Theorem to an
edge-maximal no-linkage supergraph.  Its four terminals belong to the
planar foundation.  Any nonempty clique inserted behind a facial
triangle has terminal-free interior; deleting its at most three
attachment vertices contradicts (5.1).  Therefore every insertion is
empty and (J) itself has a plane embedding with the four terminals on
one face.  This use is conditional only on the cited standard web
theorem, not on an unstated stronger connectivity hypothesis.

### 5.3 Cofaciality after contraction

The body (Bsubseteq D) is connected and disjoint from the four
terminals.  Contract a spanning tree of (B) in the plane embedding.
The image of the common face remains incident with all four untouched
terminals; deleting other edges only merges faces.  Hence adding a new
vertex (r) in that face adjacent to all four terminals preserves
planarity.

### 5.4 Displayed (K_{3,3}) subdivision

After the contraction, the claimed bipartition is

[
 {x,b,c_3}quad\bigm|quad{p,q,c_4}.
]

Its nine cross-connections are

[
egin{array}{lll}
xp,&xq,&xc_4,\\
bp,&bq,&bc_4,\\
c_3p,&c_3q,&c_3rc_4.
end{array}
]

They have pairwise disjoint interiors; only the last edge is subdivided,
by (r).  All are guaranteed by the double-thin contact rows.  Thus the
augmented graph contains a genuine subdivision of (K_{3,3}),
contradicting its planar embedding.

## 6. Repaired closure chain and dependencies

The (C_6\dot\cup K_1) boundary core is closed subject to the following
previously audited inputs.

1. **Frame ownership.**  Every frame has a unique shore owner, opposite
   frames have the same owner, and one shore owns at least two opposite
   frame pairs.
2. **Finite multiplicity base and Hall.**  Orders four and five are
   eliminated by the exact finite certificates; every remaining
   high-owner shore has an SDR for its six portal classes.
3. **Forbidden antipodal linkages.**  Each of the three antipodal
   two-linkages has a positive (K_7) quotient and is therefore absent.
4. **Bare four-web embeddings.**  The cited same-vertex web theorem plus
   seven-connectivity puts the four full portal classes of each
   antipodal demand on one facial cycle.
5. **Three-connected closure.**  If (D) is three-connected, Whitney
   uniqueness gives one common face; the exact circular occurrence
   theorem contradicts high ownership.
6. **Exact two-piece and degree-two locks.**  Every nonsingleton shore is
   two-connected, every two-cut has exactly two components, and every
   shore-degree-two vertex satisfies (4.1).
7. **Cycle-leaf frontier.**  The exact one-ear quotient certificate and
   the seven-fan eliminate broad cut vertices, leaving the double-thin
   state used in Section 5.

Now suppose (D) is not three-connected.  Its SPQR tree is nontrivial
(the one-node S and P cases are respectively the already excluded cycle
and the impossible simple parallel skeleton).  Choose any leaf edge.
The orientation-free rank conclusion gives a singleton side.  Lemma 4.1
turns that side into an actual singleton S-leaf.  The cycle-leaf frontier
and the audited bare-web/(K_{3,3}) argument eliminate that S-leaf, a
contradiction.

Thus no high-owner shore exists in this boundary cell.  This proves the
(C_6\dot\cup K_1) local closure conditional on the seven dependencies
above.  It does **not** prove (HC_7) as a whole: other degree-seven
neighbourhoods, one-component cells, and higher-degree vertices remain
outside this statement.

## 7. Citation rule

Future notes should not cite the old SPQR-path conclusion or infer that
all canonical leaves are singleton.  The safe reusable implication is

[
 	ext{rank-one side}
 \Longrightarrow
 	ext{degree-two singleton}
 \Longrightarrow
 pq\in E(D)
 \Longrightarrow
 	ext{canonical singleton S-leaf}.               	ag{7.1}
]

This implication is orientation-free and explicitly closes the R-leaf
and two-node cases.
