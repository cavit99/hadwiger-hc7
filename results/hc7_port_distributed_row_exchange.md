# Distributed-row packets in a port-rooted `K_4`

## Status and role

This is an **audited local theorem**.  It weakens the
pointwise three-row hypothesis in
`../results/hc7_port_matching_cycle_exchange.md` in two genuinely
uncontracted ways.

* A selected port may be thickened to a whole cyclic sector, and the three
  row contacts may occur anywhere in that sector.
* If two rooted corners obtain their only contact with one row from one
  common packet, that packet may be promoted into the row.  An off-skeleton
  packet gives `K_7`; a packet occupying the corner-to-corner skeleton path
  sacrifices exactly that one clique edge and gives `K_7^-`.

The second operation is the four-corner analogue of common-row promotion.
It is useful precisely when a nonsingleton carrier stores a row contact
between two port roots rather than at either literal port edge.

The note also records the only safe dynamic alternative at a packet: an
equality partition on the **actual full adhesion** produced from both open
shores.  No palette colour is identified with a branch-bag label.

## 0. The global-contact shortcut is false

It is not enough that every fixed row meet each of the two port shores.
Here is a small literal witness.

Let

\[
 C_L=(\ell _0\ell _1\ell _2\ell _3\ell _0),\qquad
 C_R=(r_0r_2r_1r_3r_0),
\]

join `ell_i` to `r_i` for every `i`, and add a triangle
`f_0f_1f_2f_0`.  For `j=0,1,2`, add only the two cross edges
`f_j ell_j` and `f_j r_j`.  The two port orders differ, and each singleton
row `f_j` meets both shores, but the graph has no `K_7` minor.

Indeed, the elimination order

\[
 \ell _3,f_0,\ell _1,r_3,r_2,f_1,f_2,
 \ell _0,\ell _2,r_0,r_1
\]

has filled-neighbour orders respectively

\[
                         3,4,4,4,4,5,4,3,2,1,0.
\]

It therefore gives a tree decomposition of width at most five.  Since
treewidth is minor-monotone and `tw(K_7)=6`, the graph has no `K_7`
minor.  Thus a proof must retain which returned corner owns each literal
row contact; shore-level incidence cannot be contracted first.

## 1. Thick-port sectors lift through the cycle exchange

Let `L,R` be disjoint graphs with port cycles `C_L,C_R` and literal
matching edges

\[
                  M=\{\ell_i r_i:i\in I\}.
\]

Fix four indices `J={1,2,3,4}` whose orders on the two cycles differ up
to reversal.  A **sector system** for `J` consists, for each `i in J`,
of a subpath `A_i` of `C_L` containing `ell_i` and a subpath `B_i` of
`C_R` containing `r_i`, such that

1. the four `A_i` are pairwise vertex-disjoint and no `A_i` contains
   `ell_h` for `h!=i`;
2. the four `B_i` are pairwise vertex-disjoint and no `B_i` contains
   `r_h` for `h!=i`.

Put

\[
                       T_i=A_i\cup \ell_i r_i\cup B_i.       \tag{1.1}
\]

The `T_i` are pairwise disjoint connected literal port sectors.  The
paths are allowed to have arbitrary order and may contain arbitrarily
many vertices; the only restriction is non-overlap at the four selected
ports.

### Theorem 1 (distributed sector lift)

Let `F_1,F_2,F_3` be pairwise disjoint connected pairwise adjacent sets,
disjoint from `L union R`.  In the setting above, the host has four
pairwise disjoint connected pairwise adjacent branch sets

\[
                         Q_1,Q_2,Q_3,Q_4                 \tag{1.2}
\]

with `T_i subseteq Q_i` for each `i`.

Consequently:

1. if every `T_i` is adjacent to every `F_j`, then the host has a
   literal `K_7` minor;
2. if among the twelve pairs `(T_i,F_j)` at most one is nonadjacent,
   then the host has a literal `K_7` or `K_7^-` minor.

Thus the three contacts of one port may be distributed anywhere over two
nonsingleton cyclic sectors; they need not occur at either endpoint of
the matching edge.

#### Proof

