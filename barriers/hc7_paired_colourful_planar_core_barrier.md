# A planar four-connected core does not synchronize two colourful sets

**Status:** barrier to a static paired-root claim; written proof with a
computer-assisted complete-minor exclusion; separate internal audit GREEN.
This is not a counterexample to `HC_7`.

## 1. Claim refuted

The following strengthening of the paired-colourful-set step is false:

> Let `R` be a planar four-connected four-chromatic graph and let `S,T`
> be colourful in `R`.  Add adjacent vertices `z,u` with
> `N_R(z)=S` and `N_R(u)=T`, and call the resulting graph `Q`.  If `Q` is
> five-chromatic and has no `K_6` minor, then `R` has a `K_4`-minor model
> every branch set of which meets both `S` and `T`.

Thus planarity, four-connectivity of the four-chromatic core, and the full
static chromatic and complete-minor conclusions of the star--Kempe
compression do not synchronize the two rooted models.  A positive theorem
must use information from the lifted seven-chromatic, minor-critical host.

## 2. The nine-vertex core

Let `R` have vertex set `0,...,8` and edge set

```text
03 04 06 07   13 15 16 18   24 25 27 28
35 36 37      46 47 48      57 58 68.
```

Its graph6 encoding is `HEhutxm`.  Put

\[
             S=\{0,3,5,7\},\qquad T=\{0,4,6,8\}.       \tag{2.1}
\]

The following oriented triangular faces give a plane embedding:

```text
063 046 074 037 153 185 168
136 247 284 275 258 357 486.
```

Every directed edge occurs once in this list.  There are `14=2-9+21`
faces, so this is a spherical two-cell embedding.  Direct inspection of
the edge list shows that these are all the triangles of `R`.  Hence the
maximal planar graph `R` has no separating triangle and is
four-connected.  The verifier independently checks planarity and vertex
connectivity.

### Proposition 2.1

The graph `R` is four-chromatic.  Up to a permutation of the colours, its
proper four-colourings induce exactly the following two partitions:

\[
 \{012,34,56,78\},\qquad \{012,38,45,67\}.             \tag{2.2}
\]

Consequently, both `S` and `T` are colourful.

#### Proof

The unique independent triple of `R` is `\{0,1,2\}`.  On the remaining
six vertices, the complement of `R` is the cycle

\[
                       3,4,5,6,7,8,3.            \tag{2.3}
\]

A three-colouring could cover at most three vertices with one colour and
at most two with each of the other two colours, so it could cover at most
seven vertices.  Thus `R` is not three-colourable.  Either partition in
(2.2) is a proper four-colouring.

In any four-colouring, some colour class has order three, since four
classes of order at most two cover at most eight vertices.  It must be the
unique independent triple `012`.  The other three classes are independent
pairs partitioning `3,...,8`; equivalently, they form a perfect matching
of the complementary cycle (2.3).  That cycle has exactly the two perfect
matchings displayed in (2.2).  Each of the sets in (2.1) contains one
vertex from every block of either partition, proving colourfulness.
\(\square\)

### Proposition 2.2

There is no `K_4`-minor model in `R` all four branch sets of which meet
both `S` and `T`.

#### Proof

Suppose that four such branch sets exist.  Since `|S|=|T|=4`, disjointness
forces each branch set to contain exactly one vertex of `S` and exactly one
vertex of `T`.  The branch set containing the common vertex `0` therefore
contains no other vertex of \(S\cup T\).  The only remaining vertices are
`1,2`, and `0,1,2` are pairwise nonadjacent.  Connectivity forces this
branch set to be the singleton `\{0\}`.

Each of the other three branch sets must be adjacent to `0`, connected,
and contain one vertex from each of

\[
                       \{3,5,7\},\qquad\{4,6,8\}.     \tag{2.4}
\]

Allowing the unused vertices `1,2` as internal vertices, the feasible
root pairs are

\[
                         36,38,54,56,74,78.           \tag{2.5}
\]

Indeed, `36` and `74` are edges; `38` and `56` require vertex `1`; and
`54` and `78` require vertex `2`.  Every other pair is either disconnected
even after using `1,2`, or has no edge to the singleton `\{0\}`.

The bipartite graph in (2.5) has exactly two perfect matchings:

\[
                    \{36,54,78\},\qquad\{38,56,74\}. \tag{2.6}
\]

In the first, both the `54` and `78` branch sets require vertex `2`; in
the second, both the `38` and `56` branch sets require vertex `1`.
Disjointness fails in either case.  Hence even three disjoint connected
branch sets satisfying the root and singleton-adjacency requirements do
not exist, and a paired `K_4` model is impossible.
\(\square\)

## 3. The five-chromatic `K_6`-minor-free extension

Add vertices `z=9` and `u=10`, the edge `zu`, all edges from `z` to `S`,
and all edges from `u` to `T`; call the resulting graph `Q`.  The
neighbourhood identities are literal:

\[
                         N_R(z)=S,\qquad N_R(u)=T.     \tag{3.1}
\]

Since the relevant neighbourhood is colourful, neither `R+z` nor `R+u`
is four-colourable.  Both are five-colourable.  In particular,
\(\chi(Q)\ge 5\).  The independent-set partition

\[
             \{0,5\},\{3,4\},\{6,7\},\{8,z\},\{1,2,u\}              \tag{3.2}
\]

is a proper five-colouring of `Q`.  Therefore

\[
                  \chi(Q)=\chi(R+z)=\chi(R+u)=5.      \tag{3.3}
\]

### Computer-assisted finite result

The graph `Q` has no `K_6` minor.  This finite assertion is checked by the
adjacent deterministic verifier in two independent exhaustive encodings:

1. enumerate every nonempty connected vertex subset and search for six
   pairwise disjoint, pairwise adjacent subsets; and
2. enumerate canonical assignments of all eleven vertices to six
   nonempty branch sets or an unused set, testing connectivity and every
   required adjacency.

Both searches permit branch sets of every possible order.  Both are first
tested on `K_6` as a positive control.  With NetworkX 3.x installed, run

```bash
python3 barriers/hc7_paired_colourful_planar_core_barrier_verify.py
```

For example, an isolated environment can be prepared with

```bash
python3 -m venv /tmp/hc7-paired-check
/tmp/hc7-paired-check/bin/pip install 'networkx>=3,<4'
/tmp/hc7-paired-check/bin/python \
  barriers/hc7_paired_colourful_planar_core_barrier_verify.py
```

The expected output is

```text
PASS graph6=HEhutxm
PASS R: planar, kappa=4, chi=4, labelled_4_colourings=48
PASS S,T: colourful; no paired K4 minor
PASS Q: chi=5; no K6 minor (two exact exhaustive encodings)
```

The verifier also enumerates all `48` labelled four-colourings of `R`,
checks (2.2), and performs an unrestricted connected-subset search for the
paired `K_4` model.  The written arguments above do not depend on those
two auxiliary checks.

If a universal vertex `x` is added to `Q`, the resulting graph
\(K_1\vee Q\) is six-chromatic and has no `K_7` minor: a `K_7` model would,
after discarding its unique branch set containing `x` if necessary, give a
`K_6` model in `Q`.  Thus the counterexample persists after the universal
contraction that represents the connected dominating subgraph in the
compressed quotient.

## 4. Exact scope

This construction refutes a static paired-root theorem even after adding
all of the following assumptions:

- the four-chromatic core is planar and four-connected;
- both prescribed neighbourhoods are colourful;
- the two outside vertices are adjacent and each individually raises the
  chromatic number to five;
- the combined core `Q` is five-chromatic and `K_6`-minor-free; and
- adjoining the universal contracted vertex gives a six-chromatic,
  `K_7`-minor-free quotient.

It does **not** construct the connected induced bipartite subgraph `X` of
the star--Kempe theorem.  It does not construct a seven-connected or
seven-chromatic graph, and it has none of the proper-minor colouring
transitions of a hypothetical minimal `HC_7` counterexample.  It therefore
does not refute the lifted alternative allowing an actual order-seven
separation or a fixed two-vertex transversal of all `K_5` models.

The correct consequence is narrower: Martinsson--Steiner's theorem applied
separately to two colourful sets cannot be synchronized by adding
planarity, four-connectivity, or the compressed complete-minor exclusion.
Any successful synchronization must use the literal lifted host and its
minor-critical colouring responses.
