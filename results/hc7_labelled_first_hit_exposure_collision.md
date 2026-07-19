# A labelled first-hit rank defect gives a tight separator or a repeated literal exposure

**Status:** written proof; separate internal audit GREEN in
[`hc7_labelled_first_hit_exposure_collision_audit.md`](hc7_labelled_first_hit_exposure_collision_audit.md).
This is a parameter-small
consequence of the Rado--gammoid reduction in
[`hc7_labelled_first_hit_rado_reduction.md`](hc7_labelled_first_hit_rado_reduction.md).
It isolates the only host-level obstruction left by the first-hit rank when
there are five labels and at most three fixed response vertices.  It does
not perform the required response-preserving exchange and does not prove
`HC_7`.

## 1. Setting

Use the clean labelled-linkage setting of the cited Rado reduction.  Thus
`H` is a finite graph, `P` is a source set, and

\[
                       T_1,\ldots,T_5
\]

are nonempty pairwise disjoint terminal classes, disjoint from `P`.  Let
`F` be a further fixed literal set, disjoint from `P` and the terminal
union, with

\[
                              |F|\le3.                  \tag{1.1}
\]

The directed first-hit network uses `H-(T union F)` as its nonterminal
part and a sink copy for every terminal vertex.  A clean labelled linkage
consists of five vertex-disjoint paths from distinct sources, one to each
terminal class, meeting the terminal union only at their ends.

## 2. Exact collision alternative

### Theorem 2.1

Suppose `H` is seven-connected and there is no clean labelled linkage.
Then there are a nonempty label set `I subseteq [5]`, a Rado--Menger set
`Z` with

\[
                              |Z|\le |I|-1,             \tag{2.1}
\]

and a surviving-source component `C` for which one of the following holds.

1. The full neighbourhood `N_H(C)` has order seven and is the boundary of
   an actual separation with two nonempty open sides.
2. Some unselected terminal class has two distinct literal exposed
   vertices:

   \[
       \text{there is }j\notin I\text{ such that }
       |N_H(C)\cap T_j|\ge2.                            \tag{2.2}
   \]

In outcome 2, each vertex counted in (2.2) is a genuine first hit: it can
be joined to a surviving source by a path whose other vertices avoid
`T union F`.  The two resulting paths need not be disjoint from each other.

#### Proof

Apply the Rado--gammoid alternative and directed Menger theorem to obtain
`I,Z,C`.  Map the ordinary members and selected terminal-sink members of
`Z` back to their literal host vertices, obtaining `bar Z`.  The exact
host exposure formula is

\[
 N_H(C)\subseteq
 \overline Z\ \cup\ (N_H(C)\cap F)\ \cup
 \bigcup_{j\notin I}(N_H(C)\cap T_j).                  \tag{2.3}
\]

The set on the right separates `C` from at least one selected terminal
not represented in `Z`.

If (2.2) is false for every `j notin I`, then (1.1), (2.1), and the five
labels give

\[
\begin{aligned}
 |N_H(C)|
 &\le |Z|+|N_H(C)\cap F|
       +\sum_{j\notin I}|N_H(C)\cap T_j|\\
 &\le (|I|-1)+3+(5-|I|)=7.                             \tag{2.4}
\end{aligned}
\]

Seven-connectivity forces equality throughout (2.4).  Hence the
right-hand side of (2.3) is exactly `N_H(C)`, has order seven, and separates
two nonempty sets.  This is outcome 1.

It remains to justify the final first-hit assertion.  Choose a source
`p` in the component `C`; such a source exists by construction.  For any
`t in N_H(C) cap T_j`, join `p` inside `C` to a neighbour of `t`, and add
the final edge to `t`.  The component `C` lies in `H-(T union F)` and the
last vertex is the first terminal met.  \(\square\)

### Corollary 2.2 (the exact residual at an extremal response kernel)

Suppose the source and terminal system is obtained from a legal
response-preserving kernel chosen first to maximize the number of distinct
first-hit labels and then to minimize its order.  Then failure of the clean
five-label linkage leaves exactly two structural obligations:

1. a bare actual order-seven separation returned by Theorem 2.1; or
2. two distinct literal exposed vertices in one unselected named branch
   set.

In the second outcome, a local exchange which increases the
response-preserving first-hit rank or gives a smaller legal kernel
contradicts the extremal choice; an explicit `K_7` model is terminal.
This does **not** make the first outcome terminal.  The selected-response
preservation theorem must still show that the bare order-seven separation
carries a partition extendable through both closed shores.  The same
state-preservation obligation remains if a collision exchange returns a
new separator.

Thus this corollary separates the two missing inputs: a repeated-exposure
exchange and compatible colouring on the exact boundary.  It proves
neither one.

## 3. Dynamic consequence inside a spanning labelled model

The repeated exposure has one automatic contraction-critical consequence
when the terminal classes are literal branch sets of the fixed model.

### Proposition 3.1 (a repeated exposure gives a model-preserving critical edge)

Assume, in addition, that `G` is not six-colourable, every proper minor of
`G` is six-colourable, and the vertices of `G` are partitioned into the
branch sets of a spanning labelled `K_7`-minus-one-edge model.  Suppose
`C` is contained in one branch set `D`, while the repeated terminal class
`T_j` in (2.2) is a different branch set `U_j`.

Choose distinct vertices `t_1,t_2 in N_G(C) cap U_j` and edges

\[
             e=c_1t_1,\qquad e'=c_2t_2,qquad c_1,c_2\in C.     \tag{3.1}
\]

Then deleting `e` preserves the same spanning labelled near-complete
model, and

\[
                         \chi(G-e)=\chi(G/e)=6.          \tag{3.2}
\]

In every six-colouring of `G-e`, the ends of `e` have one common colour
`alpha`; for each of the other five colours `beta`, they lie in one
`alpha`--`beta` component of `G-e`.

If the edge lies in one open shore of a previously fixed separation and
`sigma` is the labelled boundary trace of a fixed proper six-colouring of
the opposite closed shore, then exactly one of the following holds.

1. Every six-colouring of `G-e` rejects `sigma`.
2. Some six-colouring of `G-e` attains `sigma`; in this event `e` belongs
   to every induced non-list-colourable obstruction for that fixed trace.

#### Proof

The edges in (3.1) are distinct because their `U_j`-ends are distinct.
After deleting `e`, the edge `e'` retains the old `D`--`U_j` model
adjacency, so the same labelled near-complete model survives.

Minor-minimality makes both proper minors six-colourable.  They cannot be
five-colourable: a five-colouring of `G-e` can be extended over `e` with a
fresh sixth colour on one end, while a five-colouring of `G/e` expands in
the same way.  This proves (3.2).

The ends of `e` have the same colour in every six-colouring of `G-e`, or
else the deleted edge can be restored.  If their `alpha`--`beta`
components were different for some other colour `beta`, interchanging
those colours on one component would separate the endpoint colours and
again restore `e`.  This proves the five Kempe connections.

The final dichotomy is the fixed-trace alignment theorem applied to `e`:
attainment and total rejection are complementary, and attainment puts `e`
in every induced fixed-trace list-critical obstruction.  \(\square\)

The proposition is the strongest automatic dynamic conclusion of a
repeated exposure.  It preserves the old model, but it does not say that
the regenerated response attains the previously selected trace.  In the
rejection outcome, the existing total-rejection theorem produces its own
list-critical alternatives, whose strict transfer can still lose the five
labels.  Thus Proposition 3.1 identifies the exact state-preservation
obligation rather than closing it.

## 4. Trust boundary

The theorem proves more than an unlabelled separator alternative: failure
is localized to two literal vertices of one named terminal class.  It does
not show that the two source-to-terminal paths are mutually disjoint, that
the named terminal class can be split while preserving its old branch-set
contacts, or that the equality partition carried by the proper-minor
response extends through both shores.

The barrier
[`../barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier.md`](../barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier.md)
shows that seven-connectivity and `K_7`-minor exclusion do not remove the
repeated-exposure outcome.  The local exchange must therefore use the
operation-specific colouring response or an equivalent contraction-critical
transition.
