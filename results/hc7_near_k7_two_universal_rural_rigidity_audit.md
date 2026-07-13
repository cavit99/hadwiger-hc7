# Independent audit: two-universal rural rigidity

## Verdict

**GREEN after the incorporated small-order clarification.**  The join
Hadwiger equivalence, connectivity equivalence, Wagner consequence and
the mixed-bag `K_7` model in Proposition 2 are all correct.

## 1. Join and clique minors

If `H` has a `K_5` model, adjoining the two adjacent universal
singletons gives a `K_7` model.  Conversely, a `K_7` model in
`K_2 vee H` has at most two bags containing the two universal vertices.
After deleting those bags, at least five connected pairwise adjacent bags
remain wholly in `H`.  Their internal connectivity and mutual model
edges use only `H`, so they form a genuine `K_5` model there.  Thus

\[
       K_2\vee H\text{ is `K_7`-minor-free}
       \quad\Longleftrightarrow\quad
       H\text{ is `K_5`-minor-free}.
\]

## 2. Connectivity

If `|H|<=5`, then `|K_2 vee H|<=7`, so the join is not seven-connected
under the standard order convention.  Otherwise, any cut of `H` of
order at most four becomes a cut of the join after adding the two
universal vertices.  This proves the forward implication.

For the converse, after deleting at most six vertices of the join, a
surviving universal vertex connects the entire remainder.  If both are
deleted, at most four vertices were deleted from the five-connected
graph `H`, whose remainder is connected.  Hence the join is
seven-connected.  This checks both separator and order edge cases.

## 3. Wagner input

The named consequence is stated with the correct hypothesis: every
4-connected `K_5`-minor-free graph is planar.  It is the 4-connected
case of Wagner's structure theorem for `K_5`-minor-free graphs.  Since a
five-connected `H` is 4-connected, the theorem applies and the literal
universal pair is one global planarizing pair.

## 4. A third universal vertex

Deleting two selected vertices from five-connected `H` leaves a
three-connected graph.  Every three-connected graph has a `K_4` minor.
For any three distinct vertices of `R`, the seven displayed bags

\[
 \{r_1,h_1\},\ \{r_2,h_2\},\ \{r_3\},\ Q_1,Q_2,Q_3,Q_4
\]

are disjoint and connected.  The first three are pairwise adjacent via
the join edges `r_1h_2,h_1r_3,h_2r_3`; each sees every `Q_i` through its
`R` vertex; and the four `Q_i` form a clique model.  No edge of `R` is
assumed.  Thus Proposition 2 gives a literal `K_7` model even when `R`
is disconnected.

The note correctly limits its conclusion: two literal adjacent universal
vertices force one rural remainder, but a bounded capacity state need not
contain literal universal vertices or a common local apex pair.
