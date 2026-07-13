# Critical rural-operation composition and the Kuratowski atom

## 1. Purpose and status

This note addresses the dynamic gap left by
`hadwiger_palette_model_rural_counterarchitecture.md`.  The example in
that note proves that a repeated actual owner, a saturated five-colour
state, and a palette transversal in a fixed `K_5` frame do not by
themselves align palette colours with model labels.  A coherent rural
outcome is unavoidable.

There are two different assertions which must not be conflated.

1. Rural **pieces** in prescribed compatible rotations compose to one
   global two-apex embedding.  This is a disk-substitution statement.
2. If every proper internal operation on a piece is rural, the original
   piece need not be rural.  The sharp counterexamples are `K_5` and
   `K_{3,3}`.

The main result below proves that these are the only kind of obstruction
which can persist.  More precisely, a nonrural piece all of whose edge
deletions and contractions are rural has at most six live vertices and
ten live edges.  Every live edge is an unsubdivided branch edge of one
Kuratowski subdivision in the framed piece.  Thus the unbounded rural
composition problem disappears: the exact residue is one finite
**framed Kuratowski atom**, carrying the full proper-minor boundary-state
rejection relation.

This is a conditional composition theorem, not a proof of `HC_7`.  Its
hypotheses say explicitly which operations retain the fixed portal
society and which pieces cover the graph after deletion of the two apex
labels.

## 2. A fixed-order planarity frame

Let `(H,Omega)` be a society, where

\[
                 \Omega=(w_1,w_2,\ldots,w_k)
\]

is a cyclically ordered list of distinct vertices of `H`, with `k>=3`.
The society is **rural** when `H` has a drawing in a closed disk in which
the vertices of `Omega` occur on the boundary in the displayed cyclic
order (up to one global reversal).

Form the **wheel frame** `F_Omega(H)` as follows.  For every `i` add a
new vertex `r_i` and the rim path

\[
                       w_i r_i w_{i+1}
\]

(indices modulo `k`), and add one new hub `z` adjacent to every `w_i`.
All added vertices and edges are fixed: no operation below deletes or
contracts them.

### Lemma 2.1 (wheel-frame equivalence)

The society `(H,Omega)` is rural if and only if `F_Omega(H)` is planar.

#### Proof

Given a rural drawing, draw the subdivided rim on the boundary of the
disk and put `z` outside the disk, joining it to the `w_i` in the
exterior.  This gives a plane drawing of `F_Omega(H)`.

Conversely, take a plane drawing of `F_Omega(H)`.  Its wheel subdivision
has rim cycle

\[
                  C=w_1r_1w_2r_2\cdots w_kr_kw_1 .
\]

The hub lies on one side of the Jordan curve `C`, and the rotation of
its spokes fixes the cyclic order of the `w_i` on `C`, up to reversal.
Any `H`-bridge drawn on the hub side of `C` lies in one of the wheel
faces.  Since `H` has no edge to `z` or to an `r_i`, such a bridge has
attachments among at most the two consecutive vertices `w_i,w_{i+1}`.
It may therefore be flipped through the corresponding rim path to the
other side of `C`.  Performing this for all such bridges puts all of `H`
on the side of `C` opposite `z`.  That side is a disk whose boundary
contains `w_1,...,w_k` in the prescribed order.  Hence `(H,Omega)` is
rural.  \(\square\)

The subdivision vertices in the rim avoid any assumption that a
consecutive pair was already adjacent in `H`.

## 3. Rural reconstruction has one sharp atomic exception

Let `D` be a connected subgraph of `H` disjoint from `Omega`.  Call its
edges **live**.  Edges outside `D` and all wheel-frame edges are fixed.
For `e in E(D)`, deletion and contraction are therefore
boundary-faithful and commute with framing:

\[
 F_\Omega(H-e)=F_\Omega(H)-e,
 \qquad
 F_\Omega(H/e)=F_\Omega(H)/e.                       \tag{3.1}
\]

### Theorem 3.1 (critical rural reconstruction)

Assume that, for every `e in E(D)`, both societies

\[
                         (H-e,\Omega),\qquad(H/e,\Omega)
\]

are rural.  Then one of the following holds.

1. `(H,Omega)` is rural.
2. The framed graph `F_Omega(H)` contains a subdivision `K` of `K_5` or
   `K_{3,3}` such that every live edge is an entire unsubdivided branch
   path of `K`.  Consequently

   \[
                         |E(D)|\le10,
                         \qquad |V(D)|\le6.             \tag{3.2}
   \]

   (For a `K_{3,3}` subdivision the edge bound is nine.)

#### Proof

Suppose `(H,Omega)` is not rural.  By Lemma 2.1 the framed graph
`F=F_Omega(H)` is nonplanar.  Kuratowski's theorem gives in `F` a
subdivision `K` of `K_5` or `K_{3,3}`.

