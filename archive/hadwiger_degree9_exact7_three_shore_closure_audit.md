# Adversarial audit: the central exact-seven three-shore closure

## Verdict

**RED as written; GREEN after one explicit integration repair.**

The branch-set table in
`hadwiger_degree9_exact7_three_shore_closure.md` is correct whenever at
least one of the old literals (3,4) is outside the central separator.
The source theorem producing the separator does **not** say that its two
exceptional vertices avoid (3,4).  If both exceptional vertices are
(3,4), the set (R) used by the proof does not exist.  That exceptional
placement is, however, exactly the degree-seven pure-Moser/two-exterior
cell.  The independent closure in
`hadwiger_moser_supported_pair_transfer_closure.md`, audited below, rules
it out.  With that theorem cited as a separate final case, the central
three-shore conclusion is valid.

The switch/gluing assertions in Theorems 2.1 and 3.1 of
`hadwiger_exact7_kempe_trace_exchange.md` are **GREEN**, subject only to
two wording clarifications recorded in Section 5.

## 1. What the central separator does and does not avoid

Theorem 4.5 of `hadwiger_four_connected_rooted_diamond.md` obtains

\[
 S=\{h,1,2,5,6,y,z\}
\]

from a separator in (F=G-\{h,1,2\}).  Its proof only gives

\[
 y,z\notin\{h,1,2,5,6\}.
\]

It gives no avoidance of (v,3,4,e_6,e_0,r_5).  Indeed, Section 5 of
that source explicitly warns that the carrier cuts need not avoid
(e_6,e_0,v,3,4).

After the three-shore boundary has been proved to be an induced pure
Moser spindle, some additional exclusions follow.

* Neither (y) nor (z) can be (v).  Inside (S), the vertex (v)
  would already see (h,1,2,5,6), whereas the Moser spindle has maximum
  degree four.
* Neither can be (e_6) or (e_0).  Each of these roots is adjacent to
  (h,1,2), while in each of the three possible labelled Moser rows the
  vertices (y,z) are anticomplete to (\{1,2\}).
* The current geometry does not rule out (r_5\in\{y,z\}).
* One or both of (3,4) can lie in (\{y,z\}).  In particular
  (\{y,z\}=\{3,4\}) is fully compatible with the labelled Moser row.

Thus the original sentence that a shore (C_v) contains all of
(v,3,4) is not derivable.

## 2. Exact repair when at least one literal is outside the cut

First use the preceding degree argument to obtain (v\notin S), and let
(C_v) be the component of (G-S) containing (v).  Suppose

\[
 \{3,4\}\nsubseteq S.
\]

Choose (x\in\{3,4\}-S), and let (R) be the component of
(C_v-v) containing (x).  This is the correct definition of (R).
It covers both cases:

* if both literals are outside (S), the edge (34) puts them in the
  same component;
* if exactly one is outside, that remaining literal alone supplies the
  required nonempty component.

In both cases (vx\in E(G)), hence (v\in N(R)), and

\[
 N_G(R)\subseteq S\cup\{v\}.
\]

Either untouched shore is a far side, so (N_G(R)) is a genuine
separator.  Seven-connectivity gives

\[
 |N_G(R)\cap S|\ge 6.
\]

Nothing else in the displayed branch-set proof uses the edge (34) or
requires both literals to lie in (R).  Therefore the original table
applies unchanged after this replacement.

The dependency-free verifier checks the appropriate conservative
quotient: (R) is represented by one connected bag adjacent to (v)
and to every boundary vertex except its possible unique defect, and the
other two shores are full.  Distribution of those contacts among
different vertices of (R) is irrelevant because the whole of (R)
is one bag.

## 3. Audit of the labelled rows and all branch sets

An independent enumeration of all (7!) label placements of the
standard Moser spindle subject to

\[
 h1,h2,12,16,26,56
\]

produces exactly the three boundary edge sets used by the verifier:

\[
\begin{array}{c|c}
1&5y,5z,yz,6y,hz,\\
2&5y,5z,yz,6z,hy,\\
3&5y,5z,yz,hy,hz.
\end{array}
\]

Hence (5yz) is a triangle and at least one of (hy,hz) is present.
There is no omitted labelled placement.

For each possible defect (d\in S\cup\{\varnothing\}), all displayed
bags are connected and disjoint.  The six adjacencies among the last
four bags are as follows.

* (d\in\{\varnothing,y,z\}): (vR,v5,v6,R5,R6,56).
* (d=h): after choosing (q\in\{y,z\}) with (hq), use
  (vR,v5,v6,R5,R6,56); (q) repairs only the missing contact to (h).
* (d\in\{1,2\}): for (A,\{v,5\},R\cup\{6\},B\cup\{y\}), use
  fullness of (A,B), the edge (vR), the edge (56), and the
  (R-y) contact.  The edges (16,26) repair the one missing triangle
  contact of (R).
* (d=5): use (vR,v6,v5,R6,Ry,56).
* (d=6): use (vR,v5,v6,R5,Ry,56).

Fullness supplies every remaining incidence with the singleton triangle
(h12).  The script replays all (3\times8=24) rows and all twenty-one
pairwise bag adjacencies.  This is an exact certificate for the
conditional branch-set theorem.

## 4. The exceptional placement and the independent pure-Moser closure

If (\{y,z\}=\{3,4\}), then (S=N(v)).  Since (d(v)=7), the
component of (G-S) containing (v) is exactly (\{v\}).  Three
shores therefore mean

\[
 G-N[v]=C_1\mathbin{\dot\cup}C_2,
\]

