# Complete two-component closure in the pure-Moser cell

**Status:** proved and independently audited.

## 1. Setting and result

Let `G` be seven-connected, `K_7`-minor-free, and proper-minor-minimal
subject to not being six-colourable.  Let `v` have neighbourhood

\[
 S=\{0,1,2,3,4,5,6\},\qquad
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.       \tag{1.1}
\]

Suppose
\[
                         G-N[v]=C\mathbin{\dot\cup}D
\]
has exactly two nonempty connected components.  Both are `S`-full by
seven-connectivity.

### Theorem 1.1 (tiny-shore closure)

The component `D` cannot have order at most three.

The proof treats the standard small-graph connectivity conventions
explicitly: `K_2` is not called two-connected, and a connected graph of
order three is either a path or a triangle.

## 2. Singleton and edge shores

If `D={q}`, fullness and the fact that `D` is an exterior component give

\[
                           N(q)=S=N(v).                 \tag{2.1}
\]

The vertices `q,v` are nonadjacent because `q notin N[v]`.  A six-colouring
of the proper minor `G-q` extends to `q` by giving it the colour of its open
twin `v`, contradicting the choice of `G`.

Now let `D=\{p,q\}` have order two.  Connectivity makes `pq` an edge.  Put

\[
                  L=\{1,2\},\qquad R=\{3,4\},
\]
and for `A subseteq S` define

\[
                  P_D(A)=\{d\in D:E(d,A)\ne\varnothing\}.
\]

Then

\[
                         P_D(L)=P_D(R)=D.               \tag{2.2}
\]

For if, say, `|P_D(L)|<=1`, then

\[
                         P_D(L)\cup(S-L)                \tag{2.3}
\]

has order at most six and separates the nonempty set `D-P_D(L)` from `v`
and the opposite component `C`: after (2.3) is deleted it has no edge to the
surviving literals `L`, and exterior components are anticomplete.  This
contradicts seven-connectivity.  The proof for `R` is identical.

Regard the two singleton carriers `{p},{q}` and the two labels in `L` as a
bipartite incidence graph.  By (2.2) neither carrier is isolated; by
`S`-fullness neither label is isolated.  Hall's theorem therefore gives a
perfect matching.  The same holds for `R`.  Assign to each singleton
carrier its matched `L`-label and its matched `R`-label.  The two assigned
boundary blocks are consequently either

\[
                         13\mid24
                 \quad\hbox{or}\quad 14\mid23.         \tag{2.4}
\]

They are independent pairs, each carrier contacts both labels assigned to
it, and the two carriers are adjacent through `pq`.  The exact-state exchange
in `hc7_exact7_moser_four_corner_exchange.md`, Theorem 3.1, now gives a
six-colouring contradiction.  This closes `K_2` without assigning it any
nonstandard connectivity value.

## 3. Three-vertex shores

If `|D|=3` and `D` is not a triangle, connectedness makes it a three-vertex
path.  Its middle vertex is a cutvertex, contrary to the independently
audited pure-Moser low-cut theorem
`hc7_exact7_moser_rich_twocut_exchange.md`.

It remains that `D` is a triangle.  The separator argument in (2.3), now
with three vertices, gives

\[
                         |P_D(L)|\ge2,
                         \qquad |P_D(R)|\ge2.           \tag{3.1}
\]

Choose

\[
                         t\in P_D(L)\cap P_D(R),
\]
which exists because `D` has three vertices, and set

\[
                         X=\{t\},\qquad Y=D-\{t\}.      \tag{3.2}
\]

The sets `X,Y` are disjoint nonempty connected sets and are adjacent.  Each
has a neighbour in `L`: this holds for `X` by the choice of `t`, and for `Y`
by `|P_D(L)|>=2`.  Fullness says every label of `L` is seen by at least one
of the two carriers.  Hence their two-by-two incidence graph with `L` has a
perfect matching.  The same argument applies to `R`.  Assigning the matched
labels again yields one of the two independent complementary matchings in
(2.4).  Thus `X,Y` satisfy the exact-state carrier hypothesis, and the same
exchange gives a six-colouring contradiction.

This proves Theorem 1.1. \(\square\)

## 4. Exact state used above

For clarity, the cited exchange does not identify colours with pre-existing
bags.  If `r,e` are the two independent pairs in (2.4), contract

\[
                         \{v\}\cup r,
                         \qquad C\cup e.
\]

A six-colouring of this proper minor returns on the closed `D`-shore exactly
one of

\[
 R_0=\{r,e,0,5,6\},\qquad
 R_5=\{r,e,05,6\},\qquad
 R_6=\{r,e,06,5\}.                                    \tag{4.1}
\]

Contracting the two adjacent carriers with `r,e`, together with respectively
`{v,0}`, `{v,0,5}`, or `{v,0,6}`, reproduces the chosen state on the closed
`C`-shore.  The representatives form a literal `K_5` in the first case and
a `K_4` in the other two: each carrier contains one `L` corner (seeing `6`)
and one `R` corner (seeing `5`), while `56` is literal.  Palette permutation,
shore gluing, and the sixth colour absent from `S` then colour `G`.

## 5. Full pure-Moser two-component closure

Combine Theorem 1.1 with:

1. the audited low-cut theorem
   `hc7_exact7_moser_rich_twocut_exchange.md`, under which every
   exterior component of order at least four is three-connected; and
2. the independently audited four-corner theorem
   `hc7_exact7_moser_four_corner_exchange.md`, Theorem 4.1, which
   eliminates every two-connected full exterior component of order at least
   three (and hence every such three-connected component).

Every exterior component has positive order.  Theorem 1.1 eliminates orders
one through three; the two cited theorems eliminate every larger order.
Therefore the pure-Moser degree-seven two-exterior-component branch is
closed in full.  The only computational dependency is the finite quotient
atlas already exposed and independently audited in the low-cut theorem; the
new tiny-shore and four-corner exchanges are noncomputational.
