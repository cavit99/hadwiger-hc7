# Restarting the two-edge reduction at an arbitrary exact order-seven response boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_generic_exact7_response_restart_audit.md`](hc7_generic_exact7_response_restart_audit.md).

This theorem removes inherited-boundary-vertex retention from the recursive
part of the degree-seven programme.  At any exact order-seven separation,
one selected boundary-to-shore edge can be retained and paired with a
second vertex-disjoint entrance edge unless the connected shore is a
singleton.  The parameter-uniform two-edge list-critical reduction can
therefore be restarted without the special five-plus-two provenance.

If its list-critical core is proper and again has boundary order seven, one
of its marked edges supplies a fresh selected response on a strictly smaller
connected shore.  Thus loss of an inherited boundary vertex is not an
obstruction to **generic selected-response descent**.  What is lost is the
old near-clique branch-set labelling and the old mixed-support certificate.
The theorem does not control separator excess, eliminate the shore-filling
list-critical case, or prove `HC_7`.

## 1. Generic selected-response interfaces

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

A **generic exact-seven response interface** consists of a partition

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad S=N_G(A),
 \qquad |S|=7,
\tag{1.2}
\]

where `A` is connected and `A,B` are nonempty, together with an edge

\[
                             e=za,qquad z\in S, a\in A,
\tag{1.3}
\]

and a proper six-colouring `c` of `G-e`.  Let `Pi` be the equality
partition induced by `c` on `S`, and let `nu_B` be the maximum number of
pairwise vertex-disjoint connected subgraphs of `B` which are adjacent to
every literal vertex of `S`.

### Lemma 1.1 (automatic response properties)

Every interface in (1.2)--(1.3) has the following properties.

1. The colouring `c` is proper on `G[B\cup S]`, and `Pi` does not extend
   through the intact closed shore `G[A\cup S]`.
2. Every component of `G-S` is adjacent to every vertex of `S`.
3. Up to orienting the two open shores, their maximum numbers of disjoint
   boundary-full connected subgraphs are `(1,1)` or `(1,2)`.
4. `G[S]` is four-colourable.
5. With

   \[
      d_{G[S]}(\Pi)=|\Pi|-\omega
       \bigl(G[S][\operatorname{sing}(\Pi)]\bigr),
   \tag{1.4}
   \]

   one has

   \[
                             d_{G[S]}(\Pi)>\nu_B.
   \tag{1.5}
   \]

#### Proof

The only edge on which `c` can fail in `G` is `za`, and that edge does not
belong to `G[B\cup S]`.  If `Pi` extended through `G[A\cup S]`, a global
permutation of the six colours would align the two boundary assignments
and glue the closed-shore colourings to a six-colouring of `G`.  This proves
item 1.

Let `D` be a component of `G-S`.  Its neighbourhood is contained in `S`.
If it missed one vertex of `S`, at most six vertices would separate it from
the nonempty opposite open shore.  Seven-connectivity therefore makes `D`
adjacent to every literal boundary vertex, proving item 2.

The exact-seven full-subgraph packing theorem and adaptive `(1,3)`
reflection leave only `(1,1)` and `(1,2)`, up to orientation.  The
exact-seven boundary classification gives chromatic number at most five;
its sole five-chromatic boundary is eliminated by the cycle-boundary
completion theorem.  This proves items 3 and 4.

Finally, if (1.5) failed, the `nu_B` disjoint boundary-full connected
subgraphs on the legal shore would reproduce `Pi` through the rejecting
shore by exact full-subgraph reflection, or would give an explicit
`K_7`-minor model.  The first conclusion contradicts item 1 and the second
contradicts (1.1).  This proves item 5. \(\square\)

## 2. A second disjoint entrance edge

### Lemma 2.1

In a generic exact-seven response interface, either `A={a}` or there are
vertices

\[
                  z'\in S-\{z\},\qquad a'\in A-\{a\}
\tag{2.1}
\]

such that `z'a'` is an edge.  In the latter case `za,z'a'` are
vertex-disjoint entrance edges, and the originally selected edge `za` is
retained.

#### Proof

Suppose `A-\{a\}` is nonempty, and let `C` be one of its components.  If
no vertex of `S-\{z\}` had a neighbour in `C`, then componenthood inside
`A-\{a\}`, together with `E_G(A,B)=\varnothing`, would give

\[
                              N_G(C)\subseteq\{a,z\}.
\tag{2.2}
\]

The nonempty set `C` would then be separated from the nonempty opposite
shore `B` by at most two vertices, contrary to seven-connectivity.  Hence
some `z'\in S-\{z\}` has a neighbour `a'\in C`.  The four displayed
endpoints are distinct, proving the lemma. \(\square\)

