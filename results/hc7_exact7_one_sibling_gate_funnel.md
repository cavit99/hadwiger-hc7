# Exact-seven one-sibling gate funnel

**Status:** proved and independently audited.  The parameter-uniform Hall
principle, paired-state funnel, and finite barrier certificate are GREEN.

## 1. Normalized input

Let `G` lie in the hypothetical minimal-`HC_7` counterexample kernel.  Use
an actual exact-seven separation

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\}.
\]

Assume that the legally attained boundary state is

\[
 \Pi=\{B_1,B_2,B_3,\{c\}\},
 \qquad B_i=\{a_i,t_i\},                         \tag{1.1}
\]

where each `B_i` is independent, every two different `B_i` have a literal
edge between them, and `c` has a literal neighbour in every `B_i`.  In the
rich shore let `C` be an `S`-full component of `G[R]` and let `Q` be a connected
`S`-full packet disjoint from `C`.

Let `X={x_1,x_2,x_3}` be a three-cut of the three-connected graph `C`, and
suppose that `C-X` has exactly two components `K,J`.  Normalize

\[
 A=N_S(K)=\{c,a_1,a_2,a_3\},
 \qquad B=N_S(J).                                  \tag{1.2}
\]

Every member of `X` has a neighbour in each of `K,J`, and
`|B|\ge4`.  These facts are the audited one-sibling outcome of the
three-gate exit theorem.

For `i in [3]` put

\[
 U_i=N_X(t_i),
 \qquad
 V_i=\{x\in X:B_i-B\subseteq N_S(x)\}.             \tag{1.3}
\]

Thus `K union {x}` funds duty `B_i` exactly when `x in U_i`, while
`J union {y}` funds duty `B_j` whenever `y in V_j`.  If `B_j subseteq B`,
then `V_j=X`.

## 2. The literal two-carrier test

### Lemma 2.1

If there are distinct duties `i!=j` and distinct gate vertices

\[
                         x\in U_i,\qquad y\in V_j,       \tag{2.1}
\]

then the attained state `Pi` reflects across the rich shore and `G` is
six-colourable.

### Proof

The sets

\[
                         K\cup\{x\},\qquad J\cup\{y\}   \tag{2.2}
\]

are disjoint and connected.  They are adjacent through the literal edge
from `x` to `J`.  By (1.2)--(1.3), the first contacts both members of
`B_i`, and the second contacts both members of `B_j`.  Contract these two
carriers together with their assigned boundary blocks.  The full packet
`Q` funds the third block.

The three contracted representatives are pairwise adjacent because every
two distinct blocks in (1.1) have a literal edge.  Each is adjacent to the
retained singleton `c` because `c` has a literal neighbour in its assigned
block.  This is the exact attained-state reflection contraction.  Its
proper-minor six-colouring aligns with the colouring which legally attained
`Pi` on the opposite closed shore, so the two colourings glue.  \(\square\)

The adjacency of the two interior carriers in (2.2) is therefore literal,
although the boundary block edge would already supply the required
representative adjacency.  No palette colour is identified with a gate or
a model label.

## 3. Missing-label Hall matching

Put

\[
                  T=\{t_1,t_2,t_3\},
 \qquad           D=S-(A\cup B)=T-B.                    \tag{3.1}
\]

### Lemma 3.1 (uniform missing-label Hall principle)

Let `G` be `k`-connected and let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=k,
\]

be an actual separation with `L` nonempty.  Let `C` be a component of
`G[R]`, let `X` be a proper subset of `V(C)`, and let `D subseteq S`.
If every edge from `D` into `C` ends in `X`, then the literal incidence
graph between `D` and `X` has a matching saturating `D`.

#### Proof

If Hall fails, choose `U subseteq D` with `|N_X(U)|<|U|` and delete

\[
                         Z=(S-U)\cup N_X(U).
\]

