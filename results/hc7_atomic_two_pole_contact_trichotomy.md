# Two-pole contact trichotomy for the regenerated spanning `K_6`

**Status:** proved local lemmas; the proposed `|C_z\cup C_u|=5`
noncycling handoff is **not** supplied by the one-hole height gap.  This
note isolates the exact residual which still needs the twin-lock geometry.

## 1. Setup

Let `G` be seven-connected and `K_7`-minor-free, let `zu` be an edge, and
let

\[
                       \mathcal M=(F_1,\ldots,F_6)
\tag{1.1}
\]

be a spanning `K_6` model in `G-{z,u}`.  Put

\[
 C_z=\{i:E(z,F_i)\ne\varnothing\},\qquad
 C_u=\{i:E(u,F_i)\ne\varnothing\},
\tag{1.2}
\]

and write

\[
 r=|C_z\cup C_u|,\qquad c=|C_z\cap C_u|.
\tag{1.3}
\]

In the atomic twin seam, the audited identity `chi(G-{z,u})=6` and known
`HC_6` first give a `K_6` minor.  The graph `G-{z,u}` is connected, so
unused components can be assigned successively to adjacent branch bags,
extending the model to a spanning one.  Nothing below roots that model at
palette colours.

## 2. The exact contact-only clique outcomes

### Lemma 2.1 (two-pole contact forcing)

Each of the following gives a literal `K_7` model.

1. `r=6`.
2. `c>=5`.
3. `c>=4` and there are distinct rows
   `a in C_z-C_u` and `b in C_u-C_z`.

Consequently, in the target-free branch,

\[
                         r\le5,\qquad c\le4,             \tag{2.1}
\]

and, when `c=4`, the two contact sets cannot have exclusive rows on both
sides.

#### Proof

If `r=6`, the connected bag `{z,u}` is adjacent to every `F_i`; use it
and all six model rows.

If `c>=5`, use the singleton bags `{z},{u}` and five common rows.  The
literal edge `zu` supplies the pole--pole adjacency.

In the third case retain four common rows and replace `F_a,F_b` by their
connected union.  That union meets `z` through `F_a`, meets `u` through
`F_b`, and is adjacent to every retained common row.  Together with the
two singleton poles it gives seven pairwise adjacent connected bags.
The final assertions are the contrapositives.  \(\square\)

For the construction with `{z}` and `{u}` separate and two rows merged,
the condition is exact: every one of the four unmerged rows must be
common, while the merged pair must meet both contact sets.  Absorbing one
pole into one row and retaining the other pole as a singleton adds no
target-free contact pattern: the singleton pole must meet the other five
rows and the absorbed pole must meet the row into which it is absorbed,
which already makes `r=6`.

## 3. What contact orders five and four really imply

Whenever the family below is nonempty, let

\[
 \mu=\min\{|A|:A\text{ is the deficient centre of a labelled
 one-/two-hole near-}K_7\text{ model in }G\}.             \tag{3.1}
\]

### Lemma 3.1 (joint contact five)

If `r=5`, then

\[
                 \{z,u\},F_1,\ldots,F_6                \tag{3.2}
\]

is a labelled one-hole model with centre order two.  Moreover `mu=1`.

#### Proof

Exactly one row is anticomplete to `{z,u}`, while the other five meet it,
so (3.2) is a one-hole model and `mu<=2`.  If `mu=2`, the audited
one-hole height-gap theorem says that every one-hole centre has order at
least `mu+1=3`, contradicting (3.2).  Since deficient centres are
nonempty, `mu=1`.  \(\square\)

The conclusion is **not** a strict `S1` handoff.  It says only that some
singleton one-/two-hole model exists, possibly on a completely different
six-row frame; the minimization supplies no transition from (3.2) to that
model.  At `mu=1` the height theorem has no orientation, and legal
single-gate rotations can be exact involutions.  In the atomic kernel the
pair `{z,u}` itself cannot be the fixed-pair terminal, since
`G-{z,u}` contains the displayed `K_6` minor and therefore is not
`K_5`-minor-free.
Thus the following extra output is still required before (3.2) is an
accepted terminal of the atomic theorem:

* a literal `K_7` or a fixed pair whose deletion is `K_5`-minor-free;
* a common proper-minor equality state; or
* a global state-sensitive rank which orients the whole `mu=1` rotation
  component, not merely the move into it.

### Lemma 3.2 (joint contact four)

If `r=4`, then `{z,u}` and the six rows form a labelled two-hole model of
centre order two.  Hence `mu<=2`.  More precisely:

