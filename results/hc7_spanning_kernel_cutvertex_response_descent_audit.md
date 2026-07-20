# Independent audit of the cutvertex full-neighbourhood response transfer

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_spanning_kernel_cutvertex_response_descent.md`](hc7_spanning_kernel_cutvertex_response_descent.md)
at SHA-256

```text
4c1f590522f6ad1baccdd3b610e6fb3443e466e833018281d5a7946eb170f69c
```

The final revision changes only the source status line to link this audit;
the audited mathematics is unchanged.  The separator, edge-deletion colouring, gluing contradiction, boundary-size
estimate, lexicographic comparison, and minimum-boundary fullness conclusion
are all valid under the stated hypotheses.  The conclusion is a one-step
fresh full-neighbourhood response transfer.  It is not a recursive
exact-block descent, and the source now states that limitation explicitly.

## 1. The lobe and its literal neighbourhood

Let `R` be a component of `G[A-v]`, where `v` is a cutvertex of the
connected graph `G[A]`.  By the definition of a cutvertex, `G[A-v]` has at
least two components.  Therefore `R` is nonempty and connected and omits
`v` and at least one other component, so

```text
|R| < |A|.
```

No edge joins `R` to a different component of `G[A-v]`.  Every neighbour of
`R` in `A-R` is consequently `v`.  The standing anticompleteness
`E_G(A,D)=emptyset` excludes all neighbours in `D`.  Hence the literal open
neighbourhood satisfies

```text
X=N_G(R) subseteq B union {v},
```

and `|X|<=|B|+1=10`.

The sets `R` and `D` are both nonempty and avoid `X`.  Every path leaving
`R` meets `X=N_G(R)`, so `X` separates `R` from `D`.  Seven-connectivity
therefore gives `|X|>=7`.  It also implies that `G` is connected.  Thus
`R` has an edge to `X`; equivalently a crossing edge exists.  No hidden
fullness assumption on either original shore is used.

## 2. Proper-minor colouring and the response trace

Fix a crossing edge `xy`, with `x in R` and `y in X`.  Edge deletion is a
minor operation, and deleting the existing edge strictly lowers the edge
count, so `G-xy` is a proper minor.  The standing minor-criticality
hypothesis supplies a proper six-colouring `c` of `G-xy`.

The equality `c(x)=c(y)` is forced.  If the two colours differed, restoring
the sole deleted edge would leave the colouring proper and would
six-colour `G`, contrary to `chi(G)=7`.

The boundary trace `c|X` has the two claimed extensions:

1. `c` restricted to `G-R` is proper, since the deleted edge has its
   endpoint `x` in `R` and therefore is absent from `G-R`;
2. `c` restricted to `(G-xy)[R union X]`, equivalently to
   `G[R union X]-xy`, is proper.

The phrase `c|G[R union X]` in the proof is therefore read in its stated
context as the restriction of the colouring of `G-xy` to `R union X`; it
does not claim that `c` is proper on the intact edge `xy`.

Suppose the same labelled trace extended to a proper colouring `f` of the
intact graph `G[R union X]`.  Use `f` on `R union X` and `c` on `G-R`.
They agree vertex by vertex on the overlap `X`.  There is no edge from `R`
to `V(G)-(R union X)` because `X=N_G(R)`.  Thus the two colourings glue to
a proper six-colouring of all of `G`, a contradiction.  The trace is
therefore rejected by the intact inside, exactly as required by the
definition of a full-neighbourhood response.  This argument works for
every crossing edge and every proper six-colouring of its deletion.

## 3. Boundary size and the declared comparison

The response measure is

```text
mu(R,X)=(|R|,|X|).
```

Since `|R|<|A|`, lexicographic order gives

```text
mu(R,X) < (|A|,9)
```

independently of the second coordinate, including the possible case
`|X|=10`.  Both coordinates refer to literal vertex sets in the fixed host
graph.

This is a valid one-step comparison.  It does not show that the new trace
retains the exact singleton block, list assignment, opposite critical
kernel, or minor-model labels, nor that another transfer re-enters the same
class.  Consequently it does not by itself define a repeated well-founded
induction.  Sections 2 and 3 of the source make precisely this trust
boundary explicit.

## 4. Fullness when the returned boundary has order seven

Assume `|X|=7`.  The graph `G-X` has at least two components: `R` is one,
while the connected nonempty set `D` lies in another because every path
from `R` to `D` meets `X`.

Let `C` be any component of `G-X`.  If some `z in X` had no neighbour in
`C`, then

```text
N_G(C) subseteq X-{z}.
```

Deleting `N_G(C)` separates the nonempty component `C` from at least one
other component of `G-X`, which remains outside both `C` and `N_G(C)`.
This would be a vertex cut of order at most six, contrary to
seven-connectivity.  Hence every component of `G-X` is adjacent to every
literal vertex of `X`.

The argument is symmetric under interchanging `A` and `D`.

## 5. Scope

The audited implication is exactly:

```text
two nonempty connected anticomplete shores across a nine-vertex set
+ chi(G)=7
+ seven-connectivity
+ six-colourability of every proper minor
+ a cutvertex in one shore
=> a fresh full-neighbourhood response (R,N_G(R))
   with 7 <= |N_G(R)| <= 10 and |R| smaller than that shore,
   and literal boundary fullness when |N_G(R)|=7.
```

It does not eliminate a singleton shore, does not handle two-connected
shores, does not preserve the exact-block data, and does not prove a
recursive re-entry or a complete proof of `HC_7`.
