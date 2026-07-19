# Independent audit of jointly persistent edges or an exact order-seven separation

**Verdict:** GREEN for the theorem and exact-scope statement at the pinned
source revision below.

**Audited source:** `hc7_joint_persistent_edge_or_exact_seven.md`, SHA-256

```text
b78989355a006501d91c3732e3231e99d85fc01e6558259fdcb6b447d0845fcd
```

After the GREEN audit, only the source status line was changed to link this
audit.  The mathematical statement and proof are unchanged; this audit is
repinned to the resulting source hash above.

**Audited dependency:** `hc7_rooted_persistent_model_edge.md`, SHA-256

```text
05548e80573736ea1f56b23db7372b2487eacdcda32dd5633a0af63be65212b7
```

The dependency changed only in its status line when its GREEN audit was
linked; its mathematical content is the revision checked here.

This is a separate internal mathematical audit, not external peer review.
The audit reconstructed the support-class dichotomy, the protected label
count, both equality cases, and the literal separation.  No unproved
colouring assertion is used.

## 1. Hypotheses and inherited count

The root label `r` is not an endpoint of the missing edge of `F=K_7-e`, so
it has six required foreign neighbours.  The model is minimized inside the
protected-singleton class

\[
                         v\in B_r,\qquad B_a=\{x\},\qquad xv\in E(G).
\]

The protected version of the rooted persistence theorem therefore applies
with `t=7` and `m=6`.  It supplies at least two deletion-persistent edges
incident with `v`, while retaining the labelled branch sets, the singleton
`B_a={x}`, and the required model edge `xv` in the selected model.

For the components `Z_i` of `G[R]-v`, let `q_i` be the number of `v-Z_i`
edges, and put

\[
 I_0=\{i:q_i=1\},\qquad I_1=\{i:q_i\ge2\},
 \qquad k_j=|I_j|.
\]

Let `ell` count the nonpersistent external edges at `v`, let `p` count all
persistent incident edges, and let `q` count the distinct foreign labels
receiving a persistent external edge.  The audited dependency gives

\[
                  2(k_0+k_1)+\ell+q\le6,                 \tag{A.1}
\]

and, because the model is spanning,

\[
                         d_G(v)=k_0+\ell+p.               \tag{A.2}
\]

The protected singleton causes no exception to (A.1): the dependency proves
that it belongs to no monopoly set and that every whole-component transfer
can avoid that branch set.

## 2. Support classes and simultaneous deletion

Every persistent internal edge `vZ_i` has `q_i>=2`; all `q_i` edges into
the same component form one internal support class.  Deleting one such edge
retains another attachment of the connected component `Z_i` to `v`.

Every persistent external edge from `v` into `B_y` has another edge between
`R` and `B_y`; all persistent incident edges using label `y` form one
external support class.  Cross-edge deletion does not affect the
connectivity of either branch set.

The simultaneous-deletion assertions are correct in all three mixed cases.

1. For two different internal classes, one edge remains from `v` to each
   affected component, so `R` remains connected.
2. For an internal and an external class, the first deletion preserves
   connectivity of `R`, while the second leaves a different `R-B_y` edge.
   The surviving cross-edge still has both endpoints in the same connected
   branch sets.
3. For two external labels, each required branch-set adjacency retains its
   own second realizing edge.

Within a single internal class of order at least three, deleting two edges
leaves a third `v-Z_i` attachment.  Within a single external class of order
at least three, deleting two incident edges leaves a third incident edge to
the same foreign branch set.  Thus, if no jointly persistent pair exists,
all persistent incident edges lie in one support class and that class has
exactly two members.  Since at least two persistent edges exist, this gives

\[
                               p=2.                       \tag{A.3}
\]

This inference does not assume that two edges in one two-edge external class
fail jointly: if a further nonincident `R-B_y` edge survived their deletion,
those two edges would already realize the first outcome.  Its absence is a
consequence of assuming that outcome fails.

## 3. The internal equality case is impossible

If the unique support class is internal, then exactly one component has
`q_i>=2`; its class has order two by (A.3).  Hence

\[
                         k_1=1,\qquad q=0.
\]

Equation (A.1) becomes

\[
                         2k_0+\ell\le4.
\]

Using (A.2) and `p=2`,

