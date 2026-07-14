# Audit: packet classification after a prescribed-portal Hall descent

**Verdict:** GREEN at frozen source SHA-256
`6adbb2ede7cdd0f54b6594eb1fe753d7ce08ffb2573a4453364718986e9b9279`.

The independently audited mathematical source had SHA-256
`8c44a4968ee65cc9cb46cdeb5900c3f4c6d3b342e35ba08c6332df51f648bb66`;
promotion changed only its status line from draft to proved.

The local incidence classification, the alternating-cycle labelled
`K_7^vee` handoff, and the packet-vector corollary are correct under all the
hypotheses stated in Section 1.  This audit checked the current source after
the setup was generalized to allow a disconnected old open shore `R`.
Neither the theorem nor its proof needs `R` to be connected.

## 1. Boundary map and hypotheses

The three sets

\[
 C=L-X,\qquad \Omega=(S-U)\cup X,\qquad O=R\cup U
\]

are pairwise disjoint and partition `V(G)`.  They give a literal descended
separation:

* the old separation has no `L-R` edge, so there is no `C-R` or `X-R`
  edge;
* `X=N_L(U)` implies there is no `C-U` edge; and
* `|Omega|=7-|U|+|X|=7`.

Thus there is no `C-O` edge.  Both open shores are nonempty: this is assumed
for `C`, while `O` contains the old nonempty shore `R` and the nonempty set
`U`.  The explicit hypothesis that `C` is connected and `Omega`-full is
exactly what is needed below.

The Hall data also match the audited prescribed-portal theorem.  If `U` is
an inclusion-minimal deficient set in the forced matching from
`A-{s}` into `L-{z}`, then

\[
 Y=N_{L-\{z\}}(U),\qquad |Y|=|U|-1,
\]

and every nonempty proper `W subsetneq U` obeys
`|N_Y(W)|>=|W|`.  In the non-tiny exact-seven outcome,
seven-connectivity forces `X=N_L(U)=Y union {z}` and `|X|=|U|<=3`.
The retained label satisfies `s notin U`, and the originally prescribed
edge `sz` remains literal.  In the live four-connected branch,
`G[L-X]` is connected, so all Section 1 hypotheses follow directly.  The
draft may also be used outside that branch whenever its separately stated
connectedness hypothesis on `C=L-X` holds.

The connected-rich branch supplies the fixed adjacent packets `P,Q` by the
audited adjacent-connected-cover lemma.  More generally, the present note
only assumes those packets and therefore remains valid even if other
components of `R` exist.

## 2. Lemma 2.1: exact packet traces

Let `K subseteq O` be `Omega`-full.  For every `x in X`, an edge from `x`
to `K` cannot end in `R`, because the old separation has no `L-R` edge.
It must end in `K cap U`; hence `K cap U` is `X`-dominating.  Two disjoint
packets therefore have disjoint dominating traces.  This direction does not
need adjacency of the packets and is strong enough to control the packet
number.

Conversely, if `T_P,T_Q subseteq U` are disjoint and `X`-dominating, then

\[
 P'=P\cup T_P,\qquad Q'=Q\cup T_Q
\]

are disjoint and connected.  Every old boundary literal, hence every member
of either trace, has a neighbour in each old full packet.  Old fullness
supplies all contacts to `S-U`, trace domination supplies all contacts to
`X`, and the assumed literal `P-Q` edge makes `P'` and `Q'` adjacent.
This proves both directions of the lemma without a palette or virtual-edge
lift.

Even when all of `O` is disconnected, the particular set `P union U` is
connected: every `u in U` has a neighbour in `P`.  It is `Omega`-full
because `P` contacts `S-U` and `U` dominates `X=N_L(U)`.  Thus the absence
of two disjoint dominating traces makes the packet number of `O` exactly
one, not zero.  The former audit's statement that the whole of `O` is
connected was stale; the current argument correctly needs only this one
connected full subset.

## 3. Theorem 3.1: exhaustive incidence classification

Write `k=|U|=|X|`.

* If `k=1`, `Y` is empty and `z in N_L(U)` has the unique member of `U`
  as its unique `U`-neighbour.
* If `k=2`, minimality makes the sole `y in Y` adjacent to both members of
  `U`.  If `z` also has both neighbours, the two singleton traces dominate
  `X`; otherwise its sole neighbour is compulsory.
