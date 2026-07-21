# Landing-star closure in an arbitrary two-bridge subdivision

**Status:** written proof; separate internal audit GREEN.

This note strengthens the arbitrary-subdivision part of the exact two-bridge
seven-fan theorem.  The two clean paths used by its final `K_7` model need
not be disjoint: their union belongs to one branch set.  Consequently one
connected first-hit region meeting both of two explicit open subdivided
stars already closes.  In a `K_7`-minor-free host, the entire subdivided
star at `e` or the entire subdivided star at `x` is therefore invisible from
the marked first-hit region.  If its boundary has order at most nine in a
hypothetical minor-minimal counterexample to `HC_7`, it already contains a
literal full response interface.

The theorem does not close the remaining large one-star-avoidance case.

## 1. Setup and landing regions

Let `C` be the thirteen-vertex graph from the exact-core seven-fan theorem.
Thus `C` is obtained from

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

by replacing

\[
 fa,ga,fg,ac
 \quad\text{with}\quad
 f-p-a,\ g-q-a,\ f-h-g,\ a-r-s-c
\]

and adding `eh,hx,pr,sq`.  Let `K` be an arbitrary subdivision of `C` in
a seven-connected graph `G`, retaining the thirteen labels.  For an edge
`uv` of `C`, write
`K_uv` for its subdivided path in `K`.

Define the two landing regions

\[
\begin{aligned}
 X^\circ={}&\{x\}\cup\operatorname{int}(K_{ax})
                    \cup\operatorname{int}(K_{cx}),\\
 E^\circ={}&\{e\}\cup\operatorname{int}(K_{ae})
                    \cup\operatorname{int}(K_{ce})
                    \cup\operatorname{int}(K_{eg}).       \tag{1.1}
\end{aligned}
\]

Delete `V(K)-{q}` and let `D_q` be the component containing `q`.  Put

\[
                         \Omega_q=N_G(D_q).                \tag{1.2}
\]

Then `D_q intersect V(K)={q}` and `Omega_q` is a subset of
`V(K)-{q}`.  Every `z in Omega_q` has a path from `q` to `z` whose only
vertices in `K` are its ends: take a path in `D_q` to a neighbour of `z`
and append its last edge.

## 2. A connected region meeting both stars is terminal

### Theorem 2.1 (landing-star closure)

If

\[
                 \Omega_q\cap X^\circ\ne\varnothing,
        \qquad   \Omega_q\cap E^\circ\ne\varnothing,     \tag{2.1}
\]

then `G` contains an explicit `K_7` minor.

#### Proof

Choose `z_x in Omega_q intersect X^circ` and
`z_e in Omega_q intersect E^circ`.  Let `Q_x,Q_e` be the clean paths
supplied after (1.2).  Their interiors may intersect; this causes no
conflict below because both paths are allocated to the same branch set.

Let `L_x` be the `z_x`--`x` subpath of `K_ax` or `K_cx` containing `x`;
when `z_x=x`, put `L_x={x}`.  Define `L_e` analogously as the
`z_e`--`e` subpath of the appropriate path among `K_ae,K_ce,K_eg`, with
`L_e={e}` when `z_e=e`.  Start seven bags as follows:

\[
\begin{aligned}
 X={}&V(Q_x)\cup\bigl(V(Q_e)-\{z_e\}\bigr)\cup V(L_x),\\
 A={}&V(K_{ap})\cup V(K_{pr})\cup V(K_{rs})\cup V(K_{sc}),\\
 B={}&\{b\},\qquad D=\{d\},\qquad E=V(L_e),\\
 F={}&V(K_{fh}),\qquad G_0=\{g\}.                         \tag{2.2}
\end{aligned}
\]

Here the union defining `A` is the subdivided path
`a-p-r-s-c`.  All seven sets are connected.  They are pairwise disjoint:
the interiors of `Q_x,Q_e` lie outside `K`; their only possible mutual
intersections are deliberately placed in `X`; the two landing regions use
distinct core edges; and each landing suffix omits the other labelled end
of its core edge.

Allocate every still-unused internal vertex of a subdivided core edge to a
bag containing one of that edge's labelled ends.  If the ends lie in
different bags, allocate the two sides so that one boundary edge remains
between those bags.  On an edge containing `z_x` or `z_e`, retain the
already prescribed landing suffix and allocate the complementary side to
the bag containing the other labelled end.  These allocations preserve
connectivity and disjointness.

Let `y` be the predecessor of `z_e` on `Q_e`; if `Q_e` is the single edge
`qz_e`, then `y=q`.  One contact for each pair involving `X` is

\[
 XA:K_{qs},\quad XB:K_{xb},\quad XD:K_{xd},\quad
 XE:yz_e,\quad XF:K_{xh},\quad XG_0:K_{qg}.             \tag{2.3}
\]

Here a named subdivided core edge means its retained boundary edge after
the allocation above.  The fifteen contacts among the other six bags are

\[
\begin{array}{lllll}
 AB:K_{cb},&AD:K_{ad},&AE:K_{ae},&AF:K_{pf},&AG_0:K_{cg},\\
 BD:K_{bd},&BE:K_{be},&BF:K_{bf},&BG_0:K_{bg},\\
 DE:K_{de},&DF:K_{df},&DG_0:K_{dg},\\
 EF:K_{ef},&EG_0:K_{eg},\\
 FG_0:K_{hg}.&&&&                                      \tag{2.4}
\end{array}
\]

