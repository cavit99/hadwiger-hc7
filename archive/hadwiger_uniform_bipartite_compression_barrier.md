# Uniform bipartite compression: theorem and exact rooted barrier

## Status

This note proves the arbitrary-palette version of bipartite compression and
then audits what it can and cannot buy in a uniform proof of Hadwiger's
conjecture.

The positive statement is completely elementary.  If a connected induced
bipartite set is contracted in a non-`r`-colourable graph and the resulting
minor is `r`-coloured, then the external portals of **each** parity class are
colourful in every selected palette slice.  In particular, they are
colourful in the `(r-2)`-colour slice.

The negative conclusion is equally precise.  The fixed sliced pair
`(J,X)` carries exactly the premise of Strong Hadwiger and no hidden extra
information.  Moreover, even if the ambient graph is required to be
proper-minor-minimal non-`r`-colourable, the construction contains as a
special case an arbitrary contraction-critical instance of ordinary
Hadwiger.  Thus a uniform rooted-clique conclusion cannot be declared an
easy consequence of the compression data: it contains the original
Hadwiger obstruction.

Throughout, a set `X` is **p-colourful** in a `p`-colourable graph `J` if
every proper colouring of `J` from a fixed `p`-element palette uses every
palette colour on `X`.

## 1. The arbitrary-palette compression theorem

### Theorem 1.1 (uniform parity colourfulness)

Let `r >= 2`.  Let `G` have no proper `r`-colouring, and let `T` be a
nontrivial connected induced bipartite subgraph of `G`, with fixed
bipartition

\[
                       V(T)=U\mathbin{\dot\cup}W.
\]

Let `Q=G/T`, let `z` be the contraction vertex, and suppose `c` is a proper
`r`-colouring of `Q`.  Write `c(z)=alpha`.  Choose any nonempty palette

\[
                       \Gamma\subseteq [r]-\{\alpha\},
        \qquad p=|\Gamma|,
\]

and put

\[
 J_\Gamma=Q[c^{-1}(\Gamma)],
\]

\[
 X_U^\Gamma=(N_G(U)-V(T))\cap V(J_\Gamma),\qquad
 X_W^\Gamma=(N_G(W)-V(T))\cap V(J_\Gamma).
                                                        \tag{1.1}
\]

Then `X_U^Gamma` and `X_W^Gamma` are both `p`-colourful in
`J_Gamma`.

#### Proof

The vertex `z` is not in `J_Gamma`.  Contraction changes no edge with both
ends outside `T`, so `J_Gamma` is literally the corresponding induced
subgraph of `G-V(T)`.

Every external neighbour of `T` is adjacent to `z` in `Q`.  Hence no
external neighbour of `T` has colour `alpha` under `c`.

Suppose that a proper `Gamma`-colouring `phi` of `J_Gamma` omits
`gamma in Gamma` on `X_U^Gamma`.  On `G-V(T)`, use `phi` on `J_Gamma`
and retain `c` on all vertices whose old colours lie outside `Gamma`.
The two palettes are disjoint, so this is proper.

Now colour all of `U` with `gamma` and all of `W` with `alpha`.  There are
no edges inside `U` or inside `W`, because `T` is induced bipartite.  An
external neighbour of `U` which lies in `J_Gamma` is in `X_U^Gamma` and
does not have colour `gamma`; every other external neighbour of `U`
retains a colour outside `Gamma`.  No external neighbour of `W` has
colour `alpha`, by the preceding paragraph.  Thus we have constructed a
proper `r`-colouring of `G`, a contradiction.

Therefore `X_U^Gamma` is `p`-colourful.  Interchanging `U` and `W` proves
the assertion for `X_W^Gamma`.  \(\square\)

### Corollary 1.2 (the requested `(r-2)` slice)

If `r >= 3`, choose one colour `beta` different from `alpha` and set

\[
             \Gamma=[r]-\{\alpha,\beta\},\qquad q=r-2.
\]

Then both parity portal sets in (1.1) are `q`-colourful in the
`q`-colourable graph `J_Gamma`.