## 3. Generic two-edge restart and strict descent

### Theorem 3.1

Every generic exact-seven response interface has at least one of the
following outcomes.

1. **Singleton shore.**  `A={a}` and `N_G(a)=S`, so `d_G(a)=7`.
2. **Strict generic exact-seven descent.**  There is another generic
   exact-seven response interface in the same graph whose connected open
   shore `K` satisfies

   \[
                               |K|<|A|.
   \tag{3.1}
   \]

3. **Separator excess.**  There is a connected induced list-critical
   subgraph `K\subsetneq A` whose full neighbourhood is the boundary of an
   actual separation and has order at least eight.
4. **Shore-filling two-root obstruction.**  The whole graph `G[A]` is the
   two-root list-critical graph produced by simultaneous contraction of two
   vertex-disjoint entrance edges.

In outcomes 2--4 the two-edge list-critical core and its lists satisfy all
conclusions of the parameter-uniform two-edge list-critical descent
theorem.  Outcome 2 retains an operation-specific one-edge response, but
need not retain the old partition `Pi`, the old five-plus-two boundary
vertices, or the old near-clique branch-set labels.

#### Proof

If `A={a}`, (1.2) gives outcome 1.  Otherwise apply Lemma 2.1 and put

\[
                         e_1=za,qquad e_2=z'a'.
\tag{3.2}
\]

Contract both edges, six-colour the resulting proper minor, and expand the
two contraction images.  Apply the parameter-uniform two-edge
list-critical descent theorem to the separation (1.2), with `A` as its
operated shore.  It gives a connected induced list-critical subgraph
`K\subseteq A`, meeting at least one of `a,a'`, and an actual separation
with boundary

\[
                              T=N_G(K),\qquad |T|\ge7.
\tag{3.3}
\]

If `K=A`, this is outcome 4.  Suppose `K\subsetneq A`.  Then
`|K|<|A|`.  If `|T|\ge8`, outcome 3 holds.

It remains that `|T|=7`.  Choose `i\in\{1,2\}` whose operated-shore end
`a_i` belongs to `K`, and let `c_i` be any proper six-colouring of
`G-e_i`.  The edge `e_i` crosses from `K` to `T`, so `c_i` is proper on
the closed shore opposite `K`.  Its exact equality partition on `T` cannot
extend through the intact closed `K`-shore, since two such colourings would
glue and six-colour `G`.

The set `K` is connected and nonempty.  The old opposite shore `B` is
disjoint from `K\cup T`, because it is anticomplete to all of `A`; hence
the new opposite open shore is nonempty.  Also `T=N_G(K)`.  Thus

\[
 V(G)=K\mathbin{\dot\cup}T\mathbin{\dot\cup}
       \bigl(V(G)-(K\cup T)\bigr)
\tag{3.4}
\]

together with `e_i,c_i` is a generic exact-seven response interface.
Lemma 1.1 supplies its fullness, packing, four-colourability and demand
properties.  Equation (3.1) makes it a strict descent, proving outcome 2.
\(\square\)

### Corollary 3.2 (inherited-vertex loss is not a generic descent barrier)

Use the proper-core setting of the selected-response pullback theorem and
assume only that its full neighbourhood `T` has order seven.  No hypothesis
that the five old inherited vertices lie in `T` is needed: the selected
edge whose operated endpoint lies in the core makes `T` a strict generic
exact-seven response interface, and Theorem 3.1 applies.

#### Proof

The last two paragraphs of the proof of Theorem 3.1 apply verbatim to that
proper core. \(\square\)

## 4. Exact trust boundary

The theorem supplies a genuine induction on the order of the selected
connected shore whenever a proper core has boundary order exactly seven.
It therefore removes literal loss of an old inherited boundary vertex as a
barrier to **generic** response recursion.

It does not prove that outcome 3 can be tightened to order seven, eliminate
the singleton or shore-filling outcomes, preserve the selected complete
boundary partition, or allocate the old near-clique branch-set labels.  A
proof of `HC_7` still needs an operation-specific theorem for separator
excess and the positive-excess shore-filling core, together with the
remaining degree-eight and degree-nine interfaces.

## 5. Dependencies

- [parameter-uniform two-edge list-critical descent](hc7_direct_entry_two_edge_list_core.md)
- [exact-seven full-subgraph packing](hc7_exact_seven_packet_packing.md)
- [adaptive exact-seven reflection](hc7_exact7_adaptive_packet_reflection.md)
- [exact-seven boundary classification](hc7_exact7_no_rigid_trace.md)
- [cycle-boundary completion](hc7_cycle_boundary_completion.md)
- [selected-response pullback in the special interface](hc7_special_exact7_selected_response_pullback.md)
