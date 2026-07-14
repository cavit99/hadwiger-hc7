# The compulsory Hall portal is a six-fan bridge interface

**Status:** proved and independently audited as a companion dependency of
the compulsory-portal composition theorem.

This note turns the sole packet-collapse outcome of the prescribed-portal
Hall theorem into a literal near-model interface.  It does not yet prove
that the two bridge ends are a fixed apex pair.

## 1. A bridge behind a connectivity-minus-one set

### Theorem 1.1 (saturated bridge fan)

Let `G` be seven-connected, let `W subseteq V(G)` have order six, and
suppose `zu` is a bridge of `G-W`.  Let `A,B` be the two components of

\[
                         (G-W)-zu,
\]

with `z in A` and `u in B`.  Then there are six pairwise internally
vertex-disjoint `z-u` paths in `G-zu`, each containing exactly one member
of `W`, and the six paths use the six different members of `W`.
Consequently `G` has the rooted minor

\[
                         K_2\vee G[W],                 \tag{1.1}
\]

where the two vertices of the `K_2` are rooted at `z,u` and every literal
vertex of `W` remains a singleton root.

#### Proof

Seven-connectivity gives seven internally vertex-disjoint `z-u` paths.
Every `z-u` path other than the one-edge path `zu` meets `W`, because
`zu` is a bridge of `G-W`.  The paths are internally disjoint and `W` has
only six vertices.  Thus the family contains `zu`, while each of the other
six paths meets exactly one vertex of `W`; those six vertices are distinct
and therefore exhaust `W`.

For `w in W`, the corresponding path consists of a `z-w` segment whose
internal vertices lie in `A` and a `w-u` segment whose internal vertices
lie in `B`.  Contract all internal edges of the six `A`-segments toward
`z`, and all internal edges of the six `B`-segments toward `u`.  Internal
disjointness makes these contractions compatible and leaves every member
of `W` distinct.  The resulting minor retains the edge `zu`, makes each of
`z,u` adjacent to every member of `W`, and retains all literal edges of
`G[W]`.  This is (1.1).  \(\square\)

### Corollary 1.2 (separator core)

If `G` has no `K_7` minor under the hypotheses of Theorem 1.1, then

\[
                         G[W]\not\succeq K_5.          \tag{1.2}
\]

In particular `G[W]` is four-colourable by `HC_5`.

#### Proof

A `K_5` model in `G[W]`, together with the two universal adjacent rooted
vertices in (1.1), is a `K_7` model.  The colouring conclusion is the
known case `HC_5`.  \(\square\)

## 2. Application to the compulsory Hall portal

Use the notation and hypotheses of
`../results/hc7_exact7_hall_descent_packet_classification.md`.  Thus

\[
 X=Y\mathbin{\dot\cup}\{z\}=N_L(U),\qquad
 |Y|=|U|-1,
\]

`C=L-X` is connected and full to

\[
 \Omega=(S-U)\cup Y\cup\{z\},
\]

and in the compulsory outcome `z` has the unique neighbour `u_* in U`.
Put

\[
 W=(S-U)\cup Y,\qquad
 A=C\cup\{z\},\qquad B=R\cup U.                       \tag{2.1}
\]

### Theorem 2.1 (twin exact-seven boundaries)

Assume the host `G` is seven-connected.  Then:

1. `|W|=6`, and `A,B` are the two connected components of
   `(G-W)-zu_*`;
2. `zu_*` is the unique `A-B` edge in `G-W`;
3. the two neighbourhoods are
   \[
      N_G(A)=W\cup\{u_*\},\qquad
      N_G(B)=W\cup\{z\};                              \tag{2.2}
   \]
4. both `A` and `B` are full to their displayed seven-boundaries; and
5. Theorem 1.1 gives six disjoint literal detours through `W` and a rooted
   `K_2\vee G[W]` minor.  In a `K_7`-minor-free host, `G[W]` is
   `K_5`-minor-free.

If `|U|>=2`, then

\[
                         |A|=|L|-|Y|<|L|.              \tag{2.3}
\]

#### Proof

The order calculation is

\[
 |W|=|S-U|+|Y|=(7-|U|)+(|U|-1)=6.
\]

The set `A` is connected because `C` is connected and, by fullness of
`C` to `Omega`, `z` has a neighbour in `C`.  There is no `C-U` edge since
`X=N_L(U)`, and there is no old `L-R` edge.  By the compulsory hypothesis,
the only edge from `z` to `U` is `zu_*`.  Hence `zu_*` is the only possible
`A-B` edge after deleting `W`.

Because `G` is seven-connected and `|W|=6`, the graph `G-W` is connected.
It follows that `B` is connected and that `zu_*` is indeed a bridge with
the two sides in (2.1).

Every member of `W` has a neighbour in `A`: `C` is full to `Omega`, which
contains `W`.  The only further neighbour of `A` is `u_*`, through the
displayed bridge.  This gives the first equality in (2.2) and fullness of
`A`.

The old full packet `P subseteq R` contacts every member of `S-U`.  Every
member of `Y=N_{L-\{z\}}(U)` has a neighbour in `U`.  Thus `B=R\cup U`
contacts every member of `W`, and it contacts `z` through `u_*`; no other
neighbour is possible.  This proves the second equality in (2.2) and
fullness of `B`.  Theorem 1.1 and Corollary 1.2 now apply.

Finally, `A=C\cup\{z\}=(L-X)\cup\{z\}=L-Y`.  If
`|U|>=2`, then `|Y|=|U|-1>=1`, proving (2.3).  \(\square\)

## 3. Exact remaining composition obligation

The theorem canonically roots the possible two-apex pair at `z,u_*` and
shows that its shared six-vertex core is `K_5`-minor-free.  This is not yet
the required fixed-pair conclusion

\[
                         G-\{z,u_*\}\not\succeq K_5.  \tag{3.1}
\]

A `K_5` model in `G-\{z,u_*\}` may use interiors from both bridge sides
and the six-set `W`; Corollary 1.2 only excludes a model lying in `W`.
The next lemma must either pull such a crossing `K_5` model onto `W`, use
it with the two saturated fans to make a literal `K_7`, or derive a legal
six-colour gluing across one of the twin seven-boundaries.  No such pullback
is asserted here.
