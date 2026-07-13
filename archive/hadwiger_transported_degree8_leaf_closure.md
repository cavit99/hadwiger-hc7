# The transported degree-eight leaf: sole-shore closure and one locked relay

## 1. Setting

Let `G` be a proper-minor-minimal counterexample to `HC_7`, and use the
notation of `hadwiger_c6_hub_leaf_degree8_transport.md`.  Thus `u` is a
degree-eight leaf of the full-deletion hub graph,

\[
 P=N_S(u),\qquad
 U=N_G(u)=P\dot\cup\{w\}\dot\cup
       \{y_s:s\in S-P\}.                              \tag{1.1}
\]

The canonical exterior component `F` contains `H union (S-P)` and has

\[
                       N_U(F)=U-\{w\}.                \tag{1.2}
\]

There is at most one other component `R`; if it exists it has boundary
defect of order at most one.  The old boundary satisfies

\[
 \overline{G[S]}=C_6\dot\cup K_1.                    \tag{1.3}
\]

The exact two-piece atlas says that `P` is contained in one of

\[
 T_0\cup\{z\},\qquad T_1\cup\{z\},\qquad M_i\cup\{z\}, \tag{1.4}
\]

where `T_0,T_1` are the two prism triangles, `M_i` is an antipodal
prism edge, and `z` is the universal old-boundary vertex.  In particular,
`P` is a clique and `|P|<=4`.

This note proves two new facts.

1. If `R` is empty, the entire transported cell contains `K_7`.
2. If `R` is nonempty and `P` lies in an old-boundary `K_4`, a direct
   relay packing closes the cell except for one exact locked-relay state.

The second residue and the antipodal `K_3` row are two presentations of
the same one-extra-bag rooted exchange problem.

## 2. Why the sole-shore boundary is dense

### Lemma 2.1 (literal degree bounds)

Assume `R` is empty and put `A=G[U]`.  Then

\[
 \alpha(A)\le3,\qquad d_A(w)\ge6,qquad
 d_A(y_s)\ge5\quad(s\in S-P).                       \tag{2.1}
\]

Moreover every `p in P` has a neighbour in `U-P`.

### Proof

Dirac's neighborhood inequality at the degree-eight vertex `u` gives

\[
 \alpha(G[U])\le d(u)-7+2=3.
\]

There is no edge from the old shore `H` to the old shore `D`.  Also, for
`s in S-P`, the tight leaf identity says

\[
                         N_D(s)=\{y_s\}.             \tag{2.2}
\]

Consequently `w` has no neighbour outside `U union {u}`: it sees neither
`H` nor `S-P`, and `R` is empty.  Since `delta(G)>=7`,

\[
                         d_A(w)=d_G(w)-1\ge6.
\]

The only neighbours of `y_s` outside `U` are `u` and `s`.  It has no
neighbour in `H`, and an edge to another `t in S-P` would contradict
`N_D(t)={y_t}`.  Hence

\[
                         d_A(y_s)=d_G(y_s)-2\ge5.
\]

Finally `D-u` is full to `S`.  When `R` is empty its vertices outside
`U` are absent, so every `p in P` has a representative in
`{w} union {y_s:s in S-P}=U-P`.  This representative is an actual
boundary neighbour of `p`.  \(\square\)

## 3. Complete closure with one exterior component

### Theorem 3.1 (sole-exterior transported leaf)

If `R` is empty, `G-u` contains a `U`-meeting `K_6`-model.  Consequently
`G` contains a `K_7`-minor.

### Certified proof

The finite lemma used here is the following exact eight-boundary
statement.

> Let `A` be a graph on
> `P dotcup Y dotcup {w}`, where `|P|+|Y|=7` and `|P|<=4`.  Suppose
> `P` is a clique, `alpha(A)<=3`, `d_A(w)>=6`, every `y in Y` has
> `d_A(y)>=5`, and every vertex of `P` has a neighbour in `Y union {w}`.
> Add one helper `f` adjacent to every boundary vertex except `w`.
> Then the resulting graph has a boundary-meeting `K_6`-model.

