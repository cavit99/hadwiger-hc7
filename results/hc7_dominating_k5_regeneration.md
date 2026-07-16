# Dominating `K_5` models after deleting any two vertices

**Status:** written proof; separately internally audited in
[`hc7_dominating_k5_regeneration_audit.md`](hc7_dominating_k5_regeneration_audit.md).
This note records a uniform consequence of the Dominating 4-Colour Theorem. It does not preserve
the labels of a pre-existing minor model.

## 1. Uniform regeneration theorem

Call a graph `G` **strongly seven-contraction-critical** here if

\[
 \chi(G)=7
 \quad\text{and}\quad
 \chi(H)\le 6\text{ for every proper minor }H\text{ of }G.
\]

### Theorem 1.1

Let `G` be strongly seven-contraction-critical, let `P={p,q}` be any two
distinct vertices, and put `J=G-P`. Then

\[
                         5\le \chi(J)\le 6.              \tag{1.1}
\]

Consequently `J` contains a dominating `K_5` model. Moreover, one may choose
such a model in the form

\[
                    (T_1,T_2,T_3,\{v\},\{w\}),          \tag{1.2}
\]

where `vw` is an edge, `T_3` is a path, and

\[
                  J[V(T_3)\cup\{v,w\}]
\]

is an induced cycle. In particular, this model is an ordinary `K_5`-minor
model in `J`.

The same graph `J` also contains a subdivision of `K_5` or of
`\widehat K_5`, the graph obtained from `K_5` by splitting one vertex into
two adjacent degree-three vertices. The refinement following Corollary 1.2
in the cited paper permits two incident edges in the distinguished `K_4`
of that subdivision to remain unsubdivided.

### Proof

The graph `J` is a proper minor of `G`, so `\chi(J)\le6`. If `J` were
four-colourable, colour `p` and `q` with two fresh and distinct colours.
This is a proper six-colouring of `G`, regardless of whether `pq` is an
edge, contradicting `\chi(G)=7`. Thus `\chi(J)\ge5`.

The contrapositive of Theorem 1.1 of Girão--Illingworth--Mohar--Norin--
Steiner--Tamitegama--Tan--Wood--Yip now gives a dominating `K_5` model in
`J`. The paragraph immediately following that theorem states that the last
two branch sets can be made singletons, and the following structural remark
states that the third branch set can be made a path whose union with those
two singletons induces a cycle. This gives (1.2). Corollary 1.2 and its
following remark give the asserted subdivision refinement. \(\square\)

Here a dominating `K_5` model is an ordered tuple of pairwise
vertex-disjoint connected subgraphs `(T_1,...,T_5)` such that, for every
`i<j`, every vertex of `T_j` has a neighbour in `T_i`.

## 2. The resulting terminal condition

For a two-set `P`, the following are equivalent:

1. `P` meets the vertex-union of every dominating `K_5` model in `G`;
2. `G-P` has no dominating `K_5` model.

This is formally weaker than requiring `P` to meet every ordinary `K_5`
minor model, because every dominating model is an ordinary minor model but
the converse is not part of the definition. It is nevertheless already a
terminal contradiction: Theorem 1.1 of the cited paper would make `G-P`
four-colourable, and two fresh colours on `P` would six-colour `G`.

Thus an `HC_7` proof may aim only to find a pair meeting every **dominating**
`K_5` model. The theorem above also shows exactly what such a proof must
overcome: in a hypothetical counterexample, a normalized dominating model
can be regenerated after deleting every pair. No strict separation between
the two terminal conditions is claimed here for the strongly
seven-contraction-critical class.

## 3. Interaction with the order-eight two-root host

If `a,b` are the two deleted roots in the order-eight near-`K_7` setup, the
common host `J=G-{a,b}` therefore contains a model of the form (1.2). This
is a useful graph-global regeneration statement, but it has no prescribed
relationship to the existing branch-set labels:

- the singleton vertices `v,w` lie in `J` and need not be adjacent to either
  deleted root;
- none of `T_1,T_2,T_3` is required to meet a specified boundary vertex,
  shore, or branch set of the near-`K_7` model; and
- the induced cycle may cross several prescribed branch sets or both sides
  of a separation.

Accordingly, (1.2) may be re-chosen extremally and compared with the
order-eight structure, but it does not itself repair the missing root
adjacency or give a label-preserving rerouting. Using it for either purpose
without an additional exchange theorem would smuggle in precisely the
missing label-preservation step.

## 4. Source

António Girão, Freddie Illingworth, Bojan Mohar, Sergey Norin, Raphael
Steiner, Youri Tamitegama, Jane Tan, David R. Wood and Jung Hon Yip,
*The Dominating 4-Colour Theorem*, Theorem 1.1, the two structural remarks
following it, and Corollary 1.2,
[arXiv:2605.10112](https://arxiv.org/abs/2605.10112) (2026).
