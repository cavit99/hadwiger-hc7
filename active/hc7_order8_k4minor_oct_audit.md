# Independent audit: order-eight `K_4`-minor/OCT certificate

**Verdict:** **GREEN** for the exact computer-assisted finite assertion and
certificate package at the revisions below:

> Every simple graph on eight vertices either has an odd-cycle transversal
> of order at most two or contains a `K_4` minor.

Equivalently, every eight-vertex `K_4`-minor-free graph has an odd-cycle
transversal of order at most two.  This is a separate internal cold audit,
not external peer review and not an unbounded theorem.

## Exact revisions audited

```text
4b6eda8c37fb6a8793b65e38d0031a797b8bc9da13d4a6a3bf068fffd9cf7d5b  active/hc7_order8_k4minor_oct_certificate.py
be6ef8ef9746befe2600c47293f5a122748a85f3df978b6a8a914bd54d301cd1  active/hc7_order8_k4minor_oct_check.py
```

Any change to the construction, catalogue handling, certificate format,
expected counts, or expected digest requires renewed audit.

## Reproduction

Using nauty `2.9.3`, I ran:

```text
python3 active/hc7_order8_k4minor_oct_certificate.py
python3 active/hc7_order8_k4minor_oct_check.py
```

The generator and checker independently returned:

```text
graphs 12346
oct_witnesses 8876
k4_witnesses 3470
records_sha256 a15a855eb45886eccac037642266ff47532f490301fc6fff9a495b07f923912e
PASS
```

The generated certificate has `12,346` records, plus three header lines,
and occupies `200,764` bytes when the generator is given `--output`.  The
checker accepts that explicit path or, with no argument, invokes the pinned
generator in a temporary directory before independently checking its
output.  As elementary positive controls, the empty graph receives the
empty OCT witness and `K_8` receives four singleton branch sets.

## Generator audit

Nauty's `geng -q 8` returns `12,346` graph6 records, the known complete set
of isomorphism representatives of simple graphs on eight vertices.  The
generator rejects a catalogue with the wrong count or duplicate codes and
sorts the codes before producing the digest.

For each representative, the OCT search checks all

```text
C(8,0) + C(8,1) + C(8,2) = 37
```

possible deletion sets and directly tests the remaining graph for
bipartiteness.  If none works, the `K_4`-minor search enumerates every
nonempty vertex subset, retains exactly the connected subsets, and tests
every increasing four-tuple of those subsets for disjointness and all six
pairwise adjacencies.  Sorting any four branch sets by their bit masks puts
them into one such increasing tuple, so this exhausts all four-branch-set
minor models on the eight vertices.

The `8,876` and `3,470` counts describe the generator's ordered
classification: it records an OCT whenever one exists and searches for a
`K_4` model only otherwise.  They are not counts of two disjoint graph
properties; an OCT-labelled graph may also contain a `K_4` minor.

## Independent-checker audit

The checker imports no generator code and performs no witness search.  Its
no-argument wrapper uses the generator only to materialize a temporary
certificate; validation remains separately implemented.  It:

1. obtains its own order-eight catalogue from `geng`;
2. decodes each graph6 record independently as an edge set;
3. requires the certificate codes to equal that catalogue exactly, with no
   missing, unknown, or repeated representative;
4. directly checks the size and bipartiteness claim of every OCT witness;
5. directly checks nonemptiness, disjointness, connectedness, and all six
   adjacencies of every `K_4` model; and
6. verifies the record counts and canonical payload digest.

I also checked the two graph6 decoders on sample catalogues with
`0,1,7,14`, and `28` edges; both returned the edge count requested from
`geng`.

Thus a certificate cannot pass merely because the generator selected a
witness: the separately implemented checker validates every recorded
witness against its own decoded graph.

## Trust boundary

Catalogue completeness is delegated to nauty's `geng`; the checker uses
the same external catalogue source and is independent at the decoding and
witness-validation layers, not a second unlabeled-graph generator.  The
hard-coded count and digest provide reproducibility but are not themselves
the mathematical proof; exact catalogue coverage and direct witness checks
are.

The finite result concerns only graphs of order eight.  In combination with
the separately audited two-vertex-shore contraction lemma, it excludes the
full/full `K_4`-minor-free boundary configuration stated there.  It says
nothing by itself about near-full endpoint orientations, operation
provenance, host connectivity, `K_7`-minor exclusion, rooted models in the
host, or strict exact-seven descent.