The independent verifier is

`transported_leaf_one_shore_verify.py`.

For each `p=|P|` from zero through four it independently rebuilds all
28 boundary-edge variables.  The seventy clauses indexed by the
four-subsets of the boundary express `alpha(A)<=3`; pseudo-Boolean
clauses express the displayed degree bounds; ordinary clauses express
the clique and representative conditions.

Every boundary-meeting `K_6`-model in the nine-vertex quotient has the
following unique finite description: select between six and eight
boundary vertices, partition the selected set into six nonempty bag
traces, and either omit the helper or put it in one of the six bags.
There are 462 boundary partitions and seven helper choices, hence 3,234
templates.  For each template the verifier reconstructs connectivity by
requiring an edge across every cut of every bag, and reconstructs all
fifteen interbag adjacencies.  It asserts the negation of every template.
The five resulting formulas are all unsatisfiable:

```text
p=0 verified UNSAT with 3234 exhaustive model templates
p=1 verified UNSAT with 3234 exhaustive model templates
p=2 verified UNSAT with 3234 exhaustive model templates
p=3 verified UNSAT with 3234 exhaustive model templates
p=4 verified UNSAT with 3234 exhaustive model templates
```

This is exhaustive because every branch bag must meet the eight-vertex
boundary; the sole nonboundary helper therefore belongs to at most one
bag.  Contracting `F` to `f` gives precisely this quotient by Lemma 2.1.
Lift the helper back to the connected graph `F`, then add the singleton
bag `{u}`.  This proves the theorem.  The formal trust boundary is the
short independent verifier, Z3's Boolean/pseudo-Boolean kernel, and the
host Python runtime; no DRAT trace is exported.  \(\square\)

This closes an unbounded family: no assumption is made on the order or
internal structure of `H`.

## 4. Four-clique relay packing with two exterior components

Assume now that `R` is nonempty.  Choose an old-boundary four-clique
`T` containing `P`, when one exists, and put

\[
 Q=T-P,\qquad
 Y_Q=\{y_q:q\in Q\},\qquad
 Y_0=\{y_s:s\in S-T\}.                              \tag{4.1}
\]

Thus `|T|=4` and `|Y_0|=3`.  Put

\[
                         A=F-Q.                     \tag{4.2}
\]

The graph `A` is connected: it contains the connected full shore `H`,
and every old-boundary vertex in `S-T` has a neighbour in `H`.  It sees
every vertex of `P union Y_0`.  For every `q in Q`, the two-vertex set

\[
                         B_q=\{q,y_q\}              \tag{4.3}
\]

is a connected `U`-meeting bag.

### Lemma 4.1 (relay packing)

Let `m` be the possible unique member of `U-N_U(R)`.  If either

1. `m` is absent or does not belong to `P union Y_Q`; or
2. `m in Y_Q`; or
3. `m in P` and `m` has a neighbour in `Y_0 union {w}`,

then `G-u` has a `U`-meeting `K_6`-model.

### Proof

Start with the four pairwise adjacent bags

\[
 \mathcal B=\{\{p\}:p\in P\}\cup\{B_q:q\in Q\}.    \tag{4.4}
\]

They are pairwise adjacent because their old-boundary representatives
are the four vertices of the clique `T`.  The connected graph `A` is
adjacent to every bag of `mathcal B`, through `H` and its full contacts
with `T`.

First suppose `R` sees every `U`-trace occurring in (4.4).  Choose
distinct `a,b in Y_0`, avoiding `m` if it belongs to `Y_0`, and use

\[
                         A\cup\{a\},\qquad R\cup\{b\}. \tag{4.5}
\]

Both are connected.  The second is adjacent to the first through the
edge from `R` to `a`, and both are adjacent to every bag in (4.4).
Together these are six bags.

