# A minimum positive-excess separator gives an exact-seven restart or two or three full components

**Status:** written proof; separate internal audit GREEN in
[`hc7_minimum_positive_separator_normal_form_audit.md`](hc7_minimum_positive_separator_normal_form_audit.md).

This theorem gives an unbounded host-level normal form for separator
excess.  It replaces a false attempt to count contracted branch sets as
literal separator vertices.  The proof uses proper-minor colourings and
global `K_7`-minor exclusion, but no inherited branch-set labels.

## 1. Setting

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Call a nonempty connected set `R` **eligible** when

\[
 G-(R\cup N_G(R))\ne\varnothing,
 \qquad |N_G(R)|\ge8.                                  \tag{1.2}
\]

Assume that an eligible set exists, choose one for which

\[
                         k:=|N_G(R)|                   \tag{1.3}
\]

is minimum, and put `X=N_G(R)`.  Let

\[
                         C_1,\ldots,C_m                \tag{1.4}
\]

be the components of `G-X`.  Thus `m>=2`.

## 2. Exact-seven restart or full components

### Lemma 2.1

Exactly one of the following conclusions is forced.

1. Some component `C_i` has `|N_G(C_i)|=7`.  For every edge
   `xc`, where `x in N_G(C_i)` and `c in C_i`, a proper six-colouring of
   `G-xc` makes

   \[
    \bigl(C_i,N_G(C_i),V(G)-(C_i\cup N_G(C_i));\,xc\bigr)
   \tag{2.1}
   \]

   a generic exact-seven response interface.
2. Every component of `G-X` is adjacent to every literal vertex of `X`.

#### Proof

For every component `C_i`, one has `N_G(C_i) subseteq X`.  Another
component of `G-X` is disjoint from `C_i union N_G(C_i)`, so
seven-connectivity gives `|N_G(C_i)|>=7`.

If equality holds, delete any crossing edge `xc`.  Every proper minor is
six-colourable, and the ends of `xc` must receive the same colour in every
proper six-colouring of `G-xc`; otherwise `G` itself would be
six-colourable.  This proves item 1.

Otherwise `|N_G(C_i)|>=8` for every `i`.  Each `C_i` is then eligible.
The minimality of `k`, together with `N_G(C_i) subseteq X`, gives

\[
                 k\le |N_G(C_i)|\le |X|=k.
\tag{2.2}
\]

Thus `N_G(C_i)=X` for every `i`, proving item 2. \(\square\)

For the rest of the theorem assume outcome 2 of Lemma 2.1.

## 3. The universal contraction profile

### Lemma 3.1

Let `1<=r<=min{m,5}`.  Choose distinct components
`C_{i_1},...,C_{i_r}` and a set

\[
                       F=\{x_1,\ldots,x_r\}\subseteq X
\tag{3.1}
\]

of distinct vertices.  Then

\[
 \chi(G[X-F])\le6-r,
 \qquad K_{7-r}\not\preccurlyeq G[X-F].                \tag{3.2}
\]

#### Proof

For each `j`, the set `C_{i_j} union {x_j}` is connected.  These `r`
sets are pairwise disjoint and pairwise adjacent, because every component
is adjacent to every vertex of `X`.  Contract each of them to one vertex
and delete every vertex outside these contraction images and `X-F`.
The resulting proper minor consists of an `r`-clique complete to
`G[X-F]`.

A proper six-colouring gives distinct colours to the `r` contracted
vertices, none of which can occur on `X-F`; this proves the chromatic
inequality.  A `K_{7-r}`-minor model in `G[X-F]`, together with the `r`
contracted vertices, would be a `K_7`-minor model in `G`.  This proves the
minor exclusion. \(\square\)

## 4. At most three components

### Theorem 4.1

In outcome 2 of Lemma 2.1,

\[
                              m\in\{2,3\}.             \tag{4.1}
\]

#### Proof

Suppose first that `m>=5`.  Lemma 3.1 with `r=5` says that `X-F` is
independent for every five-set `F subseteq X`.  Since `|X|>=8`, a five-set
can be chosen disjoint from the ends of any alleged edge of `G[X]`.
Therefore `X` is independent.

Fix a component `C_j`, choose another component `C_i`, and contract the
connected set `C_i union X` to one vertex.  A proper six-colouring of the
resulting minor restricts to a colouring of `C_j` and assigns one common
colour to all vertices of the independent set `X`.  Doing this for each
`j`, permuting the palettes to give `X` one fixed colour, and gluing the
component-side colourings produces a proper six-colouring of `G`.  This is
a contradiction.  Hence `m<=4`.

Suppose now that `m=4`.  Lemma 3.1 with `r=4` says that `G[X-F]` has no
`K_3` minor, and hence is a forest, for every four-set `F subseteq X`.
Consequently every cycle of `G[X]` has length at least `|X|-3`: a shorter
cycle would survive after deleting four vertices outside it.

We claim that `G[X]` is three-colourable.  Otherwise it has a
vertex-minimal non-three-colourable subgraph `H`; then `delta(H)>=3`.
Put `n=|X|` and `g=n-3>=5`.  The girth of `H` is at least `g`.  The Moore
bound for minimum degree three gives

\[
 |H|\ge
 \begin{cases}
  3\cdot2^s-2,&g=2s+1,\\
  2^{s+1}-2,&g=2s.
 \end{cases}                                           \tag{4.2}
\]

For every `g>=5` the right-hand side is greater than `g+3=n`, contrary to
`|H|<=|X|=n`.  This proves the claim.

Let `I_1,...,I_p`, where `p<=3`, be the nonempty colour classes of a
proper three-colouring of `G[X]`.  Fix a component `C_j` and choose `p`
distinct components among the other three.  Contract the connected sets

\[
                         C_{i_h}\cup I_h,
                         \qquad h=1,\ldots,p.           \tag{4.3}
\]

and delete all other vertices except `C_j`.  The contracted vertices form
a clique and the resulting proper minor is six-colourable.  Expanding only
the independent sets `I_h` gives a proper colouring of `G[C_j union X]`
which is constant on each `I_h` and uses distinct colours on distinct
classes.  Align these boundary assignments for all four choices of `j`
and glue.  This again six-colours `G`, a contradiction.  Hence `m` is two
or three. \(\square\)

## 5. Operation-specific responses

### Corollary 5.1

Let `C_i` be one of the two or three full components and let `xc` be an
edge with `x in X`, `c in C_i`.  Every proper six-colouring of `G-xc`
induces on `X` a complete equality partition which extends through every
closed component-side other than `C_i` and does not extend through the
intact graph `G[C_i union X]`.

#### Proof

The edge-deletion colouring is proper on all unchanged component-sides.
If its literal boundary assignment extended through `G[C_i union X]`,
permute its at most six colour names to agree literally with the displayed
edge-deletion colouring on `X`.  That extension and the unchanged
restrictions on the other component-sides would then glue to a proper
six-colouring of `G`. \(\square\)

## 6. Exact trust boundary

The theorem treats arbitrary separator order `k>=8`.  Its unresolved
normal form has two or three boundary-full components, the contraction
profile (3.2), and mutually exclusive operation-specific boundary
responses.  This is an unbounded reduction, not a finite boundary census.

An order-seven component in Lemma 2.1 gives a fresh generic response
interface, but the theorem does not assert that its shore is smaller than
a previously selected generic shore.  It also does not force `k=8`, align
two complete boundary partitions, preserve an inherited near-clique model,
or construct a `K_7` minor.

## 7. Dependencies

- [generic exact-seven selected-response restart](hc7_generic_exact7_response_restart.md)
