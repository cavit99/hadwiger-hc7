# Cofacial portal concentration contradicts seven-connectivity

**Status:** proved and independently audited.

This note closes the planar outcome of the proposed four-connected
rooted-`K_4` route.  It uses neither a duty split nor a near-clique model:
once six of the seven literal portal systems lie on one face, planar
curvature produces a vertex of total degree at most six.

## 1. A plane degree lemma

### Lemma 1.1 (an off-face vertex of degree at most five)

Let `L` be a finite simple four-connected planar graph, and fix a face `F`
in its unique plane embedding.  Then there is a vertex

\[
                         x\notin V(F)
\]

such that

\[
                            d_L(x)\le 5.                \tag{1.1}
\]

#### Proof

Write `I=V(L)-V(F)`.  Let `n=|V(L)|`, `m=|E(L)|`, and let `f=|V(F)|`.
For every face `D ne F`, write `ell(D)` for the length of its facial cycle
and put

\[
             epsilon=\sum_{D\ne F}(\ell(D)-3)\ge0.
\]

Euler's formula and face-edge counting give

\[
                         m=3n-f-3-epsilon.
\]

Consequently

\[
 \sum_{v\in I}(6-d_L(v))
 +\sum_{v\in V(F)}(4-d_L(v))
 =6n-2f-2m
 =6+2epsilon.                                          \tag{1.2}
\]

Four-connectivity gives minimum degree at least four in `L`.  Every
summand indexed by `V(F)` in (1.2) is therefore nonpositive.
Consequently some vertex `x in I` has

\[
                         6-d_L(x)>0.
\]

In particular `I` is nonempty and

\[
                         d_L(x)\le5,
\]

as required.  \(\square\)

## 2. Literal-adhesion consequence

Let

\[
                   V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

be a literal separation: there is no `L-R` edge.  Fix a set `U subseteq S`
and suppose `G[L]` is four-connected and planar.  Assume that one face `F`
of `G[L]` contains every portal belonging to the other boundary literals:

\[
                N_L(S-U)\subseteq V(F).                \tag{2.1}
\]

### Theorem 2.1 (cofacial portal degree bound)

Under these hypotheses, `G` has a vertex `x in L-V(F)` satisfying

\[
                         d_G(x)\le5+|U|.                \tag{2.2}
\]

#### Proof

Apply Lemma 1.1 to obtain `x outside V(F)` with `d_L(x)<=5`.  Condition
(2.1) says that `x` has no neighbour in `S-U`, and the separation says
that it has no neighbour in `R`.  Its only possible neighbours outside
`L` therefore belong to `U`.  Thus

\[
             d_G(x)=d_L(x)+|N_S(x)|\le5+|U|.
\]

\(\square\)

### Corollary 2.2 (the exact-seven common-face cell is empty)

Suppose `G` is seven-connected, `|S|=7`, and `U={c}`.  There is no
four-connected planar open shore `L` for which all six non-`c` portal sets
lie on one face.

Indeed, Theorem 2.1 gives a vertex of `G` of degree at most six, whereas a
seven-connected graph has minimum degree at least seven.

## 3. Application to the width-two route

In the paired exact-seven cell

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},
\]

assume the rooted-model/common-face dichotomy has placed all six complete
portal sets of `a_i,t_i` on one face of a four-connected planar thin shore
`L`.  Corollary 2.2 is an immediate contradiction.  Therefore this planar
outcome cannot coexist with the actual seven-connected host assumptions.

This conclusion is independent of:

* the paired boundary edges;
* a choice of bipartition duties `A,B`;
* existence or failure of an `A-B` carrier split;
* the adjacent full packets `P,Q`; and
* exclusion of `K_7` or `K_7^vee`.

Thus no static counterexample satisfying the requested full hypotheses can
exist.  The remaining burden in this route is solely the preceding
label-faithful dichotomy: derive a rooted model or put **all six complete
literal portal sets** on one face.  Cofaciality of only selected
representatives is not enough for Theorem 2.1.
