# Component-deletion Kempe exchange at a low-degree neighbourhood

**Status:** written proof; one computer-assisted finite lemma; separately
audited GREEN.  This theorem does not prove `HC_7`.

## Theorem 1 (common-neighbourhood component exchange)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Let `u` satisfy `7<=d_G(u)<=9`, put

\[
                         X=N_G(u),\qquad H=G[X],
\]

and suppose that `G-N[u]` has at least two components.  For a labelled
proper five-colouring `phi:X->[5]`, let `R(phi)` be the set of components
`D` of `G-N[u]` for which `phi` does not extend to a proper six-colouring
of `G[D union X]` using the palette `[6]`.

Then:

1. `H` is four-degenerate.  Hence the graph of labelled proper
   five-colourings of `H`, with Kempe interchanges as its edges, is
   connected.
2. `R(phi)` is nonempty for every labelled proper five-colouring `phi`.
   For every component `D` there is such a colouring `phi_D` with

   \[
                              R(\phi_D)=\{D\}.          \tag{1.1}
   \]

Paths `Q_D` can be chosen simultaneously for every component `D` of
`G-N[u]`, with nonempty interior in `D` and endpoint pair `f_D` a nonedge
of `H`, such that

\[
 K_6\not\preccurlyeq
 H+\{f_D:D\text{ is a component of }G-N[u]\}.         \tag{1.2}
\]

The paths may arise from different Kempe interchanges and different
boundary colourings.  Their open interiors are nevertheless literal and
pairwise disjoint and anticomplete; their boundary endpoints may overlap.

3. At least one of the following occurs.

   a. **Simultaneously rejected trace.**  Some labelled proper
      five-colouring `phi` satisfies `|R(phi)|>=2`.
   b. **Direct component switch.**  Two adjacent five-colourings `phi,psi`
      differ by one `alpha`--`beta` interchange on a component `W` of
      `H[alpha,beta]`, and distinct components `C,D` satisfy

      \[
                         R(\phi)=\{C\},\qquad R(\psi)=\{D\}. \tag{1.3}
      \]

      There are paths `P_C,P_D`, with internal vertices respectively in
      `C,D`, each joining `W` to a different component of
      `H[alpha,beta]`.  Thus the two paths certify opposite failures of
      the same literal boundary interchange.  Their open interiors are
      disjoint and anticomplete, although their boundary ends need not be
      disjoint.

In outcome 3b, let `e_C,e_D` be the endpoint pairs of shortest choices of
`P_C,P_D`.  Then

\[
                         K_6\not\preccurlyeq H+e_C+e_D. \tag{1.4}
\]

Here repeated added edges are added only once.  Otherwise the two paths
lift a `K_6` model of the augmented neighbourhood and the singleton
`{u}` completes an explicit `K_7`-minor model in `G`.

Outcome 3a also has a literal common-trace form.  If `phi` uses `k<=5`
colours and `D in R(phi)`, put

\[
 L_D(v)=[6]-\phi(N_G(v)\cap X)\qquad(v\in D).          \tag{1.5}
\]

There is a connected induced subgraph `K_D` of `D`, minimal subject to
not being `L_D`-colourable, such that

\[
 d_{K_D}(v)\ge |L_D(v)|=6-|\phi(N_G(v)\cap X)|        \tag{1.6}
\]

for every `v in K_D`.  Moreover `chi(K_D)>=7-k`, so the established cases
of Hadwiger's conjecture through parameter six give a `K_{7-k}` minor in
each rejected component.  For two members of `R(phi)` these kernels and
minor models are literal, disjoint, and anticomplete, and use the same
fixed boundary colouring.

In addition, for every `D in R(phi)` there is a path `Q_D` with nonempty
interior in `D` and endpoint nonedge `g_D` in `H`, and all these paths can
be retained simultaneously.  Writing repeated edges only once,

\[
             K_6\not\preccurlyeq H+\{g_D:D\in R(\phi)\}.
\]

## 1. The finite equality lemma

The degeneracy proof needs one small classification.

### Lemma 2 (two-support equality quotients)

Let `F` be one of the following graphs.

1. `F` has seven vertices, minimum degree at least five, and 18 edges.
2. `F` has eight vertices, minimum degree at least five, and 20 edges.

Add a vertex `u` complete to `F`.  Add two further vertices `c_1,c_2`
which are pairwise nonadjacent and nonadjacent to `u`.  In the first case
make each `c_i` adjacent to any five vertices of `F`; in the second make
each adjacent to any six vertices of `F`.  The resulting graph contains a
`K_7` minor.

#### Computer verification

The retained verifier is
[hc7_component_exchange_five_core_verifier.py](hc7_component_exchange_five_core_verifier.py).
It uses nauty `geng` to enumerate every unlabelled graph in the two edge
layers and filters for minimum degree five.  There is one surviving
seven-vertex graph and three surviving eight-vertex graphs.  For each it
checks every unordered pair, with repetition, of two-vertex miss sets for
`c_1,c_2`.  These are respectively

