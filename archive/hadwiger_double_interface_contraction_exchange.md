# Simultaneous contraction breaks the two-edge XOR lock

## 1. Setting

Let (G) be (r)-minor-critical.  Let (S) separate an unchanged
side (D^*) from a side

\[
                 D=X\mathbin{\dot\cup}Y,
\]

where (X,Y) are connected and the complete (X)-(Y) interface is
the matching

\[
 e_1=x_1y_1,\qquad e_2=x_2y_2 .                 \tag{1.1}
\]

Fix a labelled (r)-colouring (phi) of (S).  Let

\[
 \begin{aligned}
 {cal A}_\phi&=\{(c(x_1),c(x_2)):c
        \text{ extends }\phi\text{ over }G[S\cup X]\},\\
 {cal B}_\phi&=\{(c(y_1),c(y_2)):c
        \text{ extends }\phi\text{ over }G[S\cup Y]\}.
 \end{aligned}                                    \tag{1.2}
\]

Only boundary colour names are fixed.  The colours at the four
interface terminals are part of the two relations.

## 2. Three interface operations

Write (Phi) for the equality partition induced by (phi).  Say that
(Phi) is an (i)-transition if it extends (D-e_i) and (D^*), but
not (D).  Say that it is a double-contraction transition if it is
induced by an (r)-colouring after simultaneously contracting the two
disjoint edges in (1.1), and it extends (D^*), but not (D).

The simultaneous contraction is a proper minor operation.  Expanding
its two contracted vertices after deleting (e_1,e_2) gives a colouring
in which

\[
 c(x_1)=c(y_1),\qquad c(x_2)=c(y_2).              \tag{2.1}
\]

As usual, the induced state cannot extend the original (D): otherwise
that extension and the unchanged (D^*)-extension could be aligned on
(S) and glued to colour (G).

### Theorem 2.1 (double-contraction exchange)

Assume that one state (Phi) is both a (1)-transition and a
(2)-transition.  Then exactly the star/XOR classification holds:

1. one of ({\cal A}_\phi,{\cal B}_\phi) is a singleton and the other
   is contained in the row-column cross through that singleton; or
2. for distinct (p,r) and distinct (q,s), after possibly
   interchanging the two relations,
   
   \[
   {\cal A}_\phi=\{(p,q),(r,s)\},\qquad
   {\cal B}_\phi=\{(p,s),(r,q)\}.                 \tag{2.2}
   \]

If the same (Phi) is also a double-contraction transition, outcome 2
is impossible.  More precisely, in outcome 1 the singleton point belongs
to the other relation as well.

Consequently, if a common deletion state has the XOR form (2.2), every
state produced by simultaneously contracting (e_1,e_2) is distinct
from it.

#### Proof

Because (Phi) does not extend (D), every
(a\in{\cal A}_\phi) and (b\in{\cal B}_\phi) agree in at least one
coordinate.  Otherwise the two side colourings would make both edges in
(1.1) proper and would glue to an extension over (D).

An extension over (D-e_1) has equality in coordinate (1) and
inequality in coordinate (2), while an extension over (D-e_2) has
inequality in coordinate (1) and equality in coordinate (2).  The
elementary cross-intersecting classification therefore gives precisely
the star/XOR alternatives above; this is Lemma 5.1 of
`hadwiger_moser_atomic_interface_lock.md`.

If (Phi) is also induced by the double contraction, (2.1) supplies
one point which belongs to both ({\cal A}_\phi) and
({\cal B}_\phi).  The two relations in (2.2) are disjoint, since
(p\ne r) and (q\ne s).  Hence the XOR outcome is impossible.

In the star outcome, suppose for definiteness that
({\cal A}_\phi=\{(p,q)\}).  The common point forced by (2.1) must then
be ((p,q)), so ((p,q)\in{\cal B}_\phi).  The argument is symmetric
when ({\cal B}_\phi) is the singleton.  The final consequence follows
immediately. \(\square\)

