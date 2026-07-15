# Separating twin seam: literal first-exit decoder

**Status:** proved and independently audited local reduction.  This decodes
the two twin-view mismatch paths without assigning palette colours to model
rows.  It does not prove the separating-edge branch of the double-lock
exchange theorem.

## 1. Setup

Use the notation and hypotheses of the audited separating-gate theorem.
Thus

\[
 A-Z=D\mathbin{\dot\cup}E,
 \qquad S=I\mathbin{\dot\cup}A_0\mathbin{\dot\cup}B_0,
 \qquad |A_0|=|B_0|=2,
\]

\[
 K=Z\mathbin{\dot\cup}I,
 \quad \Omega_D=K\mathbin{\dot\cup}A_0,
 \quad \Omega_E=K\mathbin{\dot\cup}B_0.
\tag{1.1}
\]

There is no `A-R` edge, and

\[
 N_G(D)=\Omega_D,
 \qquad
 B_E=V(G)-(E\cup\Omega_E)
     =D\mathbin{\dot\cup}A_0\mathbin{\dot\cup}R.
\tag{1.2}
\]

Let `f=dt`, with `d in D` and `t in Z`, separate `z,u` in one
two-colour compulsory lock.  The audited theorem gives shortest paths

\[
 P_D=t\ldots r_D,
 \qquad P_E=t\ldots r_E,
\tag{1.3}
\]

where both contain `f`, the internal vertices of `P_D` lie in `D`, the
internal vertices of `P_E` lie in `B_E`, and

\[
 r_D\in\Omega_D-\{t\},
 \qquad r_E\in\Omega_E-\{t\}.
\tag{1.4}
\]

## 2. Literal excursion accounting

### Lemma 2.1

At least one of the following four geometric forms can be selected.

1. **Collapsed common-duty path.**  The path `P_E` has all internal
   vertices in `D`, and its other endpoint belongs to `K`.  It is therefore
   itself eligible as a `D`-closed mismatch path and may coincide literally
   with `P_D`.
2. **Rich final-exit connector.**  The path `P_E` contains a subpath

   \[
                         J=a\ldots r_E               \tag{2.1}
   \]

   with `a in A_0`, `r_E in I union B_0`, and every internal vertex of
   `J` in `R`.  It remains an `alpha-beta` path in the original named
   compulsory lock.  The path `J` meets `P_D` in at most one vertex,
   necessarily a common endpoint of the two displayed paths.
3. **Closed rich excursion.**  The path `P_E` contains a subpath

   \[
                         J=a\ldots a'                 \tag{2.2}
   \]

   with distinct `a,a' in A_0` and every internal vertex of `J` in `R`.
   After the return through `a'`, the path eventually ends at a member of
   `K`.  The path `J` meets `P_D` in at most one vertex, necessarily one
   of `a,a'` and the endpoint `r_D` of `P_D`.
4. **Singleton boundary detour.**  The path `P_E` contains a subpath

   \[
                          x-a-y                         \tag{2.3}
   \]

   with `x,y in D` and `a in A_0`.  This maximal excursion from `D` has
   no vertex in `R`.  After the last such returning excursion, the path
   ends at a member of `K`.

In particular, if `r_E in B_0`, the second outcome occurs and `J`
is a literal connector from one exclusive pair `A_0` to the other
exclusive pair `B_0`.

### Proof

Delete the initial vertex `t` from `P_E`.  The resulting path begins at
`d in D`, ends at `r_E in Omega_E`, and otherwise lies in

\[
                     B_E=D\mathbin{\dot\cup}A_0
                              \mathbin{\dot\cup}R.
\]

If it never leaves `D` before its last vertex, then its last edge shows
that `r_E in N_G(D)=Omega_D`.  Formula (1.1) gives

\[
                         r_E\in\Omega_D\cap\Omega_E=K,
\]

which is outcome 1.

Otherwise decompose the part of `P_E-t` outside `D` into its maximal
excursions.  Every excursion starts at a vertex of `A_0`: its predecessor
lies in `D`, it cannot start in `R` because there is no `A-R` edge, and an
internal vertex of `P_E` cannot lie in `Omega_E`.

If the final excursion does not return to `D`, let `a` be its last
`A_0`-vertex.  Every internal vertex of the suffix `a P_E r_E` lies in
`R`.  The endpoint `r_E` cannot be in `Z`.  If the suffix has an internal
vertex, its final edge would be an `R-A` edge.  If it has none, the edge
from `a in A_0` to `r_E in Z` contradicts the normal-form inclusion
`N_S(Z) subseteq I`.  Hence `r_E in I union B_0`, proving (2.1).

