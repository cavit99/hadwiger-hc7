# A nontrivial reserved rural connector gives a labelled near-`K_7`

**Status:** proved and independently audited.

## Setup

Let

\[
  V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
  \qquad |S|=7,
\]

with no `A-R` edge.  Suppose `R` contains two vertex-disjoint, adjacent,
connected `S`-full packets `P_1,P_2`.

Let `Q={a_0,a_1,b_0,b_1} subseteq S`.  Suppose
`B_{a_0},B_{a_1},B_{b_0},B_{b_1}` are four pairwise disjoint, connected,
pairwise adjacent subgraphs of `G[A union S]`, with each `B_x` containing
its named literal root `x`.  Let `P` be an `a_i-b_i` path in `G[S]` whose
interior is nonempty and disjoint from all four rooted bags.

This is exactly the package produced in the rural branch of the audited
closed-shore theorem whenever the bad path reserved after repairing the
rooted diamond is nontrivial.

## Theorem

Put

\[
                         C=P-\{a_i,b_i\}.
\]

Then the seven literal bags

\[
 B_{a_0},B_{a_1},B_{b_0},B_{b_1},C,P_1,P_2
\]

form a labelled `K_7^vee` model: the only two bag adjacencies not forced
are those from `C` to the two rooted bags whose roots are not
`a_i,b_i`.

If `C` is adjacent to one of those two bags, the model is a labelled
`K_7^-`; if it is adjacent to both, it is a literal `K_7` model.

### Proof

The set `C` is nonempty and connected because it is the interior of the
path `P`.  It is disjoint from the four rooted bags by hypothesis, and it
is adjacent to `B_{a_i}` and `B_{b_i}` through the first and last edges of
`P`.  The four rooted bags already form a clique model.

Every vertex of `C` is a literal member of `S`.  Since each `P_j` is
`S`-full, both packets are adjacent to `C` and to every rooted bag (use
the literal root contained in that bag).  The packets are disjoint and
adjacent by hypothesis.  Consequently every pair among the seven bags is
adjacent except possibly the two pairs consisting of `C` and one of the
two nonendpoint rooted bags.  Those two possible missing edges share the
bag `C`, which is precisely the labelled `K_7^vee` deficiency pattern.

The two upgrades are immediate when one or both optional contacts are
present.  \(\square\)

## Exact rural residue

Apply the theorem after the audited rural normalization.  A rural branch
can avoid this labelled near-model handoff only if the path left reserved
after repairing the rooted `K_4^-` has empty interior.  The two parity-bad
paths cannot both be literal edges: they would themselves be two disjoint
paths joining alternating vertices of the displayed disk boundary.  Also,
a literal-edge pair cannot be the missing pair of the rooted diamond,
because the two bags contain the endpoints of that literal edge and are
therefore adjacent.  Hence the sole direct-reserve augmentation case is:

1. exactly one parity-bad path is nontrivial, the other is a literal edge,
   and the rooted diamond is missing the nontrivial path's rooted pair, so
   that path is consumed in the repair.

No static fifth-bag conclusion is asserted in these direct-reserve cases.
The companion quotient probe shows that arbitrary concentration of all
three spare portal labels in one rooted bag defeats such a conclusion.
The surviving proof must use the full minor-critical transition or expose
an actual exact-seven adhesion/normalised near-model rotation.
