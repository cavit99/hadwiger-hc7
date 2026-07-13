# Barrier: Moser multi-frame signs are compatible in one planar wheel

**Status:** explicit counterarchitecture to any argument which tries to
force a favourable Moser crossing from the four frame signs alone.

This is not a counterexample to `HC_7`: the displayed host is not
seven-connected or contraction-critical.  It proves the narrower negative
statement that the stipulated within-frame path disjointness, literal
fullness, portal rank, and three-connectivity do not make the hard frame
choices combinatorially inconsistent.

## 1. The portal society

Use the standard Moser boundary

\[
 S=\{0,1,2,3,4,5,6\},\qquad
 E(H)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Let `D` be the wheel whose rim, in cyclic order, is

\[
 p_0,p_1,p_2,p_5,p_6,p_3,p_4,p_0,                    \tag{1.1}
\]

and whose hub `z` is adjacent to every rim vertex.  For every `s in S`,
give the literal boundary vertex `s` the single portal edge `s p_s`.

The open society `D` is three-connected.  It is `S`-full, and its portal
incidence graph contains the literal perfect matching
`{s p_s:s in S}`.  Thus its portal matching rank is seven; no collision of
first hits is involved.

The four Hamiltonian five-cycle frames of the Moser boundary can be written

\[
\begin{array}{c|c|c|c}
\text{repeated pair}&\text{frame}&L&R\\ \hline
13&0,2,6,5,4&2&4\\
14&0,2,6,5,3&2&3\\
23&0,1,6,5,4&1&4\\
24&0,1,6,5,3&1&3.
\end{array}                                             \tag{1.2}
\]

Thus every frame has the form `0,L,6,5,R`, with
`L in {1,2}` and `R in {3,4}`.

## 2. Every hard crossing type exists

Deleting one frame vertex leaves four vertices in cyclic order; the frame
crossing joins opposite members of that order.  The three hard types are

\[
\begin{array}{c|c}
\text{omitted frame vertex}&\text{crossing pairs}\\ \hline
0&(L,5),(6,R)\\
L&(6,R),(5,0)\\
R&(0,6),(L,5).
\end{array}                                             \tag{2.1}
\]

All three are realized in the same wheel, for every one of the four
choices of `(L,R)`:

* a `p_L-p_5` path is the rim subpath inside the block
  `p_1,p_2,p_5`;
* a `p_6-p_R` path is the rim subpath inside
  `p_6,p_3,p_4`;
* a `p_5-p_0` path uses the opposite rim arc
  `p_5,p_2,p_1,p_0`; and
* a `p_0-p_6` path uses the opposite rim arc
  `p_0,p_4,p_3,p_6`.

For each row of (2.1), the two displayed rim subpaths are vertex-disjoint.
Adding the two appropriate portal edges turns them into literal paths
between the named boundary labels, with all internal vertices in `D`.

These witnesses coexist in one graph.  They are not asserted to be
mutually disjoint between different applications, because the multi-frame
reductions supply no such cross-application disjointness.

## 3. Both favourable crossing types are absent

The two favourable types for the frame `(0,L,6,5,R)` are

\[
                         (0,5),(L,R),qquad
                         (0,6),(L,R).                    \tag{3.1}
\]

On the rim (1.1), the endpoints of the first pair of demands occur in the
cyclic order

\[
                         p_0,p_L,p_5,p_R,
\]

and those of the second occur in the cyclic order

\[
                         p_0,p_L,p_6,p_R.
\]

In each case the prescribed pairs alternate on the boundary of the planar
disk containing the wheel.  By the Jordan curve theorem, the wheel cannot
contain the two corresponding vertex-disjoint portal paths.  Since every
literal label has the unique portal `p_s`, this excludes the literal
linkages in (3.1), not merely the four particular rim paths.

Consequently the same three-connected `S`-full society realizes every hard
omit-`0`, omit-`L`, and omit-`R` crossing while excluding every favourable
crossing in all four Moser frames.

## 4. Exact implication

Any proposed finite implication of the form

\[
 \text{one hard crossing chosen in each Moser frame}
 \Longrightarrow
 \text{a favourable crossing or a sign inconsistency}
\]

is false if it uses only the separately supplied path systems, their
within-system disjointness, three-connectivity, fullness, and distinct
portals.  The wheel supports any mixture of the three hard choices, because
all twelve relevant hard linkages exist in it.

The construction does **not** satisfy the minimum-degree and global
seven-connectivity constraints of a hypothetical `HC_7` counterexample,
and it has no proper-minor equality-state requirement.  Those are therefore
the only legitimate remaining sources of a contradiction.  In particular,
a valid multi-frame proof must use a global degree/separator argument,
minor-critical state transfer, or a literal branch-set construction; frame
signs alone cannot close the residue.

The dependency-free check
`../barriers/hc7_exact7_moser_multiframe_sign_barrier_verify.py` verifies the
twelve hard path pairs and the eight alternating favourable pairs.