\[
             \binom{21+1}{2}=231,
 \qquad 3\binom{28+1}{2}=1218                       \tag{2.1}
\]

marked quotients.

For every quotient the verifier searches all possible `K_7` models.  A
model on ten or eleven vertices has at least four or three singleton
branch sets, respectively.  The search enumerates every clique of the
possible singleton order and every family of disjoint, connected,
pairwise adjacent non-singleton branch sets; unused vertices are allowed.
It then independently checks disjointness, connectedness, and all 21
branch-set adjacencies of the returned model.  All 1,449 marked quotients
have a certificate and none survives.

The deterministic run records

```text
layer h=7 e=18 graphs=1 marks=231 residues=0
layer h=8 e=20 graphs=3 marks=1218 residues=0
total_marks=1449 residues=0
catalogue_sha256=0ef56bb5ba5a44e5c699f2d0a81c1f74cc9eb35e5a52aed4dc6846817948900d
witness_sha256=b5af511f5eccf17baf6bd2dc8affa792d1391eb3128bc57111d4703227277caa
PASS component-exchange five-core classification
```

## 2. Four-degeneracy of the common neighbourhood

Suppose that an induced subgraph `F=H[Y]` has minimum degree at least five,
and put `h=|Y|`.  Then `6<=h<=9`.  Choose two distinct components
`D_1,D_2` of `G-N[u]`, contract each to one vertex `c_i`, and delete all
vertices outside `Y union {u,c_1,c_2}`.  Seven-connectivity gives
`|N_G(D_i)|>=7`, while `N_G(D_i) subseteq X`.  Hence

\[
 |N_G(D_i)\cap Y|\ge 7+h-d_G(u).                       \tag{2.2}
\]

The resulting minor `Q` has `h+3` vertices.  If `d_G(u)<=8`, it has at
least

\[
 h+\left\lceil\frac{5h}{2}\right\rceil+2(h-1)>5h
       =5|V(Q)|-15                                      \tag{2.3}
\]

edges.  Mader's exact extremal bound gives a `K_7` minor, a contradiction.

It remains that `d_G(u)=9`.  For `h=9`, the corresponding lower bound is

\[
 9+23+2\cdot7=46>45.                                   \tag{2.4}
\]

For `h=6`, the graph `F` is `K_6`, so `F union {u}` is already a `K_7`
subgraph.  If `h=7`, the edge count is strict unless `|E(F)|=18` and each
`c_i` has exactly five neighbours in `F`; Lemma 2 closes the equality
case.  If `h=8`, it is strict unless `|E(F)|=20` and each `c_i` has exactly
six neighbours in `F`; Lemma 2 again applies.

Thus no subgraph of `H` has minimum degree five, proving that `H` is
four-degenerate.

## 3. Private component-deletion colourings

Fix a component `D` of `G-N[u]`.  The proper minor `G-D` has a
six-colouring.  The colour of `u` is absent from `X`, because `u` is
complete to `X`.  Rename it colour six and rename all colours used on `X`
into `[5]`.  The restriction `phi_D` is therefore a labelled proper
five-colouring of `H`.

This colouring already extends through every component other than `D`.
If it also extended through `D`, align the labelled boundary and glue that
extension to the colouring of `G-D`; the exterior components are pairwise
anticomplete and no exterior vertex is adjacent to `u`.  This would
six-colour `G`.  Therefore (1.1) holds.

More generally, if `R(phi)` were empty for some proper five-colouring of
`H`, choose one extension through every exterior component, glue the
extensions along `X`, and give `u` colour six.  Again this would
six-colour `G`.  Hence every rejection set is nonempty.

## 4. Universal component-supported augmentation

Let `mathcal D` be the set of exterior components.  Fix distinct members
`C_0,C_1`.  Connect `phi_{C_0}` to `phi_{C_1}` by a sequence of Kempe
interchanges in the labelled five-colouring graph of `H`.  The component
`C_0` is rejected at the first endpoint and accepted at the last.  Some
consecutive pair `theta,theta'` therefore changes `C_0` from rejected to
accepted.

Take an extension of `theta'` through `G[C_0 union X]` and try to reverse
that one boundary interchange.  If the full two-colour component meeting
the switched boundary component avoided every other boundary component,
switching it would extend `theta` through `C_0`, a contradiction.  Hence it
meets two distinct two-colour components of `H`.  Choose a shortest path
`Q_{C_0}` in it between those boundary components.  An internal boundary
vertex would shorten the path, so `V(Q_{C_0}) cap X` consists exactly of
its two ends and every internal vertex lies in `C_0`.  The endpoint pair
`f_{C_0}` is consequently a nonedge of `H`, and the interior is nonempty.