Its order is less than `k`.  The nonempty set `C-X` survives.  It cannot
reach a surviving member of `U`: every `U-C` edge ends in `X`, and every
member of `X` adjacent to `U` was deleted.  It cannot reach `L` directly
or leave through another component of `G[R]`; all possible boundary exits
other than `U` were deleted.  Thus a component meeting `C-X` is separated
from the nonempty far shore `L`, contradicting `k`-connectivity.
\(\square\)

The proper-subset hypothesis supplies a surviving vertex on the component
side after all of `N_X(U)` is deleted.

### Corollary 3.2 (the one-sibling matching)

The literal incidence graph between `D` and `X` has a matching which
saturates `D`.

### Proof

Apply Lemma 3.1 with `k=7`.  Here `X` is a proper subset of `C` because
the two nonempty lobes `K,J` lie in `C-X`.  Equations (1.2) and (3.1) say
that neither lobe has a neighbour in `D`, so every `D-C` edge ends in
`X`.

For completeness, the Hall cut in this instance can also be displayed
directly.

If Hall fails, choose `U subseteq D` with

\[
                           |N_X(U)|<|U|.
\]

Delete

\[
                           Z=(S-U)\cup N_X(U).            \tag{3.2}
\]

Then

\[
                  |Z|=7-|U|+|N_X(U)|\le6.               \tag{3.3}
\]

The surviving literals in `U` have no neighbour in `K` or `J`, by the
definition of `D`, and no neighbour in `X-N_X(U)`, by the definition of
`N_X(U)`.  The component `C` has no edge to the old opposite shore or to
`R-C`.  Consequently a surviving component containing a vertex of `K` is
separated in `G-Z` from the nonempty old opposite shore.  This contradicts
seven-connectivity.  \(\square\)

### Theorem 3.3 (one-sibling two-carrier funnel)

If the attained state does not reflect, then exactly one of the following
two support families contains the one-sibling residue.

1. **Cross-lobe family:**

   \[
                              T\subseteq B.              \tag{3.4}
   \]

2. **Single-missing-duty family:** after permuting the three duties,

   \[
                              B=\{c,a_1,t_2,t_3\}.       \tag{3.5}
   \]

Moreover every survivor satisfies the exact cross-incidence obstruction

\[
 \text{for all }i\ne j,\ x\in U_i,\ y\in V_j,
 \qquad x=y.                                             \tag{3.6}
\]

In family (3.5), define the complementary endpoint `bar r_i` by writing

\[
 B=\{c,r_1,r_2,r_3\},\qquad r_i\in B_i,
 \qquad \bar r_i=B_i-\{r_i\},
\]

and put `W_i=N_X(bar r_i)`.  Here `r_1=a_1` and
`r_2=t_2,r_3=t_3`, so `W_1=U_1`.  Then `U_1` is nonempty and one of the
following sharper alternatives holds:

* every set among `U_2,U_3,W_2,W_3` is empty, while `U_1=W_1` may be an
  arbitrary nonempty subset of `X`; or
* there is one literal `z in X` such that every nonempty set among

  \[
                       U_1,U_2,U_3,W_1,W_2,W_3           \tag{3.7}
  \]

  is exactly `\{z\}`.

### Proof

First suppose that `J` funds some duty `B_j`.  If `D` were nonempty, take
`t_i in D`.  Necessarily `i!=j`.  Corollary 3.2 supplies
`x in N_X(t_i)=U_i`, while `V_j=X`; choose `y in X-{x}`.  Lemma 2.1
reflects `Pi`, a contradiction.  Hence `D` is empty and (3.4) holds.

Now suppose that `J` funds no duty.  Since `|B|>=4`, while `B` contains at
most one member of each independent pair `B_i`, necessarily

\[
                 B=\{c\}\cup\{r_i:i\in[3]\},
                 \qquad r_i\in B_i.                     \tag{3.8}
\]

The set `D` consists precisely of those `t_i` for which `r_i=a_i`.
If `|D|>=2`, Corollary 3.2 gives distinct matched vertices
`x_i in N_X(t_i)` and `x_j in N_X(t_j)` for two different members of
`D`.  The carriers

