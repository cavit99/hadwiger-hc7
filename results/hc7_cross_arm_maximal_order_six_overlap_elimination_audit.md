# Independent cold audit: maximal order-six cross-arm overlap

**Verdict:** **GREEN.**

The seven six-subsets are enumerated without omission, the full-seven-point
lemma applies literally, and its small-support `K_6` lift has all required
connectivity hypotheses.

## 1. The seven-set identity

Assume `|A cap X|=5`.  Since `|X|=5`, this gives `X subset A`; as
`|A|=6`, write `A=X union {r}`.  The private pair is disjoint from `A`, so

\[
                         Y=A\cup\{p\}
\]

has exactly seven vertices.  Its seven vertex-deletion sets are:

* `Y-{p}=A`, the original support;
* `Y-{r}=X union {p}`, the `p`-arm; and
* `Y-{x}=(A-{x}) union {p}` for each of the five vertices `x in X`, the
  five forced replacements.

These are one plus one plus five distinct omissions, so every six-subset
of `Y` is covered exactly once.  Only the `p`-arm is needed.

## 2. Full-seven-point lemma

For each `v in Y`, the assertion that `Y-{v}` is a support means that the
induced six-vertex graph `G[Y-{v}]` has a spanning `K_5` model.  Thus
Lemma 4.2 of the cited result applies to `J=G[Y]` exactly as stated.

The lemma's complement proof is sound.  A spanning six-vertex `K_5` model
makes the complement a union of at most two nontrivial star components.
If a component of the seven-vertex complement were not a star, a triangle
or three-edge path on at most four vertices would survive deletion of one
of the other three vertices.  Three nontrivial components retain one edge
from each after deleting the unused seventh vertex.  Hence the complement
itself has at most two nontrivial stars, and each of its remaining cases
constructs the claimed spanning `K_6` model.  The exceptional spanning
star `K_{1,6}` is correctly excluded because deleting a leaf leaves the
complement `K_{1,5}`, whose original graph is `K_5` plus an isolated
vertex and has no spanning `K_5` model.

Therefore `G[Y]` has a `K_6` model supported on seven vertices.

## 3. Seven-connectivity lift

Lemma 4.3 also applies literally.  A seven-connected graph has at least
eight vertices, so `G-Y` is nonempty.  For any component `C` of `G-Y`, its
neighbourhood lies in the seven-set `Y`.  If it omitted a vertex of `Y`,
its neighbourhood would have order at most six and would separate `C`
from that omitted vertex, contradicting seven-connectivity.  Thus
`N(C)=Y`; the connected set `C` contacts every bag of the `K_6` model and
is a seventh branch bag.

This produces a literal `K_7` model and contradicts the theorem's host
hypothesis.  Hence `|A cap X|<=4`.

## 4. Trust boundary

The proof does not require irredundancy, contraction-criticality, the
`q`-arm, or a choice of split rows.  It uses only the exact support family,
seven-connectivity, and `K_7`-minor-freeness.  It eliminates only the case
`|X|=5` and `|A cap X|=5`; smaller overlaps and the order-four arm core are
not covered by this theorem.
