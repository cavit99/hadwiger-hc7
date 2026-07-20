# Independent audit of the static exact-block anchor barrier

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks
[`hc7_one_sided_full_trace_static_anchor_barrier.md`](hc7_one_sided_full_trace_static_anchor_barrier.md)
at SHA-256

```text
28440ff45233f523947c5ae18503d3248cbee075c3eae584bb78705a06c4d270
```

and
[`hc7_one_sided_full_trace_static_anchor_barrier_verify.py`](hc7_one_sided_full_trace_static_anchor_barrier_verify.py)
at SHA-256

```text
75cb3fe6d6fad3ec01d0929d5533de2799ba673797e446791eb58f43d31ce002
```

The repaired statement explicitly concerns abstract families of boundary
partitions and does not assume that they are extension relations of actual
shore graphs.  With that qualification, the construction proves exactly
the stated barrier.

## 1. Boundary graph and full-trace orientation

The graph is `H=K_{2,6}` with bipartition classes

```text
A={a_0,a_1},  B={b_0,...,b_5}.
```

It has the standard width-two tree decomposition, so it has no `K_5`
minor.  The verifier also checks this independently by enumerating every
choice of five pairwise disjoint nonempty connected branch sets and all ten
required adjacencies.

In every surjective proper five-colouring the palettes on `A` and `B` are
disjoint.  Hence `p(c)=|c(A)|` is one or two.  Both values occur.  If
`p(c)=1`, all four other colours occur on `B`, so no vertex of `A` has a
different legal colour.  If `p(c)=2`, each colour on `A` occurs there once;
recolouring an `A`-vertex with the other `A`-colour would cease to be
surjective, while every `B`-colour is forbidden by adjacency.  Recolouring
a vertex of `B` does not change `p(c)`.  Thus every proper, surjectivity-
preserving one-vertex recolouring preserves the declared orientation.

## 2. The two abstract partition families

For `K_{2,6}`, every independent set lies wholly in `A` or wholly in `B`.
The definitions cover all of them:

- `A` and `B` themselves occur as blocks in the displayed coarse
  partitions in both families;
- each singleton in `A` occurs in a displayed split-`A` partition in both
  families; and
- every nonempty proper subset `J` of `B` occurs as a block through the
  unordered cut `{J,B-J}`, with the joined/split choice on `A` reversed at
  the one distinguished cut.

The families are disjoint.  Their five-block members are separated by
whether `A` is joined or split.  Among the lower-block members, comparison
of that same choice together with the number and identity of the blocks on
`B` separates every listed type; the exceptional distinguished cut is
placed on opposite sides precisely to avoid overlap.  The extra right-hand
four-block partition has joined `A` and three blocks on `B`, a type absent
from the left family.

Because the construction is specified by unlabelled equality partitions
and includes every labelling of their blocks, both families are invariant
under all permutations of the five colour names.  Their five-block members
partition all proper surjective five-colourings according to `p(c)=1` or
`p(c)=2`.

## 3. Verifier reproduction

Running

```sh
python3 active/hc7_one_sided_full_trace_static_anchor_barrier_verify.py
```

returns

```text
PASS partitions=309 full_partitions=155 left=97 right=123 anchors=66 full_colourings=18600 moves=194400
```

The enumeration covers every proper equality partition with at most five
blocks, all 66 nonempty independent sets, all labelled surjective proper
five-colourings, and every legal one-vertex recolouring which remains
surjective.  Its assertions check language membership, disjointness,
anchor coverage, and invariance of `p(c)` on every one of the 194,400
directed recolouring moves.

## 4. Exact trust boundary

This is only a barrier to a conclusion drawn from abstract, static
boundary-partition data.  The two families are **not** proved realizable as
the extension relations of two connected boundary-full shores, and their
anchor partitions are not tied to any specified deletion or contraction.
The construction omits the ninth boundary vertex and all
operation-specific host data.  It is not asserted to occur in a
seven-connected, seven-chromatic, contraction-critical,
`K_7`-minor-free graph and is not a counterexample to `HC_7`.

Accordingly, the example does not refute a theorem using actual shore
realizability, operation-coupled colourings, or a host-level
path/separation alternative.  It proves only that exact-block completeness
of two abstract partition families cannot by itself force a change of the
full-trace orientation.
