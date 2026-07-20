# Spanning core in the pentagonal-bipyramid column case

**Status:** written proof; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_spanning_core_audit.md`](hc7_pentagonal_bipyramid_spanning_core_audit.md).

This note isolates a host-level consequence of the exceptional
seven-column contact graph.  It proves that an extremal column system spans
the graph outside its two fixed root branch sets and that the resulting
induced subgraph is four-connected and nonplanar.  It does **not** align a
`K_5` model in that subgraph with the five prescribed column labels, does
not synchronize colourings across a separation, and does not prove
`HC_7`.

## 1. Setup

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,
 \qquad K_7\not\preccurlyeq G,
\]

and suppose every proper minor of `G` is six-colourable.  Let `v,p,w` be
distinct vertices such that

\[
 vp,pw\in E(G),\qquad vw\notin E(G).                 \tag{1.1}
\]

Put

\[
 R_0=G[\{v,p\}],\qquad R_1=G[\{w\}].                \tag{1.2}
\]

Assume that there are seven pairwise vertex-disjoint connected subgraphs

\[
                         L_1,\ldots,L_7              \tag{1.3}
\]

of `G-{v,p,w}`, each adjacent to both `R_0` and `R_1`.  In the
order-eight construction that motivates this note, each `L_i` also
contains a fixed path from a neighbour of `v` to a neighbour of `w`.
These seven paths, and any other prescribed subgraphs already contained in
the columns, are retained throughout the enlargement below.

The **column-contact graph** `J` has vertex set `[7]` and

\[
 ij\in E(J)
 \quad\Longleftrightarrow\quad
 E_G(L_i,L_j)\ne\varnothing.                          \tag{1.4}
\]

Assume that `J` is the pentagonal bipyramid

\[
                         C_5\vee\overline{K_2}.       \tag{1.5}
\]

The proved seven-column structure theorem shows that this graph is
edge-maximal `K_5`-minor-free: adding any one of its six missing edges
creates a `K_5` minor.  See the
[seven-column contact theorem](hc7_seven_column_contact_structure.md).

Call a seven-tuple `(L'_1,...,L'_7)` an **admissible enlargement** if:

1. the `L'_i` are pairwise disjoint connected subgraphs disjoint from
   `R_0\cup R_1`;
2. `L_i\subseteq L'_i` for every `i`;
3. every `L'_i` is adjacent to both root branch sets; and
4. its column-contact graph is still exactly the graph in (1.5).

Choose an admissible enlargement maximizing