If `G` is proper-minor-minimal non-`r`-colourable, the hypothesis that
`Q` is `r`-colourable is automatic, since `|T| >= 2` makes `G/T` a proper
minor.

### Lemma 1.3 (slice colourfulness adds no new fixed-pair axiom)

Let `J` be `q`-colourable, let `X subseteq V(J)`, and fix a proper
`q`-colouring `c` with colour classes `C_1,...,C_q`.  The following are
equivalent.

1. `X` is `q`-colourful in `J`.
2. For every nonempty `I subseteq [q]`, the set
   `X cap union_{i in I} C_i` is `|I|`-colourful in
   `J[union_{i in I} C_i]`.

#### Proof

The implication 2=>1 is the case `I=[q]`.  Conversely, suppose a proper
`I`-palette colouring of the indicated induced subgraph omitted a colour
`gamma in I` on its part of `X`.  Keep the original colouring `c` on all
classes outside `I`.  Since the palettes are disjoint, the two colourings
glue to a proper `q`-colouring of `J` which omits `gamma` on all of `X`, a
contradiction.  \(\square\)

Thus even the simultaneous conclusion of Theorem 1.1 for every palette
slice is already logically contained in the single statement that the
full `(r-2)` portal set is colourful.

## 2. Every Strong-Hadwiger boundary instance occurs

The next construction shows that Theorem 1.1 does not secretly restrict
the fixed pair `(J,X)`.

### Proposition 2.1 (universal compression realisation)

Let `q >= 1`.  Let `J` be `q`-colourable and let `X subseteq V(J)` be
`q`-colourful.  Put `r=q+2`.  Construct `F=F(J,X)` as follows.

* add three vertices `u,w,b` spanning a triangle;
* make `w` and `b` complete to `J`;
* join `u` to precisely the vertices of `X` in `J` (in addition to its
  two triangle edges).

Let `T=F[{u,w}]`, with parity classes `{u}` and `{w}`.  Then:

1. `F` has no proper `r`-colouring (indeed `chi(F)=q+3`);
2. `F/T` is `r`-colourable;
3. in the `q`-colour slice of such a colouring of `F/T`, the `{u}`-portal
   set is exactly `X` and the slice graph is exactly `J`.

#### Proof

Since `X` is `q`-colourful and `J` is `q`-colourable, `chi(J)=q`.  In a
hypothetical `(q+2)`-colouring of `F`, the adjacent vertices `w,b`, each
complete to `J`, must receive two distinct colours absent from `J`.
The restriction to `J` consequently uses the other `q` colours, all of
which occur on `X`.  The vertex `u` sees those `q` colours on `X` and the
two remaining colours on `w,b`, which is impossible.  Conversely, `q`
colours on `J` and three fresh colours on `u,w,b` colour `F`, so
`chi(F)=q+3`.

Contracting `uw` gives a vertex `z`.  Both `z` and `b` are complete to
`J` and adjacent to one another, so

\[
                         F/T = J\mathbin{\vee}K_2.
\]

Colour `J` with `q` colours and use two fresh colours `alpha,beta` on
`z,b`.  The slice avoiding `alpha,beta` is `J`.  Among its vertices, the
external neighbours of the `{u}` side of `T` are precisely `X`.  \(\square\)

Consequently, any theorem whose hypotheses mention only the fixed slice
`J`, its canonical colouring, the parity portal set `X`, and all the
slice-colourfulness conclusions of Theorem 1.1 is exactly a theorem about
an arbitrary Strong-Hadwiger instance.  It cannot be used as a uniform
rooted-clique theorem without proving that genuinely stronger statement.

The same universality persists when **both** parity portal sets are kept.

### Proposition 2.2 (universal simultaneous two-set realisation)

Let `J` be `q`-colourable, and let `X,Y subseteq V(J)` both be
`q`-colourful.  Put `r=q+2`.  There is a graph `F=F(J;X,Y)` and an
induced edge `T=uw` such that:

1. `F` has no proper `r`-colouring;
2. `F/T` has a proper `r`-colouring whose `q`-slice is exactly `J`;
3. the two parity portal sets in that slice are exactly `X` and `Y`.

#### Construction and proof

