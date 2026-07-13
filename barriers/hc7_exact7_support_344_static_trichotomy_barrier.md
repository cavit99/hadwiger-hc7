# Barrier: the support-`(3,4,4)` static trichotomy is false

Let the seven-vertex boundary graph have exactly the two disjoint edges

\[
                              06,\qquad45
\]

and assign the three-palette contact masks

\[
        (1,3,6,6,4,4,3),
\]

that is,

\[
 \{1\},\{1,2\},\{2,3\},\{2,3\},
 \{3\},\{3\},\{1,2\}.
\]

The palette supports are exactly `(3,4,4)`.  The state is uncolourable
because the literal edge `45` joins two vertices forced to colour `3`.
Nevertheless the boundary plus carrier triangle has no anchored `K_4`.
Nor does any boundary clique `Q` of order at most two meet every edge: a
clique can cover at most one of the two disjoint edges, so `S-Q` is never
independent.

The exact checks are reproduced by the functions in
`../active/hc7_exact7_raw_list_no_k4_verify.py`:

```text
supports=[3,4,4]
uncolourable=True
anchored_K4=False
clique_vertex_cover_of_order_at_most_two=False
```

Thus the promoted support-four boundary trichotomy cannot be weakened
statically to one carrier of support three.  The residual `4/3/4` and
`3/3/4` cells require geometry, minor-critical transitions, or adaptive
packet reflection.  This counterexample is a guardrail, not evidence
against the adaptive `(1,3)` theorem.