\[
                         K\cup\{x_i\},\qquad
                         J\cup\{x_j\}
\]

fund `B_i,B_j`, respectively, and Lemma 2.1 reflects `Pi`.  Thus
`|D|<=1`.  When `D` is empty, (3.8) says `T subseteq B`, which is family
(3.4).  When `|D|=1`, relabel to obtain (3.5).

Condition (3.6) is the contrapositive of Lemma 2.1.  In family (3.5),
`U_1=W_1` is nonempty by Corollary 3.2.  Moreover `V_i=W_i` throughout
this dutyless family.  If any other set in (3.7) is
nonempty, apply (3.6) once with index `1` on the `U` side and once with
index `1` on the `W` side.  Every element of that set and every element of
`U_1` must be the same literal vertex `z`; hence both sets are the
singleton `\{z\}`.  Repeating this comparison for each nonempty set proves
the second alternative.  If no other set is nonempty, the first alternative
holds.  \(\square\)

## 4. Extra constraints inside the cross-lobe family

Let

\[
                         F=\{i:B_i\subseteq B\}.
\]

If `F` is nonempty, (3.6) gives the following useful normalization:

* if `F={j}`, then `U_i` is empty for every `i!=j`;
* if `|F|>=2`, then every `U_i` is empty.

Indeed `V_j=X` for every `j in F`, so any `x in U_i` with `i!=j` can be
paired with a different `y in X` and invokes Lemma 2.1.

This does not close (3.4).  It says precisely why the next mechanism must
split the complementary `A`- and `T`-portals inside `K-X-J`, or regenerate
a labelled near-`K_7` model.  Mere gate adjacency is exhausted.

## 5. Sharp static-quotient barrier

These static incidences, even together with a triangle gate and a
three-connected lobe quotient, do not force a `K_7` minor.  The following
fourteen-vertex graph satisfies them and has no `K_7` minor.

Use vertices

```text
c,a1,t1,a2,t2,a3,t3,x1,x2,x3,k,j,p,q.
```

The structural edges are:

* `p,q` are complete to `S` and nonadjacent;
* `k,j` are complete to `X` and nonadjacent;
* `N_S(k)=A` and `N_S(j)=T union {a1}`;
* `X` is a triangle; and
* the retained boundary edges are

  ```text
  a1-a2, a1-a3, a1-c, a2-c, a2-t3, a3-c.
  ```

The three paired blocks are independent, `c` sees each block, every two
blocks have a literal edge, and the lobe quotient on
`{k,j,x1,x2,x3}` is `K_5-kj`, hence is three-connected.  The graph6
string is

```text
MeB?_?@?]jl]~_~_?
```

Nevertheless the elimination order

\[
 t_1,t_2,t_3,x_1,x_2,x_3,a_3,c,a_1,a_2,k,j,p,q
\]

has filled later-neighbourhood orders

\[
 3,3,4,4,3,2,5,5,5,4,3,2,1,0.
\]

Thus its treewidth is at most five.  Since treewidth is minor-monotone and
`tw(K_7)=6`, it has no `K_7` minor.

This is a falsifier only for the **static contracted quotient**.  It is not
claimed to be seven-connected, contraction-critical, or a counterexample
to `HC_7`.  Its role is exact: even a literal triangle gate and a
three-connected lobe quotient cannot replace the missing label-faithful
internal two-carrier split or an `S1` model-regeneration handoff.

## 6. Exact remaining sub-gap

The one-sibling residue is now confined to:

1. the cross-lobe family `T subseteq N_S(J)`, subject to (3.6) and the
   funded-duty restrictions in Section 4; and
2. the single-missing-duty family (3.5), where all possible second-duty
   gate completions are absent or concentrated at one literal gate vertex.

Closing either family requires an internal portal-distribution theorem,
a legally attained replacement state, or a labelled near-`K_7` / fixed-pair
handoff.  No conclusion about `HC_7` is asserted here.
