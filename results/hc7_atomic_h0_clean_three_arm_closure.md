# Clean-root attachment matching in the atomic `H_0` frame

**Status:** written proof; separate internal audit GREEN.

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},
\]

and let `T` be a subdivision of `H_0` whose branch vertices retain the
labels `a,b,c,d,e,f,g,x`.  For a point `z` of `T`, retain the endpoint
support notation

\[
 \sigma_T(z)=
 \begin{cases}
  \{v\},&z\text{ is the branch vertex }v,\\
  \{u,v\},&z\in\operatorname{int}(T_{uv}).
 \end{cases}                                             \tag{1.1}
\]

This note closes one explicit multi-attachment configuration around the
collision vertex.  It does not compose an arbitrary dominating `K_5`
model with the atomic frame.

## 1. Three disjoint clean-root arms are terminal

For `h in {e,f,g}`, call a path `L_h` in `T` a **clean-root arm** from
`h` to `z_h` if

- `h in sigma_T(z_h)`; and
- `L_h` is the subpath from `h` to `z_h` of the corresponding segment
  incident with `h` (with `L_h={h}` when `z_h=h`).

In particular, if `z_h` is internal on `T_{hr}`, the arm stops before the
other branch vertex `r`.

### Theorem 1.1 (clean three-arm closure)

Let `X` be a connected subgraph of `G` such that

\[
                         V(X)\cap V(T)=\{x\}.             \tag{1.2}
\]

Suppose there are three distinct vertices `z_e,z_f,z_g in V(T)-{x}`
such that

1. `X` is adjacent to each of `z_e,z_f,z_g`; and
2. the three clean-root arms `L_e,L_f,L_g` from `e,f,g` to the
   corresponding vertices are pairwise vertex-disjoint.

Then `G` contains an explicit `K_7`-minor model.

#### Proof

Start seven branch sets as follows:

\[
 X,\qquad V(T_{ac}),\qquad \{b\},\qquad \{d\},
 \qquad V(L_e),\qquad V(L_f),\qquad V(L_g).              \tag{1.3}
\]

They are pairwise disjoint.  Indeed, `X` meets `T` only at `x`, none of
the clean-root arms contains `x`, the three arms are disjoint by
hypothesis, and an arm rooted at `e,f`, or `g` lies on a segment incident
with that clean root and stops before its other branch end.  It therefore
does not meet `T_{ac}` or the branch vertices `b,d`.

Allocate the unused internal vertices of every segment of `T` to branch
sets containing its ends.  On a segment containing one selected arm, keep
that arm in its clean-root branch set and allocate the unused far suffix
to the branch set containing the other end.  If two selected arms enter
the same clean--clean segment from opposite ends, split the unused middle
interval across one edge.  On every other segment, allocate its internal
vertices arbitrarily to one end, splitting across one edge when the two
end labels belong to different branch sets.  Every set in (1.3) remains
connected and disjoint, and every original segment still supplies the
required adjacency between its endpoint branch sets.

It remains to audit all quotient adjacencies.  The set `X` is adjacent to
the `e,f,g` sets at `z_e,z_f,z_g`.  It is adjacent to the set containing
`a,c`, to `{b}`, and to `{d}` along the four segments
`T_xa,T_xb,T_xc,T_xd`.  Among the other six branch sets, the merge of
`a` with `c` repairs both absent pairs: it meets `{b}` along `T_cb` and
`{d}` along `T_ad`.  The vertices `b,d` are adjacent, every clean label
is adjacent in `H_0` to each of `a,b,c,d`, and `e,f,g` are pairwise
adjacent.  The segment allocation above preserves each of those
adjacencies.  Thus the seven sets in (1.3) are connected, disjoint, and
pairwise adjacent, so they form a `K_7`-minor model.  \(\square\)

The proof uses collective adjacency of the connected set `X`; it does not
require three internally disjoint paths inside `X`.

## 2. Attachment matching and Hall deficiency

Let `X` satisfy (1.2), and put

\[
 A_X=N_G(V(X))\cap (V(T)-\{x\}).                         \tag{2.1}
\]

Define a bipartite graph `M_X` with left side `{e,f,g}`, right side `A_X`,
and edge `hz` precisely when

