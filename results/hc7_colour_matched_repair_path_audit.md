# Audit of the colour-matched deficient-branch-set path lemma

**Verdict:** GREEN (separate internal audit)

**Audited theorem revision:** SHA-256
`ff04ccf580a4ebe8b0f2d3be3e8710d48cfae5717d3f91eb48a118148ba90efc`
of `hc7_colour_matched_repair_path.md`.

## Checks performed

The proof was checked against the audited star--Kempe compression theorem
and deficient-component separator theorem.  Those hypotheses supply the
proper six-colouring, the four-coloured residue, colourfulness of `T`, the
connectivity of every induced graph `H[A union V_gamma]`, the
contact-maximal rooted `K_4` model, the exact boundary identity, and
seven-connectivity of the 7-contraction-critical host.

For an oriented `s`--`t` path, the first vertex `t'` in `T` and the last
preceding vertex `c` in `C_j` exist.  The subpath `cWt'` contains exactly
one vertex of `C_j` and exactly one vertex of `T`.  Consequently its
portion outside `C_j`, together with `u`, is connected, disjoint from
`C_j`, and adjacent to `C_j`.

The three contact sets in the other rooted branch sets and the contact
set in `X` are nonempty and pairwise disjoint.  The displayed boundary
cardinality is exact.  Seven-connectivity, followed by exclusion of an
order-seven separation, gives boundary order at least eight and hence
three contacts in excess of the one-per-class baseline.  In the
unique-deficiency case, the seven named sets form a `K_7`-minus-one-edge
minor model with precisely the asserted missing adjacency.

## Scope

The result proves the existence of the colour-matched path, the connected
repaired set containing `u`, and the exact expanded-boundary count.  It
does **not** prove that the path can be incorporated while retaining the
other branch sets.  It therefore does not by itself yield a `K_7` minor,
an order-seven separation, or `HC_7`.

No unresolved assumption or proof gap remains within this stated scope.
