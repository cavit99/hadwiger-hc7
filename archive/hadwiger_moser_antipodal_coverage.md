# Antipodal coverage forbids a universal Moser web

## 1. The circular invariant

Let \(\rho=(s_0,\ldots,s_6)\) be a circular order on seven labels.
Delete one label \(s_k\). The remaining six labels inherit a circular
order. A perfect matching on them is **antipodal** when each matched
pair occupies positions three apart in that six-order.

### Lemma 1.1 (seven-chord bound)

As the deleted singleton varies, every edge belonging to an antipodal
matching is one of the seven chords

\[
 s_i s_{i+3}\qquad(i\in\mathbb Z_7).              \tag{1.1}
\]

Consequently antipodal matchings arising from one fixed seven-label
circular order can collectively cover at most seven distinct pairs.

#### Proof

After deleting \(s_k\), write the remaining sequence as

\[
 s_{k+1},s_{k+2},s_{k+3},s_{k+4},s_{k+5},s_{k+6}.
\]

Its unique antipodal matching is

\[
 s_{k+1}s_{k+4},\quad
 s_{k+2}s_{k+5},\quad
 s_{k+3}s_{k+6}.                                  \tag{1.2}
\]

Every edge in (1.2) has cyclic distance three in the original
seven-order. The union over all \(k\) is contained in the seven pairs
(1.1). \(\square\)

This is the hand invariant behind the finite circular calculation; it
does not depend on the Moser labels.

## 2. Packet-deficient modes synchronize

Let \(G\) be seven-connected, let \(S\) be a seven-cut, and let \(D\)
be a three-connected full shore of order at least seven. Let
\(\mathcal F\) be a family of modes

\[
 A\mid B\mid C\mid\{r\},
\qquad |A|=|B|=|C|=2,                             \tag{2.1}
\]

such that \(D\) has no two-block capacity for any mode in
\(\mathcal F\).

### Theorem 2.1 (universal matching coverage forces an exit)

Assume the graph formed by the pair blocks appearing in
\(\mathcal F\) has no isolated label. Then at least one of the
following holds.

1. \(D\) exposes an exact seven-cut.
2. There is one circular order of all seven labels such that every pair
   block appearing in every mode of \(\mathcal F\) is a distance-three
   chord of that order. In particular the modes collectively use at
   most seven distinct pair blocks.

#### Proof

Apply the three-packet synchronization theorem to each mode. If one
application gives an exact cut, outcome 1 holds. Otherwise each mode
has a face containing all six full portal sets belonging to its pair
blocks.

The faces of any two modes coincide. Their matched label sets have
intersection of order at least five, and the seven-portal Hall lemma
supplies five distinct representatives in the intersection of the two
faces. Distinct faces of a three-connected plane graph meet in at most
one edge, so they cannot be different.

Call the common face \(F\). The pair-block union has no isolated label,
so every label is matched in some mode. Hence every one of the seven
full portal sets lies on \(F\). Choose one SDR of these seven portal
sets on the facial boundary, and let \(\rho\) be its circular order.

For a fixed mode, failure of its three pair-packets makes every two of
its three matching chords alternate. Thus, after deleting its singleton
representative, the six matched representatives have the hexagram
order and the matching is antipodal. Lemma 1.1 says that all its pair
blocks belong to the same seven distance-three chords of \(\rho\).
This proves outcome 2. \(\square\)

## 3. Pure-Moser consequence

The complement of the labelled Moser spindle has ten edges:

\[
 05,06,13,14,15,23,24,25,36,46.                  \tag{3.1}
\]

It has no isolated vertex. Therefore:

### Corollary 3.1

No three-connected full shore of order at least seven can be
packet-deficient for a family of perfect-matching modes whose pair
blocks collectively cover all ten Moser nonedges, unless it exposes an
exact seven-cut.

#### Proof

If no exact cut occurs, Theorem 2.1 and Lemma 1.1 bound the union by
seven pairs, while (3.1) has ten. \(\square\)

This turns a broad family of independently normalized transition states
into one structural contradiction. It is stronger than the fixed-trace
three-state holonomy theorem: the repeated pair and the omitted
singleton may both vary.

The tiny verifier moser_antipodal_coverage_verify.py independently
enumerates the 360 unoriented circular orders. It confirms that the
maximum Moser-nonedge coverage is seven (attained by four orders), so
the hand bound is sharp for this boundary.

## 4. Interface application

Suppose a proper-minor construction can be performed for every Moser
nonedge \(I\) so that, unless it yields a rooted path/packet outcome, it
produces an exact accepted mode containing \(I\) on one fixed shore
\(D\). If \(D\) is packet-deficient for all those accepted modes, then
their pair blocks cover (3.1), because each prescribed \(I\) occurs in
its own mode. Corollary 3.1 gives an exact seven-cut.

Thus the remaining burden in the simultaneous apex/interface
contraction programme is not circular geometry. It is only the
state-production assertion: preserve acceptance by one fixed shore
while normalizing the contracted colouring to a four-block mode
containing each prescribed nonedge. Once that assertion is verified,
all ten traces close at once; no ten-case analysis remains.
