# Independent audit of surjective partition connectivity

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source
[`hc7_order8_surjective_partition_connectivity.md`](hc7_order8_surjective_partition_connectivity.md)
at SHA-256

```text
7256b95862bd4a8e0e626682cbd9988436698b1285125ae5df9c451b7d401f2f
```

and the deterministic verifier
[`hc7_order8_surjective_partition_connectivity_verify.py`](hc7_order8_surjective_partition_connectivity_verify.py)
at SHA-256

```text
a4a0dbbc5e4950587a3d58e3a999d498a14cfd1efac9c8d7cd2fe796501aefb9
```

The equality-partition quotient, exhaustive order-eight census, exact
`K_5`-minor test, opposite-language one-edge deduction, and stated host
scope are correct.  This is a computer-assisted finite boundary theorem;
it does not prove `HC_7`.

The pinned revision differs from the independently checked draft only by
promotion from `active/` to `results/` and the corresponding verifier
invocation path.  The theorem statement, proof, verifier and mathematical
scope are unchanged.

## 1. The quotient adjacency is exact

A surjective labelled five-colouring induces a partition into five
nonempty independent blocks.  A one-vertex recolouring remains surjective
exactly when its old block has order at least two and the vertex moves into
a different existing independent block.  Conversely, label the common
blocks consistently before and after any such partition move; the two
resulting labelled colourings differ only at the moved literal vertex.

The verifier uses restricted-growth words, of which there are exactly
`S(8,5)=1,050`, so every equality partition occurs once.  Its source-block
multiplicity check, target-block loop, properness membership check and
canonical relabelling therefore construct precisely `Q_5^sur(H)`.  Self
loops caused only by canonical naming do not affect connected components.

This is deliberately a quotient statement.  The labelled surjective
recolouring graph can have components interchanged by a global colour
permutation; extension relations invariant under all colour permutations
cannot distinguish such components.  The quotient is therefore the right
object for Theorem 3.1.

## 2. Exhaustiveness and minor detection

`geng -q 8` returns one representative of every unlabelled simple graph of
order eight, and the verifier asserts the exact stream order `12,346`.
Its backtracking routine tries every colour not used on an already coloured
neighbour in a degree-ordered recursion, so it decides three-colourability
exactly.

The reproduced census output is

```text
order8 graphs=12346 not_3_colourable=6322 nonconnected_five_block_partition_graph=236 empty=89
positive_control G?aN~w components=27,37 has_K5_minor=yes
low_chromatic_control G??F~w components=65,90
PASS order8_K5_minor_free_chromatic_at_least_four_partition_graph_connected
```

The `236` count uses “not exactly one component”; it intentionally includes
the `89` graphs with no proper five-block partition.  For each of the `236`,
the branch-set routine allows every retained vertex set of order five
through eight, every partition into five nonempty blocks, and unused
vertices.  It checks connectedness of every block and an edge between each
pair.  These are exactly the conditions for a `K_5`-minor model.  No one of
the `236` survives that test.  Hence a non-three-colourable,
`K_5`-minor-free graph of order eight has a nonempty connected partition
graph, as claimed.

The two controls check both directions relevant to accidental overclaiming:
one disconnected high-chromatic partition graph is accepted only because
it has a `K_5` minor, while the `K_{2,6}` control shows that minor exclusion
without the chromatic hypothesis does not ensure connectivity.

## 3. The ownership argument

Take a colouring in either nonempty extension language.  Since
`chi(H)>=4`, it uses at least four colours.  If it uses four, eight boundary
vertices in four nonempty classes leave a repeated class.  Giving one
vertex of that class the globally absent fifth colour is proper, retains
the old colour and is surjective.  If this neighbour belonged to the
opposite extension language, it would already be the desired one-edge
pair.  Under the contradictory assumption it therefore belongs to the
same language.  Thus each language owns at least one surjective trace.

Colour-permutation invariance makes ownership constant on every equality
partition, and exact ownership assigns every vertex of `Q_5^sur(H)` to
exactly one language.  Connectivity gives a partition edge across the two
nonempty ownership classes.  The exact lift from Section 1 gives two
labelled colourings differing at one vertex, and invariance preserves their
opposite memberships.  This proves Theorem 3.1.

In particular, this argument also checks a subtle endpoint point: a
four-colour endpoint necessarily has a surjective neighbour **in the same
extension language**, unless the desired one-edge conclusion has already
occurred.

## 4. Host corollary and trust boundary

Fixing the exact boundary root colour leaves five freely permutable colour
names on the eight-vertex residual.  Shore extension is invariant under
those permutations.  The maximum-palette alternative supplies exact
ownership of every surjective trace, and the live four-chromatic residual
is `K_5`-minor-free.  Theorem 3.1 therefore replaces the former
distance-at-most-two fork by a one-transition conclusion in precisely this
branch.

The finite theorem does not decode the remote ends of the two forced
bichromatic shore paths into named minor-model branch sets.  The general
one-transition theorem, rather than only its palette-dropping
specialization, must be used because the ownership-changing quotient edge
is surjective at both ends.  Seven-connectivity bounds the full
neighbourhood of a supporting shore component between seven and the nine
boundary vertices, but does not make an order-seven/eight outcome carry a
common trace.  No strict host descent or explicit `K_7` model is inferred
here.

The odd-wheel example in Remark 3.2 is proper and has the stated palettes:
the centre has colour `3`, the alternating rim segment uses `0,1`, rim
vertex `6` uses `2`, and the two adjacent rim vertices `0,1` receive the
new colour `4` in the two respective endpoint colourings.  It correctly
shows that the theorem finds a different global quotient edge rather than
invalidating every local adjacent-hole two-step path.
