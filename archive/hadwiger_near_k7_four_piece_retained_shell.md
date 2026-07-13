# Four defect-one pieces close the near-`K_7` owner chain

## 1. Scope and audited dependencies

Let

\[
                       L=\{a,b,c,q_1,q_2,q_3\}
\]

induce `K_6-{ab,ac}`.  This is the singleton shell in the one-complex
`K_7^vee` normalization.  A connected piece has **defect at most one** if
it is adjacent to at least five vertices of `L`.

The only finite input below is the independently audited three-piece
classification from
`hadwiger_near_k7_defect_one_capacity_state_web.md`: three consecutive
disjoint connected defect-one pieces already give `K_7`, except possibly
when their unique missed labels form one of

\[
\begin{split}
 \mathcal E={}&\{(c,q_i,b),(b,q_i,c):1\le i\le3\}\\
 &\cup\{(c,c,a),(b,b,a),(a,b,b),(a,c,c)\}.             \tag{1.1}
\end{split}
\]

The verifier exhausts all `7^3` support profiles and all spanning
seven-bag partitions of the nine-vertex quotient; an independent
nonspanning connected-subset search reproduced the same ten negative
profiles.  The present note does not use a chain of quotient colour states.
All pieces and every separation used below remain literal disjoint
subgraphs of the original graph.

## 2. The missed four-piece closure

### Theorem 2.1 (four-piece defect-one chain)

Let `X_1,X_2,X_3,X_4` be pairwise disjoint nonempty connected sets.  Assume

\[
                         E(X_i,X_{i+1})\ne\varnothing
                         \quad(1\le i\le3),              \tag{2.1}
\]

and every `X_i` meets at least five of the six singleton labels in `L`.
Then the graph contains a `K_7` minor.

#### Proof

If either consecutive triple has a support profile outside `mathcal E`,
the audited three-piece theorem gives `K_7`.  Suppose both profiles lie in
`mathcal E`.  Matching a length-two suffix in (1.1) to a length-two prefix
shows that the only possible four-letter words are

\[
                              abba,\qquad acca.           \tag{2.2}
\]

Indeed the words involving a middle `q_i` have suffix `q_i b` or `q_i c`,
neither of which begins a word of `mathcal E`; the suffixes `ca` and `ba`
also do not begin a word; and the only remaining overlaps are

\[
             (a,b,b)\cdot(b,b,a),\qquad
             (a,c,c)\cdot(c,c,a).
\]

For `abba`, use the seven bags

\[
 \{a,b\}\cup X_1\cup X_2,quad \{c\},\quad
 \{q_1\},\quad\{q_2\},\quad\{q_3\},\quad X_3,\quad X_4.
                                                               \tag{2.3}
\]

The first bag is connected: `X_1X_2` is an edge, `X_1` sees `b`, and
`X_2` sees `a`.  It is adjacent to `X_3` through the `X_2X_3` edge and
to `X_4` because an `a`-dark piece sees `b`.  The sets `X_3,X_4` are
adjacent, both see `c,q_1,q_2,q_3`, and the four singleton bags form a
clique.  Thus (2.3) is a `K_7` model.

For `acca`, use

\[
 \{a,c\}\cup X_1\cup X_2,quad \{b\},\quad
 \{q_1\},\quad\{q_2\},\quad\{q_3\},\quad X_3,\quad X_4.
                                                               \tag{2.4}
\]

Now `X_1` sees `c`, `X_2` sees `a`, and they are adjacent, so the first
bag is connected.  It sees `b` through the edge `bc`, sees all `q_i`,
sees `X_3` through `X_2X_3`, and sees `X_4` because an `a`-dark piece
sees `c`.  The piece `X_3` is `c`-dark, the piece `X_4` is `a`-dark,
so both see `b,q_1,q_2,q_3`; they are adjacent by (2.1).  Hence (2.4)
is a `K_7` model.  QED.

The four pieces may have arbitrary order, treewidth, and internal portal
placement.  Additional contacts and nonconsecutive edges only help.  This
is therefore a uniform rooted-model theorem, not a bounded-order quotient
claim.

### Theorem 2.2 (an exceptional triple has no end cross-edge)

Let `X_1,X_2,X_3` have one of the ten profiles (1.1).  If

\[
                              E(X_1,X_3)\ne\varnothing, \tag{2.5}
\]

then the graph contains a `K_7` minor.

