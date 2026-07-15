# Barrier: the canonical reverse trace does not force the first seam

**Status:** explicit finite counterexample to the static first-seam
inference.  This graph contains a literal `K_7`, is five-colourable, and is
not contraction-critical.  It is not a counterexample to `HC_7` and does
not refute a lemma that retains `K_7`-minor-freeness or the universal
proper-minor response.

The accompanying verifier is
[`hc7_reverse_canonical_first_seam_barrier_verify.py`](hc7_reverse_canonical_first_seam_barrier_verify.py).

## 1. Construction

Let

\[
 \Omega=\{0,1,2,3,4,5,6\},\qquad
 I=\{0,1,2\},\qquad J=\{3,4,5,6\}.
\]

The boundary graph `H=G[Omega]` contains every `I-J` edge.  Inside `J`,
its only edges are the path

\[
                         6-3-4-5.                       \tag{1.1}
\]

Thus `I` is a maximum independent set of order three and
`omega(H)=3`.

Take

\[
                  D=\{d_1,d_2\},\qquad B=\{b\}.
\]

Add `d_1d_2`, make each of `d_1,d_2,b` complete to `Omega`, and add no
edge from `D` to `B`.  Then

\[
          V(G)=D\mathbin{\dot\cup}\Omega\mathbin{\dot\cup}B
                                                               \tag{1.2}
\]

is an actual order-seven separation.  The graph is exactly
seven-connected.  The two singleton sets `{d_1},{d_2}` are disjoint
`Omega`-full packets, while `{b}` is the unique packet on its shore, so

\[
                         (\nu_D,\nu_B)=(2,1).             \tag{1.3}
\]

In particular, for the canonical packet choice,

\[
                         P_1\cup P_2=D;                  \tag{1.4}
\]

there is no vertex from which a third carrier could be cut.

## 2. Legally attained canonical demand-three trace

Contract the connected star `B union I` to one vertex `t`.  The resulting
proper minor has the proper six-colouring

\[
 B\cup I,\quad \{4\},\quad \{3,5\},\quad \{6\},
 \quad\{d_1\},\quad\{d_2\}.                              \tag{2.1}
\]

On the literal boundary this returns the exact state

\[
                  \Pi=\{I,\{4\},\{3,5\},\{6\}\}.        \tag{2.2}
\]

Its singleton set is `{4,6}`, an independent set in `H`.  Consequently

\[
                  d_H(\Pi)=4-\omega(H[\{4,6\}])=3.       \tag{2.3}
\]

This is precisely the maximum-independent-set contraction used to
generate the canonical reverse demand-three trace; the state has not
been declared abstractly.

## 3. Neither static first-seam output is available

There is no third connected carrier in `D-(P_1 union P_2)`, because that
set is empty.

There is also no reserved-anchor rooted `K_5` on the closed `B`-side, for
any two distinct reserved literals `x,y in Omega`.  Indeed,

\[
              G[B\cup(\Omega-\{x,y\})]                  \tag{3.1}
\]

has five prescribed roots and only one additional vertex, `b`.  A rooted
`K_5` model either omits `b`, requiring a `K_5` on the five roots, or puts
`b` in one rooted bag, requiring the other four roots to induce a `K_4`.
Both are impossible because `omega(H)=3`.  The verifier also exhausts all
21 choices of `{x,y}` and every assignment of `b` to a rooted bag.

Therefore the implication

> canonical demand-three trace + two exhaustive full packets
> `=>` third duty carrier or reserved-anchor rooted `K_5`

is false, even with exact seven-connectivity and a named proper-minor
operation.

## 4. Exact trust boundary

The graph has a literal `K_7` model with bags

\[
 \{2,6\},\quad \{1,4\},\quad \{5\},\quad \{b,3\},
 \quad \{0\},\quad \{d_1\},\quad \{d_2\}.               \tag{4.1}
\]

It is even five-colourable: use one colour on `I`, two colours on the path
`H[J]`, distinct new colours on `d_1,d_2`, and give `b` the colour of
`d_1`.

It also fails Dirac's contraction-critical neighbourhood inequality

\[
                         \alpha(N(v))\le d(v)-5.          \tag{4.2}
\]

At each of `5,6,b`, the degree is seven while the neighbourhood has an
independent set of order three.  Hence a positive first-seam theorem must
use at least one of the hypotheses deliberately absent here:

* literal `K_7`-minor-freeness;
* the contraction-critical neighbourhood restrictions; or
* the response of every proper minor, rather than the one named trace.

The example gives no evidence against a theorem retaining the full
`HC_7` kernel.
