# Four-connectivity does not force a robust q2--q2 carrier split

## Verdict

The proposed local implication

\[
  4\text{-connected connector}
  \quad\Longrightarrow\quad
  \text{one of the four robust rooted carrier patterns}
\]

is false.  The smallest counterexample with six distinct singleton
terminals has nine vertices and is planar.  More importantly for the
actual no-`K_7^-` rotation cell, allowing a shared deficiency label makes
the obstruction stronger, not weaker: the one-shared-label cell already
fails in the eight-vertex square antiprism.

Thus connector connectivity cannot discharge the q2--q2 step.  The exact
positive replacement must retain the rural rotation/order of the portals
and compose it with the neighbouring rotation state, or use a proper-minor
equality state.  This is a barrier to a *local* carrier theorem, not a
counterexample to the global rotation-web composition target or to `HC_7`.

## 1. Six distinct terminals: the nine-vertex double-face book

Let `Z` be the graph with graph6 string

```text
HCZTfP}
```

and edge set

```text
03 05 06 07
14 15 17 18
24 26 27 28
35 36 38
47 48
58 68
```

(the numerical graph6 labels are used without relabelling).  Put

\[
 (\alpha,\beta,a_1,a_2,b_1,b_2)=(0,7,1,2,5,6).
\]

The graph is planar and exactly four-connected.  It has a plane embedding
with two quadrilateral faces

\[
 Q_1=(b_1,\alpha,\beta,a_1)=(5,0,7,1),
 \qquad
 Q_2=(\beta,\alpha,b_2,a_2)=(7,0,6,2),                 \tag{1.1}
\]

sharing the root edge `alpha beta`.

In a closed disc, two paths whose endpoints alternate on the boundary are
not vertex-disjoint.  Removing the open face from the sphere puts the
whole embedded graph in such a disc.  Hence `Q_1` forbids disjoint
`alpha-a_1` and `beta-b_1` paths, while `Q_2` forbids disjoint
`alpha-a_2` and `beta-b_2` paths.

Every pair of disjoint connected carriers containing specified terminal
sets contains the corresponding two terminal paths.  It follows at once
that all four patterns are absent:

\[
\begin{array}{ll}
 \{\alpha,a_1,a_2\}\mid\{\beta,b_1\},&
 \{\alpha,a_1,a_2\}\mid\{\beta,b_2\},\\
 \{\alpha,a_1\}\mid\{\beta,b_1,b_2\},&
 \{\alpha,a_2\}\mid\{\beta,b_1,b_2\}.
\end{array}                                             \tag{1.2}
\]

Indeed the first and third contain the crossing prescribed by `Q_1`, and
the second and fourth contain the crossing prescribed by `Q_2`.

The connectivity is not being lost at a hidden small cut.  Exhaustive
deletion of every set of at most three vertices leaves `Z` connected,
whereas deleting

\[
                  N_Z(0)=\{3,5,6,7\}
\]

isolates `0`.  Thus `kappa(Z)=4`.

An exhaustive `nauty-geng` search over every graph of minimum degree at
least four on orders six, seven, and eight, followed by an exact
four-connectivity filter and exact connected-subset carrier test, found no
counterexample.  Therefore order nine is minimal for the six-distinct-
terminal version.

The full order-nine classification is sharper.  Of the `15,471` generated
graphs, `14,480` pass the exact four-connectivity test.  Exactly one of
those graphs has a robust terminal tuple: the graph above.  It is planar,
and its two terminal tuples modulo swaps within each demand pair (the two
orientations of the roles) both have the crossed double-face book (1.1).
Thus through order nine there is no nonplanar robust example and no robust
tuple lacking the double-book order.  This is finite evidence for a rural-
order alternative, not a proof of that alternative at arbitrary order.

## 2. The exact one-shared-label cell

Let `A` be the square-antiprism graph with graph6 string

```text
GQyurg
```

and put

\[
 (\alpha,\beta,c,a,b)=(0,5,1,3,6),
 \qquad D=\{c,a\},\quad E=\{c,b\}.                     \tag{2.1}
\]

Use singleton portal sets.  The graph is planar and four-connected, and
it has the quadrilateral face

\[
                         (b,\alpha,\beta,a)=(6,0,5,3). \tag{2.2}
\]

Two of the four robust patterns ask two disjoint carriers both to contain
the singleton `c`, and are therefore impossible.  The other two ask for
disjoint `alpha-a` and `beta-b` paths, and are impossible by the alternating
facial order (2.2).  This is the portal-set variant actually left by the
audited overlap theorem when `|D cap E|=1`.

If `D=E={c_1,c_2}` and both portal sets are singletons, every one of the
four patterns is tautologically impossible because one demanded portal is
required on both sides.  This happens even in the four-connected graph
`K_5`.  Consequently no theorem stated only in terms of connector
connectivity and nonempty portal sets can close either overlap cell.

## 3. Exact surviving structural output

The counterexamples expose the reusable invariant rather than merely a
small exception.  The obstruction is a **crossed-frame rural order**:
one alternating quadrilateral face blocks two opposite robust patterns;
two faces forming a book around the root edge block all four with distinct
labels.  Sharing a label replaces one of the two facial crossings by a
literal shared-portal collision.

Accordingly, a sound proof-spine lemma must have an alternative of the
following form:

> either the two rooted demand carriers split, or the relevant connector
> society is rural with the precise crossed portal order; these rural
> orders must then compose across consecutive deficiency rotations into a
> common two-apex structure or collide with a proper-minor equality state.

Suppressing the order information and retaining only four-connectivity is
provably insufficient.

## Verification

Run

```bash
PYTHONPATH=active/runtime/deps python3 barriers/hc7_near_k7_robust_carrier_4connected_barrier_verify.py
```

To repeat the exhaustive minimal-order checks as well (requires
`nauty-geng` on `PATH`), run

```bash
PYTHONPATH=active/runtime/deps python3 barriers/hc7_near_k7_robust_carrier_4connected_barrier_verify.py --minimality
```

The reusable graph6 stream search is
`../active/hc7_robust_carrier_geng_search.py`.

The full order-nine rural-book classification was run as

```bash
geng -q -d4 9 | PYTHONPATH=active/runtime/deps \
  python3 active/hc7_robust_carrier_geng_search.py \
  --classify-all --progress 0
```

and returned

```text
examined=15471
four_connected_examined=14480
counterexample_graphs=1
planar_counterexample_graphs=1
nonplanar_counterexample_graphs=0
robust_terminal_tuples_mod_pair_swaps=2
nonbook_terminal_tuples=0
```