If `z_e` lies on `K_ae` or `K_eg`, the corresponding entry in (2.4) is
exactly the boundary edge left by the landing split.  Every other entry is
an unchanged subdivided core edge.  Thus the seven sets in (2.2) are
pairwise adjacent and form an explicit `K_7`-minor model.  \(\square\)

## 3. One complete subdivided star is avoided

For a labelled vertex `v` of `C`, define its open subdivided star by

\[
 \operatorname{St}_K(v)=\{v\}\cup
   \bigcup_{vw\in E(C)}\operatorname{int}(K_{vw}).       \tag{3.1}
\]

### Corollary 3.1 (star-avoidance normal form)

Suppose `G` has no `K_7` minor.  Then

\[
       \Omega_q\cap\operatorname{St}_K(x)=\varnothing
 \quad\text{or}\quad
       \Omega_q\cap\operatorname{St}_K(e)=\varnothing. \tag{3.2}
\]

#### Proof

The exact-core seven-fan theorem proves that `Omega_q` avoids the five
terminal labels

\[
                         U=\{b,d,f,h,p\}                 \tag{3.3}
\]

and every internal point of a subdivided core edge incident with a member
of `U`.  The neighbours of `x` in `C` are `a,b,c,d,h`.  Hence every part
of `St_K(x)` outside `X^circ` lies on an edge incident with `b,d`, or `h`
and is already excluded.  Similarly, the neighbours of `e` in `C` are
`a,b,c,d,f,g,h`; every part of `St_K(e)` outside `E^circ` lies on an edge
incident with `b,d,f`, or `h`.

If neither alternative in (3.2) held, `Omega_q` would meet both regions in
(1.1), and Theorem 2.1 would give a `K_7` minor.  \(\square\)

## 4. A minimum separator of order at most nine carries the full response

### Theorem 4.1 (first-hit response dichotomy)

Assume the established case `HC_5` and

\[
 \kappa(G)\ge7,\qquad \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{4.1}
\]

Then one of the following holds.

1. There is an actual separation with boundary `S subseteq Omega_q` of
   order seven, eight, or nine.  The two distinguished components are full
   to `S`, the graph `G[S]` is four-colourable, and both closed shores have
   every exact independent-block response and the selected entrance-edge
   responses of the audited full response-boundary theorem.
2. Every `q`--`b` separator contained in the first-hit boundary has order
   at least ten, and the boundary avoids one whole subdivided star:

   \[
    \min\{|S|:S\subseteq\Omega_q\text{ separates }q\text{ from }b\}\ge10,
    \qquad
    \Omega_q\cap\operatorname{St}_K(x)=\varnothing
    \quad\hbox{or}\quad
    \Omega_q\cap\operatorname{St}_K(e)=\varnothing.    \tag{4.2}
   \]

Every vertex of `S` in outcome 1 is a literal first-hit vertex on the
eight-vertex route skeleton from the exact-core theorem.

#### Proof

Corollary 3.1 gives the star-avoidance alternative in every `K_7`-minor-free
case.  The terminal certificate at `q` gives `b notin Omega_q`.  Since
`Omega_q=N_G(D_q)`, the set `Omega_q` separates the literal vertex `q` from
the literal vertex `b`.  Among all `q`--`b` separators contained in
`Omega_q`, choose one of minimum cardinality,

\[
                              S\subseteq\Omega_q.       \tag{4.3}
\]

If `|S|>=10`, outcome 2 follows.  Otherwise `S` is inclusion-minimal, so
apply the audited full response-boundary theorem with containing separator
`Z=S`.  Seven-connectivity and the upper bound give
`7<=|S|<=9`; that theorem supplies fullness of the two distinguished
components, four-colourability of `G[S]`, the exact independent-block
responses on both closed shores, and the selected entrance-edge responses.
Finally, `S subseteq Omega_q subseteq V(K)-{q}` preserves every boundary
vertex literally, and the exact-core theorem confines it to the stated
route skeleton.  This is outcome 1.  \(\square\)

## 5. Exact gain and trust boundary

The earlier arbitrary-subdivision theorem required two internally disjoint
clean paths to the literal vertices `e,x` for this model.  Theorem 2.1
removes both restrictions: the paths may intersect arbitrarily in their
common connected first-hit region, and their endpoints may lie anywhere on
the five displayed landing arms.  The surviving case avoids every internal
point and the centre of one complete subdivided star, not merely the two
literal endpoints.

Theorem 4.1 chooses a minimum-cardinality `q`--`b` separator contained in
`Omega_q` and returns that separator to the audited response machinery when
its order is at most nine.  In the exact unresolved case, every such
separator has order at least ten, and `Omega_q` avoids the centre and every
internal route vertex of one complete subdivided star.  Seven-connectivity
alone has not yet forced
the first-hit region to meet both stars.  A path from `q` to the avoided star
can traverse other labelled vertices or core-route intervals, and putting
those vertices in the common branch set can destroy one of the contacts in
(2.4).  Thus the surviving one-star-avoidance case is a precise dirty-path
ownership obstruction, not yet a bounded response interface or strict
same-form reduction.

## 6. Audited dependencies

- [exact two-bridge core seven-fan closure](hc7_atomic_two_bridge_exact_core_seven_fan_closure.md)
- [full response boundary for small separators](hc7_atomic_path_absence_response_boundary.md)
