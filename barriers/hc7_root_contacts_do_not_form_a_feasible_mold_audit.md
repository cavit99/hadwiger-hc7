# Independent audit of the mold-feasibility barrier

**Verdict: GREEN.**

This audit checks
`hc7_root_contacts_do_not_form_a_feasible_mold.md` at SHA-256
`6863a1496768f9b18072d6b3ba0b5c65d8b2124b5afa925aa94a4bf8bd3f9a8a`.
It is an internal mathematical audit, not external peer review.

## Exact Section 9 definitions

Let `P=C_5\vee\overline{K_2}`, let `H=K_2\vee P`, and let `S=P` under the
identity homeomorphic embedding.  In the claimed encoding,

\[
                         \bigcup_{e\in F} Z_e=\{z_0,z_1\}.
\]

This equality is the proposed encoding of both root systems, not an axiom
imposed by Norin--Thomas.  It gives

\[
                         H-V(S\cup Z)=\varnothing.
\]

By the definition in Section 9, an `S\cup Z`-link is either one edge whose
ends already lie in `S\cup Z`, or is built from a connected subgraph of
`H-V(S\cup Z)`.  The second possibility is absent here.  Hence every link
`B_{ez}` containing a mold vertex `z` is one literal edge.

For `e=uv`, such an edge contains at most one of `u,v`.  The identity
segment `\eta(e)=uv` has no internal vertex.  Therefore `B_{ez}` neither
contains an internal vertex of `\eta(e)` nor contains both ends of
`\eta(e)`.  It violates both alternatives of feasibility axiom (iv).
Thus the proposed two-root mold is not feasible.  Axiom (iii) is not
needed for this contradiction.

## Scope checks

The base graph `P` is planar, internally four-connected and not the cube,
so the example does not evade Lemma (9.8) through a base-graph hypothesis.
Feasibility is genuinely the missing input.

The two additional limitations stated in the source are also correct:

1. a prescribed minor model need not supply a homeomorphic embedding of
   `P`; replacing it by a vertex expansion need not preserve internal
   four-connectivity; and
2. the clean conclusion (9.9) assumes a triangle-free planar base, whereas
   the pentagonal bipyramid is a triangulation.

The counterexample refutes only the inference from full root-to-column
adjacency to mold feasibility.  It does not refute a stronger theorem that
assumes the required internally disjoint links to designated subdivision
segments.

## Primary source

The checked definitions and lemmas are in S. Norin and R. Thomas,
*Non-planar extensions of subdivisions of planar graphs*, corrected
version [arXiv:1402.1999v3](https://arxiv.org/abs/1402.1999), Section 9,
especially the definition of feasibility and Lemmas (9.8)--(9.9).
