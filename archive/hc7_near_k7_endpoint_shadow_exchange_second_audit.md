# Second independent audit: endpoint shadow exchange

## Verdict

**GREEN.**  No counterexample exists under the written hypotheses: the
proof explicitly constructs a smaller labelled `K_7^vee` model.  The
operation does not use seven-connectivity, contraction-criticality, or a
palette argument.  The target-free hypothesis is needed only in the
upstream programme, not for this exchange itself.

## Safe endpoint and literal branch sets

Let `P=p_0...p_m`, `m>=1`, and let `E` meet `P`.  If `P-p_0` still meets
`E`, delete `p_0`; otherwise all `E`-portals of `P` lie at `p_0`, so
delete the distinct endpoint `p_m`.  In the first case move `p_0` into
`U_1`.  Then

* `P-p_0` is nonempty and connected;
* `U_1 union {p_0}` is connected through an actual `p_0U_1` edge;
* the cut edge `p_0p_1` restores the spoke from the new path bag to the
  enlarged `U_1` bag;
* the fixed `p_mU_3,p_mU_4` edges and the safe `E`-portal survive; and
* the path remains anticomplete to the fixed missing twin `D`.

Thus the four required spokes are exactly to
`E,U_1 union {p_0},U_3,U_4`.  The bags `D,U_2` may be declared the two
unprescribed twins.  An accidental residual `P-U_2` edge is harmless,
because a minor model may have edges in addition to the target.  All old
foreign--foreign edges survive since no foreign bag loses a vertex.  The
right-end operation is symmetric.

## Deficient-first comparison

The original normalization minimizes `|A|` first over all labelled,
not-necessarily-spanning `K_7^vee` models in `G`.  The comparison is not
restricted to the original identities of `B,C`, nor to the original
orders of the later foreign bags.  Consequently both of the potentially
delicate operations are admissible:

1. a retained foreign bag may already have been enlarged by a transported
   exterior component; and
2. after the endpoint move the old fixed twin `D` and an unabsorbed
   endpoint row may be relabelled as the two unprescribed twins.

The new deficient bag has strictly fewer vertices.  This first-coordinate
improvement dominates every later coordinate, so no enlargement or
relabeling of a foreign bag can defeat the contradiction.

## Corollary 3

If a nontrivial minimal path met `B` or `C`, use that row as `E` and the
other as `D`; the theorem immediately gives a smaller model.  Hence it is
anticomplete to both.

If an unused exterior component `K` meets both `P` and, say, `B`, then
`B union K` is a connected foreign bag, retains every old clique-model
edge, and has a literal edge to `P`.  The already proved anticompleteness
of `P` to `C` makes `C` the fixed missing twin.  Applying the endpoint
exchange again gives a smaller deficient bag.  Therefore every exterior
component meeting `P` avoids both `B` and `C`.

This argument permits `K` to have additional edges to neutral bags; such
edges only add target adjacencies.  It also does not require the model to
be spanning.  Thus no static or contraction-critical counterexample can
invalidate Corollary 3 while retaining its exact hypotheses.

## Exact residual

The audit establishes only

\[
 \text{nontrivial deficient-minimal path}
 \Longrightarrow
 \text{both twins and all path-meeting exterior lobes avoid each other}.
\]

It does not shorten the both-missing path, singletonize a foreign bag, or
produce the three full shores required for the both-missing `K_7`
completion.
