# Independent audit: connected-rich carrier exchange

**Status:** GREEN after strengthening both finite verifiers to assert that
their selected contraction block is inclusion-maximal.

## 1. Exact scope

The audited conclusions apply in the actual exact-seven separation cell

\[
 |S|=7,\qquad (\nu_L,\nu_R)=(1,2),
\]

for a 7-connected, strongly 7-contraction-critical, `K_7`-minor-free graph,
and only to the ten already-audited absolute-demand-three boundary orbits.
For the geometric corollaries both open shores are nonempty and `G[R]` is
connected.  No conclusion is asserted for the other boundary orbits or for
an abstract boundaried graph lacking the counterexample hypotheses.

Within that scope, Lemmas 1.1 and 1.2, Theorems 2.1 and 2.2, and Corollaries
3.1 and 3.2 are correct.

## 2. Label-free carrier lemmas

Let `C` be a maximum clique among the singleton blocks of the returned
partition.  Demand three means that exactly three partition blocks remain
outside the retained singleton clique.

For Lemma 1.1, a carrier with sole defect `a` can fund any block avoiding
`a`.  If `a` is retained in `C`, maximality of the exact independent block
`I` supplies an `a-I` edge, so assigning `I` to the carrier repairs its only
missing representative-to-`C` adjacency.  If `a` is not in `C`, its own
partition block is one of the three unrepresented blocks, and either of the
other two avoids `a`.  The two full packets fund the remaining blocks.  They
need not have an edge to each other: fullness makes each packet adjacent to
the nonempty boundary block assigned to the other representative.  The same
observation gives their adjacencies to the partial carrier representative.
Thus every required contracted set is connected and all retained
representatives form a clique.

For Lemma 1.2, condition (1.1) is exactly the carrier criterion.  Avoiding
both defects makes the carrier--block union connected; a boundary edge from
the assigned block repairs every missed singleton in `C`.  If the two
defects both avoid `C`, at least one of the three unrepresented blocks avoids
both.  If both lie in `C`, maximality makes `I` adjacent to both and `I`
works.  With exactly one defect `a` in `C`, failure first forces the other
defect `b` into `I`; the only remaining candidates are the other two blocks,
and failure is then precisely their avoidance of `N_H(a)`.  This proves both
directions of the stated obstruction.

## 3. Equal-defect finite extension

The required quantifier order is

```text
H and the two geometric defects
  -> choose a maximal independent exact block I
  -> contract the opposite full packet together with I
  -> receive an arbitrary exact boundary state containing I
  -> choose a maximum singleton clique and assign the three carriers.
```

`active/hc7_exact7_equal_defect_extension.py` implements that order.  It
checks all 49 ordered defect pairs for each of the ten hard boundary graphs.
For the first nine graph6 certificates one fixed block works for every pair.
For the standard Moser spindle, `{0,5}` is used exactly when both defects lie
in `{3,4}`, and `{1,5}` otherwise.  I independently checked that every block
listed by this certificate is independent and inclusion-maximal; that check
is now also an assertion in the verifier.  A fresh run terminates with

```text
CERTIFIED equal-defect adaptive three-carrier extension
```

The verifier uses the corrected connectivity rule: a carrier cannot fund an
independent block containing its missed literal.  Equal defects therefore do
not conceal the connectivity error fixed in the earlier distinct-defect
audit.

## 4. Defect-two finite extension

For every hard boundary `H` and every defect set `D` of order zero, one, or
two, the theorem must choose `I(H,D)` before the returned equality state is
known.  The revised verifier restricts its witnesses to non-singleton,
inclusion-maximal independent blocks whose every exact state has demand
three.  It then requires the Lemma 1.2 carrier condition for **every** exact
state containing the chosen block and allows the carrier's assigned block
to be chosen only after that state and a maximum singleton clique are known.

There are

\[
 10\left(1+7+\binom72\right)=290
\]

