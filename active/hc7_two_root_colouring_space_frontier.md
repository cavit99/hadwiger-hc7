# Critical completion of a singleton-root `K_7`-minus-one-edge model

**Status:** frozen conditional theorem programme; this file is not part of
the current authoritative proof spine. The main completion theorem is
conjectural. The inputs explicitly identified as proved have written proofs
and separate internal audits. Nothing here proves `HC_7`.

## 1. Clean target

A graph is **strongly seven-contraction-critical** if it is
seven-chromatic and every proper minor is six-colourable.

### Singleton-root completion-or-separation theorem

Let `G` be seven-connected and strongly seven-contraction-critical. Suppose
`G` has a spanning `K_7`-minus-one-edge minor model in which the two branch
sets incident with the missing edge are nonadjacent singleton vertices
`a,b`. Then `G` contains a `K_7` minor or has an actual separation of order
seven.

This is the clean target of this frozen programme. It is narrower than
`HC_7`: it assumes a
spanning near-complete model with two already specified singleton branch
sets, and it permits a separation outcome. It would eliminate the
unbounded no-order-seven branch of this near-`K_7` programme.

Write `J=G-{a,b}`. The remaining branch sets

`B_1,...,B_5`

partition `V(J)`, are connected and pairwise adjacent, and each is adjacent
to both roots. Since `a,b` are nonadjacent, a five-colouring of `J` would
extend by one common new colour on `a,b`; hence `chi(J)=6`.

## 2. Proved global inputs

### Two-root colouring cover

For a proper six-colouring `c` of `J`, let

- `A(c)` mean that `N_J(a)` meets every colour class; and
- `B(c)` mean that `N_J(b)` meets every colour class.

Strong contraction-criticality implies that every six-colouring of `J`
satisfies `A(c)` or `B(c)`, and that both exclusive possibilities occur.
A direct Kempe interchange from an `A`-only colouring to a `B`-only
colouring has a bichromatic component with a separating neighbourhood. At
the sharp boundary size this is an actual order-seven separation.

The whole cover is essential. Selected opposite colourings, selected Kempe
paths, or one fixed minor model do not force completion.

### Dominating-model regeneration

Every two-vertex deletion of `G` has chromatic number at least five and
therefore contains a dominating `K_5` model by the Dominating 4-Colour
Theorem. A pair whose deletion has no such model is therefore a terminal
contradiction.

The ordered-clique strengthening of that theorem yields the following new
uniform input. If `H` has chromatic number at least `r+4` and `X` is a
connected induced `r`-colourable subgraph, then a normalized dominating
`K_5` model either contains all of `X` in its first branch set or its final
four branch sets separate `X` from the first branch set. A marked version
can avoid `X` together with any prescribed neighbour of `X`. A two-subgraph
version aligns `X_1` with the first branch and `X_2` with the first or
second branch when every vertex of `X_2` has a neighbour in `X_1`.

Applied to `J`, the internal vertices of every shortest `a`--`b` path
through a named `B_i` are therefore either retained intact in the first
branch set of a dominating `K_5` model or yield a separator

`S=T_2 union T_3 union {v,w}`,

where `T_3 union {v,w}` is an induced cycle, `T_1` dominates every vertex
of `S`, and `T_2` dominates the cycle. Let `E` be the `T_1`-side component
of `J-S`, and let `R_E` be the subset of `{a,b}` having a neighbour in
`E`. Then `S union R_E` separates `G`, so

`omega(S,E)=|S|+|R_E|>=7`.

Equality is an actual order-seven separation. This weighted boundary order,
not `|S|` alone, is the correct rank.

This is the first general, label-aware rooted-model principle among this
programme's proved inputs. Its exact proof and scope are in the adjacent
result and audit.

### Complete-factor join theorem

For every `r>=0`, if `K_r join F` is `(r+5)`-connected, then it contains a
`K_{r+5}` minor or has an actual separation of order `r+5`. Moreover, every
`K_{r+5}`-minor-free graph of this join form is `(r+4)`-colourable. This
eliminates the coherent complete-factor join family uniformly and shows
that the familiar `K_2`-plus-planar obstruction belongs exactly at the
order-seven separation threshold.

## 3. Decisive falsifications

The following proposed shortcuts are closed.

1. **Connectivity plus a near-complete model.** Ordinary linkage does not
   preserve the five named branch sets. No static theorem of the form used
   here has been proved, and the standard seven-connected complete-factor
   joins show the sharp lower-connectivity obstruction.
2. **Kempe connectivity.** The two exclusive root orientations can occupy
   different Kempe classes even with the common host, a spanning
   root-adjacent `K_5` model, and all root-edge contraction probes.
3. **Commuting transitions.** Two independent-looking interchanges may have
   status square `A,AB,AB,B`; no colouring satisfying neither root condition
   follows.
4. **Model-local monotonicity.** Exact branch-set rotations can be
   involutions, so branch-set size or attachment count alone is not a well-founded
   rank.
