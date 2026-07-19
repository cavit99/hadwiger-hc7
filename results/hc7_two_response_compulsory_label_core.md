# Compulsory branch-set labels in two incident-edge colour responses

**Status:** written proof; separate internal audit GREEN in
[`hc7_two_response_compulsory_label_core_audit.md`](hc7_two_response_compulsory_label_core_audit.md).
This note isolates the exact part of an `EP`/`PE` transition that
is visible to literal first-hit labels. It does not prove `HC_7`, produce a
`K_7`-minor model, or show that the common boundary colouring extends
through the intact operated shore.

## 1. Exact-seven centre-placement setting

Let `G` be a graph with `chi(G)=7` and a spanning labelled
`K_7`-minus-one-edge model whose root branch set is the singleton
`\{v\}`. Write `\mathcal L` for the six labels of the other branch sets.
Let

\[
                         e=va,\qquad f=vb
\]

be distinct edges such that `a` belongs to the branch set labelled `A`,
`b` belongs to the branch set labelled `B`, and `A\ne B`. Put

\[
                         H=G-\{e,f\}.
\]

Assume that `H` has two proper six-colourings `\phi,\psi` with signatures

\[
       \phi:(\text{equal},\text{proper}),\qquad
       \psi:(\text{proper},\text{equal})                 \tag{1.1}
\]

on `(e,f)`, and that `\psi` is obtained from `\phi` by interchanging two
colours `\alpha,\beta` on one connected bichromatic component `D`. Assume
the centre placement

\[
                         v\in D,\qquad a,b\notin D,       \tag{1.2}
\]

and name the colours so that

\[
       \phi(v)=\phi(a)=\alpha,\qquad \phi(b)=\beta.       \tag{1.3}
\]

Thus `\psi(v)=\psi(b)=\beta` and `\psi(a)=\alpha`. Finally assume that

\[
                         S=N_G(D),\qquad |S|=7.           \tag{1.4}
\]

The placement and the fact that `D` is a component of the
`\alpha,\beta`-coloured subgraph of `H` give

\[
 S-\{a,b\}\subseteq
 \bigcup_{\theta\notin\{\alpha,\beta\}}\phi^{-1}(\theta),
                                                               \tag{1.5}
\]

and `\phi` and `\psi` agree literally on `S`.  Moreover, all four colours
outside `\{\alpha,\beta\}` occur on `S`.  Indeed, if the
`\alpha`-coloured side of `D` had no neighbour of one such colour
`\theta`, recolouring that independent side with `\theta` would remain
proper and would make both restored edges `va,vb` proper.  This would
six-colour `G`, contrary to `chi(G)=7`.

Let

\[
                 \Theta=[6]-\{\alpha,\beta\}
\]

be the four untouched colours. For each `\theta\in\Theta`, define its
literal boundary-label row

\[
 R_\theta=
 \{L\in\mathcal L:
      S\cap L\cap\phi^{-1}(\theta)\ne\varnothing\}.      \tag{1.6}
\]

The four rows are nonempty by the transition saturation just recalled, and
the same sets are obtained with `\psi` in place of `\phi` because the two
colourings agree on `S`.

The response-specific fifth rows on the boundary are

\[
                         M_\phi=\{B\},\qquad
                         M_\psi=\{A\}.                   \tag{1.7}
\]

Indeed, (1.5) says that `b` is the only `\beta`-coloured boundary vertex
in the `\phi` response and `a` is the only `\alpha`-coloured boundary
vertex in the `\psi` response. The edges `f=vb` and `e=va` make these
literal first hits of the two operated labels from `D`.

A **label allocation** for a family of colour rows is a system of distinct
representatives in `\mathcal L`. This is only a statement about literal
boundary first-hit labels; no palette colour is identified with a
branch-set label.

## 2. Two-response Hall-core lemma

### Theorem 2.1

Exactly one of the following alternatives applies to the four common rows
`(R_\theta:\theta\in\Theta)`.

1. They violate Hall's condition. This Hall defect is identical in the
   `\phi` and `\psi` responses.
2. They satisfy Hall's condition. Let `\mathcal B` be the nonempty family
   of all four-element image sets of their systems of distinct
   representatives:

   \[
   \mathcal B=
   \bigl\{\{s(\theta):\theta\in\Theta\}:
       s:\Theta\longrightarrow\mathcal L\text{ is injective and }
       s(\theta)\in R_\theta\bigr\},                    \tag{2.1}
   \]

   and define the **compulsory-label core**

   \[
                         K=\bigcap_{C\in\mathcal B}C.   \tag{2.2}
   \]

   For every further nonempty row `M\subseteq\mathcal L`, the five-row
   family

   \[
                         (R_\theta:\theta\in\Theta),M   \tag{2.3}
   \]

   has no label allocation if and only if

   \[
                              M\subseteq K.             \tag{2.4}
   \]

   In particular, if both response families obtained by taking
   `M=M_\phi=\{B\}` and `M=M_\psi=\{A\}` fail Hall's condition, then

   \[
                         A,B\in K,\qquad 2\le |K|\le4.  \tag{2.5}
   \]

   Moreover, every `k\in K` has a tight common-row Hall witness: there is
   a nonempty set `I\subseteq\Theta` such that

   \[
                |N(I)|=|I|,
          \qquad |N(I)-\{k\}|=|I|-1,                   \tag{2.6}
   \]

   where `N(I)=\bigcup_{\theta\in I}R_\theta`.

