# Relative eight-connectivity of a minimum exact-seven response shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_minimum_generic_exact7_relative_connectivity_audit.md`](hc7_minimum_generic_exact7_relative_connectivity_audit.md).

This note records a host-level consequence of minimizing the connected
shore in the generic exact-seven restart.  It does not use or preserve an
older near-clique model.  Its main conclusion is that every proper part of
the selected shore has at least eight literal neighbours.

## 1. Setting

Let `G` be a graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G,
 \tag{1.1}
\]

and suppose that `G` is seven-connected.  A **generic exact-seven
response interface** is the object defined in
[`hc7_generic_exact7_response_restart.md`](hc7_generic_exact7_response_restart.md):

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \quad S=N_G(A),\quad |S|=7,
 \quad A,B\ne\varnothing,
 \tag{1.2}
\]

where `A` is connected, together with a crossing edge `e=za`, `z in S`,
`a in A`, and a proper six-colouring of `G-e`.

Choose such an interface with `|A|` minimum among all generic exact-seven
response interfaces in the fixed graph `G`.

## 2. Proper subsets have eight neighbours

### Theorem 2.1

If `A` has at least two vertices, then every nonempty proper set
`U subsetneq A` satisfies

\[
                         |N_G(U)|\ge 8.                 \tag{2.1}
\]

#### Proof

First let `C` be a nonempty connected proper subset of `A`.  The opposite
side of the separation with boundary `N_G(C)` is nonempty: the old set
`B` is anticomplete to all of `A`, and hence is disjoint from
`C union N_G(C)`.  Seven-connectivity gives

\[
                         |N_G(C)|\ge 7.                 \tag{2.2}
\]

Suppose equality held.  Choose any edge `xy` with `x in C` and
`y in N_G(C)`.  The proper minor `G-xy` has a proper six-colouring.  Its
ends have the same colour, since otherwise that colouring would also be a
proper six-colouring of `G`.  Therefore

\[
 \bigl(C,N_G(C),V(G)-(C\cup N_G(C));\,xy\bigr)          \tag{2.3}
\]

together with this edge-deletion colouring is a generic exact-seven
response interface.  Since `|C|<|A|`, this contradicts the choice of `A`.
Thus every connected proper subset of `A` has at least eight neighbours.

Now let `U` be an arbitrary nonempty proper subset of `A`, and choose a
component `C` of `G[U]`.  There is no edge from `C` to `U-C`, so

\[
                         N_G(C)\subseteq N_G(U).        \tag{2.4}
\]

The connected set `C` is a proper subset of `A`; applying the first
paragraph to `C` proves (2.1). \(\square\)

## 3. The boundary-completed shore is eight-connected

Let `Q` be the graph obtained from `G[A union S]` by adding all missing
edges with both ends in `S`.

### Corollary 3.1

If `|A|>=2`, then `Q` is eight-connected.

#### Proof

The graph has at least nine vertices.  Let `Z subseteq V(Q)` have order at
most seven.  If some vertex of `S-Z` remains, all surviving boundary
vertices lie in one component of `Q-Z` because `S` is a clique in `Q`.
Any other component `D` of `Q-Z` is contained in `A` and has

\[
                         N_G(D)\subseteq Z.             \tag{3.1}
\]

It is a proper subset of `A`: every surviving boundary vertex has a
neighbour in `A`, and a component equal to all of `A` would therefore meet
the component containing `S-Z`.  Equation (3.1) contradicts Theorem 2.1.

If no boundary vertex remains, then `S subseteq Z`.  Since `|S|=7` and
`|Z|<=7`, one has `Z=S`; the graph `Q-Z=G[A]` is connected.  Hence
deleting at most seven vertices never disconnects `Q`. \(\square\)

### Corollary 3.2 (an order-eight component is boundary-full)

Let `T=N_G(K)` have order eight, where `K` is a nonempty connected proper
subset of `A`.  Every component `D` of `G-T` which is contained in `A` is
adjacent to every vertex of `T`.

#### Proof

Because `G[A]` is connected and `K` is a nonempty proper subset of `A`,
the set `N_G(K)=T` contains a vertex of `A-K`.  Hence every component of
`G-T` contained in `A` is a proper subset of `A`.  For such a component,
`N_G(D) subseteq T`.  Theorem 2.1 gives
`|N_G(D)|>=8`, while `|T|=8`; hence `N_G(D)=T`. \(\square\)

## 4. Exact trust boundary

The theorem gives a genuine host-measured normalization.  In particular,
an order-eight separator inside a minimum generic shore has no deficient
component on that shore.  The added clique edges in `Q` are auxiliary and
must not be used as literal host edges in a minor model.

The theorem does not make components on the opposite side boundary-full,
reduce a boundary of order at least eight to order seven, synchronize two
boundary colourings, allocate five named branch-set contacts, or prove
`HC_7`.

## 5. Dependency

- [generic exact-seven selected-response restart](hc7_generic_exact7_response_restart.md)