## 3. Palette symmetry inside the terminal-rigid residue

Let (U) be the set of colours absent from the labelled boundary
colouring (phi).  Both relations in (1.2) are invariant under every
permutation of (U), because such a permutation fixes (phi)
pointwise.

### Corollary 3.1

In the terminal-rigid outcome

\[
               {\cal A}_\phi=\{(p,q)\},          \tag{3.1}
\]

neither (p) nor (q) belongs to (U) whenever (|U|\ge2).

In the XOR outcome, each coordinate set
({p,r}) and ({q,s}) is invariant under all permutations of
(U).  Hence:

* if (|U|\ge3), none of (p,q,r,s) is absent from the boundary;
* if (|U|=2), the two absent colours either occupy a whole coordinate
  set or do not occur in that coordinate.

#### Proof

If, say, (p\in U) in (3.1), interchange (p) with another member of
(U) in an (X)-extension.  This fixes the boundary and changes the
first terminal colour, contradicting (3.1).  The assertion for (q) is
identical.

For (2.2), a boundary-fixing palette permutation maps each extension
relation to itself, so it preserves its first-coordinate set and its
second-coordinate set.  The only subsets of (U) of order at most two
which are invariant under the full symmetric group on (U) are the
empty set, all of (U) when (|U|\le2), and (for a singleton palette)
the singleton itself.  The two conclusions follow. \(\square\)

### Lemma 3.2 (the local free palette is the relevant symmetry)

Suppose the complete boundary contact row of \(X\) is
\(P_X\subseteq S\), and put

\[
 C_X=\phi(P_X),\qquad F_X=[r]-C_X.                \tag{3.2}
\]

Then \({\cal A}_\phi\) is invariant under every permutation of
\(F_X\), not merely under permutations of the colours absent from all
of \(S\).  The symmetric assertion holds for \(Y\).

Consequently, if \({\cal A}_\phi=\{(p,q)\}\) and
\(|F_X|\ge2\), then \(p,q\in C_X\).  In the XOR outcome, each of
the coordinate sets \(\{p,r\}\) and \(\{q,s\}\) is invariant under
\(\operatorname{Sym}(F_X)\).  In particular:

* if \(|F_X|\ge3\), both coordinate sets avoid \(F_X\); and
* if \(|F_X|=2\), each coordinate set either avoids \(F_X\) or equals
  \(F_X\).

#### Proof

A permutation of \(F_X\), applied only to an extension over \(X\),
fixes the colour of every boundary vertex having a neighbour in \(X\).
No vertex of \(S-P_X\) has an edge to \(X\).  Thus the permutation
preserves every boundary edge and maps an \(X\)-extension of \(\phi\)
to another such extension.  This proves the invariance.

A singleton ordered pair is fixed by all of
\(\operatorname{Sym}(F_X)\), so neither coordinate can belong to a
free palette of order at least two.  In the XOR case the first- and
second-coordinate projections are invariant two-element sets.  An
invariant subset which meets \(F_X\) contains all of \(F_X\), giving
the two displayed conclusions. \(\square\)

### Corollary 3.3 (four-block Moser states)

Suppose \(r=6\), the boundary state has four blocks of sizes
\(2,2,2,1\), and \(P_X=S-\{a\}\).  Let \(U=\{u,v\}\) be the two
colours unused on \(S\).

* If \(a\) is the singleton block, then
  \(F_X=U\cup\{\phi(a)\}\), so neither a terminal-rigid ordered pair
  nor an XOR coordinate can use any of these three colours.
* If \(a\) lies in a two-vertex block, then \(F_X=U\).  An XOR
  coordinate is either entirely boundary-supported or is exactly
  \(U\).

Thus an XOR rectangle in a four-block state has only two types on a
given almost-full piece: it is boundary-supported, or it is the pure
two-unused-colour parity rectangle

