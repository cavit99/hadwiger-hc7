# Independent audit of the labelled first-hit Rado reduction

**Audit status:** separate internal audit.

**Audited source:** `results/hc7_labelled_first_hit_rado_reduction.md`

**Audited source SHA-256:**
`2bde8b468d236f26322d0072a503183efbc93f6bec9fa67f4a1a9fd101c9174f`

## Verdict

**GREEN AS PATCHED.**  The directed gammoid, Rado rank criterion, directed
Menger certificate, literal host-neighbourhood lift, seven-connectivity
exposure dichotomy, and fixed-three-vertex corollary are correct under the
stated unit-capacity source and pairwise-disjoint terminal hypotheses.

During the audit one ambiguity was repaired.  The source now creates one
sink copy `hat(t)` for each terminal vertex `t`, then adds one incoming arc
for every nonterminal--terminal edge.  The previous wording could be read
as creating a separate copy for every incidence, which was not the object
used later in the proof.

The theorem is an exact linkage reduction.  It does not prove that the
unused-label exposure is small, preserve a connected source branch set of
capacity greater than one, or synchronize colourings across the returned
order-seven separation.

## 1. Directed encoding of clean first hits

The directed network contains the vertices of `H-T`, replaces their edges
by both orientations, and gives each literal terminal `t` one sink copy
`hat(t)`.  The only arcs incident with `hat(t)` enter it from the
nonterminal neighbours of `t`.

Consequently a directed `P`--`hat(t)` path expands uniquely to a host path
whose last vertex is `t` and whose other vertices avoid the entire terminal
union.  Conversely every clean host path contracts at its terminal end to
such a directed path.  This correspondence preserves pairwise vertex
disjointness and distinct source and terminal endpoints.

The sink orientation is essential.  If terminal copies were ordinary
undirected vertices, a copy with two nonterminal neighbours could be used
internally.  The four-vertex path example in the source demonstrates this
failure exactly.

## 2. Gammoid and Rado quantifiers

After reversing every arc, take `P` as the fixed sink set and restrict the
presented strict gammoid to the ground set `hat(T)`.  A set of terminal
copies is independent precisely when it can be linked by vertex-disjoint
paths to distinct vertices of `P`.  By reversing those paths, its rank on
`hat(T_I)` is exactly the clean-linkage number `r_P(T_I)` defined in the
source.

Rado's independent-transversal theorem therefore applies to the families

\[
                  \widehat T_1,\ldots,\widehat T_m.
\]

It gives a transversal independent in that gammoid if and only if

\[
                  r_P(T_I)\ge |I|
                  \qquad(I\subseteq[m]).
\]

Because the literal terminal families are pairwise disjoint, the selected
terminal endpoints are distinct.  Gammoid independence supplies distinct
source endpoints.  Hence the independent transversal is exactly the clean
labelled linkage stated in Theorem 1.1, with neither a missing Hall
condition nor an extra pairing assumption.

If the inequalities fail, the deficient index set is nonempty.  Directed
vertex Menger, with endpoint vertices permitted in a separator, gives a
set `Z` of cardinality `r_P(T_I)<|I|` meeting every relevant path.
Unselected terminal copies occur on no path to `hat(T_I)`, since they are
sinks.  A minimum-cardinality Menger set therefore contains no such copy;
this justifies the literal map in (2.1).

## 3. Host-neighbourhood lift

The map from `Z` to `bar(Z)` is injective: nonterminal vertices retain
their names and distinct selected sink copies map to distinct literal
terminals.  Thus

\[
                         |\overline Z|=|Z|.
\]

Since `|P|>=m>=|I|>|Z|`, a source survives.  Let `C` be its component in
the nonterminal host after deleting the nonterminal members of `Z`.
Every nonterminal neighbour of `C` belongs to `Z`.  If a selected terminal
`t in T_I` met `C` and `hat(t)` were not in `Z`, a path inside `C` followed
by the final arc to `hat(t)` would avoid `Z`, contradicting the Menger
property.  The only other possible neighbours of `C` are literal vertices
in the unselected terminal classes.  This proves (2.3).

Also `|T_I|>=|I|>|Z|`, so some selected terminal copy survives.  The
corresponding literal terminal cannot meet `C`, by the preceding argument,
and belongs neither to `C` nor to the displayed containing set for its
neighbourhood.  Hence the containing set genuinely separates a nonempty
connected side from a nonempty opposite side.

## 4. Seven-connectivity and exposure

Write

\[
 e_C=|N_H(C)\cap(T-T_I)|.
\]

The two pieces of the containing set in (2.3) are disjoint, so its order is
`|Z|+e_C`.  Seven-connectivity gives `|N_H(C)|>=7`.  Therefore:

- `e_C<7-|Z|` is impossible;
- if `e_C=7-|Z|`, the containing set has order seven, so every inclusion
  is equality and it is exactly `N_H(C)`;
- otherwise integrality gives `e_C>=8-|Z|`.

This verifies both Theorem 2.1 and the exhaustiveness of (2.5).  Notice
that the argument uses literal vertex counts; a contracted connected
subgraph cannot be counted as one separator vertex.

## 5. Fixed deleted vertices

For Corollary 2.2 the fixed set `F` is removed from the routing network and
is restored only in the host-neighbourhood estimate.  The Menger part has
order at most `|I|-1`, at most three literal vertices come from `F`, and
condition (2.6) contributes at most one terminal vertex for each of the
`m-|I|` unused labels.  Thus for `m=5` the host boundary has order at most

\[
        (|I|-1)+3+(5-|I|)=7.
\]

The surviving selected terminal again supplies a nonempty opposite side.
Seven-connectivity consequently forces the boundary to have order exactly
seven.  No endpoint or empty-side case was omitted.

## 6. Exact trust boundary

The proof requires all of the following.

1. `P` is a set of at least `m` literal vertices and every path uses a
   distinct source.  Paths sharing one source branch set are a capacitated
   problem, not this unit-capacity gammoid.
2. The terminal families are pairwise disjoint.  Prescribed labels on both
   source and target families would be a different disjoint-paths problem.
3. Terminal copies are directed sinks.  Ordinary undirected terminal
   clones do not encode first hits.
4. The small separator conclusion additionally needs the unused-label
   exposure bound.  Rado and Menger alone provide only a relative cut.
5. The order-seven separator is structural only.  Compatible boundary
   equality partitions for colour gluing require a separate theorem.

Within this scope, the source proof is complete.
