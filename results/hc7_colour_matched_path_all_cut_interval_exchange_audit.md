# Audit of the all-cut interval exchange criterion

**Verdict:** GREEN for the exact theorem revision identified below.

## Audited revision

The audited file is
`results/hc7_colour_matched_path_all_cut_interval_exchange.md`.

**Source SHA-256:**
`719e034ea81221c4fbddd77ea4cdd661ce1b04b1f84b007a69e73a89de4f2057`.

## 1. Endpoint and disjointness checks

The path convention is unambiguous: `p_0` is the only path vertex in `C`,
`p_m` is the only path vertex in `T`, and the cut index `q` ranges from 1
to `m`.  Hence

\[
 C_q=C\cup\{p_1,\ldots,p_{q-1}\},\qquad
 U_q=\{u,p_q,\ldots,p_m\}
\]

are disjoint connected sets for every permitted `q`.  Their adjacency is
the literal edge `p_{q-1}p_q`.  Removing all of `V(P)` from every protected
branch set makes every selected residual component disjoint from both of
them and from the other protected branch sets.

## 2. Interval equivalence

For a residual component `L`, left adjacency at cut `q` is exactly

\[
 E(L,C)\ne\varnothing
 \quad\text{or}\quad
 A_P(L)\cap\{0,\ldots,q-1\}\ne\varnothing.
\]

When the first alternative fails, this is equivalent to
`1+min A_P(L)<=q`.  The convention `lambda=m+1` correctly represents the
empty attachment set.

Right adjacency is exactly

\[
 E(L,\{u\})\ne\varnothing
 \quad\text{or}\quad
 A_P(L)\cap\{q,\ldots,m\}\ne\varnothing.
\]

When the first alternative fails, this is equivalent to
`q<=max A_P(L)`.  The convention `rho=0` correctly represents the empty
attachment set.  Therefore the valid cuts are exactly the integer points
of `[lambda,rho]`.

## 3. Branch-set model audit

Under (3.1), choose a common integer cut `q`.  The seven branch sets are

\[
 C_q,U_q,\{z\},L_X,L_{D_1},L_{D_2},L_{D_3}.
\]

They are connected and disjoint.  The proof accounts for every adjacency:

- `C_q U_q` is the cut edge;
- `z C_q` is inherited from the deficient branch set meeting `S`;
- `z U_q` is the edge `zu`;
- each residual component sees `C_q,U_q` by the interval lemma;
- each sees `z` by hypothesis; and
- the four residual components are pairwise adjacent by hypothesis.

No completion edge, contracted quotient adjacency, or hidden planarity
assumption is used.

## 4. Quasi-model check

For seven disjoint bags with `c_i` internal components, contracting those
components produces a simple minor on `n=sum c_i` vertices.  Pairwise-union
connectedness gives at least `c_i+c_j-1` edges between parts `i,j`.
Summing gives

\[
       \sum_{i<j}(c_i+c_j-1)=6\sum_i c_i-21=6n-21.
\]

As `n>=7`, this is at least `5n-14`; the cited `p=7` case of Mader's
theorem therefore gives a `K_7` minor.  The contraction is legitimate even
though an original quasi-bag is disconnected, because its individual
components are contracted separately.

For Corollary 4.2, requiring every included component to see a connected
anchor bag makes its union with that anchor connected.  Requiring every
included component to see `z` does the same for the singleton anchor.
The separate pairwise-union hypothesis covers the six pairs among the four
protected representatives.  These are exactly all 21 bag pairs.

## 5. Independent barrier replay

The deterministic construction in
`barriers/hc7_three_common_geodesic_two_apex_verify.py` was rebuilt with
the six displayed colour classes in Section 5 of the theorem.  Direct
checks gave:

```text
S = [0,1,20,42,43]
T = [1,5,19,42,43]
C = [3,8,20,21,24,27]
P = [20,17,19]
```

Every graph induced by colour 0 and one of colours 1 through 5 is
connected.  Deleting the path from the four protected branch sets leaves
one 19-vertex component `X-{17}` and the singletons `42,43,1`.  Each has
path attachment indices `{0,1,2}`, sees both base anchors, and therefore
has interval `[1,2]`.  The 19-vertex component is nonadjacent to `{1}`.
Their open-neighbourhood orders are 24 and 7.  This confirms both the
failure of the transversal-clique hypothesis and the theorem's stated
limitation.  It also confirms failure of the natural quasi-model packaging,
since `(X-{17}) union {1}` is disconnected.

## 6. Scope

The theorem proves only an exact model-construction criterion.  It does not
prove that failure gives a separator of order at most seven.  The barrier
test is not a counterexample to a global order-seven alternative because
that host is six-colourable and has the displayed order-seven separators.

## Unresolved assumptions or gaps

None for the stated interval criterion.  The order-seven strengthening is
open.