\[
 \{(u,u),(v,v)\}\quad\hbox{versus}\quad
 \{(u,v),(v,u)\},                                \tag{3.3}
\]

up to interchanging the relations and the names \(u,v\).  The pure
parity type is impossible if the defect of either almost-full piece is
the singleton boundary block.

#### Proof

The contact palette loses the colour of \(a\) exactly when no second
root has that colour.  Hence \(|F_X|=3\) in the singleton case and
\(F_X=U\) otherwise.  Apply Lemma 3.2 on both pieces.  If an XOR
coordinate uses \(U\), invariance of the whole two-point relation (not
only its projection) forces the other coordinate to use \(U\) as well:
otherwise swapping \(u,v\) changes just one coordinate of each point
and produces two new points, since both coordinate pairs are required
to have distinct entries.  Hence either neither coordinate uses \(U\),
or both do, in which case the two rectangles are exactly (3.3).
\(\square\)

## 4. The forced parity cycle

Return to the two-edge matching interface and assume its boundary state
is a four-block state.  Suppose the common deletion state has the pure
unused-colour XOR form (3.3).  In view of Corollary 3.3, neither row
defect is the singleton block.

### Theorem 4.1 (unused XOR is an alternating interface cycle)

For either deletion witness, the Kempe alternative for the other unused
colour is necessarily the internal-ear outcome, while the four colours
used on \(S\) all have the two-boundary-anchor outcome.  In particular
there are paths

\[
 x_1\longrightarrow x_2\quad\hbox{in }X,
 \qquad
 y_1\longrightarrow y_2\quad\hbox{in }Y           \tag{4.1}
\]

using only the two unused colours.  Together with \(e_1,e_2\), they
form an alternating interface cycle.  For each of the four boundary
colours, the corresponding bichromatic components at both ends of the
deleted edge are distinct and boundary-anchored.

#### Proof

Choose the \(e_1\)-deletion extension with endpoint pairs

\[
 (c(x_1),c(x_2))=(u,u),\qquad
 (c(y_1),c(y_2))=(u,v).
\]

There is no \(u/v\)-coloured boundary vertex, so neither of the two
\(u/v\)-components at \(x_1,y_1\) can be boundary-anchored.  The
interface exchange lemma therefore supplies a \(u/v\)-path from
\(x_1\) to \(y_1\) in \(D-e_1\).  Its only possible crossing between
\(X\) and \(Y\) is \(e_2=x_2y_2\).  The portions on its two sides give
the paths in (4.1).

The two-edge interface lemma guarantees at least four anchored colours.
Only the four colours occurring on \(S\) can anchor a component, so all
four do and no further internal-ear colour exists.  The argument from
the other deletion and after interchanging \(u,v\) is identical.
\(\square\)

Theorem 4.1 is an exact structural residue, not an abstract XOR state:
the only XOR not already expelled by local palette symmetry is a
two-colour cycle with four simultaneous boundary anchors.  Breaking that
cycle by a portal-distribution or web exchange is the remaining geometric
step.

## 5. Scope

The theorem does not yet eliminate the terminal-rigid star.  It does,
however, remove XOR as a state which can absorb the two individual edge
deletions and the simultaneous contraction at once.  Thus a two-edge
atomic interface has only two genuine continuations:

* the double contraction supplies a new exact state, feeding state
  holonomy; or
* one rooted piece forces an ordered pair of boundary-used terminal
  colours, and the opposite piece contains the centre of that star.

This conclusion is label-free and applies to any two-edge matching
interface.  Moser labels enter only later, when distinct transition
states are normalized and compared geometrically.

## 6. Double-contraction normalization in the pure-Moser cell

The preceding new state can be made concrete.  This is the point at which
the Moser boundary, rather than abstract state theory, enters.

### Theorem 6.1 (a double contraction gives a new matching state or a path)