First discard all matching edges outside `J`.  Contract every `A_i`
inside `C_L` to `ell_i` and every `B_i` inside `C_R` to `r_i`, without
contracting any retained matching edge.  Because the
selected subpaths are disjoint and contain no other selected port, the
images of `C_L,C_R` are still cycles through the four named port
endpoints in their original cyclic orders.

Apply the audited port-matching cycle exchange to these two image cycles
and the four retained matching edges.  Their orders differ, so it returns
a rooted `K_4` model whose `i`-th branch set contains the whole image of
`ell_i r_i`.  Lift the contractions.  The branch set containing that
image acquires all of `A_i union B_i`; no other branch set acquires a
vertex of those two paths.  This gives (1.2) with `T_i subseteq Q_i`.

If all twelve contacts hold, the seven sets

\[
                         Q_1,Q_2,Q_3,Q_4,F_1,F_2,F_3
                                                               \tag{1.3}
\]

are connected, disjoint and pairwise adjacent.  If one displayed
cross-pair is absent, all pairs in (1.3) except possibly that pair are
adjacent.  The same seven sets are then a `K_7^-` model (or a `K_7`
model if later parts of the lifted branch sets repair the nominally
absent contact).  Every adjacency used here is a literal host edge.
\(\square\)

### Theorem 1.5 (simultaneous off-skeleton packet repair)

Let `Q_1,...,Q_4` be any four pairwise disjoint connected pairwise
adjacent branch sets, and let `F_1,F_2,F_3` be fixed rows as above.  Let
`mathcal K` be a family of pairwise disjoint connected sets, disjoint
from all seven displayed bags.  Assign each `K in mathcal K` one row
label `lambda(K) in {1,2,3}` and assume

\[
                         K\sim F_{\lambda(K)}.          \tag{1.4}
\]

Call a corner-row duty `(i,j)` **repaired** when either
`Q_i` is adjacent to `F_j`, or some packet `K` with `lambda(K)=j` is adjacent to
`Q_i`.  If all twelve duties are repaired, the host has a literal `K_7`
minor.  If at most one duty is unrepaired, it has a literal `K_7` or
`K_7^-` minor.

#### Proof

For each row put

\[
                F_j'=F_j\cup
                     \bigcup\{K\in\mathcal K:\lambda(K)=j\}. \tag{1.5}
\]

Every `F_j'` is connected because each of its added connected packets is
adjacent to the original connected core `F_j`.  The three enlarged rows
are pairwise disjoint because the packets are pairwise disjoint and each
has one label; they remain pairwise adjacent through the three old row
edges.  They are disjoint from all `Q_i`.

For a repaired duty, either its old `Q_i-F_j` edge survives, or the
packet witnessing the repair supplies a literal `Q_i-F_j'` edge.  Thus
the seven bags

\[
                          Q_1,Q_2,Q_3,Q_4,F_1',F_2',F_3'
                                                               \tag{1.6}
\]

have all clique adjacencies, except possibly the one unrepaired duty.
They give the asserted `K_7` or `K_7^-` model. \(\square\)

Theorem 1.5 is a simultaneous row-promotion operation.  A single packet
may repair several corners of its assigned row, but it is never assigned
to two different rows.  Consequently the failure of off-skeleton repair
is a literal packet-incidence deficiency rather than a failure of row
connectivity.

## 2. One common packet may replace two point contacts

The next statement starts with the rooted subdivision before its six
connections are cut into minor bags.  This is exactly the object built in
the mismatch proof of the port-cycle theorem.

A **rooted `K_4` expansion** consists of four pairwise disjoint connected
root sets `T_1,...,T_4` and, for every pair `i<k`, a `T_i-T_k` path
`P_ik` such that

* the interior of every `P_ik` avoids all root sets; and
* the six path interiors are pairwise disjoint.

The first and last edges of a path have one end in the corresponding root
set.  Additional host edges are not excluded.

### Theorem 2 (common packet promotion)

Let `T_1,...,T_4` be a rooted `K_4` expansion, with each `T_i`
containing a different literal port edge returned by the port-cycle
exchange.  Let `F_1,F_2,F_3` be fixed rows as in Theorem 1, and assume
the four roots and all six expansion-path interiors are disjoint from
`F_1 union F_2 union F_3`.  Fix distinct
corners `p,q` and one row `F_a`.  Assume

