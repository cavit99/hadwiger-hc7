# Independent audit of the rooted persistent model-edge theorem

**Verdict:** GREEN for Theorems 2.1 and 2.2, Corollary 2.3, and the stated
`t=7` specialization, under the exact hypotheses in the source.

**Audited source:** `hc7_rooted_persistent_model_edge.md`, SHA-256

```text
05548e80573736ea1f56b23db7372b2487eacdcda32dd5633a0af63be65212b7
```

After the GREEN audit, only the source status line was changed to link this
audit.  The mathematical statement and proof are byte-for-byte unchanged;
the audit is repinned to the resulting source hash above.

This is a separate internal mathematical audit, not external peer review.
It supersedes the audit of the earlier qualitative revision.  A transient
source revision whose hash began `d4d9` was not audited or promoted and is
not covered by this verdict.

The audit independently reconstructed the component transfer, the
quantitative incident-edge count, the protected-singleton transfer, and
the component bound.  It also tested the dangerous repeated-label and
small-`t` cases described below.  No counterexample to the statements at
the pinned hash was found.

## 1. Root components and persistent internal edges

Let `Z_1,...,Z_k` be the components of `G[R-v]`, and let `q_i` count the
edges from `v` into `Z_i`.  Connectedness of `G[R]` gives `q_i>=1`.

If `q_i>=2`, deletion of any selected `v-Z_i` edge leaves another such
edge and a path within the connected component `Z_i`.  Thus `G[R]`
remains connected.  No inter-branch-set adjacency is affected, so all
`q_i` edges are deletion-persistent.

If `q_i=1`, its unique `v-Z_i` edge is a bridge of `G[R]` and is not
deletion-persistent.  Hence, with

\[
 I_0=\{i:q_i=1\},\qquad I_1=\{i:q_i\ge2\},
 \qquad k_j=|I_j|,
\]

the number of persistent internal incident edges is exactly

\[
                 p_{\rm int}=\sum_{i\in I_1}q_i,
\]

and the internal degree of `v` is `k_0+p_int`.  This also covers
`R={v}`, when all three quantities vanish.

## 2. Component transfer and monopoly sets

The monopoly sets of distinct root components are pairwise disjoint.  A
required label has one nonempty set of root-side contact vertices, which
cannot be contained in two disjoint components of `R-v`.

For any component `Z`, the replacement root set `R'=R-Z` is connected:
it contains `v`, and every remaining component of `R-v` has at least one
edge to `v`.  The proof that `|Lambda(Z)|>=2` is valid even when `Z` has
several attachments to `v`.

### Empty monopoly set

If `Z` has no foreign neighbour, spanning and the fact that every
`Z-(R-Z)` edge ends at `v` imply that deleting `v` separates `Z` from the
nonempty foreign branch sets.  This contradicts `t`-connectivity.

Choose a foreign bag `B_y` met by `Z` and move all of `Z` from `R` into
`B_y`.  The new root remains connected, and `B_y union Z` is connected
through the selected contact.  Since no required root label is
monopolized by `Z`, every required root-to-foreign adjacency has an old
contact with endpoint in `R'`.  Every old foreign-to-foreign adjacency
survives by inclusion.  Any `v-Z` edge supplies the new root-to-`B_y`
contact if that is the missing label pair.

If the transfer creates an edge across the unique nonedge of `F`, the
replacement sets are a `K_t`-minor model.  Otherwise they form a rooted
spanning `F`-model with strictly smaller root branch set.  Both outcomes
contradict the respective hypothesis or extremal choice.

### Singleton monopoly set

If `Lambda(Z)={x}`, move `Z` into `B_x`.  Any `v-Z` edge supplies the one
required root contact lost by removing `Z` from `R`; every other required
root contact and all old foreign-to-foreign contacts survive.  The same
`K_t`-model-or-smaller-root dichotomy applies.

Consequently, for every root component,

\[
                              |\Lambda(Z_i)|\ge2.
\]

The surgery does not assume singleton foreign bags.  It moves a whole
connected set, retains every old foreign bag as a subset, and explicitly
accounts for every root adjacency that can be lost.

## 3. External incident edges and distinct labels

Write `ell` for the number of nonpersistent external edges at `v` and
`p_ext` for the number of persistent external edges.  Then

\[
                              p=p_{\rm int}+p_{\rm ext}.
\]

Every external neighbour lies in a required foreign bag.  An edge into
the sole nonneighbour bag of the root label would itself complete the
displayed model to a `K_t` model.

A nonpersistent external edge `vb`, with `b in B_x`, is the sole
`R-B_x` edge; otherwise deleting it leaves another required contact and
does not affect either bag's connectivity.  Therefore:

- distinct nonpersistent external edges have distinct labels;
- there are exactly `ell` private required labels; and
- each private label has complete root-side contact set `{v}`.

No private label belongs to a component monopoly set.

Let `Q` be the set of labels containing an endpoint of a persistent
external edge, and put `q=|Q|`.  A label in `Q` is required and has `v` as
a root-side contact, so it belongs to no monopoly set.  It is not private:
persistence of a cross-edge requires a second `R-B_y` edge after deletion.

Repeated persistent external edges are handled correctly.  Several such
edges may use one label, so generally `q<p_ext`; the proof counts only the
distinct labels.  Conversely, if two external edges at `v` use the same
label, deleting either leaves the other, so neither can be nonpersistent.
Thus the private labels and `Q` are disjoint.

