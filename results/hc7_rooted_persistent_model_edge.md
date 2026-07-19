# A rooted spanning near-clique model has persistent incident edges

**Status:** written proof; separate internal audit GREEN in
[`hc7_rooted_persistent_model_edge_audit.md`](hc7_rooted_persistent_model_edge_audit.md).

This note proves a parameter-uniform re-selection theorem for spanning
labelled `K_t`-minus-one-edge minor models.  Fix a host vertex and retain
the label of the branch set containing it.  After minimizing that rooted
branch set, at least `t-m+1` distinct edges incident with the fixed vertex
can each be deleted while the same `t` branch sets still form the labelled
near-clique model, where `m` is the number of required foreign labels at
the rooted label.  This gives at least two such edges in every case and at
least three when the root label is an end of the missing edge.

The proof is a direct branch-set reassignment.  Every component of the
rooted branch set after deleting the root monopolizes at least two of the
`m` required foreign labels.  Nonpersistent external edges consume
distinct private labels, while persistent external edges consume a
disjoint set of labels.  Combining this label count with the multiplicity
of the root attachments forces more than `t-m` persistent incident edges.

## 1. Labelled models and persistence

Fix an integer `t>=3`.  Let `F` be the graph obtained from `K_t` by
deleting one edge.  Its vertices are called **labels**.  Fix a label
`r in V(F)` and a vertex `v` of a graph `G`.

A **spanning labelled `F`-model rooted at `(r,v)`** is a family

\[
                        \mathcal M=(B_x:x\in V(F))       \tag{1.1}
\]

of pairwise disjoint nonempty connected vertex sets which partition
`V(G)`, such that

\[
             xy\in E(F)\quad\Longrightarrow\quad
             E_G(B_x,B_y)\ne\varnothing,                \tag{1.2}
\]

and `v in B_r`.  No adjacency is required for the unique nonedge of `F`.
Under the `K_t`-minor exclusion in Theorem 2.1, the two branch sets at
that nonedge are in fact anticomplete: any edge between them would complete
the displayed model to a `K_t`-minor model.
Write

\[
                              R=B_r                     \tag{1.3}
\]

for the rooted branch set, and put

\[
     \Gamma_F(r)=\{x\in V(F)-\{r\}:rx\in E(F)\},
     \qquad m=|\Gamma_F(r)|.                            \tag{1.4}
\]

Thus `m=t-2` if `r` is an end of the deleted edge of `F`, and `m=t-1`
otherwise.  In particular,

\[
                              m\le t-1.                  \tag{1.5}
\]

An edge `e` of `G` is **deletion-persistent for `mathcal M`** if the same
`t` vertex sets in (1.1) remain a spanning labelled `F`-model in `G-e`.
For an edge internal to a branch set, this means in particular that the
branch set remains connected.  For an edge between branch sets whose
labels are adjacent in `F`, another edge must still realize that required
branch-set adjacency.

## 2. The rooted persistence theorem

### Theorem 2.1 (rooted incident-edge persistence)

Let `G` be a `t`-connected graph with no `K_t` minor.  Suppose there is at
least one spanning labelled `F`-model rooted at `(r,v)`.  Among all such
models, choose `mathcal M` so that its rooted branch set `R=B_r` has
minimum order.

Then at least

\[
                              t-m+1                     \tag{2.1}
\]

distinct edges of `G` incident with `v` are deletion-persistent for
`mathcal M`.  In particular there are at least two, and there are at least
three if `r` is an end of the missing edge of `F`.

Consequently, given any spanning labelled `K_t`-minus-one-edge model and
any prescribed vertex `v`, one may retain the label of the branch set
which contains `v`, reselect a spanning model minimizing that rooted
branch set, and obtain at least two distinct deletion-persistent model
edges incident with `v`.

#### Proof

Let `p` be the number of deletion-persistent edges incident with `v`.
Assume for a contradiction that

\[
                              p\le t-m.                  \tag{2.2}
\]

### Step 1: the components of `R-v`

Let

\[
                        Z_1,\ldots,Z_k                  \tag{2.3}
\]

be the components of `G[R-v]`, and let `q_i` be the number of edges from
`v` to `Z_i`.  Connectedness of `G[R]` gives `q_i>=1`.

Partition the indices into

\[
 I_0=\{i:q_i=1\},\qquad I_1=\{i:q_i\ge2\},
 \qquad k_0=|I_0|,\quad k_1=|I_1|.                     \tag{2.4}
\]

If `i in I_1`, every one of the `q_i` edges from `v` to `Z_i` is a
nonbridge of `G[R]`.  For any selected edge `vz`, another `v-Z_i` edge
together with a path inside the connected set `Z_i` keeps `v` joined to
`Z_i` after `vz` is deleted.  Deleting `vz` changes no inter-branch-set
adjacency, so all `q_i` of these edges are deletion-persistent.

