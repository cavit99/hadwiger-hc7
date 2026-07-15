# Bounded order-four carrier exhaustion

**Status:** exact computer-assisted support for the first compulsory-bridge
milestone; not a proof of the unbounded theorem.

The current frozen atom has a two-connected thin shore `A`, a compulsory
root `z` with `d_A(z)>=3`, `A-z` connected and full to the six literals
`W=S-{u}`, and `zu` as the unique `A-u` edge.  The smallest shore not
already covered by the low-root-degree and cycle theorems has order four.

Up to relabelling, every such order-four graph is one of

```text
K4-e: za,zb,zc,ac,bc,
K4:   za,zb,zc,ab,ac,bc.
```

Indeed, two-connectivity makes the three vertices of `A-z` connected, so
they induce at least a two-edge path.

The companion verifier exhausts every one of the `2^24` possible literal
contact maps from `A` to `W`, for each of these two thin graphs and each
rooted paired width-two frontier.  It retains exactly the
contact maps satisfying

1. `zu` is the sole `A-u` contact;
2. `A-z` is `W`-full; and
3. for every nonempty connected `D subseteq A`,

   ```text
   |N_A(D)| + |N_S(D)| >= 7.
   ```

For every retained map it finds two disjoint nonempty connected adjacent
sets `X,Y subseteq A`, with `z in X`, and a boundary partition

```text
S = I dotunion J dotunion U
```

such that `I,J` are nonempty independent sets, `U` is a clique, `X`
contacts every member of `I`, and `Y` contacts every member of `J` (after
possibly interchanging `I,J`).  Equivalently, Z3 proves unsatisfiable the
formula asserting all three frozen geometric conditions and failure of
every adaptive carrier return.

The earlier version incorrectly used five **unrooted** representatives
while fixing one arbitrary vertex as the compulsory literal.  The repaired
verifier generates all 192 labelled paired frontiers and canonicalizes the
distinguished rooted graph `(H,u)`.  It obtains 19 rooted types (nine if
one additionally assumes `uc` is an edge, an assumption not used here).
All 38 rooted-frontier/thin-graph formulas are `UNSAT`.  Thus the entire
order-four thin-shore cell exits through the already audited
adaptive clique-reservoir theorem.  No equality-state pullback, lock-path
choice, or near-model normalization is needed at this order.

## Exact consequence and boundary

This is bounded exhaustive support for a sharp restricted lemma:

> In the frozen compulsory atom, if `|A|=4`, the carrier outcome of the
> first path/`Y` bridge-hull milestone always occurs.

The computation does **not** verify contraction-criticality, the rich
packets, or `K_7`-minor-freeness on a standalone host.  Those are used only
through the already proved adaptive return after the literal carriers have
been found.  It therefore is not an `HC_7` counterexample search and does
not close `|A|>=5`.

Its useful falsification boundary is exact: any counterarchitecture to the
post-lift implication must have at least five thin-shore vertices.  The
remaining missing hypothesis is not another order-four portal pattern; it
must control a genuinely nontrivial crossed bridge, or the all-locks
edge-nonseparable residue.
