# A seven-connected critical triangle with separated Kempe responses

**Status:** explicit computer-assisted barrier to an intermediate claim.
The deterministic standard-library verifier is
[`hc7_critical_triangle_kempe_separation_barrier_verify.py`](hc7_critical_triangle_kempe_separation_barrier_verify.py).
This graph is not a counterexample to `HC_7`: it has both an explicit
`K_7` minor and an actual order-seven separation, and it is not strongly
seven-contraction-critical.

## 1. Claim refuted

The following data do not by themselves force the two exact response
families at a critical triangle to lie in one Kempe component:

1. a seven-connected, seven-vertex-critical host;
2. two incident deleted edges `va,vb` whose outer ends are adjacent;
3. nonempty exact six-colouring responses of both orientations;
4. one spanning labelled `K_7`-minus-one-edge model which survives the
   simultaneous deletion of both edges; and
5. the literal placement of the three triangle vertices in that model.

The construction below has two Kempe components, one for each response
orientation.  It shows that a positive theorem must essentially use
strong contraction-criticality together with the exclusion of the
`K_7` and exact order-seven terminal outcomes.

## 2. The four-critical core

Let `Q` be the graph with graph6 string

```text
HCpvbqk
```

on vertices `0,...,8`, with edge set

\[
\begin{split}
\{&03,04,06,08,14,15,16,17,25,26,27,28,\\
  &35,36,37,47,48,58\}.
\end{split}                                                   \tag{2.1}
\]

The graph `Q` is four-connected and four-vertex-critical.  Put

\[
                         v=0,\qquad a=3,\qquad b=6.              \tag{2.2}
\]

These vertices induce a triangle.  Delete the two incident edges and
write

\[
                         H_0=Q-\{03,06\}.                        \tag{2.3}
\]

The graph `H_0` has exactly 24 labelled proper three-colourings.  Up to
permuting the colours, their four equality partitions are

\[
\begin{array}{ll}
 0123\mid45\mid678,&0123\mid456\mid78,\\
 0567\mid138\mid24,&0567\mid18\mid234.
\end{array}                                                   \tag{2.4}
\]

The first two partitions have \(c(0)=c(3)\ne c(6)\), while the last two
have \(c(0)=c(6)\ne c(3)\).  The Kempe-reconfiguration graph has exactly
two components, each of order 12, and each component contains only one
orientation.

In particular, the colourings in (2.4) also give exact contraction
responses for `03` and `06`: no other neighbour of either contracted pair
has their common colour.

## 3. The seven-connected lift and its labelled model

Add a triangle on new vertices `9,10,11` and join it completely to `Q`:

\[
                              \widehat G=K_3\vee Q.               \tag{3.1}
\]

The graph in (3.1) is seven-connected and seven-vertex-critical.  Put

\[
                         \widehat H=\widehat G-\{03,06\}.         \tag{3.2}
\]

The following seven sets partition \(V(\widehat H)\):

\[
 \{9\},\quad\{10\},\quad\{11\},\quad
 R=\{0,1,2,4,5,8\},\quad\{3\},\quad\{6\},\quad\{7\}.          \tag{3.3}
\]

They are connected and pairwise adjacent except for the pair
`{6},{7}`.  Thus (3.3) is a spanning labelled
`K_7`-minus-one-edge model.  The edge `03` is redundant for the
`R`--`{3}` adjacency because `35` remains, and `06` is redundant for the
`R`--`{6}` adjacency because `16` and `26` remain.  Hence both incident
edges are jointly deletion-persistent for this same model.  Their outer
ends are adjacent through `36`.

Every six-colouring of the graph in (3.2) gives the three join vertices three
singleton colours and restricts to a three-colouring of `H_0`.  Kempe
interchanges involving a join colour only permute a whole colour class
with a join singleton.  They cannot change the equality orientation on
`0,3,6`.  Therefore the two components from Section 2 remain
Kempe-separated after the join.

## 4. Both permitted terminal outcomes occur

The neighbourhood

\[
              N_{\widehat G}(0)=\{9,10,11,3,4,6,8\}              \tag{4.1}
\]

has order seven.  Its deletion isolates `0` from the nonempty opposite
side containing `1,2,5,7`.  Thus (4.1) is an actual order-seven
separator.

The following seven connected sets form an explicit `K_7`-minor model:

\[
       \{9\},\quad\{10\},\quad\{11\},\quad
       \{0\},\quad\{3\},\quad\{6\},\quad\{1,4,5\}.              \tag{4.2}
\]

Indeed `0,3,6` form a triangle, the set `{1,4,5}` is connected and is
adjacent to all three through `04,35,16`, and the join triangle is
complete to every core set.

## 5. Exact scope

The construction does not satisfy the full minimal-`HC_7` hypotheses.

- It contains the `K_7` minor (4.2).
- It has the exact order-seven separation (4.1).
- It is not strongly seven-contraction-critical, since its displayed
  `K_7` is a proper seven-chromatic minor.

It therefore does not refute the completion-or-separation programme.  It
does refute any attempt to force an orientation-changing Kempe sequence
from seven-connectivity, vertex-criticality, exact incident-edge
responses, and the common labelled near-clique model alone.

Run the certificate from the repository root with

```text
python3 barriers/hc7_critical_triangle_kempe_separation_barrier_verify.py
```

The expected output is

```text
core graph6 HCpvbqk: 4-connected and 4-vertex-critical
common deletion: 24 three-colourings in two pure Kempe components of order 12
joined host: 7-connected and 7-vertex-critical
spanning labelled K7-minus-edge model: verified
actual order-seven separator and explicit K7 model: verified
ALL CHECKS PASSED
```
