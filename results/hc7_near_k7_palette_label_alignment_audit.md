# Audit: palette-to-label alignment in the bipartite singleton shell

## Verdict

**GREEN in the spanning singleton-shell scope.**  It cannot be invoked for
arbitrary complex foreign bags.

## Checks

1. After contracting the bipartite bag, the contraction vertex and the
   singleton clique form a literal `K_{k-1}`.  Giving the apex the colour of
   a non-neighbour singleton is an explicit proper quotient colouring.
2. The bilateral split therefore contacts every nonshadow colour at its
   unique singleton vertex; only the colour shared by the apex and its
   non-neighbour remains ambiguous.
3. The same-side list argument is valid because each bipartition class is
   independent.  It produces distinct witnesses: coincidence for two
   deficient labels would make the common witness universal.
4. The proposed branch sets `C={v} union X`, `R=B-X`, and the singleton
   bags are disjoint, connected, and pairwise adjacent whenever `R` is
   connected and retains every portal class.
5. Thus target-minor exclusion forces exactly a small deletion separating
   `B` or a whole portal class contained in the witness set.  The stated
   connectivity/portal threshold eliminates both.

The hypothesis now explicitly says that the induced graph on the complex
bag is bipartite.  No claim is made that an arbitrary `K_7^vee` model can
be normalized to this shell.
