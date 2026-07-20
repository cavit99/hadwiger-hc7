# Independent audit: positive boundary excess with one frozen opposite shore

**Verdict: GREEN.**  This is a separate internal mathematical audit, not
external peer review.  The current source revision is
[`hc7_order8_positive_excess_frozen_outer_shore.md`](hc7_order8_positive_excess_frozen_outer_shore.md)
at SHA-256

```text
b9e913fbece2258d4a9d8448c2ea414a5f2b76df7ab895ffe3a13a115becc9f3
```

The complete mathematical source was independently audited at SHA-256

```text
87d98eeb318dc164f14493450c600f8534caa96deaa1e585dcf0f06f0a6501e8
```

There were two editorial revisions after the mathematical audit.  First,
the source promoted its opening status from “independent audit pending” to
the adjacent GREEN-audit link and reflowed the immediately following scope
sentence; that status-only revision had SHA-256
`cbaeea1363054cfebe8c657065826f016277c9bd20b00433d38cd6d6acd932ab`.
Second, the project-specific term “literal duty” was replaced by the
standard descriptive term “required boundary set”, and the notation
`D_U(C_i)` was replaced everywhere by `R_U(C_i)`.  Its defining vertex set

\[
 C_i\cup\{u\in U:E_G(u,C_i)=\varnothing\}
\]

and the Hall-incidence condition requiring a neighbour at every vertex of
that set are unchanged.  The corresponding prose substitutions
“supports a duty” to “meets a required boundary set” likewise change no
hypothesis, conclusion, or proof step.  The staged diff confirms that these
are the only changes from the status-only revision.  Restoring both
editorial revisions reproduces the audited mathematical hash.  No
mathematical content changed.

The theorem is an unbounded conditional reduction.  It does not close the
remaining two-piece obstruction or prove `HC_7`.

## 1. Audited inputs

The cited GREEN inputs were checked at the following source revisions:

- ordered two--three allocation:
  `3f62092ab492815d5c21489e001e5732da76bc28454dac75206ba5aa61299dde`;
- positive-excess host lift:
  `a2bb06c0c6301f5a1a5d806b3e2dd1cebb9f8c9b71fcc50e4b1fd5d30632981e`;
- transported-partition Hall reflection:
  `e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4`;
- incident-edge bichromatic bypass:
  `5d5a5eda08701262a1bf6b821194aacd7192a41f0ecf997134764b5b59c80961`;
  and
- generic exact-seven response restart:
  `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a`.

The host-lift identity is literal:

\[
 N_G(E)=B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad W=N_G(E)\cap D.
\]

There are no `E`--`R` edges, and the exact induced normalization accounts
for every remaining neighbour.  Thus `E` is a component of `G-B`, every
vertex of `B` has a neighbour in `E`, and `|W|>=2` gives `|B|>=9`.

## 2. Full-neighbourhood response sides and strictness

Let `K` be a component of `G-B` other than `E`.  Its full neighbourhood is
contained in `B`.  If it misses a member of `B`, then

\[
                  7\le |N_G(K)|<|B|.
\]

The lower bound uses a genuine separation: `K` is nonempty, while the
component `E` remains outside `K union N_G(K)`.  The upper inequality is
strict because `N_G(K)` is a proper subset of the literal set `B`.

For a crossing edge `xy`, every six-colouring of `G-xy` gives its ends one
colour; otherwise the edge can be restored.  Its restrictions colour both
edge-deleted closed shores.  If the induced partition extended through the
intact `K`-shore, a palette permutation would align the two boundary
assignments and give a six-colouring of `G`.  Therefore this is exactly a
full-neighbourhood response side, and it strictly decreases boundary order
as claimed in outcome 2.

## 3. The third-component `K_7` construction

The edge between `P_0,P_1` places them in one component `C_0` of `G-B`.
Suppose there were a further component `C_1` besides `E,C_0`.  The four
connected subgraphs