* if `mu=1`, a singleton normalized near model exists elsewhere;
* if `mu=2`, the displayed pair-centred model is already at the minimum
  two-hole floor; and
* if either pole contacts all four rows in the union, that pole itself is
  a singleton two-hole centre on the same six-row frame.

None of these alternatives orients a two-hole rotation component.

#### Proof

The pair centre meets exactly four of the six foreign rows, proving the
first assertion.  The three bullets follow immediately from the
definition of `mu` and from (1.2).  Exact reversibility of single-gate
rotations shows why minimum centre order alone is not a noncycling rank.
\(\square\)

If `r<=3`, neither the pair `{z,u}` nor either singleton pole, on this
fixed frame, is a one-/two-hole centre.  A near-model output in that range
therefore needs a literal row split, a contact-increasing re-choice of the
model, or an independently regenerated frame.

## 4. The positive same-row split-or-separator theorem

### Lemma 4.1 (rooted row-duty split or actual separator)

Suppose that one common row `F_h` contains distinct vertices

\[
                  x\in N(z)\cap F_h,\qquad
                  y\in N(u)\cap F_h.                    \tag{4.1}
\]

Then there is a partition

\[
                         F_h=X_z\mathbin{\dot\cup}X_u   \tag{4.2}
\]

into nonempty connected adjacent sets with `x in X_z` and `y in X_u`.
For every such partition, one of the following holds.

1. Both `X_z` and `X_u` meet every foreign row `F_i`, `i ne h`; then
   `G` contains a literal `K_7` minor.
2. One of `X_z,X_u`, say `Y`, misses a foreign row; then `N_G(Y)` is an
   actual vertex separator.  In particular

   \[
                              |N_G(Y)|\ge7.              \tag{4.3}
   \]

   If equality holds, every component of `G-N_G(Y)` is
   `N_G(Y)`-full.

#### Proof

Take a spanning tree of `G[F_h]` and delete any edge on its `x-y` path.
The two resulting tree components give (4.2).

In the first outcome use

\[
 \{z\}\cup X_z,\quad \{u\}\cup X_u,
 \quad F_i\ (i\ne h).                                  \tag{4.4}
\]

The first two bags are connected, disjoint, and adjacent through `zu`.
They each meet all five retained rows, which remain pairwise adjacent.
Thus (4.4) is a literal `K_7` model.

Otherwise choose a foreign row `F_j` anticomplete to `Y`.  The connected
set `Y` is one component-side of `G-N_G(Y)`, while the nonempty connected
bag `F_j` lies outside `Y union N_G(Y)`.  Hence `N_G(Y)` is an actual
separator.  Seven-connectivity proves (4.3).  If its order is seven and
some component `C` of its deletion misses a boundary vertex `s`, then
`N(C) subseteq N_G(Y)-{s}` would be a separator of order at most six.
Thus every component is full.  \(\square\)

In the separating twin response, the two end segments of the literal
cycle through `zu` have distinct first-hit vertices in the spanning model.
If those hits lie in one row, Lemma 4.1 applies exactly: the branch is a
literal `K_7` or an actual separator.  An order-seven separator is a real
`S2/S3` interface, but it is a **ranked state handoff only after** a named
proper-minor operation supplies its exact state and a noncycling rank.
An order greater than seven is an `S4` input, not a terminal by itself.

## 5. Contact multiplicity and the remaining low-union cell

Because the model is spanning, every neighbour of either pole other than
the other pole lies in one of its contacted rows.  Seven-connectivity
therefore gives

\[
 \sum_{i\in C_z}|N(z)\cap F_i|\ge6,\qquad
 \sum_{i\in C_u}|N(u)\cap F_i|\ge6.                     \tag{5.1}
\]

Consequently each pole has two distinct neighbours in some contacted row
whenever `r<=4`.  More jointly, if

\[
 m_i=|N(z)\cap F_i|+|N(u)\cap F_i|,
\]

then

\[
             \max_{i\in C_z\cup C_u}m_i
                    \ge \left\lceil\frac{12}{r}\right\rceil . \tag{5.2}
\]

These are portal multiplicities, not labelled duties.  In particular they
do not imply that one common row has distinct roots for both poles.

For a useful extremal formulation, choose the spanning model to maximize
`r`.  A **contact-increasing row transfer** consists of distinct rows
`F_i,F_j`, with `j notin C_z union C_u`, and a proper nonempty set
`Y subset F_i` such that:

