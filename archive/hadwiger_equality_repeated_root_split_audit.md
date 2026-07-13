# Audit of the repeated-root equality packet closure

## 1. Verdict

**GREEN after one hypothesis repair.**  Proposition 4.2 and Corollary 4.4
must assume that `G` is not six-colourable.  The two-shore web argument
only says "crossing or a six-colouring"; seven-connectivity,
minimum degree seven, and `K_7`-minor-freeness alone do not exclude its
second outcome.  The intended equality-gate application is
proper-minor-minimal non-six-colourable, so the repaired hypothesis is
available.

With that addition:

* the last cyclic hull is literally the order `(1,2,5,6)`;
* its opposite terminal pairs are `1-5` and `2-6`;
* the exact quotient check forces that crossing into the repeated-root
  shore for every one of the thirty negative rows; and
* after making the two carriers adjacent, the seven displayed branch bags
  form a valid `K_7`-model.

The closure applies only to seven-edge missing graphs having exactly three
vertices of missing degree at least two.  Equivalently, it closes the four
pendant leaves on a missing triangle, including the balanced `(2,1,1)`
case.  It does **not** close all seven-edge boundaries.

## 2. Exact crossing convention

In the normalized missing graph

\[
 E(Q)=\{01,02,12,03,04,15,26\},                    \tag{2.1}
\]

the order

\[
                            (1,2,5,6)                 \tag{2.2}
\]

is a cyclic hull.  The only edges of `J` on these four vertices are

\[
                           25,56,61;
\]

they are consecutive in (2.2).  The two nonconsecutive/opposite pairs are

\[
                              \{1,5\},\quad\{2,6\}.  \tag{2.3}
\]

Thus a crossing in a shore consists of vertex-disjoint connected paths
between the `1`- and `5`-portal sets and between the `2`- and `6`-portal
sets.  If one uses literal boundary-to-boundary paths, deleting their
boundary endpoints leaves nonempty disjoint connected carriers in the
shore: `15` and `26` are missing boundary edges, so each literal path has
at least one interior vertex.  If the society convention starts directly
at portal vertices, those portal paths themselves are the carriers.

The verifier's construction is exact.  For a hull
`(h_0,h_1,h_2,h_3)`, it uses

\[
 \{h_0,h_2\}\mid\{h_1,h_3\}
\]

and its reverse as the two orientations.  The other three boundary labels
are assigned independently to either side, giving all eight minimal
covering rows.  Overlap contacts in an actual full split may be deleted,
so these eight rows exhaust every crossing split relevant to minor
existence.

## 3. Why the crossing is in the repeated-root shore

For each of the three possible common triangle pairs, Proposition 4.1 has
ten negative repeated-root rows.  Suppose the `(1,5)/(2,6)` crossing were
in the opposite shore.  Extend its two disjoint carriers to a connected
covering split, contract that split and the repeated-root split, and retain
only one assigned contact for each overlap label.  This gives exactly the
eleven-vertex quotient tested by
`double_split_quotient()`.

The complete search considers all support orders seven through eleven and
all 159,027 candidate seven-bag partitions.  For every negative
repeated-root row, both orientations, and all eight remaining-label
assignments, the quotient contains a `K_7`-model.  Hence the crossing
cannot occur in the opposite shore.  Non-six-colourability and the
two-shore web theorem force a crossing in at least one shore, so it occurs
in the repeated-root shore.

The verifier was strengthened during this audit.  It now asserts, for
each individual row,

```python
assert (1, 2, 5, 6) not in survivable_hulls
```

and asserts that the intersection over all rows has exactly this one
forced hull.  This matches the proposition, rather than merely checking
that some hull is forced.

## 4. Making the two carriers adjacent

Let `C_15,C_26` be the two disjoint nonempty connected carriers in the
connected repeated-root shore `R`.  Choose a shortest path

\[
 v_0v_1\cdots v_k,qquad
 v_0\in C_{15},\quad v_k\in C_{26}.
\]

Its internal vertices avoid both carriers.  If `k=1` the carriers are
already adjacent.  Otherwise assign an initial segment of
`v_1,...,v_{k-1}` to `C_15` and the remaining terminal segment to
`C_26`.  The enlarged carriers remain nonempty, connected and disjoint,
retain their four portal contacts, and have an edge between them.  No
other vertex of `R` is needed by the final model.

This operation does not assume that the carriers align with the earlier
repeated-root bipartition `R=X dot-union Y`; that split has already served
to force the crossing location.  The final minor may discard all unused
vertices of `R`.

## 5. Complete adjacency replay for the final bags

Put

\[
\begin{array}{lll}
 A_0=\{0,5\},&A_1=\{1\}\cup C_{15},&
 A_2=\{2\}\cup C_{26},\\
 A_3=\{3\},&A_4=\{4\},&A_6=\{6\},
\end{array}
\]

and use the opposite full shore `D` as the seventh bag.

Connectivity is literal:

* `05` is a boundary edge, so `A_0` is connected;
* the `1`-portal contact connects `1` to `C_15`;
* the `2`-portal contact connects `2` to `C_26`; and
* the other four bags are connected by definition.

The only pairs requiring more than an untouched boundary edge are:

| Bag pair | Supplying edge |
|---|---|
| `A_0,A_1` | the `5-C_15` portal edge, since both `01` and `15` are missing |
| `A_0,A_2` | boundary edge `52`, repairing missing `02` |
| `A_0,A_3` | boundary edge `53`, repairing missing `03` |
| `A_0,A_4` | boundary edge `54`, repairing missing `04` |
| `A_1,A_2` | the constructed `C_15-C_26` edge, repairing missing `12` |
| `A_2,A_6` | the `C_26-6` portal edge, repairing missing `26` |

For completeness, `A_0A_6` has the boundary edges `06` and `56`;
`A_1` sees `A_3,A_4,A_6` through `13,14,16`; `A_2` sees
`A_3,A_4` through `23,24`; and `A_3,A_4,A_6` form a triangle.
The full shore `D` has an edge to a boundary vertex in each of the other
six bags.  The seven bags are disjoint because the boundary vertices,
the two carriers in `R`, and the opposite component `D` are pairwise
disjoint.

Hence they form a `K_7`-model.  The direct replay in
`audit_forced_packet_completion()` independently checks connectedness,
disjointness and all 21 adjacencies.

## 6. Exact scope

If a seven-edge graph `Q` has exactly three vertices of degree at least
two, equality in the low-degree count forces:

* those three vertices to induce a triangle;
* the other four vertices to be independent degree-one leaves; and
* the leaf multiplicities to be one of

\[
              (4,0,0),(3,1,0),(2,2,0),(2,1,1).
\]

The first three distributions are quotient-positive by Proposition 4.1.
The forced packet closes only the final `(2,1,1)` distribution.  Together
these prove Corollary 4.4 for the **three-high pendant-triangle class**.

They do not address a seven-edge missing graph with four or more vertices
of degree at least two.  The verifier contains a sharp warning example:
a `K_4` on `1,2,3,4` plus the pendant edge `01`, with one repeated-root
row full and the other contacting only the common pair `{1,2}`, has no
`K_7` in the ten-vertex static split quotient.  Thus replacing the scope
by "all seven-edge equality boundaries" would be false at the level of
the proved static data.

## 7. Final status

The packet closure is a valid complete elimination of one infinite shore
family over the normalized balanced boundary.  It is not a closure of the
general equality gate, the other seven-edge degree patterns, or denser
boundaries.  Those cases still require the repeated-root split exchange or
operation-state descent stated in Section 5 of the source note.