5. **Edge saturation.** Maximizing a `K_7`-minor-free supergraph and adding
   a nonedge merely repackages the unresolved high-connectivity clique-minor
   assertion; it does not preserve singleton branch labels.
6. **Abstract boundary languages.** Extension languages can be arbitrarily
   flexible under rooted-minor exclusion, so equality partitions without
   host-level branch-set data are insufficient.

These are guardrails, not evidence against the clean target. Each example
misses either strong contraction-criticality or one of the target terminal
exclusions.

## 4. Current constructive problem

The new absorption-or-separator theorem leaves exactly two branches.

### Branch A: aligned path

A prescribed induced internal root-to-root path `X` lies in the first branch set `T_1` of
a dominating `K_5` model. The missing operation is a label-preserving
exchange between this ordered model and the pre-existing five bags
`B_1,...,B_5`. It must split connected branch sets without identifying the
two roots and must preserve every adjacency used in the resulting minor
model.

### Branch B: normalized separator

The final four branch sets form

`S=T_2 union C`,

where `C` is an induced cycle, `T_1` dominates `S`, `T_2` dominates `C`,
and `S` separates `X` from `T_1` in `J`. With `E,R_E` as above,
`omega(S,E)=7` finishes the clean target by an actual order-seven
separation. This includes the three sharp possibilities
`(|S|,|R_E|)=(5,2),(6,1),(7,0)`. Neither normalization nor minimum model
size bounds `|S|`: five-chromatic graphs of large girth rule out that
shortcut.

The complete-factor icosahedral join realizes the sharp `(7,0)` case with
all the static normalized-model data and a spanning singleton-root
near-`K_7` model. It is six-colourable and fails the universal two-root
colouring cover. Thus the weighted terminal is sharp, and every strict
compression step must use contraction-critical colouring data.

### Frozen conjectural compression target

The following is a conjectural compression target, not a proved transition.
In particular, the displayed tuple becomes a usable rank only after a new
outcome in the original graph has been constructed with the same roots and
prescribed path. The
[root-contraction rank barrier](../barriers/hc7_normalized_root_contraction_rank_barrier.md)
shows that contracting a root--`E` edge does not automatically preserve the
comparison class or decrease any coordinate.

**High-connectivity compression of a normalized dominating-model
separator.** In the clean target setup, let `X` be the internal vertices of
one of the five shortest root-to-root paths and choose an
absorption-or-separator outcome minimizing

`(omega(S,E), |E|, |C_X|)`,

where `C_X` is the component of `J-S` containing `X`. Then either

1. `G` contains a `K_7` minor;
2. `omega(S,E)=7`, hence `S union R_E` is an actual order-seven separator;
   or
3. a proper-minor colouring transition gives another normalized outcome
   with a strictly smaller displayed signature.

When `R_E` is nonempty, a six-colouring after contracting an edge from a
root in `R_E` into `E` is only response data. A proof still needs a
response-to-regeneration lemma producing a comparable normalized outcome
in the original graph; lifting the colouring alone is insufficient.
When `R_E` is empty, `S` already separates `G`; the task is to compress that
larger separator or glue proper-minor colourings across it.

The theorem must use both the old labelled frame and the ordered domination
inside `S`. Seven-connectivity alone is not enough, and merely restating a
generic branch-set splitter is not progress. A proof must exhibit the
branch sets, the separator, or the strict replacement explicitly.

This mechanism is frozen after the contraction transition failed its impact
gate. The older support-six and web programmes remain frozen unless they
supply an explicit construction needed in one of these two branches.

## 5. Trust boundary

Proved and separately audited:

- the two-root common host and universal colouring cover;
- opposite root orientations and the direct-transition separator;
- rooted Kempe paths/fans from contraction witnesses;
- dominating `K_5` regeneration after deleting two vertices;
- low-colour subgraph alignment or normalized separation; and
- the complete-factor join dichotomy and colouring corollary.

Open:

- high-connectivity compression of the normalized separator;
- label-preserving composition in the aligned-path branch; and
- the full singleton-root completion-or-separation theorem.

The canonical rooted-web route does not settle these obligations. Web
completion edges need not be host edges, and explicit finite quotients show
that a localized facial attachment may coexist with the two forced
linkages while the repairing linkage remains absent. Further progress must
use contraction-criticality in the host.

## 6. Primary external inputs

- Girão et al., *The Dominating 4-Colour Theorem*, Lemmas 2.1 and 2.2
  ([arXiv:2605.10112](https://arxiv.org/abs/2605.10112)).
- Norin--Totschnig, every non-six-colourable graph contains a
  `K_7^vee` minor ([arXiv:2507.03244](https://arxiv.org/abs/2507.03244)).
- Las Vergnas--Meyniel, Kempe equivalence for five-colourings of
  `K_5`-minor-free graphs. Broad extensions are false and are not assumed.
- Dvořák--Swart, flexibility of boundary colouring-extension languages
  under rooted-minor exclusion
  ([arXiv:2504.07764](https://arxiv.org/abs/2504.07764)).
