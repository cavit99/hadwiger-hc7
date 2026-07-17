# Connected transfer and extremal normalization in a near-`K_7` model

**Status:** written proof; separate internal audit GREEN.

This note gives a reusable exchange principle for the current conditional
`HC_7` branch.  It first records a consequence of the component-count
density lemma already proved in
[`hc7_component_contact_defect_theorem.md`](../results/hc7_component_contact_defect_theorem.md):
for seven disjoint sets, it is enough that the union of every two sets be
connected.  An individual set need not be connected.

Applied to the connected deficient-branch-set trichotomy, this removes its
reversible near-`K_7` outcome: a weak transfer either gives a `K_7` minor or
exposes the full neighbourhood of a connected subgraph as an actual
separation.  In fact, every residual component must miss a fixed set; if
one component retained all five contacts, it would itself complete the
seven branch sets.  The separation can have order greater than seven, and
the result does not yet synchronize its two boundary colourings or return
a complete valid defect-one configuration.  A model-order extremal choice
does, however, reduce the reversible residue to a vertex-minimal connector
spanning its prescribed portal and external-attachment vertices.

## 1. Pairwise-connected unions already force a `K_7` minor

Call pairwise disjoint nonempty vertex sets

\[
                         B_1,\ldots,B_7                         \tag{1.1}
\]

a **pairwise-connected-union family** when

\[
                         G[B_i\cup B_j]\text{ is connected}
                         \qquad(i\ne j).                         \tag{1.2}
\]

The individual graphs `G[B_i]` need not be connected.  This is the object
usually called a quasi-`K_7` model, but no external quasi-minor theorem is
needed here.

### Lemma 1.1

Every graph containing a family (1.1)--(1.2) contains a `K_7` minor.

#### Proof

For each `i`, let

\[
                    c_i=\operatorname{cc}(G[B_i]),
                    \qquad n=\sum_{i=1}^7c_i.
\]

Every `B_i` is nonempty, so `n>=7`.  Condition (1.2) says that

\[
                    \operatorname{cc}(G[B_i\cup B_j])=1
                    \qquad(i<j).
\]

The sum of the twenty-one pairwise component counts is therefore `21`, and

\[
                              21\le n+14.
\]

Lemma 1.1 of the component-contact defect theorem now applies to the seven
sets `B_i` and gives a `K_7` minor.  \(\square\)

The proof is worth recording because it explains exactly why disconnected
provisional branch sets are harmless at `t=7`: after contracting their
components, pairwise connectedness supplies enough edges for Mader's exact
`K_7` extremal bound.

## 2. The weak transfer theorem

### Theorem 2.1 (connected transfer or separation)

Let `G` be seven-connected.  Let

\[
                       W,C,F_1,F_2,F_3,F_4,F_5                 \tag{2.1}
\]

be pairwise disjoint nonempty connected vertex sets such that

1. the five sets `F_1,...,F_5` are pairwise adjacent;
2. `C` is adjacent to every `F_i`;
3. `W` is adjacent to `C`.

Put

\[
               \Omega=\{i\in[5]:E_G(W,F_i)=\varnothing\}.       \tag{2.2}
\]

Suppose there is a nonempty connected proper subset `T` of `C` such that

1. `T` is adjacent to `W`; and
2. `T` is adjacent to every `F_i` with `i in Omega`.

Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. Every component `D_a` of `G[C-T]` is anticomplete to at least one
   `F_i`.  In particular, if `D_1,...,D_k` are those components and

   \[
      M=\bigl|\{(a,i):a\in[k],\ i\in[5],\
                    E_G(D_a,F_i)=\varnothing\}\bigr|.              \tag{2.3}
   \]

   then `M>=k`.  For every component `Y` of `G[C-T]`, choosing an `F_i`
   anticomplete to it gives an actual separation

   \[
              \bigl(Y\cup N_G(Y),\;V(G)-Y\bigr)                \tag{2.4}
   \]

   with two nonempty open sides and

   \[
                              |N_G(Y)|\ge7.                       \tag{2.5}
   \]

   If equality holds in (2.5), every component of `G-N_G(Y)` is adjacent
   to every vertex of `N_G(Y)`.

#### Proof

Let `D` be any component of `G[C-T]`.  The connected set `C` forces an
edge from `D` to `T`: distinct components of `G[C-T]` are anticomplete,
so every edge of `G[C]` leaving `D` has its other end in `T`.