Add adjacent vertices `b_0,b_1`, each complete to `J`.  Add the edge
`uw`.  Join each of `u,w` to `b_1`, join neither to `b_0`, join `u` to
exactly `X` in `J`, and join `w` to exactly `Y` in `J`.  Add no other
edges.

In an alleged `(q+2)`-colouring, the adjacent vertices `b_0,b_1`, both
complete to `J`, have two distinct colours absent from `J`.  The graph
`J` is `q`-chromatic (because it is `q`-colourable and has a
`q`-colourful set), so it uses exactly the remaining `q` colours.  All
of them occur on each of `X` and `Y`.  Each of `u,w` sees those `q`
colours and the colour of `b_1`; its only available colour is therefore
the colour of `b_0`.  This is impossible because `uw` is an edge.

After contracting `uw` to `z`, colour `J` with `q` colours, give `b_1`
a fresh colour `beta`, and give both nonadjacent vertices `z,b_0` a
second fresh colour `alpha`.  This is a proper `(q+2)`-colouring.  The
slice avoiding `alpha,beta` is exactly `J`, and its two parity portal
sets are `X` and `Y` by construction.  \(\square\)

Thus even the simultaneous data

\[
       X_U\text{ colourful},\qquad X_W\text{ colourful}
\]

and the fact that they arise from the two ends of one contracted induced
edge impose no restriction on the abstract pair `(J;X_U,X_W)`.  Any
usable two-set theorem must invoke additional ambient minor-critical
transition geometry, not merely the common contraction colouring.

The graph `F(J,X)` need not be proper-minor-minimal.  The next section
shows that imposing ambient proper-minor-minimality still leaves the full
ordinary Hadwiger obstruction inside the construction.

## 3. Proper-minor-minimal ambient graphs still contain arbitrary contraction-critical Hadwiger instances

Call `H` **q-minor-critical** if `chi(H)=q` and every proper minor of `H`
is `(q-1)`-colourable.

### Theorem 3.1 (join lift of a contraction-critical instance)

Let `H` be any `q`-minor-critical graph, put `r=q+2`, and let

\[
                              G=H\mathbin{\vee}K_3.
                                                        \tag{3.1}
\]

Then `G` is proper-minor-minimal non-`r`-colourable.  If `u,w,b` are the
three vertices of the `K_3` and `T=G[{u,w}]`, then a colouring of
`G/T=H vee K_2` has an `(r-2)`-slice

\[
                              J=H,
\]

and both parity portal sets in that slice equal `V(H)`.

#### Proof

The chromatic number of a join is additive, so

\[
                    \chi(G)=\chi(H)+3=q+3=r+1.
                                                        \tag{3.2}
\]

We prove that every proper minor `M` of `G` is `r`-colourable.  Use a
branch-set presentation of `M`.  A branch set meeting the apex triangle
is adjacent to every branch set disjoint from it.  There are at most
three such branch sets.  All remaining branch sets lie in `H` and define
a minor `H'` of `H`.  Hence, after possibly deleting edges, `M` is a
subgraph of

\[
                              H'\mathbin{\vee}K_s
              \quad\hbox{for some }s\le 3.             \tag{3.3}
\]

If `H'` is a proper minor of `H`, then (3.3) is colourable with at most
`(q-1)+3=q+2=r` colours.  If `s<=2`, it is colourable with at most
`q+2=r` colours even when `H'=H`.

The only remaining presentation has `s=3` and `H'=H` with the same
vertex and edge counts as the original graph (not merely an abstract
isomorphic copy named `H`).  Finiteness then forces the three
apex-containing branch sets to be the three singleton apices and forces
every `H` branch set to be a singleton: otherwise a vertex of `H` is
absorbed into an apex branch set, or a genuine deletion/contraction has
occurred in `H`, making the displayed `H'` proper.  Thus a proper `M` in
this last case is a proper spanning subgraph of `G`.

It is enough to colour `G-e` for one deleted edge `e`.

* If `e` lies in `H`, the proper minor `H-e` is `(q-1)`-colourable; give
  the apex triangle three fresh colours.
