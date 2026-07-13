# Audit: exact ownership of pair modes from Diwan extension

## Verdict

The bare-web lifting, Diwan palette argument, exact-ownership conclusion,
and the \(q\ge6\) small-or-exact dichotomy in
hadwiger_pair_mode_diwan_ownership.md are **GREEN**, after one scope
correction to the optional ownership-count paragraph.

The resulting theorem is:

> Let \(G\) be \(r\)-minor-critical and \(k\)-connected.  Let \(S\) be
> a full \(k\)-cut with exactly \(q\ge2\) shores, where
> \(k=2q+1\).  If \(G[S]\) has an optimal partition
> \[
> B_1\mid\cdots\mid B_q\mid\{s\},\qquad |B_i|=2,
> \]
> and \(r\ge q+4\), then exactly one shore contains disjoint connected
> carriers for two pair blocks.

## 1. Bare-web lifting

Fix \(B_a=\{a_1,a_2\}\) and \(B_b=\{b_1,b_2\}\), and suppose a full
shore \(D\) has no two-block capacity for them.  Add four artificial
terminals, each adjacent precisely to the relevant portal class.
A linkage for the pairs

\[
(a_1,a_2),\qquad(b_1,b_2)
\]

would give the forbidden disjoint carriers inside \(D\).  Complete on
the same vertex set to an edge-maximal nonlinkable graph.  The rooted
Two Paths Theorem gives a web with alternating frame.

An inserted clique behind a facial triangle cannot be nonempty.  Every
actual neighbour of that clique outside it belongs to:

* one of the at most three triangle vertices, with an artificial
  terminal replaced by its actual root; or
* one of the \(k-4\) roots omitted from the auxiliary graph.

Thus at most

\[
3+(k-4)=k-1
\]

actual vertices separate a nonempty part of \(D\) from another
nonempty shore.  This contradicts \(k\)-connectivity.  The hypothesis
\(q\ge2\) is used here to supply that far shore.

Deleting all completion edges except the frame and relabelling the
artificial terminals gives exactly

\[
H^+=G[D\cup B_a\cup B_b]+E(K_{B_a,B_b}).
\]

The outer frame stays facial.  It is induced: each pair block is
independent, and the four added cross edges are all edges of the
induced \(K_{2,2}\).  No unlisted completion edge is used later.

## 2. Diwan palette and gluing

Assume no shore owns the selected mode and fix \(B_1,B_2\).  The
previous argument gives the same labelled induced facial \(C_4\) in
every shore disk.

Use one colour on \(B_1\), a second on \(B_2\), and reserve \(q-1\)
distinct colours for

\[
B_3,\ldots,B_q,\{s\}.
\]

The residual palette has

\[
h=r-(q-1)\ge5
\]

colours.  The frame has length four and uses two colours, so

\[
4\le2h-5,\qquad 2\le h-1.
\]

Diwan's induced-cycle theorem therefore extends this fixed frame state
over every \(H_i^+\) using only the residual palette.

All omitted roots use reserved colours.  Hence every root--shore edge
omitted from a disk is proper by palette separation.  Boundary blocks
are independent and receive pairwise distinct colours; the shore
colourings agree on the frame; and different shores are anticomplete.
The extensions glue to an \(r\)-colouring of \(G\), the required
contradiction.

No minor contraction is used in the at-least-one direction.

## 3. At-most-one and exact ownership

The general shore-capacity theorem applies because:

* the number of shores equals the number \(q\) of pair blocks;
* optimality makes the singleton adjacent in the block quotient to
  every pair block;
* \(r\ge q+4\) in particular gives \(q+1\le r\); and
* two owners let one owner realize two blocks while the other
  \(q-2\) helper shores realize one remaining block each.

For every target shore, an owner outside the target is available.
The \(q\) contracted carrier sets and the singleton form a labelled
\(K_{q+1}\), so a colouring of the proper minor transfers the exact
mode to the target.  The target-side colourings then align and glue.
Thus there is at most one owner.  Together with the Diwan theorem,
there is exactly one.

## 4. The \(q\ge6\) consequence

Every nonowner shore with more than \(q\) vertices and no proper exact
\(k\)-fragment is internally \(q\)-connected by the separator-capacity
theorem.  For pair blocks, Jung's theorem makes any four-connected
nonplanar or maximal-planar shore two-linked, which would give
capacity.  A surviving atomic nonowner is therefore planar and not
maximal planar.  Planar connectivity is at most five, so none exists
when \(q\ge6\).

Exact ownership leaves \(q-1\) nonowners.  Consequently, for
\(q\ge6\), **every** nonowner shore has at most \(q\) vertices or
contains a nested exact \(k\)-fragment.

## 5. Scope correction

Exact ownership alone does not automatically activate the abstract
ownership-count inequality for \(q=4,5\).  That inequality additionally
requires a simultaneous-face statement bounding the number of
nonowner modes of each tag.  A facial transversal selected separately
for each mode is insufficient.  The source note has been patched to
make this premise explicit.  This correction does not affect the
Diwan ownership theorem or the \(q\ge6\) dichotomy.

