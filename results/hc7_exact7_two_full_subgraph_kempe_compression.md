# Two full connected subgraphs force a first-hit Kempe path

**Status:** written proof; separate internal audit.  This is a conditional
transition lemma for an exact order-seven
separator.  It either synchronizes the complete boundary equality partition
or forces a literal bichromatic path to enter one of two named connected
subgraphs.  It does not supply those subgraphs and does not prove `HC_7`.

## 1. Setup

Let `G` be a graph which is not six-colourable and every proper minor of
which is six-colourable.  Let

\[
        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
        \qquad E_G(A,B)=\varnothing,                    \tag{1.1}
\]

where `A,B` are nonempty and

\[
 S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
 \qquad |D|=3,\quad |E|=2.                             \tag{1.2}
\]

Put `H=G[S]`.  Suppose `G[A union S]` has a proper six-colouring `c`
such that `D` and `E` are monochromatic in two distinct colours.  No
condition is initially imposed on the colours of `r,z`.  Let `Pi` be the
complete equality partition induced by `c` on `S`.

Suppose `G[A]` contains two vertex-disjoint connected subgraphs `C_D,C_E`,
each adjacent to every literal vertex of `S`.

These are literal host subgraphs, not quotient vertices.  In the terminology
of the exact packet-reflection lemma, they are two disjoint `S`-full packets.

## 2. The demand reduction

For a partition `Omega` of `S` into independent blocks, write

\[
 \operatorname{sing}(\Omega)
   =\{s\in S:\{s\}\in\Omega\},
 \qquad
 d_H(\Omega)
   =|\Omega|-\omega\bigl(H[\operatorname{sing}(\Omega)]\bigr). \tag{2.1}
\]

The [exact packet-reflection lemma](../results/hc7_exact7_adaptive_packet_reflection.md)
says that if one open shore contains `q` disjoint `S`-full packets and
`d_H(Omega)<=q`, then contractions supported in that closed shore produce
either a `K_7`-minor model or a proper-minor colouring of the opposite
closed shore whose equality partition on the literal boundary is exactly
`Omega`.  In the present application `q=2` and `|Pi|<=4`, so the seven-block
`K_7` alternative in the proof of that lemma cannot occur.  Hence

\[
                         d_H(\Pi)\le2                  \tag{2.2}
\]

immediately gives a colouring of `G[B union S]` with exact boundary
partition `Pi`; after a permutation of colour names it glues to `c`.

It remains to classify `d_H(Pi)>2`.  The blocks containing `D` and `E` are
distinct.  If either `r` or `z` joins one of those blocks, then `Pi` has at
most three blocks; in the three-block case the other displayed vertex is a
singleton, so `d_H(Pi)<=3-1=2`.  If neither joins those blocks, there are
only two possibilities:

\[
 \begin{aligned}
   \Pi_A&=D\mid E\mid\{r\}\mid\{z\},\\
   \Pi_B&=D\mid E\mid\{r,z\}.
 \end{aligned}                                        \tag{2.3}
\]

For `Pi_A`, the singleton graph is `H[{r,z}]`.  Thus its demand exceeds
two exactly when `rz` is not an edge.  The partition `Pi_B` has no singleton
blocks and has demand three.  Consequently

\[
 d_H(\Pi)>2
 \quad\Longleftrightarrow\quad
 \Pi=\Pi_A\text{ with }rz\notin E(G),
 \quad\text{or}\quad
 \Pi=\Pi_B.                                           \tag{2.4}
\]

This short calculation is the only boundary-state enumeration used below.

## 3. Synchronization or first entry

### Theorem 3.1

Under the setup in Section 1, one of the following holds.

1. `G` is six-colourable.
2. `Pi=Pi_A`, and the two-colour subgraph of `G[A union S]` induced by
   `c(r),c(z)` contains an `r-z` path with interior in `A`; every such path
   meets `C_D union C_E`.
3. `Pi=Pi_B`, and for some colour `theta` absent from `S` under `c`, the
   two-colour subgraph induced by `c(r),theta` contains an `r-z` path with
   interior in `A`; every such path meets `C_D union C_E`.

In either path outcome, a shortest path has a well-defined first vertex in
the two named connected subgraphs.  Thus failure of synchronization returns
a literal label-preserving first-entry point.

### Proof

If `d_H(Pi)<=2`, exact packet reflection gives outcome 1 as explained in
Section 2.  Hence assume `d_H(Pi)>2`, so (2.4) applies.

Put

\[
                 K_D=C_D\cup D,\qquad K_E=C_E\cup E.   \tag{3.1}
\]

Both sets induce connected subgraphs and they are disjoint.  They are also
adjacent: fullness of `C_D` supplies an edge from `C_D` to every vertex of
`E subseteq K_E` (and symmetrically fullness of `C_E` supplies edges into
`D subseteq K_D`).  Contract a spanning tree in each set.  This is a proper
minor, so it has a proper six-colouring.  Expand that colouring only on the
unchanged closed side `G[B union S]`.

The two contracted representatives are adjacent to one another and to both
`r,z`.  Consequently the resulting boundary partition has `D,E` as two
exact blocks with distinct colours, and neither `r` nor `z` uses either
block colour.  There are exactly two possible returned partitions:

\[
                         \Pi_A,\qquad \Pi_B.            \tag{3.2}
\]

We now treat the two possible original partitions separately.

#### Case A: the original partition is `Pi_A`

If the returned partition is `Pi_A`, permute the six colour names on one
closed side and glue, giving outcome 1.  Suppose it is `Pi_B`.  Write

\[
                         \gamma=c(r),\qquad
                         \eta=c(z).                     \tag{3.3}
\]

These colours are distinct.  Consider the `gamma,eta` Kempe component in
`G[A union S]` containing `r`.  If it does not contain `z`, interchange
the two colours on that component.  The only boundary vertices with either
colour are `r,z`; hence the interchange changes only `r` on the boundary,
produces `Pi_B`, and glues to the returned colouring.

Therefore the component contains `z`.  Every `r-z` path in it has all
internal vertices in `A`, because no other boundary vertex uses either
colour.  Suppose such a path `P` avoids `C_D union C_E`.  Split `P` at any
edge into two nonempty connected vertex sets `P_r,P_z` containing `r,z`,
respectively.  The four connected sets

\[
                         K_D,\quad K_E,\quad P_r,\quad P_z              \tag{3.4}
\]

are pairwise disjoint and pairwise adjacent.  The only non-immediate
adjacencies are from `K_D` or `K_E` to a path part, and these are supplied
by the full subgraph's contact with the boundary vertex `r` or `z` in that
part.  Contracting spanning trees in (3.4) therefore forces exact partition
`Pi_A` on the untouched closed side `G[B union S]`, which glues to `c`.
Thus every such path meets the named union, giving outcome 2.

#### Case B: the original partition is `Pi_B`

Put

\[
                         \kappa=c(r)=c(z).              \tag{3.5}
\]

If the returned partition is `Pi_B`, it glues to `c`.  Suppose it is
`Pi_A`.  Permute its six colour names so that its `D`- and `E`-colours
agree with those under `c`, its colour at `z` is `kappa`, and its colour
at `r` is a colour `theta` absent from the boundary under `c`.  This is
possible: the returned four blocks have four distinct colours, whereas
`c` uses only the three block colours of `Pi_B` on `S`, leaving three
palette colours absent there.

Consider the `kappa,theta` Kempe component of `G[A union S]` containing
`r`.  If it does not contain `z`, interchange the two colours on that
component.  On the boundary, `theta` is absent and `kappa` occurs exactly
at `r,z`; hence only `r` changes.  The resulting boundary partition and
colour names agree with the returned `Pi_A` colouring, so they glue.

Therefore the component contains `z`, and every `r-z` path in it has all
internal vertices in `A`.  Suppose such a path `P` avoids
`C_D union C_E`.  This time keep the whole path as one connected set.  The
three sets

\[
                              K_D,\quad K_E,\quad V(P)                 \tag{3.6}
\]

   are pairwise disjoint and pairwise adjacent: each full subgraph contacts
   `r` (and `z`) on `P`, while fullness supplies the adjacency between
   `K_D,K_E`.  Contract
a spanning tree in each of (3.6).  The three clique representatives contain
the boundary blocks `D,E,{r,z}` and therefore force exact partition `Pi_B`
on the untouched closed side.  It glues to `c`, giving outcome 1.

Hence every `kappa,theta` path joining `r` to `z` meets the named union,
which is outcome 3.  This completes the proof.  \(\square\)

## 4. Application and exact residue

For the separator returned by the Kempe-fan theorem, the intended
substitution is

\[
              D=J\cup\{q\},\qquad E=\{b,z_1\},
              \qquad z=z_2.                            \tag{4.1}
\]

The strengthened theorem removes the former exact-four-block normalization
gap.  It needs only a one-sided colouring in which `D` and `E` are
monochromatic in distinct colours, together with two disjoint `S`-full
connected subgraphs on that side.  The complete boundary partition
is then either reflected immediately because its packet demand is at most
two, or it is one of the two explicit high-demand partitions in (2.3),
where the Kempe argument gives the first-entry conclusion.

The theorem does **not** prove that every Kempe-fan separator supplies the
two required full connected subgraphs on the correctly coloured shore.
Nor does it act at the returned first entry.  Those are the remaining
host-level obligations: a further operation there must construct a
`K_7`-minor model, synchronize the boundary colouring, or produce a strict
descent through another actual separation.

## 5. Dependencies and trust boundary

- [Adaptive exact-seven packet reflection](../results/hc7_exact7_adaptive_packet_reflection.md),
  especially Lemma 2.1.
- [Kempe-fan packing or exact-seven boundary](../results/hc7_kempe_fan_or_exact_seven_boundary.md).
- [Boundary-operation parity barrier](../barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md).

The parity barrier shows why contractions and one-sided boundary partitions
alone cannot supply the missing subgraphs or close the first-entry step; its
host contains an explicit `K_7` minor and therefore does not refute this
conditional lemma in the `HC_7` setting.

This theorem assumes the exact two large monochromatic sets and the two
named disjoint full connected subgraphs.  It returns only a bichromatic path forced
to meet their union.  It does not identify a model-improving split at that
entry, bound the full neighbourhood of the first-hit component, or prove
`HC_7`.
