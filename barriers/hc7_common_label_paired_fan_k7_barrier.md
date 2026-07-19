# A paired five-label fan does not by itself repair a near-complete minor model

**Status:** explicit barrier to the intermediate assertion that the paired
five-label fan in the order-eight setting forces a `K_7` minor.  A
deterministic verifier is provided in
[`hc7_common_label_paired_fan_k7_barrier_verify.py`](hc7_common_label_paired_fan_k7_barrier_verify.py).
This note does not refute an alternative which returns a compatible
order-seven boundary partition, and it is not a counterexample to `HC_7`.

## 1. Exact assertion refuted

The following data do not force a `K_7` minor:

1. a seven-connected, `K_7`-minor-free graph with an eight-vertex
   separation whose two open components are adjacent to every boundary
   vertex;
2. a spanning labelled `K_7`-minus-one-edge model whose boundary labels
   have the form

   \[
   \{k_1,k_2\}\mathbin{\dot\cup}
   \{s_X,s_Y,s_D,s_{F_1},s_{F_2},s_{F_3}\},
   \]

   where `k_1,k_2` have label `U` and the other vertices have their
   displayed labels;
3. a path in one open component with five paths to

   \[
                     \{k_1,s_D,s_{F_1},s_{F_2},s_{F_3}\},
   \]

   pairwise disjoint outside the source path and meeting the boundary only
   at their five distinct terminal vertices;
4. two of those paths are vertex-disjoint boundary edges with distinct
   common-model labels; and
5. the two edges admit all three contraction responses

   \[
   ({\rm equal},{\rm equal}),\qquad
   ({\rm equal},{\rm proper}),\qquad
   ({\rm proper},{\rm equal}).                         \tag{1.1}
   \]

The missing operation-specific hypothesis is the prohibition of
`(proper,proper)`.  In a minor-minimal seven-chromatic graph that
prohibition follows because such a colouring would colour the original
graph.  The example below realizes (1.1) and also realizes
`(proper,proper)`.  Equivalently, it fails the universal assertion that
every six-colouring after deleting either one of the two edges makes that
edge's endpoints equal: a colouring with both pairs proper restricts to a
counterexample to either such assertion.

## 2. Host graph and exact boundary

Use the icosahedral graph `I` on

\[
 t,d,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

with the standard edges

\[
 tu_i,\quad dw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1},
\]

where subscripts are modulo five.  Add adjacent vertices `p,q`, each
complete to `I`, and put

\[
                              G=K_2\vee I.             \tag{2.1}
\]

The audited selected-fan barrier proves that `G` is seven-connected and
has no `K_7` minor: deleting `p,q` from a hypothetical `K_7` model would
leave a `K_5` minor in the planar graph `I`.

Set

\[
\begin{aligned}
 S&=\{p,q,t,d,u_0,w_0,u_2,w_2\},\\
 C&=\{u_3,u_4,w_3,w_4\},\\
 C'&=\{u_1,w_1\}.
\end{aligned}                                           \tag{2.2}
\]

The sets `C,C'` are the two components of `G-S`, and each is adjacent to
every literal vertex of `S`.

## 3. The labelled spanning model

The seven connected branch sets are

\[
\begin{array}{c|l}
U& t,u_2,u_3,u_4,w_3,w_4\\
X& d\\
Y& u_0,u_1\\
D& p\\
F_1&q\\
F_2&w_0\\
F_3&w_1,w_2.
\end{array}                                             \tag{3.1}
\]

They partition `V(G)`.  Every two are adjacent except `X,Y`; those two are
anticomplete.  Thus they form a spanning labelled
`K_7`-minus-one-edge model.  On the boundary take

\[
\begin{aligned}
 &k_1=t,\qquad k_2=u_2,\\
 &s_X=d,\quad s_Y=u_0,\quad s_D=p,\quad
 s_{F_1}=q,\quad s_{F_2}=w_0,\quad s_{F_3}=w_2.
\end{aligned}                                           \tag{3.2}
\]