\[
 T_i\sim F_j\quad\text{for every }(i,j)
       \notin\{(p,a),(q,a)\}.                         \tag{2.1}
\]

Suppose one of the following two types of nonempty connected **common
packet** exists.

1. An off-skeleton packet `K` is disjoint from all roots, all three fixed
   rows and all six expansion-path interiors, and

   \[
                      K\sim T_p,\qquad K\sim T_q,
                      \qquad K\sim F_a.                \tag{2.2}
   \]

2. An on-skeleton packet `K` is a nonempty subpath of the interior of
   `P_pq`, is disjoint from the three fixed rows, and `K` is adjacent to
   `F_a`.

In the off-skeleton case the host has a literal `K_7` minor.  In the
on-skeleton case it has a literal `K_7` or `K_7^-` minor; in the latter
model the only absent pair is the pair of corner bags rooted at
`T_p,T_q`.

#### Proof

First suppose `K` is off the skeleton.  Cut each of the six
expansion paths at one edge and assign the two remaining segments to its
two roots.  This gives four disjoint connected pairwise adjacent bags
`Q_i` with `T_i subseteq Q_i`, while leaving `K` unused.  Replace

\[
                            F_a\longmapsto F_a'=F_a\cup K.
                                                               \tag{2.3}
\]

The new row is connected by the last contact in (2.2).  It meets the
two formerly deficient corner bags through the first two contacts in
(2.2), and it retains every old edge from `F_a` to the other two corner
bags and to the other fixed rows.  All other corner-row edges follow
from (2.1).  The four corner bags retain their `K_4` adjacencies.  Hence

\[
                    Q_1,Q_2,Q_3,Q_4,F_a',F_b,F_c       \tag{2.4}
\]

are seven literal clique branch sets.
Here `{b,c}={1,2,3}-{a}`.

Now suppose `K` is an on-skeleton packet.  Do the same cutting on the
other five paths.  Removing the nonempty subpath `K` from `P_pq` leaves
an initial segment at the `T_p` end and a final segment at the `T_q`
end (either may have no internal vertex).  Assign the initial segment to
the `p`-corner bag and the final segment to the `q`-corner bag.  The two
boundary edges of `K` give `Q_p-K` and `K-Q_q` contacts.  The four corner
bags remain connected and pairwise disjoint.  Every corner pair except
possibly `Q_p,Q_q` retains its cut edge on one of the other five paths.
Promote `K` into `F_a` as in (2.3).  The seven bags (2.4) now have every
required adjacency except possibly `Q_pQ_q`.  An additional host edge
between those two bags gives `K_7`; without it they give `K_7^-`.

No vertex of a fixed row is made monochromatic or contracted into a
palette colour.  The operation is only a reassignment of the displayed
connected packet to the displayed connected row. \(\square\)

### Corollary 2.1 (the minimum-centre floor is preserved)

In the on-skeleton case of Theorem 2, suppose `T_p=X`, `|X|=mu>=2`, where `mu` is
the height-gap theorem's global minimum centre order among all exact
one- and two-hole near-`K_7` models in a `K_7`-minor-free host,
suppose the on-skeleton packet contains the first internal vertex of
`P_pq` at the `X` end, and cut the other expansion paths at their first
edges incident with `X`.  Then the `K_7^-` model returned by the proof
has the **same literal bag `X`** as a one-hole centre.
Consequently it is forbidden by the audited one-hole height-gap theorem.

#### Proof

On each of the three paths incident with `X`, assign no internal vertex
to the `X`-bag.  On the sacrificed path this is possible because the
packet begins at the first internal vertex; assign every vertex after the
packet to the opposite corner.  On each other path, assign its internal
segment to the opposite corner and retain the first edge as the corner
adjacency.
Thus `Q_p=X` literally.  The only absent pair in (2.4) is `XQ_q`, so
if that edge exists the bags already give `K_7`, and otherwise `X` is a
one-hole centre of order `mu`.  Every other bag may have expanded, but
this is irrelevant to the height parameter, which counts the deficient
centre only; the six other bags are still pairwise adjacent by the five
unsacrificed expansion paths and the fixed-row clique.  The height-gap
theorem says that every one-hole centre has order at least `mu+1`.
\(\square\)