Let \(G\) be a hypothetical \(7\)-contraction-critical graph, let
\(v\) have degree seven, and let \(S=N_G(v)\) induce the pure Moser spindle.
Use the standard labels and fix the independent pair \(I=\{1,3\}\).  Let
\(e_1,e_2\) be vertex-disjoint edges in one component of \(G-N[v]\).

Then at least one of the following holds.

1. There is a path between a nonedge \(xy\) of \(G[S-I]\) whose interior
   lies in one component of \(G-N[v]\).
2. Simultaneously contracting the star \(G[\{v\}\cup I]\) and the two
   edges \(e_1,e_2\) produces, after expansion and deletion of \(v\), an exact
   boundary state

   \[
   I\mid J\mid K\mid\{r\},                       \tag{6.1}
   \]

   where \(I,J,K\) are three disjoint nonedges of the Moser spindle.  In the
   corresponding colouring the two ends of each \(e_i\) have the same
   colour.

Moreover, if an exact state \(\Phi\) common to the two individual edge
deletions has the XOR form of Theorem 2.1, the state (6.1) is different from
\(\Phi\).

#### Proof

The three contraction sets are pairwise disjoint.  Colour the resulting
proper minor with six colours.  Expand the contracted star only to the two
boundary vertices \(1,3\), delete \(v\), and expand each contracted edge
after deleting it.  This gives a colouring of

\[
G-v-\{e_1,e_2\}
\]

in which \(1,3\) have one colour \(\sigma\) and no other vertex of \(S\) has
colour \(\sigma\), while the ends of both \(e_i\) have equal colours.  The
trace on \(I\) is exact because every vertex of \(S-I\) was adjacent through
\(v\) to the contracted star vertex.

Every colour class on \(S\) has order at most two, since it is independent
and \(\alpha(G[S])\le2\).  Thus the boundary uses between four and six
colours.  We now work in the contracted minor, so every Kempe switch keeps
the two edge contractions intact.

If the boundary uses six colours, all five vertices of \(S-I\) are
singletons.  Choose any missing-cycle edge \(J\) of
\(\overline{G[S-I]}\cong C_5\).  If its two uniquely coloured ends lie in
different bichromatic components, switch the component of one end; this
merges exactly those two boundary vertices into the independent block
\(J\).  If they lie in the same component, a shortest bichromatic path
between them has no other boundary vertex and avoids the contracted star
vertex.  Lifting the two contracted interface vertices turns it into a path
in the original graph whose interior lies outside \(N[v]\).  All its internal
vertices lie in one component of \(G-N[v]\), giving outcome 1.

After the first merge, or if the original boundary used five colours, its
blocks have sizes \(2,2,1,1,1\), one two-block being \(I\).  Let \(J\) be the
other two-block.  The matching-extension property of the Moser spindle says
that the three vertices of \(S-(I\cup J)\) contain a nonedge \(K\).  Apply the
same bichromatic switch to its two singleton ends.  It either gives outcome
1 or merges them into \(K\), leaving exactly (6.1).  If the boundary already
used four colours, it had the form (6.1) from the start.  Fewer than four
colours are impossible because seven vertices with independent colour
classes of order at most two need at least four colours.

Finally, a state induced by the double contraction supplies a common ordered
pair in the two extension relations: both interface coordinates are equal.
The two relations of an XOR state are disjoint.  Theorem 2.1 therefore shows
that their equality partitions cannot be the same.  Hence (6.1) differs from
\(\Phi\). \(\square\)

### Consequence 6.2

In the two-edge pure-Moser atomic lock, an XOR common deletion state cannot
be the only normalized state.  The simultaneous double contraction either
produces an actual exterior missing-edge path or produces a second, distinct
member of the five-state matching family.  Thus any remaining parity lock
must absorb at least two normalized states geometrically; it cannot be a
one-state parity gadget.

### Theorem 6.3 (rainbow double contraction destroys bilateral XOR)

