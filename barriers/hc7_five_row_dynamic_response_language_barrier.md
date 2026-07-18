# A dynamic response-language barrier for five labelled branch sets

**Status:** written barrier to an intermediate proof mechanism; independent
audit pending.  This is not a counterexample to `HC_7`.

## 1. Statement refuted

The following information does not force a boundary colouring which is
monochromatic on every labelled branch-set intersection:

1. an order-seven boundary and two disjoint boundary-colouring extension
   languages;
2. five disjoint connected, pairwise adjacent subgraphs on one closed side,
   each adjacent to one distinguished boundary vertex and together covering
   the rest of the boundary;
3. a member of the five with empty boundary intersection;
4. six-colourability after every proper minor operation supported wholly
   in the open side; and
5. for every such critical edge and every alternate colour, the usual
   bichromatic connection between its two endpoints.

Thus the family of all proper-minor equality-partition responses, even with
the unlabelled Kempe connections forced by criticality, cannot prove the
universal row-response theorem.  A positive theorem must use the literal
first-hit locations of those connections, seven-connectivity together with
the full-neighbourhood geometry, `K_7`-minor exclusion, or the global
two-vertex-transversal alternative.

## 2. A five-row scaffold preserves every extension language

Let `T` be a labelled boundary with a distinguished vertex `a`, and fix a
partition

\[
                     T-\{a\}=T_1\mathbin{\dot\cup}\cdots
                     \mathbin{\dot\cup}T_5.                 \tag{2.1}
\]

Let `R_0` be any `T`-boundaried graph.  Add new vertices
`r_1,...,r_5` which induce a `K_5`, and join `a` to every `r_i`.  For each
`t in T_i`, add a new vertex `p_t` and the two-edge path

\[
                              t-p_t-r_i.                     \tag{2.2}
\]

Put

\[
             Q_i=\{r_i\}\cup\{p_t,t:t\in T_i\}.             \tag{2.3}
\]

The five sets in (2.3) are pairwise disjoint and connected, are pairwise
adjacent through the clique on the `r_i`, and are each adjacent to `a`.
They cover `T-{a}`.

### Lemma 2.1 (language preservation)

The augmented graph `R` has exactly the same six-colouring extension
language on `T` as `R_0`.

#### Proof

Restriction from `R` to `R_0` proves one inclusion.  Conversely, fix a
six-colouring of `R_0`.  Colour `r_1,...,r_5` bijectively with the five
colours different from the colour of `a`.  For every `t in T_i`, the new
vertex `p_t` has only the two already coloured neighbours `t,r_i`; one of
the other four colours is available.  These choices are independent.
Thus every boundary colouring extending to `R_0` also extends to `R`.
\(\square\)

If some `T_i` contains an edge of the boundary graph, no proper colouring
of `R` is monochromatic on `T_i`.  Hence the five-row geometry can be
imposed on an arbitrary boundary extension language without creating even
one reflectable colouring.

## 3. Exact seven-vertex dynamic realization with independent row traces

Take

\[
              T=\{a,b,v_0,v_1,v_2,v_3,v_4\},
\]

and let the boundary graph be `K_2 join C_5`, with `a,b` the two universal
adjacent vertices.  Label the five cycle vertices so that its nonedges are

\[
                    e_i=v_iv_{i+1}\quad(i\in\mathbb Z_5).   \tag{3.1}
\]

Partition `T-{a}` by

\[
 T_1=\{b\},\quad T_2=e_0=\{v_0,v_1\},\quad
 T_3=e_2=\{v_2,v_3\},\quad T_4=\{v_4\},\quad
 T_5=\varnothing.                                           \tag{3.2}
\]

Every set in (3.2) is independent.  Let `mathcal S` be the five six-block
partitions whose sole nonsingleton block is one `e_i`, and let `mathcal D`
be the five five-block partitions whose nonsingleton blocks form a
two-edge matching in the complementary cycle (3.1).  The exact pentagonal
partition classification gives

