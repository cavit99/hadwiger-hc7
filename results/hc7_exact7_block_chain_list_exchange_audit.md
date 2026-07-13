# Independent audit: exact-seven block-chain list exchange

## Verdict

**GREEN, under the intended audited two-lobe scope.**  The fresh-label
lemma, separator bounds, cut-duty carrier construction, finite gate-support
classification, nesting argument, common-gate closure, and raw monotone
list-state sweep are correct.  Every proposed carrier is literal, connected,
and disjoint; every claimed carrier adjacency has a literal edge; and both
uses of the three full packets produce all 21 adjacencies of a `K_7` model.

There is one presentation dependency to make explicit before promotion.  The
phrase “the audited exact-seven `(1,3)` two-lobe setting” must include that
`G[L]` is three-connected.  Sections 2--5 repeatedly use this fact.  This is
indeed part of the promoted setting cited by the note, but it is not repeated
in the displayed list of hypotheses in Section 1.  Adding it there would make
the theorem self-contained; no mathematical change is needed.

The monotonicity conclusion concerns the **raw literal carrier-contact
lists** `Lambda_h`.  It does not imply that lists remaining after singleton
propagation, a selected critical core, or an implication bicycle are nested.
The note does not make that stronger inference, and it correctly leaves the
operation-state theorem open.

## 1. Frozen dependencies

The proof uses exactly the following promoted inputs.

1. `G[L]` is three-connected.  Consequently each component of `G[L]-T`
   meets every literal member of the three-cut `T`.
2. The nested-cutvertex exchange implies that, in a `K_7`-minor-free
   survivor, `J-z` has exactly two components whenever `z` is a cutvertex of
   `J`.
3. The branching-block exchange implies that the block--cutvertex tree of
   each surviving lobe is a path.
4. The spanning-triangle list-state theorem synchronizes any proper
   list-colouring of `G[S]` across a spanning three-carrier clique partition
   of `L` and three disjoint `S`-full packets in `R`.

The fixed `T`-rooted triangle has portal matching rank two.  Hence a maximum
matching really can be written as two distinct literal representatives

\[
 p_j\in N_S(B_j),\qquad p_k\in N_S(B_k),
\]

with the third rooted bag indexed by `i`.  The proof never assumes that
`B_i` has no boundary contact; “unmatched” refers only to this chosen
maximum matching.

## 2. Fresh representatives and separator counts

Lemma 2.1 is an exact two-set Hall calculation.  If `X-F` and `Y-F` had no
distinct representatives, their union would have order at most one.  Thus

\[
 |X\cup Y|\le |F|+1\le3,
\]

contrary to the assumed lower bound four.  The individual differences are
nonempty because each original set has order at least three while `|F|=2`.

Let `A` be a component of `J-z`.  Inside `G[L]`, all exits from `A` lie in

\[
                    \{z\}\cup U_A,
        \qquad U_A=N_T(A).
\]

If `|U_A|<=1`, those at most two vertices separate `A` from the nonempty
opposite lobe, contradicting three-connectivity.  Therefore `|U_A|>=2`.
In the whole graph all exits lie in

\[
                 \{z\}\cup U_A\cup N_S(A).
\]

Deleting this set leaves both `A` and vertices of the opposite lobe and open
shore, so it is a genuine separator.  Seven-connectivity gives

\[
 1+|U_A|+|N_S(A)|\ge7,
 \qquad |N_S(A)|\ge6-|U_A|\ge3.
\]

The same holds for the other component `D`.  Also
`T\cup N_S(J)` separates `J` from the other lobe and opposite open shore,
so `|N_S(J)|>=4`.  Both allocations in (2.5) partition `J` into connected
sets, retain the preceding contact lower bounds, and have contact-set union
exactly `N_S(J)`.  Lemma 2.1 therefore applies exactly as stated.

## 3. Cut-duty exchange and its literal `K_7`

Under

\[
 i\in U_A,\qquad \{j,k\}\subseteq U_D,
\]

the four proposed carriers are

