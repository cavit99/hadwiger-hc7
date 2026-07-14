# Independent audit: connected-rich width-two frontier

Audited file before promotion:
`active/hc7_connected_rich_width2_frontier_draft.md`.

Promoted file:
`results/hc7_exact7_connected_rich_width2_frontier.md`.

Audited SHA-256:
`c75de683a80888ebfe14857444f20864ff46e64367a39a538312a847d2523bec`.

Promoted SHA-256 (status/path change only):
`943808c3b7aa2e53d299d500b2ea2ff0f8fe03bf09d1d70e573a656bc4b33225`.

**Verdict for Sections 1--6:** **GREEN.**  Promotion changed only the
status line and path; the audited mathematics is unchanged.

The adjacent-packet cover, exact three-packet quotient criterion,
`K_4^vee` obstruction, paired-boundary classification, portal count, and
exact-state gluing are all correct.  The thin-cutvertex theorem correctly
reduces every surviving articulation to the stated same-duty two-lobe lock
and produces two literal descending seven-adhesions.  Lemma 6.2 and Theorem
6.3 then turn that last lock into a literal `K_7^vee` model, so the
cutvertex case has no remaining state-pullback obligation.  The quotient
criterion was also checked independently on every unlabeled graph of order
seven.

Section 7 is explicitly a proposed theorem.  It is not established by the
audited material and is not included in this GREEN verdict.

## 1. Adjacent connected cover

After contracting the two disjoint connected roots `P_0,Q_0`, a spanning
tree of the connected quotient has a unique root-to-root path.  Deleting
any edge of that path separates the tree into two connected vertex sets,
one containing each root.  Expanding the two contractions gives a genuine
partition of `V(R)` into connected sets containing the prescribed packets.
The deleted tree edge is literal and joins the two expanded sets.  Enlarging
a full packet preserves fullness.  Lemma 1.1 is therefore valid.

## 2. Exact three-packet quotient criterion

### Forward constructions

If `H` has a `K_4` model, its four bags and the singleton packet bags
`l,p,q` have only the two missing pairs `lp,lq`.  These share `l`.

If `H-x` has a `K_4^vee` model, `{l,x}` is connected because `l` is
complete to `S`.  Together with `{p},{q}` it forms a packet triangle:
`xp,xq,pq` are literal.  All three packet bags meet every boundary bag,
and the only possible missing pairs are the two incident defects inherited
from the boundary model.  Both forward implications are literal.

### Converse for `r<=2`

At least five model bags then avoid all of `l,p,q` and hence lie wholly in
`S`.  Choose four of them and choose a literal vertex `x` from a fifth.
The selected four bags are disjoint from `x`, remain connected in `H-x`,
and inherit at most the two mutually incident nonadjacencies of the
seven-bag model.  Thus they contain a `K_4^vee` model in `H-x`.

### Converse for `r=3`

There are exactly four boundary-only bags.  If any packet bag also contains
a boundary vertex `x`, the four boundary-only bags avoid `x` and give the
same `H-x` conclusion.  Otherwise three nonempty packet-containing bags
use exactly the three packet vertices and no boundary vertices, so they are
precisely `{l},{p},{q}`.  Their actual nonedges `lp,lq` already consume the
entire allowed two-edge missing star.  The other four bags must therefore
be pairwise adjacent, giving a `K_4` model in `H`.

These cases also cover `r=0,1`; there is no hidden assumption that a packet
vertex must occur in the minor model.

### Exhaustive independent check

The equivalence was tested on all `1,044` unlabeled simple graphs of order
seven from the NetworkX graph atlas.  For each `H`, an independent
forest/deletion enumerator checked both sides.

For `J(H)` on ten vertices, every seven-bag minor model was enumerated by
choosing an acyclic forest of `k=0,1,2,3` host edges and deleting `3-k`
vertices outside that forest.  This is exhaustive because spanning trees
inside seven connected branch sets use exactly

\[
               |V(\text{used})|-7=k
\]

forest edges.  The resulting seven quotient bags were accepted precisely
when they had at most two nonadjacent pairs and, when there were two, those
pairs shared an endpoint.  `K_4` and `K_4^vee` minors on the right-hand
side were checked by the analogous four-bag forest enumeration in `H` and
each `H-x`.  The comparison returned

```text
checked 1044 mismatches []
```

This computation is supplementary; the preceding converse proof is
already complete.

## 3. The elementary `K_4^vee` obstruction

