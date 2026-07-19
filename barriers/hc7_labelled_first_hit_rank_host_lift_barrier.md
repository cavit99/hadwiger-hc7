# A first-hit rank defect need not lift to a small host separator

**Status:** explicit barrier to an intermediate linkage-to-separator claim.
The graph below is seven-connected, but it contains a `K_7` subgraph and is
not a hypothetical counterexample to `HC_7`.

## 1. The overstrong claim

The construction refutes the following inference:

> In a seven-connected graph, failure of a five-label clean first-hit
> linkage produces a host separator of order at most seven merely because
> Rado's theorem and Menger's theorem produce a relative separator of order
> at most four.

The missing datum is a bound on neighbours in the terminal classes not
selected by the deficient Rado set.

## 2. Construction

Take pairwise disjoint vertex sets

\[
 P=\{p_1,\ldots,p_8\},\qquad
 U=\{u_1,\ldots,u_7\},
\]

and three further vertices `a,b,z`.  Define `H` by the following edges:

1. `P union U` induces a clique;
2. `U union {a,b}` induces a clique;
3. `z` is adjacent to every vertex of `P union {a,b}`; and
4. there are no further edges.  In particular, `z` is anticomplete to `U`
   and `P` is anticomplete to `{a,b}`.

Set

\[
 T_1=\{a\},\qquad T_2=\{b\},
\]

and partition `U` into three nonempty sets `T_3,T_4,T_5`.  The source set
is `P` and the full terminal union is `T=U union {a,b}`.

## 3. Verification

### Lemma 3.1

The graph `H` is seven-connected.

#### Proof

After deleting at most six vertices, at least one vertex of `P` and at
least one vertex of `U` remain.  The surviving vertices of `P union U`
lie in one clique.  Each surviving one of `a,b` is adjacent to every
surviving vertex of `U`, and `z`, if present, is adjacent to every surviving
vertex of `P`.  Hence the remaining graph is connected.  \(\square\)

### Lemma 3.2

For `I={1,2}`, the clean first-hit linkage rank is one and the singleton
`{z}` is a minimum separator in the directed terminal-avoiding network.

#### Proof

After the whole terminal union `T` is forbidden internally, the
nonterminal graph is induced by `P union {z}`.  Each of the sink copies
`hat(a),hat(b)` has the single in-neighbour `z`: their other host neighbours
belong to `T` and are deleted from the network.  Therefore every clean path
from `P` to either selected terminal uses `z`.  One such path exists, so
the rank is one and `{z}` is a minimum Menger set.  \(\square\)

### Lemma 3.3

The relative separator `{z}` is not a host separator.  The source-side
component `P` has

\[
                           N_H(P)=U\cup\{z\},
\]

of order eight.

#### Proof

In `H-z`, every vertex of `P` is joined through `U` to both `a` and `b`.
Thus deleting `z` does not separate the host.  In the terminal-avoiding
network the seven vertices of `U=T_3 union T_4 union T_5` were unavailable
as internal vertices; in the host they are precisely the unselected-label
exposure which enlarges the boundary from one to eight.  \(\square\)

## 4. Exact scope

The graph contains the clique `P union U`, so it contains a `K_7` and does
not satisfy the global minor exclusion or contraction-criticality of a
hypothetical `HC_7` counterexample.  It therefore does not refute a theorem
which uses those hypotheses to control unused-label attachments.

It does prove that seven-connectivity, five labelled terminal sets, and the
Rado--Menger rank defect alone cannot supply a literal order-seven host
separator.  A positive `HC_7` theorem must additionally bound the literal
exposure to unused terminal classes, preserve one portal per unused label,
or use the proper-minor colouring responses to obtain a compatible
boundary equality partition directly.
