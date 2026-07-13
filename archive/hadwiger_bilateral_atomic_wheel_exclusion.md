# Bilateral fullness eliminates the sharp atomic wheel

## 1. A label-free packet completion

### Lemma 1.1 (two-tag covered-packet lift)

Let `F_1,...,F_4` be four disjoint connected pairwise adjacent bags.  Let
`a,b,p,q` be vertices outside them, and let `R` be a connected set
disjoint from all displayed objects.  Assume:

1. `ab` is an edge;
2. each of `a,b` is adjacent to every `F_i`;
3. every `F_i` is adjacent to at least one of `p,q`; and
4. `R` is collectively full to `\{a,b,p,q\}`.

Then the graph contains a `K_7` minor.

### Proof

Use

\[
             F_1,F_2,F_3,F_4,\qquad
             \{a\},\qquad\{b\},\qquad R\cup\{p,q\}. \tag{1.1}
\]

The last bag is connected because `R` has a neighbour at each of `p,q`.
It is adjacent to every `F_i` by item 3, and to the two singleton bags by
item 4.  Items 1--2 give all remaining adjacencies.  The seven bags are
disjoint and connected, proving the claim.  QED.

Only collective fullness is used; no single vertex of `R` is assumed
complete to the four boundary vertices.

## 2. Application to the atomic wheel

Use the wheel `K` from
`hadwiger_order8_atomic_web_curvature_counterarchitecture.md`, with rim
`v_0v_1v_2v_3v_0`, hub `h`, neutral tags `c_0,z,p,q`, and opposite
connected shore `R` full to the exact-eight gate.  The four bags

\[
             \{v_0\},\qquad \{v_3\},\qquad \{h\},
             \qquad \{v_1,v_2\}                     \tag{2.1}
\]

form a `K_4` model in the wheel.  Indeed `v_0v_3` and `v_1v_2` are rim
edges; the hub sees all three other bags; `v_0` sees the last bag through
`v_1`, and `v_3` sees it through `v_2`.

Both `c_0` and `z` contact every vertex of the wheel, and `c_0z` is an
old-boundary edge.  The pole `p` contacts `v_0,v_1,h`, while `q` contacts
`v_2,v_3,h`; hence `p,q` collectively contact every bag in (2.1).  Lemma
1.1, with

\[
                         a=c_0,\qquad b=z,
\]

gives the explicit model

\[
 \{c_0\},\{z\},\{v_0\},\{v_3\},\{h\},
 \{v_1,v_2\},R\cup\{p,q\}.                         \tag{2.2}
\]

### Theorem 2.1 (bilateral atomic-wheel exclusion)

The sharp strict-relative-eight wheel obstruction cannot occur as one
side of a bilateral full exact-eight adhesion in a `K_7`-minor-free
graph.

### Proof

Model (2.2) is a `K_7` minor.  QED.

## 3. Consequence for the four-colour rooted-partition route

The earlier wheel was the edge-maximal planar/web obstruction surviving
strict atomic surplus, portal order, and disk curvature.  Its old
`K_7`-minor-free proof depended on the opposite side not contacting both
gate poles.  The forced three-cut theorem supplies exactly the missing
bilateral full shore, and the two-pole half-rim distribution then becomes
the seventh bag of (2.2).

Thus a rooted-partition failure may still produce a web, but the sharp
wheel residue is now closed geometrically.  What remains to make this a
complete rooted-clique-or-separator theorem is the reduction from every
four-colour anchored linkage failure to either this covered packet or a
proper nested order-seven/eight adhesion.
