# Independent audit: mobile-path exchange

## Verdict

**GREEN AS PATCHED.**  Theorem 1, Lemma 2, Theorem 3, the repaired
Corollary 4, and the 13-vertex barrier are correct under their written
hypotheses.  The repairs in Section 5 have been applied to
`results/hc7_mobile_path_exchange.md`: the whole portal sets are now
explicitly nonempty and pairwise disjoint, and the protected-helper
version now imports all required avoidance and attachment hypotheses.
This audit does not infer that a raw `HC_7` carrier has that protected
support.

## 1. Rooted total-contraction state: GREEN

For two distinct portals `r_i,r_j` of one mobile bag, the interval `X` is
an induced path with at least two vertices.  In a proper-minor-minimal
non-six-colourable graph its total contraction is a proper minor and has
chromatic number exactly six by the audited bipartite total-contraction
lemma.  Thus every selected six-colouring of `G/X` is a legitimate input
to the bilateral full-palette theorem.

Using the path as spanning tree, the returned tree edge is some
`r_kr_{k+1}` with `i<=k<j`; its two components are exactly the two path
intervals displayed in (1.6).  They contain `r_i,r_j`, respectively, so
both have literal edges to the same unchanged bag `Q`.  Equation (1.7)
is exactly the audited theorem with the whole interval `X` removed from
the external neighbourhood.

When `|X|>=3`, at least one of the two interval contractions is genuine,
so the two-block graph is a proper minor.  Corollary 2.5 of the source
theorem says precisely that no six-colouring of it induces, modulo one
global palette permutation, the total-contraction state on the actual
boundary `N_G(X)`.  This is a marked actual-boundary statement; it does
not label any of the five secondary colours by a foreign bag.

## 2. Five-carrier frame and literal `K_7`: GREEN

Merging one rim edge of `K_2 join C_4` leaves three connected rim-derived
bags forming a triangle.  The two common rows are adjacent to one another
and complete to those three bags.  Hence every `mathcal K_h` is a literal
five-bag clique model.

Under Theorem 3, set

`L^+=L union Z_L` and `R^+=R' union Z_R`.

The packet hypotheses make these sets connected; packet disjointness and
avoidance of the path and five carriers make all seven sets disjoint.  The
old path-cut edge joins `L^+` and `R^+`.  Each original shore contacts four
carriers and its packet supplies the unique fifth contact.  Consequently

`L^+, R^+, S, T, U_h union U_{h+1}, U_{h+2}, U_{h+3}`

are seven connected pairwise adjacent literal branch sets.  Coincident
missed-carrier labels cause no problem because the two repair packets are
disjoint.  If one shore misses no carrier, leaving that shore unaugmented
is valid.

## 3. Direct four-terminal support: GREEN

In the first paragraph of Corollary 4, the two prescribed disjoint paths
inside `Z` themselves are the packets.  Their `l,r` ends have literal
edges to the two path shores, and their `x,y` ends have literal edges to
the assigned missed carriers.  Since `Z` avoids the path and all five
carriers, Theorem 3 applies directly.

The current proof's instruction to delete a terminal when it belongs to a
retained carrier is inapplicable: (3.1) puts all four terminals in `Z`, and
`Z` is explicitly disjoint from every retained carrier and from the path.
Replace that sentence simply by “take the two paths as `Z_L,Z_R`.”

## 4. Why the original advertised compositions needed repair

The set-rooted rural theorem requires four **nonempty, pairwise disjoint
whole portal sets** in one 4-connected graph.  Corollary 4 currently says
only that the “four portal classes lie in a 4-connected connector.”  In a
raw carrier, a connector vertex can meet a path shore and a foreign bag,
or meet both foreign bags, so the four attachment sets can overlap.  The
quoted theorem then does not apply.  Four selected distinct vertices do
not make the four whole portal classes disjoint.

The final protected-support paragraph is also underspecified.  The audited
two-portal theorem supplies both shores with one common row only when it
has four distinct protected terminals (or its explicitly stated flexible
attachment hypotheses).  To combine that duplication with a helper for a
different missed carrier, the helper must avoid the support and all branch
bags, be disjoint from the helper assigned to the other shore, and already
attach to its assigned shore and missed carrier.  These are material
conditions from the audited support theorem, not consequences of the words
“supplied by a disjoint helper.”

Accordingly, the conclusions “every four-portal 4-connected connector”
and “the protected support ... plus a disjoint helper” are not established
under the written hypotheses.  No counterexample to the repaired versions
is asserted.

## 5. Exact repairs to Corollary 4

Replace its 4-connected paragraph by the following conditional statement.

> Put
> `A=N_Z(L)`, `B=N_Z(R')`, `P=N_Z(K_L)`, and `Q=N_Z(K_R)`.
> Assume `Z` is 4-connected and these four sets are nonempty and pairwise
> disjoint.  Then the set-rooted Two Paths theorem gives either disjoint
> `A-P` and `B-Q` paths, which are the packets of Theorem 3, or a planar
> connector with all four whole portal sets on one facial cycle in the
> alternating block order `A,Q,P,B` (up to reflection).

Replace the protected-support paragraph by a statement which explicitly
assumes either:

1. four distinct terminals `l,r,x,y` in an old exterior support `K`, with
   `l,r` attached to opposite path shores and both `x,y` attached to the
   common missed carrier; or the flexible attachment hypotheses of
   Theorem 3 of the audited support note; and
2. every additional helper family is pairwise disjoint, avoids `K`, the
   path and all five carriers, and already attaches to its assigned path
   shore and corresponding missed carrier.

Under those hypotheses the cited support theorem gives the two protected
paths or its exact cutvertex-portal-arm/degenerate-gate alternative; in the
path outcome, adjoining the stated helpers gives the seven bags already
audited in Section 2.

The opening/status claim should receive the same qualification: a
2-connected support forces the two paths only for four distinct protected
terminals and with the stated helper compatibility.

## 6. The 13-vertex probe: GREEN as a barrier only

The displayed bags in (4.3) form a valid tree decomposition.  Every edge
of `K_2 join C_4`, every path edge, and every listed endpoint/mobile contact
appears in a bag.  For each vertex, its bags form a connected subtree of
the displayed bag tree.  The largest bag has six vertices, so the graph
has treewidth at most five and cannot contain a `K_7` minor.

The label-minimality argument is also correct.  The only path vertex
adjacent to either label `0` or `1` is `p_0`.  If a retained connected row
omits it, the prefix has only one edge to the retained interval, so after
assigning prefix vertices to foreign bags that edge can restore at most
one of the two distinct row duties.  Thus `p_0` is forced.  The symmetric
argument with labels `2,3` forces `p_6`; an induced-path connected set
containing both ends is the whole path.

Running

`python3 active/hc7_mobile_path_probe.py`

returned

`NO 7 {0, 1} {2, 3} {4: {1, 2, 3, 4}, 5: {5}}`

and

`min labelled row (7, (6, 6, 6, 6, 6, 6, 6))`.

The connected-branch-set search is exhaustive: connected vertex sets are
enumerated as bitmasks, disjoint pairwise-touching families are searched in
canonical increasing-mask order, and reaching seven sets is exactly a
`K_7` minor model.  The labelled assignment search checks all assignments
of path vertices to the row or six old bags and verifies connectedness and
every required quotient edge.

This graph is low-connected and not contraction-critical.  It is only a
valid barrier to an unconditional palette-to-label or static
label-incidence inference.
