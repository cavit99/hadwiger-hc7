# Internal audit of bounded-interface endpoint-pair selection

**Verdict:** **GREEN** for Lemma 2.1, Theorem 2.2, Propositions 3.1,
3.2, and 4.1, and the exact neighbourhood accounting in Section 5.
This is a separate internal mathematical cold audit, not external peer
review.  The result is nonterminal and does not prove the pole-free bridge
composition theorem or `HC_7`.

**Audited source:**
[`hc7_bounded_interface_endpoint_pair_selection.md`](hc7_bounded_interface_endpoint_pair_selection.md)

**Audited source SHA-256:**
`3494dbf62978115012ff195533f5320fd90affe1d71b52d1b2d62dc3624dc1e3`.

The independent audit checked the mathematical content at SHA-256
`7d3473b9bd8b5cc76eef70160f379135e3926f148fd2ef48241c69c830e03ae9`.
The only later changes were the status link to this audit and the three
dependency links in Section 6; the claims and proofs are unchanged.

## 1. Endpoint alternative

The audited exact-block reduction legitimately returns a path `P_x` for
every `x in S`.  Its two colours exclude the fixed colour of `u,x`, so
`x` is not an endpoint.  Its ends lie in distinct components of the same
boundary two-colour graph and therefore cannot be adjacent in `G[S]`.

The two-set argument handles repeated endpoint pairs.  If all `e_x` had
one value `{a,b}`, then `e_a` would contain its forbidden index.  A
pairwise-intersecting family of at least two distinct two-sets either has
a common vertex or is contained in the three edges of one triangle.  The
common-vertex case is excluded by `e_q` at its centre.  In the triangle
case, avoidance forces `e_q=Q-{q}` for every `q in Q`; all three pairs are
boundary nonedges, so `Q` is independent.  The degree-seven independence
bound excludes this outcome, but does not make paths selected from
different colourings disjoint.

## 2. Literal minor constructions

In Proposition 3.1 the two virtual edges have disjoint ends and their
replacement paths have disjoint interiors outside `S union {u}`.  Each
virtual edge used within a `K_6` bag can be replaced by its entire path;
when it supplies an interbag adjacency, splitting the path at one literal
edge preserves both bags.  The two replacements are compatible, every bag
retains an `S` vertex, and the singleton `{u}` is adjacent to all six.

For Proposition 3.2, the five bags are

```text
P_1-q_1, {q_1}, P_2-q_2, {q_2}, {b}.
```

They are disjoint, connected and pairwise adjacent: the last edge of each
path replaces one missing matching edge and `G[R]` supplies the other eight
adjacencies.  The bags `{u,a}` and `C` are connected and disjoint from those
five.  The vertex `u` sees all five rooted bags, `a` joins its bag to `C`,
and fullness of `C` supplies the remaining five contacts.  Thus all 21
adjacencies of the displayed `K_7` model have literal witnesses.

## 3. Fixed aligned restart

For a component `D` of `G-N[u]`, its full boundary satisfies

```text
S_D=N(D) subseteq N(u),   7 <= |S_D| <= d(u) <= 9.
```

If the original aligned vertex `z` lies in `S_D`, the unchanged equality
`chi(G-{u,z})=6` preserves the same aligned pair and the same `G-uz`
response.  The audited low-degree separation and exact-block arguments
therefore reinstantiate with `D,S_D`.  The inequality `|D|<|C|` is a strict
decrease of the declared literal host-component parameter.  Merely finding
a path in `D` supplies neither `z in S_D` nor a fresh eligible aligned
vertex, exactly as the source warns.

## 4. Residual accounting and scope

For a component `D` of `C-Z`, all external neighbours lie either in `S` or
in `Z`, and these sets are disjoint.  Hence (5.1) is the complete literal
neighbourhood identity.  Seven-connectivity gives exactly the lower bound

```text
a(D) >= 7-|S|+d(D),
```

not the upper bound needed for a boundary of order at most nine.  Since a
nonempty residual has a neighbour in `Z subseteq C`, its new boundary also
contains a nonneighbour of `u`; even a numerically small residual boundary
is not automatically a same-form anti-neighbourhood interface.

No unresolved assumption remains in the stated lemmas.  The unresolved
step is exactly the one retained in the source: a common operation-specific
colouring or another literal mechanism must make two endpoint pairs into
disjoint usable paths, force one augmented-boundary minor, or preserve the
aligned response through a strict restart.