`(H,D)` cells.  A fresh run reports zero failures, explicitly asserts all
290 cells were visited, and terminates with

```text
CERTIFIED single defect-two carrier exchange
```

The original draft did not require the enumerated witness to be maximal,
even though the analytic lemma assumed maximality.  Independent probing
showed that all 290 cells possess a maximal witness.  The verifier and
Theorem 2.2 have now been patched to impose that requirement, closing the
certificate gap rather than relying on a stronger unstated finite lemma.

## 5. Connected-rich cutvertex geometry

Let `P_1,P_2` be disjoint full packets in connected `R`, and let `w` be a
cutvertex.  At most one packet contains `w`; the other, call it `Q`, is
contained in one component `D_0` of `R-w`.  If `R-w` had at least three
components, choose two others `D_1,D_2` and set

```text
X = D_1,
Y = D_2 union {w}.
```

Then `Q,X,Y` are nonempty, connected and pairwise disjoint, and an edge from
`D_1` to `w` gives the required `XY` adjacency.  For each `i=1,2`,

\[
 N_G(D_i)\subseteq S\cup\{w\}.
\]

The nonempty opposite shore remains after this neighbourhood is removed, so
it is a genuine separator.  Seven-connectivity gives
`|N_S(D_i)| >= 6`.  Hence `X` is near-full, and `Y`, which contains `D_2`,
is also near-full.  Their defects may coincide, exactly the case supplied by
Theorem 2.1.  Adaptive contraction on the thin full packet and reflection
through `Q,X,Y` therefore six-colour `G`.  Thus every cutvertex of connected
`R` has exactly two components after deletion.

This does **not** by itself prove that the whole block-cut structure is a
path or that either lobe is full.

## 6. Three-attachment bridge condition

Fix any two disjoint full packets `P_1,P_2`, and let `K` be a component of
`R-(P_1 union P_2)`.  All neighbours of `K` outside `S` lie in the packet
union, so with

\[
 A_K=N_R(K)\cap(P_1\cup P_2)
\]

we have `N_G(K) subseteq S union A_K`.  The opposite shore again makes this
a genuine separator.  If `|A_K| <= 2`, seven-connectivity implies

\[
 |N_S(K)|+|A_K|\ge7,
\]

and therefore `K` has boundary defect at most two.  It is a connected third
carrier, disjoint from both full packets, so Theorem 2.2 reflects the state
returned by the adaptively chosen thin-shore contraction.  This contradiction
proves `|A_K| >= 3`.

The attachments counted here are three distinct **vertices** of
`P_1 union P_2`; the corollary does not claim three disjoint paths, three
attachments on each packet, or any prescribed distribution between them.

## 7. Cross-bridge triangle addendum

Lemma 3.3 is GREEN.  Its seven branch sets are literal and pairwise
disjoint: three full packets receive three distinct anchors outside the
boundary triangle, the cross-bridge is the fourth nonsingleton bag, and the
three triangle vertices remain singleton bags.  Packet fullness supplies
all adjacencies among the anchored packet bags and from them to the
triangle.  The stated two rich-packet attachments, the bridge contact with
the thin packet's anchor, and the three triangle contacts supply every
remaining adjacency.  No quotient edge, palette-to-label identification,
or stronger connectivity assertion is used.

The conclusion is deliberately conditional on the bridge attaching to both
rich packets and contacting a whole boundary triangle plus one further
literal.  It does not say that every complementary bridge has those
contacts.

## 8. Reproducibility

The audited runs were:

```text
PYTHONPATH=active/runtime/deps:active active/runtime/venv/bin/python \
  active/hc7_exact7_equal_defect_extension.py

PYTHONPATH=active/runtime/deps:active active/runtime/venv/bin/python \
  active/hc7_exact7_single_defect2_probe.py
```

Both terminated at their stated certificates.  The computational part is a
finite boundary-algebra certificate; the geometric shore arguments are
order-independent and do not enumerate interior vertices.
