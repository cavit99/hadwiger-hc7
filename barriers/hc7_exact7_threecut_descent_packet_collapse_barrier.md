# Barrier: a strict three-cut descent can collapse `(1,2)` to `(1,1)`

**Status:** adversarial finite certificate with a dependency-free verifier.

This order-minimal architecture satisfies the literal hypotheses used by
the audited three-cut descent, together with several stronger
counterexample-like properties:

* exact seven-connectivity;
* every Dirac neighbourhood inequality
  `alpha(N(v)) <= d(v)-5`;
* chromatic number seven;
* an actual old seven-separation with packet vector `(1,2)`;
* a legally attained paired equality state; and
* an exact support-four three-cut lobe descent.

At the descended boundary, however, the new opposite shore has packet
number one.  The two old full packets cannot be completed disjointly, and
the natural paired state cannot be pulled back because every old
literal--gate pair is an edge.

This is not an `HC_7` counterexample: it contains the explicit `K_7` minor
displayed below and is not minor-minimal.  It therefore shows exactly that
packet preservation and state pullback do not follow from the audited local
data, even after adding chromaticity and Dirac.  A positive composition
theorem must spend `K_7`-minor-freeness or a genuinely universal
minor-critical transition.

The verifier is
[`hc7_exact7_threecut_descent_packet_collapse_barrier_verify.py`](hc7_exact7_threecut_descent_packet_collapse_barrier_verify.py).

## 1. The fourteen-vertex graph

Let

\[
 S=\{c,b_1,a_1,b_2,a_2,b_3,a_3\},\qquad
 B_i=\{b_i,a_i\}.
\]

The boundary edges are:

1. the two triangles on `a_1,a_2,a_3` and on `b_1,b_2,b_3`;
2. `ca_i` for all `i`, together with `cb_1`; and
3. `b_1a_2,b_2a_3,b_3a_1`.

No `a_i b_i` is an edge.  Hence

\[
                  \Pi=\{B_1,B_2,B_3,\{c\}\}             \tag{1.1}
\]

is a proper paired state: distinct paired blocks are adjacent and `c`
meets every block.

Put

\[
 T=\{z_1,z_2,z_3\},\qquad
 L=T\cup\{x,y\},\qquad R=\{p,q\}.
\]

Make `T` a triangle and join each of `x,y` to every member of `T`.  Add
the following boundary contacts:

\[
\begin{aligned}
 N_S(x)&=\{c,b_1,b_2,b_3\},\\
 N_S(y)&=\{c,a_1,a_2,a_3\},\\
 N_S(z_j)&=\{b_1,b_2,b_3,a_j\}\quad(1\le j\le3).
\end{aligned}                                             \tag{1.2}
\]

Finally, `p,q` are adjacent and each is complete to `S`.  There are no
`L-R` edges.

The old separation is therefore `(L,S,R)`.  The graph `G[L]=K_5-xy` is
three-connected, and `T` is its three-cut with singleton lobes `x,y`.
Both lobes have support exactly four.  The boundary graph contains the
spanning non-path tree

```text
c-a1, c-a2, c-a3, a2-b1, a3-b2, a1-b3.
```

Thus the support-four branch of the audited three-cut theorem applies
literally.

## 2. Old packet vector and attained state

Exhaustive connected-subset enumeration gives

\[
                         (\nu_L,\nu_R)=(1,2).             \tag{2.1}
\]

The two rich packets are the adjacent singleton sets `{p}` and `{q}`.
Although `L` has several full connected subsets, every two intersect.

The old state (1.1) is legally attained.  Contract the connected full set

\[
                         \{y,z_2\}\cup B_1               \tag{2.2}
\]

to a vertex `tau`.  The resulting proper minor has the six-colouring

\[
\begin{array}{c|c}
\text{vertices}&\text{colour}\\ \hline
\tau&1\\
b_2,a_2&2\\
b_3,a_3&3\\
c,z_3&4\\
q,x&5\\
p,z_1&6.
\end{array}                                               \tag{2.3}
\]

Expanding `B_1` on the boundary gives exactly (1.1).  Thus the paired
state is not merely an abstract proper partition.

## 3. The strict descent and packet collapse

For the lobe `D={x}`,

\[
 N_L(D)=T,qquad N_S(D)=\{c,b_1,b_2,b_3\}.
\]

Consequently

\[
          \Omega=T\cup\{c,b_1,b_2,b_3\}=N_G(x)           \tag{3.1}
\]

is an exact order-seven boundary.  The new opposite open shore is

\[
                   O=\{y,a_1,a_2,a_3,p,q\}.              \tag{3.2}
\]

Both `{x}` and `O` are connected and literally `Omega`-full.  Nevertheless
the exhaustive packet calculation gives

\[
                         (\nu_{\{x\}},\nu_O)=(1,1).       \tag{3.3}
\]

The obstruction to naively preserving the old rich packets is transparent.
The old packets `{p},{q}` meet none of the new gate vertices `z_j`.  A
packet using `y` sees all three gates, while a packet avoiding `y` must use
all three vertices `a_1,a_2,a_3`.  The former still needs an `a_i` to join
`y` to either `p` or `q`, so the two completions cannot be vertex-disjoint.
The exhaustive verifier checks this without relying on that description.

The natural paired pullback is also impossible.  To replace the lost old
partners `a_i`, one would need independent blocks

\[
                         \{b_i,z_{\sigma(i)}\}.
\]

But (1.2) gives

\[
                         b_i z_j\in E(G)
                 \quad\text{for all }i,j.                \tag{3.4}
\]

Thus the compatibility graph is empty; no permutation supplies even one
of the proposed independent blocks.

## 4. Counterexample-like checks and exact trust boundary

The verifier exhausts all deletions of at most six vertices and confirms
that `G` is seven-connected; deleting `S` disconnects it, so connectivity
is exactly seven.  It also checks every local Dirac inequality and proves
by exact colouring search that `chi(G)=7`.

The graph deliberately violates the target-minor hypothesis.  The seven
branch sets

\[
 \{x,z_1\},\ \{y,z_2\},\ \{b_1\},\
 \{b_3,a_2,q\},\ \{a_3,a_1,p\},\ \{z_3\},\ \{b_2\}
                                                               \tag{4.1}
\]

are connected, disjoint and pairwise adjacent, and hence form a literal
`K_7` model.  The verifier also finds that deleting `a_1` leaves a graph
which is not six-colourable, so the host is not seven-vertex-critical.

Accordingly this barrier does not refute a theorem whose conclusion also
allows a target minor, nor a theorem using the full response of every
proper minor.  It refutes the naive intermediate assertions

```text
strict descent preserves (1,2),
old full packets can always absorb the replaced labels/gates disjointly,
the paired state pulls back from fullness and exact attainment alone.
```

## 5. Order minimality

Fourteen vertices are unavoidable for a literal architecture of this
three-cut type.  The old boundary uses seven vertices.  A three-cut with
two nonempty lobes uses at least `3+1+1=5` shore vertices.  Two disjoint
nonempty opposite packets use at least two more vertices.  Hence

\[
                            |G|\ge7+5+2=14,
\]

and the displayed construction attains equality.
