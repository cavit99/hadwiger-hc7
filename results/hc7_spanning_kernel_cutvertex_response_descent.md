# A cutvertex in a spanning shore gives a smaller full-neighbourhood response

**Status:** written proof; separate internal audit GREEN in
[`hc7_spanning_kernel_cutvertex_response_descent_audit.md`](hc7_spanning_kernel_cutvertex_response_descent_audit.md).

This note treats one reducible part of the order-nine paired list-critical
endpoint.  It uses only the literal two-shore separation and minor-criticality:
if either connected shore has a cutvertex, one of its lobes is a strictly
smaller connected response side.  The returned boundary has order between
seven and ten.  The theorem does not preserve the old exact boundary block or
the fixed list assignment.

## 1. Setting

Let

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,                       \tag{1.1}
\]

where `A,D` are nonempty and connected and `|B|=9`.  Assume

\[
 \chi(G)=7,\qquad \kappa(G)\ge7,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                                  \tag{1.2}
\]

A **full-neighbourhood response** consists of a nonempty connected vertex
set `R`, its literal neighbourhood `X=N_G(R)`, a crossing edge `xy` with
`x in R` and `y in X`, and a proper six-colouring of `G-xy` whose boundary
colouring on `X`

1. extends through `G-R`;
2. extends through `G[R union X]-xy`; and
3. does not extend through the intact graph `G[R union X]`.

The pair

\[
                         \mu(R,X)=(|R|,|X|)                       \tag{1.3}
\]

is ordered lexicographically.  It is a host-level measure: both entries
refer to literal vertex sets of `G` and do not depend on a quotient model or
on colour names.

## 2. Cutvertex descent

### Theorem 2.1

Under (1.1)--(1.2), suppose that `G[A]` has a cutvertex `v`.  Let `R` be
any component of `G[A-v]`, and put

\[
                              X=N_G(R).                            \tag{2.1}
\]

Then:

1. `R` is nonempty and connected, and

   \[
              |R|<|A|,\qquad X\subseteq B\cup\{v\},
              \qquad 7\le |X|\le10;                              \tag{2.2}
   \]

2. for every crossing edge `xy`, every proper six-colouring of `G-xy`
   gives a full-neighbourhood response on `(R,X)`;
3. consequently

   \[
                         \mu(R,X)<_{\rm lex}(|A|,9);               \tag{2.3}
   \]

4. if `|X|=7`, every component of `G-X` is adjacent to every literal
   vertex of `X`.

The symmetric statement holds if `G[D]` has a cutvertex.  Thus every
cutvertex shore returns a strictly smaller **fresh** connected response
side.  Conditional on treating such fresh responses as an allowed transfer,
the residual paired spanning-kernel endpoint has two two-connected shores.

#### Proof

Because `v` is a cutvertex of the connected graph `G[A]`, the graph
`G[A-v]` has at least two components.  Hence `R` is nonempty and connected,
and `|R|<|A|`.  No vertex of `R` has a neighbour in another component of
`G[A-v]`; all its neighbours in `A-R` therefore lie at `v`.  It has no
neighbour in `D` by (1.1).  Consequently

\[
                              X\subseteq B\cup\{v\},              \tag{2.4}
\]

so `|X|<=10`.

The set `X` separates `R` from the nonempty opposite shore `D`.  Therefore
seven-connectivity gives `|X|>=7`, proving (2.2).  There is a crossing edge:
otherwise the nonempty set `R` would be a component of the connected graph
`G`.

Fix such an edge `xy`, with `x in R` and `y in X`.  The graph `G-xy` is a
proper minor of `G`, so it has a proper six-colouring `c`.  Necessarily

\[
                               c(x)=c(y),                           \tag{2.5}
\]

because otherwise restoring `xy` would give a proper six-colouring of `G`.
The restriction `c|G-R` proves extension through the outside, and
`c|G[R union X]` proves extension through the edge-deleted inside.  If the
same labelled colouring `c|X` extended through the intact graph
`G[R union X]`, gluing that extension to `c|G-R` would give a proper
six-colouring of `G`, contrary to `chi(G)=7`.  Hence `c|X` is rejected by
the intact inside.  This proves item 2.

The first coordinate in (1.3) has strictly decreased, so (2.3) follows
even when `|X|=10`.

Finally, suppose `|X|=7` and let `C` be a component of `G-X`.  There are at
least two such components, because `R` and `D` lie on different sides of
`X`.  If `C` missed a vertex `z in X`, then

\[
                             N_G(C)\subseteq X-\{z\}
\]

would be a separator of order at most six, contradicting
seven-connectivity.  Thus every component of `G-X` is adjacent to every
vertex of `X`.  Interchanging `A` and `D` gives the symmetric assertion.
\(\square\)

## 3. Exact gain and trust boundary

The theorem gives a single-step host-level normalization of every
cutvertex shore.  Its literal first coordinate strictly decreases in that
step, independently of colour names or a chosen quotient model.

The response boundary may grow from nine to ten, and its colouring need not
retain the old exact singleton block, the fixed list assignment, the
opposite spanning list-critical kernel, or any minor-model labels.  Thus the
result is a strict full-neighbourhood response transfer, not by itself a
recursive instance of the exact-block theorem.  In particular, (2.3) alone
does **not** prove that repeated transfers form a well-founded induction:
one first needs a re-entry theorem preserving enough of the paired labelled
setting.  The result does not address the endpoint in which both shores are
two-connected, nor does it eliminate a singleton shore (which has no
cutvertex).

## 4. Dependencies

The proof uses only seven-connectivity, six-colourability of proper minors,
and the literal separation (1.1).  It does not use a finite classification or
an external structural theorem.
