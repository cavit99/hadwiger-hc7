# First-hit boundaries in an arbitrary atomic `H_0` subdivision

**Status:** written proof; separate internal audit GREEN.

This note generalizes the useful part of the finite shared-vertex
saturation from one thirteen-vertex graph to an arbitrary labelled
subdivision.  It proves an actual order-seven separator outcome and an
explicit `K_7` model when the two clean first-hit boundaries both attach
inside the common `fg` segment.  It also proves that one `T`-bridge cannot
join the clean `f`- and `g`-incident route stars in a `K_7`-minor-free
host.  The remaining case is stated as a one-sided bridge restriction
together with a normalized single-path interval trace;
it is not claimed to close the full atomic-collision theorem.

The proof uses the separately audited
[`cross-pair path closure`](hc7_atomic_h0_bridge_quadrant_normal_form.md#2-a-path-crossing-a-missing-pair-is-terminal).

## 1. Setup and first-hit regions

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},                 \tag{1.1}
\]

and let `T` be a labelled subdivision of `H_0` in a seven-connected graph
`G`.  Write `T_uv` for the subdivided segment corresponding to `uv`, and
for a vertex `z in V(T)` put

\[
 \sigma_T(z)=
 \begin{cases}
  \{r\},&z\text{ is the branch vertex }r,\\
  \{r,s\},&z\in\operatorname{int}(T_{rs}).
 \end{cases}                                             \tag{1.2}
\]

Fix distinct vertices

\[
 q\in\operatorname{int}(T_{ad}),\qquad
 q'\in\operatorname{int}(T_{bc}),\qquad
 h\in\operatorname{int}(T_{fg}),                       \tag{1.3}
\]

and suppose that the literal edges `eh,hx` belong to `G`.

Delete every vertex of `T` except `q`, and let `D_q` be the component
containing `q`.  Define `D_q'` analogously.  Put

\[
 \Omega_q=N_G(D_q),\qquad \Omega_{q'}=N_G(D_{q'}).       \tag{1.4}
\]

Because each `D` is a component after deleting the other vertices of `T`,

\[
 D_q\cap V(T)=\{q\},\quad
 D_{q'}\cap V(T)=\{q'\},\quad
 \Omega_q\subseteq V(T)-\{q\},\quad
 \Omega_{q'}\subseteq V(T)-\{q'\}.                     \tag{1.5}
\]

Every `u in Omega_q` is joined to `q` by a path whose only vertices in `T`
are its ends: take a path inside `D_q` from `q` to a neighbour of `u` and
then its last edge to `u`.  Thus `Omega_q` is exactly the clean first-hit
boundary visible from `q`; the same statement holds at `q'`.

A **`T`-path** is a path with distinct ends in `T` and no internal vertex
in `T`.  A **`T`-bridge** is either an edge outside `T` with both ends in
`T`, or a component of `G-V(T)` together with all of its incident edges to
`T`; its vertices in `T` are its attachments.

For `r in {a,b}` and `s in {c,d}`, let `T^{r,s}` denote the vertices whose
endpoint support omits both `r,s`, as in the audited bridge normal form.

## 2. Complementary quadrant confinement

### Lemma 2.1

If `G` has no `K_7` minor, then

