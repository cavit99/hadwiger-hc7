# Dirac equality and external-path witnesses do not escape an atomic fan

**Status:** written finite barrier with a deterministic exact checker;
independently audited in
[`hc7_atomic_fan_dirac_rolek_barrier_audit.md`](hc7_atomic_fan_dirac_rolek_barrier_audit.md).
The
graphs below are not seven-connected or contraction-critical, so this is
not a counterexample to `HC_7`.  It shows that minimum degree, Dirac's
neighbourhood bound, and the standard equality-case external paths do not
by themselves repair the concentrated-fan obstruction.

## 1. Literal atomic fan

Use any one of the seven completed cores from the
[two-fan barrier](hc7_repaired_contact_two_fan_barrier.md).  Its normalized
vertices are

\[
 a_0,a_1,a_2,a_3,x,y,b_0,b_1,b_2,r,p,q,c,d,
\]

where `c` is the centre of the first fan and `d` is the centre of the
second.  Replace the artificial edge `a0-b0` by the literal two-edge path

\[
                         a_0-w-b_0,                    \tag{1.1}
\]

and retain the edges `ca0, cw, cb0`.  Thus the first filled adhesion
triangle has been replaced by a literal atomic wheel sector.  Let `H` be
the resulting fifteen-vertex graph before any further edge incident with
`w` is added.

The three compulsory neighbours of `w` are

\[
                         a_0,b_0,c.                    \tag{1.2}
\]

Every statement below is checked for all seven choices of the second fan.

## 2. Exact neighbourhood calculation

### Proposition 2.1

Add edges from `w` to vertices of

\[
 V(H)-\{a_0,b_0,c,w\}.                                \tag{2.1}
\]

The following assertions hold.

1. If exactly four such edges are added and the resulting graph has no
   `K7` minor, then the neighbourhood of `w` has independence number three.
2. If exactly five such edges are added, the resulting graph has no `K7`
   minor precisely for the following two sets of five additional
   neighbours:

   \[
   \{a_1,a_2,a_3,b_1,b_2\},\qquad
   \{a_1,a_2,x,b_1,b_2\}.                              \tag{2.2}
   \]

   In both cases `alpha(N(w))=3`.
3. If at least six such edges are added, the resulting graph contains a
   `K7` minor.

#### Proof

For four additional neighbours there are `binom(11,4)=330` choices.  The
exact connected-branch-set search leaves eleven choices in every one of
the seven rows, and direct exhaustive inspection of each induced
neighbourhood gives independence number three.

A five-set can be negative only if all five of its four-subsets occur in
that eleven-set negative list, because adding an edge cannot destroy a
minor model.  There are exactly two such candidates, namely (2.2), and the
exact search verifies that both are negative.  Their neighbourhood
independence number is three.

Finally, every six-subset of (2.1) contains a four-subset outside the
eleven negative four-sets.  That positive four-subset already gives a
`K7` minor.  The same is true after adding still more neighbours.  This
proves all three assertions.  \(\square\)

### Corollary 2.2 (the exact critical residue)

Suppose the displayed configuration occurs in a seven-contraction-critical,
`K7`-minor-free graph `G`, and `w` has no neighbour outside the displayed
fourteen-vertex core.  Then

\[
 d_G(w)=8                                                   \tag{2.3}
\]

and its five additional neighbours have one of the two forms (2.2).

#### Proof

A noncomplete seven-contraction-critical graph has minimum degree at least
seven.  If `d(w)=7`, Dirac's bound gives

\[
 \alpha(N(w))\le d(w)-7+2=2,
\]

contradicting Proposition 2.1(1).  Proposition 2.1(3) excludes degree at
least nine.  Proposition 2.1(2) gives (2.2).  \(\square\)

Thus the local use of minimum degree and Dirac's inequality is exact: it
does force an external neighbour unless the fan vertex has degree eight,
but it leaves two genuine degree-eight patterns.

## 3. The equality-case paths are absorbed by the old core

For either pattern in (2.2), Dirac's inequality is attained:

\[
 d(w)=8,qquad \alpha(N(w))=3.                         \tag{3.1}
\]

The two independent triples

\[
 I_1=\{a_1,b_2,c\},\qquad I_2=\{a_2,b_1,c\}           \tag{3.2}
\]

occur in both patterns.  The standard equality-case external-path lemma
for contraction-critical graphs therefore gives the following disjoint
path demands.  Put `t=a3` for the first pattern of (2.2), and `t=x` for
the second.

\[
\begin{array}{c|cc}
 &\text{first path}&\text{second path}\\ \hline
 I_1&a_0\mathbin{-}b_1&t\mathbin{-}b_0\\
 I_2&a_0\mathbin{-}b_2&t\mathbin{-}b_0.
\end{array}                                             \tag{3.3}
\]

For each row, the two paths in either line can be chosen vertex-disjoint,
with all their internal vertices outside `N[w]`, **entirely within the
same fifteen-vertex atomic graph**.  The checker supplies all 28 path-pair
certificates.  For example, in the row `(z=p, second rail=P3)`, the first
pattern admits

\[
 a_0-x-y-r-b_i,qquad a_3-p-b_0
 \quad(i=1,2),                                          \tag{3.4}
\]

and the second admits

\[
 a_0-a_3-y-r-b_i,qquad x-q-b_0
 \quad(i=1,2).                                          \tag{3.5}
\]

Consequently, invoking the equality-case paths after the Dirac reduction
does not force a path to leave the concentrated fan quotient.  The old
normalized core already realizes every required pair.

## 4. What this blocks

The following proposed mechanism is invalid:

> Restore the minimal-counterexample degree bound and Dirac's
> neighbourhood inequality at an atomic fan vertex; in the equality case,
> apply the contraction-critical external-path lemma.  One of these steps
> must produce an external bridge escaping the fan interval.

The degree argument stops exactly at (2.2), and all the resulting path
demands can remain inside the quotient.  This does **not** refute an
escape theorem that uses seven-connectivity globally, a complete boundary
colouring transition, or an order-seven separation argument.  It shows
that one of those additional ingredients is indispensable.  In
particular, the next useful statement must control how the internally
available paths coexist with bridges forced elsewhere by
seven-connectivity; merely citing the equality-path lemma cannot do that.

## 5. Verification

Run from the repository root:

```sh
python3 barriers/hc7_atomic_fan_dirac_rolek_barrier.py
```

Expected output:

```text
rows 7
degree_seven_negative_counts (11, 11, 11, 11, 11, 11, 11)
degree_eight_negative_counts (2, 2, 2, 2, 2, 2, 2)
rolek_core_path_pairs 28
certificate_digest 0bfc8eb21a675c644c86a639df2bcf699e4f373bc9bd9abc40dc50e51d51d86c
GREEN: atomic Dirac residues and internal Rolek path pairs verified
```

The checker uses the exact `K7` detector from the audited six-terminal
crossing decoder.  The degree-at-least-nine conclusion is a monotonic
finite reduction to the verified degree-seven cases, not an extrapolation
from a bounded host order.
