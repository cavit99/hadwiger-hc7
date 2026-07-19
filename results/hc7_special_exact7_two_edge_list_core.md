# Two distinguished boundary vertices yield a singleton shore or a two-root list-critical core

**Status:** written proof; separate internal audit GREEN in
[`hc7_special_exact7_two_edge_list_core_audit.md`](hc7_special_exact7_two_edge_list_core_audit.md).
This note couples the two distinguished boundary vertices in the audited
special five-plus-two exact-seven separation.  It gives a strict
connected-subgraph reduction or a shore-filling list-critical core.  The
reduction is not yet a recursive instance of the same special separation.
It does not force the new separator to have order seven, preserve either
selected one-edge boundary partition, construct a `K_7`-minor model, or
prove `HC_7`.

## 1. Setting

Assume the complete setting of the audited
[special five-plus-two exact-seven response theorem](../results/hc7_special_five_plus_two_exact7_response.md).
Thus

\[
 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad Y=Y_0\mathbin{\dot\cup}\{z_1,z_2\},
 \qquad |Y_0|=5,
\tag{1.1}
\]

both open shores are nonempty, `Y=N_G(A)`, `G` is seven-connected and
seven-chromatic, `G` has no `K_7` minor, and every proper minor of `G` is
six-colourable.

## 2. Two disjoint entrance edges or a singleton shore

### Lemma 2.1

Exactly one of the following alternatives holds.

1. `A={a}` for one vertex `a`, and

   \[
                           N_G(a)=Y,
                           \qquad d_G(a)=7,
                           \qquad \nu_B=1.
   \tag{2.1}
   \]

   Moreover, `B` is connected.

2. There are distinct vertices `a_1,a_2 in A` such that

   \[
                           z_1a_1,z_2a_2\in E(G).
   \tag{2.2}
   \]

#### Proof

Every vertex of `Y=N_G(A)`, and in particular each `z_i`, has a neighbour
in `A`.  If the two neighbourhoods `N_A(z_1),N_A(z_2)` do not have distinct
representatives, Hall's theorem for this two-set family says

\[
                         N_A(z_1)=N_A(z_2)=\{a\}
\tag{2.3}
\]

for one vertex `a`.

Suppose `A-a` is nonempty and let `C` be one of its components.  The set
`A` is a component of `G-Y`; hence no vertex of `C` has a neighbour in
`B`.  Equation (2.3) says that neither `z_1` nor `z_2` has a neighbour in
`C`.  Componenthood inside `A-a` therefore gives

\[
                       N_G(C)\subseteq\{a\}\cup Y_0.
\tag{2.4}
\]

The right side has order six and separates the nonempty set `C` from the
nonempty opposite shore `B`, contradicting seven-connectivity.  Thus
`A={a}`.  Since `A` is a component of `G-Y` and `Y=N_G(A)`, the first two
equalities in (2.1) follow.

It remains to exclude `nu_B=2` in this singleton alternative.  The adaptive
`(1,2)` boundary theorem places every surviving boundary in its audited
129-graph residual.  Dirac's neighbourhood inequality at the degree-seven
vertex `a` gives `alpha(G[Y])<=2`.  The audited residual extraction leaves
only the Moser spindle `M` and its one-edge extension `M+13`.  If `B` is
connected, the one-anchor connected-rich theorem eliminates both boundary
graphs.

Suppose instead that `B` is disconnected.  Every component is `Y`-full,
so `nu_B=2` makes `B` the union of exactly two components `B_1,B_2`.
Relative to the degree-seven vertex `a`, the graph `G-N_G[a]` therefore has
exactly these two components, both full to `Y=N_G(a)`.  The complete
pure-Moser two-component theorem excludes `G[Y]=M`.

For completeness, the remaining `M+13` case has a direct colouring
contradiction.  Use its standard labelling, in which `25` and `46` are
vertex-disjoint nonedges and `013` is a triangle.  To colour
`G[Y\cup B_i]`, let `j\ne i` and contract the two disjoint connected sets

\[
                         \{a,2,5\},\qquad B_j\cup\{4,6\}.
\tag{2.5}
\]

Their images are adjacent, and together with the literal triangle `013`
they form a `K_5`: the first image sees the triangle through `a`, and the
second sees it through the `Y`-full component `B_j`.  Six-colour this
proper minor and restrict to the untouched closed shore.  It induces the
exact boundary partition

\[
                         25\mid46\mid0\mid1\mid3.
\tag{2.6}
\]