\[
                              h\in\sigma_T(z).            \tag{2.2}
\]

### Corollary 2.1 (clean attachment matching)

If `M_X` has a matching saturating `{e,f,g}`, then `G` contains a `K_7`
minor.  Consequently, in a `K_7`-minor-free graph,

\[
                              \nu(M_X)\le2.               \tag{2.3}
\]

Equivalently, Hall's theorem gives a nonempty set
`Y subseteq {e,f,g}` such that

\[
                              |N_{M_X}(Y)|<|Y|.            \tag{2.4}
\]

#### Proof

Choose a saturating matching.  Each matched edge `hz` determines the
clean-root arm from `h` to `z`.  Arms belonging to different segments are
vertex-disjoint.  The only possible overlap occurs when two matched
attachments lie internally on the same segment between two clean roots.
Both attachment vertices are then adjacent in `M_X` to both ends of that
segment.  If necessary, interchange their matched clean roots so that the
attachment nearer each end is assigned to that end.  The two resulting
arms are disjoint.  Performing this uncrossing on each clean--clean
segment gives three pairwise disjoint clean-root arms, so Theorem 1.1
applies.  Statements (2.3) and (2.4) follow by contraposition and Hall's
theorem.  \(\square\)

This applies in particular to one component bridge.  If `B` is a component
of `G-V(T)` with `x in N_G(B)`, then

\[
                              X=G[B\cup\{x\}]             \tag{2.5}
\]

is connected and satisfies (1.2).  In a seven-connected host the bridge
has at least seven attachments, hence at least six attachments other than
`x`.  If the host has no `K_7` minor, however, their clean-support incidence
graph must still satisfy (2.3)--(2.4).  The numerical attachment bound by
itself does not force a saturating clean matching: arbitrarily many
attachments may lie on segments whose endpoint supports avoid one or more
of `e,f,g`.

The same conclusion applies to any union of off-`T` pieces whose union with
`{x}` is connected and meets `T` only at `x`.

## 3. Two contacts on the missed clean segment

### Corollary 3.1 (ordered `T_ef` contacts)

Let `X` satisfy (1.2).  Suppose `X` is adjacent to `g` and to two distinct
vertices `p,q` of `T_ef`.  After ordering them as

\[
                              e\,T_{ef}\,p\,T_{ef}\,q\,T_{ef}\,f,
                                                               \tag{3.1}
\]

where either contact may be an endpoint, `G` contains a `K_7` minor.

#### Proof

Use the arms `eT_ef p`, `fT_ef q`, and `{g}`.  They are pairwise disjoint,
so Theorem 1.1 applies.  \(\square\)

The symmetric statement holds with `f` and `g` interchanged: adjacency to
`f` together with two ordered contacts on `T_eg` is terminal.

## 4. Exact residue

The audited
[multipartite guardrail](../barriers/hc7_atomic_h0_multipartite_bridge_guardrail.md)
has exactly the deficient pattern left by Corollary 2.1.  Its subdivision
`T` replaces `ef` by `e-p-f`, takes `X={x}`, and adds the contacts `xp,xg`.
Thus the clean-incidence edges contributed by these contacts are

\[
                              ep,\qquad fp,\qquad gg,
\]

and the clean attachment graph has matching number two.  A second
**distinct** contact anywhere on `T_ef` would trigger Corollary 3.1.

For a component bridge, `M_X` may also contain edges arising from other
vertices of `T` adjacent directly to `x`, not only from the bridge's own
attachments.  The bound \(\nu(M_X)\le2\) nevertheless passes to the
bipartite subgraph induced by the bridge attachments, which is the only
direction used in the component-bridge conclusion.

The proved conclusion is deliberately narrower than the outstanding bridge
theorem.  Seven-connectivity supplies many attachments to each nontrivial
component bridge, but it does not force three distinct clean-supported
attachments, let alone a saturating matching.  When (2.4) holds, this note
does not yet produce an order-seven separator, a planar two-vertex deletion,
or a smaller anti-neighbourhood component carrying the named proper-minor
response.  It also does not align an arbitrary normalized dominating
`K_5` model with the three clean roots.  The remaining task is to combine
the Hall-deficient clean attachment pattern with quadrant confinement and
the contraction-critical colouring responses.