```text
E, C_1, P_0, P_1
```

are pairwise disjoint.  The first two are full to `B`, while the last two
are full to `S`; hence all four meet every vertex of

\[
 A\cup Q
  =\{x_e,y_e,x_0,y_0\}\cup\{d,x_d,y_d\}.
\]

Assigning the four vertices of `A` bijectively to those four connected
subgraphs gives four disjoint connected branch sets.  For two such sets,
the underlying subgraph of either one has a literal edge to the boundary
anchor of the other, so the four are pairwise adjacent without any assumed
edge between their underlying subgraphs.  Each is adjacent to all three
singletons in `Q`, and `Q` is a triangle.  These are seven explicit
pairwise adjacent branch sets.  Thus a third component really gives a
`K_7`-minor model.

Consequently, outside the terminal minor outcome, `G-B` has exactly the two
components `E,C`, with `C` connected and containing `P_0 union P_1`.

## 4. Maximal-coverage normalization of `C`

Eligible pairs exist because `P_0,P_1` form one.  The source selects
`Q_0,Q_1` with maximum covered vertex set subject to the literal
containments `P_i\subseteq Q_i`.  If a component `Z` of the uncovered
induced subgraph existed, connectedness of `G[C]` would give an edge from
`Z` to at least one selected subgraph.  Adding all of `Z` to that subgraph
preserves disjointness, connectedness, both prescribed containments, and
therefore every old contact with `S`, while increasing coverage.  Hence

\[
                         C=Q_0\mathbin{\dot\cup}Q_1.
\]

Passing to the induced graphs on these vertex sets preserves connectedness,
and connectedness of `C` supplies an edge between them.  No unclassified
ambient component remains.

## 5. The fixed partition and the first Hall orientation

The fixed colouring restricts to `G[E union B]` and induces `Pi`.  If the
same partition extended through `G[C union B]`, equality of the boundary
blocks would allow a global colour permutation and gluing.  Thus `Pi` is
legal on `E` and rejected on `C`.

For the first application of transported-partition reflection, the coloured
shore is `E`, the opposite shore is `C`, and the single support is the
whole connected subgraph `E`.  It is boundary-full because `B=N_G(E)`.
The demand is positive: a partition of at least nine vertices into at most
six colour blocks has a nonsingleton block, which cannot belong to a clique
of singleton blocks.  With one universal support, demand at most one gives
a saturating matching and would reflect `Pi` to `C`.  The rejection above
therefore forces demand at least two.  Item 4 is correctly oriented.

## 6. The operation-specific partitions and the second Hall orientation

Let `uv` be an `E`--`B` edge and let `psi` colour `G-uv`.  Because the only
deleted edge has an endpoint in `E`, the restriction to `G[C union B]` is
proper.  If its boundary partition `Sigma` extended through the intact
`E`-shore, that extension would glue to the restriction and six-colour
`G`.  Thus `Sigma` is legal on `C` and rejected on `E`.

In the second Hall application the coloured shore is therefore `C`, the
opposite shore is `E`, and `Q_0,Q_1` are the two named supports.  They are
disjoint, connected and adjacent, exactly as required.  They need not be
`B`-full: their incidence with a block is defined by meeting its complete
literal required boundary set.  A saturating matching would transport `Sigma` to the intact
`E`-shore and contradict rejection, so no such matching exists.

Each `Q_j` is adjacent to all of `S`, hence to all seven vertices of
`S-{e}` in `B`.  Any literal required-set vertex witnessing an absent incidence
edge must consequently belong to

\[
                         B-(S-\{e\})=W.
\]

This proves the claimed location of every failed required-set contact without
identifying a palette colour with a branch-set label.

## 7. The exact Hall residues at demand at most two

The demand is nonzero.  For one required boundary set, Hall failure means
that neither support is incident with it.  For two required boundary sets,
Hall failure either already has such an isolated set or the two sets together have at most one
incident support.  These are exactly the two forms stated in the source.