* If `k=3`, minimality gives `d_U(y_1),d_U(y_2)>=2` and
  `d_Y(u)>=1` for every `u in U`.  Two disjoint dominating subsets of a
  three-set exist exactly when one singleton `{u_0}` dominates `X` and its
  complement does too.  This is equivalent to
  `u_0 in N(y_1) cap N(y_2) cap N(z)` together with `d_U(z)>=2`.
  If `d_U(z)=1`, its neighbour is compulsory.  If `d_U(z)=3`, the two
  size-at-least-two `Y`-neighbourhoods intersect and give such a `u_0`.
  Finally, when `d_U(z)=2` and no split exists, the two
  `Y`-neighbourhoods intersect exactly in the unique member missed by
  `z`; both have degree two and miss different members.  The three missed
  incidences are therefore a perfect matching, so `G[U,X]=C_6`.

The outcomes are mutually exclusive.  In the compulsory case every
dominating trace contains `u_*`.  In the `C_6` case no singleton dominates
all three gates, so every full packet uses at least two vertices of the
three-set `U`; two such traces necessarily intersect.  Together with the
full packet `P union U`, this proves packet number exactly one in both
residues.

As an independent exhaustive check, all bipartite incidences satisfying
the displayed Hall-minimality conditions were enumerated for
`k=1,2,3`.  The mutually exclusive outcome counts were

\[
\begin{array}{c|ccc}
k&\text{compulsory}&\text{two traces}&C_6\\ \hline
1&1&0&0\\
2&2&1&0\\
3&39&46&6
\end{array}
\]

with no unclassified or multiply classified incidence.

## 4. Lemma 4.1: literal labelled `K_7^vee`

In the `C_6` residue, a perfect matching of the literal six-cycle gives
three disjoint two-vertex connected bags `A_1,A_2,A_3`.  The three
unmatched cycle edges make these bags pairwise adjacent.  Exactly one bag,
`A_z`, contains `z`.

Since `|U|=3`, the set `S-U` has four vertices, so a literal
`r in (S-U)-{s}` exists.  The six bags

\[
 C\cup\{r\},\quad P,\quad Q,\quad A_1,A_2,A_3
\]

are disjoint and form a literal `K_6` model:

* `C union {r}` is connected because `C` has a neighbour at `r`;
* `P,Q` are adjacent, and each contacts the first bag through `r`;
* every `A_i` contains one old boundary literal in `U`, which contacts
  both `P,Q`, and one new gate in `X`, which contacts `C`; and
* the unmatched cycle edges supply all three `A_i-A_j` adjacencies.

The seventh singleton bag `{s}` contacts `P,Q`, and `C union {r}` by
fullness, and contacts `A_z` through the prescribed literal edge `sz`.
It therefore has at least four spokes to the `K_6` rim.  Its at most two
missing rim edges are incident with the same singleton centre, exactly the
allowed deficiency of the repository's labelled `K_7^vee`.  All branch
sets are disjoint, and no unproved boundary edge or completion edge is
used.

## 5. Corollary 4.2 and proof-spine scope

In the two-trace outcome, `C` supplies at least one new full packet and
`O` supplies at least two.  Applied in the strongly
seven-contraction-critical, seven-connected, `K_7`-minor-free kernel, the
audited exact-seven packet theorem gives packet vector `(1,2)` or `(1,3)`,
with `C` the packet-one shore.  The audited adaptive reflection theorem
eliminates `(1,3)`.  Because `X` is nonempty, `C=L-X` has strictly fewer
vertices than `L`; hence every surviving pull-through is a strict `(1,2)`
shore-order descent.

This corollary is green with the normal document-wide convention that
"a prescribed-portal descent" retains all of Section 1, especially the
fixed adjacent packets and connected full set `C=L-X`.  It is not a claim
about a general Hall descent for which `L-X` has several components.  In
the actual proof spine these assumptions hold in the connected-rich,
four-connected branch; elsewhere they must be verified before invocation.

The note correctly does not claim equality-state preservation in the
strict descent.  In the compulsory residue it stops at the exact statement
that every new full packet contains `u_*`; it does not infer a bounded
transversal, fixed apex pair, near model, or colouring.
