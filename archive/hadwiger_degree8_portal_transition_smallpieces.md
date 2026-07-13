# Transition synchronization for the smallest portal pieces

## 1. Result

This note attacks the exact one-step transition condition from
`hadwiger_portal_exact_boundary_transfer.md` in the explicit static
obstruction from `hadwiger_degree8_portal_static_falsification.md`.

### Theorem 1

Let \(X=N\cup\{z\}\), where \(N=\{0,\ldots,7\}\), and put

\[
E(G[N])=\{01,07,17,24,45,35,36,26\},\qquad N_X(z)=\{2\}. \tag{1.1}
\]

Thus \(G[N]\cong K_3\dot\cup C_5\) and \(\alpha(G[N])=3\).
Let \(R_1,R_2,D\) be three connected \(X\)-boundaried pieces satisfying

\[
\begin{aligned}
N_X(R_1)=N_X(R_2)&=X-\{0,1\},\\
N_X(D)&=N-\{0\}.
\end{aligned}                                           \tag{1.2}
\]

In particular, the branch pieces see \(z\), while \(D\) does not.
Suppose every piece has at most two interior vertices. Then the following
conditions cannot hold simultaneously:

1. there is no common exact \(X\)-state with at most six blocks and at
   most five blocks meeting \(N\); and
2. for every deletion of an interior vertex, and every label-preserving
   deletion or contraction of an internal edge or boundary--interior edge
   in piece \(i\), the operated piece admits a state excluded by the
   original piece and admitted by both other pieces.

Thus the static obstruction (1.1)--(1.2) cannot satisfy the transition
condition forced in a minor-minimal counterexample when all three pieces
have order at most two.

### Corollary 2

Any transition-satisfying counterarchitecture in this exact-defect cell
has at least three interior vertices in one of its pieces.

The conclusion is independent of clique-minor assumptions: the transition
and coloring constraints already give the contradiction.

## 2. Exact finite state space

An exact state is a partition \(\Pi\) of \(X\) into at most six independent
blocks with \(\beta_N(\Pi)\le5\). For (1.1), there are exactly

\[
2355.                                                     \tag{2.1}
\]

For a boundaried piece \(Q\), write \(\mathcal E(Q)\) for the subset of
these states extending to a six-coloring of \(Q\). For an operation \(\mu\),
put

\[
\Delta_\mu(Q)=\mathcal E(Q^\mu)-\mathcal E(Q).          \tag{2.2}
\]

The forced transition condition for a triple \((Q_1,Q_2,Q_3)\) is exactly

\[
\Delta_\mu(Q_i)\cap\mathcal E(Q_j)\cap\mathcal E(Q_k)
\neq\varnothing                                         \tag{2.3}
\]

for \(\{i,j,k\}=\{1,2,3\}\) and every allowed \(\mu\).

## 3. Exhaustion of pieces of order at most two

A connected one-vertex piece is \(K_1\). A connected two-vertex piece is
\(K_2\). For a \(K_2\)-piece with vertices \(a,b\), every required
boundary vertex has three possible attachment types:

\[
a\text{ only},\qquad b\text{ only},\qquad a,b.          \tag{3.1}
\]

Interchanging \(a,b\) is quotiented out. No edge to a vertex excluded in
(1.2) is allowed in this exact-defect cell. This is exhaustive: a simple
connected graph on one vertex is \(K_1\), one on two vertices is \(K_2\),
and (3.1) lists every nonempty neighborhood of a required boundary vertex
inside that interior.

For every candidate, the verifier computes \(\mathcal E(Q)\) and (2.2)
for all of:

* deletion of either interior vertex;
* deletion and contraction of the internal edge;
* deletion of every boundary--interior edge; and
* contraction of every boundary--interior edge, retaining the boundary
  endpoint as its label.

For the last operation, if \(ax\) is contracted, the color of \(x\) must
differ from the color of every other boundary neighbor of \(a\), and the
surviving interior vertex must avoid the color of \(x\). These are exactly
the new edges produced by the label-retaining contraction.

Candidates for which some \(\Delta_\mu(Q)\) is empty are discarded. The
survivors are

\[
215\text{ branch signatures},\qquad156\text{ exterior signatures}. \tag{3.2}
\]

After the necessary pairwise-intersection filter, exactly

\[
7,211,100                                               \tag{3.3}
\]

ordered triples remain. Every triple either has a common state or violates
(2.3) for at least one operation. This proves Theorem 1.

## 4. Independent verification and trust boundary

The discovery calculation is `degree8_transition_gadget_search.py`.

The independent replay `degree8_transition_gadget_verify.py` does not
import the discovery program or its state list. It independently:

1. regenerates the 2,355 exact states;
2. regenerates every \(K_1/K_2\) attachment;
3. computes every deletion and contraction family;
4. verifies the counts (3.2); and
5. exhausts the triples in (3.3).

Expected output:

```text
low exact states verified: 2355
individually critical signatures: 215 branch + 156 exterior
compatible triples exhausted: 7211100
no order-at-most-two transition architecture
```

No SAT solver or graph-minor oracle is used. The trust boundary is the two
short Python implementations and the host Python runtime; no proof-assistant
trace is exported.

## 5. Exact remaining sub-gap

The theorem does not eliminate:

* a piece with at least three interior vertices;
* a branch additionally contacting \(0\) or \(1\), or an exterior piece
  additionally contacting \(0\); or
* the other defect-intersection types and other boundary graphs.

The next smallest cell is one three-vertex connected piece together with
two pieces of order at most two under the same exact attachments. For an
actual deleted internal edge, the stronger Kempe-fan endpoint condition is
also available and was not needed above.
