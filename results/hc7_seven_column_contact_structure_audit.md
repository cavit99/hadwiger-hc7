# Independent audit: structure of a seven-column contact graph

**Audited file:** `hc7_seven_column_contact_structure.md`
**Mathematical source SHA-256:**
`960bebf9fd702d4c2e807301539f4e18a071e1dd69dbf4dd71f3ed2b885a6f70`
**Promoted source SHA-256:**
`b48e19642347571a713f60d2b045be85907bfe6a07052465ba09d2446d516859`
**Audit date:** 2026-07-20
**Verdict:** **GREEN.**  The seven-vertex classification, all displayed
minor models, the literal `K_7` lift, the clean-path augmentation, and the
localization of unused components are correct at the audited revision.

This audit is independent of the proof's original derivation.  No graph
census or unproved structure theorem is used.

The promoted revision differs from the audited mathematical revision only
in its status paragraph, which now links this GREEN audit.  No theorem
statement, proof, or trust-boundary claim changed.

## 1. Complement classification in Theorem 1.1

Assume `delta(J)>=4` and set `H=overline J`.  Then `Delta(H)<=2`.
Extending `H` on its fixed seven-vertex set to an edge-maximal graph `H^+`
of maximum degree at most two is legitimate, and complementation reverses
edge inclusion:

\[
                         \overline{H^+}\subseteq J.
\]

The classification of `H^+` is exhaustive.  In an edge-maximal graph of
maximum degree at most two, any two distinct nonadjacent vertices of degree
at most one could otherwise be joined.  Hence those vertices form a clique
of order at most two.

- If there are two, they are adjacent and each has degree one.  They form a
  `K_2` component, while the other five vertices form `C_5`.
- If there is one, all other vertices have degree two.  The handshaking
  lemma makes its degree even, hence zero.  The other six vertices form
  either `C_6` or `2C_3`.
- If there is none, the graph is two-regular on seven vertices, hence is
  either `C_7` or `C_3 dotcup C_4`.

These are exactly the five graphs displayed in (1.3).

## 2. Explicit `K_5` models and the surviving graph

Every row of the table following (1.3) was checked branch set by branch
set.

1. For `H^+=C_7`, the sets
   `{0,3}`, `{1,5}`, `{2}`, `{4}`, `{6}` are connected in the complement
   and pairwise adjacent.
2. For `H^+=C_3 dotcup C_4`, the same five sets are connected; the cross
   edges between the two components and the two diagonals of the
   quadrilateral supply every required adjacency.
3. For `H^+=C_6 dotcup K_1`, `{0,2,4}` is a triangle in the complement;
   `{1}`, `{3}`, `{5}` are pairwise adjacent there, and the isolated vertex
   of `H^+` is universal in its complement.
4. For `H^+=2C_3 dotcup K_1`, `{0,3}` and `{1,4}` are connected by cross
   edges, all displayed branch sets are mutually adjacent, and vertex `6`
   is universal in the complement.

Thus the first four possibilities give a `K_5` minor already in
`overline{H^+}`, hence in `J`.  Only `H^+=C_5 dotcup K_2` can survive.

If `H` omits the `K_2` edge `ab`, the two resulting adjacent poles are
complete to the rim `\overline{C_5}\cong C_5`; contracting the rim to a
triangle gives a `K_5` model.  If `H` omits a cycle edge, relabelled
`c_0c_1`, the five sets in (1.5) form a `K_5` model exactly as claimed:

\[
 \{a,c_2,c_4\},\quad \{b\},\quad
 \{c_0\},\quad \{c_1\},\quad \{c_3\}.
\]

The nonsingleton set is connected through `a`; the other four sets are a
clique; and `a`, together with `c_2`, supplies all adjacencies from the
first set.  The construction remains valid if `H` omits further edges.
Consequently `H=H^+`, and

\[
                      J=\overline{K_2 dotcup C_5}.
\]

This graph is the planar pentagonal bipyramid.  Its six missing edges are
the pole-pole edge and the five complementary rim edges; the preceding two
models show that adding any one creates a `K_5` minor.  Its
four-connectivity is also verified correctly in the revised proof.  If a
pole survives deletion of at most three vertices, it connects all surviving
rim vertices and any other surviving pole.  If neither pole survives, at
most one rim vertex was deleted, so the remaining rim is connected.

