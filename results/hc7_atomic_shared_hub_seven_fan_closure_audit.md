# Independent audit: seven-fan closure of the shared-hub graph

**Verdict:** GREEN.

The fan lemma, saturated-endpoint forcing, transported certificates, two
clean paths, first-intersection construction, and final `K_7` branch-set
model are correct.  No unresolved assumption or gap remains within the
stated theorem.

## 1. Audited revision and dependency

This audit checks the finalized
[`hc7_atomic_shared_hub_seven_fan_closure.md`](hc7_atomic_shared_hub_seven_fan_closure.md)
at SHA-256
`1b14e893d9822e55d86016985f395428dac469bec2e5a04034ea4ebed5ad32f2`.

The mathematical content was first checked at SHA-256
`f25825212b9a5638c146b89c325872048a05685508974c5d0ccde7c30b1acea5`.
The finalized source differs only by changing its audit status from pending
to GREEN and updating the adjacent-audit sentence accordingly.  I rechecked
that status-only diff after completing this audit; the theorem statement,
proof, branch sets, and trust boundary are unchanged.

The proof uses the five one-edge certificates in
[`hc7_atomic_shared_hub_same_vertex_saturation.md`](hc7_atomic_shared_hub_same_vertex_saturation.md),
whose finalized audited source has SHA-256
`d315456f5189af245f2249d52aa6cd84d9eb35fedfbc0cc4e81ccb432dbad303`.
I also reran its deterministic verifier, SHA-256
`ba17649fa24c8abceae189d4566ca145d996c247f73d203b4759741c86186e3d`,
and obtained its recorded GREEN output.

This is an internal audit independent of the authoring pass, not external
peer review.

## 2. Fan lemma

In Lemma 2.1, after adjoining a vertex `z` complete to `S`, no set `X` of
fewer than `k` vertices disjoint from `v,z` separates those two vertices.
Indeed, `G-X` is connected by `k`-connectivity, and
`|S|>=k>|X|` leaves a vertex of `S-X` adjacent to `z`.  The vertex form of
Menger's theorem therefore supplies `k` internally disjoint `v`--`z`
paths.

Their penultimate vertices in `S` are distinct, because those vertices are
internal to the `v`--`z` paths.  Truncating each path at its first visit to
`S` preserves pairwise intersection only at `v` and makes every interior
avoid `S`.  This proves exactly the clean-interior form used later.

## 3. Saturated endpoint forcing

For a fan path `R` from `v` to an endpoint `u in U`, its interior avoids
`S=V(K)-{v}` and also avoids `v`, because `R` is simple.  Thus it avoids
all of `V(K)`.  Contracting every edge of `R` except the final edge incident
with `u` identifies no two vertices of `K`: the contracted vertex contains
`v` and vertices outside `K`, while `u` remains distinct.  All retained
edges of `K` survive, and the uncontracted final edge supplies `vu`.
Hence the resulting minor contains `K+vu`, exactly as claimed.

If no endpoint belongs to `U`, the `k` distinct fan endpoints all belong
to the `k`-set `A`, so they equal `A`.  The proof does not choose seven
unrelated paths; it retains one simultaneous fan.

For `q=p_ad`, the twelve possible endpoints split as

\[
 \{a,d,g,e,f,h,x\}\mathbin{\dot\cup}
 \{b,c,p_{ac},p_{bd},p_{bc}\}.                         \tag{3.1}
\]

The second set is precisely the five one-edge-terminal neighbours checked
in the same-vertex theorem.  The permutation

\[
 (a\ b)(c\ d)(p_{ac}\ p_{bd})(p_{ad}\ p_{bc})          \tag{3.2}
\]

is an automorphism of the whole labelled base graph.  It maps the terminal
set in (3.1) to

\[
                    \{a,d,p_{ac},p_{bd},p_{ad}\},       \tag{3.3}
\]

while fixing `e,f,g,h,x`.  Applying it to each explicit branch-set
certificate transfers the certificates to `q'=p_bc`; no symmetry of the
ambient host is assumed.

Consequently, in a `K_7`-minor-free host, the two applications of endpoint
forcing really do return clean paths `P:q--h` and `P':q'--h` satisfying

\[
 V(P)\cap V(G_*)=\{q,h\},\qquad
 V(P')\cap V(G_*)=\{q',h\}.                            \tag{3.4}
\]

## 4. First-intersection construction

Traverse `P'` from `q'` and let `y` be its first vertex on `P`.  The vertex
`q'` is not on `P`, so `y` has a predecessor `z` on `P'`.  The prefix
`B_0=P'[q',z]` is connected and disjoint from `H=V(P)`; the edge `zy`
joins those two sets.  Cleanliness in (3.4) gives

\[
 B_0\cap V(G_*)=\{q'\},\qquad
 H\cap V(G_*)=\{q,h\}.                                \tag{4.1}
\]

Therefore adjoining `b` to `B_0` along the base edge `bq'` preserves
connectedness and creates no intersection with `H` or with any other
displayed branch set.  This remains valid when `y=h`, when `z=q'`, or when
the two paths meet before `h`; those possibilities require no separate
case.

The seven branch sets in Theorem 5.1 are nonempty and pairwise disjoint.
Their nontrivial connectedness is supplied by the paths `P`, `P'[q',z]`,
the edge `bq'`, and the base edges

\[
                         ag, ap_{ac}, dp_{bd}, cx.    \tag{4.2}
\]

## 5. Complete contact audit

The theorem's contact table contains exactly the twenty-one unordered
pairs of its seven bags.  Each listed base contact has the asserted
endpoints:

- `e` uses `ef,ea,eh,eb,ed,ec`;
- `f` uses `fa,fh,fb,fd,fc`;
- the `A` bag uses `a-q,gb,gd,ax`;
- the path bag `H` uses `zy,q-d,hx`;
- the `B` bag uses `b-p_bd,bx`; and
- the `D` bag uses `dx`.

Here `q=p_ad`, so `a-q` and `q-d` are the two halves of the subdivided
`ad` route; `q'=p_bc`, so `bq'` is the edge used inside `B`; and `zy` is
the first-intersection edge with one endpoint in each path bag.  All other
contacts are edges of `G_*`.  Thus all seven connected bags are pairwise
adjacent and form an explicit `K_7` model.

## 6. Trust boundary

The verdict covers arbitrary larger hosts and uses only seven-connectivity
once the exact labelled `G_*` subgraph is retained.  It does not prove that
an arbitrary dirty replacement path contains this labelled subgraph.  The
four subdivided routes, anchor edges, common vertex `h`, and edges `eh,hx`
must first be preserved literally.  The result uses no contraction-critical
colouring response and does not close configurations lacking that ownership.
