# Excess density for paired spanning list-critical kernels at order eight

**Status:** written proof; [separate internal audit](hc7_order8_paired_all_tight_closure_audit.md)
GREEN.  This is a conditional unbounded theorem in the
minimum-positive-excess response-coupling programme.  It does not prove
`HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
\tag{1.1}
\]

Among all nonempty connected sets `R` satisfying

\[
 G-(R\cup N_G(R))\ne\varnothing,
 \qquad |N_G(R)|\ge8,                                \tag{1.2}
\]

choose one lexicographically minimizing

\[
                         (|N_G(R)|,|R|).              \tag{1.3}
\]

Suppose `S=N_G(R)` has order eight and `G-S` has exactly two components
`A,D`, both adjacent to every literal vertex of `S`.  Assume

\[
                           |A|,|D|\ge2.               \tag{1.4}
\]

Let `phi` be a proper six-colouring of `G[S]`.  For `Z in {A,D}` and
`v in Z`, put

\[
 c(v)=|\{\phi(s):s\in N_G(v)\cap S\}|,
 \qquad L_Z(v)=[6]-\{\phi(s):s\in N_G(v)\cap S\}.    \tag{1.5}
\]

For each shore vertex define its list-degree excess `epsilon(v)` by

\[
 d_{G[Z]}(v)=|L_Z(v)|+\varepsilon(v)
            =6-c(v)+\varepsilon(v),
 \qquad \varepsilon(v)\ge0.                           \tag{1.6}
\]

The usual source of the nonnegativity is a spanning vertex-minimal
list-uncolourable kernel on each shore: after colouring the graph with one
vertex removed, a vertex of internal degree below its residual-list order
could be added back.  The proof below needs only (1.6).

## 2. The paired excess inequality

### Theorem 2.1

Under the hypotheses of Section 1, at least one of the following holds.

1. Some vertex of `G` has degree seven.  Its full neighbourhood is the
   boundary of a nontrivial singleton-side order-seven separation, and
   deleting any incident edge gives a generic exact-seven selected
   response.
2. Writing

   \[
    s=|A|+|D|,\quad
    C=\sum_{v\in A\cup D}c(v),\quad
    E=\sum_{v\in A\cup D}\varepsilon(v),\quad
    h=|E(G[S])|,                                      \tag{2.1}
   \]

   one has

   \[
       s\ge24,
       \qquad E\ge 2s+C+2h-48\ge C+2h.               \tag{2.2}
   \]

Consequently the all-tight case `E=0` always gives outcome 1.

#### Proof

If `G` has a degree-seven vertex `x`, then `G-N_G[x]` is nonempty because
the graph has at least twelve vertices.  Thus `N_G(x)` is the boundary of
an actual separation with singleton open side `{x}`.  For any incident
edge `xy`, every proper six-colouring of `G-xy` makes `x,y` one colour,
since otherwise the edge could be restored.  Its restrictions colour the
edge-deleted singleton side and the opposite closed side.  If the induced
boundary equality partition extended through the intact singleton side,
the two closed-shore colourings would align and glue to a six-colouring of
`G`.  Hence the intact singleton side rejects that partition.  This is
outcome 1.

Suppose that `G` has no vertex of degree seven.  No vertex has degree eight
either.  Indeed, if `d_G(x)=8`, then `{x}` is an eligible connected set in
(1.2): the graph has at least twelve vertices by (1.4), so
`G-N_G[x]` is nonempty.  The pair `(8,1)` would be lexicographically
smaller than the selected `(8,|R|)`, because `R` is one of the two
components `A,D` and has order at least two.  This contradicts (1.3).

Seven-connectivity and the exclusion of degrees seven and eight give

\[
                              \delta(G)\ge9.           \tag{2.3}
\]

Let `e_cross` be the number of edges from `A union D` to `S` and let
`e_int=|E(G[A])|+|E(G[D])|`.  Since there are no edges between the two
open components, (1.6) and (2.1) give

\[
 2e_{\rm int}=6s-C+E,
 \qquad e_{\rm int}=3s-\frac C2+\frac E2.            \tag{2.4}
\]

For a shore vertex `v`, all neighbours outside its own component lie in
`S`.  Summing its boundary degree over both shores and using (1.6) and
(2.3) gives

\[
 e_{\rm cross}
   =\sum_{v\in A\cup D}(d_G(v)-d_{G[Z]}(v))
   \ge9s-(6s-C+E)=3s+C-E.                            \tag{2.5}
\]

The strict form of Mader's bound for the present host is

\[
                         |E(G)|\le5|V(G)|-16.         \tag{2.6}
\]

Since `|V(G)|=s+8`, equations (2.3)--(2.6) give

\[
 6s+\frac C2-\frac E2+h
   \le e_{\rm int}+e_{\rm cross}+h
   =|E(G)|
   \le5s+24,
\]

and hence

\[
                              E\ge2s+C+2h-48.         \tag{2.7}
\]

On the other hand, (2.3), the handshake lemma and (2.6) give

\[
 \frac{9(s+8)}2\le |E(G)|\le5(s+8)-16=5s+24,
\]

so `s>=24`.  Together with (2.7), this proves both inequalities in (2.2).

If `E=0`, let `b` be the number of colours used by `phi` on the nonempty
set `S`.  For every used colour, fullness supplies a neighbour of a
boundary vertex of that colour in each shore.  Hence the colour is counted
by `c(v)` at least once in each shore and

\[
                              C\ge2b\ge2.              \tag{2.8}
\]

But (2.2) would give `0=E>=C+2h>=2`, a contradiction.  Therefore the
all-tight case cannot enter outcome 2 and must have outcome 1. \(\square\)

## 3. Exact contribution and trust boundary

Theorem 2.1 gives a scalar obstruction for the whole paired spanning
list-critical branch.  Any nonterminal survivor has at least twenty-four
shore vertices and total list-degree excess at least
`2s+C+2h-48`.  Its all-tight specialization eliminates cliques, odd cycles
and multiblock Gallai trees uniformly, provided both kernels span their
nontrivial open components.  The all-tight output is a singleton-side
generic exact-seven response, strictly smaller than the selected component
`R`.

The theorem does not prove that every order-eight interface has one common
boundary colouring which produces spanning list-critical kernels on both
shores.  It does not treat a singleton open component, and the lower bound
on positive excess does not itself turn that excess into a labelled minor
model or compatible boundary colouring.  Those are the remaining
response-coupling branches.
An exact-seven response is a recursive output, not by itself a common
closed-shore colouring or a proof of `HC_7`.

## 4. Dependencies

- [minimum positive-excess separator normal form](hc7_minimum_positive_separator_normal_form.md);
- [the strict Mader bound for the present host](hc7_large_boundary_singleton_response_descent.md),
  Lemma 1.1; and
- elementary degree sums.
