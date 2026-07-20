# Full root-to-column contact does not imply mold feasibility

**Status:** written barrier/counterexample to a proposed application of
Norin--Thomas Lemma (9.8); separately audited **GREEN** in
[`hc7_root_contacts_do_not_form_a_feasible_mold_audit.md`](hc7_root_contacts_do_not_form_a_feasible_mold_audit.md).

## Statement refuted

The following implication is false, even when the prescribed
pentagonal-bipyramid model is a subgraph rather than merely a minor.

> If two adjacent vertices are each adjacent to every branch set of a
> prescribed pentagonal-bipyramid model, then their attachment systems can
> be encoded as a nonempty mold feasible for the corresponding homeomorphic
> embedding in the sense of Norin--Thomas Section 9.

## Construction

Let

\[
                         P=C_5\vee\overline{K_2}
\]

and let `H=K_2\vee P`.  Write the two vertices of the `K_2` as `z_0,z_1`
and take the identity homeomorphic embedding

\[
                         \eta:P\hookrightarrow S=P\subseteq H.
\]

The seven singleton vertices of `P` are a prescribed model of `P` in `H`.
The roots `z_0,z_1` are adjacent to one another and each is adjacent to
every one of those seven branch sets.

## Failure of feasibility

Suppose a mold `Z=(Z_e:e\in F)` encodes both root systems, so that

\[
                         \bigcup_{e\in F}Z_e=\{z_0,z_1\},
\]

and each root occurs in at least one mold set.  Choose `e=uv\in F` and
`z\in Z_e`.  In this construction

\[
                       H-V(S\cup\{z_0,z_1\})=\varnothing.
\]

Consequently every `S\cup Z`-link containing `z` is a single literal edge
whose two ends already lie in `S\cup Z`.  A candidate link `B_{ez}` can be
`zu` or `zv`, can end at some vertex unrelated to `e`, or can be the edge
between the two roots.

The path `\eta(e)` is the one-edge path `uv`, so it has no internal vertex.
The link contains at most one of its ends.  It therefore satisfies neither
alternative in feasibility axiom (iv) of Norin--Thomas:

1. it has no attachment in the interior of `\eta(e)`; and
2. it does not contain both ends of `\eta(e)`.

Thus no such nonempty mold is feasible for `\eta`, despite the complete
root-to-column contact.

## Consequence for the mold route

Lemma (9.8) assumes feasibility; it does not derive it from ordinary
adjacency to branch sets.  In the current HC7 configuration, feasibility
would require substantially stronger literal data: for every selected
mold edge and root, a link must reach the interior of the corresponding
subdivision segment (or one common link must reach both segment ends), and
links belonging to distinct mold edges must be internally disjoint outside
the subdivision and the mold vertices.

There is an earlier issue for a general column model.  Such a model gives a
minor, hence a topological model of an expansion of `P`, but need not give a
homeomorphic embedding of `P` itself.  Taking the expansion as the base
graph need not preserve the internal four-connectivity required by Lemma
(9.8).

Even after those two hypotheses were supplied, the clean minor conclusion
(9.9) is not directly available: it assumes that the planar base graph is
triangle-free, whereas every face of `P` is a triangle.  This barrier does
not show that mold methods are useless; it identifies the first missing
model-relative routing theorem needed before they can be invoked.

## Source

The definitions of mold, cast and feasibility, and Lemma (9.8), are in

> S. Norin and R. Thomas, *Non-planar extensions of subdivisions of planar
> graphs*, Journal of Combinatorial Theory, Series B **121** (2016),
> 326--366; corrected version [arXiv:1402.1999v3](https://arxiv.org/abs/1402.1999),
> Section 9.