Suppose `D` is adjacent to every `F_i`.  Consider the following seven
disjoint nonempty connected sets:

\[
                    W\cup T,\qquad D,\qquad F_1,\ldots,F_5.       \tag{2.6}
\]

They are pairwise adjacent.  The set `W union T` is adjacent to `D`
through the edge just found.  It is adjacent to `F_i` through `W` when
`i notin Omega` and through `T` when `i in Omega`.  The component `D`
is adjacent to every `F_i` by assumption, and the five fixed sets are
pairwise adjacent.  Thus (2.6) is an explicit `K_7`-minor model.

Consequently, if outcome 1 fails, every component `D` misses at least one
fixed set.  This proves the assertion `M>=k` as well.

Choose a missed pair `(Y,F_i)`.  The set `Y` is a nonempty connected open
side of (2.4), while the nonempty set `F_i` is disjoint from
`Y union N_G(Y)` and lies in the other open side.  Hence (2.4) is an
actual separation.  Seven-connectivity gives (2.5).

If `|N_G(Y)|=7` and a component `K` of `G-N_G(Y)` missed a boundary
vertex `x`, then

\[
                         N_G(K)\subseteq N_G(Y)-\{x\}
\]

would separate `K` from another component of `G-N_G(Y)` with at most six
vertices.  This contradicts seven-connectivity.  Therefore every component
is adjacent to every boundary vertex.  \(\square\)

### Exact gain over ordinary branch-set surgery

The theorem never requires `C-T` to be connected.  Nor does it require one
connected subgraph of `C-T` to retain all five named adjacencies.  Instead,
it proves that any single component retaining those adjacencies is already
terminal.  Hence every residual component separately exposes an actual
full-neighbourhood separation in a `K_7`-minor-free host.  Moreover,
`C-Y` is connected for each returned component `Y`: it consists of the
connected set `T` together with the other components of `G[C-T]`, each of
which has an edge to `T`.

## 3. Application to a connected-subgraph rotation

Use the setup of the mutually-unavoidable branch in
[`hc7_connected_one_hole_trichotomy.md`](../results/hc7_connected_one_hole_trichotomy.md)
and
[`hc7_rotation_opposite_boundary_responses.md`](../results/hc7_rotation_opposite_boundary_responses.md).
Thus

\[
                         A,R,F_1,\ldots,F_5
\]

is the old labelled configuration, `U=F_i` is the donor, and

\[
                         U=Z\mathbin{\dot\cup}W
\]

with `Z,W` nonempty connected and adjacent.  The new connected centre is

\[
                              C=A\cup Z.
\]

Use as the five fixed sets

\[
                  \mathcal F=\{R\}\cup\{F_j:j\ne i\}.           \tag{3.1}
\]

The set `C` is adjacent to every member of `mathcal F`; the original centre
`A` supplies the contacts with the four old rows, and `Z` supplies the
contact with `R`.  The residual donor `W` is adjacent to `C` and misses
precisely the nonempty set

\[
        \Omega=\{H\in\mathcal F:N_U(H)\subseteq Z\}.             \tag{3.2}
\]

### Corollary 3.1 (the reversible rotation reduces to a separation)

Fix any connected subgraph `T` of `Z` containing the unique `W-Z`
attachment vertex `s` and meeting `N_Z(H)` for every `H in Omega`.  Under
this setup, `G` contains a `K_7` minor or every component `Y` of
`G[(A union Z)-T]` has `N_G(Y)` as the boundary of an actual separation
with

\[
                              |N_G(Y)|\ge7.                       \tag{3.3}
\]

In the latter case, `(A union Z)-Y` is connected.

#### Proof

Each portal set `N_Z(H)`, `H in Omega`, is nonempty, so such a `T` exists:
choose one vertex in each portal set and join the selected vertices and
`s` inside the connected graph `G[Z]`.  The edge from `s` to `W` makes
`T` adjacent to `W`, and the selected portal vertices make `T` adjacent
to every missed fixed set.

The set `T` is a proper subset of `C=A union Z`, because `A` is nonempty
and disjoint from `Z`.  Apply Theorem 2.1 to

\[
                       W,\quad C=A\cup Z,\quad\mathcal F.
\]

It gives the asserted `K_7` minor or the connected set `Y` and separation.
\(\square\)

### Corollary 3.2 (collapsed trichotomy)

Under the hypotheses of the connected one-missing-adjacency trichotomy,
the third, reversible near-`K_7` outcome always yields either a `K_7` minor
or an actual full-neighbourhood separation of order at least seven.
Consequently that trichotomy can be restated with only two conclusion
types:

