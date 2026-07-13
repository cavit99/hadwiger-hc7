# A common root face has one coherent prism order

## 1. Structural input

Use the minimum all-full-deletion atom and its simultaneous selected roots

\[
                         p_0,\ldots,p_5\in D
\]

for the six cycle labels.  Suppose a three-connected planar torso contains
all six roots on one face, as in outcome 1 of Lemma 6.3 of
`hadwiger_full_deletion_propagation.md`.

### Lemma 1.1 (the whole six-row portal society is facial)

In a target-free atom, the same face contains

\[
                         \bigcup_{i=0}^5 N_D(c_i).   \tag{1.1}
\]

### Proof

Let `F` be the face containing the selected six roots, fix a cycle label
`c_i`, and take any occurrence `x in N_D(c_i)`.  If `x` is already one of
the six selected vertices, it lies on `F`.  Otherwise replace only
`p_{c_i}` by `x`; the other five selected cycle roots remain fixed, so this
is again an SDR of the six cycle portal classes.

Apply the three antipodal-complement rooted-`K_4` views to the new SDR.  A
rooted model in any view gives `K_7` by Theorem 6.1 of the propagation
note, so all three views are cofacial.  The view omitting the antipodal pair
which contains `c_i` is unchanged and has four vertices on `F`; its face
is therefore `F`.  Each of the other two new views shares three unchanged
vertices with its old view on `F`.  Distinct faces of a three-connected
plane graph share at most two vertices, so their face is also `F`.  Both
views contain `x`, proving `x in F`.  QED.

No exchange of colour states is used here.  Literal occurrence usability
is enough because an occurrence outside the current SDR can replace its
own coordinate while the other five coordinates stay fixed.  The universal
`z` portal row is irrelevant to this facial amplification.

### Corollary 1.2 (common-face fragments have order at least ten)

The common-face outcome forces

\[
                              |D|\ge10.              \tag{1.2}
\]

### Proof

Apply strict Hall surplus to the proper six-label set
`\{c_0,...,c_5\}`.  Its portal union has at least seven distinct vertices,
all on one face by Lemma 1.1.  If `n=|D|` and `m=|E(D)|`, a simple plane
graph with a face of length at least seven satisfies

\[
                         m\le3n-10.
\]

The singleton row bound and atomic surplus give `delta(D)>=4`, hence
`m>=2n`.  Therefore `n>=10`.  QED.

The face boundary is a cycle.  Contract every open facial arc between two
consecutive selected roots to an edge, delete everything else in the torso,
retain the six literal portal edges `c_i p_i`, and contract the opposite
full shore to one helper `h`.  For the circular root order `sigma` this
gives a fourteen-vertex quotient `Q_sigma` consisting of

* the `C6+K1` boundary `S`;
* a six-cycle through the roots in order `sigma`;
* the matching `c_i p_i`; and
* `h`, complete to `S`.

Every clique model in `Q_sigma` lifts to the original graph.

## 2. Exact circular-order theorem

### Theorem 2.1 (common-face order lock)

Up to rotation and reversal there are sixty circular orders of the six
selected roots.  The quotient `Q_sigma` contains a `K_7` minor for all but
the following three:

\[
 (0,1,2,5,4,3),\qquad
 (0,1,4,3,5,2),\qquad
 (0,2,1,4,5,3).                                  \tag{2.1}
\]

The three orders form one orbit under the dihedral automorphism group of
the missing six-cycle.  A representative is

\[
                         0,1,2,5,4,3,              \tag{2.2}
\]

the Hamiltonian prism order: it traverses one prism triangle, the matching
edge `25`, the other triangle in reverse, and the matching edge `30`.

Consequently a target-free common-face torso has the unique coherent order
(2.2), up to the natural boundary symmetries.

### Certified proof

The dependency-free verifier `c6_allhub_common_face_order_probe.py`
canonicalizes all `6!/12=60` circular orders.  For each order it enumerates
all connected vertex subsets of the fourteen-vertex quotient and performs
an exact recursive search for seven pairwise adjacent disjoint branch
sets.  It asserts that the complete negative list is exactly (2.1), and
prints

```text
orders 60 negative 3
(0, 1, 2, 5, 4, 3)
(0, 1, 4, 3, 5, 2)
(0, 2, 1, 4, 5, 3)
```

The search is exhaustive: every branch set is a connected subset and the
recursion tests disjointness and all pairwise adjacencies.  A positive
certificate is a literal quotient minor and therefore lifts through the
facial-arc contractions.  The three negative rows are not claimed to make
the original graph `K_7`-minor-free; they are precisely the orders for
which this forced quotient alone does not close.  QED.

## 3. Consequence

The common-face outcome is no longer an arbitrary circular society.  Its
six portal classes have one fixed prism-compatible rotation, while every
internal edge still carries the endpoint-complete palette warehouse and
every class has a reserve portal.  Thus the remaining operation theorem
only has to break one coherent annular order, not compare sixty unrelated
orders.