#### Proof

The additional edge makes `X_1,X_2,X_3` pairwise adjacent.  There are
three symmetry classes.

* For `(c,q_i,b)` or its reverse, use

  \[
   \{a,q_i\}\mid\{b,c\}\mid\{q_j\}\mid\{q_k\}
      \mid X_1\mid X_2\mid X_3,                         \tag{2.6}
  \]

  where `\{i,j,k\}=\{1,2,3\}`.
* For `(a,b,b)` or `(b,b,a)`, use

  \[
   \{a,b,q_1\}\mid\{c\}\mid\{q_2\}\mid\{q_3\}
      \mid X_1\mid X_2\mid X_3.                         \tag{2.7}
  \]

* For `(a,c,c)` or `(c,c,a)`, interchange `b,c` in (2.7).

The merged label bags are connected through the displayed neutral label
or the edge `bc`.  Direct inspection of each defect word shows that every
piece sees every merged label bag and every retained singleton; (2.5) and
the two chain edges make the three pieces a triangle.  These are seven
pairwise adjacent connected bags.  QED.

The ten negative profiles are therefore induced three-piece paths at the
piece-quotient level in every target-free graph.

### Theorem 2.3 (canonical rural expansion or one local conflict)

Assume that the one-complex model is spanning and that

\[
                         V(B)=X_1\mathbin{\dot\cup}
                              X_2\mathbin{\dot\cup}X_3. \tag{2.8}
\]

If the three-piece profile is outside (1.1), the graph has a `K_7` minor.
If it is in (1.1) and no `K_7` minor exists, choose two neutral labels as
follows:

* for `(c,q_i,b)` or `(b,q_i,c)`, delete the two neutral labels other than
  `q_i`;
* for the other four profiles, retain any one `q_i` and delete the other
  two.

After contracting the three pieces, the simple quotient of the displayed
deletion is a seven-vertex maximal planar graph.  It has a unique plane
rotation up to reflection.  Consequently exactly one of the following
holds:

1. the full multigraph quotient, including all parallel portal and
   interpiece edges, has the compatible lift of that rotation and every
   piece society is rural in its induced order; then the original graph is
   two-apex;
2. one of the three named societies is nonrural in its forced rotation, or
   one of the two interpiece parallel bundles has incompatible end orders.

#### Proof

The first assertion is the audited three-piece theorem, and Theorem 2.2
removes the only possible nonconsecutive piece edge in a target-free graph.
It remains to certify the planar quotient.  Write `q` for the retained
neutral label and `x_i` for the contracted piece.  Up to reversing the
piece path and interchanging `b,c`, there are three profiles.  The
following lists are their triangular face sets:

\[
\begin{array}{c|l}
(c,q,b)&
 ax_1q,ax_2x_1,ax_3x_2,aqx_3,bcq,bx_2c,bx_1x_2,
 bqx_1,cx_2x_3,cx_3q;\\[2mm]
(c,c,a)&
 ax_1q,ax_2x_1,aqx_2,bcq,bx_3c,bx_2x_3,bx_1x_2,
 bqx_1,cx_3q,qx_3x_2;\\[2mm]
(a,b,b)&
 ax_2q,ax_3x_2,aqx_3,bcq,bx_1c,bqx_1,cx_1x_2,
 cx_3q,cx_2x_3,qx_2x_1.
\end{array}                                               \tag{2.9}
\]

Every listed triple consists of quotient edges; every edge occurs in two
faces.  Thus each row is a plane triangulation.  It has 15 edges on seven
vertices, so it is maximal planar and hence three-connected; Whitney
uniqueness gives the forced rotation.

If the full parallel-edge rotations and all three societies are compatible
and rural, substitute their disk drawings into this quotient drawing.
Because (2.8) covers the complex bag and the original model is spanning,
this draws every vertex and edge after deletion of the chosen two neutral
labels.  The graph is two-apex.  Failure of that substitution is exactly
the local alternative 2.  QED.

This is the sharp extra hypothesis missing from a bare statement that the
simple near-clique quotient is planar.  In the defect-one three-piece
family, global coherence is no longer an unbounded condition: it is the
rurality of three named societies and compatibility of two named bundles
in one unique triangulation.

## 3. Retained-tree capacity and state consequence

