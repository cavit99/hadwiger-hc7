# Proper paired list-critical subgraphs return a smaller connected response

**Archive note:** unaudited exploratory result retained for provenance; it
is not part of the current proof spine.

**Status:** written proof; separate audit pending.

This note continues the exact-block two-shore Kempe-transition theorem.  An
intermediate boundary colouring rejected by both shores gives one
list-critical induced subgraph in each shore.  If either subgraph is proper,
the unused part of that shore contains a strictly smaller connected subgraph
whose literal full neighbourhood carries a rejected colouring response.  If
neither is proper, both complete shores are vertex-minimal list-uncolourable
for the same fixed boundary colouring.  The result does not bound the new
full neighbourhood from above and does not close the shore-filling case.

## 1. Setting

Let

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,                       \tag{1.1}
\]

where `A,D` are nonempty and connected.  Assume

\[
 \chi(G)=7,\qquad \kappa(G)\ge7,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                                  \tag{1.2}
\]

Let `phi` be a proper six-colouring of `G[B]` which extends through neither
closed shore.  For `Z in {A,D}` and `v in Z`, put

\[
 L_Z(v)=[6]-\phi(N_G(v)\cap B).                                  \tag{1.3}
\]

Choose a connected induced subgraph `K_Z subseteq G[Z]` which is
vertex-minimal subject to not being `L_Z`-colourable.  Such subgraphs are
provided, for example, by the distance-at-least-two outcome of the
exact-block Kempe-transition theorem.

## 2. Proper-kernel transfer

### Theorem 2.1

Suppose `K_A` is a proper subgraph of `G[A]`.  Then there is a component
`R` of `G[A-V(K_A)]` with all of the following properties.

1. `R` is nonempty and connected, `|R|<|A|`, and its literal full
   neighbourhood

   \[
                              X=N_G(R)                            \tag{2.1}
   \]

   is the boundary of an actual separation with `|X|>=7`.
2. There is a proper six-colouring `c` of `G-R` whose restriction to `X`
   does not extend through the intact graph `G[R union X]`.
3. For every edge `xy` with `x in R` and `y in X`, every proper
   six-colouring of `G-xy` gives `x,y` one colour.  Its restriction to `X`
   extends through `G-R` and through `G[R union X]-xy`, but is rejected by
   `G[R union X]`.
4. If `|X|=7`, then every component of `G-X` is adjacent to every literal
   vertex of `X`.

The symmetric statement holds when `K_D` is proper.  Consequently the
paired list-critical outcome returns either such a strictly smaller
connected response side, or

\[
                              K_A=A,\qquad K_D=D.                  \tag{2.2}
\]

#### Proof

Let `R` be any component of `G[A-V(K_A)]`.  Delete `R`.  The resulting
graph is a proper minor of `G`, and hence has a proper six-colouring `c` by
(1.2).  If the labelled colouring `c|N_G(R)` extended through
`G[R union N_G(R)]`, that extension would glue directly to `c` and give a
proper six-colouring of all of `G`, contrary to (1.2).  This proves item 2.

The set `X=N_G(R)` separates `R` from the nonempty opposite shore `D`.
Seven-connectivity gives `|X|>=7`.  Since `K_A` is nonempty and `R` is a
component of its complement in `A`, one has `|R|<|A|`.  This proves item 1.

Fix a crossing edge `xy`.  Since `G-xy` is a proper minor, it has a proper
six-colouring.  The ends have one colour: otherwise restoring `xy` would
six-colour `G`.  The outside restriction colours `G-R`, while the inside
restriction colours `G[R union X]-xy`.  If the same boundary colouring
extended through the intact inside graph, that extension would glue to the
outside restriction and six-colour `G`.  Hence it is rejected by the intact
inside graph.  This proves item 3.

Finally suppose `|X|=7`, and let `C` be a component of `G-X`.  If `C`
missed some `z in X`, then

