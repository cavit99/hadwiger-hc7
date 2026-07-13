# Antipodal edge coverage at a bilateral Moser adhesion

## 1. The odd-boundary chord lemma

The circular obstruction is uniform.  Put (n=2q+1), delete one of
(n) circularly ordered occurrences, and partition the other (2q)
occurrences into (q) pairs whose chords are pairwise alternating.

### Lemma 1.0 (only (2q+1) possible antipodal pairs)

Every matched pair has cyclic distance (q) (equivalently (q+1))
in the original ((2q+1))-order.  Thus the union of every such matching,
over every deleted occurrence, uses at most the (2q+1) edges of the
distance-(q) circulant cycle.

#### Proof

Pairwise alternating disjoint chords on (2q) points have endpoint word

\[
              e_1,e_2,\ldots,e_q,e_1,e_2,\ldots,e_q
\]

up to relabelling and reversal.  Hence each pair is antipodal after the
deletion, with (q-1) surviving occurrences on either open arc.  Before
the deleted occurrence was removed, one arc had (q) occurrences and
the other had (q-1).  The endpoints therefore have cyclic distances
(q) and (q+1) in the odd order.  There is exactly one such unordered
pair starting at each of the (2q+1) positions. \(\square\)

The seven-vertex form used below is the case (q=3).

Let (z_0,ldots,z_6) occur in this circular order.  Delete one
occurrence (z_s), and pair the other six occurrences so that the
three pairs are pairwise alternating.

### Lemma 1.1

Every pair in the resulting matching has the form

\[
                         z_i z_{i+3}
\]

with indices modulo seven.  Consequently the union of all pairwise
alternating matchings obtained after all seven possible deletions uses
at most the seven distance-three chords of the circular order.

#### Proof

This is Lemma 1.0 with (q=3). \(\square\)

This elementary observation is stronger than a bound on the number of
matching states: no family of packet-deficient matching states supported
by one facial order can cover more than seven different boundary pairs.

## 2. A matching-extension fact for the pure Moser spindle

Let (M) be the labelled Moser spindle with

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

### Lemma 2.1

Let (I,J) be disjoint nonedges of (M).  The three vertices outside
(I\cup J) contain a nonedge of (M).

#### Proof

Otherwise those three vertices form a triangle of (M).  The only
triangles of the displayed spindle are

\[
                         012,quad034,quad126,quad345.
\]

On their respective four-vertex complements, the nonedges of (M) are

\[
 \{36,46\},\quad \{15,25\},\quad \{05\},\quad \{06\},
\]

respectively.  None of these four graphs has a matching of order two,
contrary to the existence of the disjoint nonedges (I,J). \(\square\)

It follows that any boundary state on seven Moser vertices with one
specified two-vertex block can be Kempe-normalized either to a
(2+2+2+1) state containing that block or to an actual missing-edge
path: from six blocks first merge a nonedge among the other five roots;
from five blocks use Lemma 2.1 on the remaining three singleton roots.

## 3. Bilateral antipodal-cover exchange

Let (G) be a hypothetical seven-contraction-critical graph.  Let
(v) have degree seven and let (S=N_G(v)) induce the pure Moser
spindle.  Let (D,D^*) be distinct components of (G-N[v]), with
(D^*) full to (S).  Let (e_1,e_2) be vertex-disjoint edges in
(D).  Other exterior components, if present, are left unchanged.

For every nonedge (I\subseteq S), simultaneously contract

\[
                    G[\{v\}\cup I],qquad e_1,qquad e_2. \tag{3.1}
\]

The resulting graph is a proper minor.  Expand (I), delete (v),
and expand the two internal contractions after deleting their edges.
The induced boundary state has (I) as an exact block, and both
interface pairs initially have equal colours.  Subsequent Kempe
normalization is performed in the edge-deleted graph; it need not preserve
those two interface equalities.

### Theorem 3.1 (ten nonedges versus seven facial chords)

Assume that (D^*) is three-connected and has at least seven vertices.
Then one of the following occurs.

1. For one choice of (I), Kempe normalization of (3.1) supplies a
   missing-edge path whose interior lies in one exterior component.
2. A normalized state supplied by (3.1) has a two-packet in (D^*).
3. The shore (D^*) exposes an exact seven-cut.

In a capacity-state lock in which every normalized state from (3.1)
is known not to extend the uncontracted target containing (D), outcome
2 is impossible: the packet, together with the apex carrier
({v}), transfers that state to the target.  Hence such a lock must
give an actual path or an exact adhesion.

#### Proof

Suppose outcome 1 never occurs.  Expand the two interface contractions
after deleting their edges and apply the two Kempe merges described after
Lemma 2.1 in that edge-deleted graph.  The switches avoid the colour of
the apex block, so they preserve the exact trace (I), but they need not
preserve equality at the two interface pairs.  For every nonedge (I) this
gives an optimal state

\[
                      I\mid J\mid K\mid\{r\}.     \tag{3.2}
\]

It extends the unchanged shore (D^*) and the target with the two interface
edges deleted.
It does not extend the original target: aligning such an extension with
the unchanged parts of the minor and giving (v) either of the two
colours absent from (S) would six-colour (G).

Choose one state (3.2) for each of the ten nonedges (I).  The pair
blocks of the chosen states therefore cover all ten nonedges of (M).

If outcome 2 never occurs, all three pair-packets fail in (D^*) for
every chosen state.  The three-packet synchronization theorem applies.
If it gives an exact cut, outcome 3 holds.  Otherwise the six portal
classes of every state lie on one face of the unique plane embedding of
(D^*).

All these faces are the same.  Two states with different singleton
labels share five portal classes; two with the same singleton share six.
The seven-portal Hall lemma supplies distinct representatives, while two
distinct faces of a three-connected plane graph meet in at most one edge.
Thus one fixed face contains all relevant portal classes.

Choose one global system of seven distinct portal representatives on
that face.  Packet failure makes the three pair blocks of every state
pairwise alternating in the induced circular order after its singleton
is removed.  Lemma 1.1 says that every pair block belongs to one fixed
set of seven distance-three chords.  This contradicts the fact that the
chosen states cover all ten nonedges of the Moser spindle.  Hence one of
the three outcomes must occur.

For the final assertion, suppose a state in outcome 2 has pair blocks
(I,J,K).  Use the two disjoint carriers in (D^*) for two blocks and
the connected apex star through (v) as a carrier for the third.  The
packet-transfer contraction colours the unchanged target with exact
state (3.2), contradicting its established nonextension. \(\square\)

## 4. Significance

The theorem removes the fixed-trace limitation of the earlier five-state
holonomy argument.  Its finite boundary input is only the label-free
fact that a circular order of seven points has seven distance-three
chords; the ten Moser nonedges cannot all be hidden in one packet-deficient
web.

The remaining path outcome is geometric rather than state-theoretic.
It must be combined with the covering split or the reserved connector.
But a bilateral shore can no longer absorb every apex-aligned internal
minor transition merely by changing among common-web boundary states.

The dependency-free script `moser_antipodal_edge_cover_probe.py`
independently checks the sharp count.  It finds maximum coverage seven;
the proof of Lemma 1.1 is the hand certificate.