Use the defect-one retained web definition of the audited capacity-state
note: the complex bag is partitioned into actual disjoint connected pieces
indexed by a rooted tree; consecutive tree pieces are adjacent; every
piece has defect at most one; and child-subtree lobes at a branching node
are actual pairwise anticomplete open shores behind one common two-cut.

### Corollary 3.1 (three-level retained-web bound)

In a `K_7`-minor-free, proper-minor-minimal non-six-colourable graph, such
a retained web has at most

\[
                         1+108+108^2=11,773             \tag{3.1}
\]

pieces.

#### Proof

Theorem 2.1 forbids four vertices on a root-to-leaf path, so the rooted
tree has at most three vertex levels.  At a branching node, delete one
literal child-subtree lobe and six-colour the resulting proper minor.  On
the common boundary

\[
                       L\mathbin{\dot\cup}\{x,y\},
\]

the clique `\{b,c,q_1,q_2,q_3\}` is rainbow, `a` has at most three
equality classes, and each of `x,y` has at most six.  Hence there are at
most `3*6^2=108` equality states.  Two deleted lobes with the same state
cross-splice, because the lobes are retained simultaneously, are
anticomplete, and have the same actual boundary.  That would six-colour
the original graph.  Thus every node has at most 108 children, and the
three-level tree bound is (3.1).  QED.

This proof uses only boundary-faithful deletions of simultaneous shores in
the original graph.  It does not pigeonhole states along a sequence of
already-colourable contraction quotients.

### Corollary 3.2 (split/rural/state trichotomy with corrected depth)

For any defect-one retained web in the one-complex `K_7^vee`
normalization, at least one of the following holds:

1. four consecutive pieces give the explicit `K_7` model of Theorem 2.1;
2. two child lobes have a common faithful boundary state and crossed
   splicing six-colours the graph;
3. the web has at most 11,773 pieces; or
4. after deleting two neutral singleton labels, the full piece quotient
   and every induced society rotation are globally compatible and rural,
   so disk substitution makes the graph two-apex.

In a hypothetical `HC_7` counterexample, outcomes 1, 2 and 4 are
impossible; therefore any web satisfying the displayed decomposition
hypotheses is the bounded outcome 3.

#### Proof

The first three outcomes are Theorem 2.1 and Corollary 3.1.  For outcome
4, draw the full planar piece quotient, retaining every parallel portal
occurrence, and substitute the rural drawings in disjoint disks with their
recorded rotations.  This draws the deletion of the two neutral labels.
The planar remainder is four-colourable and the two deleted vertices use
two fresh colours.  QED.

## 4. Audit of the surrounding route

The following conclusions survive the present audit.

1. The label-free portal splitter is safe only as a **one-step** theorem:
   a contractible edge either preserves the forbidden-pattern and relative
   connectivity data while creating one new boundary state, or exposes an
   actual tight adhesion.  Repeating those quotient contractions and
   pigeonholing states is invalid.
2. The two-cut owner/state theorems use literal simultaneous lobes and are
   valid retained-shell arguments.
3. A coherent full contact multigraph with rural societies really is
   two-apex; planarity of the simple contracted quotient alone is
   insufficient.
4. The tree-society split theorems close the compatible rural and balanced
   peel families, but leave unbalanced owner cuts.  Their later strict
   surplus example is only a counterexample to a selected peel: as its own
   audit observes, the literal graph already has a `K_7` model.
5. The fixed-owner nested-shell theorem is a legitimate retained-shell
   principle only when the seven boundary labels are carried through every
   annulus by actual disjoint paths.  It supplies a finite depth bound, not
   a rooted split.

The present correction removes the former `abba/acca` four-piece frontier.
The exact defect-one residue is now a chain of at most three pieces with
one of the ten profiles (1.1), together with defect-at-least-two pieces,
failure of the retained decomposition, or an incompatible rural rotation.

## 5. Exact remaining theorem

The near-`K_7` route will close if the following retained-shell exchange is
proved.

> Let two adjacent rural pieces be the first rotation conflict, or let a
> retained annular piece have two dark singleton rows.  Then either the
> actual pieces realize the three-shore split, a minimum seven-adhesion has
> the same boundary extension state from both retained sides, or the two
> apex labels extend coherently across the conflict.

The first conclusion is `K_7`, the second six-colours by crossed splicing,
and the third propagates the globally two-apex web.  This statement is
localized at one actual annulus; it neither contracts recursively nor asks
arbitrary quotient states to repeat.
