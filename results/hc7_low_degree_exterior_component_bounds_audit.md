# Separate internal audit: low-degree exterior-component bounds

**Verdict:** GREEN.

This verdict is within the finite-computation trust boundary in Section 7.

This is a renewed separate internal cold audit, not external peer review.
The source consolidates two older computer-assisted classifications whose
proofs and retained certificates were archived administratively.  It does
not prove `HC_7`.

## Exact revisions audited

The mathematical wrapper was audited at

```text
c056a899a89f5d868efd098c752902b93f23fce73027202205c6ce51816e80dc  audited theorem content
```

Promotion changed only its status paragraph.  The promoted source hash is

```text
4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29  results/hc7_low_degree_exterior_component_bounds.md
```

The incorporated archived proof appendices were checked at

```text
876e0f3c1364e2e835acc621f4c48009cb5197b75402ffef29a6bd61eee25f28  archive/hadwiger_degree8_degree9_exterior_bounds.md
65e09300daa18bb83b7f6fd155495f755f443a34cd73d23bd619f75ed3fe4c43  archive/hadwiger_degree8_three_component_closure.md
15baedfa85826e5850830c0ba3a93abbdbcba9166180866bd77f45ebb9b16383  archive/hadwiger_degree9_four_component_closure.md
87c629b8e1a2b0166468d09f2df14cf54f2fd7f72ac99e3290d8d8ec8ae7bd17  archive/hadwiger_degree89_component_closure_audit.md
```

The retained verifiers were checked at

```text
80d64be307046382d4d944d2332b338e051843f4a96026ca78ae357299ff3b69  archive/degree8_three_shore_verify.py
60e8a0d098c59f61f8e2549ba7507ba33b62824b11e6afa655947e584219ffab  archive/degree9_four_shore_verify.py
```

The SHA-256 aggregate of the three degree-eight certificate files, formed
by hashing their canonical `shasum -a 256` listing including paths, is

```text
00390c29fbd32f0de8b15a4bcdf8b9b422c4819bed9f0c9e7892484e5fa52843
```

and the corresponding aggregate for the twenty-three degree-nine files is

```text
8bd734a865ccafe06ff64f4969c3549bce3126eb27212037733b8bd6e13646df
```

Any mathematical change to the wrapper or incorporated appendices, or any
change to a verifier or certificate file, invalidates this audit until the
affected checks are renewed.

## Claim checked

For a seven-connected, seven-chromatic, `K_7`-minor-free graph whose
proper minors are six-colourable, the audit establishes

\[
 d_G(u)=8\Longrightarrow
   \#\operatorname{comp}(G-N[u])\le2,
 \qquad
 d_G(u)=9\Longrightarrow
   \#\operatorname{comp}(G-N[u])\le3.
\]

Together with the separately audited degree-seven theorem, the respective
upper bounds at degrees seven, eight, and nine are one, two, and three.

## 1. Analytic reduction

For every exterior component `D`, its boundary lies in `N(u)` and
separates `D` from `u`; seven-connectivity therefore gives at least
seven boundary neighbours.  The component consequently misses at most one
neighbour of a degree-eight vertex and at most two neighbours of a
degree-nine vertex.

The displayed independence bound is valid under the wrapper's hypotheses.
Contracting the star on `u` and an independent set `I subseteq N(u)`
is a proper minor.  If `|N(u)-I|<=4`, its six-colouring lifts with at most
five colours on `N(u)`; an unused sixth colour then colours `u`, a
contradiction.  Hence `alpha(G[N(u)])<=d_G(u)-5`.

The initial packing arguments were checked separately.  Four one-miss
components in degree eight, or five two-miss components in degree nine,
give an `N(u)`-meeting `K_6` model.  In degree nine, the representative
argument covers the common-unused-vertex cases and the exceptional
`P_3 dotunion 3K_2` incidence form is repaired using the independence
bound.  Adding `{u}` produces a `K_7` model.  Thus it remains only to
exclude exactly three components in degree eight and exactly four in
degree nine.

## 2. Exhaustive boundary types

In degree eight, three singleton misses have exactly the equality patterns
`000`, `001`, and `012`, up to boundary and component permutations.
These are exactly the three certificate inputs.

