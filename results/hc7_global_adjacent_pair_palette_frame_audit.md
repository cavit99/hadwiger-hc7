# Independent audit: global adjacent-pair palette frame

**Audited source:** `hc7_global_adjacent_pair_palette_frame.md`
**SHA-256:** `ec80047b58639f3d2357e5cf6ba06d9ba8b25b92c2530de098f216201b521463`
**Verdict:** **GREEN.**

**Promoted source SHA-256:**
`e4f99a43d6f45d3c1e7d93bbf854185e0009ecdc143c733d25449c2956aead98`.
The only change is the status-line update recorded in the revision note.

The stated reduction is correct.  Every hypothetical minor-minimal
counterexample satisfying the source hypotheses has at least one adjacent
pair whose deletion leaves a six-chromatic graph, and that graph admits a
spanning `K_6`-minor model.  The separately audited adjacent-pair palette
theorem therefore applies.  The conclusion is uniform but label-free: it
does not select a previously designated edge or align the resulting model
with a pre-existing balanced boundary or near-`K_7` model.

## 1. Primary double-critical input

The citation and theorem number are exact.  Kawarabayashi, Pedersen and
Toft define a connected `k`-chromatic graph to be double-critical when
`G-{u,v}` is `(k-2)`-colourable for every edge `uv`.  Their Theorem 7.1
states that every double-critical seven-chromatic graph contains a `K_7`
minor:

K. Kawarabayashi, A. S. Pedersen and B. Toft,
[*Double-critical graphs and complete minors*](https://doi.org/10.37236/359),
Electronic Journal of Combinatorics 17 (2010), R87, Theorem 7.1.

The graph in the source is seven-connected and hence connected.  If
`G-{u,v}` were five-colourable for every edge `uv`, then `G` would be
double-critical, and Theorem 7.1 would contradict the exclusion of a
`K_7` minor.  Thus some edge `zu` satisfies

\[
                       \chi(G-\{z,u\})>5.
\]

This use of the published theorem is valid for both complete and
non-complete double-critical graphs: the complete case is immediate and is
included explicitly in the proof of Theorem 7.1.

## 2. Exact chromatic number after deleting the pair

Put `H=G-{z,u}`.  The graph `G-z` is a proper minor and is therefore
six-colourable by hypothesis.  Restricting such a colouring to `H` gives
`chi(H)<=6`.  Combined with the selected inequality `chi(H)>5`, this proves

\[
                              \chi(H)=6.
\]

Equivalently, one may note that deleting two adjacent vertices from a
seven-chromatic graph can lower the chromatic number by at most two, but
that lower bound is not needed in the source proof.

## 3. Spanning `K_6` model

The established case `HC_6` implies that every six-chromatic graph contains
a `K_6` minor, so `H` has a `K_6`-minor model.  Deleting two vertices from a
seven-connected graph leaves a five-connected graph; in particular, `H`
is connected.

The spanning-extension argument is correct.  The union of the six branch
sets is connected because every two branch sets are adjacent.  While an
unused vertex remains, connectedness supplies an edge from the current
union to an unused vertex.  Adding that vertex to the incident branch set
preserves its connectivity, disjointness from the other branch sets, and
all existing inter-branch-set adjacencies.  Iteration produces a spanning
model.

Only connectedness of `H`, rather than full five-connectivity, is needed
for this extension.  Five-connectivity is used later by the palette theorem
to obtain five simultaneous disjoint paths.

## 4. Application of the palette theorem

For the selected edge `zu`, all hypotheses of
`results/hc7_adjacent_pair_palette_linkage.md` are present:

- `G` is seven-connected and seven-chromatic;
- every proper minor, including the edge deletion `G-zu`, is
  six-colourable;
- `chi(G-{z,u})=6`; and
- `H` has a spanning `K_6`-minor model.

Its Lemma 2.1 therefore gives the common pole colour, its occurrence in
`H`, its absence from both pole neighbourhoods, and saturation of the five
other colours at both poles.  Its Theorem 3.1 gives the five disjoint paths
whose endpoint colours are paired by a permutation.  Since the spanning
model was arbitrary, its contact-profile conclusions apply relative to
every spanning `K_6` model in `H`, subject to the explicit contact-count and
separator hypotheses in Theorem 4.1 and Corollary 5.1.

## 5. Scope and trust boundary

The reduction is genuinely uniform over the class stated in the theorem,
but it is not label-preserving.  It proves the existence of **some**
non-double-critical edge and allows the choice of **some** spanning
`K_6`-minor model after deleting its endpoints.  It does not prove that a
specified outer edge from the balanced order-eight configuration is
eligible, nor that the six colour classes align with the branch sets of a
previously fixed model.

Accordingly, the source may be cited as a global entry point for the
adjacent-pair palette linkage.  It may not be cited as a common boundary
colouring, a colour-preserving linkage, a bounded separator, a
label-preserving exchange between two `K_6` models, or a proof of `HC_7`.

## 6. Hypothesis economy

Seven-connectivity is stronger than necessary for selecting the edge and
for making the `K_6` model spanning, but it is an actual hypothesis of the
downstream palette-permutation theorem.  Likewise, requiring every proper
minor to be six-colourable is stronger than the bare double-critical
contrapositive needs; it also supplies the six-colouring of `G-zu` required
by the palette theorem.  No missing hypothesis or invalid implication was
found.

## Revision note

The audited source had SHA-256
`ec80047b58639f3d2357e5cf6ba06d9ba8b25b92c2530de098f216201b521463`.
Promotion changed only its status line from “independent audit pending” to
“separately audited”; every mathematical statement and proof is otherwise
unchanged from the audited revision.