\[
                        \Omega=\mathcal D\mathbin{\dot\cup}
                        \mathcal S.                           \tag{3.3}
\]

Both families meet every exact-independent-block cylinder.  Nevertheless
no member of `mathcal S` is monochromatic on both `T_2` and `T_3`: those
are two disjoint nonedges, while a member of `mathcal S` has only one
nonsingleton block.

The colouring-relation realization theorem of Dvorak--Swart gives
`T`-boundaried graphs `L_0,R_0` having exact extension languages
`mathcal D,mathcal S`.  Replace `R_0` by the five-row augmentation of
Section 2, which leaves its language equal to `mathcal S`, and glue it to
`L_0`.  The glued graph is not six-colourable.

Among all graphs obtained by taking a minor of the open part of `L_0`
(never deleting, identifying or contracting a member of `T`) for which
the glued graph remains non-six-colourable, choose a minor-minimal one.
Call the resulting glued graph `Gamma`.  Its right closed side and all
five labelled subgraphs are unchanged.

### Theorem 3.1 (all internal responses remain nonreflectable)

The graph `Gamma` is seven-chromatic.  Every proper minor operation whose
deletions and contractions are wholly in its open left side makes `Gamma`
six-colourable.  Nevertheless every six-colouring arising after any such
operation multicolours at least one of the two independent row traces
`T_2 subseteq Q_2` and `T_3 subseteq Q_3`.

For every internal edge `uv`, every six-colouring of `Gamma-uv` gives
`u,v` one common colour, and for each of the other five colours the two
vertices lie in one component of the corresponding bichromatic subgraph.
Thus adding the full family of standard edge-critical Kempe connections
does not change the conclusion.

#### Proof

The initial graph is not six-colourable because the two languages in
(3.3) are disjoint.  The defining minor-minimality of `Gamma` says exactly
that every proper minor supported wholly in its open left side is
six-colourable.  Its open left side is nonempty, since otherwise `Gamma`
would be a subgraph of the six-colourable right closed side.  Deleting one
open-left vertex and then giving that vertex a seventh colour proves
`chi(Gamma)<=7`; non-six-colourability proves equality.

In a colouring after deleting an internal edge `uv`, its endpoints must
be monochromatic; otherwise the edge could be restored, contrary to the
choice of `Gamma`.  (The contraction is six-colourable independently by
the same internal-minor minimality.)

Conversely, every colouring after any displayed operation restricts on
the unchanged right side to a member of `mathcal S`.  Such a partition has
only one nonsingleton block, whereas both `T_2=e_0` and `T_3=e_2` would
have to be nonsingleton blocks if both labelled intersections were
monochromatic.  Hence at least one of the two independent intersections is
multicoloured in every response.

Finally, if the two ends of a deleted internal edge lay in different
components of the subgraph induced by their common colour and an alternate
colour, interchange those colours on the component containing one end.
The edge could then be restored, six-colouring `Gamma`, a contradiction.
This proves all five bichromatic connections.  \(\square\)

## 4. Exact trust boundary

The construction proves a limitation of a proof language, not a graph
theorem under the complete `HC_7` hypotheses.  It is not asserted that
`Gamma` is seven-connected or `K_7`-minor-free, and the simultaneous
connected-full realization and internal proper-minor minimality of the left
open side are not supplied.  The minor-minimal open side need not remain
connected or adjacent to every boundary vertex.

Those omissions are precisely the remaining possible engines.  In the
actual five-row separator, a successful argument must convert the five
bichromatic paths into information about their first vertices in the named
subgraphs, or use failure of that conversion to expose a `K_7` model, an
exact order-seven separation with a common boundary partition, or a fixed
two-vertex `K_5`-minor transversal.  Merely enlarging the finite response
state space cannot do so.

## Dependencies

- [complementary-state realization barrier](hc7_state_realization_barrier.md)
- [pentagonal dynamic-language barrier](hc7_exact7_pentagonal_dynamic_language_barrier.md)
- [five-row reflection theorem](../results/hc7_five_row_separator_reflection.md)