A minor of a tree or cycle cannot have the triangle-with-pendant form.
Conversely, in a connected graph which is neither, choose a cycle `C`.
If a vertex lies outside `C`, a shortest attachment path and a contraction
of `C` to a triangle give a pendant triangle minor after deleting unwanted
edges.  If `C` spans, a chord and one cyclic arc give the triangle, while
the other arc can be broken at its far end and contracted to the pendant
edge.  Both arcs of a genuine chord have the necessary internal vertex.
Thus Lemma 3.1 is correct componentwise.

## 4. Cycle and disconnected-frontier analysis

For Lemma 4.1, if a cycle has at least two outside vertices, delete one
while retaining an outside vertex attached to the cycle.  One component of
the deletion then contains both a cycle and an extra vertex and is neither
a tree nor a cycle, contradicting Lemma 3.1.  Hence every cycle has at most
one outside vertex and length at least six.

If a second cycle exists, the union supplies a chord or a `C`-ear `P`.
There can be at most one vertex outside `C`, so `|P|<=2`.  If the two
cyclic arcs have lengths `r,s`, both new cycles have length at least six,
whereas

\[
 r+s+2|P|\le7+4=11<12.
\]

Thus the cycle is unique.  A vertex-disjoint second cycle cannot be an
exception because it would require more than the one available outside
vertex.

Theorem 2.1 says that a frontier boundary `H` has no `K_4` minor and every
`H-x` is `K_4^vee`-minor-free.  If `H` is connected, Lemma 4.1 leaves a
tree, `C_7`, or `C_6` with one pendant vertex.  The `C_7` case is excluded
because the three named `c-B_i` contacts give `d_H(c)>=3`.

If `H` is disconnected, deleting a vertex in another component proves
that every component is `K_4^vee`-minor-free, hence a tree or cycle.  The
component containing `c` contains at least one literal from every `B_i`
and has `d_H(c)>=3`; it is therefore a tree on at least four vertices.
Only three vertices remain, so the only possible odd-cycle component is a
triangle.

The three `c-B_i` edges and the three inter-`B_i` edges are six distinct
literal edges.  A disjoint union of the permitted components has at most
six edges.  Equality forces a four-vertex `c`-tree and a three-cycle.  The
three distinct neighbours of `c` make the tree exactly `K_{1,3}`.  This
validates the disconnected equality case and exhausts the structural list.

The edge bounds, treewidth at most two, and clique odd-cycle transversal of
order at most one follow immediately: the two connected forms are
bipartite, while deleting one triangle vertex handles the disconnected
form.

## 5. Counterexample consequences

Because `L,P,Q` partition `G-S`, for every `s in S`

\[
 d_{G-S}(s)=|N_L(s)|+|N_P(s)|+|N_Q(s)|.
\]

Minimum degree seven and `|E(H)|<=7` give

\[
 \sum_{s\in S}d_{G-S}(s)
 =\sum_{s\in S}(d_G(s)-d_H(s))
 \ge49-2|E(H)|\ge35.
\]

Fullness supplies the baseline twenty-one incidences, so the surplus is
at least fourteen.  Pigeonhole gives at least twelve contacts in one of
the three packets, and positive surplus gives two distinct neighbours of
some boundary literal in one packet.  Corollary 5.1's accounting is exact.

For Lemma 5.2, `A,B` are independent and partition `S-U`.  The two thin
contraction sets `X union A`, `Y union B` are disjoint and connected, meet
through `X-Y`, and—when `U={u}`—both see `u` by hypothesis.  Their images
and the possible singleton `u` therefore form a clique.  Restriction to
the untouched rich side and expansion only of the independent literal
sets `A,B` gives exactly `A|B|U`.

On the other side, `P union A` and `Q union B` are disjoint and connected;
the `P-Q` edge joins their images and fullness joins both to the possible
singleton `u`.  The rich-side contraction is proper and gives the same
exact state on the untouched thin side.  Clique representatives make the
block colours distinct, and a palette permutation aligns the two closed-
side colourings before gluing.  No colour is identified with a packet or
branch label without a literal contraction.

Finally, if the thin shore were one vertex, fullness makes its literal
neighbourhood exactly `S` and its degree seven.  Dirac's neighbourhood
inequality gives `alpha(H)<=2`, while every graph in Theorem 4.2 has an
independent set of order at least three.  The claimed nonsingleton
consequence is valid.

## 6. Thin-cutvertex descent

In the disconnected frontier, choosing `U={u}` from the triangle leaves
the other two triangle vertices adjacent and hence in opposite sides of a
bipartition of `H-U`.  Thus each of `A,B` contains a literal neighbour of
`u`.  Consequently a near-full carrier missing only `u` really does fund
both duties: the retained `u`-adjacency is supplied by a boundary edge from
the corresponding side.  The other funding assertions follow directly
from an empty or singleton contact defect.