\[
                           N_G(C)\subseteq X-\{z\},
\]

an order-at-most-six separator.  There is another component of `G-X`
because `R` and the opposite shore `D` lie on different sides of `X`.
This contradicts seven-connectivity and proves item 4.  Applying the same
argument with `A,D` interchanged proves the symmetric assertion.  Therefore
failure of either proper-kernel alternative is exactly (2.2). \(\square\)

## 3. The paired shore-filling endpoint

### Proposition 3.1

Assume (2.2).  Then, for each `Z in {A,D}`:

1. `G[Z]` is vertex-minimal subject to not being `L_Z`-colourable;
2. for every `v in Z`, every `L_Z`-colouring of `G[Z]-v`, glued to `phi`
   on `B`, uses all six colours on `N_G(v) cap (Z union B)`;
3. every vertex satisfies

   \[
        d_{G[Z]}(v)\ge |L_Z(v)|;
                                                                  \tag{3.1}
   \]

4. if

   \[
   \begin{aligned}
       \varepsilon_Z(v)&=d_{G[Z]}(v)-|L_Z(v)|,\\
       \rho_Z(v)&=|N_G(v)\cap B|-|\phi(N_G(v)\cap B)|,
   \end{aligned}                                                   \tag{3.2}
   \]

   then

   \[
                       d_G(v)=6+\varepsilon_Z(v)+\rho_Z(v);         \tag{3.3}
   \]

5. the subgraph induced by vertices with `epsilon_Z(v)=0` is a Gallai
   forest: every block is complete or an odd cycle.

If `G` has no actual order-seven separation, then

\[
                       \varepsilon_Z(v)+\rho_Z(v)\ge2              \tag{3.4}
\]

for every vertex of both shores.

#### Proof

Items 1 and 3 are the defining vertex-minimality and the standard greedy
extension inequality.  For item 2, colour `G[Z]-v` from its lists and add
the fixed boundary colouring `phi`.  If some colour were absent from the
displayed neighbourhood of `v`, assigning it to `v` would extend `phi`
through the intact shore, contrary to the choice of `K_Z=Z`.

There are no edges from `Z` to the opposite shore.  Since `K_Z=Z`, direct
counting gives

\[
\begin{aligned}
 d_G(v)
   &=d_{G[Z]}(v)+|N_G(v)\cap B|\\
   &=6-|\phi(N_G(v)\cap B)|+\varepsilon_Z(v)
       +|N_G(v)\cap B|,
\end{aligned}
\]

which is (3.3).  The degree-choosability theorem, applied blockwise after
colouring the complement of a block of tight vertices, proves item 5.

Seven-connectivity gives `d_G(v)>=7`.  If equality held, the full
neighbourhood of the singleton component `{v}` would be an actual
order-seven separation: the opposite shore is nonempty and anticomplete to
`v`.  In the absence of such a separation, `d_G(v)>=8`; equation (3.3)
then gives (3.4). \(\square\)

## 4. Exact gain and remaining gap

Theorem 2.1 is well-founded on the order of the operated connected shore.
It applies to either of the simultaneous kernels and retains a literal
full-neighbourhood rejection certificate.  It does not retain the exact
boundary colouring `phi`, the independent exact block used to obtain it,
or any inherited minor-model labels; the new boundary `X` can have
arbitrarily large order.

The sole nontransferring endpoint consists of two anticomplete connected
shores which are simultaneously vertex-minimal list-uncolourable for one
fixed boundary colouring and satisfy (3.4).  Turning their repeated
boundary-colour incidences into distinct literal boundary contacts, or
bounding the full neighbourhood returned by a proper kernel, remains the
host-level obstruction.  Palette data alone do not identify those literal
contacts.

## 5. Dependencies

- [exact-block two-shore Kempe transitions](../results/hc7_two_full_shore_exact_block_kempe_transition.md)
- the degree-choosability theorem
- seven-connectivity and proper-minor six-colourability
