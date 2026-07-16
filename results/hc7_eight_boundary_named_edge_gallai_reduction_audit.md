# Independent audit: named-edge Gallai--Edmonds normal forms

**Verdict:** **GREEN.**  Every structural conclusion in
[`hc7_eight_boundary_named_edge_gallai_reduction.md`](hc7_eight_boundary_named_edge_gallai_reduction.md)
follows from the stated hypotheses.  No correction is required.

**Audited revision:** SHA-256
`21338b88ba85d363592a71b5f5ed60f7acf8ef0bd668e336a60269db2c7fc65c`.

The preceding audited revision had SHA-256
`65d4c48dc8025faffadb652449be73bf20faca8bc8825f39406b39201e0a4c0c`.
The current revision changes only the status declaration to record and link
this adjacent GREEN audit.  Its theorem statement, proof, exact-contribution
discussion, and mathematical limitations are unchanged.  Replacing the new
status block by the preceding status block reproduces the preceding hash
exactly; this was checked before rebinding the audit to the current hash.

This audit independently reconstructs the Gallai--Edmonds type list, the
explicit `K_7`-minor obstruction, every clique bound and named-vertex
placement, and supplements the written argument with an exhaustive
eight-vertex counterexample search.  There are no unresolved assumptions or
gaps within the theorem's stated structural scope.

## 1. Inputs and the four Gallai--Edmonds types

Let `nu(F)` denote the size of a maximum matching.  For the
Gallai--Edmonds decomposition `V(F)=D dotcup A dotcup C`, with `q`
components `D_1,...,D_q` of `F[D]`, the standard structure theorem gives:

1. every `F[D_i]` is factor-critical and hence has positive odd order;
2. `F[C]` has a perfect matching;
3. there is no `F`-edge between `D` and `C`; and
4. the matching deficiency is

   \[
                         8-2\nu(F)=q-|A|.            \tag{1.1}
   \]

Distinct `D_i` have no `F`-edge between them by their definition as
components of `F[D]`.

The asserted four types can be recovered directly.  If `q>=5`, choose one
vertex from each of five distinct `D_i`.  They form a five-vertex clique in
`J`.  If `u,v` are the vertices of `I_2` and `w` is any of the three unused
boundary vertices, then

\[
       \{u,w\},\quad \{v\},\quad
       \{z_1\},\ldots,\{z_5\}
\]

are seven disjoint connected branch sets.  The five singleton branch sets
are pairwise adjacent, each meets both apex branch sets through the join,
and `wv` gives adjacency between `\{u,w\}` and `\{v\}`.  This is an
explicit `K_7`-minor model, so `q<=4`.

Because `F` has even order and no perfect matching, the left side of (1.1)
is a positive even integer.  Thus `q-|A|>=2`, whence `|A|<=2`.  Enumerating
`q<=4`, `|A|<=2`, and positive even `q-|A|` gives exactly

\[
 (|A|,q)\in\{(0,2),(0,4),(1,3),(2,4)\}.
\]

Thus the type list used in the audited theorem does not require any
additional unstated property.

## 2. Clique bounds

The same explicit minor model shows the stronger fact `omega(J)<=4`: if
`Q` is any five-vertex clique of `J`, choose `w` outside `Q` and use
`\{u,w\}`, `\{v\}`, and the five singleton vertices of `Q`.  In particular,
the construction does not mistakenly require the non-edge `uv` to be
present.

In `J`, distinct `D_i` are complete to one another, and every `D_i` is
complete to `C`.  Extending a clique of `J[D_i]` by one vertex from each of
the other `q-1` components gives

\[
                         \omega(J[D_i])\le 5-q.
\]

Extending a clique of `J[C]` by one vertex from every `D_i` gives

\[
                         \omega(J[C])\le 4-q.
\]

These arguments remain valid when `C` is empty, with the standard
convention `omega(emptyset)=0`.  This verifies Lemma 2.1 exactly.

## 3. Use of the named induced matching

On the named vertices, the only `J`-edges are `x_1x_2` and `y_1y_2`.
Consequently their induced subgraph in `F` is the connected cycle
`K_{2,2}`.  Deleting any one named vertex leaves a connected three-vertex
path, and that path contains both endpoints of the other named `J`-edge.
If one endpoint of each named `J`-edge is deleted, the two remaining named
vertices are adjacent in `F`.