#### Proof

The response invariance of the four rows was proved immediately after
(1.6). Hall's theorem therefore gives alternative 1 simultaneously in
both responses, or makes the family `\mathcal B` in (2.1) nonempty.

Assume the latter. The five-row family in (2.3) has a label allocation
exactly when there are `C\in\mathcal B` and `m\in M-C`: use the common-row
allocation with image `C` and assign `m` to the fifth row. Consequently it
fails exactly when `M\subseteq C` for every `C\in\mathcal B`, which is
equivalent to

\[
                         M\subseteq\bigcap_{C\in\mathcal B}C=K.
\]

This proves (2.4).

If both response families fail, then (1.7) and (2.4) give

\[
                         B\in K,\qquad A\in K.
\]

The labels are distinct, so `|K|\ge2`. Every member of `\mathcal B` has
order four, and `K` is contained in every such member, so `|K|\le4`. This
proves (2.5).

Finally fix `k\in K` and delete `k` from the label ground. Every common-row
allocation uses `k`, by the definition of `K`, so the four rows have no
allocation in `\mathcal L-\{k\}`. Hall's theorem gives a nonempty
`I\subseteq\Theta` with

\[
                         |N(I)-\{k\}|<|I|.              \tag{2.7}
\]

The original four rows satisfy Hall, so `|N(I)|\ge|I|`. Removing one label
can lower cardinality by at most one. Equality is therefore forced on both
sides:

\[
                         |N(I)|=|I|,
             \qquad     |N(I)-\{k\}|=|I|-1.
\]

This is (2.6). \(\square\)

## 3. Boundary consequences

### Corollary 3.1

Suppose the four common rows satisfy Hall and both five-row response
families fail Hall. Then all of the following hold.

1. Each of the operated labels contains at least two boundary vertices:

   \[
                           |S\cap A|\ge2,
                    \qquad |S\cap B|\ge2.              \tag{3.1}
   \]

2. Up to ordering, the multiplicities with which foreign branch-set
   labels occur on `S` are exactly one of

   \[
             (2,2,1,1,1),\qquad (2,2,2,1),\qquad
             (3,2,1,1).                                \tag{3.2}
   \]

3. The common equality partition induced by `\phi` and `\psi` on `S` has
   one block of order two and five singleton blocks. At least one of the
   labels `A,B` contains two vertices of `S` which belong to two distinct
   singleton blocks of that partition.

#### Proof

Choose any common-row allocation `s` and write

\[
                         C_s=\{s(\theta):\theta\in\Theta\}.
\]

By (2.5), `A,B\in K\subseteq C_s`. Hence there are distinct colours
`\theta_A,\theta_B\in\Theta` and literal boundary vertices

\[
       x_A\in S\cap A\cap\phi^{-1}(\theta_A),
       \qquad
       x_B\in S\cap B\cap\phi^{-1}(\theta_B).          \tag{3.3}
\]

They are distinct from `a,b`, whose colours are `\alpha,\beta`. This proves
(3.1).

The allocation supplies four distinct foreign labels on four distinct
`\Theta`-coloured vertices of `S`, including `A,B`. Adding `a\in A` and
`b\in B` accounts for six boundary vertices and gives current label
multiplicities `2,2,1,1`. The seventh boundary vertex either has a fifth
label, repeats one of the two singleton labels, or repeats `A` or `B`.
These are exactly the three partitions in (3.2).

In the centre placement, `a` and `b` have the distinct colours
`\alpha,\beta`, while the other five boundary vertices use all four colours
in `\Theta`. Thus `a,b` are singleton colour blocks and exactly one
`\Theta` colour occurs twice. The common boundary partition consequently
has block sizes `(2,1,1,1,1,1)`.

The vertices `x_A,x_B` in (3.3) have different colours. At most one of
them can lie in the unique nonsingleton colour block. For the other one,
say `x_A`, both `a` and `x_A` are singleton blocks, are in the same
branch set `A`, and have different colours. This proves item 3.
\(\square\)

## 4. Exact contribution and trust boundary

The theorem makes the two-colouring obstruction finite without identifying
colours with model labels. Either the four rows unchanged by the Kempe
interchange already have a transition-invariant Hall defect, or simultaneous
failure of the two five-row allocations forces the two distinct operated
labels into the compulsory core of every common four-row allocation.

At the exact-seven centre-placement separator, the second outcome gives a
literal same-branch-set pair of singleton boundary blocks and the three
label-multiplicity patterns in (3.2). It does **not** show that a path
between that pair avoids the other five boundary vertices, that the path
can be combined with the boundary-full connected subgraphs on the opposite
shore, or that the common partition extends through the intact `D`-shore.

No use of `K_7`-minor exclusion is made here. The next host-level theorem
must use one tight witness (2.6) inside a compulsory branch set to obtain
one of:

1. a label-preserving branch-set split giving an explicit `K_7`-minor
   model;
2. an actual order-seven separation on which one complete equality
   partition extends through both closed shores; or
3. a strict response- and label-preserving branch-set descent.

The existence of two disjoint unlabelled three-vertex paths would not by
itself supply this conclusion: the paths must realize the compulsory
branch-set labels and retain the five outside contacts needed by the
labelled minor-model construction.