\[
                         d_G(v)=k_0+\ell+2\le6.
\]

The last inequality is sharp when `k_0=0` and `ell=4`; every positive
`k_0` only lowers the maximum.  It contradicts the minimum-degree
consequence `d_G(v)>=7` of seven-connectivity.  Therefore the surviving
support class cannot be internal.

## 4. The external equality case

If the unique support class is external, there is no persistent internal
edge, so `k_1=0`, and exactly one foreign label receives persistent external
edges, so `q=1`.  Equations (A.1)--(A.3) and `d_G(v)>=7` give

\[
                 2k_0+\ell\le5,
        \qquad   k_0+\ell+2\ge7.                         \tag{A.4}
\]

The second inequality says `k_0+ell>=5`.  Comparing it with the first gives
`k_0<=0`; hence

\[
                 k_0=0,\qquad \ell=5,\qquad d_G(v)=7.   \tag{A.5}
\]

Together with `k_1=0`, this says that `G[R]-v` has no component.  Therefore

\[
                                R=\{v\}.                 \tag{A.6}
\]

At this point every `R-B_y` edge is incident with `v`.  The external support
class has exactly two such edges by (A.3); a third would be a third
persistent incident edge, while any other surviving `R-B_y` edge after
deleting the pair would make the pair jointly persistent.  Thus the proof
does not overlook a nonincident backup contact.

The singleton protection is consistent with the equality case.  Since
`B_a={x}` in a simple graph, the two-edge external support class cannot be
the protected label once `R={v}`; the protected edge `xv` is simply one of
the five private external edges counted by `ell`.  No step moves or enlarges
`B_a`.

## 5. The separator is actual and has order seven

Equation (A.5) gives `|N_G(v)|=7`.  There must be a vertex outside
`N_G[v]`.  If not, `G` would have eight vertices.  Seven-connectivity would
then force every vertex to have degree at least seven, so `G=K_8`, which has
a `K_7` minor.

Define two subgraphs by the vertex sets

\[
                  V(G_1)=N_G[v],\qquad V(G_2)=V(G)-\{v\}.
\]

They cover `G`, their intersection is exactly `N_G(v)`, and there is no edge
between

\[
             V(G_1)-V(G_2)=\{v\}
       \quad\text{and}\quad
             V(G_2)-V(G_1)=V(G)-N_G[v].
\]

Both open sides are nonempty by the preceding paragraph.  Hence this is an
actual separation of order seven, not merely a neighbourhood lower bound.

## 6. Adversarial cases checked

1. **Two persistent edges in different classes.**  Their two functions are
   independent: internal deletion affects only connectivity of `R`, while
   external deletion affects only one required cross-bag adjacency.
2. **Two external incident edges with a nonincident backup.**  Such a backup
   makes the two incident edges jointly persistent, so it is excluded only
   inside the assumed failure of outcome 1.
3. **Several persistent edges at one label.**  Three incident edges leave a
   third after any chosen pair is deleted; the proof counts the label once
   in `q`, so there is no label overcount.
4. **Several internal components.**  Any second component with at least two
   root attachments creates a second support class and hence a jointly
   persistent pair.  Components with one attachment are counted by `k_0`.
5. **The protected singleton label.**  The model minimization and monopoly
   count are exactly those of the protected theorem; the equality case does
   not require transferring that singleton.
6. **A graph of order eight or less.**  Under seven-connectivity, the only
   eight-vertex possibility is `K_8`, and a seven-vertex graph is not
   seven-connected under the standard definition.  Both are incompatible
   with `K_7`-minor exclusion.

## 7. Exact trust boundary

The theorem proves only the following dichotomy for the selected protected
spanning labelled near-clique model:

- two incident edges can be deleted simultaneously while those same branch
  sets remain a labelled `K_7`-minus-one-edge model; or
- the rooted branch set is one degree-seven vertex and its neighbourhood is
  an actual order-seven separator with both open sides nonempty.

The first outcome does **not** assert that the simultaneous two-edge
deletion is a proper minor with a prescribed six-colouring, that either edge
lies in a selected shore or list-critical kernel, or that colours match
branch-set labels.  The second outcome does **not** align the two closed-shore
colourings or produce a common boundary equality partition.  Neither outcome
alone constructs a `K_7` minor or proves `HC_7`.