\[
          B_i\cup A,\qquad B_j,\qquad B_k,
          \qquad D\cup\{z\}.
\]

They are disjoint because the rooted bags partition subsets of `K\cup T`,
whereas `A,D,z` lie in `J`.  Connectivity uses `At_i`, the root
`t_i\in B_i`, and the `D-z` edge.  Their six adjacencies are:

| Pair | Literal witness |
|---|---|
| the three pairs among `B_i\cup A,B_j,B_k` | the rooted-triangle edges |
| `(B_i\cup A),(D\cup\{z\})` | an `A-z` edge |
| `B_j,(D\cup\{z\})` | a `D-t_j` edge |
| `B_k,(D\cup\{z\})` | a `D-t_k` edge |

Lemma 2.1 supplies distinct `a,b` outside
`F=\{p_j,p_k\}`.  Thus the four carriers receive four distinct literal
boundary representatives `a,p_j,p_k,b`.

For completeness, if `r_1,r_2,r_3` are the remaining boundary vertices and
`P_1,P_2,P_3` are the full packets, the packet bags are
`P_h\cup\{r_h\}`.  The 21 adjacencies are the six carrier adjacencies above,
12 packet--carrier edges `P_h-s` supplied by fullness, and three
packet--packet edges `P_h-r_l` supplied by fullness.  Hence Theorem 3.1 is a
literal `K_7` construction, not a palette-to-label lift.

## 4. Equal/crossed gate-support enumeration

Every support `U_A,U_D` is one of the three two-subsets of `T` or all of
`T`.

* If one support is `T`, the other either contains `i` or is `{j,k}`;
  orienting the two sides appropriately invokes Theorem 3.1.
* If the two supports are distinct two-sets and one is `{j,k}`, the other
  contains `i`, so Theorem 3.1 again applies.
* If the supports are equal to `T-\{g\}`, neither open component sees `t_g`.
  Since the whole lobe `J` sees every gate, the literal edge `zt_g` exists.
  Allocating `z` to the appropriate side gives one carrier side duty `i`
  and the other side duties `j,k`, so the same four-carrier construction
  applies.

The only surviving ordered support pairs are therefore

\[
    (\{i,j\},\{i,k\}),\qquad
    (\{i,k\},\{i,j\}).
\]

As a finite guardrail I enumerated all ordered pairs of two- or
three-element subsets of a three-set.  After applying the noncrossed and
equal-support closures, these were exactly the two survivors above.

The equal-support proof handles the gate edge at `z` correctly.  If `g=i`,
put `z` on the side assigned duty `i`.  If `g=j` or `g=k`, put `z` on the
side assigned the pair of outer duties.  In every case the relevant two
parts are connected and adjacent and retain the fresh-label hypotheses.

## 5. Nesting and global orientation

Order the cutvertices along the lobe's block--cutvertex path.  For
`h<ell`, the left component at the earlier cut is contained in the left
component at the later cut, and dually on the right:

\[
 A_h\subseteq A_\ell,
 \qquad D_\ell\subseteq D_h.
\]

More precisely, the carrier sets later used in Section 6 satisfy

\[
 A_h\cup\{z_h\}\subseteq A_\ell,
 \qquad D_\ell\cup\{z_\ell\}\subseteq D_h.
\]

Taking literal gate-neighbour sets preserves the first pair of inclusions.
Every support has order two, so inclusion forces equality.  The finite
classification from Section 4 then forces one fixed ordered pair of crossed
supports throughout the chain.  Reversal of the chain and interchange of
the two matched outer indices are harmless relabellings.  Formula (4.3)
follows literally: the first right tail has no `t_j` neighbour and the last
left tail has no `t_k` neighbour; a possible edge at the endpoint cutvertex
is retained by the displayed union with that cutvertex.

No local support is propagated through a model bag in this argument.  The
sets `U_A=N_T(A)` are raw literal gate contacts, so there is no hidden
palette-to-labelled-carrier inference.

## 6. Common-gate closure

For a crossed cut the four carriers in (5.2) are

