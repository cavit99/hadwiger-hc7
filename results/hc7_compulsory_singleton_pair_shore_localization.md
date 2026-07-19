# Shore localization of a compulsory same-label singleton pair

**Status:** written proof; separate internal audit GREEN in
[`hc7_compulsory_singleton_pair_shore_localization_audit.md`](hc7_compulsory_singleton_pair_shore_localization_audit.md).
This note starts from the audited two-response Hall-core theorem.  It gives
one literal host-graph consequence of its same-label singleton pair and a
partition-specific completion criterion.  It does not prove that the
completion criterion is always attained and does not prove `HC_7`.

## 1. Setting

Use the exact-seven centre-placement setting of
[`hc7_two_response_compulsory_label_core.md`](hc7_two_response_compulsory_label_core.md).
Assume additionally that every proper minor of `G` is six-colourable and
that `ab` is an edge, as in the critical-triangle application.  Thus `G`
has a spanning labelled `K_7`-minus-one-edge model with singleton root
branch set `\{v\}`; the two operated edges are

\[
                         va,\qquad vb,
\]

where `a` and `b` lie in the distinct foreign branch sets labelled `A` and
`B`.  The common deletion has two six-colourings related by interchanging
the colours `alpha,beta` on one connected bichromatic component `D`, with

\[
 v\in D,\qquad a,b\notin D,\qquad
 \phi(a)=\alpha,\qquad \phi(b)=\beta .                 \tag{1.1}
\]

Put

\[
 S=N_G(D),\qquad |S|=7,\qquad
 R=V(G)-(D\cup S),                                     \tag{1.2}
\]

and assume `R` is nonempty.  The two colourings agree on `S`.  Their common
equality partition has the form

\[
             \Pi=I\mid\{q\}\quad(q\in Q),
 \qquad |I|=2,\quad |Q|=5.                              \tag{1.3}
\]

Assume that the four untouched-colour rows satisfy Hall's condition and
that both response-specific five-row families fail it.  The Hall-core
theorem then supplies vertices

\[
 x_A\in S\cap A,\qquad x_B\in S\cap B                 \tag{1.4}
\]

of distinct untouched colours.  At least one of the pairs
`a,x_A` and `b,x_B` consists of two singleton blocks of `Pi`.

Every mention of a branch-set label below refers to the fixed literal
branch-set partition.  No palette colour is identified with a model label.

## 2. The compulsory path is on the opposite shore

### Theorem 2.1 (same-label singleton localization)

Exactly one of the following two conclusions is forced by the data above.

1. For some `L in {A,B}`, with operated end `p` and untouched-colour
   vertex `x_L`,

   \[
       \{p\},\{x_L\}\in\Pi,
       \qquad S\cap L=\{p,x_L\}.                       \tag{2.1}
   \]

   The branch set `L` contains a `p`--`x_L` path whose internal vertices
   lie in `R`; when the path has an internal vertex, all of its internal
   vertices lie in one component of `G-S` contained in `R`.

2. Up to interchanging `A,B`, the label multiplicities on `S` are
   `(3,2,1,1)`, and there is a vertex `y_A` such that

   \[
   \begin{aligned}
       S\cap A&=\{a,x_A,y_A\},&
       S\cap B&=\{b,x_B\},\\
       \{a\},\{x_A\}&\in\Pi,&
       I&=\{x_B,y_A\}.                                \tag{2.2}
   \end{aligned}
   \]

   Thus the only obstruction to conclusion 1 is the crossed placement in
   which the tripled operated label contains the mate of the other
   operated label's untouched-colour vertex.  Even in this residue there
   are two vertex-disjoint labelled paths with interiors in `R`: one joins
   `b` to `x_B` inside branch set `B`, and the other joins `a` to one of
   `x_A,y_A` inside branch set `A`.  The two paths are adjacent through
   the boundary edge `ab` from the critical triangle.

#### Proof

The Hall-core theorem gives the label multiplicity patterns

\[
 (2,2,1,1,1),\qquad (2,2,2,1),\qquad (3,2,1,1).       \tag{2.3}
\]

The vertices `a,b` are singleton blocks.  The vertices `x_A,x_B` have
distinct untouched colours, so at most one of them lies in the unique
two-vertex block `I`.

Suppose first that one of `x_A,x_B`, say `x_L`, is a singleton and its
label has multiplicity two on `S`.  With `p=a` when `L=A` and `p=b` when
`L=B`, equation (2.1) follows.

The branch set `L` is connected.  Since its only boundary vertices are
`p,x_L`, a shortest `p`--`x_L` path in `G[L]` has no internal vertex in
`S`.  If the path is the edge `px_L`, conclusion 1 is immediate.  Otherwise
its internal vertices lie in one component `C` of `G-S`.  They cannot lie
in `D`.  Indeed, the first edge of the path from `p` to `C` is an edge of
the common-deletion graph: the only deleted edge at `p` has other end `v`,
and `v` belongs to the disjoint singleton root branch set rather than to
`L`.  Both `p` and its neighbour in `D` have one of the colours
`alpha,beta`, so that edge would put `p` in the same `alpha,beta`
component `D`, contrary to (1.1).  Hence `C subseteq R`, which proves
conclusion 1.

