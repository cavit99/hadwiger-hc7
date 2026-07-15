# A failed four-web and a spanning `K_6` can be exactly two-apex

**Status:** explicit, deterministically checked guardrail.  It is not an atomic
twin-seam instance and not a counterexample to the active terminal
disjunction.  It proves that seven-connectivity, `K_7`-minor-freeness, a
genuine failed RST pairing, and a common spanning `K_6` do not by
themselves force a rooted `C_4`, a `K_7`, or a ranked descent.  The
fixed-pair alternative is indispensable.

The executable certificate is
[`hc7_twin_seam_failed_web_two_apex_barrier_verify.py`](hc7_twin_seam_failed_web_two_apex_barrier_verify.py).

## 1. The graph

Let `I_ico` be the icosahedral graph with vertices

\[
 T,B,U_0,\ldots,U_4,L_0,\ldots,L_4
\]

and, with subscripts modulo five, edges

\[
 TU_i,\quad BL_i,\quad U_iU_{i+1},\quad L_iL_{i+1},
 \quad U_iL_i,\quad U_iL_{i-1}.                        \tag{1.1}
\]

Add adjacent vertices `a,b`, each universal to `I_ico`, and put

\[
                            G=K_2\vee I_{ico}.           \tag{1.2}
\]

The graph is exactly seven-connected.  Deleting at most six vertices
leaves an apex, or deletes both apices and at most four vertices from the
five-connected icosahedron.  Conversely, deleting `a,b` and the five
neighbours of one icosahedral vertex isolates that vertex.

The graph has no `K_7` minor.  At most two branch sets of a clique model
can contain `a,b`; deleting those branch sets from a hypothetical `K_7`
model would leave five branch sets forming a `K_5` minor in the planar
graph `I_ico`.  The pair

\[
                              \{a,b\}                    \tag{1.3}
\]

is therefore the coherent fixed-pair terminal: deleting it leaves the
planar, hence `K_5`-minor-free, icosahedron.

## 2. A genuine failed RST pairing

Let

\[
                         W=I_{ico}-T
\]

and choose four singleton roots

\[
                  p=U_0,\qquad q=U_1,\qquad
                  c_1=U_3,\qquad c_2=U_4.              \tag{2.1}
\]

The five-cycle `U_0U_1U_2U_3U_4U_0` bounds the face created by deleting
`T`.  Its four roots occur in the order

\[
                            p,q,c_1,c_2.                 \tag{2.2}
\]

Thus disjoint connected fragments for

\[
                         \{p,c_1\},\{q,c_2\}            \tag{2.3}
\]

would contain two disjoint paths joining alternating vertices of one
face, contrary to the Jordan curve theorem.  The other RST pairing is
feasible: use the path `U_1U_2U_3` and the edge `U_0U_4`.  Hence `W` is a
literal cell-free four-web obstruction for exactly one of the two RST
tests.

## 3. A spanning `K_6` in the common two-edge-deletion host

Take the disjoint named edges

\[
                             e=aT,\qquad f=bB
\]

and put `H=G-{e,f}`, where the braces mean edge deletion.  The following
six bags partition `V(H)`:

\[
\begin{array}{lll}
 F_1=\{T,U_3,U_4\}, & F_2=\{L_0,L_4\},
   & F_3=\{U_0,U_1,U_2\},\\
 F_4=\{L_1,L_2\}, & F_5=\{a,B,L_3\},
   & F_6=\{b\}.
\end{array}                                             \tag{3.1}
\]

Every bag is connected in `H`, and every two bags are adjacent there.
Neither deleted edge is needed: `F_1-F_5` has the literal edges
`U_3L_3,U_4L_3`, while `F_5-F_6` retains `ab` and `bL_3`.  Thus (3.1) is
a literal spanning `K_6` model in the exact common edge-deletion host.

## 4. Scope

This graph simultaneously has

* exact seven-connectivity;
* no `K_7` minor;
* a genuine cell-free failed four-web pairing; and
* a spanning `K_6` in a two-edge-deletion host.

It nevertheless has no rooted-`C_4` conclusion for the selected roots and
no `K_7`; it exits through the fixed pair (1.3).  Therefore the failed-web
branch cannot be closed by localizing an arbitrary spanning `K_6` alone.
A valid atomic proof must use strong contraction-critical state data to
exclude or identify this coherent two-apex outcome.

The example is six-colourable and does not have the frozen twin-seam
boundary maps, packet states, or named Kempe responses.  It does not
falsify a theorem which uses those hypotheses.