\[
 X=A\cup\{z,t_j\},\quad
 Y=D\cup\{t_k\},\quad K,\quad \{t_i\}.
\]

They are disjoint and connected.  Their six pairwise adjacencies are:

| Pair | Literal witness |
|---|---|
| `X,Y` | a `z-D` edge |
| `X,K` | a `t_j-K` edge |
| `Y,K` | a `t_k-K` edge |
| `X,{t_i}` | an `A-t_i` edge |
| `Y,{t_i}` | a `D-t_i` edge |
| `K,{t_i}` | a `K-t_i` edge |

Their boundary-contact sets have lower bounds `3,3,4,1` as written
(indeed the crossed two-gate tails have the stronger lower bound four).
These bounds satisfy Hall for four sets.  A subfamily omitting the singleton
has union at least three, and if it contains all three nonsingleton sets its
union contains the four-set from `K`.  A subfamily containing the singleton
and one or two nonsingleton sets has union at least three, while the full
family again has union at least four.  An exhaustive check over all set
families on seven labels of exact lower-bound sizes `3,3,4,1` found no Hall
failure.

Thus four distinct literal boundary representatives exist.  With the three
packet bags, the same `6+12+3=21` adjacency audit from Section 3 applies.
Therefore `N_S(t_i)\ne\varnothing` really does force a literal `K_7`, and a
surviving common gate is literally `S`-unlabelled.  This conclusion does not
say that the colour corresponding to `i` is absent from any propagated
list state.

## 7. Exact raw list-state sweep

For each cut, the first allocation is

\[
 C_j^h=A_h\cup\{z_h,t_j\},\qquad
 C_k^h=D_h\cup\{t_k\},\qquad
 C_i=K\cup\{t_i\}.
\]

All three sets are nonempty, connected, disjoint, and together span `L`.
The first two are adjacent through `z_hD_h`; their adjacencies to `C_i`
are the literal `t_jK` and `t_kK` edges.  Thus the promoted
spanning-triangle list-state theorem applies without identifying palette
names with old model bags.

Every raw list is nonempty because the connected open shore `L` is
`S`-full.  Each palette symbol occurs in at least four raw lists:

* `j` occurs on `N_S(A_h)`, whose order is at least four because
  `|U_{A_h}|=2`;
* `k` occurs on `N_S(D_h)`, also of order at least four; and
* `i` occurs on `N_S(K)`, of order at least four because
  `T\cup N_S(K)` is an order-at-least-seven separator.

If the raw list instance is colourable, the carrier-list theorem creates
the same literal equality partition by contractions on the two opposite
shores and glues two six-colourings.  Hence, in a hypothetical counterexample,
each raw instance is uncolourable.

The stronger nesting displayed in Section 5 gives

\[
 C_j^h\subseteq C_j^\ell,qquad
 C_k^\ell\subseteq C_k^h\quad(h<\ell),
\]

while `C_i` is fixed.  Therefore the **raw** support of `j` is
nondecreasing, the raw support of `k` is nonincreasing, and the raw support
of `i` is fixed.  This is an exact contact statement.  It does not rely on
the uncolourability of one state to infer another; the counterexample
hypothesis and list-state theorem establish uncolourability independently at
every cut.

The alternative allocation (6.3) is also a valid spanning clique partition:
the `A-z` edge replaces `z-D` as the edge between the first two carriers.
Its raw lists may differ only through literal contacts of `z`, and it too is
uncolourable in a survivor.  The note correctly does **not** claim that
these alternative states form a nested sequence.

## 8. Trust boundary

The audited theorem proves a genuine infinite-family structural reduction:
all noncrossed block-chain cuts close, crossed duties have one global order,
and a surviving common gate has no literal boundary neighbour.  It also
manufactures a monotone sequence of exact **raw** uncolourable list
instances.

It does not prove that unit propagation is monotone along this sequence,
that the same critical list core survives at consecutive cuts, that an
implication bicycle has a fixed orientation, or that a coherent two-vertex
endgame exists.  Any subsequent operation-state theorem must establish one
of those assertions separately.
