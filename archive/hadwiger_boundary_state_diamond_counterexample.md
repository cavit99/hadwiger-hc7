# A graph-realizable boundary-state diamond

## 1. Purpose

Crossed-state disjointness and minor-critical novelty do not, as abstract
finite-state axioms, force a common repair state.  This note gives a
uniform graph realization with

* a rainbow core \(R\);
* one portal shadow \(p\);
* two incompatible original shore states;
* a new opposite state after every nontrivial faithful minor operation
  on either shore; and
* a joint third state after operations on both shores.

Thus synchronizing the Hall-circuit portal partition requires additional
geometry, such as join-primality, high connectivity, or label-distributed
portals.  It cannot follow from the transition relation alone.

## 2. The equality gadget

Fix \(q\ge3\).  For two nonadjacent labeled vertices \(p,a\), let

\[
                         E_q(p,a)=K_{q+1}-pa.                 \tag{2.1}
\]

Write \(Z_a\) for its other \(q-1\) vertices.  Thus \(Z_a\) is a clique
and every vertex of \(Z_a\) is adjacent to both \(p,a\).

### Lemma 2.1 (equality and operated inequality)

1. Every proper \(q\)-colouring of \(E_q(p,a)\) gives
   \[
                              c(p)=c(a).                      \tag{2.2}
   \]
2. Let \(M\) be any nonidentity boundary-faithful minor operation on
   \(E_q(p,a)\) which retains \(p,a\) as distinct labels.  Then the
   resulting minor has a proper \(q\)-colouring in which
   \[
                              c(p)\ne c(a).                   \tag{2.3}
   \]

#### Proof

The clique \(Z_a\) uses \(q-1\) colours.  Both \(p,a\) see all those
colours, so each must use the one remaining colour, proving (2.2).

For (2.3), perform the same minor operation on
\[
                         E_q(p,a)+pa=K_{q+1},
\]
retaining the edge between the two labeled images.  Because the
operation is nonidentity and does not merge \(p,a\), the result is a
proper minor of \(K_{q+1}\), hence is \(q\)-colourable.  The retained
edge makes the two labels different.  Deleting that edge leaves a
colouring of the operated equality gadget satisfying (2.3).
\(\square\)

This covers arbitrary sequences of deletions and contractions in the
open shore, as well as contractions anchored at exactly one boundary
label.  It does not cover an operation identifying \(p\) with \(a\),
which is correctly excluded by boundary faithfulness.

## 3. The three-state construction

Fix integers

\[
                         2\le h<r,\qquad
                         q=r-h+2\ge3.                         \tag{3.1}
\]

Let \(C\) be a clique of order \(h-2\) (empty when \(h=2\)).  Take two
disjoint equality gadgets

\[
                         E_q(p,a),\qquad E_q(p,b),             \tag{3.2}
\]

identifying their vertex named \(p\), add the edge \(ab\), and then join
every vertex of \(C\) to every vertex of both gadgets.  Call the result
\(G_{r,h}\).

It has a separation with full adhesion

\[
                         W=R\mathbin{\dot\cup}P,\qquad
 R=C\cup\{a,b\},\quad P=\{p\},                               \tag{3.3}
\]

and open shores \(Z_a,Z_b\).  The core \(R\) is a clique of order \(h\)
and hence is rainbow in every \(r\)-colouring of either shore.

Modulo palette permutations, there are three relevant proper equality
states on \(W\):

\[
\begin{array}{c|c}
\sigma_a&p=a,\\
\sigma_b&p=b,\\
\sigma_\ast&p\text{ has a colour absent from }R.
\end{array}                                                  \tag{3.4}
\]

The join with \(C\) prevents \(p\) from sharing a colour with a vertex
of \(C\), so (3.4) lists every possible portal relation.

### Theorem 3.1 (transition diamond)

The two original shores and all their nontrivial faithful minors have
the following exact behavior.

1. The \(a\)-shore accepts only \(\sigma_a\), while the \(b\)-shore
   accepts only \(\sigma_b\).  Hence \(G_{r,h}\) is not
   \(r\)-colourable.
2. After any nonidentity boundary-faithful operation on the \(a\)-shore,
   the modified shore accepts \(\sigma_b\).  It therefore glues to the
   original \(b\)-shore.
3. Symmetrically, every nonidentity operation on the \(b\)-shore
   creates the state \(\sigma_a\).
4. After arbitrary nonidentity faithful operations on both shores, the
   two modified shores have the common state \(\sigma_\ast\).

Thus every one-shore and every two-shore operated graph is
\(r\)-colourable, while the original graph is not.

#### Proof

The clique \(C\) consumes \(h-2\) colours, leaving exactly \(q\) colours
on the two equality gadgets.  Lemma 2.1 makes the original \(a\)-shore
force \(p=a\), and the original \(b\)-shore force \(p=b\).  Since
\(ab\) is an edge, the original states are incompatible.