1. an explicit `K_7`-minor model; or
2. an actual separation whose boundary is the full neighbourhood of a
   named connected subgraph and has order at least seven.

#### Proof

Outcomes 1 and 2 of the original theorem already have the displayed forms.
Apply Corollary 3.1 to outcome 3.  \(\square\)

### Corollary 3.3 (conditional defect-one application)

In the conditional defect-one branch, apply the rainbow-diamond separation
and then the connected one-missing-adjacency trichotomy with

\[
 A=X,\qquad R=V_r,\qquad
 \{F_1,\ldots,F_5\}=\{A_1,A_2,A_3,V_m,V_n\}.
\]

Then `G` contains a `K_7` minor or has an actual separation whose boundary
is the full neighbourhood of a named connected subgraph and has order at
least seven.

#### Proof

Section 5 of the connected one-missing-adjacency trichotomy verifies all of
its hypotheses for the displayed seven connected sets.  Corollary 3.2
therefore applies.  \(\square\)

This conclusion removes the reversible rotation from this conditional
branch.  It does **not** assert that the returned separation preserves the
four protected labels, the colour-matched path and its admissible cut, or
the component-contact graph.  It is therefore a reduction to an unbounded
full-neighbourhood separation, not a new valid defect-one configuration.

## 4. The induced near-complete model and the exact minimality issue

The rotation setup contains one distinguished residual component.  Let
`D_A` be the component of `G[(A union Z)-T]` containing `A`.  It is
well-defined because `A` is connected and disjoint from `T subseteq Z`.

### Proposition 4.1 (one-missing-adjacency replacement)

If `G` has no `K_7` minor, then the seven connected sets

\[
                 D_A,\qquad W\cup T,\qquad
                 R,\qquad F_j\ (j\ne i)                         \tag{4.1}
\]

form a near-`K_7` model whose only possible missing adjacency is the pair
`D_A,R`.  In fact, that pair is anticomplete.  Moreover,

\[
                         (A\cup Z)-D_A                            \tag{4.2}
\]

is connected.

#### Proof

The component `D_A` has an edge to `T`, so it is adjacent to `W union T`.
It contains all of `A`, and hence is adjacent to each of the four sets
`F_j`, `j ne i`.  As in Theorem 2.1, `W union T` is adjacent to every one
of the five fixed sets, and those fixed sets are pairwise adjacent.

If `D_A` were adjacent to `R`, the seven sets in (4.1) would be an explicit
`K_7`-minor model.  Hence `D_A` is anticomplete to `R` in a
`K_7`-minor-free graph, and (4.1) is a labelled `K_7^-`-minor model with
that unique missing adjacency.

Finally, `(A union Z)-D_A` consists of `T` and all the other components of
`G[(A union Z)-T]`.  Every such component has an edge to `T`, so their
union is connected.  \(\square\)

The replacement also preserves the hypothesis needed to run the connected
one-missing-adjacency trichotomy, provided the transferred set contains
all external attachment vertices of `Z`.  Put

\[
 O=V(G)-\bigl(A\cup R\cup F_1\cup\cdots\cup F_5\bigr)
\]

and

\[
 E_Z=\{z\in Z:E_G(z,O)\ne\varnothing\}.                         \tag{4.3}
\]

### Proposition 4.2 (supported-centre preservation)

Suppose, in addition to the requirements in Corollary 3.1, that `T`
contains `E_Z`.  Then the replacement in (4.1), relabelled as

\[
 A'=D_A,\qquad R'=R,\qquad
 \{F'_1,\ldots,F'_5\}
   =\{W\cup T\}\cup\{F_j:j\ne i\},                              \tag{4.4}
\]

satisfies the full supported-centre hypotheses