Together with the pairwise disjoint monopoly sets, these are disjoint
subsets of the `m` required labels.  Hence

\[
                   2(k_0+k_1)+\ell+q\le m.              \tag{A.1}
\]

## 4. Quantitative degree contradiction

Spanning accounts for every neighbour of `v`.  Its internal degree is
`k_0+p_int`, and its external degree is `ell+p_ext`.  Therefore

\[
                    d_G(v)=k_0+\ell+p.                  \tag{A.2}
\]

Assume, as in the source, that `p<=t-m`.

If `p=0`, then `k_1=0` and `q=0`.  Equations (A.1)--(A.2) give

\[
                  d_G(v)=k_0+\ell
                    \le 2k_0+\ell\le m\le t-1,
\]

contradicting `d_G(v)>=t`.

If `p>0`, then either a persistent internal edge exists, so `k_1>0`, or
a persistent external edge exists, so `q>0`.  In particular,

\[
                         k_0+2k_1+q\ge1.
\]

Using (A.1) in (A.2),

\[
\begin{aligned}
d_G(v)
  &=k_0+\ell+p\\
  &\le m+p-(k_0+2k_1+q)\\
  &\le m+p-1\\
  &\le t-1,
\end{aligned}
\]

again contradicting `t`-connectivity.  Therefore

\[
                              p\ge t-m+1.
\]

When the root label is not an endpoint of the missing edge, `m=t-1` and
the bound is two.  When it is an endpoint, `m=t-2` and the bound is three.
The arithmetic and the strict integer step are correct.

## 5. Protected-singleton theorem

Fix the required label `a`, with `B_a={x}` and edge `xv`.  For every root
component `Z`, the label `a` is not in `Lambda(Z)`: its root-side contact
set contains `v`, which is outside `Z`.

If `Lambda(Z)` is a singleton, its label is therefore different from `a`,
so transferring `Z` leaves `B_a={x}` untouched.

If `Lambda(Z)` is empty and `Z` meets no foreign bag other than `B_a`,
then spanning gives

\[
                              N_G(Z)\subseteq\{v,x\}.
\]

Deleting `v,x` separates the nonempty set `Z` from another nonempty
foreign bag.  Such a bag exists at `t=3` as well: among the two foreign
labels, only one is `a`.  Thus `{v,x}` is a separator of order at most two,
contradicting `t`-connectivity for all `t>=3`.

Hence an empty-monopoly component meets some `B_y` with `y!=a`, and the
transfer into that bag preserves the singleton, every label, and the
literal required edge `xv`.  The quantitative label and degree count from
Sections 3--4 is otherwise unchanged.  Theorem 2.2 therefore has the same
lower bound `p>=t-m+1` within the protected class.

## 6. Component bound

In the protected class, the label `a` belongs to no monopoly set.  The
pairwise disjoint monopoly sets, each of order at least two, are therefore
subsets of the `m-1` labels in `Gamma_F(r)-{a}`.  Their number is exactly
the number of components of `G[R]-v`.  Consequently,

\[
             c(G[R]-v)\le\left\lfloor\frac{m-1}{2}\right\rfloor.
\]

For `t=7` with the root label not an endpoint of the missing edge,
`m=6`, and the right side is two.  Corollary 2.3 is correct.

## 7. Adversarial cases checked

1. **Several internal attachments to one component.**  Every such edge is
   persistent; counting all `q_i` of them in `p_int` gives the exact
   internal degree.
2. **Repeated persistent edges at one foreign label.**  They contribute
   several edges to `p_ext` but only one label to `q`; the proof never
   overcounts them in (A.1).
3. **A persistent and a purported nonpersistent edge at one label.**  This
   cannot occur: either edge remaining after deletion preserves the same
   required bag adjacency.
4. **The singleton root bag.**  Then `k_0=k_1=p_int=0`; the external-label
   count and the `p=0` branch still force the stated bound.
5. **Root at either type of label.**  The proof uses only `m`; substituting
   `m=t-1` or `m=t-2` gives the claimed two- or three-edge conclusion.
6. **The protected edge among the persistent edges.**  This is allowed.
   Since Theorem 2.2 supplies at least two distinct persistent edges, the
   `t=7` specialization can still choose one distinct from `g=xv`.
7. **The `t=3` protected transfer.**  A second foreign bag still exists,
   so the order-two separator contradiction is valid.
8. **Nontrivial branch sets.**  The component transfer preserves their
   connectivity and all old contacts by inclusion; no singleton-bag
   assumption is used except for the explicitly protected `B_a={x}`.

## 8. Exact trust boundary

Theorems 2.1 and 2.2 give multiple deletion-persistent edges in one
reselected labelled spanning model.  In the protected theorem the original
singleton and the critical model edge `g=xv` remain present.  Because at
least two persistent edges are supplied, one can choose a persistent edge
`f` distinct from `g`, whether or not `g` itself is persistent.

The results do not put `f` in a prescribed shore or list-critical kernel,
preserve a boundary colouring, identify palette colours with branch-set
labels, construct a `K_t` minor by themselves, or supply a
colour-compatible separation.  The internal-versus-boundary-crossing fork
in the source correctly leaves this side-alignment problem open.

Subject to this trust boundary, no gap was found.
