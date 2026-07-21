# Seven-fan closure of the atomic defect-rotation graph

**Status:** written proof; separate internal audit GREEN.

This note proves that the thirteen-vertex graph `G_*` from the
[`atomic defect-rotation barrier`](../barriers/hc7_atomic_shared_hub_defect_rotation_barrier.md)
cannot occur as a subgraph of a seven-connected `K_7`-minor-free graph.
Unlike the adjacent
[`same-vertex saturation theorem`](hc7_atomic_shared_hub_same_vertex_saturation.md),
the host here may have arbitrarily many additional vertices.

The proof uses the five explicit one-edge `K_7` models checked in that
adjacent result.  That result has a
[`GREEN separate internal audit`](hc7_atomic_shared_hub_same_vertex_saturation_audit.md);
the present fan theorem has the adjacent GREEN internal audit.

## 1. The graph and the finite certificates

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

on core vertices `a,b,c,d,e,f,g` and the additional vertex `x`.  Form
`G_*` as follows:

1. subdivide `ac,bd,ad,bc` once, using respectively
   `p_ac,p_bd,p_ad,p_bc`;
2. add `f-p_ac,f-p_bd,g-p_ad,g-p_bc`;
3. replace `fg` by `f-h-g`; and
4. add `eh,hx`.

Put

\[
 q=p_{ad},\qquad q'=p_{bc},\qquad
 U=\{b,c,p_{ac},p_{bd},p_{bc}\}.                         \tag{1.1}
\]

The same-vertex saturation theorem gives an explicit `K_7`-minor model in
`G_*+qu` for every `u in U`.  No inference from finite search is used here:
the five models are displayed branch by branch in that theorem and checked
by its deterministic verifier.

The permutation

\[
 \sigma=(a\ b)(c\ d)(p_{ac}\ p_{bd})(p_{ad}\ p_{bc})   \tag{1.2}
\]

fixing `e,f,g,h,x` is an automorphism of `G_*`.  Consequently the same five
certificates, transported by `sigma`, give a `K_7` minor in
`G_*+q'u` for every

\[
 u\in U'=\sigma(U)=\{a,d,p_{ac},p_{bd},p_{ad}\}.         \tag{1.3}
\]

## 2. The fan lemma with clean interiors

We record the exact standard form needed below.

### Lemma 2.1 (fan lemma)

Let `G` be `k`-connected, let `v` be a vertex, and let
`S subseteq V(G)-{v}` have at least `k` vertices.  Then there are `k` paths
from `v` to `k` distinct vertices of `S` which intersect pairwise only at
`v` and whose internal vertices avoid `S`.

#### Proof

Add a new vertex `z` adjacent to every vertex of `S`.  No set of fewer than
`k` vertices, excluding `v,z`, separates `v` from `z`: after deleting such
a set, `G` remains connected and at least one vertex of `S` remains to meet
`z`.  Menger's theorem therefore gives `k` internally vertex-disjoint
`v`--`z` paths.  Delete `z` from them and truncate each remaining path at
its first vertex in `S`.  Their endpoints are distinct, their interiors
avoid `S`, and they intersect pairwise only at `v`.  \(\square\)

## 3. Reusable saturated-fan endpoint forcing

The finite certificates enter the host only through the following general
mechanism.

### Lemma 3.1 (saturated-fan endpoint forcing)

Let `G` be `k`-connected and contain a retained subgraph `K`.  Let
`v in V(K)`, put `S=V(K)-{v}`, and suppose

\[
                         S=A\mathbin{\dot\cup}U,
                         \qquad |A|=k.                   \tag{3.1}
\]

Fix a target graph `L`.  Suppose `K+vu` contains an `L` minor for every
`u in U`.  Then either `G` contains an `L` minor, or there is a `k`-fan
from `v` to `S` whose endpoint set is exactly `A` and whose path interiors
avoid `V(K)`.  In particular, in the second outcome there is a
path from `v` to every vertex of `A` whose internal vertices avoid `V(K)`.

Here `K+vu` means that the edge `vu` is added if it is absent.  The paths
in the conclusion belong to one fan simultaneously; the last sentence
does not discard their pairwise disjointness.

#### Proof

Apply Lemma 2.1 to `v` and `S`.  Consider one of the resulting fan paths
`R` with endpoint `u in U`.  Its interior avoids `S`; because `v` is an
endpoint of the simple path, it therefore avoids all of
`V(K)=S union {v}`.  Contract every edge of `R` except its last edge at `u`.  No two
vertices of `K` are identified, and the resulting minor of `G` contains
`K+vu`.  It therefore contains an `L` minor.

If this happens for any fan endpoint, the first outcome holds.  Otherwise
all `k` distinct endpoints avoid `U`.  They lie in the `k`-element set `A`,
so the endpoint set is exactly `A`.  The clean-interior assertion comes
from Lemma 2.1.  \(\square\)