Retain Theorem 6.1 and suppose the component (D^*), distinct from (D),
is unchanged by the contractions.  Assume (D^*) is three-connected and has
order at least seven.  If the initial double-contraction colouring is rainbow
on the five vertices of (S-I), then one of the following holds:

1. some missing edge of (G[S-I]) has a path with interior in one exterior
   component;
2. (D^*) exposes a nested exact seven-cut; or
3. one of the five normalized states has a two-packet in (D^*), which
   contradicts nonextension over (D).

Consequently the rainbow branch cannot remain in a common-web bilateral XOR
lock.

#### Proof

Let the five missing-cycle edges of the complement of (G[S-I]), which is
a (C_5), be (f_0,\ldots,f_4).  If the uniquely coloured ends of some
(f_j) lie in one bichromatic component of the doubly contracted minor, the
shortest-path and lifting argument in Theorem 6.1 gives outcome 1.  Hence
assume that the ends of every (f_j) lie in different bichromatic
components.

Every normalized state containing (I) is obtained by choosing two
vertex-disjoint edges of this missing (C_5), leaving its fifth vertex as
the singleton.  For such a matching {(f_j,f_k)}, switch one endpoint
component for (f_j) and one for (f_k).  The two switches use disjoint
pairs of colours, so they commute and neither changes the boundary vertices
involved in the other.  Working in the contracted minor preserves equality
at both contracted interface edges.  Thus all five normalized states

\[
I\mid J\mid K\mid\{r\}
\]

extend the unchanged shore (D^*) and the doubly contracted shore.

None extends the original (D).  Indeed, if one did, align its four block
colours with the colouring on (D^*), restore (D), and give (v) one of
the two colours absent from (S).  This would six-colour (G).
Consequently (D^*) has no two-packet for any two pair blocks of any of the
five states.  Indeed, use that packet for two blocks and the apex singleton
shore {(v)} as the connected carrier for the third pair block.  The
packet version of one-way transfer then makes the exact four-block state
extend (D), a contradiction.

Apply Theorem 3.1 of `hadwiger_moser_matching_holonomy.md` to any four of the
five states on the accepting shore (D^*).  It gives either a two-packet,
already excluded, or a nested exact seven-cut.  These are outcomes 3 and 2,
respectively. \(\square\)

### Corollary 6.4 (five-block double traces also descend)

If the initial double-contraction trace has five boundary blocks, it has the
form (I|J|x|y|z).  The three singleton vertices induce a two-edge path in
the missing (C_5).  Unless one of those two edges gives outcome 1, the two
independent Kempe switches give two distinct normalized double-contraction
states, both different from the original XOR deletion state.  All three
states extend the accepting shore and fail on the original split shore, so
the accepting shore is totally packet-deficient for each of them.  Theorem
3.3 of the matching-holonomy note forces an exact seven-cut (or an earlier
packet/path outcome).  Thus the five-block trace also descends.

If the initial trace already has four blocks, only one new normalized state
is forced.  The four-block trace is therefore the sole sharp parity residue;
the five- and six-block traces are closed to a path, packet, or exact
adhesion.

### Lemma 6.5 (the four-block double state avoids a boundary block)

Let Ψ be the normalized four-block state induced by the simultaneous
contraction, and let ψ be a labelled representative.  Define the two
extension relations for the original uncontracted pieces as in (1.2).
Then:

1. the relations are cross-intersecting and have a common point
   (z=(p,q));
2. at least one of (p,q) is a colour used on the boundary;
3. if (p) is the colour of a boundary block (B), then both ends
   (x_1,y_1) of (e_1) are anticomplete to (B); symmetrically, a
   boundary-used (q) makes both ends of (e_2) anticomplete to its block.

If exactly one coordinate is unused, interchanging the two unused colours
gives two common points lying in one row or one column.  If both coordinates
are boundary-used, both interface edges avoid specified boundary blocks.

#### Proof

