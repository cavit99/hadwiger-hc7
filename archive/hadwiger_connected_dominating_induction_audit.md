# Connected-dominating chromatic descent: exact audit

## 1. Candidate statement

For a (t)-vertex-critical graph (G), consider

\[
 (\mathrm{CD}_t)\qquad
 \exists D\subseteq V(G):quad G[D]\text{ is connected},\quad
 D\text{ dominates }G-D,\quad \chi(G-D)=t-1.
\]

(The inequality `at least` is equality because (G-D) is a proper induced
subgraph of a (t)-vertex-critical graph.)

This statement has survived the finite tests made so far, but it is **not** a
routine strengthening of vertex-criticality.  The implications below show that
it is at least a full-conjecture-strength target and in fact proves a recognized
strengthening of Hadwiger.

## 2. It proves the Dominating Hadwiger Conjecture

A dominating (K_t)-model is an ordered list

\[
 (T_1,\ldots,T_t)
\]

of pairwise disjoint nonempty connected subgraphs such that, whenever (i<j),
**every vertex** of (T_j) has a neighbor in (T_i).

### Proposition 2.1

If ((\mathrm{CD}_t)) holds for every (t)-vertex-critical graph and every
(t), then every graph (G) has a dominating (K_{\chi(G)})-model.

### Proof

Induct on (t=\chi(G)).  Pass to an induced (t)-vertex-critical subgraph
(C\subseteq G).  By ((\mathrm{CD}_t)), (C) has a connected dominating set
(D) with (\chi(C-D)=t-1).  Pass inside (C-D) to an induced
((t-1))-vertex-critical subgraph (C').  By induction, (C') has a
dominating (K_{t-1})-model ((T_2,\ldots,T_t)).  Since (D) dominates all of
(C-D), every vertex of every (T_j) has a neighbor in (D).  Therefore

\[
 (D,T_2,\ldots,T_t)
\]

is a dominating (K_t)-model in (G).  (square)

Illingworth and Wood introduced this exact model notion and isolated the
statement that every (t)-chromatic graph contains such a model as the
**Dominating Hadwiger Conjecture**, explicitly a strengthening of Hadwiger.
Thus the candidate descent lemma is not an innocuous induction lemma: it would
settle that stronger conjecture as well.

Primary reference: F. Illingworth and D. R. Wood, *Dominating (K_t)-Models*,
J. Graph Theory (2025), arXiv:2405.14299.

## 3. On contraction-critical graphs it is equivalent in strength to Hadwiger

Call (G) (t)-contraction-critical when (\chi(G)=t) and every proper minor
of (G) is ((t-1))-colorable.

### Lemma 3.1 (the contraction obstruction)

Let (G) be (t)-contraction-critical and let (D) be a connected dominating
set with (|D|\ge2).  Then

\[
 \chi(G-D)\le t-2.
\]

### Proof

Contract all edges of a spanning tree of (G[D]) to a vertex (z).  The
resulting graph (G/D) is a proper minor.  Domination says that (z) is
adjacent to every vertex of (G-D), and hence

\[
 \chi(G/D)=1+\chi(G-D).
\]

Minor-criticality gives (\chi(G/D)\le t-1), proving the claim. (square)

Thus a ((\mathrm{CD}_t))-witness in a contraction-critical graph cannot have
two or more vertices.  It must be a singleton universal vertex.

### Lemma 3.2 (peeling a universal vertex)

If (G) is (t)-contraction-critical and has a universal vertex (v), then
(H=G-v) is ((t-1))-contraction-critical.

### Proof

Since (v) is universal,

\[
 t=\chi(G)=1+\chi(H),
\]

