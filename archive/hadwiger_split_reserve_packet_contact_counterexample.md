# Split-reserve packets: a valid lift and a sharp contact counterexample

## 1. The explicit packet lemma

### Lemma 1.1 (split-reserve packet)

Let `X` be a boundary with an opposite connected shore `R` full to `X`.
Let another open shore split as

\[
                         C=\{u\}\mathbin{\dot\cup}A,           \tag{1.1}
\]

where `A` is connected and adjacent to `u`.  Put

\[
                         P=N_X(u),\qquad Q=N_X(A).              \tag{1.2}
\]

Suppose that for some `x in P cap Q`, the graph `G[X-x]` has a `K_4`
model `F_1,...,F_4` such that every `F_i` meets both `P` and `Q`.  Then
`G` contains a `K_7` minor.

#### Proof

Use the seven bags

\[
             \{u\},\quad A,\quad R\cup\{x\},
             \quad F_1,F_2,F_3,F_4.                            \tag{1.3}
\]

They are disjoint and connected.  The first two bags are adjacent by
hypothesis.  Since `x in P cap Q`, both are adjacent to `R union {x}`.
Every `F_i` meets `P`, so `{u}` is adjacent to it; every `F_i` meets
`Q`, so `A` is adjacent to it.  Fullness of `R` joins `R union {x}` to
every `F_i`.  The last four bags are pairwise adjacent by the given
model.  Thus (1.3) is a literal `K_7` model.  QED.

No palette/model alignment is used.

## 2. The antipodal boundary pattern

Let

\[
                     X=B\mathbin{\dot\cup}T,qquad
                     B=W_5,quad T=\{t_1,t_2,t_3\},             \tag{2.1}
\]

where `T` is independent and anticomplete to `B`.  Write `z` for the
hub of `W_5` and let its four rim vertices induce `C_4`.  This is exactly
the sparsest allowed boundary in the antipodal/antipodal exact-eight
polarity.

Set

\[
                 P=B\cup\{t_1\},
                 \qquad Q=B\cup\{t_2,t_3\}.                    \tag{2.2}
\]

Then

\[
        |P|=6,qquad |X-Q|=1,qquad P\cup Q=X,qquad P\cap Q=B. \tag{2.3}
\]

### Lemma 2.1 (`W_5` is vertex-minimal for a `K_4` minor)

The wheel `W_5` has a `K_4` minor, but `W_5-x` has no `K_4` minor for
every vertex `x`.

#### Proof

Contracting one rim edge turns the rim `C_4` into a triangle; with the
hub this gives `K_4`.

Deleting the hub leaves `C_4`, which has no `K_4` minor.  Deleting a rim
vertex leaves the cone over a three-vertex path.  If that cone had a
`K_4` model, deleting the branch bag containing the cone vertex would
leave a `K_3` model in the path, impossible; if the cone vertex were
unused, the path itself would contain `K_4`, also impossible.  QED.

### Corollary 2.2 (the numerical contact bounds do not force the packet)

For the boundary (2.1) and contacts (2.2), there is no reserve
`x in P cap Q` satisfying Lemma 1.1.

#### Proof

Every possible reserve lies in `B`.  But

\[
                         G[X-x]=(W_5-x)\mathbin{\dot\cup}3K_1
\]

has no `K_4` minor by Lemma 2.1.  QED.

Thus the failure is stronger than inability to make all four bags meet
both contact rows: after reserving a common contact, no boundary `K_4`
exists at all.

## 3. A seven-connected realization of the contact pattern

The preceding pattern is compatible with seven-connectivity.  Construct
`G_0` as follows.

* Keep the boundary `X` from (2.1).
* Let `A` be a seven-vertex clique and join every vertex of `A` to every
  vertex of `Q`.
* Add `u`, join it to every vertex of `A`, and join it to exactly the
  boundary vertices in `P`.
* Let `R` be another seven-vertex clique, join every vertex of `R` to
  every vertex of `X`, and put no edge from `R` to `A union {u}`.

Then `G_0-X` has exactly the two components

\[
                           C=\{u\}\cup A,qquad R,              \tag{3.1}
\]

both full to `X`, and (1.1)--(1.2) hold exactly.

### Lemma 3.1

The graph `G_0` is seven-connected.

#### Proof

Delete at most six vertices.  Each of the seven-cliques `A,R` retains a
vertex, and at least two vertices of `X` remain.  Since `|Q|=7`, at least
one vertex of `Q` remains; it joins the surviving parts of `A` and `R`.
The vertex `u`, if present, joins the surviving part of `A` because it
has seven neighbours there.

Every remaining boundary vertex is connected to the preceding component:
vertices of `B` see `u,A,R`; `t_1` sees `u,R`; and `t_2,t_3` see `A,R`.
Hence the deletion leaves a connected graph.  No cut of order at most
six exists.  QED.

This graph intentionally contains `K_7` subgraphs in `A` and `R`; it is
not a counterexample to Hadwiger and is not minor-critical.  Its purpose
is exact: even

\[
 \text{seven-connectivity}+|P|\ge6+|X-Q|\le1+
 \text{the actual antipodal exact-eight boundary}
\]

does not force the contact `K_4` required by Lemma 1.1.  A positive
singleton-web application must additionally use `K_7`-minor-freeness,
proper-minor novelty, or a stronger distributed-portal conclusion.