Put

\[
                         p_{\rm int}=\sum_{i\in I_1}q_i. \tag{2.5}
\]

The internal degree of `v` is `k_0+p_int`.  The `k_0` edges belonging to
indices in `I_0` are bridges of `G[R]` and are not deletion-persistent.
This notation also covers `R={v}`, when `k_0=k_1=p_int=0`.

### Step 2: labels monopolized by one component

For a component `Z` of `R-v`, define its **monopoly set**

\[
 \Lambda(Z)=
 \bigl\{x\in\Gamma_F(r):
       N_G(B_x)\cap R\ne\varnothing
       \text{ and }N_G(B_x)\cap R\subseteq Z\bigr\}.   \tag{2.6}
\]

For \(x\in\Gamma_F(r)\), the first condition in (2.6) is automatic from
the model.  It is displayed to make the definition literal.  Thus
\(x\in\Lambda(Z)\) exactly when every endpoint in `R` of every `R-B_x`
edge lies in `Z`.  Removing `Z` from `R` would lose the required
adjacency to `B_x` unless `Z` itself were reassigned to `B_x`.

The sets \(\Lambda(Z_i)\), over all components in (2.3), are pairwise
disjoint.  If
a label `x` belonged to both \(\Lambda(Z_i)\) and \(\Lambda(Z_j)\), the
nonempty set \(N_G(B_x)\cap R\) would be contained in the disjoint sets
`Z_i` and `Z_j`, which is impossible.

We claim that

\[
                          |\Lambda(Z_i)|\ge2
                          \quad(1\le i\le k_0+k_1).      \tag{2.7}
\]

Fix a component `Z=Z_i` and put `R'=R-Z`.  This is nonempty because it
contains `v`.  It is connected: it consists of `v` together with all the
other components of `R-v`, each joined to `v` by at least one edge.

First suppose \(\Lambda(Z)=\varnothing\).  The set `Z` has a neighbour in some
foreign branch set `B_y`.  Otherwise, because the model is spanning and
every edge from `Z` to `R-Z` has endpoint `v`, the vertex `v` would
separate the nonempty set `Z` from all `t-1` foreign branch sets.
That would make `v` a cutvertex of `G`, contrary to `t`-connectivity.

Choose a foreign label `y` met by `Z` and replace

\[
                         R\longmapsto R'=R-Z,
             \qquad B_y\longmapsto B_y'=B_y\cup Z,     \tag{2.8}
\]

leaving the other `t-2` branch sets unchanged.  The set `B_y'` is
connected through the chosen `Z-B_y` edge, and `R'` is connected as
observed above.  The `t` sets remain nonempty, disjoint, and spanning.

Every required adjacency from `R'` to a foreign branch set remains: no
required label is monopolized by `Z`.  In particular, if `ry in E(F)`,
then `R'` still has an old edge to `B_y subseteq B_y'`.  If `ry notin
E(F)`, then any edge from `v` to `Z` now joins `R'` to `B_y'` and repairs
the missing pair.  All required adjacencies among foreign branch
sets survive because each old branch set is contained in its replacement.

If the enlargement creates an edge between the two labels of the unique
nonedge of `F`, the `t` replacement sets form a `K_t`-minor model.
Otherwise they form a spanning labelled `F`-model rooted at `(r,v)` with
the strictly smaller rooted branch set `R'`.  The first outcome contradicts
the hypothesis that `G` has no `K_t` minor, and the second contradicts the
choice of `R`.

Now suppose \(\Lambda(Z)=\{x\}\).  The definition of monopoly gives an edge
between `Z` and `B_x`.  Apply (2.8) with `y=x`.  Any edge from `v` to `Z`
supplies the required adjacency between `R'` and
`B_x'=B_x union Z`.  For every other required label `h`, the fact that
\(h\notin\Lambda(Z)\) means that `R'` retains an old edge to `B_h`.  Again
all foreign-foreign adjacencies survive.  As before, either the
reassignment repairs the sole missing pair and gives a `K_t`-minor model,
or it gives a smaller spanning labelled `F`-model rooted at `(r,v)`.
Both outcomes are impossible.  This proves (2.7).

### Step 3: labels used by external edges at `v`

Let `ell` be the number of nonpersistent edges from `v` to foreign branch
sets, and let `p_ext` be the number of persistent such edges.  Thus

\[
                             p=p_{\rm int}+p_{\rm ext}. \tag{2.9}
\]

Consider a nonpersistent edge `vb` with `b in B_x`.  The label `x`
belongs to \(\Gamma_F(r)\): if `rx` were the unique nonedge of `F`, the
displayed branch sets would already form a `K_t`-minor model.  Moreover,
`vb` is the sole edge between `R` and `B_x`; otherwise deleting `vb` would
leave both branch sets connected and retain their required adjacency.
Call `x` a **private label at `v`**.

