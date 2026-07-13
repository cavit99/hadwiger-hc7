# Matching holonomy in the common Moser web

## 1. The five normalized states

Use the pure-Moser boundary

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}
\]

and fix the repeated pair \(13\). The matching-normalization theorem in
hadwiger_exact_trace_interface_dichotomy.md produces one of the five
three-pair states

\[
\begin{aligned}
\mathcal M_1&=05\mid13\mid24\mid\{6\},\\
\mathcal M_2&=05\mid13\mid46\mid\{2\},\\
\mathcal M_3&=06\mid13\mid24\mid\{5\},\\
\mathcal M_4&=06\mid13\mid25\mid\{4\},\\
\mathcal M_5&=13\mid25\mid46\mid\{0\}.
\end{aligned}                                      \tag{1.1}
\]

These are exactly the matchings of order three in
\(\overline M\) which contain \(13\).

## 2. Circular-order bound

Say that a circular order of \(\{0,\ldots,6\}\) **realizes**
\(\mathcal M_i\) if, after deleting its singleton vertex, the endpoints
of every two matching edges alternate. Equivalently, the six remaining
vertices have the hexagram order from Corollary 5.1 of
hadwiger_three_pair_common_web.md.

### Lemma 2.1 (at most three matching webs share one face)

No circular order realizes four members of
\(\{\mathcal M_1,\ldots,\mathcal M_5\}\).

The five possible maximal triples are

\[
 \{1,2,3\},\quad \{1,2,5\},\quad \{1,3,4\},\quad
 \{2,4,5\},\quad \{3,4,5\}.                        \tag{2.1}
\]

#### Verification

Fix vertex \(0\) first and enumerate the \(6!=720\) remaining circular
orders. For each matching, test the three pairwise alternation
conditions. The dependency-free verifier
moser_matching_hexagram_order.py asserts that the maximum number of
simultaneously realized matchings is three and prints exactly (2.1).

This finite check is only the exceptional seven-label residue. The
structural input which puts every state on one actual face is the
label-free three-packet synchronization theorem.

## 3. Holonomy theorem for a full shore

### Theorem 3.1 (four states force augmentation or descent)

Let \(G\) be seven-connected, let \(S\) be a seven-cut inducing the
pure-Moser boundary, and let \(D\) be a full component of \(G-S\).
Assume \(D\) is three-connected and \(|D|\ge7\).

Let \(\mathcal F\subseteq\{\mathcal M_1,\ldots,\mathcal M_5\}\).
Then at least one of the following holds:

1. \(|\mathcal F|\le3\);
2. \(D\) exposes a nested exact seven-cut; or
3. one of the states in \(\mathcal F\) has a two-packet and hence gives
   the corresponding rooted capacity augmentation.

In particular, four distinct normalized transition states cannot all
remain in the common-web branch.

#### Proof

If outcome 3 holds there is nothing to prove, so assume every state in
\(\mathcal F\) fails all three pair-packets. Apply Theorem 4.1 of
hadwiger_three_pair_common_web.md to each state.
If any application gives a nested exact cut, outcome 2 holds. Otherwise
each matching has a face containing the full portal sets of its six
matched labels.

Two distinct matchings in (1.1) omit different singleton labels.
Their matched label sets therefore share five labels. If their portal
faces were distinct, their intersection would contain five distinct
portal representatives, using the global SDR of Lemma 2.1 in the
three-pair note. Distinct faces of a three-connected plane graph meet
in at most an edge, a contradiction. Hence every matching in
\(\mathcal F\) uses one common face.

Choose one global SDR for all seven boundary portal sets on that face.
For each matching in \(\mathcal F\), failure of its three pair-packets
forces the three alternation constraints, so the SDR circular order
realizes that matching. Lemma 2.1 gives
\(|\mathcal F|\le3\). Thus if four states were supplied, one of the
geometric packet-failure assumptions must fail, giving outcome 3.
\(\square\)

### Theorem 3.2 (three-state pentagram collapse in a minimum fragment)

Retain the hypotheses of Theorem 3.1 and suppose, in addition, that
(S) has another component (D^*) on its far side and that (D) is a
minimum fragment among all components behind seven-cuts of (G).
Consider any specified family of interface-transition witnesses aligned
to the exact trace (13), and apply the matching-normalization theorem
to every witness.  Then one of the following occurs:

1. one application gives its path outcome;
2. one returned matching state has a two-packet, and hence gives its
   rooted capacity augmentation; or
3. the applications return at most two distinct members of
   \(\{\mathcal M_1,\ldots,\mathcal M_5\}\).

There is no residual three-state common hexagram on a minimum fragment.

#### Proof