\[
                   \Omega_q\subseteq T^{b,c},\qquad
                   \Omega_{q'}\subseteq T^{a,d}.        \tag{2.1}
\]

Moreover, each boundary has order at least seven.  If either has order
seven, it is the boundary of an actual order-seven separation in `G`.

#### Proof

Let `u in Omega_q` and choose the clean `q`--`u` path supplied after
(1.5).  Since `sigma_T(q)={a,d}`, the cross-pair path theorem gives a
`K_7` minor if `b in sigma_T(u)` or `c in sigma_T(u)`.  Under the stated
minor exclusion, `sigma_T(u)` omits both `b,c`, proving the first inclusion.
The second follows symmetrically: `sigma_T(q')={b,c}`, so an attachment
supported at `a` repairs `ab`, while one supported at `d` repairs `cd`.

The set `Omega_q=N_G(D_q)` separates `D_q` from every vertex of
`T-(Omega_q union {q})`.  The subdivision contains the eight branch
vertices and the three distinct internal vertices `q,q',h`; hence this
last set is nonempty whenever `|Omega_q|<=7`.  Seven-connectivity therefore
gives `|Omega_q|>=7`, and equality makes it a literal order-seven boundary.
More explicitly, in the equality case

\[
 \bigl(D_q\cup\Omega_q,\;V(G)-D_q\bigr)
\]

is a separation of order seven: its intersection is `Omega_q`, no edge
joins its two exclusive sides, and both exclusive sides are nonempty.  The
argument at `q'` is identical.  \(\square\)

### Lemma 2.2

If `G` has no `K_7` minor, then `D_q,D_q'` are disjoint and anticomplete.

#### Proof

An intersection, or an edge between the two connected sets, would give a
`q`--`q'` path whose internal vertices avoid `V(T)`.  Its endpoint supports
are `{a,d}` and `{b,c}`, so it crosses both absent pairs.  The cross-pair
path theorem would give a `K_7` minor.  \(\square\)

## 3. Two terminal clean-support configurations

### Theorem 3.1 (common-support matching closure)

Suppose

\[
 \Omega_q\cap\operatorname{int}(T_{fg})\ne\varnothing,
 \qquad
 \Omega_{q'}\cap\operatorname{int}(T_{fg})\ne\varnothing. \tag{3.1}
\]

Then `G` contains an explicit `K_7` minor.

#### Proof

Assume otherwise, so Lemma 2.2 applies.  Choose

\[
 u\in\Omega_q\cap\operatorname{int}(T_{fg}),\qquad
 v\in\Omega_{q'}\cap\operatorname{int}(T_{fg}).         \tag{3.2}
\]

Let `R` be a clean `q`--`u` path with its interior in `D_q-{q}`, and let
`R'` be the analogous `q'`--`v` path.  The two paths are disjoint except
possibly when `u=v`, because their interiors lie in the disjoint
anticomplete sets from Lemma 2.2.

Let `I` be the minimal subpath of `T_fg` containing `h,u,v`.  All three
vertices are internal on `T_fg`, so `I` contains neither `f` nor `g`.
Define the following seven initial branch sets:

\[
\begin{aligned}
 H={}&V(R)\cup V(I),\\
 B={}&(V(R')-\{v\})\cup V(T_{bq'}),\\
 A={}&V(T_{ag})\cup\bigl(V(T_{aq})-\{q\}\bigr),\\
 D={}&V(T_{qd})-\{q\},\\
 C={}&\bigl(V(T_{q'c})-\{q'\}\bigr)\cup V(T_{cx}),\\
 E={}&\{e\},\\
 F={}&V(T_{fw})-\{w\},
\end{aligned}                                             \tag{3.3}
\]

where `w` is the first vertex of `I` encountered from `f` along `T_fg`.
Thus `F` is the `f`-side component of `T_fg-V(I)`, together with `f`.
Here `T_fw` is the `f`--`w` subpath of `T_fg`.  The notation
`T_aq,T_qd,T_bq',T_q'c` similarly means the indicated subpaths of the two
marked segments.

These sets are pairwise disjoint.  The only vertices of `R` and `R'`
outside their ends lie outside `T`, and Lemma 2.2 separates their two
owners.  The displayed subpaths of `T` lie on internally disjoint segments,
apart from their stated common endpoints, which were removed from exactly
one side.  The interval `I` avoids `f,g`, and its only possible common
vertex with `R'` is the removed endpoint `v`.

Every set is connected.  For `B`, the path `R'-v` contains `q'` and meets
the path `T_bq'` there.  The other claims are immediate from (3.3).

Allocate every still-unused internal vertex of a segment of `T` to a bag
containing one of that segment's ends.  On `T_fg`, allocate the unused
`g`-side component to `A`.  Each allocation attaches a path at an existing
bag vertex, preserves connectedness and disjointness, and leaves the last
edge of the segment as the required inter-bag contact.

The bag `H` is adjacent to all six others as follows:

\[
 HE:he,\quad HF:T_{fg}\text{ at }w,\quad
 HA:T_{ad}\text{ at }q,\quad HB:R'\text{ at }v,\quad
 HD:T_{ad}\text{ at }q,\quad HC:hx.                    \tag{3.4}
\]

Among the other six bags, one contact for every pair is

\[
\begin{array}{lllll}
 EF:T_{ef},&EA:T_{ea},&EB:T_{eb},&ED:T_{ed},&EC:T_{ec},\\
 FA:T_{fa},&FB:T_{fb},&FD:T_{fd},&FC:T_{fc},\\
 AB:T_{gb},&AD:T_{gd},&AC:T_{ax},\\
 BD:T_{bd},&BC:T_{bc}\text{ at }q',\\
 DC:T_{dx}.&&&&
\end{array}                                               \tag{3.5}
\]

All contacts in (3.4)--(3.5) are literal edges or surviving boundary edges
of the named subdivided segments.  Hence `H,B,A,D,C,E,F` are seven disjoint
connected pairwise adjacent sets, an explicit `K_7`-minor model.  This is
the desired contradiction.  \(\square\)

The proof permits `u=v`.  In that case `R'-v` and `H` are still disjoint,
and the last edge of `R'` supplies the `BH` contact.

Put

\[
 \begin{aligned}
  \mathcal S_f={}&\operatorname{int}(T_{fh})\cup
       \bigcup_{u\in\{a,b,c,d,e\}}\operatorname{int}(T_{fu}),\\
  \mathcal S_g={}&\operatorname{int}(T_{hg})\cup
       \bigcup_{v\in\{a,b,c,d,e\}}\operatorname{int}(T_{gv}),
 \end{aligned}                                           \tag{3.6}
\]

where `T_fh,T_hg` are the two subpaths into which `h` splits `T_fg`.
These are the open subdivided route stars visible from `f` and `g`, with
only the appropriate side of `T_fg` included in each.

### Theorem 3.2 (clean-root-star bridge closure)

If a `T`-path `Q` has one end \(p\in\mathcal S_f\) and the other end
\(r\in\mathcal S_g\), then \(T\cup Q\cup\{eh,hx\}\) contains an explicit
`K_7` minor.

#### Proof

There are unique labels

\[
 u\in\{a,b,c,d,e,g\},\qquad
 v\in\{a,b,c,d,e,f\}                                  \tag{3.7}
\]

such that \(p\in\operatorname{int}(T_{fu})\) and
\(r\in\operatorname{int}(T_{gv})\).  In the exceptional choice `u=g`,
the point `p` lies on `T_fh`; in the exceptional choice `v=f`, the point
`r` lies on `T_hg`.

Choose an edge `yz` of `Q`, oriented so that `y` is on the `p`-side and
`z` is on the `r`-side.  Start seven bags as follows:

- `A` contains the whole path `T_ac`, and hence both `a,c`;
- `E={e}`, `B={b}`, and `D={d}`;
- `F` contains `T_fp`, the `p`--`y` part of `Q`, and, when `u` is not `g`,
  `T_fh-h`;
- `G` contains `T_gr`, the `z`--`r` part of `Q`, and, when `v` is not `f`,
  `T_hg-h`; and
- `X` contains `x,h`, together with `T_ph-p` when `u=g` and `T_hr-r`
  when `v=f`.

Here every named path is viewed as its vertex set.  Each bag is connected.
The only possible equality of an `f`-incident and a `g`-incident segment
is the segment `T_fg`; in that case `p,h,r` occur in this order.  The
displayed convention partitions that segment into an `F`-part, an
`X`-part, and a `G`-part.  Since the interior of `Q` avoids `T` and the
edge `yz` is omitted from both path parts, the seven bags are pairwise
disjoint.

If `u` is not `g`, allocate `T_pu-p` to the bag containing `u`; if `v` is
not `f`, allocate `T_rv-r` to the bag containing `v`.  Thus the far suffix
of each cut segment is attached to its labelled endpoint.  Allocate every
still unused segment interior to a bag containing one of its ends.  These
allocations preserve connectedness and disjointness, while a boundary edge
of every allocated segment preserves the contact between its two endpoint
bags.

The bag `X` meets the other six bags through

\[
 XE:eh,\quad XA:T_{xa},\quad XB:T_{xb},\quad XD:T_{xd},
 \quad XF:T_{fh},\quad XG:T_{hg}.                       \tag{3.8}
\]

For `XF` or `XG`, the contact is the boundary edge at `p` or `r` in the
exceptional case, and the boundary edge at `h` otherwise.  Among the
remaining six bags, the following routes give all fifteen contacts:

\[
\begin{array}{lllll}
 EA:T_{ea},&EB:T_{eb},&ED:T_{ed},&EF:T_{ef},&EG:T_{eg},\\
 AB:T_{cb},&AD:T_{ad},&AF:T_{af},&AG:T_{ag},\\
 BD:T_{bd},&BF:T_{bf},&BG:T_{bg},\\
 DF:T_{df},&DG:T_{dg},\\
 FG:yz.&&&&
\end{array}                                             \tag{3.9}
\]

Every named core route exists in `H_0`; the only new contact is the edge
`yz` of `Q`.  Hence `X,E,A,B,D,F,G` are seven disjoint connected pairwise
adjacent sets, as required.  \(\square\)

### Corollary 3.3 (one-sided bridge support)

If `G` has no `K_7` minor, no `T`-bridge has both an attachment in
\(\mathcal S_f\) and an attachment in \(\mathcal S_g\).

#### Proof

An edge bridge with such attachments is itself a `T`-path.  For a bridge
arising from a component of `G-V(T)`, a path through that component between
the two attachments is a `T`-path.  Theorem 3.2 applies in either case.
\(\square\)

## 4. The exact first-hit normal form

### Theorem 4.1

Under the setup of Section 1, at least one of the following holds.

1. `G` contains a `K_7` minor.
2. `G` has an actual order-seven separator.  In particular, this occurs
   if `Omega_q` or `Omega_q'` has order seven.
3. After possibly interchanging the two marked roots and simultaneously
   interchanging `(a,d)` with `(b,c)`, all of the following hold:

   \[
   \begin{gathered}
    |\Omega_q|\ge8,\qquad |\Omega_{q'}|\ge8,\\
    \Omega_q\subseteq T^{b,c},\qquad
    \Omega_{q'}\subseteq T^{a,d},\\
    D_q\cap D_{q'}=\varnothing,qquad E_G(D_q,D_{q'})=\varnothing,\\
    \Omega_{q'}\cap\operatorname{int}(T_{fg})=\varnothing.
   \end{gathered}                                         \tag{4.1}
   \]

   In addition, every `T`-bridge `B` is one-sided with respect to the two
   clean route stars:

   \[
    \operatorname{Att}(B)\cap\mathcal S_f=\varnothing
    \quad\hbox{or}\quad
    \operatorname{Att}(B)\cap\mathcal S_g=\varnothing.  \tag{4.2}
   \]

#### Proof

Assume outcomes 1 and 2 fail.  Lemmas 2.1 and 2.2 give every assertion in
(4.1) except the last.  Theorem 3.1 says that the two boundaries cannot
both meet `int(T_fg)`.  Interchange the two marked roots if necessary so
that `Omega_q'` is the one which misses that interval.  Corollary 3.3 gives
(4.2).  \(\square\)

This is a first-hit statement, not merely an attachment count.  If `P'` is
any `q'`--`h` path whose internal vertices avoid the eight branch vertices
of `T` and avoid `q`, let `z` be its first vertex of `T` after `q'`.  Then
the initial `q'`--`z` subpath is clean, so

\[
                  z\in\Omega_{q'}\subseteq T^{a,d}.      \tag{4.3}
\]

In outcome 3, it also satisfies

\[
                  z\notin\operatorname{int}(T_{fg}).    \tag{4.4}
\]

Thus every such path meets `T` outside `T_fg` before it reaches the common
vertex `h`.  This is the exact unresolved ownership event.

No existence assertion for `P'` is hidden here.  If there is no such path,
then

\[
                 Z=\{a,b,c,d,e,f,g,x,q\}               \tag{4.5}
\]

separates `q'` from `h`.  An inclusion-minimal `q'`--`h` separator contained
in `Z` has order seven, eight, or nine, by seven-connectivity.  Thus failure
of path existence is itself a precise bounded-separation residue.  After
outcome 2 of Theorem 4.1 has been excluded, its order is eight or nine.

## 5. Canonical interval representation of the dirty residue

Let `M` consist of the eight branch vertices together with `q,q',h`.
On each segment of `T`, list its vertices from `M` in route order.  The
subpaths between consecutive listed vertices are the **elementary
intervals**.  This definition includes a single edge whose two ends both
belong to `M`.

### Lemma 5.1 (interval normalization)

Let `P` be a path with ends in `M` whose internal vertices avoid any
specified subset of `M`.  There is a path with the same ends and the same
avoidance property such that its intersection with every elementary
interval is empty or a connected subpath.

#### Proof

Choose such a path minimizing the total number of connected components of
its intersections with the elementary intervals.  If its intersection
with one elementary interval `J` is disconnected, let `r,s` be respectively
the first and last vertices of `J` encountered along the path.  Replace the
path section from `r` to `s` by the unique `r`--`s` subpath of `J`.

The new section contains no vertex of `M` internally, because `J` has no
marked vertex in its interior.  The prefix before `r` and suffix after `s`
avoid `J` by their choice, so the replacement is again a simple path.  It
introduces no new vertex in another elementary interval.  Nor can deleting
the replaced section split one connected intersection with another
interval: two distinct elementary intervals have disjoint interiors and
at most one common marked endpoint.  Thus the number of intersection
components for every other interval does not increase, while the
intersection with `J` becomes connected.  This contradicts minimality.
\(\square\)

Consequently, whenever a path `P'` considered above exists, it may be chosen
with a finite interval trace: at most one interval on each elementary part
of `T`.  Combining this with (4.1)--(4.5), and after excluding outcomes 1
and 2 of Theorem 4.1, the sole residue is the following canonical form:

- two anticomplete connected first-hit regions have at least eight literal
  attachments each in the complementary quadrants `T^{b,c}` and `T^{a,d}`;
- one region has no attachment in the interior of `T_fg`; and
- no single `T`-bridge has attachments in both clean route stars; and
- either a separator of order eight or nine contained in `Z` blocks
  all branch-avoiding paths from that root to `h`, or a normalized such path
  first meets `T` again outside `T_fg` and has at most one connected
  intersection on each elementary interval.

This interval trace is not itself declared terminal.  A subsequent theorem
must analyze how successive one-sided bridge excursions and subpaths of `T`
combine, and either decode them into a crossing support or produce a
response-bearing separation.  In particular, (4.2) rules out a direct
transition inside one bridge.  The present theorem proves neither a chain
decomposition nor laminarity of the remaining attachment intervals.

## 6. Impact and trust boundary

Theorem 4.1 genuinely advances the terminal disjunction in two ways: it
returns an actual order-seven separator whenever one is exposed here,
and it closes every configuration with one clean internal `T_fg` contact
from each marked root.  It also closes every individual bridge joining the
clean `f`- and `g`-route stars, and strengthens the remaining dirty case
by a one-sided bridge restriction and a normalized single-path interval
trace.

It does **not** prove that the separator carries compatible proper-minor
colourings, it does not improve the possible order-eight or order-nine
separator in (4.5), and it does not close the one-sided single-path residue.
No laminar bridge decomposition, global collision descent, or same-form
reduction is claimed.

A possible next structural input is Hayashi and Kawarabayashi,
[*Rooted topological minors on four vertices*](https://doi.org/10.1016/j.jctb.2021.05.002),
J. Combin. Theory Ser. B **158** (2023), 146--185.  Their Theorem 5.3
characterizes the absence of a diamond on four prescribed vertices under
a three-fan hypothesis by four obstruction types.  It is not a bare
`diamond-or-web` theorem, and a use here would still have to prove that the
rooted subdivision avoids, or consistently absorbs, the literal `T`
corridors owned by the seven branch sets.  The present result does not
invoke that characterization.