Distinct nonpersistent external edges give distinct private labels, since
two `v-B_x` edges for the same label would prevent either edge from being
the sole `R-B_x` edge.  There are therefore exactly `ell` private labels
at `v`, and for each one

\[
                          N_G(B_x)\cap R=\{v\}.          \tag{2.10}
\]

No private label at `v` belongs to any \(\Lambda(Z_i)\), because every
`Z_i` is a subset of `R-v`.

Let `Q` be the set of foreign labels which contain an endpoint of a
persistent external edge at `v`, and put `q=|Q|`.  Every member of `Q`
belongs to \(\Gamma_F(r)\), again by `K_t`-minor exclusion.  A label in
`Q` is not private: if `vb` is persistent with `b in B_y`, some second
edge joins `R` to `B_y`, since deleting a cross-edge does not affect the
connectivity of either branch set.  It is also in no monopoly set, because
the persistent edge itself puts the contact vertex `v` in
\(N_G(B_y)\cap R\), whereas every `Z_i` lies in `R-v`.

Repeated external edges cause no overcount.  If two or more external
edges at `v` have their other endpoint in the same `B_y`, then every one
of those edges is persistent, because another such edge retains the
`R-B_y` adjacency after deletion.  More generally, once one external
edge at label `y` is persistent, no external edge at the same label is
private.  Thus the `ell` private labels and the `q` labels in `Q` are
disjoint, although `q` may be strictly smaller than `p_ext`.

Together with the pairwise disjoint monopoly sets from Step 2, these are
disjoint subsets of the `m` required foreign labels.  By (2.7),

\[
                   2(k_0+k_1)+\ell+q\le m.             \tag{2.11}
\]

### Step 4: the degree contradiction

Because the model is spanning, every neighbour of `v` lies either in `R`
or in one of the `t-1` foreign branch sets.  Step 1 and (2.9) give the
exact identity

\[
                            d_G(v)=k_0+\ell+p.           \tag{2.12}
\]

If `p=0`, then (2.11) and (2.12) give

\[
                            d_G(v)=k_0+\ell\le m\le t-1,
\]

contrary to `t`-connectivity.  Suppose instead that `p>0`.  Then either
`k_1>0`, because there is a persistent internal edge, or `q>0`, because
there is a persistent external edge.  Hence

\[
                         k_0+2k_1+q\ge1.                \tag{2.13}
\]

Using (2.11) in (2.12), and then the contradictory bound (2.2), gives

\[
\begin{aligned}
 d_G(v)
   &=k_0+\ell+p\\
   &\le m+p-(k_0+2k_1+q)\\
   &\le m+p-1\\
   &\le t-1.
\end{aligned}                                           \tag{2.14}
\]

This again contradicts `t`-connectivity.  Therefore
`p>=t-m+1`, as claimed.  \(\square\)

### Theorem 2.2 (protected-singleton persistence)

In the setting of Theorem 2.1, fix a required neighbour label

\[
                          a\in\Gamma_F(r)                \tag{2.15}
\]

and a vertex `x` adjacent to `v`.  Suppose the class of spanning labelled
`F`-models satisfying

\[
                         v\in B_r,\qquad B_a=\{x\}      \tag{2.16}
\]

is nonempty.  Among only the models in this protected-singleton class,
choose `mathcal M` so that `R=B_r` has minimum order.

Then at least `t-m+1` distinct edges incident with `v` are
deletion-persistent for `mathcal M`.  In particular, the reselected model
still has `B_a={x}` and still contains the prescribed required model edge
`xv`.

#### Proof

Repeat the proof of Theorem 2.1 under the contradictory assumption
`p<=t-m`.  Step 1, the monopoly-set definition, the pairwise disjointness
of the monopoly sets, and the degree count are unchanged.  It remains
only to verify that every branch-set reassignment used to prove (2.7)
stays inside the protected-singleton class (2.16).

Fix a component `Z` of `R-v`.  The label `a` does not belong to
`Lambda(Z)`: the fixed edge `xv`, with `x in B_a` and `v in R-Z`, shows
that

\[
                          v\in N_G(B_a)\cap R
                          \quad\text{and}\quad v\notin Z.       \tag{2.17}
\]

Suppose first that \(\Lambda(Z)=\varnothing\).  There is a foreign branch
set `B_y` with `y!=a` adjacent to `Z`.  Indeed, if no such branch set
existed, spanning and the fact that every `Z-(R-Z)` edge has endpoint `v`
would give

\[
                              N_G(Z)\subseteq\{v,x\}.    \tag{2.18}
\]