Assume that neither of the first two outcomes occurs and that three
distinct matching states are returned.  Thus every application is in its
matching branch, none of these states has a two-packet, and the exact-cut
outcome in the three-pair common-web theorem is impossible by
minimum-fragment atomicity.

Write

\[
 U=\{0,2,4,5,6\}.
\]

The two matching edges of each \(\mathcal M_i\) other than (13) are
vertex-disjoint edges of the missing five-cycle on (U).  As (i) runs
from 1 to 5, these are exactly the five frames

\[
 05\mid24,\quad05\mid46,\quad06\mid24,\quad
 06\mid25,\quad25\mid46.                          \tag{3.1}
\]

Failure of the two-packet for a normalized state therefore makes the
corresponding frame in (3.1) crossless in (D).  Three distinct states
give three distinct crossless frames.

The common-web faces for the three states coincide, by the five-shared-
portal argument in the proof of Theorem 3.1.  Their union contains every
label of (S), because distinct states omit distinct singleton labels.
Consequently all five full portal sets indexed by (U) lie on this one
face.  The occurrence-level synchronization theorem (Theorem 5.1 of
`hadwiger_reserved_connector_rank_leaf.md`) now applies with the two
omitted labels renamed (1,3): three crossless frames force all five
frames to be crossless, in pentagram order.

Apply the disk-curvature theorem of
`hadwiger_moser_pentagram_curvature.md`, again with its two exceptional
boundary labels (w,a) renamed (1,3).  It produces one of the following
vertices (x\in D):

* an interior vertex of degree seven in (G);
* an ordinary facial vertex of degree seven in (G); or
* a triple-lock facial vertex with a shield label (s\in U), for which
  (N_D(s)=\{x\}).

The first two outcomes contradict minimum-fragment choice.  Indeed, if
(d_G(x)=7), then (N_G(x)) is a seven-cut: (x) is an isolated
component of (G-N_G(x)), while the anticomplete far shore (D^*) is
still present.  Hence \(\{x\}\) is a fragment smaller than (D).

In the triple-lock outcome, three-connectivity makes (D-x) connected.
Its internal boundary is \(\{x\}\), it has no contact with the shield
label (s), and relative seven-connectivity gives contact with all six
other labels.  Therefore

\[
 N_G(D-x)=\{x\}\cup(S-\{s\}),                    \tag{3.2}
\]

an exact seven-cut.  The connected set (D-x) is a component behind
this cut (the far shore lies on the other side), and is strictly smaller
than (D), again contradicting minimum-fragment choice.  All curvature
outcomes are impossible.  This proves the theorem. \(\square\)

### Theorem 3.3 (three deficient states force an exact adhesion)

Retain the seven-connected pure-Moser setting of Theorem 3.1, with (D)
three-connected, full, of order at least seven, and with a nonempty far
shore.  Suppose three distinct normalized states are **totally
packet-deficient** in (D): for each state, none of its three choices of two
pair blocks has a two-packet in (D).  Then (D) exposes an exact seven-cut.

No minimum-fragment hypothesis is required.

#### Proof

Apply the three-packet synchronization theorem to each state.  If one
application exposes an exact seven-cut, we are done.  Otherwise the three
states have common portal faces.  The five-shared-portal SDR argument from
Theorem 3.1 shows that these are one and the same face.

After removing the common pair (13), the three states give three distinct
crossless frames of the missing (C_5) on (U=\{0,2,4,5,6\}).  The
occurrence-level synchronization theorem forces all five frames to be
crossless.  Apply the disk-curvature theorem with its two exceptional labels
renamed (1,3).

If curvature gives an interior or ordinary facial degree-seven vertex (x),
then (N_G(x)) is an exact seven-cut: ({x}) is one component after its
deletion and the anticomplete far shore is another.  In the triple-lock
outcome, let (s) be the shield label, so (P_s={x}).  Three-connectivity makes
(D-x) connected.  Its external neighbourhood is contained in

\[
\{x\}\cup(S-\{s\}),
\]

and this set has order seven.  Relative seven-connectivity forces equality,
so it too is an exact seven-cut.  Every curvature outcome therefore exposes
the required adhesion. \(\square\)

## 4. Consequence for the capacity--state exchange

For a fixed accepting shore, normalized non-rainbow transitions from
the opposite shore can occupy at most two of the five matching states
without producing:

* a rooted two-packet;
* a nested exact adhesion; or
* the path outcome of the matching-normalization theorem.

Theorem 3.3 gives the exact-adhesion exit without a minimum-fragment
hypothesis.  If the accepting shore itself is a minimum fragment, Theorem
3.2 rules out that exit as well, so no triple survives at all.

This does not prove that four distinct states must occur. That is the
remaining minor-transition diversity question. The theorem prevents a
future proof from treating arbitrarily many transition states as
independent web embeddings.