* If `e` lies in the apex triangle, colour its two ends alike, use one
  further fresh colour on the third apex, and use `q` colours on `H`.
* If `e=h u` is a cross-edge, colour `H-h` with `q-1` colours, give `h`
  and `u` one common fresh colour, and give the other two apices two
  further fresh colours.

Each case uses at most `q+2=r` colours.  Every proper spanning subgraph is
contained in one of these one-edge deletions.  This proves the
proper-minor-minimal assertion.

Finally, contracting `uw` turns the apex triangle into `K_2`, so
`G/T=H vee K_2`.  Colour `H` with `q=r-2` colours and the two apex
vertices with two fresh colours.  The requested slice is exactly `H`,
and both `u` and `w` are adjacent to every vertex of `H`, so both parity
portal sets are `V(H)`.  \(\square\)

### Corollary 3.2 (the uniform rooted step contains Hadwiger)

Consider the proposed uniform assertion:

> whenever `G,T,J,X_U` satisfy Theorem 1.1, with `G`
> proper-minor-minimal non-`r`-colourable and `|Gamma|=r-2`, the graph
> `J` contains an `X_U`-rooted `K_{r-2}`-model.

For `r=q+2`, applying this assertion to Theorem 3.1 yields a `K_q` minor
in every `q`-minor-critical graph `H`, because `J=H` and `X_U=V(H)`.
That is exactly the contraction-critical formulation of `HC_q`.

Thus ambient minor-criticality is not, by itself, an extra hypothesis
which makes the uniform rooted step easier than Hadwiger.  It contains an
arbitrary lower-parameter Hadwiger instance as the join-lift special
case.

## 4. What operation-criticality actually supplies

Let `G` now be proper-minor-minimal non-`r`-colourable.

### Lemma 4.1 (exact one-operation witnesses)

For every vertex `x` and every proper `r`-colouring of `G-x`, all `r`
colours occur on `N_G(x)`.

For every edge `xy` and every proper `r`-colouring `psi` of `G-xy`:

1. `psi(x)=psi(y)=delta` for some colour `delta`;
2. every other colour occurs in `N_G(x)-{y}` and in
   `N_G(y)-{x}`;
3. for each `epsilon != delta`, the vertices `x,y` lie in the same
   `(delta,epsilon)` Kempe component of `G-xy`.

The same conclusions hold after lifting any colouring of `G/xy` to
`G-xy`.

#### Proof

If a colour were absent from `N_G(x)` in a colouring of `G-x`, it could
be assigned to `x`.  If `x,y` had different colours in `G-xy`, restoring
`xy` would colour `G`.  If a colour `epsilon` were absent from the
neighbourhood of one endpoint, recolour that endpoint `epsilon` and
restore `xy`.  Finally, if the two endpoints lay in different
`(delta,epsilon)` Kempe components, interchange the two colours on the
component containing `x`; the endpoints would then have different
colours and `xy` could again be restored.  Each conclusion contradicts
the non-`r`-colourability of `G` if it fails.  \(\square\)

### Corollary 4.2 (the genuine two-parity Kempe carriers)

Suppose the contracted bipartite graph is the edge `T=uw`, and let `c`
be the fixed `r`-colouring of `G/uw`, with contraction colour `alpha`.
Lift `c` to `G-uw` by giving both `u,w` colour `alpha`.  For every colour
`gamma != alpha` there is an `u-w` path whose vertices use only
`alpha,gamma`.

In particular, if `gamma` belongs to the selected `(r-2)` palette, the
first internal vertex of the path is a `gamma`-coloured member of the
`u`-portal set and the last internal vertex is a `gamma`-coloured member
of the `w`-portal set.  Thus minor-criticality supplies a colour-matched
carrier between the two parity portal sets for every slice colour.

#### Proof

The lifted colouring is a proper `r`-colouring of `G-uw`.  Apply the
Kempe-component conclusion of Lemma 4.1 to `uw`.  The first and last
internal vertices have colour `gamma`, since neither endpoint has an
external neighbour of colour `alpha`.  \(\square\)