After a nonidentity operation on the \(a\)-gadget, Lemma 2.1 gives a
colouring with \(p\ne a\) when the operation lies wholly in the
unsuspended gadget.  More generally, add the missing edge \(pa\) before
performing any faithful \(a\)-shore operation.  On the vertex set

\[
                         C\cup\{p,a\}\cup Z_a
\]

the graph with that edge added is \(K_{r+1}\).  The same nonidentity
operation gives a proper minor of \(K_{r+1}\), hence an
\(r\)-colouring in which the retained boundary clique
\(C\cup\{p,a\}\) is rainbow.  Delete the auxiliary edge \(pa\).
Now prescribe \(p=b\); because \(a,b\) are different and both avoid the
colours of \(C\), a palette permutation aligns the operated-shore
colouring, and the untouched \(b\)-gadget already forces \(p=b\).
This proves item 2 for every faithful shore operation, including one
on an edge between \(C\) and the open shore.  Item 3 is symmetric.

If both shores are operated, use three distinct colours on \(p,a,b\),
all outside the colours assigned to \(C\).  This is possible because
\(q\ge3\).  Apply the preceding \(K_{r+1}\)-minor argument separately
on both shores.  Separate palette permutations, agreeing on the fixed
colours of \(C\) and \(p\), assign the prescribed pairs
\((p,a)\) and \((p,b)\).  Both restrictions agree in state
\(\sigma_\ast\), proving item 4.  \(\square\)

The graph before the join with \(C\) is precisely a Hajós join of two
copies of \(K_{q+1}\): delete \(pa\) in one copy and \(pb\) in the
other, identify the two vertices \(p\), and add \(ab\).

## 4. The abstract relation algebra

Let

\[
                         \Omega=\{\sigma_a,\sigma_b,\sigma_\ast\}.
\]

The construction realizes the minimal transition diamond

\[
\begin{array}{c|c|c}
 &\text{original}&\text{after a nontrivial operation}\\ \hline
a\text{-shore}&\{\sigma_a\}&
       \text{contains }\{\sigma_b,\sigma_\ast\},\\
b\text{-shore}&\{\sigma_b\}&
       \text{contains }\{\sigma_a,\sigma_\ast\}.
\end{array}                                                  \tag{4.1}
\]

It satisfies all of the purely relational consequences used in the
current programme:

1. the two base extension relations are disjoint;
2. every one-shore operation creates a state accepted by the opposite
   original shore (minor-critical novelty);
3. opposite one-shore transition states remain different, exactly as
   required by crossed-state disjointness; and
4. any pair of nontrivial opposite operations has a common joint repair
   state.

There is nevertheless no fixed point accepted by both original shores.
The joint repair state \(\sigma_\ast\) appears only after both sides
move.

## 5. Consequence for Hall-circuit portal synchronization

The Hall-circuit simultaneous contraction produces a rainbow core
\[
                         R=\{v\}\cup X
\]
and asks that the two singly operated shores realize one common
partition on the portal shadows \(P\).

The transition diamond shows that the following proposed inference is
invalid:

\[
\begin{array}{c}
\text{every one-shore operation has an opposite-side transition,}\\
\text{every pair of opposite operations has a joint colouring,}\\
\text{and crossed transition states are disjoint}
\\[1mm]\Longrightarrow\\[1mm]
\text{the original shores have a common repair state.}
\end{array}                                                  \tag{5.1}
\]

Even one shadow vertex can rotate through

\[
 \text{left anchor}\longrightarrow
 \text{fresh colour}\longrightarrow
 \text{right anchor}                                        \tag{5.2}
\]

without ever synchronizing the original sides.

The example is deliberately not a candidate Hadwiger counterexample.
It is a low-connectivity Hajós construction; for \(h>2\) it also has
an explicit clique-join factor \(C\).  Therefore it does not refute a
theorem using the least-parameter join-prime core, high connectivity,
or actual portal-label geometry.  It proves that at least one such
geometric hypothesis is indispensable: permutation-invariant boundary
relations, crossed-state disjointness, and exhaustive shore-minor
novelty alone admit the transition diamond.

## 6. Smallest instance

Take \(r=3,h=2\), so \(C=\varnothing\) and each equality gadget is
\(K_4\) minus one edge.  The adhesion is \(\{a,b,p\}\).  The two
original shores force \(p=a\) and \(p=b\); an operation on one shore
permits the opposite equality; and operations on both permit
\(a,b,p\) to be rainbow.

This is the smallest graph realization with the three equality states
needed for the diamond.  With only two colours, the “fresh” state
\(\sigma_\ast\) does not exist, and the analogous construction is the
odd-cycle parity obstruction.