These elementary observations justify every localization step below: a
connected named subgraph disjoint from `A` cannot meet two `D_i`, nor can it
meet both `D` and `C`.

### Type `(0,4)`

Here the clique bounds say that every `J[D_i]` is independent and that
`omega(J[C])<=0`, so `C` is empty.  Since `A` is empty, the connected named
four-cycle lies in one `D_i`.  That component then contains both named
`J`-edges, contradicting independence.  Hence this type is impossible.

### Type `(2,4)`

Again every `J[D_i]` is independent and `C` is empty.  The four positive
odd component orders sum to `8-|A|=6`; hence they are `3,1,1,1`.

Let `k` be the number of named vertices in `A`.  If `k=0`, the named cycle
lies in one independent `J[D_i]`, a contradiction.  If `k=1`, the remaining
named path lies in one `D_i` and contains a named `J`-edge, again a
contradiction.  Therefore `k=2`, and because `|A|=2`, every vertex of `A`
is named.

If `A` is one entire named edge, the endpoints of the other named edge
cannot share an independent `J[D_i]`; they therefore occupy distinct
components.  If `A` contains one endpoint of each named edge, the two
remaining vertices are `F`-adjacent and hence share a component.  That
component contains at least two vertices and so must be the unique
three-vertex component.  This is precisely the placement asserted in part
2 of the theorem.

### Type `(1,3)`

The clique bounds give `omega(J[D_i])<=2` and `omega(J[C])<=1`; thus every
`J[D_i]` is triangle-free and `J[C]` is independent.

If the single vertex of `A` is unnamed, the full named cycle lies in one
component of `F-A`.  It cannot lie in `C`, because it contains the two named
`J`-edges while `J[C]` is independent.  It therefore lies in one `D_i`.
That factor-critical component contains at least four vertices and has odd
order, so its order is at least five.

If the vertex of `A` is named, the remaining named path lies in one
component of `F-A`.  It contains a named `J`-edge and hence cannot lie in
`C`; it lies in one `D_i`.  Were that component of order three,
factor-criticality would force all three of its pairs to be `F`-edges:
after deleting any vertex, the other two must form a perfect matching.
Thus `F[D_i]=K_3` and `J[D_i]` is independent, contradicting the named
`J`-edge.  Its order is therefore at least five.

In both subcases one deficient component has order at least five, and the
other two have positive odd order.  Together with the one vertex of `A`,
these already account for all eight vertices.  Hence `C` is empty and the
component orders are exactly `5,1,1`.  The named placements stated in part
3 follow from the two subcases.

### Type `(0,2)`

With `A` empty, the connected named cycle lies in one component of `F`.
The absence of edges between distinct `D_i` and between `D` and `C` implies
that it lies either in one `D_i` or wholly in `C`.  Substituting `q=2` in
the clique bounds gives

\[
       \omega(J[D_i])\le3,\qquad \omega(J[C])\le2,
\]

as asserted.

## 4. Exhaustive counterexample search

As a diagnostic stronger than a search only over the theorem's instances,
all `2^22=4,194,304` completions of the six prescribed pairs among the four
named vertices were enumerated.  The search imposed only the necessary
condition `omega(J)<=4`, rather than the stronger hypothesis that
`I_2 vee J` is `K_7`-minor-free.  It computed maximum matchings by the exact
subset recurrence, then used

\[
             v\in D \quad\Longleftrightarrow\quad
             \nu(F-v)=\nu(F)
\]

to reconstruct `D`, followed by `A=N_F(D)-D`, `C`, and the components of
`F[D]`.

There were `4,123,887` completions with `omega(J)<=4`, of which `120,276`
had no perfect matching in `F`.  Their type counts were

\[
\begin{array}{c|rrrr}
(|A|,q)&(0,2)&(0,4)&(1,3)&(2,4)\\ \hline
\text{count}&87,572&0&21,960&10,744.
\end{array}
\]

Every one satisfied the theorem's component-order, clique, and named-vertex
placement conclusions.  This computation is supplementary: the verdict
rests on the written derivation in Sections 1--3.

## 5. Scope

The proof uses no colouring-extension assertion and makes no claim that an
alternating path in `F` is a Kempe chain in either shore.  It also does not
show that `A` meets every `K_5`-minor model.  The limitations in the audited
file therefore match the actual proof.  The theorem is a boundary-structure
result only and does not prove `HC_7`.