Repeating the construction for `i=1,2`, aligning the five boundary blocks,
and assigning to `a` the sixth colour absent from `Y` gives a six-colouring
of `G`, a contradiction.  Thus the disconnected case is also impossible,
and `nu_B=1`.  Since every component of `B` is `Y`-full, this also shows
that `B` is connected.  Otherwise the two-set Hall condition holds and
gives the distinct representatives in (2.2).
\(\square\)

## 3. The coupled two-edge response

Assume alternative 2 of Lemma 2.1 and put

\[
                         e_i=z_ia_i\qquad(i=1,2).
\tag{3.1}
\]

The edges are vertex-disjoint.  Contract both and six-colour the resulting
proper minor.  Expanding the two contraction images gives a proper
six-colouring `psi` of `G-{e_1,e_2}` satisfying

\[
                    \psi(z_i)=\psi(a_i)\qquad(i=1,2).
\tag{3.2}
\]

For `v in A`, define

\[
 \mathcal L(v)=[6]\setminus
   \{\psi(y):y\in N_G(v)\cap Y\}.
\tag{3.3}
\]

### Lemma 3.1 (the three response chambers)

The graph `G-{e_1,e_2}` has six-colourings with each of the endpoint
signatures

\[
      (\mathrm{equal},\mathrm{proper}),\qquad
      (\mathrm{proper},\mathrm{equal}),\qquad
      (\mathrm{equal},\mathrm{equal}),
\tag{3.4}
\]

and none with signature `(proper,proper)`.  Every exact boundary partition
induced by any of these colourings

1. extends through the original closed shore `G[B\cup Y]`;
2. does not extend through `G[A\cup Y]`;
3. has full-subgraph demand greater than `nu_B`; and
4. satisfies the mixed-support Hall-deficiency conclusion of Theorem 2.1(3)
   in the special five-plus-two response theorem.

#### Proof

A six-colouring of `G-e_1` makes the ends of `e_1` monochromatic—otherwise
restoring that edge would six-colour `G`.  It restricts to a colouring of
the double deletion with the first edge monochromatic and the still-present
second edge proper.  Interchanging the edges gives the second signature.
Contracting both
vertex-disjoint edges and expanding their images gives the third.  A
`(proper,proper)` colouring would already colour `G`.

Both deleted edges lie between `A` and `Y`, so every displayed colouring
restricts properly to `G[B\cup Y]`.  If its exact boundary partition also
extended through the intact closed `A`-shore, the two colourings would
align by a global permutation of the six colours and glue, contradicting
`chi(G)=7`.

Choose `nu_B` disjoint `Y`-full connected subgraphs in `B`.  Apply the
transported-partition Hall theorem with its two shore names interchanged.
If the displayed partition had demand at most `nu_B`, the full connected
subgraphs would reflect it through `B` to the original closed `A`-shore,
contrary to the preceding paragraph.  Thus its demand is greater than
`nu_B`.  For every additional support family allowed in Theorem 2.1(3) of
the special response theorem, a saturating matching would give the same
forbidden reflection.  Hall's theorem therefore supplies exactly the
deficient block family asserted there.  This argument applies equally to
the double-equality partition; it uses its legality on `B`, not an
incorrect claim that it comes from a one-edge deletion colouring.
\(\square\)

### Theorem 3.2 (two-root list-critical reduction)

There is a connected induced subgraph `K` of `G[A]` such that:

1. `K` is not `\mathcal L`-colourable, every proper induced subgraph of `K`
   is `\mathcal L`-colourable, and

   \[
                         V(K)\cap\{a_1,a_2\}\ne\varnothing;
   \tag{3.5}
   \]

2. `psi|K` uses a colour from `\mathcal L(v)` at every vertex other than
   possibly `a_1,a_2`, and at `a_i` only the additional colour
   `psi(a_i)=psi(z_i)` may be used;
3. every `v in V(K)` satisfies

   \[
                              d_K(v)\ge|\mathcal L(v)|;
   \tag{3.6}
   \]

4. with

   \[
                         T=N_G(V(K)),
   \tag{3.7}
   \]

   the set `T` is the boundary of an actual separation, `|T|>=7`, and
   `K\subsetneq A` implies `|V(K)|<|A|`;
