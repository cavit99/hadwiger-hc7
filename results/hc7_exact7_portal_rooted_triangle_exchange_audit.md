# Independent audit: portal-rooted triangle exchanges

## Verdict

**GREEN after two textual corrections.**  The branch-set exchanges in
Lemmas 3.1, 3.2, 4.1, and 4.2 are literal and valid.  Corollary 4.3 uses
the audited forbidden-label matching theorem with the correct parameters.
Lemma 5.1 has the correct strict inequalities, including after reversing
the `x`--`y` orientation, and connected bipartitions are equivalent to
fundamental cuts over the family of all spanning trees.

The two corrections do not change any theorem or conclusion.

## 1. Frozen input and Hall normal form

Because the rooted triangle is extended to a spanning partition of
`K union T`, every boundary neighbour of `K` belongs to at least one of
the three portal sets.  Thus

\[
N_S(K)\subseteq P_1\cup P_2\cup P_3,
\]

and the audited inequality `|N_S(K)|>=4` excludes a Hall defect on the
whole three-element family.  A failed SDR is therefore witnessed either
by a singleton with empty portal set or by a pair whose union has order
at most one.

The phrase **"exactly one"** in Section 2 must be replaced by **"at
least one (and possibly both)"**, or simply by **"one of"**.  The two
forms are not disjoint.  For example,

\[
P_1=\varnothing,\qquad P_2=\{a\},\qquad
P_3=\{b,c,d,e\}
\]

has union of order five, but both `P_1=emptyset` and
`|P_1 union P_2|<=1` hold.  The intended Hall equivalence and everything
later in the note remain correct.

## 2. Branch-bag peels

### Lemma 3.1

All branch-set conditions check literally.

* `t_j notin Z` leaves the root `t_j` in `B_j-Z`; the other roots do not
  move.
* The three new bags are disjoint and span the same vertex set.
* Their connectivity is an explicit hypothesis.
* Since `G[B_j]` is connected and both sides of the proper partition
  `Z, B_j-Z` are nonempty, an actual edge joins them.  This gives the
  new `B_i'B_j'` adjacency.
* The old `B_iB_k` edge survives, and hypothesis 3 supplies the possibly
  endangered `B_j'B_k'` adjacency.

Thus no adjacency is inferred through a contraction or through an
unavailable completion edge.

### Lemma 3.2

The three displayed bags are disjoint and spanning.  The roots `t_1`
and `t_2` remain in their original bags, while the first hypothesis keeps
`t_3` in `B_3^0`.  Connectivity is assumed; the old literal `B_1B_2`
edge survives; and hypothesis 3 supplies the other two edges.  A label
touching `Z_1` represents `B_1 union Z_1`, and similarly for `Z_2`, so
the stated three-label condition really is a portal-rank-three
certificate.

The explanatory sufficient conditions following Lemma 3.1 are not used
as converses and introduce no hidden assertion.

## 3. Other-lobe splits

### Lemma 4.1

For nonempty `X_i`, the literal edge from `X_i` to `t_i` connects
`B_i union X_i`; for empty `X_i`, that bag is simply `B_i`.  The old
rooted-triangle edges give all three pairwise adjacencies among these
bags.  The core `X_0` meets each such bag through either an `X_0X_i`
edge or, when `X_i` is empty, an `X_0t_i` edge.  Hence the four carriers
are genuinely connected, disjoint, and pairwise adjacent.

The unlabelled star partition construction is valid.  A minimal subtree
joining chosen neighbours `y_i of t_i` has a unique median after allowing
coincident terminals.  The median is the nonempty core, and the open
arms are disjoint connected sets, empty exactly when the corresponding
terminal equals the median.  Every component outside the subtree has an
edge to it because `J` is connected; assign the whole component to one
incident nonempty part.  This preserves connectivity and exhausts
`V(J)`.  Extra cross-edges cause no problem.

### Lemma 4.2 and Corollary 4.3

The `XY` edge gives the `Y`--`(B_i union X)` adjacency; the contacts of
`Y` with `t_j,t_k` give the other two adjacencies to `Y`; and the three
old rooted-triangle edges remain.  Thus (4.3) is a literal `K_4` model.

In Corollary 4.3, `F={p_j,p_k}` has order two.  Lemma 2.1 of the audited
two-lobe gate exchange gives a matching of order

\[
\min\{4-|F|,|J|\}=2
\]

when `|J|>=2`.  Hence the vertices `x,y` and labels `a,b` in (4.4) are
indeed pairwise distinct in the required senses, and both labels avoid
`p_j,p_k`.  Under (4.5), the representatives of the four carriers are
exactly `a,p_j,p_k,b`.

For completeness, the standard four-carrier lift is valid: enlarge the
four carriers by their four distinct boundary representatives, and
enlarge the three opposite `S`-full packets by the remaining three
boundary vertices.  Packet fullness gives packet--carrier and
packet--packet adjacencies, while the original four carriers already
form a clique model.

## 4. Lemma 5.1: projection and fundamental cuts

The definition of `pi_Q(z)` should be made literal: replace "the unique
vertex where the `z`--path projection ... first meets this path" by
**"the index of the unique closest vertex of the `x`--`y` path to `z`
in the tree `Q`"**.  Equivalently, it is the unique vertex of the
`x`--`y` path lying on both the `z`--`x` and `z`--`y` paths.  This removes
a grammatical ambiguity; uniqueness is standard in a tree.

For the path edge `v_{r-1}v_r`, with `1<=r<=h`, a vertex `z` lies on
the `x`-side precisely when `pi_Q(z)<r`.  Therefore the cut has the
required forward orientation precisely when

\[
\ell_Q(A_i)<r\le r_Q(A_j),r_Q(A_k).
\]

Such an integer exists exactly when

\[
\ell_Q(A_i)<\min\{r_Q(A_j),r_Q(A_k)\},
\]

so (5.2) and its strict inequality are correct.

Under path reversal, `pi'_Q(z)=h-pi_Q(z)`.  Consequently

\[
\ell'_Q(A_i)=h-r_Q(A_i),\qquad
r'_Q(A_l)=h-\ell_Q(A_l).
\]

Failure of (5.2) in the reverse orientation is exactly

\[
r_Q(A_i)\le\max\{\ell_Q(A_j),\ell_Q(A_k)\},
\]

which is the second inequality in (5.3).  Thus violation of either
inequality produces the corresponding oriented split.

Finally, the spanning-tree equivalence is exact in both directions.
Deleting an `x`--`y` path edge of any spanning tree gives two connected
vertex sets and hence a legal graph bipartition.  Conversely, for a
legal connected bipartition `J=X dotunion Y`, choose spanning trees of
`G[X]` and `G[Y]` and one literal `XY` edge.  Their union is a spanning
tree of `J`, and that chosen edge has fundamental cut exactly `(X,Y)`.
Therefore quantification over every spanning tree in the negative
certificate loses no graph bipartition.

## 5. Scope of the conclusion

The final alternative is correctly local.  It does not claim that
three-connectivity alone eliminates the block-terminal web, nor that the
crossed inequalities already yield an apex pair or a common equality
state.  The two-vertex example at the end is a valid obstruction to such
an unconditional strengthening.

With the two wording corrections above, the note is safe to promote as
an audited constructive exchange and an exact negative certificate.