This corollary is why one shared packet is terminal at the floor even
when it does not produce `K_7` outright.

## 3. The safe dynamic output is an actual-adhesion equality state

The packet exchange has a second, independent terminal output when the
packet is an open shore rather than a freely promotable path.

### Lemma 3 (opposite-shore equality splice)

Let `G` be a graph all of whose proper minors are six-colourable.  Let
`(C,O)` be a separation with literal common boundary

\[
                         S=V(C)\cap V(O),                \tag{3.1}
\]

and nonempty open shores.  Let `rho` be a deletion or contraction
supported strictly in `V(C)-S`, and let `sigma` be one supported strictly
in `V(O)-S`.  Write `G rho` and `G sigma` for the two resulting proper
minors.  If six-colourings of `G rho` and `G sigma` induce the same
equality partition `Pi` of the **actual vertices of `S`**, then `G` is
six-colourable.

#### Proof

The operation `rho` leaves `O` unchanged, so restrict its minor colouring
to `O`.  The operation `sigma` leaves `C` unchanged, so restrict its minor
colouring to `C`.  Their labelled equality partitions on `S` agree.
Permute the six colour names on one side so that every boundary block has
the same colour on both sides, then unite the two colourings.  A separation
has no edge between the open shores, so this is a proper colouring of the
original graph. \(\square\)

In particular, if a common row packet is trapped behind an actual
adhesion and cannot be promoted without consuming a boundary vertex, a
matching operation state from the opposite open shore is terminal.  A
colouring of a contracted row, or agreement only on row labels, does not
satisfy Lemma 3.

## 4. Exact infinite family closed and exact residue

Theorems 1 and 2 close the following unbounded distributed-contact
family.

* Four mismatched literal port sectors can be chosen disjointly.
* After simultaneous repair by a disjoint off-skeleton packet family,
  every sector-row duty is present except possibly two duties belonging
  to the same row and two corners.
* In the two-duty case, the connecting skeleton path contains a connected
  packet meeting that row (or an off-skeleton packet meets both corners
  and the row).

The result is `K_7` or `K_7^-`; under the extra first-edge hypothesis of
Corollary 2.1 the exact floor centre is preserved.  No bound is imposed
on either shore, any sector, any row, or the common packet.
The arbitrary one-duty `K_7^-` from Theorem 1 is terminal only in a
branch which excludes `K_7^-` outright; the height-floor contradiction
is asserted only in Corollary 2.1.

After this exchange, a **no-`K_7^-`** port-order mismatch has the
following precise residue; it cannot be described merely as “more
linkage is needed”.  For every choice of four mismatched ports and
disjoint cyclic sectors, at least one of these failures occurs:

1. at least two uncovered corner-row duties use different fixed rows, or
   at least three duties are uncovered;
2. two corners miss one common row, but their entire skeleton connection
   is anticomplete to that row and there is no off-skeleton connected
   packet adjacent to both corners and the row;
3. the contact spans needed around two selected ports overlap before
   four disjoint sectors can be formed; or
4. a trapped contact span lies behind an actual adhesion, and every
   proper-minor equality state produced on that side differs from every
   state produced by an operation in the opposite open shore.

Item 4 is the faithful dynamic negation of Lemma 3, not a palette
statement.  Items 1--3 are the remaining multi-packet/overlapping-span
exchange problem.  The theorem makes no claim that connectivity alone
eliminates them.

In a merely `K_7`-minor-free host, add one further nonterminal output to
this list: an arbitrary `K_7^-` model whose one-hole centre has not been
proved to have order `mu`.  Corollary 2.1 removes that output only in its
stated floor-preserving on-skeleton subfamily.

### Applicability boundary

The local theorems do not assert that an arbitrary output of the
seven-root trichotomy already comes with four mismatched **distinct**
ports, disjoint cyclic sectors, or the common packet of Theorem 2.  Those
features must be exhibited in the uncontracted trichotomy adhesion before
this note applies.  Once they are exhibited, however, no singleton-row,
point-contact, or palette-to-label assumption remains: all branch sets and
all promoted contacts above are literal.  Failure to exhibit them is
exactly residue 1--4, not a defect in the local branch-set construction.
