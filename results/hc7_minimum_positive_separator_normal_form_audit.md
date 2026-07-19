# Independent internal audit of the minimum positive-separator normal form

**Verdict:** GREEN for the exact source revision

```text
4b6a4d7a434cb255229fcf4fe12e1393d7b0dadad27985e8528b0535d4cf64ba
```

of
[`hc7_minimum_positive_separator_normal_form.md`](hc7_minimum_positive_separator_normal_form.md).
This is a separate internal audit, not external peer review.

## 1. Scope checked

The audit checked the eligibility and minimum-boundary argument, all
component contractions and expansions, the `K_{7-r}` lift, both component
count exclusions, the Moore-bound inequalities, the boundary-colouring
gluing, and the operation-specific response corollary.

## 2. Findings

Every component of `G-X` has its full neighbourhood contained in `X` and
has another component on the opposite side.  Seven-connectivity gives
order at least seven.  Order seven supplies the stated generic response;
otherwise minimum positive boundary order forces equality with `X`.

For `r` full components and `r` distinct boundary vertices, the sets
`C_i union {x_i}` are connected, disjoint, pairwise adjacent, and complete
to `X-F` after contraction.  Six-colourability of the proper minor and
`K_7`-minor exclusion give both conclusions of Lemma 3.1.

With at least five components, deleting arbitrary five-sets leaves an
independent graph.  Since `|X|>=8`, this makes all of `X` independent, and
the one-block closed-side colourings glue.  With four components, every
four-vertex deletion leaves a forest, so every cycle has length at least
`|X|-3`.  A vertex-minimal non-three-colourable subgraph has minimum degree
at least three.  The two displayed Moore bounds are strictly greater than
`g+3=|X|` for every `g>=5`, proving three-colourability.  Contracting three
other full components together with the nonempty independent colour
classes reproduces the same boundary partition on each closed side; the
palette permutations and gluing are valid.

Finally, an edge-deletion colouring is proper on every unchanged component
side.  If the same equality partition extended through the intact operated
side, a palette permutation would make the assignments agree literally and
would six-colour `G`.

## 3. Trust boundary

The theorem does not force the minimum positive boundary to have order
eight, make an order-seven component smaller than an earlier selected
shore, preserve inherited model labels, or synchronize the remaining two-
or three-component response languages.  No unresolved assumption remains
in the stated result.
