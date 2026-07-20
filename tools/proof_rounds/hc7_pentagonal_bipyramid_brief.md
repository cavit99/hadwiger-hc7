# Frozen proof brief: paired-rooted pentagonal-bipyramid theorem

## Target

Let `F` be a five-connected graph with a vertex partition

\[
V(F)=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_7,
\]

where every `C_i` is nonempty and connected and the contact graph of the
seven parts is exactly the pentagonal bipyramid
`C_5\vee\overline{K_2}`. Let `A,B\subseteq V(F)`, and suppose every
`F[C_i]` contains an `A`--`B` path. Prove that at least one of the following
holds:

1. `F` is four-colourable;
2. `F` contains five pairwise disjoint, connected, pairwise adjacent
   subgraphs `M_1,...,M_5`, with every `M_i` meeting both `A` and `B`.

This is Conjectural Theorem 3.1 in the frozen technical frontier. It is not
Hadwiger's Conjecture and is not currently proved in the repository.

## Why this target matters

In the audited host construction, the five subgraphs in outcome 2, together
with two fixed adjacent connected root subgraphs, form a `K_7`-minor model.
Outcome 1 gives a six-colouring of the host. Thus the theorem eliminates the
whole five-connected pentagonal-bipyramid branch, but it says nothing about
the other exact-seven, order-eight, or order-nine interfaces.

## Trusted inputs

Only the exact statements and hypotheses in the frozen context may be used.
Important proved inputs include:

- the spanning pentagonal-bipyramid core and seven-column contact structure;
- the spanning two-sided five-part normalization;
- the one-defect two-root completion-or-separation theorem;
- alternating-split, adjacent-rim-linkage, and two-column-absorption
  constructions;
- tree, single-contact, and four-connected-column planar/minor dichotomies;
- the finite type-5 endpoint and one-defect classifications.

Finite classifications are evidence and local inputs only. They are not an
unbounded proof.

## Known barriers and proof guidance

- An unrooted `K_5` subdivision does not align its branch sets with `A,B`.
- Abstract enlargement minors do not preserve the two literal root sets.
- Root-to-column adjacency does not supply the feasible cast required by
  mold theory.
- Static boundary-colouring languages alone can be too flexible.
- Persistent conforming planar reroutings should be assembled into the
  four-colourable alternative rather than treated indefinitely as failures.

Seymour's colour-extension-cutset perspective may be used as a mechanism:
failure of the paired-rooted model may force a one-way inclusion between
colour-extension families. Such a step counts only if the inclusion is
universal for the stated family and is explicitly shown to yield a
four-colouring or a strictly smaller instance satisfying the same theorem.

## Allowed outcomes

Return exactly one of:

1. `proof`: a complete proof of the target;
2. `counterexample`: an explicit graph and sets satisfying every target
   hypothesis, together with certificates of five-connectivity,
   non-four-colourability, and absence of the paired-rooted `K_5` model;
3. `strict_reduction`: a proved unbounded theorem with a well-founded
   host-level parameter, a proved strict decrease, and an explicit induction
   back to the target;
4. `no_result`: an honest first unresolved inference.

## What does not count

- another finite census without an unbounded reduction;
- an unlabelled or quotient-only clique minor;
- a model in which even one branch set lacks literal contact with `A` or `B`;
- a selected colouring presented as universal colour extension;
- a new theorem-strength lemma without its proof;
- a rerouting that can cycle or lacks a declared decreasing parameter;
- a reduction that merely renames the paired-rooted conclusion.

Every citation must identify the exact frozen source and statement used.
Every contraction or absorption must retain disjointness, connectedness, and
the five pairwise adjacencies. If no allowed outcome is complete, return
`no_result` rather than optimism.