This lemma is useful whenever local terminal certificates saturate all but
exactly `k` possible endpoints of a retained core.  Connectivity then
forces clean paths to every unsaturated endpoint; it is not merely a degree
argument and does not require the ambient host to have the same vertex set
as `K`.

## 4. Seven-connectivity supplies two clean paths to `h`

### Lemma 4.1

Let `G` be seven-connected and contain `G_*` as a subgraph.  If `G` has no
`K_7` minor, then it contains paths `P` from `q` to `h` and `P'` from `q'`
to `h` such that

\[
 V(P)\cap V(G_*)=\{q,h\},\qquad
 V(P')\cap V(G_*)=\{q',h\}.                              \tag{4.1}
\]

#### Proof

Apply Lemma 3.1 with retained subgraph `K=G_*`, target `L=K_7`, `v=q`,
and

\[
 S=V(G_*)-\{q\}
  =\underbrace{\{a,d,g,e,f,h,x\}}_{A}
   \mathbin{\dot\cup}\underbrace{U}_{\text{forbidden}}. \tag{4.2}
\]

The five certificates from Section 1 verify the hypothesis for every
`u in U`.  Since `G` has no `K_7` minor, the second outcome of Lemma 3.1
holds.  Its fan path with endpoint `h` is `P` and has the first property in
(4.1).

Apply Lemma 3.1 again with `v=q'`, the transported certificates for `U'`,
and

\[
 V(G_*)-\{q'\}
  =\underbrace{\{b,c,g,e,f,h,x\}}_{A'}
   \mathbin{\dot\cup}\underbrace{U'}_{\text{forbidden}}.\tag{4.3}
\]

The fan path with endpoint `h` is `P'` and has the second property in
(4.1).  \(\square\)

## 5. First-intersection construction

### Theorem 5.1 (seven-fan closure)

Every seven-connected graph containing `G_*` as a subgraph contains a
`K_7` minor.

#### Proof

Suppose for a contradiction that a seven-connected graph `G` contains
`G_*` but has no `K_7` minor.  Choose `P,P'` from Lemma 4.1.  The path `P`
avoids `q'`, and `P'` avoids `q`.  Since both end at `h`, they intersect.

Traverse `P'` from `q'`, and let `y` be its first vertex on `P`.  Because
`q'` is not on `P`, the vertex `y` has a predecessor `z` on `P'`.  Put

\[
 H=V(P),\qquad
 B_0=V(P'[q',z]),\qquad
 B=B_0\cup\{b\}.                                        \tag{5.1}
\]

Thus `B_0` is the prefix of `P'` strictly before `y`.  It is
connected, contains `q'`, and is disjoint from `H` by the choice of `y`.
The edge `zy` joins `B_0` to `H`.  The edge `bq'` belongs to `G_*`, so `B`
is connected.  By (4.1), `B_0` meets `V(G_*)` only at `q'`, while `H` meets
`V(G_*)` only at `q,h`.  In particular, adding `b` to `B_0` creates no
intersection with `H` or with any branch set below.

Now take the seven branch sets

\[
\begin{array}{lll}
 E=\{e\},&F=\{f\},&A=\{a,g,p_{ac}\},\\
 H,&B,&D=\{d,p_{bd}\},\\
 C=\{c,x\}.&&
\end{array}                                               \tag{5.2}
\]

They are pairwise disjoint.  The preceding paragraph proves connectedness
of `H` and `B`; the remaining nontrivial branch sets are connected through
`ag,a-p_ac`, `d-p_bd`, and `cx`.

For completeness, the following list supplies one edge for every pair of
branch sets:

| first bag | contacts with later bags |
|---|---|
| `E` | `EF:ef`, `EA:ea`, `EH:eh`, `EB:eb`, `ED:ed`, `EC:ec` |
| `F` | `FA:fa`, `FH:fh`, `FB:fb`, `FD:fd`, `FC:fc` |
| `A` | `AH:a-q`, `AB:gb`, `AD:gd`, `AC:ax` |
| `H` | `HB:yz`, `HD:q-d`, `HC:hx` |
| `B` | `BD:b-p_bd`, `BC:bx` |
| `D` | `DC:dx` |

All listed edges except `yz` belong to `G_*`; the edge `yz` is the split
edge of `P'`.  Thus the seven disjoint connected sets in (5.2) are pairwise
adjacent and form an explicit `K_7`-minor model in `G`, the desired
contradiction.  \(\square\)

## 6. Scope and consequence

Theorem 5.1 is an unbounded host-level conclusion: unlike same-vertex
saturation, it permits arbitrary additional vertices and edges.  Its only
host hypothesis beyond containing the exact labelled subgraph `G_*` is
seven-connectivity.

The theorem does not assert that every dirty replacement path in an
arbitrary subdivision has this thirteen-vertex subgraph.  Its application
therefore requires preserving the four named subdivided routes, their
`f`- and `g`-anchor edges, the common vertex `h`, and the edges `eh,hx`
literally.  Subject to that ownership condition, the sparse shared-vertex
configuration is terminal by an explicit `K_7` minor rather than a valid
collision reduction.