with both exterior components full to the pure-Moser boundary.  This is
precisely Theorem 4.1 of
`hadwiger_moser_supported_pair_transfer_closure.md`.

That theorem's dependency chain is sound:

1. Contracting the star (\{v,1,3\}) gives one fixed exact trace: (1,3)
   share one colour and the five roots (U=\{0,2,4,5,6\}) receive the
   other five colours distinctly.
2. Every missing edge of the (C_5) on (U) has a bichromatic path
   whose interior lies in at least one exterior component.  Unique root
   colours ensure that the interior cannot return to the boundary.
3. State exclusivity is ordinary labelled-partition gluing.  A common
   (D_i) or (T_{ij}) state uses at most five boundary colours, so the
   glued colouring of (G-v) extends to (v).
4. Two-anchor coverage follows by contracting (\{v,1,3\}) and the
   opposite full shore together with the endpoints of (e_i).  The
   remaining three roots avoid the two contracted colours; their only
   possible equality is one of the two missing (C_5)-edges disjoint
   from (e_i).  Thus the state is exactly (D_i) or an incident
   (T_{ij}).
5. If one side does not support (e_i), a Kempe interchange on the
   endpoint component gives (D_i) on that side.  For vertex-disjoint
   (e_i,e_j), the four colours are distinct, so the two swaps commute
   and give (T_{ij}).
6. The supported-pair transfer lemma is valid.  Paths for disjoint
   (e_i,e_j) use disjoint pairs of colours and are therefore
   vertex-disjoint.  A shortest connector inside the shore can be split
   at one edge to make two adjacent connected blocks.  Together with
   (\{v,1,3\}) and the leftover root, their contraction images form a
   literal (K_4).  The four blocks cover the boundary, so the induced
   opposite-side state is exactly (T_{ij}), with no hidden equality.
7. The fourteen words listed in that note are all the genuinely mixed
   orbits under the dihedral group and side interchange.  This is
   independently checked by canonicalizing all (3^5) support words.
   The short propagation proofs close five initial words and five
   transfer words; the disjoint-bi-support lemma closes the remaining
   four.  The combined dependency-free state verifier finds no feasible
   assignment for any of the fourteen representatives.
8. If no genuinely mixed word remains, one shore supports all five
   missing-cycle edges.  Kriesell--Mohr's pseudoforest theorem gives a
   rooted certificate in the five unique colour classes on that shore;
   the complementary edges already present in (M[U]) complete a rooted
   (K_5).  The other exterior component together with (\{1,3\}) is
   a connected sixth bag adjacent to all five, and (\{v\}) is the
   seventh.

The only presentational repair needed in the last item is to say
explicitly that one restricts to the vertices of the five unique colour
classes in (U\cup C_s), not necessarily to every vertex of (C_s).
The bichromatic support paths lie in that restriction.

Consequently the exceptional placement is independently impossible; it
must not be claimed as a consequence of the (R)-table itself.

## 5. Kempe-trace exchange audit

### Theorem 2.1

**GREEN.**  A join block is a union of blocks of every shore partition.
Switching precisely the bichromatic components whose nonempty boundary
traces lie in the join block (X) changes exactly the colours on (X)
on every side.  The side colourings continue to agree on (S), and
exactly one of (a,b) changes colour.  Restoring (ab) therefore gives
an (r)-colouring of (G).

If (a,b) lie in one join block, a shortest path in the bipartite
boundary/component support graph has distinct boundary nodes.  Two
successive component nodes cannot come from the same shore, since both
would contain their intervening boundary vertex and hence would be the
same bichromatic component.  The clean/dirty conclusion is exactly the
dichotomy according as a connector can avoid the other boundary
vertices.

### Theorem 3.1

**GREEN.**  In the operated/far incidence graph, the labels in one
incidence component form simultaneously

* a union of operated-side bichromatic component traces, and
* a union of far-side join blocks, hence a union of component traces in
  every far shore.

The proposed switches are therefore legitimate and induce the same
boundary change.  They switch (C_u) but not (C_x), so (ux) can be
restored.  This remains valid when (C_u) has empty boundary trace: it
is then an isolated left node, its switch changes no boundary colour,
and immediately repairs (ux).

Two wording clarifications are advisable.

1. Expanding a far-side join block may use several consecutive far
   shores.  The exact conclusion is that consecutive actual regions
   come from different shores; it need not alternate strictly
   `operated, far, operated, far` at the level of every single region.
2. For the first operated region, one displayed endpoint may be the
   interior vertex (u), rather than a boundary vertex.  Its clean
   connector should be defined as avoiding (S) except at its displayed
   boundary endpoint; the same shortest-path proof gives the named dirty
   hit otherwise.

Neither clarification affects the synchronized switching theorem or
the central-edge corollary.

## 6. Correct final statement

The source theorem should be replaced by the following dependency-exact
version.

> **Corrected central three-shore closure.**  Assume the central
> exact-seven outcome and three full shores.  The boundary is the pure
> Moser spindle.  If at least one of (3,4) lies outside the separator,
> define (R) using that literal and apply the 24-row branch-set table.
> If both lie in the separator, then the separator is (N(v)), the
> (v)-shore is (\{v\}), and Theorem 4.1 of the independently audited
> pure-Moser two-exterior closure gives the contradiction.  Hence the
> central exact-seven outcome cannot have three shores.

There is one small omitted justification in the inherited boundary
classification: a (K_4)-free graph on seven vertices is
four-colourable.  Choose a nonedge; the remaining five-vertex
(K_4)-free graph is three-colourable (a minimal four-chromatic graph on
at most five vertices is (K_4)).  Adding this sentence makes the chain
`three shores -> four-chromatic boundary -> pure Moser` explicit.