For every component `D_i` of `L-z`, connectedness of `L` gives a literal
`D_i-z` edge and the original separation gives

\[
                         N_G(D_i)\subseteq S\cup\{z\}.
\]

The nonempty rich shore is separated from `D_i` by this set.  Seven-
connectivity and the mandatory neighbour `z` therefore force
`|N_S(D_i)|>=6`; every lobe defect is empty or a singleton.

When there are at least three lobes, the chosen carrier containing `z` is
full whenever it contains two lobes with distinct singleton defects (with
an empty defect also making it full).  Such a choice is possible unless all
defects are the same singleton or all are empty.  The all-empty case gives
two full carriers.  In the common-singleton case, fullness of the entire
thin shore forces the missing boundary literal to see `z`, again making
the carrier containing `z` full.  The remaining lobe funds at least one
duty in every case, so Lemma 5.2 closes.  This validates the `k>=3`
argument, including its all-empty edge case.

For two lobes, one must use genuinely adjacent carriers rather than the raw
components.  The proof does so by assigning `z` to one side and using
`D_1 union {z},D_2` (or the symmetric choice).  Adding `z` cannot destroy a
funded duty.  Hence an empty defect, a defect at `u`, defects in opposite
bipartition sides, a common defect repaired by `z`, or either distinct
defect repaired by `z` all give the split in Lemma 5.2.  The only survivor
has two distinct singleton defects in the same duty side, neither seen by
`z`, exactly as (6.1) states.

As a supplementary finite check, all `7,744` two-lobe empty/singleton-
defect and `z`-contact patterns compatible with fullness were enumerated
(using representative three-element sides `A,B` and one possible `u`).
Existence of an adjacent two-carrier duty assignment failed exactly in the
same-side, distinct-defect, neither-repaired pattern; there were no
mismatches.

Finally, the original actual separation has no thin-rich edge.  Since
`D_i` is a component of `L-z`, it has no neighbour in another lobe either.
Together with its exact boundary defect and its edge to `z`, this proves

\[
              N_G(D_i)=(S-\{d_i\})\cup\{z\}=S_i.
\]

The set has order seven, and deleting it separates the nonempty connected
`D_i` from the nonempty rich shore.  It is therefore a literal actual
seven-adhesion.  Because the other lobe and `z` lie outside `D_i`, its thin
shore is strictly smaller than `L`.  The geometric descent conclusion is
fully justified.

For Lemma 6.2 in the connected frontier, orient the bipartition so that
`c in A`.  Its neighbours in the three disjoint paired blocks are three
distinct members of `B`, so `|B|>=3`.  If `|A|<=2`, at most one of the six
paired-block literals can lie in `A`; hence at least two paired blocks lie
wholly in `B`.  The required edge between those two blocks would violate
bipartiteness.  Therefore `|A|>=3` as well.  Deleting two same-side
literals leaves a vertex in that side, and connectedness gives it an edge
to the untouched opposite side.  In the disconnected frontier, the two
triangle vertices outside `U={u}` occupy opposite sides of `H-u`; a
same-side pair deletes at most one, leaving its literal edge to `u`.
Thus the edge `xy` asserted outside both defects always exists.

The seven bags in Theorem 6.3 are literal and pairwise disjoint.  Their
connectivity and every required adjacency can be checked as follows:

* `D_1 union {z,d_2}` is connected through a `D_1-z` edge and a
  `D_1-d_2` edge, since `d_2` is not its defect `d_1`;
* `D_2 union {d_1}` is connected because `d_1` is not its defect `d_2`;
* the two lobe bags are adjacent through a literal `z-D_2` edge;
* each of `P,Q` meets the first lobe bag at `d_2`, the second at `d_1`,
  and the other rich packet through the audited `P-Q` edge, so the four
  carrier bags form a clique;
* the literals `x,y,t` avoid both defects, hence each lobe contacts all
  three, while fullness gives the corresponding contacts from `P,Q`;
* `xy` is literal, leaving at most `xt,yt` absent among the three singleton
  bags.

The only possible missing bag pairs are therefore the two incident pairs
at `{t}`.  Extra singleton edges, if present, may be deleted.  This is a
genuine `K_7^vee` minor and validates Corollary 6.4: every thin cutvertex
either reflects the low state or hands a labelled near model to `S1`.

## 7. Audit boundary

Section 7 asks for a width-two portal pullback which either realizes the
split of Lemma 5.2, descends through a state-preserving actual adhesion, or
gives the spanning near model.  Sections 1--6 now close every cutvertex
geometry.  They do not prove the cutvertex-free block-terminal case.  That
trichotomy remains the active theorem target and is deliberately outside
this audit verdict.
