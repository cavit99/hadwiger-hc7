# Independent audit of the dirty two-bridge-chain barrier

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical and computational audit, not external peer
review.  The auditor did not author the barrier or its verifier.

## Revisions audited

- barrier:
  [`hc7_atomic_dirty_two_bridge_chain_barrier.md`](hc7_atomic_dirty_two_bridge_chain_barrier.md)
- barrier SHA-256:
  `8e5bd1998a40b765b0180e88cac43bba3c0ad0986c4559c1266441db5e6c8d2a`
- retained verifier:
  [`hc7_atomic_dirty_two_bridge_chain_barrier_verify.py`](hc7_atomic_dirty_two_bridge_chain_barrier_verify.py)
- verifier SHA-256:
  `5037c1e198eefe3be17873f0a3ea50ab632d7a729f9ff417520a02ebff41370c`

The promoted barrier differs from the audited pre-promotion revision only
in its status metadata: `separate internal audit pending` became
`separate internal audit GREEN`.  Replacing `GREEN` by `pending` on that
single line reconstructs SHA-256
`9d982965ea14f7148cba0ae1cb7c8533c8fb4eb6b8a36ace3658e5d98bb927af`,
the exact revision audited above.  No mathematical or computational content
changed.

## Verdict

GREEN.  The graph, written `K_7`-minor exclusion, connectivity and colouring
claims, all 78 Kuratowski certificates, the `K_2`-joined-icosahedron
subdivision exclusion, and the complete incident-nonedge saturation table
are correct at the revisions above.  The scope is also stated correctly:
this is a barrier to a bare local two-bridge implication, not a counterexample
to `HC_7` or to a theorem that uses seven-connectivity.

The verifier was rerun with

```text
.venv/bin/python -B barriers/hc7_atomic_dirty_two_bridge_chain_barrier_verify.py
```

and returned `GREEN atomic dirty two-bridge-chain barrier`.  Its reported
checks included 92 connectivity deletions, 78 validated Kuratowski
subdivisions (`32` of `K_5` and `46` of `K_{3,3}`), all five saturation
profiles, and 33 exhaustive subdivision-embedding cases in
`K_2\vee I` over 377,661 backtracking states.

## Checks performed

1. **Construction.**  Independent reconstruction gives thirteen vertices
   and thirty-two edges.  The four retained routes are exactly
   `f-h-g`, `f-p-a`, `g-q-a`, and `a-r-s-c`; `eh,hx,pr,sq` are present.
   The added edges `pr,sq` are distinct `T`-bridges, and their composition
   uses the retained interval `rs`.  Reversing the two attachments on the
   `ac` route gives an isomorphic graph under `f<->g` and `p<->q`.

2. **Width-five decomposition.**  For `J=D_*-e`, every edge occurs in one
   of the seven displayed bags, every vertex's bag set is connected in the
   displayed tree, and the largest bags `U,V` have order six.  Thus the
   decomposition has width five.  The verifier checks these three defining
   properties directly.

3. **Helly reduction.**  In a hypothetical spanning `K_6` model of `J`,
   the decomposition nodes meeting any connected branch set form a subtree.
   An edge between two branch sets puts both subtrees through a common bag,
   so the six subtrees are pairwise intersecting.  Subtree Helly gives one
   common bag.  Six disjoint branch sets meeting a bag of order at most six
   force the common bag to be `U` or `V`, with exactly one distinct root
   vertex of that bag in each branch set.  For every absent root pair, the
   two corresponding branch sets and their contact edge therefore contain a
   root-to-root path whose internal vertices avoid the common bag.  Paths
   for disjoint root pairs are vertex-disjoint because their four branch
   sets are disjoint.