In degree nine, the four two-element miss sets are four edges of a loopless
multigraph, with parallel edges allowed.  A separate half-edge enumeration
generated all 1,657 restricted-growth partitions of eight labelled
half-edges subject to looplessness and quotiented them by all edge
permutations and endpoint flips.  It independently returned exactly the
twenty-three types used by the verifier, including types with parallel
misses and unused boundary vertices.

Enlarging a smaller miss set to the prescribed size merely deletes
component-boundary edges.  Every model or usable partition found in this
weakened quotient remains valid in the original host.

## 3. Certificate encodings

The independence clauses say exactly `alpha(H)<=3` on eight boundary
vertices and `alpha(H)<=4` on nine.  For each independent-block
partition, the verifier reconstructs block independence, connectivity of
each component-block union, every required pairwise adjacency, every
allowed assignment, and the optional singleton adjacencies.

For each listed quotient model, it checks six nonempty disjoint bags,
boundary meeting, connectivity through every nontrivial bag cut, and all
fifteen pairwise bag adjacencies.  Fixed component-boundary edges are
constants and boundary edges are Boolean variables, so the formulas are
exact for the weakened quotients.

The degree-eight files contain respectively 141, 183, and 98 model
templates.  The twenty-three degree-nine files contain 423 in total.  The
claim is that every boundary satisfying the independence bound has either
one of these checked model templates or one of the checked usable
partitions; no assertion is made that the template lists enumerate every
possible minor model.

## 4. Quotient lift

Replace each contracted component vertex in a quotient bag by its original
connected component.  Disjointness, bag connectivity, and pairwise
adjacency all lift edge by edge, and every lifted bag retains a boundary
vertex.  Thus a quotient outcome gives an `N(u)`-meeting `K_6` model
in `G-u`; adding the singleton `{u}` completes an explicit `K_7`
model.

## 5. Proper-minor colouring and gluing

For a retained exterior component, the proof contracts the star consisting
of `u` and its assigned independent boundary block, and contracts every
other exterior component together with its assigned independent block.
The usability conditions give connected, pairwise adjacent contraction
sets.  The star contraction makes the minor proper.

After six-colouring that minor, deleting the other exterior components and
expanding the independent blocks gives a proper colouring of the retained
closed side.  Edges internal to a block do not exist, and every edge from
an expanded block was represented at the contracted image.  The clique of
images gives distinct block colours.  Colour permutations align these
colours over all retained components, which are pairwise anticomplete.
At most four boundary colours occur in degree eight and at most five in
degree nine, leaving a colour for `u`.  Hence every usable-partition
outcome contradicts `chi(G)=7`.

## 6. Fresh verification

The degree-eight verifier was rerun under CPython 3.14.6 with Z3 5.0.0 and
returned

```text
degree8_three_shore_certificate_0.txt verified UNSAT with 141 model templates
degree8_three_shore_certificate_1.txt verified UNSAT with 183 model templates
degree8_three_shore_certificate_2.txt verified UNSAT with 98 model templates
```

All twenty-three degree-nine types were also rerun in parallel under the
same environment.  Every type returned `verified UNSAT`; the template
counts were

```text
10 13 15 15 13 14 13 21 13 18 22 24 17 18 20 20 26 20 23 25 19 17 27
```

and sum to 423.

## 7. Trust boundary and provenance

The computer-assisted portion trusts CPython and `ast.literal_eval`, the
two audited verifier implementations, Z3 and its Python bindings, and the
retained certificate-template files.  The certificate files list model
templates rather than proof-producing UNSAT traces.  A fully formal
version would require a checked proof-producing encoding or a
proof-assistant reconstruction.

Repository history shows that these sources entered the repository already
under `archive/`; no later retraction or counterexample was found.
Their placement was administrative and is not a mathematical invalidation.
This renewed audit promotes only the concise current wrapper: the original
appendices, verifiers, and certificates remain in `archive/` to preserve
their exact provenance.

The result is an unbounded host theorem with a finite boundary
classification.  It does not synchronize the remaining component
colouring languages, solve the one-component tight-pole case, or prove
`HC_7`.
