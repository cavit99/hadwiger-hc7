# Independent audit: terminal-free low-cut descent

Audited file: `results/hc7_exact7_terminal_free_lowcut_descent.md`.

## Verdict

**GREEN after two scope clarifications.**  The low-cut argument is a valid
literal gate descent.  A leaf side of a cutvertex or a two-cut can be
chosen disjoint from the fixed three-connected carrier `K_0`.  At a
carrier-minimal spanning triple, such a side cannot see zero poles by
seven-connectivity and cannot see exactly one pole by absorption.
Consequently it sees both poles, and moving it into the target pole gives
a trace-preserving core in which the enlarged locked component supports
the old pair block and one named target.

The two clarifications required in the source are:

1. Section 1 must retain **all** hypotheses of Section 1 of the audited
   terminal-free state-or-rural theorem, rather than only the definition
   of `J^circ`.  In particular, the traces of `K_0,A,B` partition `U`,
   `W={w} union L` supports the pair carrier, `w` has a neighbour in `L`,
   and `L` is anticomplete to `A union B`.
2. The target returned in the both-poles branch is the named side of the
   endpoint-faithful partition which contains the selected `C-X` edge.
   It is not a preselected one of `A,B`.  If its unchanged trace is
   admissible, the operation attains that supported target state in
   addition to the pair state; otherwise the literal `w`--trace edge is
   the boundary-incompatibility certificate.  The lemma does not by
   itself promise that the attained target is the one supported on the
   opposite shore.

With these qualifications incorporated, every graph operation, exposure
count, trace statement, and state conclusion is literal.  The theorem does
not close the rural-page outcome or bilateral state matching.

## 1. Existence of a trace-free leaf side

The carrier `K` is connected and contains the fixed three-connected graph
`K_0`.

If `K` has a cutvertex `z`, every three-connected subgraph of `K` lies in
one block: if vertices of `K_0-z` occurred in two components of `K-z`,
then `K_0-z` would be disconnected.  Root the block-cut tree at the block
containing `K_0` and choose a component of `K-z` on a leaf side away from
that block.  Its vertex set `C` is connected, misses `K_0`, has
`N_K(C)={z}`, and its deletion leaves the root side and every other branch
joined through `z`.  Hence `K-C` is connected.

If `K` is two-connected but not three-connected, choose a two-cut
`{r,s}`.  The graph `K_0-{r,s}` is nonempty and connected, so all of it
lies in one component `H` of `K-{r,s}`.  Any other component `C` misses
`K_0`.  Every component of `K-{r,s}` sees both `r` and `s`: missing, say,
`r` would make `s` a cutvertex of `K`.  Thus

```
N_K(C)={r,s},
```

and the union of `{r,s}` with all other components is connected.  This
proves all clauses of Lemma 2.1.  The carrier has at least five vertices
from its two roots and a three-element inherited portal set, so no
small-graph convention for three-connectivity intervenes.

## 2. Exact exposure and the zero-pole branch

Every eligible triple has `K_0 subseteq K`, `A union B subseteq X`, and
`L subseteq Y`.  Since the traces of `K_0,A,B` already partition `U`, a
set `C subseteq K-K_0` contains no adhesion vertex; it lies entirely in
the open shore `D_t`.

The exact shore identity gives

```
N_G(C)-V(J^circ) subseteq {w,t}.
```

Because `K,X,Y` span `J^circ`, this is precisely equation (3.1).  If `C`
sees neither pole, then

```
|N_G(C)| <= |N_K(C)|+2 <= 4.
```

The vertex `v` is outside `C union N_G(C)`: open-shore vertices have no
edge to `v`.  Therefore `N_G(C)` is a genuine separator between nonempty
`C` and `v`, contradicting seven-connectivity.  No neighbour class has
been omitted from this count.

## 3. One-pole absorption and well-foundedness

Suppose `C` sees `X` and misses `Y`.  Replacing

```
(K,X,Y) by (K-C,X union C,Y)
```

is legal.  The retained carrier is connected by Lemma 2.1; `X union C`
is connected through a selected `C-X` edge; and it remains anticomplete to
`Y`.  The three parts remain induced, disjoint, and spanning.  The fixed
sets `K_0,A union B,L` remain in their named parts.  In particular, the
two inherited portal lower bounds count vertices of unchanged `K_0` and
survive exactly.

The new carrier has `|C|` fewer vertices, so finite minimization of `|K|`
is a genuine well-founded descent.  The `Y`-only case is symmetric.  Thus
at a carrier-minimal low-cut triple the selected `C` must see both poles.

## 4. Both-poles transfer

All adhesion vertices of `X` already lie in the fixed sets `A union B`.
The endpoint-faithful target-partition lemma therefore partitions `X`
into connected adjacent sets `A',B'`, containing `A,B` respectively,
without moving either trace.

Choose one literal `C-X` edge.  Let `M'` be the named part containing its
`X` endpoint and `N'` the other.  Put

```
K'=K-C,                 M''=M' union C.
```

The three blocks `K',M'',N'` are connected and disjoint.  Their
adjacencies are literal:

* `M''-N'` uses the retained edge of the target partition;
* `K'-M''` uses the old `K_0-A` or `K_0-B` adjacency belonging to `M'`;
* `K'-N'` uses the corresponding old adjacency belonging to the other
  target.

The set `C` contains no adhesion vertex, and `A',B'` did not exchange any
adhesion vertex, so all three traces are unchanged.

Now `Y` is connected, contains `L`, and contains no adhesion vertex.
Because `w` has an edge to `L`,

```
W'={w} union Y
```

is connected, avoids the side terminal, is disjoint from the core, and
has exact trace `{w}`.  It meets `M''` through the selected literal
`Y-C` edge.  It meets `K'` through an inherited `L-K_0` edge, since
`K_0 subseteq K'` and the inherited marked set has at least three
nonroot members.  Also, `Y` remains anticomplete to `N' subseteq X`.

The original support of the pair decoration says
`{w,x,y}` is independent.  Hence `W'` still supports the retained pair
block.  If `{w} union (M' cap U)` is independent, it also supports the
named target `M''`, attaining literal admissible rank at least two.  If
not, the offending edge from `w` to the unchanged target trace is exactly
the advertised boundary-incompatibility certificate.

This verifies the state conclusion without treating a raw contact as an
attained duty.  It also identifies the precise naming limitation: `M'`
is selected by the actual `C-X` edge and need not be a prescribed target.

## 5. Falsification checks and trust boundary

The natural attempted counterexamples do not break the proof:

* a pendant tree attached to a three-connected `K_0` gives the asserted
  cutvertex leaf side;
* a two-pole bridge attached through a two-cut gives the asserted
  two-cut side;
* a leaf side seeing no pole violates the exact exposure count and
  seven-connectivity;
* a leaf side seeing one pole is strictly absorbable; and
* a leaf side seeing both poles may force the target selected by its
  endpoint, which is why a **preselected-target** version would be false.

The proved conclusion is therefore

```
carrier low cut
  => strict one-pole descent,
     or an attained pair-plus-one-named-target state,
     or its literal boundary-incompatibility certificate.
```

It is not a common-state theorem, a low-cut exclusion without the exact
exposure hypothesis, or an induced-pole expansion theorem.
