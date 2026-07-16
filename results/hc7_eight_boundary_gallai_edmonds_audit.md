# Independent audit: canonical Gallai--Edmonds barrier

**Verdict:** GREEN for the theorem and all deductions stated in
`hc7_eight_boundary_gallai_edmonds.md`.

**Audited revision:** SHA-256
`da9dd8ba410000a1296753aa527aabe7088d21c3033231267487dedafa303bb8`.

The preceding audited revision had SHA-256
`d5409104852f78cfb33c99014075c69691c13495cf62ceace46d5f704927c420`.
The later revision changes only the status declaration and trust-boundary
metadata to record this audit.  Its theorem statement, proof, example, and
mathematical limitations are unchanged.  Those metadata changes were
checked before rebinding the audit to the new hash.

This audit independently replays the Gallai--Edmonds deduction, the
displayed `K_7`-minor model, the parity enumeration, and the
`K_{3,5}` example.  It does not assert any colouring-state transfer across
the two shores of an eight-vertex separation.

## 1. Gallai--Edmonds input

Use the standard notation from the theorem file.  If `q` is the number of
components of `F[D]`, the Gallai--Edmonds structure theorem gives:

1. every component of `F[D]` is factor-critical and hence has odd order;
2. `F[C]` has a perfect matching, so each of its components has even
   order;
3. there is no edge from `D` to `C`;
4. every maximum matching matches all vertices of `A` into pairwise
   distinct components of `F[D]`; and
5. the number of vertices left unmatched by a maximum matching is

   \[
                         q-|A|.                       \tag{1.1}
   \]

These are exactly the external facts used in the theorem file.  In
particular, (1.1) is the matching deficiency appearing there.

## 2. The bound on deficient components

Suppose `q>=5`, and choose vertices `x_1,...,x_5` from five distinct
components of `F[D]`.  Distinct components of the induced graph `F[D]`
have no edge between them.  Therefore the five chosen vertices are
pairwise adjacent in `J=\overline F`.

There are three unused boundary vertices, so choose one of them as `w`.
Let `u,v` be the two nonadjacent vertices in `I_2`.  The seven sets

\[
              \{x_1\},\ldots,\{x_5\},\{u,w\},\{v\}
\]

are disjoint and connected.  The first five are pairwise adjacent;
`u` and `v` are each complete to `J`; and `w v` supplies the adjacency
between `\{u,w\}` and `\{v\}`.  Thus these sets are an explicit
`K_7`-minor model in `I_2\vee J`, contradicting the hypothesis.  Hence
`q<=4`.  The construction in the theorem file is therefore correct and
does not silently require `u v` to be an edge.

## 3. Deficiency, parity, and the canonical barrier

Since `F` has eight vertices, the number of vertices missed by a maximum
matching is even.  Since `F` has no perfect matching, this number is
positive and hence at least two.  By (1.1),

\[
                         q-|A|\ge2.                   \tag{3.1}
\]

Together with `q<=4`, this proves `|A|<=2`.

After deleting `A`, the absence of `D`--`C` edges means that the
components of `F[D]` remain components of `F-A`.  They are odd.  Every
component of `F[C]` is even, because `F[C]` has a perfect matching.
Consequently the odd components of `F-A` are exactly the `q` components
of `F[D]`, and

\[
                    o(F-A)=q>|A|.                    \tag{3.2}
\]

Thus `A` attains the deficiency in Tutte--Berge and is indeed a canonical
Tutte barrier.  Enumerating `0<=|A|<=2`, `q<=4`, and positive even
`q-|A|` gives exactly

\[
 (|A|,q)\in\{(0,2),(0,4),(1,3),(2,4)\}.
\]

No fifth pair is possible.

## 4. The `K_{3,5}` calibration

For `J=K_{3,5}`, its complement is `F=K_3\mathbin{\dot\cup}K_5`.
A maximum matching leaves one vertex uncovered in each odd clique, and
any chosen vertex of either clique can be the uncovered vertex of a
maximum matching.  Hence `D=V(F)` and `A=C=\varnothing`.

The join `I_2\vee J` is the complete tripartite graph `K_{2,3,5}`.  A
complete multipartite graph on `n` vertices with largest part of order
`m` has treewidth `n-m`; here the treewidth is `10-5=5`.  Since treewidth
is minor-monotone and `K_7` has treewidth six, `K_{2,3,5}` has no
`K_7` minor.  The example therefore correctly shows that the canonical
set `A` may be empty under all hypotheses of Theorem 1.1.

## 5. Scope and limitations

The proof is entirely state-free.  It strengthens the previously proved
existence of a Tutte witness of order at most two by selecting the
canonical Gallai--Edmonds witness and recording factor-critical deficient
components.  It does **not** prove that:

- `A` has order exactly two;
- vertices of `A` meet all `K_5` models;
- either shore extends a boundary colouring determined by `(D,A,C)`;
- the two shores have a common boundary colouring; or
- the two-edge contraction residue, the support-six transversal theorem,
  or `HC_7` is closed.

Those limitations are stated accurately in the theorem file.  No
computer-assisted assertion is used in this proof or audit.