Fix a live edge `e`.  If `e` did not belong to `K`, the same
Kuratowski subdivision would survive in `F-e`.  But `H-e` is rural, so
Lemma 2.1 says that `F-e` is planar.  Therefore every live edge belongs
to `K`.

Let `P` be the branch path of `K` containing `e`.  If `P` had length at
least two, contracting `e` would merely shorten `P`; the image `K/e`
would still be a subdivision of the same `K_5` or `K_{3,3}`.  It would
be a nonplanar subgraph of `F/e`.  On the other hand `H/e` is rural, so
(3.1) and Lemma 2.1 say that `F/e` is planar.  This contradiction proves
that `P` has length one.  Thus every live edge is itself a branch path,
and its two ends are branch vertices of `K`.

Different live edges occupy different branch paths.  A `K_5` has ten
edges and five branch vertices, while a `K_{3,3}` has nine edges and six
branch vertices.  Since `D` is connected, every vertex of `D` is
incident with a live edge unless `D` is a singleton.  Hence all vertices
of a nonsingleton `D` are branch vertices of `K`, proving (3.2); the
singleton case also satisfies it.  \(\square\)

Both alternatives in Theorem 3.1 are necessary.  With an empty or
harmless boundary frame, `K_5` and `K_{3,3}` are nonrural while deleting
or contracting any edge makes them planar.  Thus no proof can infer the
rurality of the unoperated torso merely from rurality of all of its
proper one-edge operations.

### Corollary 3.2 (large live torso reconstruction)

Under the hypotheses of Theorem 3.1, if `D` has at least seven vertices
or at least eleven edges, then `(H,Omega)` is rural.

This is the promised uniform, infinite-family conclusion.  The
operation-minimal nonrural residue is bounded independently of the
orders of the portal sets, the surrounding web, and the number of
colour states.

## 4. Composition in a retained near-`K_7` shell

We record the exact form used by the repeated-owner and joint-edge
warehouses.  Let `p,q` be two fixed singleton labels.  Suppose
`G-{p,q}` is the union of

* one fixed plane quotient `Q`;
* pairwise interior-disjoint society pieces `(H_i,Omega_i)` placed in
  named faces of `Q`; and
* the literal portal edges represented by the occurrences in
  `Omega_i`.

The order `Omega_i` is the order induced by the boundary of its named
face.  In particular it is fixed before any minor operation is chosen.

### Lemma 4.1 (prescribed rural disks compose)

If every `(H_i,Omega_i)` is rural, then `G-{p,q}` is planar.  Hence `G`
is two-apex and six-colourable.

#### Proof

Draw `Q`.  In the disk bounded by the named face for `H_i`, substitute a
rural drawing of `(H_i,Omega_i)`, identifying equal portal occurrences.
The interiors of the disks are disjoint and the hypotheses say that the
quotient, pieces, and literal portal edges cover all of `G-{p,q}`.
Thus the substitutions draw that whole graph in the plane.  Four-colour
it and give `p,q` two fresh colours.  \(\square\)

The wheel frame is useful here because every operated rural drawing is
rural in the **same prescribed order**.  There is no independent choice
of a rotation for each operation: the fixed plane quotient supplies the
rim, and Lemma 2.1 supplies only the one global reflection allowed by
that rim.

### Theorem 4.2 (critical rural-operation trichotomy)

Let `G` be a proper-minor-minimal non-six-colourable graph with no
`K_7` minor.  Assume a localized repeated-owner or joint-edge warehouse
has been normalized as follows.

1. After deleting two fixed singleton labels `p,q`, the retained shell
   has the plane-quotient form preceding Lemma 4.1.
2. All pieces except one society `(H,Omega)` are already rural in their
   prescribed quotient rotations.
3. The live part `D` of `H` is one connected owner torso.  Deleting or
   contracting any edge of `D` is boundary-faithful and preserves the
   four private active extensions and the common pool/reserve bags.
4. For every operated society, either its four active roots have a
   rooted `K_4`, or they lie on the active face supplied by the
   active-root face theorem.  In the latter case, incompatibility between
   that facial order and the fixed column annulus gives the labelled
   four-column split by the two-cycle rotation exchange.  Either labelled
   obstruction completes with the common pool/reserve bags to a literal
   `K_7` model.  Thus an operated society which is not rural in the
   prescribed quotient order gives `K_7`.

Then at least one of the following conclusions is forced.

1. `G` contains the labelled `K_7` model of item 4.
2. `G` is two-apex and hence six-colourable.
3. `D` is a framed Kuratowski atom satisfying

   \[
                           |V(D)|\le6,qquad |E(D)|\le10. \tag{4.1}
   \]

   Every live edge is an unsubdivided branch edge of one framed `K_5`
   or `K_{3,3}` subdivision.

