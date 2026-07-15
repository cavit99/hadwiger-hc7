# Cross-arm dichotomy at a private support pair

**Status:** proved in the graph-specific form below; independently audited
after correction.  The earlier purely set-system formulation was false in
the `5/5` case; see the accompanying audit.

This lemma strengthens the private-pair V-extraction without assuming
private split edges.  It identifies the only way in which two genuinely
separated labelled arms can fail to form a separated triple: those arm
families collapse to one common near-top core.

## 1. Statement

Let `G` be a seven-connected graph with no `K_7` minor, let
`F \subseteq S_{<=6}(G)` satisfy `tau(F)>2`, and let `A \in F`.  Suppose
that `P={p,q}` is disjoint from `A` and meets every member of `F-{A}`.
Define the two families of arms genuinely separated from `A` by

\[
\begin{aligned}
 \mathcal B_p&=\{B\in\mathcal F:
   P\cap B=\{p\},\
   |A\cap B|\le \max\{|A|,|B|\}-2\},\\
 \mathcal B_q&=\{C\in\mathcal F:
   P\cap C=\{q\},\
   |A\cap C|\le \max\{|A|,|C|\}-2\}.
\end{aligned}                                          \tag{1.1}
\]

Both families in (1.1) are nonempty.  Exactly one of the following holds.

1. There are `B in B_p` and `C in B_q` such that `A,B,C` are pairwise
   separated in the small-support sense:

   \[
    |U\cap V|\le \max\{|U|,|V|\}-2
       \quad(U,V\in\{A,B,C\},\ U\ne V).              \tag{1.2}
   \]

2. There are `k in {5,6}` and a `(k-1)`-set `X`, disjoint from `{p,q}`,
   such that

   \[
       \mathcal B_p=\{X\cup\{p\}\},\qquad
       \mathcal B_q=\{X\cup\{q\}\}.                \tag{1.3}
   \]

   In this second outcome, for every `a in A cap X`, both sets

   \[
                    (A-\{a\})\cup\{p\},\qquad
                    (A-\{a\})\cup\{q\}              \tag{1.4}
   \]

   belong to `F`.

Thus every private pair in an `HC_7` support-six kernel gives either a
labelled separated triple or the rigid near-top certificate (1.3)--(1.4).
The audited V-extraction gives arms with intersection at most four; the
next section contains the additional argument needed to make `5/5` arms
genuinely separated.

## 2. Genuinely separated arms exist

Fix `a in A`.  Since `{q,a}` is not a transversal of `F`, choose
`D_a in F` disjoint from it.  This support is not `A`, so the private pair
meets it and

\[
                       p\in D_a,\qquad q\notin D_a.   \tag{2.1}
\]

Suppose that no such `D_a` is separated from `A` in the sense of (1.1).
If `|A|=5`, then `D_a` cannot have order six: avoidance of `a` would give
`|A cap D_a|<=4`, already the required mixed-size bound.  Hence

\[
                         D_a=(A-\{a\})\cup\{p\}       \tag{2.2}
\]

for every `a in A`.  The support `A` and the five supports in (2.2) are
all five-subsets of the six-set `A union {p}`.  A `K_5` model supported on
five vertices is a literal `K_5`, so every five-subset is a clique.  It
follows that `A union {p}` is a literal `K_6`, which lifts to a `K_7` minor
by seven-connectivity, a contradiction.

If `|A|=6`, a nonseparated `D_a` cannot have order five, because it
contains `p outside A`; if it has order six, avoidance of `a` forces
again (2.2).  Consequently every six-subset of the seven-set
`A union {p}` supports a `K_5` model.  The audited full-seven-point-family
lemma gives a `K_6` model on this seven-set, which again lifts to `K_7`.

Thus some `D_a` belongs to `B_p`.  Interchanging `p,q` proves that
`B_q` is nonempty.

## 3. Proof of the arm collapse

Call two supports **near-identical** when their intersection has order at
least the larger support order minus one.  If some
`B in B_p,C in B_q` are not near-identical, then their intersection obeys
the bound in (1.2).  The other two bounds are the defining bounds in
(1.1), so outcome 1 holds.

Assume instead that every cross-pair from `B_p x B_q` is near-identical.
Fix `B in B_p` and `C in B_q`.  They cannot have different orders.  Indeed,
near-identity for orders five and six says that the five-set is contained
in the six-set.  But `p in B-C` and `q in C-B`, so neither set contains the
other.

Write their common order as `k`.  Since `p in B-C` and `q in C-B`, their
intersection has order at most `k-1`; near-identity makes it exactly
`k-1`.  The two unique differences are precisely `p` and `q`.  Thus, for
`X=B cap C`,

\[
                         B=X\cup\{p\},\qquad
                         C=X\cup\{q\}.                \tag{3.1}
\]

Now let `B' in B_p`.  The pair `B',C` is near-identical.  The same
different-order argument shows `|B'|=k`, and the prescribed differences
`p in B'-C` and `q in C-B'` force

\[
                              B'=X\cup\{p\}=B.
\]

Hence `B_p={B}`.  Symmetrically `B_q={C}`, proving (1.3).  The two
outcomes are mutually exclusive because in outcome 2 the sole cross-pair
is near-identical.

## 4. The forced near-top witnesses

Fix `a in A cap X`.  Since `{q,a}` is not a transversal of `F`, choose a
support `D_a` disjoint from it.  This support is not `A`, and the private
pair `P` meets it.  Therefore

\[
                         p\in D_a,\qquad q\notin D_a. \tag{4.1}
\]

If `D_a` were separated from `A`, then `D_a in B_p`, so (1.3) would give
`D_a=B`.  But `a in A cap X subseteq B`, contrary to the choice of
`D_a`.  Therefore `D_a` is not separated from `A`.

If `|A|=5`, this forces `|D_a|=5` and `|A cap D_a|=4`: an order-six
support avoiding `a` would already be separated.  If `|A|=6`, it forces
`|D_a|=6` and `|A cap D_a|=5`: an order-five support cannot contain five
vertices of `A` as well as `p`.  In either case, avoidance of `a` and the
presence of `p outside A` give

\[
                            D_a=(A-\{a\})\cup\{p\}.   \tag{4.2}
\]

Interchanging `p` and `q` gives the second support in (1.4).  This proves
the theorem. \(\square\)

## 5. Exact contribution and remaining gap

The theorem is a graph-specific extraction invariant, not a composition
theorem.  It removes arbitrary arm--arm overlap from the private-pair
programme: failure of a separated labelled triple produces one common
core `X` and a forced family of literal near-top replacements around every
vertex of `A cap X`.

It does not yet prove that the split rows of the separated triple are
compatible.  Nor does (1.3) by itself compose the two near-identical models
with `A`.  The next graph-specific step is to use the actual spanning
`K_5` models on the sets in (1.3)--(1.4): either their complement
star-forest constraints force `K_7`, or one replacement strictly reduces
the overlap between the avoided model and the common core.