The graph `G-{v,x}` would then have `Z` in a component disjoint from every
foreign branch set other than `B_a`.  Such a branch set exists because
`t>=3`, and it is nonempty.  Hence `{v,x}` would be a separator of order
at most two, contradicting `t`-connectivity.

Choose the label `y!=a` just obtained and perform the reassignment (2.8).
The singleton branch set `B_a={x}` is untouched.  The vertex `v` remains
in `R'=R-Z`, so the prescribed edge `xv` still realizes the required
`R'-B_a` adjacency.  The verification of every other branch-set adjacency
is exactly the one in the empty-monopoly case of Theorem 2.1.  Thus the
reassignment either gives a `K_t`-minor model or a member of the protected
class with smaller rooted branch set.

Now suppose \(\Lambda(Z)=\{y\}\).  Equation (2.17) gives `y!=a`.  Move
`Z` into `B_y` exactly as in Theorem 2.1.  Again `B_a={x}`, `v in R'`, and
the edge `xv` are unchanged, while any `v-Z` edge restores the
required `R'-B_y'` adjacency.  The result is either a `K_t`-minor model or
a member of the protected class with smaller `R`.

Therefore both \(|\Lambda(Z)|=0\) and \(|\Lambda(Z)|=1\) contradict the
choice of `mathcal M`, so (2.7) holds for the protected minimum as well.
Steps 3 and 4 now give the same contradiction to `p<=t-m`.  Consequently
at least `t-m+1` distinct incident edges are deletion-persistent, and the
singleton branch set and prescribed edge remain present.  \(\square\)

### Corollary 2.3 (protected root-bag component bound)

Under the hypotheses and extremal choice of Theorem 2.2,

\[
               c(G[R]-v)\le\left\lfloor\frac{m-1}{2}\right\rfloor.
                                                               \tag{2.19}
\]

In particular, for `t=7` when `r` is not an end of the missing edge and
therefore `m=6`, the graph `G[R]-v` has at most two components.

#### Proof

Equation (2.17) shows that the protected label `a` belongs to none of the
pairwise disjoint monopoly sets \(\Lambda(Z_i)\).  By (2.7), each such
set has order at least two.  They are therefore pairwise disjoint subsets
of the `m-1` labels in \(\Gamma_F(r)-\{a\}\).  Since their number is
exactly the number of components of `G[R]-v`, (2.19) follows.  \(\square\)

## 3. What the theorem does and does not align

The theorem is rooted and label-preserving.  The vertex `v` is fixed
before the model is reselected, its branch label `r` is retained, and the
persistent edge is incident with that literal vertex.  The proof changes
only the allocation of a whole component of `R-v`; it never identifies
vertices or appeals to an unlabelled model.

Each persistent edge can have either of two forms:

1. an internal nonbridge of the rooted branch set; or
2. an edge from the root to a foreign branch set whose required
   branch-set adjacency has another realizing edge.

In particular, the theorem does **not** force the persistent edge to lie
inside a prescribed shore, list-critical kernel, branch set other than
`R`, or specified separation side.  It does not preserve a previously
chosen boundary colouring when the model is reselected.  It does not
identify palette colours with model labels, construct a `K_t` minor by
itself, or supply a colour-compatible separation.

The hypotheses are essential to the count as stated.  Spanning is used to
account for every neighbour of `v`; `t`-connectivity supplies both the
cutvertex contradiction and `d_G(v)>=t`; and `K_t`-minor exclusion rules
out the terminal outcome of the reassignment.

## 4. Specialization to `t=7` and the interface fork

For `t=7`, suppose a critical edge `g=xv` has already been selected and
that a spanning labelled `K_7`-minus-one-edge model has `v` in branch set
`B_r`, has the required neighbouring branch set `B_a={x}`, and therefore
uses `g=xv` as a labelled model edge.  Theorem 2.2 permits the model to be
reselected while preserving both `B_a={x}` and `g=xv`, and it supplies at
least two distinct deletion-persistent model edges incident with `v`.
Choose one of them, say `f=vu`, distinct from `g`.  This is possible
whether or not `g` itself is persistent.  Thus the critical model edge
`g` and the distinct deletion-persistent model edge `f` share the literal
endpoint `v` without losing the critical singleton branch set.

Relative to a specified separation, there is an exact fork.

1. If `u` lies in the same open shore as `v`, then `f=vu` is an internal
   deletion-persistent edge and can be tested against a list-critical
   obstruction on that shore.
2. If `u` lies on the boundary or in the opposite side, then `f` is a
   boundary-crossing persistent edge.  The theorem supplies the desired
   common endpoint but does not put `f` inside the list-critical kernel.

Thus side alignment remains: the persistent incident edge may cross the
specified boundary rather than lie in the list-critical shore containing
the desired obstruction.  That issue requires additional colouring or
separation information and is not asserted here.
