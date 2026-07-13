# A Two-Paths dichotomy for the sharp `C5` contact core

## 1. Setting

Let `S={0,1,2,3,4,r_1,r_2}` and suppose

\[
 G[S]=C_5\vee K_2,
\]

where the cycle is `0 1 2 3 4 0`.  Let `D,E` be disjoint, anticomplete,
connected subgraphs of `G-S`, each adjacent to every vertex of `S`.
For `i in {0,...,4}` write

\[
 P_i=N_D(i).
\]

Every `P_i` is nonempty.  The next lemma gives an exact linkage target
inside one shore.

## 2. The portal two-linkage closes the core

### Lemma 2.1

If `D` contains two vertex-disjoint paths, one with an end in `P_4` and
the other end in `P_1`, and the second with an end in `P_2` and the other
end in `P_0`, then `G` contains a `K_7` minor.

The paths are allowed to have length zero when the two relevant portal
sets intersect.

### Proof

Let the paths be `Q_41` and `Q_20`.  Enlarge them, if necessary, to
disjoint connected sets `X,Y subseteq D` that are adjacent to one another.
Indeed, if they are not already adjacent, take a shortest path in the
connected graph `D` joining them.  Its internal vertices avoid both sets;
split this connector at any edge and assign its two parts to `X` and `Y`.
This preserves disjointness and all four portal contacts and creates an
edge between the enlarged sets.

Now use the seven branch sets

\[
 \{0\},\quad \{1\},\quad \{r_1\},\quad \{r_2\},
 \quad X\cup\{4\},\quad Y\cup\{2\},\quad E.          \tag{2.1}
\]

The two enlarged shore bags are connected because `X` meets `P_4` and
`Y` meets `P_2`.  They are adjacent by construction.  The first sees
`{0}` through the cycle edge `40` and sees `{1}` through its `P_1`
contact.  The second sees `{1}` through `21` and sees `{0}` through its
`P_0` contact.  Both see `{r_1},{r_2}` through their boundary anchors,
and those four singleton bags form a clique.  Finally the full shore `E`
sees every boundary-containing bag, including the two enlarged shore
bags through their anchors.  Thus (2.1) is a `K_7` model. \(\square\)

By cyclic symmetry, for every cycle edge `i(i+1)` there is an analogous
crossing pair of portal paths.  It is enough that one of the five
corresponding two-linkages exist in either full shore.

## 3. Exact web alternative

Construct an auxiliary graph `A_D` from `G[D]` by adding five new terminal
vertices `t_0,...,t_4`, where `t_i` is adjacent precisely to `P_i`.
There are no edges among the terminals.  The graph is connected because
`D` is connected and every portal set is nonempty.

Use the ordered terminal tuple

\[
 T=(t_0,t_1,t_2,t_3,t_4),                           \tag{3.1}
\]

in the cyclic order of the boundary cycle in `G[S]`.  Its five possible
crossings are exactly the five rotated linkages from Lemma 2.1.  For
example, on the four terminals `t_0,t_1,t_2,t_4`, the crossing joins
`t_0` to `t_2` and `t_1` to `t_4`, which is the linkage used in Section 2
with the two paths interchanged.

### Corollary 3.1 (linkage or web)

Either `G` has a `K_7` minor, or `A_D` embeds in a `5`-web whose frame is
the ordered tuple (3.1).  The same conclusion holds for the other shore.

### Proof

If the frame is crossed, one of its five four-terminal crossings occurs,
and the corresponding rotation of Lemma 2.1 applies.  If it is crossless,
the generalized Two Paths Theorem says that the graph is a subgraph of a
web with that frame. \(\square\)

Here the invoked theorem is the standard Two Paths Theorem in its
generalized tuple form: a graph with a prescribed crossless tuple embeds
in a web with that tuple as frame.  The web consists of a planar
near-triangulation (the rib) with arbitrary cliques inserted into facial
triangles.

## 4. What seven-connectivity adds inside a web

In the counterexample-derived sharp core, `|S|=7`, `G-S` has exactly the
two components `D,E`, and `G` is seven-connected.  Consequently, for every
nonempty proper `X subsetneq D`,

\[
 |N_D(X)-X|+|N_S(X)|\ge7.                            \tag{4.1}
\]

Thus any separation of the web rib that exposes at most three internal
vertices forces at least four distinct boundary contacts on the separated
side.  This is the exact leverage absent from a generic Two Paths
instance.

The remaining web-exclusion lemma can now be stated without reference to
colourings or arbitrary rooted `K_5` models:

> **Sharp web-exclusion target.**  A connected shore `D` satisfying
> (4.1), full attachment to `S`, and all five rotated crossless portal
> linkages cannot occur simultaneously with an anticomplete connected full
> shore `E` in a `K_7`-minor-free graph.

This target is strictly narrower than generic two-linkedness.  It fixes
the seven-vertex boundary, supplies a second full shore, imposes every
relative order-seven cut inequality, and packages all five linkage
failures into one common `5`-web.  In the counterexample-derived cell the
shore is moreover 2-connected, every 2-cut is contact-locked, and every
actual vertex, internal-edge, and portal-edge deletion has the exact
rainbow/private-block transition recorded in
`hadwiger_c5_full_shore_transition.md`.  A proof should combine those
transition constraints with the web's facial-triangle separators: (4.1)
forces every side behind such a separator to have at least four distinct
boundary contacts, while transition criticality prevents a facial clique
from being an irrelevant replaceable module.
