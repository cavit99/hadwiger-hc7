# Cold audit: Kempe-component parity obstruction

**Verdict:** **GREEN after two palette-size scope repairs.**  The algebraic
theorems, the multigraph cycle criterion, and the two defect-peeling
calculations are correct.  The result is presently **YELLOW as an `HC_7`
proof-spine advance**: it does not by itself close the overlap-one `G1`
cell, produce a literal `K_7`, or produce a global support-six transversal.

Audited source SHA-256:

```text
830f9c618f1f763215938c7ca894f4d04447164bc5a550b95a8e331f961825e7
```

## 1. Unsigned quotient

In Theorem 1.1 every deleted row starts with two `alpha` ends.  Switching
a family of whole `alpha,beta` components preserves the colouring of
`K`.  A row becomes proper exactly when precisely one of its two quotient
components is switched.  Thus repairing all rows is exactly a
two-colouring of `Gamma_beta`; a loop is correctly an immediate
obstruction.  This proves both Theorem 1.1 and Proposition 1.2.

Corollary 1.3 also retains the right objects.  A shortest non-loop odd
cycle in a multigraph has distinct quotient vertices and distinct retained
edges, so it lifts to disjoint connected two-colour components joined
cyclically by distinct literal rows.  It need not be induced in `G`, and
the source does not claim that it is.

For three quotient edges, a loopless nonbipartite multigraph must contain
a three-cycle.  Parallel edges give only two-cycles and cannot create an
odd cycle on two quotient vertices.  Hence Corollary 2.1 is exact.  The
matching hypothesis is not needed for quotient parity, but is correctly
used to make all six row endpoints literal distinct vertices.

### Sharp examples

* `C_3` with one edge deleted gives the loop alternative.
* Write `C_9` cyclically as three paths
  `x_i-z_i-y_i` joined by the deleted matching rows
  `y_i x_{i+1}` (indices modulo three).  Colour every `x_i,y_i` by
  `alpha` and every `z_i` by `beta`.  The common deletion is three
  disjoint two-colour components and the quotient is a literal triangle.
  Thus the triangle alternative is sharp and, by itself, is only a
  `K_3` carrier.
* Two disjoint paths `x_1-z-x_2` and `y_1-w-y_2`, with deleted rows
  `x_1y_1,x_2y_2`, give two parallel label-one quotient edges.  Restoring
  them gives `C_6`; the quotient is balanced and switching one component
  repairs both rows.  This confirms that parallel all-equal rows are not
  an obstruction.

## 2. Signed `GF(2)` system

For a row whose endpoint colours lie in `{alpha,beta}`, its final colour
difference is

\[
 c_2(u)\oplus c_2(v)\oplus s(C_u)\oplus s(C_v).
\]

Requiring this to equal one gives exactly equation (3.2), with

\[
 \rho(uv)=1\oplus c_2(u)\oplus c_2(v).
\]

Rows outside `F_{alpha beta}` retain their equality status: zero endpoints
are switched, or one endpoint switches between `alpha,beta` while the
other keeps a third colour.  Therefore a solution gives precisely

\[
             \operatorname{Eq}_F(c)-F_{\alpha\beta},
\]

not merely a subset of this set.

A binary difference system on a multigraph is soluble exactly when every
cycle has right-hand-side xor zero.  For a loop this says its label is
zero; for two parallel edges it says their labels agree.  Hence the
label-one loop, differently labelled parallel pair, and xor-one triangle
are the complete obstructions with at most three quotient edges.

As an explicit signed sharpness example, delete the matching rows
`x_1y_1,x_2y_2` from the five-cycle

```text
x_1-z-x_2-y_2-y_1-x_1.
```

In the remaining components colour `x_1,x_2,y_1` by zero and `z,y_2` by
one.  The two quotient rows are parallel; `x_1y_1` has label one and
`x_2y_2` has label zero.  Their two-cycle is unbalanced, and the restored
graph is the nonbipartite `C_5`.  Thus parallel quotient edges cannot be
discarded or replaced uniformly by triangles.

An exhaustive independent check of all signed three-edge multigraphs on
one through four quotient vertices found no missing obstruction.  The
numbers of inconsistent systems were respectively `7,64,314,1056`; every
one contained a label-one loop, a differently labelled parallel pair, or
an xor-one triangle.

## 3. Defect peeling

Corollary 3.3 is the consistent/inconsistent dichotomy for the displayed
linear system, so its two outcomes are mutually exclusive and exhaustive.
When `F` is a matching, contraction of the residual equal rows is legal:
the rows are disjoint, every other deleted row is proper, and every
non-row edge was already proper in `K`.  No same-colour quotient conflict
is introduced.

The two special patterns are correct with explicit palette-size
hypotheses.

