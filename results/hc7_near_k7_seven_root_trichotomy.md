# Seven-root trichotomy for the both-missing frame

## Status

This synthesizes the endpoint shadow, neutral separator, row-core gate,
and surplus-transfer theorems.  It is the first rooted-model principle in
this programme which handles the whole nontrivial both-missing interface
at arbitrary adhesion order, not only the exact-seven case.

The output is `K_7`, an actual nested adhesion, or a labelled deficiency
rotation whose new centre is a proper connected part of one neutral bag.
The latter two outputs still require a well-founded state/coherence
argument; the theorem is not `HC_7` by itself.

## Theorem 1 (uniform seven-root trichotomy)

Let `G` be seven-connected.  Let

\[
                         X,B,C,U_1,U_2,U_3,U_4           \tag{1.1}
\]

be pairwise disjoint connected sets such that:

1. `B,C,U_1,...,U_4` form a `K_6` model;
2. `X` is anticomplete to `B,C` and meets every `U_i`; and
3. the literal neutral portal set
   
   \[
              S=N_G(X)\cap(U_1\cup\cdots\cup U_4)       \tag{1.2}
   \]
   
   has order at least seven.

Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. There is a nonempty connected set `Y` contained in one neutral bag
   such that `N_G(Y)` is an actual vertex separator of order at least
   seven.  If its order is seven, it is full to every component of
   `G-N_G(Y)`.
3. There is a labelled `K_7^-` or `K_7^vee` model whose deficient centre
   is a proper nonempty connected subset of one old neutral bag.

### Proof

Every `S cap U_i` is nonempty by item 2.  Choose a seven-element subset
`R subseteq S` containing at least one vertex from each neutral bag.  Mark
the selected vertices.  Four are protected, one in each `U_i`; the other
three are surplus.  Their distribution has exactly two forms.

#### Case 1: at least two neutral bags contain surplus marks

Apply the opposite-root row-core theorem in two such donors.  For each
donor it gives a monopoly-free surplus component, an actual nested
separator, or a gate-to-centre deficiency rotation.  A separator is
outcome 2 and a rotation is outcome 1 or 3.

In the remaining branch, each donor supplies a monopoly-free connected
piece containing a surplus mark and leaving its protected donor core
connected.  If such a piece missed either twin, the missed connected bag
would lie beyond its open neighbourhood, giving outcome 2.  Hence both
pieces meet both twins and are transferable to either one.  The pieces
lie in distinct donor bags and are disjoint.  Let `W_1,W_2` be their two
connected donor complements.  If `W_1,W_2` are anticomplete,
`N_G(W_1)` is an actual separator with `W_2` on a far side, giving
outcome 2.  Otherwise transfer one piece to `B` and one to `C`.  The
surviving `W_1W_2` edge is the only simultaneous-transfer adjacency not
certified by the two individual monopoly-free conditions.  The resulting
six clique bags contain six distinct marks of `R`; `X` is adjacent to
every marked vertex.  They and `X` form a `K_7` model, outcome 1.

#### Case 2: all three surplus marks lie in one neutral bag `U`

The donor `U` contains four marks.  The three-root connected-partition
lemma gives

\[
                         U=U_0\dot\cup Z_B\dot\cup Z_C   \tag{1.3}
\]

with all parts nonempty and connected, `U_0` adjacent to both moved
parts, and all three containing distinct marks.  If either moved part
misses one twin, its neighbourhood gives outcome 2.  Otherwise assign
`Z_B` to `B` and `Z_C` to `C`.

Regard `U_0` as a new deficient centre.  The six foreign bags are `X`,
the two enlarged twins, and the three untouched neutral bags.  They form
a clique model: the marked moved roots give the two `X`-twin edges, and
all remaining edges are old foreign-clique or `X`-neutral edges.  The
protected root gives `U_0X`, and the two partition cut edges give the
two centre--twin edges.

If `U_0` retains all three untouched neutral contacts, these seven bags
give `K_7`.  If it loses one or two, they give respectively `K_7^-` or
`K_7^vee`, and `U_0` is a proper connected subset of `U`: outcome 3.  If
it loses all three, it is anticomplete to any untouched neutral bag, so
its open neighbourhood is an actual separator: outcome 2.

This exhausts the two distributions and proves the theorem. \(\square\)

## Corollary 2 (application to every nontrivial normalized path)

In the target-free nontrivial path branch of the `HC_7` proof spine, let
`X` be the full path-side envelope.  The endpoint-shadow theorem makes
`X` anticomplete to both twins, and the neutral-separator theorem gives

\[
                         N_G(X)\subseteq U_1\cup\cdots\cup U_4,
                         \qquad |N_G(X)|\ge7.             \tag{2.1}
\]

Thus Theorem 1 applies regardless of whether the original neutral
separator has order seven, eight, or larger.  The former split into root
distributions and the latter “selected seven-fan” problem are the same
rooted-model state.

Consequently a nontrivial both-missing path is no longer an independent
terminal configuration.  It either gives `K_7`, descends to an actual
neutral-bag adhesion, or rotates the two-spoke deficiency into a proper
part of a neutral bag.  What remains is to show that repeated rotations
and adhesion descents terminate in matching proper-minor states or one
coherent two-apex society.

## Corollary 3 (every adhesion output is a faithful equality-state interface)

Assume in addition that `G` is proper-minor-minimal non-six-colourable,
and let `Y` be an adhesion output of Theorem 1.  Put

\[
                  T=N_G(Y),\qquad
                  C_Y=G[Y\cup T],\qquad O_Y=G-Y.         \tag{3.1}
\]

Then `(C_Y,O_Y)` is an actual separation with labelled boundary `T` and

\[
                   Ext(C_Y,T)\cap Ext(O_Y,T)=\varnothing. \tag{3.2}

Every deletion or contraction supported strictly inside `Y` produces a
six-colour boundary equality partition which extends to `O_Y` but not to
`C_Y`.  If the same labelled partition is produced by a proper operation
in the opposite open shore, the two restrictions splice to a
six-colouring of `G`.

### Proof

Theorem 1 supplies a connected nonempty far bag anticomplete to `Y`, so
`T` is an actual separator and (3.1) is a separation.  Equality of an
extendable boundary partition on both closed sides would allow a
permutation of six colour names followed by gluing, contradicting the
choice of `G`; this proves (3.2).

An internal proper operation gives a six-colouring of the corresponding
proper minor of `G`.  Its restriction to the unchanged opposite side is
an `O_Y` extension of the induced labelled partition.  Were that
partition extendable to the original `C_Y`, gluing would again colour
`G`.  The crossed-operation statement is the same gluing argument with
the two unchanged closed sides supplied by opposite proper minors.
\(\square\)

Thus even when `|T|>7`, the separator outcome is not merely a numerical
cut: it is the safe palette-free state interface needed by the dynamic
programme.  Exact order seven adds fullness, but fullness is not required
for equality-state splicing.

## General mechanism

The proof uses no Moser labels, no planarity, and no exact-boundary
enumeration.  Its reusable core is:

\[
 \boxed{\begin{array}{c}
 \text{a full connected shore plus seven roots in four bags}\cr
 \Longrightarrow\ K_7,\ \text{actual adhesion, or a smaller-bag
 deficiency rotation.}
 \end{array}}
\]

The number seven enters only through the target clique order and ambient
connectivity.  The row-core avoidable/unavoidable dichotomy and opposite-
root monopoly inequality are parameter-uniform.