so (\chi(H)=t-1).  If (H') is a proper minor of (H), then
(K_1\vee H') is a proper minor of (G).  Therefore

\[
 1+\chi(H')=\chi(K_1\vee H')\le t-1,
\]

and (\chi(H')\le t-2). (square)

### Corollary 3.3

The assertion that every contraction-critical graph satisfies
((\mathrm{CD}_t)), for all (t), is equivalent to Hadwiger's Conjecture.

### Proof

If the assertion holds, Lemma 3.1 forces a universal singleton witness; Lemma
3.2 allows induction on (t), forcing (G=K_t).  Hence every
contraction-critical graph is complete, which is the standard minimal-minor
form of Hadwiger.

Conversely, if Hadwiger holds, a (t)-contraction-critical graph contains a
(K_t)-minor and therefore must itself equal (K_t); otherwise (K_t) would
be a proper minor of chromatic number (t).  In (K_t), any singleton is a
connected dominating set and leaves (K_{t-1}). (square)

This is the most important adversarial conclusion: in the exact
minor-minimal-counterexample class, the candidate is not a weaker structural
step.  It is another full-strength formulation.

## 4. Exact structure of a counterexample to the candidate

The following equivalence is useful for falsification.

### Lemma 4.1

For a (t)-vertex-critical graph (G), ((\mathrm{CD}_t)) holds if and only if
there is an induced ((t-1))-vertex-critical subgraph (H) such that

1. (G-H) is connected; and
2. every vertex of (H) has a neighbor in (G-H).

### Proof

If (D) witnesses ((\mathrm{CD}_t)), choose an induced
((t-1))-vertex-critical subgraph (H\subseteq G-D).  Adding the vertices of
((G-D)-H) to (D) preserves connectedness: every such vertex has a neighbor
in the original dominating set (D).  It also preserves domination of (H).
Thus (G-H) has the two stated properties.

The converse follows by taking (D=V(G)\setminus V(H)). (square)

Consequently a counterexample is exactly a (t)-vertex-critical graph in which
**every** induced ((t-1))-vertex-critical subgraph (H) either has disconnected
complement (G-H), or contains a vertex with no neighbor outside (H).

## 5. Why the obvious maximality proof stops

Take a connected set (D), maximal by inclusion subject to
(\chi(G-D)=t-1), and put (H=G-D).  If (D) is not dominating, let

\[
 S=N_G(D)\cap V(H).
\]

For every (x\in S), the set (D\cup\{x\}) is connected.  Maximality only
implies

\[
 \chi(H-x)\le t-2.
\]

Thus every boundary vertex (x\in S) is a critical vertex of the
((t-1))-chromatic graph (H).  There is no contradiction: (H) may itself be
((t-1))-vertex-critical.  Any proof that calls the extension from this point
"routine" is missing the entire difficult step.

## 6. The low-chromatic cases

The candidate is elementary for (t\le3).  For (t=3), a critical graph is an
odd cycle; leave an edge as the 2-chromatic remainder and take the complementary
path as (D).

It also follows for (t=4) from the standard nonseparating-odd-cycle theorem:
every 4-critical graph has an induced odd cycle (C) such that (G-C) is
connected.  Since (\delta(G)\ge3) and (C) is induced, every vertex of (C)
has a neighbor outside (C).  Hence (D=G-C) is connected and dominates the
3-chromatic graph (C).

The mechanism does not iterate: in a general (t)-critical graph the same
theorem still only leaves a 3-chromatic odd cycle, not a
((t-1))-chromatic remainder.

## 7. Computation performed in this audit

The scripts

* `critical_dominating_search.py`,
* `critical_dominating_ore.py`,
* `critical_dominating_schrijver.py`, and
* `critical_dominating_z3.py`

perform independent exact checks of chromatic number, vertex-criticality,
connected domination, and the remainder condition.  Random critical cores,
random Ore compositions, the Schrijver graph (SG(7,2)), and Brown's
17-vertex 5-vertex-critical circulant all had witnesses.  An eager SMT encoding
returned `UNSAT` for a labeled 5-vertex-critical counterexample on eight
vertices (without a separately checked proof certificate).  These are
falsification checks only; they do not support a general proof.

Brown's graph was encoded from the primary construction: vertices are
(\mathbb Z_{17}), with (i,j) adjacent exactly when

\[
 i-j\pmod {17}\in\{2,6,7,8,9,10,11,15\}.
\]

It is not a counterexample: one witness has

\[
 D=\{1,3,4,5,6,7,9,11,12,13,14,15,16\},
\]

leaving the 4-chromatic set (\{0,2,8,10\}).

## 8. Weakest sufficient replacement

For the ordinary Hadwiger induction, full domination of (G-D) is unnecessary.
It is enough to find

* a connected set (D), and
* a (K_{t-1})-model (T_1,\ldots,T_{t-1}) in (G-D),

such that (D) has at least one edge to every (T_i).  Then

\[
 (D,T_1,\ldots,T_{t-1})
\]

is a (K_t)-model.  This is exactly the model-meeting/contact obstruction
already isolated elsewhere in the project.  Replacing the fixed minor model by
the stronger demand that (D) dominate a ((t-1))-chromatic induced graph again
moves toward Dominating Hadwiger rather than simplifying ordinary Hadwiger.

## 9. Verdict

No proof or explicit counterexample to ((\mathrm{CD}_t)) was found.  What *was*
settled decisively is its strategic status:

* it proves the Dominating Hadwiger Conjecture, not merely Hadwiger;
* restricted to contraction-critical graphs, it is equivalent in strength to
  Hadwiger itself;
* the natural maximal-connected-set proof stops at a genuine critical-boundary
  configuration;
* the honest weaker target is labelled contact with an existing clique model.

Accordingly, ((\mathrm{CD}_t)) should not be installed as a lemma or treated as
a promising shortcut unless a new connectedization mechanism is supplied.
