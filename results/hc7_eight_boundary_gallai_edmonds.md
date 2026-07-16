# A canonical Gallai–Edmonds barrier on an eight-vertex boundary

**Status:** proved and independently internally audited in
[`hc7_eight_boundary_gallai_edmonds_audit.md`](hc7_eight_boundary_gallai_edmonds_audit.md).
This theorem canonicalizes a previously proved Tutte-witness bound.  It
does not align colouring extensions across a separation and does not prove
`HC_7`.

## 1. Statement

For graphs on disjoint vertex sets, `G \vee H` denotes their join.  Thus
`I_2 \vee J` is obtained from an eight-vertex graph `J` by adding two
nonadjacent vertices, each adjacent to every vertex of `J`.

### Theorem 1.1 (canonical boundary barrier)

Let `J` be a graph on eight vertices, put `F=\overline J`, and suppose

\[
             I_2\vee J \not\succcurlyeq K_7
\]

and `F` has no perfect matching.  Let

\[
             V(F)=D\mathbin{\dot\cup}A\mathbin{\dot\cup}C
\]

be the Gallai–Edmonds decomposition of `F`, and let `q` be the number of
components of `F[D]`.  Then:

1. `q\le 4`;
2. `q-|A|` is a positive even integer, and hence `|A|\le2`;
3. the odd components of `F-A` are exactly the `q` components of `F[D]`,
   so `o(F-A)=q>|A|`; and
4. consequently

   \[
      (|A|,o(F-A))\in
      \{(0,2),(0,4),(1,3),(2,4)\}.
   \]

Moreover, every component of `F[D]` is factor-critical, `F[C]` has a
perfect matching, and every maximum matching of `F` matches every vertex
of `A` to a vertex in a different component of `F[D]`.

Thus `A` is a canonical Tutte barrier of order at most two.  The word
"barrier" does not mean that `A` is always a two-vertex set: it may be
empty.

## 2. Proof

Use the standard Gallai–Edmonds definitions: `D` is the set of vertices
missed by at least one maximum matching, `A=N_F(D)-D`, and
`C=V(F)-(A\cup D)`.  The Gallai–Edmonds structure theorem gives the final
three assertions in Theorem 1.1 and the deficiency formula

\[
                 \operatorname{def}(F)=q-|A|.       \tag{2.1}
\]

We first prove `q\le4`.  If `F[D]` had five distinct components, choose
one vertex from each of them.  There is no edge of `F` between two
different components of `F[D]`; the five chosen vertices therefore induce
a `K_5` in `J`.  Choose a sixth boundary vertex `w` outside this `K_5`,
and denote the two vertices of `I_2` by `u` and `v`.  In `I_2\vee J`, the
seven connected branch sets

\[
       \{u,w\},\quad \{v\},\quad
       \{x\}\quad(x\text{ one of the five clique vertices})
\]

are pairwise adjacent.  They form a `K_7`-minor model, contrary to the
hypothesis.  Hence `q\le4`.

The graph `F` has eight vertices and has no perfect matching.  Therefore
its matching deficiency is a positive even integer, so by (2.1)

\[
                   q-|A|\ge2.                       \tag{2.2}
\]

It follows that `|A|\le q-2\le2`.

Every component of `F[D]` is factor-critical and hence has odd order.
There are no edges from `D` to `C`, while `F[C]` has a perfect matching;
in particular, every component of `F[C]` has even order.  It follows that
the odd components of `F-A` are precisely the `q` components of `F[D]`.
Thus

\[
                   o(F-A)=q>|A|,
\]

where the strict inequality follows from (2.2).  Finally, `0\le|A|\le2`,
`q\le4`, and `q-|A|` is positive and even.  The four displayed pairs in
part 4 are the only possibilities.  \(\square\)

## 3. Exact contribution and limitation

In the support-six programme, an eight-vertex boundary arises after two
specified model edges remain split.  The absence of a balanced
four-pair boundary partition is equivalent to the failure of a perfect
matching in the complement.  Theorem 1.1 replaces an arbitrary
Tutte-witness set of order at most two by the canonical set `A` and also
records at most four factor-critical deficient components.

This is useful only as a canonical descriptor.  Gallai–Edmonds theory
does not determine which proper boundary colourings extend through either
shore of a separation.  In particular, the theorem yields neither a
common boundary colouring, nor a distinguished terminal pair, nor a
`K_7`-minor model.  Any further state-transfer theorem must combine the
full decomposition `(D,A,C)` with the named split model edges and the
proper-minor colouring transitions.

The set `A` can be empty.  For example, take `J=K_{3,5}`.  Then
`F=K_3\mathbin{\dot\cup}K_5`, so `D=V(F)` and `A=C=\varnothing`; also
`I_2\vee J=K_{2,3,5}` has treewidth five and hence has no `K_7` minor.

## 4. Trust boundary

The only external input is the classical Gallai–Edmonds structure theorem
and its deficiency formula.  The deduction above is internal to this
repository.  The adjacent audit is an independent internal check, not
external peer review.