\[
                         \sum_{i=1}^7 |V(L'_i)|,       \tag{1.6}
\]

and rename it `(L_1,...,L_7)`.

## 2. The spanning reduction

### Theorem 2.1 (maximal pentagonal-bipyramid columns span)

Under the setup above,

\[
             V(G)=\{v,p,w\}\mathbin{\dot\cup}
                    \bigsqcup_{i=1}^7 V(L_i).          \tag{2.1}
\]

In particular, all fixed paths and other prescribed column subgraphs from
the original paired-column construction survive in a spanning column
system.

#### Proof

Suppose instead that `Z` is a component of

\[
 G-\left(\{v,p,w\}\cup\bigcup_{i=1}^7V(L_i)\right).  \tag{2.2}
\]

The component `Z` has a neighbour in some column.  Otherwise

\[
                         N_G(Z)\subseteq\{v,p,w\},    \tag{2.3}
\]

which contradicts seven-connectivity.

Let `A\subseteq[7]` be the set of column labels met by `Z`.  If `A`
contains two nonadjacent labels `i,j` of the pentagonal bipyramid, then
connectedness of `Z` gives an `L_i`--`L_j` path whose internal vertices
lie in `Z`.  Absorb that path, except for its final vertex in `L_j`, into
`L_i`.  The seven modified columns remain pairwise disjoint and connected,
retain both root contacts and every old column contact, and acquire the
missing contact `ij`.  Their contact graph therefore contains `J+ij`.
By edge-maximality, `J+ij` contains a `K_5` minor.  Its five branch sets
lift through the corresponding columns, and together with `R_0,R_1` form
an explicit `K_7`-minor model in `G`, a contradiction.

It follows that `A` is a clique of `J`.  Choose `i\in A` and replace

\[
                         L_i\quad\hbox{by}\quad L_i\cup Z.   \tag{2.4}
\]

This new column is connected.  It is disjoint from the other columns and
the roots, contains its original prescribed subgraphs, and retains both
root contacts.  Every column newly met through `Z` has a label in `A` and
is already adjacent to `i`, because `A` is a clique.  Hence (2.4) creates
no new edge in the contact graph, so it is an admissible enlargement.  It
strictly increases (1.6), contradicting maximality.

No component `Z` exists, proving (2.1).  \(\square\)

## 3. The induced core

Put

\[
                          F=G-\{v,p,w\}.               \tag{3.1}
\]

By Theorem 2.1, the seven columns partition `V(F)`.

### Theorem 3.1 (connectivity and chromatic core)

The graph `F` has all of the following properties.

1. `F` is four-connected.
2. `F` is nonplanar.
3. `5\le\chi(F)\le6`.
4. `\chi(G-\{v,w\})=6`.

#### Proof

If `X\subseteq V(F)` with `|X|\le3` separated `F`, then

\[
                         X\cup\{v,p,w\}                \tag{3.2}
\]

would separate `G` and have order at most six.  This contradicts
seven-connectivity.  Since the seven columns are nonempty, `|V(F)|\ge7`,
so `F` is four-connected.

If `\chi(F)\le4`, colour `F` with four colours and colour `v,w` alike
with a fifth colour and `p` with a sixth.  This is proper by (1.1), and
contradicts `\chi(G)=7`.  Hence `\chi(F)\ge5`.  Since `F` is a proper
minor of `G`, the minor-minimality assumption gives `\chi(F)\le6`.
The Four Colour Theorem now also shows that `F` is nonplanar.

Finally, `G-\{v,w\}` is a proper minor, so it is six-colourable.  If it
were five-colourable, that colouring could be extended by assigning the
same new sixth colour to the nonadjacent vertices `v,w`.  This would
again six-colour `G`.  Therefore

\[
                         \chi(G-\{v,w\})=6.             \tag{3.3}
\]

\(\square\)

### Proposition 3.2 (what a four-cut returns)

If `X` is a four-vertex cut of `F`, then

\[
                         S_X=X\cup\{v,p,w\}             \tag{3.4}
\]

is the boundary of an actual order-seven separation in `G`.  Moreover,
every component of `G-S_X=F-X` has a neighbour at every literal vertex of
`S_X`.

#### Proof

The components of `F-X` are precisely the components of `G-S_X`, so
(3.4) is an actual order-seven separator.  Let `C` be one such component.
If `C` missed some `s\in S_X`, then

\[
                         N_G(C)\subseteq S_X-\{s\},     \tag{3.5}
\]

and `N_G(C)` would have order at most six.  Since `F-X` has another
component, this contradicts seven-connectivity.  Thus `C` is adjacent to
all seven vertices of `S_X`.  \(\square\)

Proposition 3.2 is only a structural separation statement.  It does not
show that the two closed shores induce the same equality partition on
`S_X`, and hence does not by itself give a six-colouring of `G`.

### Corollary 3.3 (the no-four-cut branch)

If `F` has no four-vertex cut, then `F` is five-connected and contains a
subdivision of `K_5`.

#### Proof

Theorem 3.1 gives four-connectivity, so the absence of a four-cut makes
`F` five-connected.  It is nonplanar by the same theorem.  The
Kelmans--Seymour theorem therefore gives a subdivision of `K_5` in `F`.
The cited theorem was proved by Dawei He, Yan Wang and Xingxing Yu in the
four-paper series culminating in *The Kelmans--Seymour conjecture IV: A
proof*, Journal of Combinatorial Theory, Series B 144 (2020), 309--358;
preprint <https://arxiv.org/abs/1612.07189>.  \(\square\)

## 4. Exact contribution and remaining gap

The maximal-coverage argument removes all vertices outside the fixed
roots and the seven prescribed columns.  Thus the exceptional quotient is
not hiding arbitrary additional components: it produces a spanning
four-connected nonplanar graph `F`, partitioned into the seven connected
columns and retaining the seven prescribed paths from `N_F(v)` to
`N_F(w)`.

There are now two precise branches.

1. A four-cut of `F` returns an actual order-seven separator whose every
   complementary component is adjacent to every boundary vertex.  What is
   still missing is a common boundary equality partition supplied by
   colourings of both closed shores.
2. If there is no four-cut, `F` is five-connected and contains a
   subdivision, hence a minor model, of `K_5`.  What is still missing is a
   label-preserving construction of a `K_5` model with all five branch
   sets adjacent to both fixed root branch sets.  An arbitrary `K_5`
   subdivision need not have that property.

In the second branch, such a simultaneously rooted `K_5` model would,
together with `R_0=G[\{v,p\}]` and `R_1=G[\{w\}]`, be an explicit
`K_7`-minor model.  Producing that rooted model, or proving the compatible
colouring conclusion in the first branch, is the remaining
pentagonal-bipyramid response-coupling problem.