#### Proof

If some faithful deletion or contraction of a live edge is nonrural,
item 4 gives outcome 1.  Otherwise every live edge satisfies the two
rural operation hypotheses of Theorem 3.1.  If the original society is
rural, Lemma 4.1 gives outcome 2.  If it is not rural, Theorem 3.1 gives
outcome 3.  \(\square\)

In a hypothetical minimal counterexample outcomes 1 and 2 are
impossible.  Thus the rural branch cannot propagate through an
unbounded owner torso: it terminates in the atom (4.1).

## 5. The full critical state carried by the atom

Let the atom lie in one open shore of a separation `(A,B)` with literal
boundary `W`; in the one-complex applications `|W|=7`.  For a boundaried
graph `J` write `E(J,W)` for the equality partitions of `W` induced by
proper six-colourings of `J`.

### Lemma 5.1 (atomic operation rejection)

For every nonidentity boundary-faithful operation `mu` on the atom there
is a partition `Pi_mu` of `W` into at most six independent blocks such
that

\[
 \Pi_\mu\in E(A^\mu,W)\cap E(B,W),
 \qquad
 \Pi_\mu\notin E(A,W).                                  \tag{5.1}
\]

If `nu` is an `A`-faithful proper operation supported in the opposite
open shore, then no six-colouring of that operated minor induces
`Pi_mu` on `W`.

#### Proof

The first assertion is the exact operation-novelty argument.  Colour the
proper minor `G^mu` and restrict its equality partition to `W`.  The
colouring restricts to both displayed operated/unoperated closed shores.
If `A` also accepted the partition, align the block colours and splice
to obtain a six-colouring of `G`.

For the last assertion, a colouring of the opposite operated minor with
the same equality partition, together with the colouring of `G^mu`,
would satisfy the boundary-faithful crossed-minor theorem and again
six-colour `G`.  \(\square\)

This uses rejection under every internal deletion and contraction; it is
exactly the hypothesis absent from the seven-connected rural
counterarchitecture `K_2 join P`.

### Corollary 5.2 (exact-seven incidence floor)

Suppose in addition that the atom is a component of `G-W`, where
`|W|=7`, and `delta(G)>=7`.  Put `m=|V(D)|`.  Then every `x in D` has

\[
                         |N_W(x)|\ge 8-m,                 \tag{5.2}
\]

and hence the atom has at least `m(8-m)` literal incidences with the
seven boundary labels.  In particular every vertex of a six-vertex
atom has at least two actual boundary neighbours.

#### Proof

All neighbours of `x` outside `D` lie in `W`, while
`d_D(x)<=m-1`.  Therefore

\[
 |N_W(x)|=d_G(x)-d_D(x)\ge7-(m-1)=8-m.
\]

Sum over `x`.  \(\square\)

Thus the atom gate is not an arbitrary labelled `K_5`/`K_{3,3}`: it is
a six-or-fewer-vertex core with a dense, literal seven-boundary incidence
matrix and a rejected operation state on every branch edge.

## 6. Exact remaining gate

The preceding theorems prove the following part of the proposed critical
palette/model trichotomy.

```text
nonrural faithful operation
    -> active rooted K4 -> labelled K7;
all faithful operations rural, original torso rural
    -> prescribed disk composition -> one global two-apex embedding;
all faithful operations rural, original torso nonrural
    -> a framed K5/K3,3 atom on at most six live vertices,
       with a rejected exact-boundary state on every live operation.
```

Therefore the remaining statement is no longer a general rural-order or
portal-placement theorem.  It is the following bounded but genuinely
model-labelled gate.

> **Framed Kuratowski state gate.**  In a seven-contraction-critical
> one-torso shell, let a repeated-owner atom `D` satisfy (4.1), with its
> four active extension roles and common pool/reserve bags.  Then either
> a branch edge of the framed `K_5`/`K_{3,3}` subdivision realizes the
> labelled owner split, or one of the at most twenty edge-operation
> states (5.1) (deletion and contraction for each of at most ten live
> edges) is also realized by an opposite boundary-faithful operation.

The first outcome gives `K_7`; the second six-colours by crossed
splicing.  Proving this gate would complete the localized critical
trichotomy.  Merely asserting that all operated disks have compatible
orders cannot bypass it: `K_5` and `K_{3,3}` show that such an assertion
would be false.

There is a second, logically prior qualification.  If an internal
operation destroys two active extension roles rather than preserving the
four-role product in item 3 of Theorem 4.2, it falls outside the theorem.
The exact residual is then the bilateral exact-seven/two-coordinate
state-forcing exchange already isolated in
`hadwiger_near_k7_active_root_face_exchange.md`.  No rotation issue
remains there: one must either restore the two private roles or match the
faithful states of opposite minimum-separator shores.