This is exactly the two-plus-six label distribution used by the paired-fan
alternative.  In addition, the whole selected component `C` lies in the
old branch set labelled `U`.  Its retained part is the connected edge
`tu_2`, which is adjacent to `C`, as in the concentrated donor setting;
the example is not exploiting mixed ownership or a disconnected retained
part.

## 4. The five-label fan and the paired responses

Choose

\[
 e=u_3w_2,\qquad f=w_4w_0,
 \qquad P=u_3u_4w_4.                                   \tag{4.1}
\]

The five paths from `P` to one representative of each common model label
are

\[
 u_4t,\qquad u_4p,\qquad u_4q,
 \qquad w_4w_0,\qquad u_3w_2.                          \tag{4.2}
\]

They have terminals `t,p,q,w_0,w_2`, meet `S` only at those terminals,
and are pairwise disjoint outside `P`.  The fourth and fifth paths are the
vertex-disjoint edges `f,e` and have the distinct labels `F_2,F_3`.

Four explicit six-colourings are recorded by the verifier.  Restricted to
the icosahedral factor, their colour vectors are:

\[
\begin{array}{c|rrrrrrrrrrrr}
 &t&d&u_0&u_1&u_2&u_3&u_4&w_0&w_1&w_2&w_3&w_4\\ \hline
EE&0&1&1&2&1&3&2&3&0&3&0&3\\
EP&0&0&1&2&3&2&3&3&1&2&1&2\\
PE&0&1&1&2&1&3&2&3&0&2&0&3\\
PP&0&1&1&2&1&2&3&3&0&3&0&2.
\end{array}                                             \tag{4.3}
\]

Give `p,q` colours `4,5`.  The first row is proper after deleting `e,f`
and makes both endpoint pairs equal.  The next two rows are proper after
deleting respectively `e` and `f`, with the other pair proper.  The last
row is a proper colouring of all of `G`.

Hence the example satisfies the full local geometry and all three positive
operation responses while remaining `K_7`-minor-free.  What it lacks is
exactly the critical response exclusion

\[
                         ({\rm proper},{\rm proper})
                         \text{ is impossible}.       \tag{4.4}
\]

## 5. Why the compatible-separator alternative survives

This example does not refute the proposed disjunction

\[
 \text{explicit `K_7` model}\quad\text{or}\quad
 \text{compatible order-seven boundary partition}.
\]

Indeed,

\[
                  Q=\{d,p,q,u_1,u_2,w_0,w_2\}         \tag{5.1}
\]

is an order-seven separator.  The components of `G-Q` are

\[
 \{w_1\},\qquad \{t,u_0,u_3,u_4,w_3,w_4\}.            \tag{5.2}
\]

Both `e,f` cross from the second component to `Q`.  For each of the first
three rows of (4.3), its equality partition on `Q` is induced by a proper
six-colouring of the whole graph, and therefore by proper colourings of
both closed shores.  The verifier checks explicit extensions.

Thus the barrier lands exactly in the compatible-separator outcome.  It
shows that the five paths and the three positive responses cannot be used
as a branch-set-repair theorem.  Any proof which excludes the separator
outcome must use (4.4), or an equivalent universal nonextendability
condition, at the literal branch-set contacts.

## 6. Trust boundary

The graph is six-colourable and coherently two-apex; it is not a
hypothetical `HC_7` counterexample.  It does not refute a theorem retaining
seven-chromaticity, contraction-criticality and the compatible-separator
alternative.  It also does not realize the full upstream three-owner
concentration hypothesis: relative to the connected retained donor
`\{t,u_2\}`, only two displayed outside branch sets have all their donor
contacts inside `C`.  Thus “minimal missing” here refers only to the
operation-signature coordinate; the example does not prove that forbidding
`PP` is sufficient under a weaker model-local hypothesis.

Its exact contribution is to isolate the final missing operation-specific
input after the paired-fan alternative: not another unlabelled fan, but the
prohibition of the fourth response signature and its conversion, together
with any retained upstream concentration data, into either labelled
branch-set absorption or a common boundary partition.