In the isolated-set form, absence of the two incidence edges supplies
vertices `w_0,w_1 in W` missed by `Q_0,Q_1`, respectively.  They are
distinct: `C=Q_0 dotcup Q_1` is full to `B`, so no literal boundary vertex
can be missed by both parts.  The opposite part therefore meets each missed
vertex, as claimed.

If both `Q_0,Q_1` happen to be `B`-full, both are universal vertices in the
incidence graph.  They saturate every family of at most two required sets, so the
proved absence of a saturating matching forces demand at least three.

## 8. The incident-star proper-minor transition

For `w in W`, the definition of `W` gives a neighbour `u in E`, and
fullness of the other component `C` gives a neighbour `q in C`.  Since
`E,C` are distinct components of `G-B`, `u,q` are nonadjacent.  Contracting
the literal two-edge tree `u-w-q` is therefore a proper minor whose
six-colouring expands to `G-{wu,wq}` with `w,u,q` monochromatic.  Every
hypothesis of the GREEN-audited incident-edge bypass theorem is present.

In the bypass outcome, switching the component through `u` restores `wu`
and gives a colouring of `G-wq`; restricting this colouring to `E union B`
is proper.  Switching the component through `q` symmetrically gives a
colouring of `G-wu` whose restriction to `C union B` is proper.  If their
boundary equality partitions agreed, the two restrictions would align and
glue because `G-B` has exactly the anticomplete components `E,C`.
Therefore the partitions differ.

Both switched components avoid the common centre `w`.  If neither met
`B-{w}`, neither switch would change any boundary colour, so both resulting
partitions would equal the central partition.  At least one named
bichromatic component must therefore meet `B-{w}`.  Proposition 3.1 is
valid, including the saturated alternative and the two coupled one-edge
responses.

## 9. Optional extremal rank

Assume the optional lexicographic normalization.  For a nonempty proper
connected `A subsetneq E`, every neighbour outside `E` belongs to
`B=N_G(E)`, so the disjoint count is exactly

\[
 |N_G(A)|=|N_G(A)\cap E|+|N_G(A)\cap B|
           =|B|+h(A)-m(A).
\]

The old nonempty opposite side of the response interface remains outside
`A union N_G(A)`.  Hence deleting any `A`--`N(A)` edge makes `A` another
full-neighbourhood response side by the same restoration-and-gluing
argument.

If `h(A)<m(A)`, its boundary has smaller order.  Seven-connectivity gives
order at least seven, and the additional hypothesis excludes order seven;
it is therefore another positive-excess response side, contradicting the
primary minimization.  If `h(A)=m(A)`, its boundary has equal order but
`|A|<|E|`, contradicting the secondary minimization.  Thus

\[
                              h(A)\ge m(A)+1.
\]

If `A` is a component behind an internal separator `K` of `G[E]`, all its
internal neighbours lie in `K`, so `h(A)<=|K|`.  The displayed inequality
then gives

\[
 |N_G(A)\cap B|=|B|-m(A)\ge |B|-|K|+1.
\]

The rank is literal and well founded under its stated normalization.  The
source correctly presents it as optional; it does not assert that every
proper-minor transition preserves the full ordered order-eight data.

## 10. Trust boundary

The theorem closes the case of more than one component opposite `E`, except
when a strict boundary-order response descent has already been obtained.
Its final structural residue is one connected opposite component partitioned
into two adjacent connected `S`-full subgraphs, with exact operation-specific
Hall obstructions and coupled incident-edge colourings.

It does **not** prove that a Hall-deficient required set is repairable, assign the
five alternate colours to named branch-set labels, synchronize the two
intact closed-shore partitions at an order-seven separator, or close the
positive-excess branch.  No group action or holonomy invariant is proved.
Within this scope, no unresolved assumption remains.
