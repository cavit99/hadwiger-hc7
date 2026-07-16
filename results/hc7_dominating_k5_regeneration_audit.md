# Audit of the dominating-`K_5` regeneration theorem

**Audit status:** GREEN (separate internal audit).

**Audited file:** `hc7_dominating_k5_regeneration.md`

**Audited SHA-256:**
`cd0abe45c2ccfcd386f1a03ed20f72486eecbc2eb084ddb734c5a9f9c8e1e904`

The exact promoted revision was rechecked on 2026-07-16 after its status
header and adjacent-audit link were updated.  The mathematical statement
and proof are unchanged and are the revision covered below.

**External source checked:** António Girão, Freddie Illingworth, Bojan
Mohar, Sergey Norin, Raphael Steiner, Youri Tamitegama, Jane Tan, David R.
Wood and Jung Hon Yip, *The Dominating 4-Colour Theorem*,
arXiv:2605.10112v1 (11 May 2026), especially Theorem 1.1, the two remarks
immediately following it, Corollary 1.2, and the remark following that
corollary.

## Verdict

The theorem and its stated terminal consequence are correct. No adjacency
assumption on the deleted pair is used. For every two distinct vertices
`p,q`, the graph `G-{p,q}` is a proper minor, has chromatic number between
five and six, and hence contains the normalized dominating `K_5` model and
the stated subdivision. A pair meeting every dominating `K_5` model would
make its deletion four-colourable and therefore gives a six-colouring of
`G`; this is a valid terminal contradiction.

## Detailed checks

### Definition and chromatic inequalities

1. The local definition of strongly seven-contraction-critical is explicit:
   `chi(G)=7` and every proper minor has chromatic number at most six. The
   argument uses exactly this definition, regardless of possible variation
   in terminology elsewhere.
2. If `P={p,q}` consists of two distinct vertices, then `J=G-P` is a proper
   minor of `G`, obtained by vertex deletions. Hence `chi(J)<=6`.
3. If `chi(J)<=4`, any proper four-colouring of `J` extends to a proper
   six-colouring of `G` by assigning two new, distinct colours to `p` and
   `q`. This works both when `pq` is an edge and when it is a nonedge. Thus
   `chi(J)>=5`.
4. No hidden small-order issue occurs: `chi(G)=7` already implies that `G`
   has at least seven vertices, so deleting two distinct vertices is a
   genuine proper-minor operation.

### Use of the Dominating 4-Colour Theorem

5. The cited Theorem 1.1 says exactly that every graph with no dominating
   `K_5` model is four-colourable. Its contrapositive applies to `J` because
   `chi(J)>=5`.
6. The paper defines a dominating model exactly as the draft does: the
   branch sets are pairwise disjoint connected subgraphs, and every vertex
   in a later branch set has a neighbour in every earlier branch set.
7. Immediately after Theorem 1.1, the paper observes that a dominating
   model `(T_1,...,T_5)` may be replaced by
   `(T_1,T_2,T_3,{v},{w})`, where `v` is chosen in the old `T_5` and `w` is
   a neighbour of `v` in the old `T_4`. Thus `vw` is an edge and the last
   two branch sets are singletons, exactly as stated.
8. The next remark permits `T_3` to be a shortest path between a neighbour
   of `v` and a neighbour of `w`, so the subgraph induced by
   `V(T_3) union {v,w}` is a cycle. The normalization in (1.2) is therefore
   exact.
9. Corollary 1.2 applies to every graph of chromatic number at least five
   and yields a subdivision of `K_5` or of the graph obtained by splitting
   one `K_5` vertex into two adjacent degree-three vertices. Its following
   remark gives the asserted two incident unsubdivided edges in the
   relevant `K_4` subgraph.

### The pair-transversal conclusion

10. A dominating model in `G` avoids `P` if and only if the same branch
    sets form a dominating model in the induced subgraph `G-P`. Therefore
    the two conditions in Section 2 are equivalent.
11. Meeting all dominating `K_5` models is indeed weaker than meeting all
    ordinary `K_5` models: every dominating model is an ordinary model, but
    the external paper gives explicit examples showing that the converse
    fails in general.
12. If `G-P` has no dominating `K_5` model, Theorem 1.1 makes `G-P`
    four-colourable. Giving `p,q` two new distinct colours then
    six-colours `G`, again without assuming whether `pq` is present.
13. Conversely, the regeneration theorem shows that no such pair can exist
    in a strongly seven-contraction-critical graph. Thus deriving such a
    pair elsewhere in an `HC_7` argument is a contradiction, not an
    additional structural conclusion about `G-P`.

### Interaction with labelled near-clique models

14. Section 3 correctly limits the conclusion. The external theorem does
    not prescribe the deleted roots' adjacencies, the locations of branch
    sets relative to an existing model or separation, or a label-preserving
    exchange. No such stronger assertion is used.

## Trust boundary

- The audit treats the cited Dominating 4-Colour Theorem and its corollary
  as established external input; their proofs are not reproduced here.
- The result regenerates an unlabelled dominating `K_5` model after every
  two-vertex deletion. It does not itself construct a `K_7` minor, preserve
  an existing `K_5` model, or identify a pair meeting all ordinary `K_5`
  models.

No unresolved mathematical gap remains in the theorem as stated.