It remains to determine when no operated label satisfies the preceding
condition.  At most one label in (2.3) has multiplicity three.  Therefore
one of `A,B`, say `A`, has multiplicity three, the other has multiplicity
two, and the singleton among `x_A,x_B` must be `x_A`; otherwise the
multiplicity-two label would already give conclusion 1.  Consequently
`x_B in I`.  The seventh boundary vertex, which is responsible for the
third occurrence of label `A`, must be the other member `y_A` of `I`:
the other six vertices are

\[
                    a,x_A,b,x_B
\]

together with two vertices having two further distinct labels.  This is
exactly (2.2).  The argument is symmetric if `B` is the tripled label.

It remains to verify the two asserted paths.  Since `S cap B={b,x_B}`,
the preceding shortest-path argument gives a `b`--`x_B` path in `B` whose
interior lies in `R`.  In the connected branch set `A`, choose a shortest
path from `a` to the set `\{x_A,y_A\}`.  Its internal vertices avoid `S`.
They cannot lie in `D`, by the same common-deletion component argument at
`a`, and hence lie in `R`.  The two paths are vertex-disjoint because the
branch sets `A,B` are disjoint, and `ab` is the critical-triangle boundary
edge.  Thus conclusion 2 is the unique residue and has the stated path
geometry. \(\square\)

## 3. When the localized path already reflects the boundary partition

The next statement records the exact extra geometry needed to turn the
path from Theorem 2.1 into a common boundary colouring.  It is useful
because it separates the now-proved shore location from the still-open
avoidance and contact-allocation problem.

### Theorem 3.1 (path-assisted exact response reflection)

Assume conclusion 1 of Theorem 2.1, and abbreviate `x=x_L`.  Let `P` be
the resulting `p`--`x` path with internal vertices in `R`.  Suppose there
are

* `r in {1,2}` pairwise vertex-disjoint `S`-full connected subgraphs
  `F_1,...,F_r` in `R-V(P-S)`; and
* a clique `U` of order `5-r` in `G[Q-x]` which contains `p` and for which

  \[
                         U-\{p\}\subseteq N_G(x).       \tag{3.1}
  \]

Then the common equality partition `Pi` is induced by proper
six-colourings of both original closed shores.  In particular, `G` is
six-colourable.

#### Proof

The restriction of either response colouring to `G[R\cup S]` is proper
and induces `Pi`, because the two deleted edges run between `D` and `S`.

If `px` is an edge, then `U union \{x\}` is a clique of order `6-r`
among singleton blocks.  The only blocks of `Pi` not represented by this
clique number exactly `r`; assign the `r` boundary-full connected
subgraphs to them.  They form a `Pi`-carrier system, so exact response
reflection applies.

Assume now that `px` is not an edge.  The path has a nonempty internal
vertex set

\[
                         Z=V(P)-\{p,x\}\subseteq R.    \tag{3.2}
\]

Use `Z` as the connected subgraph assigned to the singleton block
`\{x\}`.  The union `Z union \{x\}` is connected.  It is adjacent to `p`
through the first edge of `P` at the `p` end, and it is adjacent to every
vertex of `U-\{p\}` through the boundary edges in (3.1).

There are

\[
        6-|U|-1=r                                      \tag{3.3}

further blocks of `Pi`: the two-vertex block `I` and, when `r=2`, one
additional singleton block.  Assign `F_1,...,F_r` bijectively to these
blocks.  Boundary fullness makes every assigned block union connected,
makes the assigned unions pairwise adjacent, joins each of them to
`Z union \{x\}`, and joins them to every vertex of `U`.  Thus these
`r+1` connected subgraphs are a `Pi`-carrier system relative to `U`.

The exact response-reflection theorem now supplies a proper six-colouring
of `G[D\cup S]` with equality partition `Pi`.  It aligns with the already
proper colouring of `G[R\cup S]`, so the two colourings glue. \(\square\)

## 4. Exact remaining host obstruction

The Hall-core obstruction has therefore been lifted one genuine level.
Except for the crossed tripled-label pattern (2.2), it forces an
opposite-shore path inside one fixed labelled branch set.  That path is
terminal whenever it can avoid the required one or two boundary-full
connected subgraphs and its endpoint has the clique contacts in Theorem
3.1.

What remains is not another colour-to-label allocation.  It is the literal
host alternative that, for the localized path, either

1. supplies the disjoint full connected subgraphs and clique contacts of
   Theorem 3.1;
2. exposes an order-seven full neighbourhood on which the same partition
   is legal on both closed shores; or
3. permits a strict branch-set replacement preserving the selected
   response and all six foreign labels.

Neither seven-connectivity nor the packet vector alone guarantees item 1:
the localized path may meet every maximum full-subgraph packing, and the
required singleton clique edges are literal boundary edges, not merely
adjacencies between the corresponding old branch sets.

## 5. Dependencies

* the audited two-response compulsory-label core;
* exact response reflection by a partition-specific carrier system; and
* the literal spanning branch-set partition of the selected
  `K_7`-minus-one-edge model.
