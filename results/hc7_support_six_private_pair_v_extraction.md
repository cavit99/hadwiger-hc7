# Private-pair V-extraction for small `K_5` supports

**Status:** proved.  This is a graph-specific rooted extraction lemma.  It
does not by itself compose the three returned models.

## 1. Statement

Let `S_{<=6}(G)` denote the supports of `K_5` models using at most six
vertices.

### Theorem 1.1 (private-pair V-extraction)

Let `G` be a seven-connected graph with no `K_7` minor, and let
`F subseteq S_{<=6}(G)` satisfy `tau(F)>2`.  Suppose `A in F` and a
two-set

\[
                             P=\{p,q\}                 \tag{1.1}
\]

meets every member of `F-{A}`.  Then `P cap A` is empty, and there are
members `B,C in F-{A}` such that

\[
\begin{aligned}
 &P\cap B=\{p\},\qquad P\cap C=\{q\},                 \tag{1.2}\\
 &|A\cap B|\leq4,\qquad |A\cap C|\leq4.              \tag{1.3}
\end{aligned}
\]

Thus every two-vertex private transversal of one member of a critical
support kernel produces two label-faithful arms, one through each endpoint,
and both arms satisfy the separated-support intersection bound relative to
the avoided support.

## 2. Proof

The pair `P` is disjoint from `A`; otherwise it would meet `A` as well as
every member of `F-{A}`, contradicting `tau(F)>2`.

Fix `a in A`.  The pair `{q,a}` is not a transversal of `F`, so some
member `B_a in F` is disjoint from it.  This member is not `A`, because it
avoids `a`.  Since `P` meets every member other than `A`, it follows that

\[
                  p\in B_a,\qquad q\notin B_a,
                  \qquad a\notin B_a.                 \tag{2.1}
\]

If `|A|=5`, equation (2.1) immediately gives `|A cap B_a|<=4`, so any
choice of `a` supplies the required `p`-arm.

Suppose `|A|=6`.  If some `a` gives `|A cap B_a|<=4`, again the required
arm has been found.  Otherwise every one of the six choices satisfies
`|A cap B_a|=5`.  The rank-six condition and (2.1) then force

\[
                         B_a=(A-\{a\})\cup\{p\}        \tag{2.2}
\]

for every `a in A`.  Put `X=A union {p}`.  The support `A` is `X-{p}`,
and (2.2) says that `X-{a}` is a support for every `a in A`.  Hence every
six-subset of the seven-set `X` supports a spanning `K_5` model.

The audited full-seven-point-family lemma now gives a `K_6` model supported
on `X`; seven-connectivity lifts that model to a `K_7` minor.  This
contradicts the hypothesis on `G`.  Therefore a `p`-arm `B` satisfying
`|A cap B|<=4` must exist.

Interchange `p` and `q`.  Applying the same argument to the nontransversal
pairs `{p,a}` produces a `q`-arm `C` with
`P cap C={q}` and `|A cap C|<=4`.  This proves (1.2)--(1.3). \(\square\)

## 3. Consequence for bounded critical kernels

For a 3-critical rank-six support family, the bounded-kernel theorem gives,
for each `A_i`, a private transversal `P_i` of order exactly two.  Theorem
1.1 therefore upgrades every abstract set-pair certificate to the
rooted pattern

\[
                         B_i\;--\;p_i\quad
                         A_i\quad
                         q_i\;--\;C_i,                 \tag{3.1}
\]

where `B_i` contains only `p_i` from the private pair, `C_i` contains only
`q_i`, and both meet `A_i` in at most four vertices.  This is a legitimate
input shape for decorated three-model composition: unlike an unlabelled
separated triple, it remembers which literal endpoint belongs to which
arm.

The theorem does not control `|B_i cap C_i|`, choose compatible split rows,
or guarantee that simultaneous row contractions preserve
seven-connectivity.  Those remain graph-minor composition tasks.
