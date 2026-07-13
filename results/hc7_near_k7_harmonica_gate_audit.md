# Independent audit: harmonica structure at a two-heavy rural gate

## Verdict

**GREEN after a wording correction.**  The Postle--Thomas hypotheses
hold exactly, the direction and endpoint order of Theorem 1.3 are used
correctly, and every resulting list-colouring glues to the fixed
colouring outside the carrier.  The theorem statement was corrected so
that the one-singleton harmonica outcome and the two-singleton residue
are disjoint, and so that containment is attributed to the pair
`(K,L)` rather than to an informally specified canvas.  The subsequent
four-connectivity exclusion is also valid: exact list inheritance, not
containment alone, puts the first harmonica triangle on the original
outer cycle.

## 1. Exact imported theorems

Postle--Thomas Theorem 1.2 applies to a plane graph with outer cycle
`C`, two arbitrary (not necessarily adjacent) vertices `p1,p2` of `C`,
lists of size at least five off `C`, lists of size at least three on
`C-{p1,p2}`, and lists of size at least two at `p1,p2`.  Its conclusion
is unconditional `L`-colourability.

Their Theorem 1.3 has the same hypotheses except that
`|L(p1)|>=1` and `|L(p2)|>=2`.  It states

\[
 G\text{ is }L\text{-colourable}
 \quad\Longleftrightarrow\quad
 (G,L)\text{ contains no colouring harmonica from }p_1\text{ to }p_2.
\]

Thus the direction needed here is valid: non-`L`-colourability forces a
contained colouring harmonica, ordered from the singleton-list endpoint
to the two-list endpoint.  “Contains” means that an appropriate subgraph
with the inherited lists is a colouring harmonica; it does not assert
that the whole pair is itself one.

## 2. Plane and list hypotheses

The selected `F` is explicitly the outer facial cycle of the connected
plane graph `K`, so it is the outer cycle required by both imported
theorems.  Every vertex of `K` with a neighbour in the actual adhesion
`S` lies on `F`.  Hence every vertex off `F` has no boundary neighbour
and receives the full six-element list, stronger than the required
interior size five.

After contracting `K` to `z`, every member of `S=N_G(K)` is adjacent to
`z`.  Properness of `c` therefore gives `c(s)!=alpha=c(z)` for every
`s in S`.  Consequently

\[
             \alpha\in L(u)
             \qquad\text{for every }u\in V(K),
\]

so all lists are nonempty.  On `F`, a nonheavy vertex sees at most three
boundary colours and hence has list size at least three.  A heavy vertex
has a nonempty list of size one or two.  These are precisely the list
sizes used in the case split.

## 3. Exhaustive two-heavy split

If both heavy lists have size at least two, Theorem 1.2 applies directly,
regardless of whether the two heavy vertices are adjacent.  It colours
`K`.

Otherwise a heavy list is a singleton.  Since every list contains
`alpha`, it must be `{alpha}`.  If the other heavy list has size two,
Theorem 1.3 applies with the singleton vertex as `p1` and the two-list
vertex as `p2`.  Colourability gives the first outcome; failure of
colourability gives a contained colouring harmonica in exactly that
direction.  If the other list is also a singleton, it too equals
`{alpha}` and Theorem 1.3 is not invoked.  This is exactly the retained
double-singleton outcome.  For either vertex, list `{alpha}` is
equivalent to seeing all five non-`alpha` palette colours on its literal
boundary neighbours.

After the wording correction, these three cases are mutually exclusive
and exhaustive.

## 4. Gluing check

The minor colouring `c` restricts to a proper colouring of `G-K`.  For
each `u in K`, the list `L(u)` excludes every colour used by `c` on an
actual neighbour of `u` in `S`.  Therefore an `L`-colouring of `K` is
proper on edges internal to `K` and conflicts with no edge from `K` to
`S`; all remaining edges are already proper under `c`.  The two
colourings consequently glue to a proper six-colouring of `G`.

## 5. Four-connectivity exclusion

The definition of containment is essential here.  A contained colouring
harmonica may use a subgraph whose outer face exposes vertices that were
interior in `K`; faciality in the subgraph alone would not put its first
triangle on `F`.  Postle--Thomas containment does, however, preserve the
original list exactly at every retained vertex.

For a colouring harmonica from the singleton endpoint `x`, the first
recursive clause supplies a triangle `xuv` with

\[
 L(u)-L(x)=L(v)-L(x),\qquad |L(u)-L(x)|=2.
\]

Here `L(x)={alpha}` and every carrier list contains `alpha`.  Hence the
inherited original lists satisfy

\[
                 L(u)=L(v)=\{\alpha,\beta,\gamma\}
\]

for two further colours.  Both auxiliary vertices therefore have list
size exactly three.  Under the fully rural attachment hypothesis every
vertex strictly inside the original outer cycle has the full
six-element list, so neither `u` nor `v` is interior.  Thus `x,u,v` all
belong to the original cycle `F`.

The outer facial boundary of a three-connected plane graph is an
induced cycle; a chord would make its ends a cut of order at most two.
Four-connectivity supplies this property, and the four distinct portal
representatives ensure `|F|>=4`.  Three vertices on an induced cycle of
length at least four cannot span a triangle.  This excludes the
one-singleton/two-list harmonica at the stated scope and leaves only the
double-singleton state when there are exactly two heavy vertices in a
non-six-colourable host.

## Scope

Theorem 1 closes all two-heavy states with two two-element lists and
reduces the exactly-one-singleton case to a contained,
direction-labelled colouring harmonica.  Theorem 2 additionally excludes
that harmonica for a four-connected carrier whose outer cycle contains
four distinct literal portal representatives.  It does not eliminate
the double-singleton state, states with at least three heavy vertices,
or produce a prescribed model linkage or one global two-apex structure.
