# Lock transfer at an edge of an ordered deficient-subgraph passage

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_passage_edge_lock_transfer_audit.md`](hc7_order8_passage_edge_lock_transfer_audit.md).  This is an
operation-specific reduction inside the connected order-eight
opposite-response interface.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
\]

and suppose that `G` is not six-colourable.  Let `d,e` be distinct
nonadjacent vertices of `S`, and write

\[
                   S-\{d,e\}=X\mathbin{\dot\cup}Y,
\]

where `X,Y` are nonempty independent sets.  Assume the following opposite
boundary responses.

1. The closed `L`-shore has a proper six-colouring `c` inducing

   \[
                        X\mid Y\mid\{d,e\}.            \tag{1.1}
   \]

2. The closed `R`-shore has a proper six-colouring inducing

   \[
                        X\mid Y\mid\{d\}\mid\{e\}.    \tag{1.2}
   \]

Write `alpha` for the common colour of `d,e` under `c`, and let
`beta` be one of the three colours absent from `S`.  Let `H` be the
connected component containing `d,e` in the subgraph of `G[L union S]`
induced by colours `alpha,beta`.  Such a component exists by the
three-colour-indexed Kempe-lock theorem.

Assume also the ordered-crossing conclusion for the deficient connected
subgraphs `A_e,A_d`: every `d`--`e` path with interior in `L` first meets
`A_e` and last meets `A_d`.  This assumption is used only to retain the
literal order after a rerouting.

## 2. Passage-edge lock-transfer theorem

### Theorem 2.1

Let `f=uv` be an edge on an `alpha`--`beta` `d`--`e` path in `H`.  Exactly
one of the following two alternatives applies.

1. **Ordered rerouting.**  The graph `H-f` contains a `d`--`e` path.  A
   shortest such path has all internal vertices in `L`, uses only the
   colours `alpha,beta`, first meets `A_e`, last meets `A_d`, and avoids
   `f`.
2. **Critical-edge lock transfer.**  The vertices `d,e` lie in different
   components of `H-f`.  The split partition (1.2) extends to a proper
   six-colouring of `G-f` in which `u,v` have one common colour.  The same
   colouring descends to `G/f`.  Moreover, in every proper six-colouring
   `phi` of `G-f`, if

   \[
                              \phi(u)=\phi(v)=\gamma,
   \]

   then, for every colour `delta` different from `gamma`, the vertices
   `u,v` lie in the same connected component of

   \[
                    (G-f)[\phi^{-1}(\{\gamma,\delta\})].           \tag{2.1}
   \]

   In particular, each end of `f` has a neighbour of every other colour.

The alternatives are exhaustive.  In the second alternative, no single
Kempe interchange in `G-f` can make the ends of `f` different while
preserving properness.

### Proof

If `H-f` still connects `d` to `e`, choose a shortest `d`--`e` path there.
The only boundary vertices with colours in `\{alpha,beta\}` are `d,e`:
the colour `beta` is absent from `S`, while the exact partition (1.1)
makes `d,e` the only boundary vertices of colour `alpha`.  Hence all
internal vertices of the path lie in `L`.  The ordered-crossing theorem
then says that it first meets `A_e` and last meets `A_d`.  This proves
alternative 1.

Suppose now that `H-f` does not connect `d` to `e`.  Since `f` lies on a
`d`--`e` path in `H`, it is a bridge separating `d` from `e`.  Let `D` be
the component of `H-f` containing `d`.  In the colouring `c` of the closed
`L`-shore with `f` deleted, interchange `alpha,beta` on `D`.  This is a
proper Kempe interchange in `G[L union S]-f`.  It changes the colour of
`d` and not the colour of `e`; it changes no vertex of `X union Y`.
Consequently the resulting colouring induces the exact split partition
(1.2) on `S`.

Align its four boundary-block colours with those of the assumed colouring
of `G[R union S]`.  The open shores are anticomplete, so the two colourings
glue to a proper six-colouring of `G-f`.

The ends `u,v` of the bridge lie in different components of `H-f`.  Before
the interchange their colours are `alpha,beta` in some order, and exactly
one endpoint belongs to `D`.  After the interchange their colours are
therefore equal.  The colouring consequently descends to the contraction
`G/f`.

It remains to prove the universal lock statement.  Let `phi` be any
proper six-colouring of `G-f`.  Since `G` itself is not six-colourable,
the two ends of `f` must have the same colour, say `gamma`; otherwise
restoring `f` would give a proper six-colouring of `G`.

Fix another colour `delta`.  If `u,v` belonged to distinct components of
the `gamma,delta`-coloured subgraph of `G-f`, interchange those colours on
the component containing `u`.  This preserves properness in `G-f`, makes
the colours of `u,v` different, and therefore permits `f` to be restored.
The result would be a proper six-colouring of `G`, a contradiction.  Thus
`u,v` lie in one component of (2.1).  A path between them in that
bichromatic component begins and ends with a `delta`-coloured neighbour,
so both endpoints see the colour `delta`.  This holds for each of the five
colours other than `gamma`.

Finally, a Kempe interchange which changes exactly one endpoint must use
`gamma` and some other colour and must interchange a component containing
one endpoint but not the other.  The preceding paragraph excludes every
such component.  This proves the final assertion and the theorem.
\(\square\)

## 3. Two-edge coupling: the exact response cube

The preceding theorem shows that a one-edge operation is necessarily
self-locking in the critical alternative.  The next elementary statement
records exactly what two vertex-disjoint such edges provide before any
label-preserving model extraction.

### Proposition 3.1

Assume that `f_1=u_1v_1` and `f_2=u_2v_2` are vertex-disjoint edges of
`G`.  Put

\[
                              J=G-\{f_1,f_2\}.
\]

If every proper minor of `G` is six-colourable, then `J` has proper
six-colourings with each of the three equality signatures

\[
             (=,=),\qquad (=,\ne),\qquad(\ne,=)                   \tag{3.1}
\]

on `(f_1,f_2)`, and it has no proper six-colouring in which both deleted
edges have differently coloured ends.  In addition, `J` is at least
five-connected whenever `G` is seven-connected.

When `G` is seven-connected, if `J` is not six-connected, `G` has an
actual order-seven separation.  If `J` is six-connected, it has a
`K_4`-minor model rooted at `u_1,v_1,u_2,v_2`.

#### Proof

Contract any nonempty subset of the two independent edges, six-colour the
resulting proper minor, expand the contracted edges, and leave both edges
deleted.  This gives the three signatures in (3.1).  A colouring with both
edges proper would remain proper after restoring them and would
six-colour `G`.

The remaining assertions are the two-edge case of the audited
[matching-deletion separator budget](../results/hc7_matching_deletion_separator_lift.md)
and the audited
[two-independent-critical-edge placement theorem](../results/hc7_two_edge_opposite_shore_or_rooted_k4.md).
For completeness, that budget gives `kappa(J)>=5`.  At an order-five
separation both deleted edges cross.  Orient their ends as

\[
                    f_1=a_1b_1,\qquad f_2=a_2b_2,
              \qquad a_1,a_2\in A,\quad b_1,b_2\in B.
\]

Then `T union {b_1,a_2}` has order seven and separates the nonempty
residual sets containing `a_1` and `b_2`: the selected vertices meet the
only restored crossing edges, and `J-T` has no `A`--`B` edge.  Thus it is
an actual order-seven separator in `G`.

If `J` is six-connected, Jung's two-linkage theorem gives all three
pairings of the four nominated endpoints.  The rooted-`K_4`
characterization for a three-connected graph therefore gives a rooted
`K_4`-minor model. \(\square\)

Proposition 3.1 is included to make the remaining gap explicit.  Its
rooted `K_4` may traverse either deficient connected subgraph and may use
the two boundary-full subgraphs on the opposite shore.  It is not yet a
label-preserving split of `A_e,A_d`.  The order-seven separation likewise
does not automatically carry a common complete boundary partition.

### Proposition 3.2 (two private-colour bridges share the split trace)

Retain the fixed merged-root colouring `c`.  Let `beta_1,beta_2` be two
distinct colours absent from `S`.  For `i=1,2`, let `H_i` be the
`alpha,beta_i` component containing `d,e`, and let `f_i` be a bridge of
`H_i` separating `d` from `e`.  Suppose that `f_1,f_2` are
vertex-disjoint.  Then the common deletion

\[
                         J=G-\{f_1,f_2\}
\]

has two proper six-colourings with signatures

\[
                         (=,\ne),\qquad(\ne,=)          \tag{3.2}
\]

on `(f_1,f_2)`, and both induce the same exact boundary equality
partition

\[
                         X\mid Y\mid\{d\}\mid\{e\}.    \tag{3.3}
\]

Here “the same” means the same partition of the literal boundary; colour
names may be permuted.  If every proper minor of `G` is six-colourable,
`J` also has an `(=,=)` colouring and no colouring in which both deleted
edges have differently coloured ends.

#### Proof

Fix `i` and let `D_i` be the component containing `d` in `H_i-f_i`.
Interchange `alpha,beta_i` on `D_i`.  The proof of Theorem 2.1 shows that
this gives the split boundary partition and makes the two ends of `f_i`
equal.

The other edge `f_j`, where `j` is different from `i`, remains proper.
Before the interchange its endpoint colours are `alpha,beta_j` in some
order.  The interchange changes neither a `beta_j`-coloured vertex nor any
vertex to colour `beta_j`; it can only change the `alpha` endpoint to
`beta_i`.  Since `beta_i` and `beta_j` are distinct, the two endpoint
colours of `f_j` remain different.  The colouring therefore remains proper
when `f_j` is retained.  Gluing to the split-response colouring on the
closed `R`-shore gives a colouring of `J` of signature `(=,\ne)` when
`i=1`, and symmetrically one of signature `(\ne,=)` when `i=2`.  Both have
the literal partition (3.3).

Contracting both independent edges and six-colouring the resulting proper
minor gives the `(=,=)` signature after expansion.  A colouring of `J`
in which both deleted edges have differently coloured ends would permit
both edges to be restored and would six-colour `G`.
This proves the proposition. \(\square\)

Proposition 3.2 is the precise extra information supplied by two
colour-indexed passage bridges: the two one-edge responses agree on the
old eight-vertex boundary.  It does not say that they agree on the new
seven-vertex boundary returned by Proposition 3.1.

## 4. Why the two-edge static upgrade is false

The two-edge coupling does not make an arbitrary endpoint-rooted `K_4`
label-preserving.  The solver-free
[`rooted-K_4` upgrade barrier](../barriers/hc7_exact7_rooted_k4_k7_upgrade_barrier.md)
contains the relevant rooted four-terminal expansion and a labelled
near-`K_7` model but has treewidth at most five, hence no `K_7` minor.
Thus the overstrong implication

\[
 \text{endpoint-rooted `K_4` plus the static completing contacts}
 \Longrightarrow K_7
\]

is genuinely false.  That barrier does not carry the operation-specific
common split trace in Proposition 3.2, so it does not refute the full live
disjunction.  Conversely, the audited exact-seven two-edge response
barriers carry the equality-signature cube and common traces but already
contain a `K_7` minor.  Together these examples show exactly which coupling
has not yet been decoded: the common split trace must control the literal
first intersections of the rooted `K_4` branch sets with `A_e,A_d`.

## 5. Exact gain and trust boundary

For an edge of one of the three colour-indexed ordered passages, the
theorem gives a complete operation-level dichotomy:

- the same colour-indexed, label-ordered passage can be rerouted around the
  edge; or
- deleting the edge unlocks the split boundary partition but transfers the
  obstruction to a five-colour-locked critical edge.

Thus deleting or contracting a first passage edge is not by itself a
colour-gluing conclusion in the original graph.  Any completion must use a
second edge or a literal branch-set split.  For two vertex-disjoint edges,
Proposition 3.1 supplies the exact equality-signature cube, an actual
order-seven separator, or an endpoint-rooted `K_4`; the still-open step is
to preserve the labels of `A_e,A_d` and of the completing branch sets.

## 6. Dependencies

- [ordered crossings of the deficient connected subgraphs](../results/hc7_order8_ordered_defect_crossing.md);
- [three colour-indexed Kempe locks on the merged-root shore](../results/hc7_merged_root_three_kempe_locks.md);
- the split-root colouring on the opposite closed shore;
- the [matching-deletion separator budget](../results/hc7_matching_deletion_separator_lift.md);
- the [two-independent-critical-edge placement theorem](../results/hc7_two_edge_opposite_shore_or_rooted_k4.md);
- Jung's theorem that every six-connected graph is two-linked, quoted as
  Stephens--Ye, Theorem 1.1; and
- the rooted-`K_4` characterization of Fabila-Monroy and Wood, Theorem 8.
