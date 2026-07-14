# Atomic four-vertex packet-path classification

**Status:** proved and independently audited finite classification.  This is
also a static barrier: it is not an `HC_7` counterexample and does not close
the unbounded atomic cell.

The certificate is
`hc7_atomic_four_vertex_packet_path_classification.py`.

## 1. Atomic boundary and trace

Let

\[
S=\{0,1,2,3,4,5,6\}
\]

induce the paired width-two tree

\[
02,23,31,04,45,06.
\]

Its bipartition is

\[
I=\{0,3,5\},\qquad J=\{1,2,4,6\}.
\]

Take the compulsory literal to be `u=0`.  Split the independent block `J`
as

\[
B=\{1,2\},\qquad C=\{4,6\}.
\]

The thin shore is the singleton `a`, complete to `S`.  Thus it is connected
and `S`-full, and `a0` is the unique thin-shore portal edge to `u`.

The rich shore is the path

\[
                       p_0-p_c-q_b-q_0,
\]

with preselected adjacent packets

\[
P=\{p_c,p_0\},\qquad Q=\{q_b,q_0\}.
\]

Use the boundary contacts

\[
\begin{aligned}
N_S(p_c)&=\{1\},&N_S(p_0)&=S-\{1\},\\
N_S(q_b)&=\{4\},&N_S(q_0)&=S-\{4\}.
\end{aligned}
\]

Both `P,Q` are connected and `S`-full.  Exhausting every connected subset
of the rich shore gives five full packets but packing number exactly two.

There is a proper trace colouring

\[
 I:0,\qquad B:1,\qquad C:2,
 \qquad p_c:2,\quad q_b:1,\quad p_0:3,\quad q_0:4.
\]

The only bichromatic `B-C` path is

\[
                         1-p_c-q_b-4.                 \tag{1.1}
\]

It necessarily meets both preselected packets.  Neither packet alone
contains a blocking path in these two colours.  The equality state
`I|B|C` has packet demand three, so the two-packet reflection theorem does
not reflect this particular trace.

## 2. Exact static outcome

The graph has twelve vertices and thirty edges.  Exact spanning-partition
minor searches certify

\[
G\not\succeq K_7,qquad
G\not\succeq K_7^\vee,qquad
G-\{a,0\}\not\succeq K_5.                            \tag{2.1}
\]

Thus (1.1) does not itself escape either packet or create the labelled near
model.  The canonical pair `{a,0}` nevertheless already gives the allowed
fixed-pair terminal outcome.

This graph is deliberately not a counterexample-derived graph.  It is
four-colourable, has connectivity three, and fails Dirac's neighbourhood
inequality at every vertex.  In particular it does not encode the universal
proper-minor response or the atomic bridge Kempe locks.

## 3. Complete trace-legal extension language

Freeze the twelve vertices, the boundary tree, the separation, the displayed
trace colouring, and the three packet-path edges.  There are exactly thirteen
remaining trace-legal edges which preserve this interface:

\[
\begin{array}{ll}
p_c0,p_c2,p_c3,p_c5,&q_b0,q_b3,q_b5,q_b6,\\
p_01,q_04,&p_0q_b,p_cq_0,p_0q_0.
\end{array}                                             \tag{3.1}
\]

The first eight are every additional boundary contact allowed at the two
blocking-colour centres.  The next two complete a leaf to the boundary.
The last three are all missing trace-proper cross-packet edges.  There are
therefore `2^13=8,192` extensions.

### Theorem 3.1 (finite first-hit classification)

Every extension from (3.1) with rich packet number two satisfies at least
one of:

1. it contains a `K_7^vee` minor; or
2. deleting the canonical pair `{a,0}` leaves a `K_5`-minor-free graph.

#### Exact certificate

Each of the following nine singleton additions already creates a spanning
`K_7^vee` model:

\[
\begin{gathered}
p_c0,p_c2,p_c3,p_c5,
q_b0,q_b3,q_b5,q_b6,
p_0q_0.                                                \tag{3.2}
\end{gathered}
\]

Minor containment is monotone, so every extension containing one of (3.2)
has outcome 1.  Avoiding (3.2) leaves only the four optional edges

\[
                         p_01,q_04,p_0q_b,p_cq_0.
\]

The verifier checks all sixteen subsets and finds no `K_5` minor after
deleting `{a,0}`.  Hence each has outcome 2.

The minor checker is exact: in a connected graph every clique-minor model
can be extended to a spanning model, and the verifier exhausts all
restricted-growth spanning partitions, checking bag connectivity and every
required bag adjacency.  For `K_7^vee`, it checks all choices of the
deficient hub, requires the other six bags to form a clique, and permits at
most two missing hub spokes.

## 4. Consequence for the proof spine

The geometry-only implication

\[
\text{blocking path through both packets}
\Longrightarrow
\text{packet-disjoint escape}
\]

is false even in the smallest literal atomic shell.  However this shell
does **not** refute the correct terminal disjunction.  In the complete
four-vertex rich-shore extension language, every attempt to destroy the
canonical fixed pair immediately produces a labelled near model.

Therefore the live obstruction must use at least one feature absent here:

1. a larger packet with several competing first-hit vertices;
2. a nontrivial width-two bridge/web inside a packet; or
3. the strongly contraction-critical state transition itself.

Further static searches should not revisit four-vertex packet paths.  The
next constructive lemma should classify the first nontrivial packet block:
after suppressing degree-two trace vertices, either it reduces to this
atomic path and Theorem 3.1 applies, or it contains a genuine branch where
two proper-minor colour responses can choose different first hits.

## 5. Reproduction

```text
PYTHONPATH=active/runtime/deps python3 \
  results/hc7_atomic_four_vertex_packet_path_classification.py
```

The script verifies the literal trace and packet assertions, the unique
blocking path, the three exact minor exclusions in (2.1), all 8,192 legal
extensions, and the nine singleton near-model triggers.