This is genuine joint information which is absent from Proposition 2.2.
It is nevertheless still insufficient, by itself, to package a clique.
In the join lift `G=H vee K_3` of Theorem 3.1, choose the two contracted
apices as `u,w`.  For every colour `gamma` used on `H`, and every vertex
`v_gamma` of that colour, the path

\[
                              u v_\gamma w
                                                        \tag{4.1}
\]

is the required bichromatic carrier.  The `q` paths in (4.1) can be
chosen internally vertex-disjoint, one for each colour.  Yet turning their
internal vertices into pairwise adjacent connected bags is exactly the
problem of finding a `K_q` minor in the arbitrary `q`-minor-critical graph
`H`.  Therefore even perfectly disjoint, colour-matched two-parity
carriers do not bypass ordinary Hadwiger.

These are global witnesses.  They do **not** canonically descend to the
fixed `(r-2)`-slice `J` from Theorem 1.1:

* an operation colouring may use all `r` colours on the vertices of
  `J`, rather than the old `(r-2)` colours;
* its colour classes need not agree, even after a permutation, with the
  classes of the contraction colouring `c`;
* its Kempe paths may run through `T`, through the two omitted colour
  classes, and through the rest of `G-J`;
* after an edge contraction, the old induced slice need not even remain
  `(r-2)`-colourable, since contraction can increase chromatic number.

One may reapply Theorem 1.1 to a new contraction colouring and obtain a
new colourful slice, but that slice moves with the colouring.  Identifying
it with the original labelled `J` is an additional alignment theorem,
not a consequence of minor-criticality.

The join lift in Theorem 3.1 shows that this is not merely a technical
warning.  In that family the operation witnesses on the slice are exactly
the witnesses of an arbitrary `q`-minor-critical graph `H`.  Packaging
them into a `K_q` minor is precisely `HC_q`.

## 5. Consequence for the proof programme

The compression theorem is still useful at fixed small palette size.  At
`r=6`, the slice size is four and the proved four-colour Strong Hadwiger
theorem turns each parity portal set into a rooted `K_4`; this is a genuine
input to `HC_7` branch-set surgery.

For arbitrary `r`, however, the following inference is unavailable:

\[
 \text{parity portal set is `(r-2)`-colourful}
 \quad\Longrightarrow\quad
 \text{parity-rooted }K_{r-2}\text{ model}.
\]

Using only the fixed pair would invoke Strong Hadwiger.  Adding generic
minor-critical transition witnesses still contains ordinary Hadwiger by
Theorem 3.1.  A noncircular uniform continuation must therefore introduce
an additional mechanism which excludes the join-lift family or uses the
already-obtained unrooted `K_{r-2}` model in a genuinely label-preserving
exchange.  Examples of hypotheses which would be genuinely new are:

1. two disjoint parity sets with a forced incompatible portal order;
2. a bounded adhesion separating the omitted colour classes from the
   slice, together with a proved colour-gluing theorem;
3. a branch-set surgery invariant tied to a pre-existing unrooted clique
   model, not merely to the colouring relation on `X`;
4. an operation-colouring alignment theorem which explicitly keeps all
   Kempe paths inside the fixed slice.

Without such extra geometry, the uniform bipartite-compression route has
reached a theorem-strength barrier rather than a proof of the rooted step.

## 6. Audit boundaries

1. `T` must be induced bipartite.  Edges inside one parity class destroy
   the two-colour expansion in Theorem 1.1.
2. `T` must have at least two vertices when proper-minor-minimality is used
   to obtain a colouring of `G/T`.
3. The colour `alpha` is absent only from the **external neighbourhood**
   of `T`, not from all of `G-V(T)`.
4. Contraction can increase chromatic number.  No fixed-slice
   minor-monotonicity is claimed.
5. Proposition 2.1 does not claim that `F(J,X)` is minor-minimal.
   Theorem 3.1 is the separate construction which genuinely has that
   property.
6. Theorem 3.1 uses arbitrary branch-set models to check all proper
   minors, not merely one-step operations.
7. An `V(H)`-rooted clique model is just an ordinary clique model; hence
   Corollary 3.2 is an exact reduction, not an analogy.