1. For the `2+1` pattern, a colour `beta` outside
   `{alpha,delta}` must exist.  Then the two repeated-colour rows are the
   only quotient edges and both have label one.  The only inconsistent
   possibility is a label-one loop; two parallel label-one rows form a
   balanced two-cycle.  Otherwise switching a solution repairs exactly
   those two rows and leaves the exact singleton `delta` state.
2. For the `1+1+1` pattern, a colour `beta` outside the three row colours
   must exist.  The quotient contains one label-one row.  It is
   inconsistent exactly when that row is a loop; otherwise the switch
   repairs it and leaves the exact double state.

The audited source now includes:

* `p>=3` to the `2+1` instruction; and
* `p>=4` to the `1+1+1` instruction.

Both conditions hold in the intended six-colour `HC_7` application, so
this is a scope repair rather than a mathematical failure there.  Without
them the commands “choose beta” are not defined.  The trust boundary also
now clarifies that three distinct row colours lie outside a **single
simultaneous** two-colour treatment.

## 4. Comparison with existing support-six machinery

The peeling states do not materially advance the current frontier by
themselves.  The audited missing-colour matching transition already starts
from every nonempty exact state and gives, for each named split row,
either

* a literal missing-colour path avoiding its singleton `K_4` core; or
* a legal lower exact state carried by one connected two-colour component.

That result works without first classifying the row equality colours.  In
the non-loop branch here, the switching set may be a disconnected union of
components, so the new peeling theorem has less carrier geometry even
though it relates the new state to the same chosen colouring.

The common-colour triangle is genuinely new packaging, but it supplies
only three mutually adjacent carriers.  To obtain `K_7`, four further
pairwise adjacent bags must each contact all three carriers.  The three
support-six models do not provide those contacts: for row `e_i`, adjacency
to its singleton core `Q_i` is distributed between the two triangle
carriers incident with `e_i`, and says nothing about the third carrier.
The cores `Q_i` need not agree.  If all three split models already share
one singleton `K_4` core and have disjoint rows, the existing common-core
composition theorem gives `K_7` without the parity theorem.

In particular, the triangle outcome does not bypass the exact
order-six-arm/overlap-one `G1` barrier.  It retains useful internal
two-colour connectivity, but a new labelled contact-allocation or
row-splitting theorem is still required to connect those three carriers
to four common bags.  Until such a decoder is proved, this result is a
clean reusable parity lemma rather than a discharged proof-spine step.

## 5. Palette-component extension

The later palette-component Theorem 4.1 is also **GREEN**.  Identify a
`q`-colour palette `A` with `Z_q`.  Adding one fixed group element to all
colours in one component of `K[c^{-1}(A)]` is a permutation of `A` and
preserves every edge internal to that component.  Any `K`-edge with both
endpoint colours in `A` lies inside one such component, while an edge
with exactly one endpoint colour in `A` remains proper against a colour
outside `A`.  Therefore independent cyclic shifts on the components
preserve the colouring of `K`.

A proper `q`-colouring of the quotient assigns different shifts to the
two components incident with every monochromatic deleted row.  Since the
two row endpoints start with the same colour, their final colours then
differ.  This would repair all rows and `p`-colour `G`; hence the quotient
is not `q`-colourable.

If the quotient is loopless, a `(q+1)`-critical simple subgraph has
minimum degree at least `q` and consequently at least
`binom(q+1,2)` distinct simple edges.  Each requires a distinct retained
row.  At equality it has exactly `q+1` vertices, is `q`-regular, and is
therefore `K_{q+1}`; all rows are already used, so no parallel or other
nonisolated quotient edge remains.  Both the strict edge threshold and
the equality carrier statement are correct.

For three equal deleted rows and `p>=3`, choose a three-colour set `A`
containing their at most three common row colours.  Since
`3<binom(4,2)`, the quotient has a loop.  Thus some named row has a path
in `K` using at most those three colours.  This uniform path is valid,
but need not be bichromatic or avoid a named singleton `K_4` core.

## 6. Final trust boundary

Promote as GREEN:

* the unsigned odd-cycle/repair equivalence;
* the labelled loop-or-triangle conclusion for three matching rows;
* the arbitrary signed `GF(2)` criterion, retaining loops and parallels;
* defect peeling and contraction descent;
* the `2+1` and `1+1+1` calculations after adding the palette-size
  hypotheses;
* the palette-component chromatic obstruction and its sharp edge
  threshold; and
* the uniform three-colour row path.

Do not promote:

* any inference from the triangle alone to `K_7` or a global
  `tau_5^{<=6}` pair;
* any claim that the peeling components for different colour pairs are
  disjoint; or
* any claim that equality-set size gives a global decreasing rank.