4. **The `U` case.**  The components of `J-U` and their attachment sets are
   exactly the singleton `h` with attachments `{f,g,x}` and
   `K=J[{a,p,q,r,s}]` with attachments `{c,d,f,g,x}`.  The only absent pairs
   in `J[U]` are `cd,fg,fx,gx`.  If `h` is assigned to the `f`- or
   `g`-rooted branch set, the two remaining disjoint-pair paths both require
   `a`, because `d` and `x` have `a` as their unique contact with `K`.  If
   `h` is assigned to the `x`-rooted branch set, a `c`--`d` path contains
   both `s,a`, while every `f`--`g` path in
   `K` joins `p` to `q` and meets the separator `{a,s}`.  Each assignment is
   impossible.

5. **The `V` case and final deletion.**  The components outside `V` are
   `{b}`, `{h}`, and the path `L=p-r-s-q`, with exactly the attachment sets
   in the note.  Only `b` can repair `cd`, so it belongs to the `c`- or
   `d`-rooted branch set.  Since `L` has no contact with `x`, `h` must belong
   to the `x`-rooted branch set to repair both `xf,xg`.  The remaining
   `a`--`c` and `f`--`g` paths through `L` both contain `s`, contradicting
   their required disjointness.  Hence `J` has no `K_6` minor.  Deleting the
   at most one branch set containing `e` from any `K_7` model in `D_*` would
   give such a `K_6` model, so `D_*` has no `K_7` minor.  The independent
   spanning-partition search agrees.

6. **Connectivity and colouring.**  All `1+13+78=92` deletions of at most
   two vertices leave `D_*` connected, while deleting
   `N(p)={a,f,r}` disconnects it.  Thus its vertex-connectivity is three.
   The displayed four sets are independent and partition the vertex set;
   `b,c,e,f` induce a `K_4`.  Therefore the chromatic number is exactly four.

7. **All two-vertex planarizing candidates.**  For each of the 78 vertex
   pairs, the returned counterexample is checked to be a literal subgraph of
   the deletion remainder.  The verifier walks and removes every
   degree-two path, rejects repeated suppressed edges, and verifies that the
   resulting core is isomorphic to `K_5` or `K_{3,3}`.  The resulting counts
   are 32 and 46, respectively.  Hence no two-set planarizes `D_*`; a
   planarizing set of smaller order would also give a planar remainder after
   one further deletion.

8. **The standard seven-connected guardrail.**  Independent checks give
   that the icosahedron is planar and five-connected and that
   `K_2\vee I` is seven-connected.  It is `K_7`-minor-free because deleting
   the at most two branch sets containing the complete-factor vertices from
   a hypothetical model would leave a `K_5` minor in the planar
   icosahedron.

9. **Subdivision-search exhaustiveness.**  Every vertex of `D_*` has degree
   at least three, so its thirteen branch vertices have distinct host images
   in any subdivision.  The fourteen-vertex host leaves at most one vertex
   for all path interiors.  The exhaustive universe is therefore precisely
   the literal pattern plus the thirty-two patterns obtained by subdividing
   one edge once.  The injective-map search is complete: it enforces distinct
   images and every pattern adjacency; its degree and unused-neighbour tests
   are necessary-condition pruning only.  It finds no embedding in all 33
   cases.

10. **Exact saturation.**  The fifteen stored positive edges cover exactly
    the positive entries in the five table rows.  Every displayed branch-set
    tuple is spanning, connected, disjoint, and pairwise adjacent after its
    edge is added.  The five negative augmentations cover exactly all other
    incident nonedges.  The exact spanning-partition oracle finds no `K_7`
    model in the second augmentation; after deleting `e`, it finds no `K_6`
    model in each of the other four.  The deletion argument and subgraph
    monotonicity therefore certify every individual negative entry.

## Trust boundary

No unresolved assumption remains within the stated local barrier.  The
graph is only three-connected and four-chromatic, and the fourteen-vertex
guardrail search does not address subdivisions in larger hosts.  The barrier
does not classify arbitrary one-sided bridge chains, produce a bounded
response interface, or refute any conclusion that uses seven-connectivity
or proper-minor colouring responses.
