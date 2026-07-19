# Operation responses at the special five-plus-two exact-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_special_five_plus_two_exact7_response_audit.md`](hc7_special_five_plus_two_exact7_response_audit.md).
This note packages consequences of already audited results for the
order-seven separation produced in the proof of the concentrated
three-owner order-eight reduction.  It does not
prove that the two closed shores have colourings with the same complete
boundary equality partition, and it does not prove `HC_7`.

## 1. Inherited setting and the special boundary

Assume the complete setting of the audited
[concentrated three-owner order-eight reduction](../results/hc7_three_owner_order8_exact7_reduction.md),
Sections 1 and 2.  In particular,

\[
 \chi(G)=7,\qquad \kappa(G)\ge 7,\qquad
 K_7\not\preccurlyeq G,
\]

and every proper minor of `G` is six-colourable.  The graph has the fixed
spanning labelled `K_7`-minus-one-edge model and the concentrated
three-owner component `C` from that theorem.  Its literal order-eight
boundary is

\[
 S_8=\{k_1,k_2\}\mathbin{\dot\cup}
 \{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.
\tag{1.1}
\]

Let

\[
 T=\{s_{R_1},s_{R_2},s_{R_3}\}
\tag{1.2}
\]

be the three owner representatives.  Choose the vertex `v in C` adjacent
to `k_1` used in the three-fan argument, and put

\[
 H_0=G[C\cup T].
\tag{1.3}
\]

The cited theorem proves that no three-fan from `v` to `T` exists.  Let
`Z` be a Menger separator of order at most two meeting every `v`--`T`
path in `H_0`, and let `A` be the component of `H_0-Z` containing `v`.
Its proof gives

\[
 N_G(A)\subseteq (S_8-T)\cup Z.
\tag{1.4}
\]

The sets on the right are disjoint, at least one owner representative is
outside `Z`, and the opposite side is nonempty.  Seven-connectivity
therefore makes every inequality sharp:

\[
 |Z|=2,\qquad
 Y:=N_G(A)=(S_8-T)\mathbin{\dot\cup}Z,
 \qquad |S_8-T|=5,\qquad |Y|=7.
\tag{1.5}
\]

Put

\[
 B=V(G)-(A\cup Y),\qquad F=G[Y].
\tag{1.6}
\]

Then

\[
                 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
                 \qquad E_G(A,B)=\varnothing,
\tag{1.7}
\]

and both open shores are nonempty.

A connected subgraph of an open shore is **`Y`-full** if it has a
neighbour at every literal vertex of `Y`.  Let `nu_A,nu_B` be the maximum
numbers of pairwise vertex-disjoint `Y`-full connected subgraphs in `A`
and `B`, respectively.

For an independent-block partition `Pi` of `Y`, write

\[
 d_F(\Pi)=|\Pi|-\omega\bigl(F[\operatorname{sing}(\Pi)]\bigr).
\tag{1.7}
\]

For a closed subgraph `J` containing `Y`, let
`Ext(J,Y)` denote the exact equality partitions of `Y` induced by proper
six-colourings of `J`.

## 2. Exact normal form

### Theorem 2.1

In the setting above, all of the following hold.

1. Every component of `G-Y` is `Y`-full.  Up to interchanging the two
   shores,

   \[
                       (\nu_A,\nu_B)\in\{(1,1),(1,2)\}.
   \tag{2.1}
   \]

2. The boundary graph is four-colourable:

   \[
                              \chi(F)\le4.
   \tag{2.2}
   \]

3. Fix `z in Z`, choose an edge `za` with `a in A`, and let `c` be any
   proper six-colouring of `G-za`.  Let `Pi_z` be the exact equality
   partition induced by `c` on `Y`.  Then

   \[
   \Pi_z\in \operatorname{Ext}(G[B\cup Y],Y)
          \setminus \operatorname{Ext}(G[A\cup Y],Y)
   \tag{2.3}
   \]

   and

   \[
                             d_F(\Pi_z)>\nu_B.
   \tag{2.4}
   \]

   More generally, choose `nu_B` pairwise disjoint `Y`-full connected
   subgraphs `P_1,...,P_{nu_B}` in `B`.  Let `Q` be any maximum clique
   among the singleton blocks of `Pi_z`, and list the blocks not
   represented by `Q` as `C_1,...,C_d`.  Let

   \[
                    W_1,\ldots,W_t\subseteq B
   \tag{2.5}
   \]

   where `d=d_F(Pi_z)`, and be pairwise disjoint connected subgraphs,
   disjoint from all the
   `P_j`, and assume that the `W_i` are pairwise adjacent.  Join `W_i` to
   `C_j` when `W_i` has a neighbour at every vertex of

   \[
        D_Q(C_j)=C_j\cup
          \{q\in Q:E_G(q,C_j)=\varnothing\}.
   \tag{2.6}
   \]

   Then the resulting incidence graph has a nonempty block family
   `X subseteq {C_1,...,C_d}` satisfying

   \[
                 \nu_B+|N_{\{W_1,\ldots,W_t\}}(X)|<|X|.
   \tag{2.7}
   \]

   In particular, if `(nu_B,d)=(2,3)` or `(1,2)`, no displayed `W_i`
   meets the complete duty set of any `C_j`.

4. For the same edge `za` and colouring `c`, let `alpha=c(z)=c(a)`.
   For each of the other five colours `beta`, choose an
   `alpha`--`beta` path from `a` to `z` in `G-za`, and stop it at its
   first vertex `t_beta` of `Y`.  Put

   \[
                    T_0=\{z\}\cup\{t_\beta:\beta\ne\alpha\}.
   \tag{2.8}
   \]

   There is always a six-ended fan from `a` to six distinct vertices of
   `Y`, preserving the direct edge `az` and the first edge of each of the
   five selected bichromatic paths.  In addition, at least one of the
   following three alternatives follows from the audited
   critical-edge fan reduction.

   1. `|T_0|=6`.
   2. `|T_0|<=5`, and, for a chosen five-set `T'` with
      `T_0 subseteq T' subseteq Y`,
      there are five `a`--`T'` paths preserving the five selected first
      edges and pairwise vertex-disjoint outside `{a} union T'`.  Their
      ends in `T'` are allowed to coincide.
   3. `|T_0|<=5`, and, for the same choice of `T'`, there are a four-set
      `Z' subseteq A-{a}` and a nonempty connected proper subset
      `A' subsetneq A` such that

      \[
          N_G(A')=(Y-T')\mathbin{\dot\cup}\{a\}
                              \mathbin{\dot\cup}Z',
          \qquad |N_G(A')|=7.
      \tag{2.9}
      \]

      The restriction of `c` to the closed `A'`-side is proper in the
      original graph, and its exact `alpha`-coloured boundary block has
      order at least two.  A proper six-colouring of the opposite closed
      shore attains that same exact block.

Alternatives 4.1 and 4.2 do not allocate the paths to the inherited
minor-model labels.  Alternative 4.3 synchronizes one exact boundary
block, not the complete equality partition.

## 3. Proof

### Step 1: full connected subgraphs and packing vectors

Let `K` be a component of `G-Y`.  Its neighbourhood is contained in `Y`.
If it missed a vertex of `Y`, its neighbourhood would have order at most
six and would separate `K` from the nonempty opposite shore, contrary to
seven-connectivity.  Thus every component is `Y`-full.

The audited
[exact-seven full-subgraph packing theorem](../results/hc7_exact_seven_packet_packing.md),
Theorem 1, gives

\[
 \nu_A+\nu_B\le4,
 \qquad \min\{\nu_A,\nu_B\}=1.
\tag{3.1}
\]

Its only possible vectors are `(1,1)`, `(1,2)` and `(1,3)`, up to
orientation.  The audited
[adaptive `(1,3)` reflection theorem](../results/hc7_exact7_adaptive_packet_reflection.md),
Theorem 1.1, excludes `(1,3)` in a seven-chromatic `K_7`-minor-free graph.
This proves item 1.

### Step 2: the boundary is four-colourable

Corollaries 2.2 and 2.3 of the audited
[exact-seven no-rigid-trace theorem](../results/hc7_exact7_no_rigid_trace.md)
give `chi(F)<=5`.  If equality held, then

\[
                      F\cong K_2\vee C_5,
\tag{3.2}
\]

both open shores would be connected and `G-{p,q}` would contain a
`K_5` minor, where `p,q` are the two universal adjacent boundary
vertices.

The five cycle vertices induce a cycle, both open shores are connected
and adjacent to every vertex of that cycle and to `p,q`, and there are
exactly two components outside the displayed seven-set.  The audited
[cycle-boundary completion theorem](../results/hc7_cycle_boundary_completion.md)
therefore produces a `K_7` minor, contrary to the hypotheses.  Hence
`chi(F)<=4`, proving item 2.

### Step 3: the operation-specific partition and Hall obstruction

Equation (1.5) says that every `z in Z` has a neighbour `a in A`.
The edge-deleted graph `G-za` is a proper minor and hence has a proper
six-colouring `c`.  Necessarily `c(z)=c(a)`, since otherwise restoring
`za` would six-colour `G`.

The edge `za` does not belong to the opposite closed shore `G[B\cup Y]`.
Thus `c` restricts to a proper colouring of that original closed shore
and induces `Pi_z`.  If `Pi_z` also extended through the original closed
shore `G[A\cup Y]`, a permutation of the six colour names would align the
two exact boundary partitions and the colourings would glue.  This would
six-colour `G`.  Therefore (2.3) holds.

Suppose `d_F(Pi_z)<=nu_B`.  Lemma 2.1 of the audited adaptive reflection
theorem, applied to `nu_B` disjoint `Y`-full connected subgraphs in `B`,
gives either an explicit `K_7`-minor model or a proper colouring of
`G[A\cup Y]` whose exact boundary partition is `Pi_z`.  The former
contradicts minor exclusion; the latter contradicts (2.3).  Hence (2.4)
holds.

For the mixed-support assertion, adjoin one universal incidence vertex
for every `P_j` to the incidence graph in item 3.  If the resulting graph
had a matching saturating `C_1,...,C_d`, the audited
[transported-partition Hall reflection theorem](../results/hc7_transported_partition_hall_reflection.md),
Theorem 2.1, would reproduce `Pi_z` on `G[A\cup Y]`.  It would then glue
to `c|G[B\cup Y]`, again six-colouring `G`.  Hall's theorem therefore
gives a nonempty family `X` satisfying (2.7).

If `d=nu_B+1`, a deficient family cannot have at most `nu_B` members,
because it already sees all `nu_B` universal vertices.  Hence `X` is the
whole block family and has no `W_i`-neighbour.  This proves the two sharp
cases and completes item 3.

### Step 4: the critical-edge fan alternatives

The standard critical-edge Kempe argument applied to `za` gives, for
every colour `beta` different from `alpha`, an `alpha`--`beta` path from
`a` to `z` in `G-za`.  Truncating it at its first boundary vertex gives
the paths and first edges used in item 4.

Theorem 2.1 of the audited
[critical boundary-edge fan and descent theorem](../results/hc7_exact7_critical_edge_fan_descent.md)
gives the six-ended fan with six distinct boundary ends while preserving
all six prescribed first edges.

If `|T_0|=6`, this is alternative 4.1 and the target-retaining part of the
cited theorem has no further conclusion.  If `|T_0|<=5`, choose a
five-set `T'` containing it and apply Theorem 3.1 of the same source.  Its
packing outcome is alternative 4.2.  Its separation outcome gives (2.9),
the strict inequality `|A'|<|A|`, and the proper one-sided colouring with
an exact `alpha`-block of order at least two.  Corollary 3.2 of that source
attains the same exact block on the opposite closed shore.  This is
alternative 4.3 and proves item 4.  \(\square\)

## 4. Exact remaining gap

The decomposition

\[
                         Y=(S_8-T)\mathbin{\dot\cup}Z,
                         \qquad 5+2=7,
\]

does not itself imply any useful adjacency in `F=G[Y]`.  It also does not
make a retained labelled branch-set piece connected, disjoint from the
chosen full connected subgraphs, or adjacent to every vertex of a complete
duty set (2.6).  Therefore the conclusions above do not yet imply any of:

1. one complete equality partition attained on both closed shores;
2. an explicit `K_7`-minor model obtained by assigning the five response
   paths to inherited branch-set labels; or
3. a recursive exact-seven instance preserving the selected complete
   partition and all inherited labels.

The next theorem must use the literal first-hit locations and the
operation-specific Hall deficiency to obtain one of those conclusions.
Merely applying another boundary operation or obtaining another unlabelled
fan does not close the interface.

## 5. Audited dependencies

- [concentrated three-owner order-eight reduction](../results/hc7_three_owner_order8_exact7_reduction.md), Sections 1--2; [audit](../results/hc7_three_owner_order8_exact7_reduction_audit.md)
- [exact-seven full-subgraph packing](../results/hc7_exact_seven_packet_packing.md), Theorem 1; [audit](../results/hc7_exact_seven_packet_packing_audit.md)
- [adaptive exact-seven reflection](../results/hc7_exact7_adaptive_packet_reflection.md), Lemma 2.1 and Theorem 1.1; [audit](../results/hc7_exact7_adaptive_packet_reflection_audit.md)
- [exact-seven boundary classification and no-rigid-trace theorem](../results/hc7_exact7_no_rigid_trace.md), Corollaries 2.2--2.3; [audit](../results/hc7_exact7_no_rigid_trace_audit.md)
- [cycle-boundary completion](../results/hc7_cycle_boundary_completion.md); [audit](../results/hc7_cycle_boundary_completion_audit.md)
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md), Theorem 2.1; [audit](../results/hc7_transported_partition_hall_reflection_audit.md)
- [critical boundary-edge fan and strict descent](../results/hc7_exact7_critical_edge_fan_descent.md), Theorems 2.1 and 3.1 and Corollary 3.2; [audit](../results/hc7_exact7_critical_edge_fan_descent_audit.md)