For each `D in mathcal D-{C_0}`, connect `phi_{C_0}` to `phi_D`.  The
component `D` is accepted at the first endpoint and rejected at the last.
At the first accepted-to-rejected move, start with an extension of the
accepted colouring and apply the forward interchange.  The same
full-component argument gives a path `Q_D` with nonempty interior in `D`,
no other vertex in `X`, and endpoint nonedge `f_D`.  The moves used for
different components need not be the same.

The open path interiors lie in distinct exterior components, so they are
pairwise disjoint and anticomplete.  Contracting every interior toward a
boundary end realizes the graph in (1.2) as a minor of `G-u`, even when
some endpoint pairs overlap or repeat.  A `K_6` model in this augmented
graph would lift to six branch sets each meeting `X`; the singleton `{u}`
would complete a `K_7` model.  This proves (1.2).

## 5. A direct switch or one simultaneous trace

The theorem of Las Vergnas and Meyniel says that all `q`-colourings of a
`(q-1)`-degenerate graph are Kempe equivalent.  Apply it with `q=5` to
the four-degenerate graph `H`.

If some rejection set has order at least two, outcome 3a holds.  Otherwise
every proper five-colouring has a unique rejecting component.  The
colourings `phi_D` show that every component occurs as such a label.  Since
the five-colouring Kempe graph is connected and there are at least two
labels, some edge has differently labelled ends.  This gives (1.3).

Suppose that the edge interchanges `alpha,beta` on the component `W` of
`H[alpha,beta]`.  The colouring `phi` extends through `D`, while `psi`
does not.  Apply the one-interchange lifting argument to an extension of
`phi` through `G[D union X]`: an `alpha`--`beta` component in that extension
must join `W` to another boundary component, or the interchange would
produce an extension of `psi`.  A shortest such route has all internal
vertices in `D`.  Reversing the same interchange and using an extension of
`psi` through `C` gives the path with interior in `C`.  This proves the
direct-switch assertions.

Contracting the open interior of each path toward one of its ends realizes
`H+e_C+e_D` as a minor of `G-u`; this remains valid when the endpoint pairs
overlap, because the two open interiors lie in distinct components and any
shared boundary endpoint receives both contractions.  A `K_6` model in the
augmented graph therefore lifts to six branch sets each meeting `X`.
The singleton `{u}` is adjacent to all six and gives a `K_7` model.  This
proves (1.4).

## 6. The simultaneous-trace kernels

Fix `phi`, let `k=|phi(X)|`, and take `D in R(phi)`.  Extension through
`D` is exactly list-colourability of `G[D]` from (1.5).  Choose an induced
non-list-colourable subgraph with a minimum vertex set.  It is connected,
and colouring `K_D-v` proves (1.6): otherwise an unused colour from
`L_D(v)` would extend the colouring to `v`.

Every colour of `[6]-phi(X)` belongs to every list.  If `K_D` were
`(6-k)`-colourable, using only these common colours, it would be
`L_D`-colourable.  Hence `chi(K_D)>=7-k`, and the established cases
`HC_j`, `j<=6`, give the stated clique minor.  Distinct exterior
components are disjoint and anticomplete, so simultaneous kernels retain
the asserted literal separation.

For the simultaneous path assertion, fix `D in R(phi)` and choose an
exterior component `E ne D`.  The private colouring `phi_E` accepts `D`.
Along a Kempe sequence from `phi` to `phi_E`, take the first move changing
`D` from rejected to accepted and repeat the reverse-lifting argument of
Section 4.  It gives `Q_D` with nonempty interior in `D` and boundary
nonedge `g_D`.  Make this choice separately for every member of `R(phi)`.
The resulting interiors lie in distinct exterior components, so they are
simultaneously disjoint and anticomplete.  Contracting all of them realizes
the displayed augmentation as a minor of `G-u`; a `K_6` model would again
join `{u}` to form a `K_7` model.

## 7. Exact gain and remaining gate

The theorem removes equal component order as the organizing obstruction.
Whenever at least two exterior components exist, component deletion puts
all of them into one connected five-colour reconfiguration space on the
same literal neighbourhood `X=N(u)`.  Every chosen pair of components
already supplies two simultaneously retained paths and a `K_6`-minor-free
augmentation of `H`.  The rejection-map dichotomy further preserves one
of two forms of colouring provenance:

1. two or more literal components reject one fixed boundary trace; or
2. one literal Kempe interchange transfers the unique rejection and is
   witnessed by paths in both components.

This bypasses the earlier attempt to reinterpret a path from one component
as a failed-lift witness for another.  It does not yet convert either new
alternative into an explicit `K_7` model or a common complete boundary
partition.  It also does not address the case in which `G-N[u]` is
connected, including the tight pole residue.  Those are the exact next
proof obligations.

## References and inputs

- W. Mader, the exact extremal bound
  `|E(J)|<=5|V(J)|-15` for a simple graph `J` with no `K_7` minor and
  `|V(J)|>=7`.
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B **31** (1981), 95--104,
  Proposition 2.1.
- The established cases of Hadwiger's conjecture through `HC_6`.
