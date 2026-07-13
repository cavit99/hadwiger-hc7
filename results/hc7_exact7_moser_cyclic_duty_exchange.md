# Moser cyclic attained-duty exchange

**Status:** proved and independently audited.  This is an infinite-family
closure inside the normalized Moser `(1,2)` state.  It leaves one literal
orientation of the alternating width-two web; it does not claim to close
the general attained-duty exchange.

## 1. Exact cell

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
 \qquad (\nu_L,\nu_R)=(1,2)
\]

be an actual separation in the frozen hypothetical `HC_7` counterexample.
Let `Q subseteq L` be an `S`-full thin packet and let `P,P' subseteq R` be
disjoint `S`-full rich packets.  Use the standard Moser boundary

\[
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.           \tag{1.1}
\]

Consider the legal exact state

\[
 \Pi=\{A,B,D,\{6\}\},\qquad
 A=\{2,3\},\quad B=\{1,4\},\quad D=\{0,5\}.           \tag{1.2}
\]

For the maximum singleton clique `C={6}`, its three attained duties are
exactly `A,B,D`: vertex `6` has a boundary neighbour in each block.

Assume `P` contains a cycle `Z` through six distinct duty-specific portal
witnesses, one for each literal in `S-{6}`.  No uniqueness of those portals
and no inducedness of `Z` are assumed.  Record the six literal labels in
their cyclic order on `Z`.

## 2. The cycle theorem

### Theorem 2.1 (cyclic duty exchange or one literal order)

Under the setup above, at least one of the following holds.

1. The exact state `Pi` reflects across the rich shore and `G` is
   six-colourable.
2. `G` contains a literal `K_7` minor.
3. Up to reversing and rotating `Z` and applying the Moser automorphism

   \[
       \varphi=(1\ 2)(3\ 4),                            \tag{2.1}
   \]

   the cyclic literal portal order is

   \[
                         2,4,5,3,1,0.                    \tag{2.2}
   \]

Thus a cyclic packet closes unless it has the single exceptional literal
orientation (2.2).

#### Proof

First forget the literal names and retain only the duty word.  If the two
portal pairs of some two duties do not alternate on `Z`, two disjoint cycle
arcs join the respective pairs.  Extend the arcs disjointly through an
intervening portal-free interval until one cycle edge joins them.  They are
adjacent connected carriers discharging those two exact duties.  The other
full packet `P'` discharges the third duty.  The audited attained-duty packet
split theorem reflects `Pi`, giving outcome 1.

We may therefore assume every two duty pairs alternate.  The elementary
cyclic-word argument in the audited gate-bypass certificate says that, up
to duty names and dihedral symmetry, the duty word is

\[
                         A,B,D,A,B,D.                     \tag{2.3}
\]

Fix (2.3).  Choosing which literal of each two-set occurs first gives eight
orientations.  Under dihedral symmetry and the literal automorphism (2.1),
they form the following three orbits:

\[
\begin{array}{c|c|c}
\text{flip vectors}&\text{representative literal order}&\text{outcome}\\
\hline
000,001,110,111&(2,1,0,3,4,5)&K_7\\
010,101&(2,4,0,3,1,5)&K_7\\
011,100&(2,4,5,3,1,0)&\text{exception (2.2)}.
\end{array}                                             \tag{2.4}
\]

Here a flip vector records, for `A,B,D` respectively, whether the second
rather than the first displayed member of the pair occurs in the first
half of (2.3).  The orbit calculation in (2.4) is checked directly:
`varphi` preserves (1.1), fixes `0,5,6`, interchanges the blocks `A,B`, and
interchanges `1,2` and `3,4`; cycle rotation and reversal supply the listed
dihedral identifications.

It remains to give literal branch sets for the first two representatives.
Write `x_0,...,x_5` for the portal witnesses in their displayed cyclic
order.  Partition the cycle into the two indicated arcs, cutting each of
the two complementary portal-free intervals at one edge so that the arcs
are vertex-disjoint, connected, and adjacent.

For order `(2,1,0,3,4,5)`, let `X` be the arc through
`x_1,x_2,x_3,x_4` and `Y` the complementary arc through `x_5,x_0`.
The seven branch sets are

\[
 \{0\},\quad \{3\},\quad \{4\},\quad
 X\cup\{1\},\quad Y\cup\{2,5\},\quad
 P',\quad Q\cup\{6\}.                                  \tag{2.5}
\]

For order `(2,4,0,3,1,5)`, let `X` be the arc through
`x_0,x_1,x_2,x_3` and `Y` the complementary arc through `x_4,x_5`.
Use

\[
 \{0\},\quad \{3\},\quad \{4\},\quad
 X\cup\{2\},\quad Y\cup\{1,5\},\quad
 P',\quad Q\cup\{6\}.                                  \tag{2.6}
\]

All seven sets in either display are nonempty, connected, and disjoint.
The singletons `0,3,4` form a literal triangle in (1.1).  In (2.5), `X`
contains portals for `0,3,4`, while the boundary set `{2,5}` is adjacent
to each of `0,3,4`; in (2.6), `X` again contains portals for `0,3,4`, while
`{1,5}` is adjacent to each of them.  The two arc bags are adjacent at a
chosen cycle cut edge.  Finally `P'` and `Q` contact every literal boundary
vertex: this supplies all their adjacencies to the five preceding bags,
and the literal vertex `6` in the last bag supplies the `P'`--`Q` adjacency.
Thus (2.5) and (2.6) are literal `K_7` models.  This proves outcome 2 in
the first two rows of (2.4), leaving only (2.2).  \(\square\)

## 3. Why this is a multi-attachment bridge result

The theorem does not assume that `P` is a cycle.  It needs only a cycle
through the six selected duty portals, so arbitrary subdivisions, chords,
attached bridge systems, and unused packet vertices are harmless.  A
multi-attachment bridge which closes with a portal-tree path to form such a
cycle therefore falls under Theorem 2.1.

The exact surviving obstruction is not merely the unlabelled
`A B D A B D` web from the gate-bypass barrier.  Six of its eight literal
orientations (two of its three symmetry orbits) close by the two explicit
branch-set templates; only the orbit represented by (2.2) remains.  Any
next web-to-adhesion argument may consequently assume that exact literal
order.

## 4. Reproducibility aid

`results/hc7_exact7_moser_alternating_cycle_probe.py` independently
enumerates the eight orientations and searches for the rooted `K_5` core
of (2.5)--(2.6).  It is not needed for the proof: the orbit table and both
branch-set templates above are directly checkable.