The two alternatives in Theorem 1.1 are exclusive because the pentagonal
bipyramid has minimum degree four.

## 3. Quotient separation

For a vertex `x` of degree at most three, the two sets

\[
          \{x\}\cup N_J(x),\qquad V(J)-\{x\}
\]

form a separation with intersection `N_J(x)`.  There is no edge from `x`
to the other open side by definition, and that side has order
`6-d_J(x)>=3`.  Corollary 1.2 is therefore correct.

The source explicitly and correctly confines this conclusion to the
seven-vertex contact graph.  A quotient separator vertex represents a whole
literal column, so this calculation gives no bounded-order separator of the
host graph.

## 4. Lift from the contact graph

The nine subgraphs in (2.1) are pairwise disjoint and connected.  If the
column-contact graph `J` has a `K_5` model, then for each branch set of that
model, the union of its corresponding literal columns is connected: a
spanning tree in the quotient branch set lifts edge by edge to literal
column contacts.  Distinct unions are disjoint and adjacent exactly where
the quotient model requires.  Both fixed roots are adjacent to every such
union and to each other.  Adjoining the two roots therefore gives seven
pairwise adjacent connected branch sets in `G`.

The revised second outcome of Theorem 2.1 states all hypotheses needed for
the same lift after a modification.  The modified columns are pairwise
disjoint and connected, avoid the fixed roots, retain adjacency to both
roots, and have contact graph containing `J+xy`.  Edge-maximality of the
pentagonal bipyramid supplies a `K_5` model in `J+xy`, so the claimed
explicit `K_7`-minor model follows.  No destroyed old contact or changed
root is silently assumed.

## 5. Clean-path augmentation and extremal quantifier

For Lemma 2.2, truncate the `L_x`--`L_y` path at its last vertex in `L_x`
and first subsequent vertex in `L_y`.  Its remaining internal vertices lie
outside all nine old subgraphs.  Absorbing all vertices except the final
`L_y` vertex into `L_x` therefore:

- preserves connectivity of `L_x`;
- preserves pairwise disjointness of all nine subgraphs;
- retains both old root contacts and every old column contact; and
- adds the missing contact `xy` through the final path edge.

Thus the new contact graph contains `J+xy`, not merely the new edge `xy`.
In the bipyramid case Theorem 2.1 gives a `K_7` model.  More generally,
there are only finitely many systems in the fixed finite host, so a system
maximizing `|E(J)|` exists.  In a `K_7`-minor-free host its modified contact
graph cannot contain a `K_5` minor, while its edge count is strictly larger;
this contradicts the extremal choice.  The extremal quantifier is therefore
used correctly.

## 6. Localization of unused components

Let `Z` be a component outside all nine subgraphs.  If it has neighbours in
noncontacting columns `L_x,L_y`, a path inside connected `Z`, together with
its two incident column edges, is a clean path of the kind excluded by
Lemma 2.2.  Hence the set of column labels met by `Z` is a clique in `J`.

In the pentagonal bipyramid the poles are nonadjacent and the rim has clique
number two.  Every clique is contained in a maximal clique consisting of
one pole and the endpoints of one rim edge.  Corollary 2.3 follows, including
the bound of three met columns.

## 7. Trust boundary

The audited result proves only:

- the exact seven-vertex quotient classification;
- a correct lift of a quotient `K_5` model to a host `K_7` model when the
  fixed roots and literal columns satisfy the stated conditions;
- a safe augmentation by a path whose interior avoids every old root and
  column; and
- clique localization for components outside an edge-maximal literal
  column system.

It does **not** prove that a low-degree contact-graph vertex has a small
literal neighbourhood, turn a quotient separation into an order-seven host
separation, preserve an operation-specific boundary colouring, identify a
palette colour with a column label, or decrease the selected response
shore.  Edge maximization is only a finite normalization of literal column
systems.  The source states these limitations accurately and does not prove
`HC_7` or the remaining response-coupling theorem.

At the audited hash, the source is therefore **GREEN**.
