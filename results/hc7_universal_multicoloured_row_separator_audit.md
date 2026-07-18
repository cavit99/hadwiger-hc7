# Audit of the universal multicoloured-row separator theorem

**Verdict:** GREEN.

**Audited source:**
`results/hc7_universal_multicoloured_row_separator.md`

**Audited SHA-256:**
`9a62bd17005bcd327e77f4dcfdd636f83bb680ea8c173e1a607e545ff24a88f8`

The audit checked the theorem against the two independently audited inputs
`hc7_two_mark_branch_set_split.md` and
`hc7_five_row_separator_reflection.md`.

The mathematical revision was audited GREEN at SHA-256
`382f26d41caacd82dfa5b4f5e563ad22ec077480cb5f4a83190734b9deb092db`;
the current hash differs only in the status line recording that verdict.

In the first separation orientation, `Z` is anticomplete to `D`.  The old
`U`--`D` adjacency must therefore have its `U`-end in `W`, so `D union W`
is connected.  The old clique-model adjacencies make this merged set and
the four untouched sets pairwise adjacent, and spanningness gives

\[
 N_G(Z)\subseteq\{a\}\cup W\cup V_1\cup\cdots\cup V_4.
\]

If `Z` met all four `V_i`, the seven displayed sets would be a `K_7`
model.  Hence, in the non-`K_7` outcome, one row is disjoint from the
boundary.

In the second orientation, `Z` meets `D` and `W` misses some `V_j`.
Now `D union Z` is connected, the same old adjacencies give the five
pairwise adjacent rows, spanningness covers `N_G(W)-{a}`, and `V_j` is
the boundary-free row.  Thus simultaneous losses do not create a third
geometric case: merging `D` with the opposite donor part restores every
row--row adjacency needed by reflection.

In both orientations all five rows lie in the far closed shore minus
`a`, are disjoint and connected, are pairwise adjacent, and are adjacent
to `a`.  Therefore any far-shore six-colouring that is monochromatic on
every nonempty row intersection satisfies the audited five-row reflection
theorem and would six-colour the whole graph.  Universal multicolouring is
the exact negation.

## Trust boundary

- The theorem gives only `|N_G(L)|>=7`; it does not give an upper bound.
- Which row is multicoloured may depend on the colouring.
- In the second orientation the protected root of the split donor lies in
  the open side, so later root-faithful use requires a new argument.
- The theorem supplies five named connected rows, not one literal boundary
  root in every row.
- Nothing here proves that a multicoloured row can be split, nor does it
  prove `HC_7`.
