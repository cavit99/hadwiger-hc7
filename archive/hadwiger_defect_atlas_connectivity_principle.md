# A label-free defect-atlas principle for full shores

## 1. Quotient obstruction family

Fix integers `k>=2` and `lambda>=1`.  Let `J` be a graph on a boundary
set `S`.  For two sets `L_1,L_2 subseteq S` with
`L_1 union L_2=S`, define

\[
 Q_k(J;L_1,L_2)
\]

on `S union {x,y,h}` by retaining `J`, adding `xy`, making `h`
complete to `S`, making `x` adjacent precisely to `L_1` in `S`, and
making `y` adjacent precisely to `L_2` in `S`.  Put

\[
 \mathcal B_k(J)=\{(L_1,L_2):
       \eta(Q_k(J;L_1,L_2))<k\}.                    \tag{1.1}
\]

This is the **bad-split family** of `J`.  It is downward closed in the
two contact coordinates, subject to their union remaining `S`.

Define its balanced-contact width by

\[
 \beta_k(J)=
 \max_{(L_1,L_2)\in\mathcal B_k(J)}
       \min\{|L_1|,|L_2|\},                         \tag{1.2}
\]

with value `-infinity` if the bad family is empty.

## 2. Lifting a positive quotient

### Lemma 2.1

Let `G` contain a boundary `S`, two disjoint anticomplete connected full
shores `D,D'`, and a connected bipartition

\[
 D=X\mathbin{\dot\cup}Y
\]

with an `X-Y` edge.  Put `J=G[S]` and
`L_X=N_S(X), L_Y=N_S(Y)`.  If

\[
 (L_X,L_Y)\notin\mathcal B_k(J),                    \tag{2.1}
\]

then `G` contains a `K_k` minor.

### Proof

Contract `X,Y,D'` to `x,y,h`.  Connectivity makes the contractions
valid; the `X-Y` edge gives `xy`; fullness makes `h` complete to `S`;
and the two other contact rows are exactly `L_X,L_Y`.  Thus
`Q_k(J;L_X,L_Y)` is a minor of `G`, and (2.1) lifts its `K_k` model.

## 3. Global connectivity becomes internal shore connectivity

### Theorem 3.1 (defect-atlas connectivity transfer)

Suppose `G` is `lambda`-connected and has no `K_k` minor, while `S` and
the two shores satisfy Lemma 2.1.  Put `beta=beta_k(G[S])`.  Then no
shore has a separating vertex set of order

\[
 w<\lambda-\beta.                                   \tag{3.1}
\]

Equivalently, apart from the usual complete-small-graph convention, each
shore is internally `(lambda-beta)`-connected.

### Proof

Suppose `W subset D`, `|W|=w`, and `D-W` has distinct components
`C_1,C_2`.  For any component `C` of `D-W`,

\[
 N_G(C)\subseteq W\cup N_S(C).
\]

The opposite shore lies outside this set, so `lambda`-connectivity gives

\[
 |N_S(C)|\ge\lambda-w.                              \tag{3.2}
\]

Contract every component of `D-W` to one vertex in an auxiliary graph
whose other vertices are `W`.  Choose a spanning tree of that connected
auxiliary graph and delete an edge on the tree path between the vertices
representing `C_1,C_2`.  Lifting the two tree components partitions `D`
into connected adjacent sets `X,Y`, one containing `C_1`, the other
`C_2`.  By (3.2),

\[
 |N_S(X)|,|N_S(Y)|\ge\lambda-w>\beta.
\]

Their contact pair cannot belong to the bad family by (1.2).  Lemma 2.1
then gives a `K_k` minor, a contradiction.

### Corollary 3.2

If every maximal member of `mathcal B_k(J)` has one contact coordinate
of order at most `q`, then, apart from complete shores of order below
`lambda-q`, every full shore has no separator of order below
`lambda-q`.

This is the abstract mechanism behind the complete `2K3+K1` closure:
there `k=lambda=7`, every maximal bad pair is a full row opposite a
three-vertex cross-triangle, so `beta=3` and every surviving shore is
4-connected.  For `C6+K1`, balanced bad pairs of size `5|5` give
`beta=5`; the same theorem yields exactly 2-connectivity and explains,
without labels, why an additional portal-order invariant is needed.

## 4. Local portal-row transfer

For an integer `r>=1`, define

\[
 \Lambda_r(J)=\{L\subseteq S:\ 
   (L,R)\in\mathcal B_k(J)
   \text{ for some }R\subseteq S\text{ with }|R|\ge\lambda-r\}.
                                                               \tag{4.1}
\]

### Theorem 4.1 (connected-set portal locality)

Under the hypotheses of Theorem 3.1, let `X` be a nonempty connected
proper subset of a shore such that `D-X` is connected.  If `|X|<=r`,
then

\[
 N_S(X)\in\Lambda_r(J).                              \tag{4.2}
\]

### Proof

The set `X union N_S(D-X)` separates `D-X` from the opposite shore, so

\[
 |N_S(D-X)|\ge\lambda-|X|\ge\lambda-r.             \tag{4.3}
\]