5. the common assignment `psi|T` has exactly one of the following three
   placements:

   - both `a_1,a_2` lie in `K`; the opposite closed shore is properly
     coloured by `psi`, while the `K`-side fails only on `e_1,e_2` and
     rejects the common proper boundary assignment;
   - exactly one `a_i` lies in `K`, and the other deleted edge lies only on
     the opposite closed shore; the two failed edges are on opposite
     sides of the returned separation and `psi|T` is proper; or
   - exactly one `a_i` lies in `K`, and the other deleted edge lies in the
     literal boundary graph `G[T]`; this is the only placement in which
     `psi|T` is improper.

In particular, `K\subsetneq A` is a strict host-level connected-side
descent carrying one common double-contraction assignment.  If `K=A`, then
both `a_1,a_2` lie in `K` and the whole exposed shore is a two-root
list-critical graph.

#### Proof

Apply Theorem 2.1 of the audited
[two-edge list-critical descent](../results/hc7_direct_entry_two_edge_list_core.md)
with its shore names

\[
                  L=B,\qquad S=Y,\qquad R=A,
\tag{3.8}
\]

and with

\[
                  x=z_1,\quad p=a_1,\quad
                  y=z_2,\quad q_0=a_2.
\tag{3.9}
\]

Equation (1.1) supplies the actual separation and (3.1) supplies the two
vertex-disjoint edges required by that theorem.  Its list (1.4) is exactly
`\mathcal L` in (3.3), and its expanded double-contraction colouring is
`psi`.  Its five conclusions give items 1--5 verbatim.  \(\square\)

## 4. The shore-filling equality case

Assume `K=A`.  For `v in A`, put

\[
\begin{aligned}
 c_Y(v)&=|\{\psi(y):y\in N_G(v)\cap Y\}|,\\
 \rho(v)&=|N_G(v)\cap Y|-c_Y(v),\\
 \varepsilon(v)&=d_{G[A]}(v)-|\mathcal L(v)|.
\end{aligned}
\tag{4.1}
\]

### Corollary 4.1

For every `v in A`,

\[
                         d_G(v)=6+\varepsilon(v)+\rho(v).
\tag{4.2}
\]

Consequently, if some vertex satisfies

\[
                         \varepsilon(v)+\rho(v)\le2,
\tag{4.3}
\]

then `N_G(v)` is the boundary of an actual singleton-side separation of
order seven or eight.  If `\varepsilon(v)=0` for every `v in A`, every
block of `G[A]` is a complete graph or an odd cycle.

#### Proof

These are Corollaries 3.1 and 3.2 of the cited two-edge list-critical
theorem, with the identification (3.7).  Since `A` is the whole open shore,
all neighbours of `v` lie in `A\cup Y`, and its displayed calculation
gives (4.2).  Seven-connectivity and (4.3) give degree seven or eight, and
`B` is a nonempty opposite shore.  The final assertion is the
degree-choosability theorem applied exactly as in the cited corollary.
\(\square\)

## 5. Exact remaining gap

This theorem gives a genuine finite descent in `|A|` when `K\subsetneq A`,
but it deliberately does not call that descent terminal.  The new
boundary `T` may have order greater than seven, and the common assignment
may have one failed edge on each closed shore or one failed boundary edge.
Moreover, the double-contraction partition need not equal either selected
one-edge partition from the special five-plus-two theorem.  The audited
two-edge deletion-lattice barrier shows that those three responses do not
force a fourth compatible partition abstractly.

In the shore-filling case the degree identity is exact, but it does not
force a vertex satisfying (4.3).  The next theorem must use the inherited
branch-set labels and global `K_7`-minor exclusion to do one of:

1. bound `|T|` by seven and repair every failed edge while retaining the
   complete boundary partition;
2. turn the two-root list-critical core into an explicit labelled
   `K_7`-minor model; or
3. force the low-excess alternative (4.3), after which the exact-seven or
   order-eight interface machinery applies.

## 6. Dependencies

- [special five-plus-two exact-seven response](../results/hc7_special_five_plus_two_exact7_response.md)
- [adaptive `(1,2)` boundary closure](../results/hc7_exact7_adaptive_12_boundary_closure.md)
- [singleton-thin residual extraction](../results/hc7_exact7_singleton_thin_moser_extension_escape.md)
- [complete pure-Moser two-component closure](../results/hc7_exact7_moser_two_component_closure.md)
- [direct two-anchor `M+13` construction](../results/hc7_exact7_two_component_singleton_closure.md)
- [exact packet reflection](../results/hc7_exact7_adaptive_packet_reflection.md)
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md)
- [two-edge list-critical descent](../results/hc7_direct_entry_two_edge_list_core.md)
- [two-edge deletion-lattice barrier](../barriers/hc7_two_edge_deletion_lattice_barrier.md)