It remains to consider the case in which every excursion returns to `D`.
Choose the last excursion and let `a` be its first `A_0`-vertex and `a'`
its last `A_0`-vertex.  If `a` and `a'` are distinct, the subpath from `a`
to `a'` has all internal vertices in `R`, possibly none; this is outcome 3.
If `a=a'`, simplicity of `P_E` makes the excursion the single vertex
`a in A_0`, entered and left through vertices `x,y in D`; this is outcome
4.  After either kind of last returning excursion, the remaining path
stays in `D` until its endpoint, so the last edge gives
`r_E in N_G(D)`.  As also `r_E in Omega_E`, formula (1.1) gives
`r_E in K`.

In outcomes 2 and 3 the internal vertices of `P_D` lie in `D`, whereas
those of `J` lie in `R`.  The only vertices of `P_D` outside `D` are
`t,r_D`; the endpoints of `J` lie in the old boundary and never include
`t`.  Consequently an intersection can only be `r_D` at one endpoint of
`J`.  In outcome 3 the two endpoints of `J` are the two distinct members
of `A_0`, so at most one can equal `r_D`.  This proves the asserted
intersection bounds and the final assertion.  \(\square\)

## 3. The exact duplicated-duty closure

The path decoder becomes terminal only after its one labelled connector is
upgraded to two disjoint copies of the five common duties.  The following
is the precise safe upgrade.

### Lemma 3.1 (matched common-duty split exclusion)

Assume the normalized residual packet number

\[
                         \nu_{B_E}^{\Omega_E}=1.       \tag{3.1}
\]

Let `A_0={a_1,a_2}`, and let `R_1,R_2` be the two old disjoint connected
`S`-full packets in `R`.  There do not exist disjoint connected subgraphs
`X_1,X_2 subseteq D` such that, after possibly interchanging `a_1,a_2`,

1. `X_i` is adjacent to `a_i`; and
2. every literal vertex of `K` has a neighbour in each `X_i`.

### Proof

Suppose such subgraphs exist and put

\[
                       Y_i=X_i\cup\{a_i\}\cup R_i.
\tag{3.2}
\]

The two sets are disjoint and lie in
`B_E=D dotunion A_0 dotunion R`.  Each is connected: the first required
edge joins `X_i` to `a_i`, while `S`-fullness of `R_i` supplies an edge
from `a_i` to `R_i`.

Each `X_i` contacts every member of `K`, and each `R_i` contacts both
members of `B_0`.  Hence both `Y_i` are `Omega_E=K dotunion B_0`-full.
They are two disjoint full packets in `B_E`, contradicting (3.1).
\(\square\)

The symmetric statement holds with `D,A_0,B_E,Omega_E` replaced by
`E,B_0,B_D,Omega_D`.

## 4. Exact unresolved implication

Lemmas 2.1 and 3.1 identify the label-faithful content of the two mismatch
paths.

* In the collapsed outcome, the two paths may be the same literal
  `t-K` path through `D`; there is no second carrier to allocate.
* In the first-exit outcome, `J` supplies one genuine old-boundary duty
  connector, internally disjoint from the `D`-path.  It supplies no second
  copy of all five labels in `K`.
* In the closed-excursion outcome, `J` joins the two exclusive duties in
  `A_0` through `R`, but the remaining path returns to the same lobe and
  ends in `K`.  This again supplies no duplicated copy of all five common
  duties.
* In the singleton-detour outcome there is no rich-shore connector at all;
  the path merely visits one exclusive boundary vertex between two lobe
  vertices before ending in `K`.

Thus the remaining separating-edge implication is exactly:

> Use the four response-matched bypasses, the double-contraction saturation
> fork, or an internal-edge response to turn the one first-exit connector
> into the forbidden matched common-duty split of Lemma 3.1; otherwise
> prove that the unique owners of the missing `K` duties form one coherent
> fixed pair or an actual state-carrying separator.

No audited input presently proves this implication.  The response bundle
can be concentrated in one portal core, and palette saturation names
colours rather than the five literal members of `K`.  Treating either as
the two subgraphs `X_1,X_2` would be precisely the forbidden
palette-to-duty lift.  Consequently this note is a rigorous decoder of the
two mismatch paths, but not the requested double-lock exchange theorem.