The connected bipartition `X,D-X` cannot have a positive quotient by
Lemma 2.1.  Its first contact row therefore belongs to (4.1).

The theorem turns a finite or structural classification of maximal bad
splits into restrictions on every vertex, edge, or small connected set
of a highly connected shore.  In the `2K3+K1` boundary, `Lambda_1`
consists of subsets of cross-triangles; distinct same-part portal classes
consequently become disjoint.  Applying `Lambda_2` to an edge makes those
classes anticomplete.  Two-connectivity already packages three distinct
portals into a rooted triangle.  In the `C6+K1` boundary, `Lambda_1`
contains additional balanced singleton/cycle-neighbour locks; their cyclic
compatibility is the exact next obstruction.

## 5. Uniform research target

The preceding results suggest a boundary theorem independent of any
seven-vertex labels:

> **Bad-split compatibility target.**  For a counterexample-derived
> boundary `J`, either `beta_k(J)` is small enough that Theorem 3.1 and
> portal locality produce an `S`-meeting rooted clique model, or the
> balanced maximal members of `mathcal B_k(J)` admit a laminar/web
> decomposition across which the two proper-minor colourings can be
> aligned.

This target is strictly stronger than continuing an edge-count atlas:
the atlas supplies only the downward-closed family `mathcal B_k(J)`;
the proof obligation is the uniform dichotomy between rooted model and
colour-gluable decomposition.

## 6. A Helly bound for the components behind a minimum shore cut

It is useful to state one further consequence without boundary labels.
Write

\[
 \mathcal D_k(J)=\{(S-L_1,S-L_2):(L_1,L_2)\in
 \mathcal B_k(J)\}                                  \tag{6.1}
\]

for the corresponding family of **bad defect pairs**.  Its two
coordinates are disjoint.

### Theorem 6.1 (defect--Helly component bound)

Assume `|S|=lambda`, and let `D` be an internally `r`-connected full
shore in the setting of Theorem 3.1.  Let `Z subseteq D`, `|Z|=r`, and suppose that `D-Z` has
components `C_1,...,C_m`.  Assume that every member `(A,B)` of
`mathcal D_k(J)` with `|A|,|B|<=r` has `A,B` both nonempty.  Then

\[
 m\le r+1.                                           \tag{6.2}
\]

#### Proof

Put

\[
 A_i=S-N_S(C_i),\qquad R=S-N_S(Z).
\]

Global `lambda`-connectivity gives `|A_i|<=r`, because
`Z union N_S(C_i)` separates `C_i` from the opposite shore.  Internal
`r`-connectivity implies that every component of `D-Z` has a neighbour
at every vertex of `Z`; otherwise `Z-z` would be a smaller separator.
Hence `D-C_i` is connected (there is at least one other component), and
`C_i mid (D-C_i)` is a connected bipartition.  The defect on its second
side is exactly

\[
 E_i=R\cap\bigcap_{j\ne i}A_j.                       \tag{6.3}
\]

Both split defects have order at most `r`; hence the hypothesis on the
bad family gives `E_i ne empty` for every `i`.  Fullness of `D` gives

\[
 R\cap\bigcap_i A_i=\varnothing.                    \tag{6.4}
\]

Choose `x_i in E_i`.  Equation (6.4) implies `x_i notin A_i`, while
`x_i in A_j` whenever `j ne i`.  The witnesses `x_i` are distinct:
if `x_i=x_j` with `i ne j`, membership in `A_i` forced by the witness
for `j` contradicts `x_i notin A_i`.  Thus each `A_j` contains the
`m-1` distinct elements `x_i`, `i ne j`.  Since `|A_j|<=r`, we get
`m-1<=r`, proving (6.2).  \(\square\)

There is a useful exact equality refinement.  Define the compatibility
graph `Gamma_r(J)` on `S` by joining distinct `u,v` when some low-defect
bad pair `(A,{u})` has `v in A` and `|A|<=r` (symmetrise this relation).
If equality `m=r+1` holds in (6.2), then

\[
 A_i=\{x_j:j\ne i\}.                                \tag{6.5}
\]

Whenever the low-defect atlas forces the second coordinate in (6.3) to
be the singleton `{x_i}`, it follows that the witness set
`{x_1,...,x_{r+1}}` is a clique of `Gamma_r(J)`.  Consequently

\[
 \omega(\Gamma_r(J))\le r
 \quad\Longrightarrow\quad m\le r.                 \tag{6.6}
\]

For the `C6+K1` boundary and `r=2`, the singleton/pair rows of the exact
atlas are precisely

\[
 \{v\}\mid N_{C_6}(v)
\]

and their reversals.  Thus the equality compatibility graph is the
missing cycle `C_6`, which is triangle-free.  Formula (6.6) recovers,
without using the numerical labels, the sharp fact that every two-cut
of a surviving shore has exactly two components.  This is the first
nontrivial instance of the general programme in Section 5: a finite bad
atlas is converted into a Helly/compatibility obstruction rather than
left as a list of quotient cases.