\[
 A'R'=\varnothing,qquad
 A'\text{ is adjacent to every }F'_h,qquad
 N_G(A')\subseteq F'_1\cup\cdots\cup F'_5.                     \tag{4.5}
\]

#### Proof

Proposition 4.1 gives the first two assertions.  It remains to check the
neighbourhood inclusion.  The old support hypothesis gives
`N_G(A) subseteq F_1 union ... union F_5`, so `A` has no neighbour in
`O`.  Every vertex of `Z` with a neighbour in `O` belongs to `T`; hence
`D_A intersect Z` also has no neighbour in `O`.

Inside the union of the old seven branch sets, the only sets not displayed
on the right of (4.5) are `A'` itself, `R`, and the other components of
`G[(A union Z)-T]`.  The first is internal, `A'` is anticomplete to `R`
by Proposition 4.1, and distinct residual components are anticomplete.
Thus every neighbour of `A'` lies in one of the five displayed met branch
sets.  \(\square\)

Call seven sets a **supported one-missing-adjacency configuration** when
they satisfy hypotheses 1--3 of the connected one-missing-adjacency
trichotomy: six form a `K_6`-minor model, the seventh connected set misses
one named branch set and meets the other five, and its whole open
neighbourhood lies in those five met branch sets.  Call the sum of the
orders of its seven branch sets its **model order**.  Let
`D_A,D_2,...,D_k` be all the components of `G[(A union Z)-T]`.  The old
configuration has order

\[
 |W|+|A\cup Z|+\sum_{H\in\mathcal F}|H|,
\]

whereas the model in (4.1) has order

\[
 |W|+|T|+|D_A|+\sum_{H\in\mathcal F}|H|.
\]

Their difference is

\[
                            \sum_{a=2}^{k}|D_a|.                  \tag{4.6}
\]

Choose, among all supported one-missing-adjacency configurations in `G`,
one of minimum model order and, subject to that, with `|A|` maximum.  Such
a choice exists whenever the connected trichotomy is invoked.  In its
reversible outcome, choose one vertex of every lost portal set, and let
`T` be an inclusion-minimal connected subset of `Z` containing those
vertices, `s`, and all of `E_Z`.

Proposition 4.2 makes the replacement another supported
one-missing-adjacency configuration.  Formula (4.6) and minimum model order
therefore force `k=1`.  The new centre then contains `A`, and

\[
                         |D_A|=|A|+|Z-T|.                         \tag{4.7}
\]

It has the same model order as the old configuration.  Maximality of
`|A|` forces `Z-T` to be empty.  Consequently

\[
                                  T=Z.                            \tag{4.8}
\]

We have therefore obtained a host-level extremal normalization: in a
minimum-order, maximum-centre supported configuration, every reversible
outcome has `Z` itself inclusion-minimal among connected vertex sets
containing

\[
       \{s\}\cup E_Z\cup
       \{\text{one selected vertex of }N_Z(H):H\in\Omega\}.      \tag{4.9}
\]

This is a genuine well-founded partial descent.  It does not yet eliminate
the final equality case.  The exact equal-order obstruction is now
explicit: `k=1` and

\[
                    A\cup Z=Z\mathbin{\dot\cup}A,                \tag{4.10}
\]

and the equal-order operation merely moves the vertex-minimal connector
`Z` back to the donor branch set while moving the unique missing adjacency
back to `AR`.  If `E_Z` is empty, (4.9) has at most three terminals because
`|Omega|<=2`; the survivor is therefore a minimal connector for at most
three prescribed portal vertices.  With external attachment vertices
present, their placement is the remaining unbounded obstruction.

## 5. Consequence for the response-collision programme

The opposite boundary-response theorem attaches two polarized colouring
languages to every reversible rotation.  Corollary 3.1 and the extremal
normalization show that a general rotation need not be attacked directly:
it either yields the displayed separation or reduces to the atomic case in
which `Z` is a vertex-minimal connector for (4.9).

This does **not** complete the active exchange-or-gluing theorem.  The new
separation can have order greater than seven.  The proof does not give the
same equality partition from operations in its two open shores, and `Y`
need not be an eligible component in a new valid defect-one
colour-matched-path configuration.  Model order gives a strict decrease
outside the atomic connector case, but no strict decrease of the globally
minimum lifted simplicial component has been proved.

The exact remaining step after this note is therefore narrower: trim the
returned full-neighbourhood separation to order seven while retaining a
common proper-minor boundary partition, or prove that its connected near
shore re-enters the complete valid defect-one setup with the required
strict host-level decrease.  In the equal-order branch, it is enough to
couple the two boundary-response languages on the vertex-minimal connector
described by (4.9), rather than on an arbitrary transferred subgraph.

## 6. Dependency and terminology

The only non-elementary input used above is already internal to the active
proof spine:

* [component-count density and component-contact defect](../results/hc7_component_contact_defect_theorem.md),
  Lemma 1.1.

Families satisfying (1.2) are called quasi-clique-minor models in the
literature.  For seven sets, Lemma 1.1 gives the required genuine clique
minor directly, so no separate external quasi-minor theorem is invoked.
