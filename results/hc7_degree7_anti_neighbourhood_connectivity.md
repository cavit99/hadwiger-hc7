# Connectivity outside the closed neighbourhood of a degree-seven vertex

**Status:** written proof; separate internal audit GREEN.  The proof
combines previously audited exact-seven separation theorems.  It does not
prove `HC_7`.

## Theorem 1 (degree-seven anti-neighbourhood connectivity)

Let `G` be a seven-connected graph with no `K_7` minor such that `G` is not
six-colourable and every proper minor of `G` is six-colourable.  If

\[
                              d_G(u)=7,
\]

then `G-N[u]` is nonempty and connected.

### Proof

Put `S=N(u)`, so `|S|=7`.  The set `G-N[u]` is nonempty.  Otherwise `u`
would be universal.  The proper minor `G-u` would then have chromatic
number six: it is six-colourable, and a five-colouring would extend to a
six-colouring of `G`.  By the established case `HC_6`, the graph `G-u`
would contain a `K_6` minor, which the singleton branch set `{u}` would
complete to a `K_7` minor.

Let

\[
                         D_1,\ldots,D_m
\]

be the components of `G-N[u]`.  Every `D_i` is adjacent to every literal
vertex of `S`.  Indeed, `N_G(D_i)\subseteq S`; if it missed one vertex of
`S`, then `N_G(D_i)` would be a separator of order at most six, contrary to
seven-connectivity.

Fix `D_1` and consider the actual order-seven separation with open sides

\[
 L=D_1,
 \qquad
 R=\{u\}\mathbin{\dot\cup}D_2\mathbin{\dot\cup}\cdots
       \mathbin{\dot\cup}D_m.
\]

The connected graph `D_1` is an `S`-full connected subgraph in `L`.  On
the other side, the singleton `{u}` and the components `D_2,\ldots,D_m`
are pairwise disjoint `S`-full connected subgraphs.  If `m\ge3`, then `L`
contains one such subgraph and `R` contains at least three.  The audited
adaptive exact-seven `(1,3)` reflection theorem gives either a `K_7` minor
or a six-colouring of `G`, both impossible.  Hence

\[
                              m\le2.                 \tag{1.1}
\]

Suppose that `m=2`.  Let `nu_L,nu_R` be the maximum numbers of pairwise
vertex-disjoint `S`-full connected subgraphs in the two open sides.  One
has `nu_L\ge1` and `nu_R\ge2`, because `{u}` and `D_2` are two such
subgraphs.  The audited exact-seven packet-packing theorem excludes
`nu_L,nu_R\ge2`, so `nu_L=1`.  If `nu_R\ge3`, the adaptive `(1,3)` theorem
again gives a contradiction.  Therefore

\[
                         (nu_L,nu_R)=(1,2).           \tag{1.2}
\]

Write `H=G[S]`.  The audited adaptive `(1,2)` boundary theorem eliminates
this separation unless `H` lies in its invariant 129-graph residual.  We
may therefore assume that it does.  Dirac's contraction-critical
neighbourhood inequality gives

\[
                         \alpha(H)\le d_G(u)-7+2=2.   \tag{1.3}
\]

Inside that audited residual, the only two graphs satisfying (1.3) are
the Moser spindle and its specified one-edge extension.  The audited
singleton-component closure excludes both: apply it to the separation
above with the singleton component `{u}` and the other component `D_2` on
the `(1,2)` side.  This contradiction rules out `m=2`.

Together with nonemptiness and (1.1), this proves `m=1`.  Hence `G-N[u]`
is connected.  \(\square\)

## Corollary 2 (the pole-free bridge lies in the sole exterior component)

Use a degree-seven vertex `u` in the bounded anti-neighbourhood interface,
and write

\[
                         C=G-N[u],\qquad S=N(u).
\]

Then every pole-free path returned by the exact-block Kempe reduction has
all its internal vertices in `C`.

### Proof

Theorem 1 says that `C` is the sole component of `G-N[u]`.  Consequently
the opposite closed shore is exactly `G[S\cup\{u\}]`, and

\[
                       B-(S\cup\{u\})=\varnothing.
\]

The two ends of a returned path lie in distinct components of a two-colour
subgraph of `G[S]`, so they are not joined by a boundary edge and the path
has an internal vertex.  The opposite-shore alternative is therefore
impossible.  The shore dichotomy in the exact-block theorem leaves only a
path whose internal vertices lie in `C`.  \(\square\)

## Exact contribution

This theorem turns the degree-seven part of the bounded-interface
programme into a one-component problem.  In particular, the simultaneous
matching-indexed Kempe paths available at degree seven all live in one
fixed connected graph `C`; there is no second exterior component to which
their labels can drift.

The result does not address degree eight or nine.  At those degrees the
separator `N_G(D)` of a second anti-neighbourhood component can replace
some vertices of the original boundary by vertices of `N(u)-S`, and the
exact-seven packet theorems no longer apply directly.

## Audited inputs

- `results/hc7_exact_seven_packet_packing.md`;
- `results/hc7_exact7_adaptive_packet_reflection.md`;
- `results/hc7_exact7_adaptive_12_boundary_closure.md`;
- `results/hc7_exact7_two_component_singleton_closure.md`; and
- `results/hc7_bounded_interface_exact_block_kempe_reduction.md` for
  Corollary 2; and
- Dirac's contraction-critical neighbourhood inequality.

### Audit-integrity note

All four repository inputs and all three finite verifiers used by their
proofs are Git-tracked.  At the revision checked for this draft, the source
hashes are

| input | SHA-256 | audit record |
|---|---|---|
| exact-seven packet packing | `501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57` | GREEN legacy audit; no source hash recorded |
| adaptive `(1,3)` reflection | `14690180c44a9e5836591a54c4c7cdb7a26f1a2c78147470257072d5bc425e96` | GREEN legacy audit; no source hash recorded |
| adaptive `(1,2)` closure | `df8d47261337659ade312bf8a6dfab22453c92bae5841bbb6b6fd303eadf6533` | GREEN legacy audit; no source hash recorded |
| singleton-component closure | `a68b0f0efe5b526d050261fbec3e0c3df47a96d022cb90f95ae5b3ca9616d8d4` | GREEN audit pinned to this hash |

The adjacent audit independently checks this composition at the displayed
input revisions and pins the present theorem revision.  No cited finite
residual or verifier is untracked.