Nonextension of Ψ over (D) says that every point of the first relation
shares a coordinate with every point of the second.  The double-contraction
colouring restricts on the two pieces to the same ordered terminal pair
(z=(p,q)), proving (z) belongs to their intersection.

Let the two colours absent from the four-block boundary state be (u,v).
Both relations are invariant under their interchange.  If both (p,q) were
unused, the swapped common point would differ from (z) in both coordinates.
Taking one of these points from each relation would violate cross
intersection.  Hence at least one coordinate is boundary-used.  When, say,
(p) is the colour of (B), properness of the double-contraction colouring
forbids an edge from either (x_1) or (y_1), both coloured (p), to any
vertex of (B), also coloured (p).  The remaining assertions follow by
symmetry and by applying the unused-colour swap. \(\square\)

Thus the final four-block parity residue is no longer an abstract two-state
lock: one or both matching-interface edges have a prescribed whole
boundary-colour block from which both ends are excluded.  Any portal exchange
may use the near-full row to route that block through vertices away from the
locked edge.

### Corollary 6.6 (the final residue is a three-mode packet derangement)

Assume in addition that the split shore (D) is a minimum fragment of order
at least six, the accepting shore (D^*) is three-connected of order at least
seven, and no exact seven-cut or exterior-path outcome has occurred.  Let
Φ be the original XOR deletion state and Ψ the distinct normalized
four-block double-contraction state.  Then:

1. (D^*) is totally packet-deficient for Φ and Ψ;
2. for each of the other three normalized Moser modes, (D^*) has a
   two-packet;
3. (D) has a two-packet for every one of the five modes; and
4. for each of the other three modes, the packet types available in (D)
   and (D^*) are disjoint.  Here a packet type records which two of the
   mode's three pair blocks it carries.

#### Proof

The first assertion is one-way packet transfer: both states extend (D^*)
but not (D), and the apex is the carrier for the unused third pair block.
If a third normalized mode were also totally packet-deficient in (D^*),
Theorem 3.3 of the matching-holonomy note would expose an exact seven-cut.
This proves assertion 2.

Assertion 3 is the atomic three-block ownership theorem
`hadwiger_atomic_threeblock_nonowner_collapse.md`, applied to the minimum
fragment (D).

Finally suppose both shores had a packet of the same type for one of the
last three modes.  Use the matching two-packets on the two sides and the apex
as carrier for the third pair block.  Packet transfer in both directions
gives colourings of the two closed shores with the same exact boundary
state.  Align them, glue, and colour the apex with a colour absent from the
four-block boundary state.  This six-colours (G), a contradiction.  Hence
the packet-type sets are disjoint. \(\square\)

The corollary isolates the remaining nonenumerative exchange: three boundary
modes carry complementary packet types on the two shores, while the two
exceptional modes are exactly the deletion and double-contraction locks.

### Corollary 6.7 (the unbounded two-edge lock descends)

Suppose the accepting opposite shore (D^*) has order at least two.  Then
every normalized four-block transition accepted by (D^*) and rejected by
(D) exposes a proper exact seven-adhesion inside (D^*).

#### Proof

The accepting shore (D^*) is totally packet-deficient for the transition
mode: a packet for two pair blocks, together with the apex carrier for the
third, would transfer the exact state to (D).  Apply Theorem 1.2 of
`hadwiger_atomic_threeblock_nonowner_collapse.md` to (D^*).  It gives either
a packet, already excluded, or the asserted exact adhesion. \(\square\)

Thus star/XOR analysis is needed only before normalization.  Once a
four-block matching state is available, every nonsingleton accepting-shore
branch exits through an exact cut, independently of the two shore orders.
In the degree-seven apex setting, a second full singleton shore is a false
twin of the apex: deleting it, colouring the proper minor, and copying the
apex colour back gives a six-colouring.  Hence the accepting exterior shore
is automatically nonsingleton there.
