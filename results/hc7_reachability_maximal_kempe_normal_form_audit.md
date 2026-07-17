# Independent audit: reachability-maximal Kempe normal form

**Audited file:** `results/hc7_reachability_maximal_kempe_normal_form.md`
**SHA-256:** `90ad2acb2e74e41f8f5fdac85755df8403b70870738c5946fefbe2619ce0f4fe`
**Verdict:** **GREEN.** Theorem 2.1, Corollary 2.2, and the balanced
order-eight specialization are correct as stated. No mathematical change
to the audited source is required.

This is an independent internal mathematical audit, not external peer
review. It uses the already audited generalized two-deleted-edge Kempe fork
at exact source hash
`880b9d30946357b1df0540543b5ffe1d38def7f68224577ebe476e4bed9a6370`.

## Promotion recheck

The promoted source differs from the audited draft only in its status and
adjacent-audit link. Reversing those metadata edits reproduces the original
audited SHA-256
`52912e5c63f81c89dfaccfeb1c968e813b9e86096c075dcf0129f745c4b73336`.
No theorem hypothesis, conclusion, proof step, or trust-boundary statement
changed, so the GREEN verdict transfers to the promoted hash above.

## 1. Admissible colouring family

The family `mathcal E` is finite and nonempty by hypothesis, so a colouring
maximizing `|F_kappa|` exists. Because `sigma` permutes `Omega`, rotating an
`Omega`-coloured reachable set does not change which vertices belong to the
induced three-colour graph. The prescribed colouring of `R` is fixed because
none of its colours belongs to `Omega`.

For three colours, every edge of the proper induced `Omega`-coloured graph
has ends with two different colours. Exactly one of those colours is the
`sigma`-successor of the other, so the draft correctly orients every such
edge in exactly one direction.

## 2. Theorem 2.1

The reachable-set recolouring is proper on `H` by Theorem 2.1 of the audited
generalized fork. The three cases used in the new theorem are exhaustive:

1. If `b` is not reachable, exactly one end of `e` is rotated. The resulting
   colouring makes `e` proper. Non-`q`-colourability of `G` forces `f` to
   remain monochromatic, giving outcome 1.
2. If `b` is reachable, both ends of `e` are rotated from their common
   colour by the same permutation and remain monochromatic. If the ends of
   `f` become different, `f` can be restored and outcome 2 follows.
3. If both deleted edges remain monochromatic, the rotated colouring still
   lies in `mathcal E`: its restriction to `R` is unchanged and the common
   colour on `e` remains in `Omega`.

It remains to check the strict maximality step in the third case. Every
directed path witnessing membership in `F_kappa` stays directed after all
its vertex colours are advanced by `sigma`. Hence every old reachable
vertex remains reachable under `kappa'`.

For an edge `uv` of the induced three-colour graph with `u in F_kappa` and
`v` outside it, the edge cannot be directed `u` to `v` under `kappa`.
Therefore

\[
                  \kappa(u)=\sigma(\kappa(v)).
\]

Only `u` is rotated, so

\[
 \kappa'(u)=\sigma^2(\kappa(v)),\qquad
 \kappa'(v)=\kappa(v)=\sigma(\kappa'(u)).
\]

Thus the crossing edge is directed `u` to `v` under `kappa'`. Since `u`
remains reachable, `v` becomes reachable. This strictly increases the
reachable set while keeping the colouring in `mathcal E`, contradicting
maximality. Consequently no edge of the induced three-colour graph crosses
`F_kappa`. As a nonempty connected reachable set containing `a`, it is
exactly the connected component containing `a`. This proves outcome 3.

The theorem only claims that at least one outcome holds. The argument
actually selects the relevant outcome according to whether `b` is reachable
and whether the recolouring separates the ends of `f`; no missing case is
hidden by the weaker wording.

## 3. Corollary 2.2

A directed `a-b` path for `sigma^{-1}`, read backwards, is a directed
`b-a` path for `sigma`. Outcome 3 already gives an `a-b` path and, more
strongly, reachability from `a` to every vertex of the whole three-colour
component. Hence `a,b` lie in one strong component `Z`, and `Z` reaches
every vertex of the condensation.

If another strong component reached `Z`, the reachability from `Z` back to
that component would merge the two, a contradiction. Thus `Z` is a source.
Every other condensation vertex lies at the end of a nontrivial directed
path from `Z`, and so has positive indegree. Therefore `Z` is the unique
source, exactly as claimed.

## 4. Finite increasing process

The process described in the specialization is justified, not merely the
existence of a maximal colouring. Starting from any member of `mathcal E`,
a rotation either gives a one-edge response, or stays in `mathcal E`. In
the latter case, if the reachable set is not already the whole relevant
three-colour component, the crossing-edge calculation above strictly
increases its size. Membership in `Omega` is invariant under every
rotation, so the underlying induced three-colour graph and its relevant
component do not change during the process. Finiteness therefore forces a
response or the normal form in outcome 3.

In the balanced order-eight application, the reserved triangle has three
distinct colours and its two leaf vertices have a fourth common colour.
The two remaining colours together with that common colour form `Omega`,
so all three reserved colours lie outside `Omega` and remain pointwise
fixed. The specialization therefore matches the general hypotheses.

## 5. Trust boundary

The audit proves only a well-founded normalization of one cyclic
Kempe-reachability process. It does not infer internal disjointness of the
two oppositely ordered paths, the missing rooted linkage in the canonical
web, compatible closed-shore colourings, an order-seven separation, a
`K_7`-minor model, `HC_7`, or Hadwiger's Conjecture.

The cited balanced-order-eight barrier can already be terminal for this
normalization while lacking the desired rooted linkage. Accordingly, any
positive composition theorem must use hypotheses beyond the abstract
reachability-maximal normal form, exactly as the source states.
