# Audit of the surjective five-colouring Kempe barrier

Verdict: **GREEN**.

Audited source:

```text
barriers/hc7_surjective_five_colour_kempe_connectivity_barrier.md
SHA-256 319c53e51a7acc2027eb2c0238e5251219552a941b3eb817faee5fa97cd137dd
```

Checked verifier revisions:

```text
barriers/hc7_surjective_five_colour_kempe_connectivity_barrier_verify.py
SHA-256 b8cc59ecb5fc2dffd21a49ce38da6519ca8564b26e1c130e32789b26d71762f0

barriers/hc7_surjective_five_colour_kempe_connectivity_barrier_census.cpp
SHA-256 59d9b9bfcfadb6360021fc5242752a26856380ce7ad7bb5e77121f7409679922
```

The final revision changes only the source status paragraph to link this
audit; the audited mathematics is unchanged.

## Mathematical audit

For `K_{2,6}`, properness makes the colour palettes of the two bipartition
sides disjoint.  A two-colour component meeting both sides is the entire
connected complete bipartite graph induced by those colours, so its swap
does not change the number of colours on the size-two side.  A two-colour
component lying on one side is a singleton.  Surjectivity forbids precisely
the singleton swaps that would remove one of the two singleton colours on
the size-two side.  Therefore equality of the colours on vertices `6,7` is
invariant.  Both modes occur.

An independent enumeration recovered all 18,600 labelled surjective proper
five-colourings and exactly two connected Kempe components, of orders 7,800
and 10,800.  The counts agree with

```text
5 * 4! S(6,4) = 7,800,
(5*4) * 3! S(6,3) = 10,800.
```

The displayed width-two tree decomposition proves `K_{2,6}` has no `K_5`
minor.  An independent nauty census of all 3,793 unlabelled order-eight
graphs with at most twelve edges found `G??F~w` as the unique disconnected
colouring graph.  This independently verifies minimum-edge uniqueness.  The
full retained census over all 12,346 order-eight graphs gives the stated 23
counterexamples and edge histogram.

For the strengthened graph

```text
H* = I_2 join (2K_2 disjoint union 2K_1),
```

independent graph6 decoding gives ``G?`F~w`` and the displayed edge set.
The same equality invariant remains valid: an opposite-side colour pair
still induces a connected complete bipartite graph, while moves involving
only forest-side colours do not change the twins.  Direct enumeration gives
11,040 states and exactly two Kempe components, each of order 5,520.  The
counts cross-check as `5*1104` and `20*276`, using the proper onto four- and
three-colourings of `2K_2` disjoint union `2K_1`.

The four displayed bags form a width-three decomposition.  Adding the leaf
bag `{d,0,4}` covers exactly the two new edges and preserves width three.
Independent graph6 decoding gives ``H?`F~yG`` for this extension.  Thus both
graphs are `K_5`-minor-free.

## Computational audit

The fixed verifier was run successfully and checks:

- both graph6 encodings and the exact edge sets;
- exact colouring-state counts and Kempe-component orders;
- constancy of the twin-equality invariant on every component; and
- the two stated tree decompositions.

The C++ census was compiled with a C++17 compiler and run on the complete
`geng -q 8` stream.  It returned exactly the output recorded in the source.
Its `K_5`-minor test exhausts every partition of every retained vertex subset
into five nonempty branch sets; it separately checks connectedness and all
ten branch-set adjacencies.  It also checks four-colourability independently.

## Scope

The conclusion is exactly a barrier to unconditional surjective Kempe-space
connectivity.  The strengthened example realizes the static boundary labels
listed in the source, but does not realize the full host hypotheses.  In
particular, the audit finds no claim about seven-connectivity,
contraction-criticality, full shores, `K_7`-minor exclusion, or preservation
of named minor-model branch sets.

No unresolved mathematical or computational issue was found.