Suppose `m=y_q in Y_Q`.  The only neighbours of `y_q` outside `U` are
`u,q`, because `R` misses `y_q`, `H` is anticomplete to `D`, and (2.2)
excludes every other old-boundary neighbour.  Minimum degree gives
`d_{G[U]}(y_q)>=5`.  Among the other traces in (4.4) there are only
three vertices, so `y_q` has a neighbour

\[
                         b\in Y_0\cup\{w\}.          \tag{4.6}
\]

Use `R union {b}`; the edge `by_q` repairs its sole missing adjacency,
namely the adjacency to `B_q`.  Choose `a in Y_0-{b}` when `b in Y_0`,
and arbitrary `a in Y_0` when `b=w`.  The two bags in (4.5), with this
new choice of `b`, again complete (4.4).

The same repair works when `m in P` and hypothesis 3 supplies `b`.
These cases cover the statement.  \(\square\)

### Corollary 4.2 (the four-contact row closes)

If `|P|=4`, the transported cell contains a `K_7`-minor.

### Proof

Here `Q` is empty.  If the possible defect `m` belongs to `P`, fullness
of `D-u` supplies an actual neighbour of `m` in
`Y_0 union {w}`.  Lemma 4.1 applies in every case.  Add `{u}` to its
six-bag model.  \(\square\)

## 5. Exact two-shore residue

Lemma 4.1 leaves only the following state when `P` lies in a four-clique:

\[
 \begin{gathered}
 U-N_U(R)=\{p\}\quad\text{for some }p\in P,\\
 N_U(p)\cap(Y_0\cup\{w\})=\varnothing.             \tag{5.1}
 \end{gathered}
\]

Since `D-u` is full to `S`, (5.1) forces

\[
                         N_U(p)\cap Y_Q\ne\varnothing. \tag{5.2}
\]

Thus `Q` is nonempty and `|P|<=3`.  Every available literal repair of
the missing `R`--`p` adjacency lies in `P union Y_Q`, hence is already
committed to one of the four clique bags (4.4); (5.2) guarantees in
particular an available private relay in `Y_Q`.  This is the
**locked-relay state**.  It is an internal placement obstruction, not a
contact-count obstruction.

If no four-clique `T` contains `P`, (1.4) says exactly that `P` contains
an antipodal prism pair and is contained in the three-clique
`M_i union {z}`.  The relay packing then begins with three, rather than
four, canonical clique bags and is short by the same one bag.

Both forms are therefore covered by one remaining rooted statement.

> **One-extra-bag relay web theorem.**  In a seven-connected
> contraction-critical graph, take a clique row of order three, or a
> four-clique row in the locked state (5.1)--(5.2), together with the
> exact edge-deletion state on the promoted hub edge `uw`.  Then either
> the canonical relay bags extend by connected shore surgery to a
> `U`-meeting `K_6`-model, or failure produces a labelled two-shore web
> gate on which the two proper-minor equality states agree and hence
> six-color-glue.

This target is label-free after naming the clique row, its private relay
edges, and the one deficient root.  It asks for exactly one additional
rooted bag; it is not the unrestricted degree-eight neighborhood problem.
The promoted-edge coloring gives the dynamic hypothesis: in every
six-coloring of `G-uw`, `u,w` share one color and both endpoints have a
literal neighbour in every other palette on the specified old shore.

## 6. Net effect

The transported hub-leaf branch is now reduced as follows.

* One exterior component: eliminated completely by Theorem 3.1.
* Two exterior components with `|P|=4`: eliminated completely by
  Corollary 4.2.
* Two exterior components with a four-clique completion: eliminated
  except for the exact locked relay (5.1)--(5.2).
* No four-clique completion: the unique structural cause is the
  antipodal three-clique row, which needs the same one-extra-bag exchange.

Thus the unbounded sole-shore family is closed, and the two-shore cell no
longer ranges over arbitrary degree-eight neighborhoods or arbitrary
defect placements.
