# Static exact-block anchors do not change a one-sided full-trace orientation

**Status:** written finite barrier with deterministic verifier; separate
internal audit GREEN in
[`hc7_one_sided_full_trace_static_anchor_barrier_audit.md`](hc7_one_sided_full_trace_static_anchor_barrier_audit.md).
This is not a counterexample to `HC_7`.

## 1. Refuted principle

The following static principle is false.

> Let `H` be an eight-vertex, `K_5`-minor-free graph.  Suppose two disjoint,
> colour-permutation-invariant **abstract families of proper boundary
> partitions** together contain every proper surjective five-colouring of
> `H`, and each family realizes every nonempty independent set of `H` as an
> exact equality block.  The families are not assumed to be realizable as
> the extension relations of actual shore graphs.  Then some
> surjectivity-preserving single-vertex recolouring changes the family
> containing a full trace.

The construction below has all the stated properties, but the language of
every full trace is constant on every component of the single-vertex
reconfiguration graph.  It therefore rules out a purely static attempt to
close the one-sided full-trace alternative in the order-nine interface.

## 2. Boundary graph and full traces

Let

\[
 A=\{a_0,a_1\},\qquad B=\{b_0,b_1,b_2,b_3,b_4,b_5\},
 \qquad H=K_{A,B}=K_{2,6}.
\]

The graph has treewidth two, and in particular it has no `K_5` minor.
Every proper surjective five-colouring `c` uses disjoint palettes on `A`
and `B`.  Put

\[
             p(c)=|c(A)|\in\{1,2\}.
\tag{2.1}
\]

Let the full traces of the left language be exactly those with `p(c)=1`,
and let the full traces of the right language be exactly those with
`p(c)=2`.  These two sets are nonempty and partition all proper surjective
five-colourings.

The value `p(c)` is invariant under every single-vertex recolouring which
remains proper and surjective.  Indeed, if `p(c)=1`, then `B` uses the other
four colours, so neither member of `A` has a new legal colour.  If `p(c)=2`,
then the two colours on `A` occur there once each; recolouring one member of
`A` with the other colour would destroy surjectivity.  A recolouring in `B`
does not change `c(A)`.  Thus the orientation is locally constant on every
single-vertex reconfiguration component.

## 3. Two disjoint exact-block-complete languages

It remains to add lower-palette traces so that each language answers every
exact-block query.  We state the languages as families of unlabelled
equality partitions.  Taking every labelling of the blocks makes the
associated colouring relations invariant under all permutations of the
five colour names.

Write `A` for the block `{a_0,a_1}` and use vertical bars to separate
blocks.  Choose the distinguished cut

\[
                 C_* = \{\{b_0\},B-\{b_0\}\}.
\]

The left language `mathcal L` contains:

1. every five-block proper partition in which `A` is one block (equivalently,
   `B` is partitioned into four nonempty blocks);
2. the two-block partition `A | B`;
3. the distinguished four-block partition
   `a_0 | a_1 | {b_0} | B-{b_0}`; and
4. for every other unordered nontrivial cut `{J,B-J}` of `B`, the
   three-block partition `A | J | B-J`.

The right language `mathcal R` contains:

1. every five-block proper partition in which `a_0,a_1` are distinct
   singleton blocks (equivalently, `B` is partitioned into three nonempty
   blocks);
2. the three-block partition `a_0 | a_1 | B`;
3. the distinguished three-block partition `A | {b_0} | B-{b_0}`;
4. for every other unordered nontrivial cut `{J,B-J}` of `B`, the
   four-block partition `a_0 | a_1 | J | B-J`; and
5. the four-block partition
   `A | {b_0} | {b_1} | {b_2,b_3,b_4,b_5}`.

These families are disjoint.  This follows directly by comparing whether
`A` is joined or split and the number of blocks induced on `B`.  Their
five-block members are exactly the two full-trace orientations from
Section 2.

Every nonempty independent set of `H` lies wholly in `A` or wholly in `B`.
Both languages realize all of them as exact blocks:

- `A` and `B` are blocks of `A | B` on the left; on the right, `A` occurs
  in item 5 and `B` occurs in item 2;
- `{a_0}` and `{a_1}` occur in the distinguished four-block partition on
  the left and in item 2 on the right; and
- for every nonempty proper `J subset B`, the cut `{J,B-J}` is represented
  once in each language, with the joined/split choice on `A` reversed only
  at `C_*`.

Thus even exact-block completeness on both sides does not force the
orientation of a full trace to change along a local reconfiguration.

## 4. What additional host input is needed

The construction is an abstract pair of boundary extension languages.  Its
exact-block witnesses are merely members of those relations: they are not
claimed to be the colourings returned by contracting a specified connected
shore together with the queried independent set.  The eight-vertex graph
is the prospective restriction left after separating off the distinguished
singleton colour; the construction does not encode that ninth boundary
vertex or its literal adjacencies.

In particular, the construction does not assert the existence of a single
seven-connected, seven-chromatic, contraction-critical,
`K_7`-minor-free host realizing the two languages on opposite shores.  It
does not supply connected boundary-full open shores, and it does not encode
operation-specific colourings of edges or vertices inside either shore.
General finite-relation realization results are therefore not being used
to promote this static relation to an `HC_7` host.

Consequently, a positive theorem must use an operation-coupled hypothesis.
One sufficient form would say that an exact-block response produced by a
specified deletion or contraction can be refined, through the same closed
shore and without changing its attained orientation, to a surjective
five-colour trace.  A weaker usable conclusion would be that failure of
such a palette-preserving refinement returns an actual smaller
full-neighbourhood separator or an explicit `K_7`-minor model.  Static
existence of all exact blocks cannot provide that step.

## 5. Verification

Run

```sh
python3 active/hc7_one_sided_full_trace_static_anchor_barrier_verify.py
```

The verifier enumerates all proper equality partitions with at most five
blocks, checks the two language definitions, checks every independent-set
anchor, checks every full trace and every single-vertex reconfiguration,
and independently checks `K_5`-minor exclusion by exhaustive branch-set
enumeration.