1. `Y` and `F_i-Y` are connected and adjacent;
2. `Y` meets `F_j` and at least one pole;
3. `F_i-Y` retains every old `F_i-F_k` duty for `k ne i,j`; and
4. `F_i-Y` retains every old pole contact with `F_i`.

Replacing

\[
                   F_i\longmapsto F_i-Y,qquad
                   F_j\longmapsto F_j\cup Y             \tag{5.3}
\]

is a spanning `K_6` model with strictly larger joint contact.  Therefore
no such transfer exists in a contact-maximal model.

The proof is literal: the cut edge in item 1 restores the
`(F_i-Y)-(F_j union Y)` adjacency, old `F_j` preserves all of its foreign
duties, item 3 preserves those of the residual donor, and item 4 prevents
the loss of any old pole row.  Item 2 creates the new pole contact at
`F_j union Y`.

Thus the exact residue for `r<=4` is not a contact count.  It is one of:

* distinct pole roots in a common row, reduced by Lemma 4.1 to `K_7` or
  an actual separator;
* a contact-increasing row transfer, contradicting extremality; or
* a **row-duty lock**: every candidate pole-rooted peel toward an
  uncontacted row disconnects the donor, monopolizes a foreign-row duty,
  or consumes an old pole contact.  Decoding that last lock is precisely
  where the response-matched Kempe paths and proper-minor states must be
  used.

## 6. Sharp guardrail for the height-gap inference

The implication in Lemma 3.1 cannot be promoted to a noncycling handoff
using only seven-connectivity, `K_7`-minor-freeness, and model contacts.
Use the standard icosahedron `I` with vertices

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and edges (indices modulo five)

\[
 tu_i,\ bw_i,\ u_iu_{i+1},\ w_iw_{i+1},\
 u_iw_i,\ u_iw_{i-1}.
\]

Let `G_0=K_2 vee I`, with universal adjacent vertices `p,q`, and take the
two poles `z=u_3`, `u=u_4`.  In `G_0-{u_3,u_4}` the six bags

\[
 \{t,u_0\},\quad \{u_1\},\quad \{u_2\},\quad
 \{b,w_0,w_1,w_2,w_3,w_4\},\quad \{p\},\quad \{q\}     \tag{6.1}
\]

form a spanning `K_6` model.  Their pole contact sets are

\[
 C_{u_3}=\{1,3,4,5,6\},\qquad
 C_{u_4}=\{1,4,5,6\}.                                  \tag{6.2}
\]

Thus the joint contact is exactly five.  The singleton `u_3` is already a
one-hole centre on the same six rows, so `mu=1`.  The independently
audited model in `hc7_near_k7_rotation_involution_barrier.md` gives an
exact balanced two-cycle of singleton one-hole rotations in this same
host.  The graph is seven-connected and `K_7`-minor-free.

This is not an atomic counterexample: it is six-colourable and the pair
`{p,q}` is a valid coherent terminal.  It proves the precise methodological
point needed here: **the contact-five model plus the height-gap theorem
does not itself identify that fixed pair and does not orient the `mu=1`
rotation.**
Strong contraction-criticality or the twin-lock state data must perform
that additional step.

The exact inverse rotation and its scope are proved and audited in
`../barriers/hc7_near_k7_rotation_involution_barrier.md` and its adjacent
audit.

The companion audited file
`../barriers/hc7_same_row_split_two_apex_icosahedron.md` strengthens this
guardrail in the direction of the separating decoder.  In another choice
of poles and spanning rows in the same graph, the joint contact five is
globally maximal, the two first hits are distinct vertices of one
size-two row, and that row has no duty split.  Lemma 4.1 returns the
literal separator there; the graph's coherent apex pair is the intended
terminal.  Thus contact maximality and balanced bag minimality do not
replace the proper-minor response either.

## 7. Decoder consequence

The regenerated model gives the following rigorous branch structure.

\[
\begin{array}{c|l}
r=6 & \text{literal }K_7;\\
r=5 & \text{one-hole centre of order two and }\mu=1,
       \text{ but no automatic ranked handoff};\\
r=4 & \text{two-hole centre of order two at level }\mu\le2,
       \text{ but no automatic ranked handoff};\\
r\le3 & \text{no one-/two-hole output on this frame.}
\end{array}
\]

For `r<=4`, the positive geometric promotion is Lemma 4.1 or the strict
model augmentation (5.3).  After both fail, the remaining object is a
literal row-duty lock.  A proof of the atomic double-lock theorem must
show that its response bundle either unlocks one of those transfers,
attains a common exact state across the resulting separator, or names the
same global fixed pair.  Raw contact order cannot discharge that step.
