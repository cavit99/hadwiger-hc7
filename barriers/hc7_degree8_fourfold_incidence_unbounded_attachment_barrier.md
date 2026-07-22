# Four incidence splits do not bound the literal path attachments

**Status:** barrier/counterexample to a local finite-reduction claim.  This
is a self-contained decorated host construction, not a hypothetical
minor-minimal counterexample to `HC_7`.

## 1. Refuted claim

The following implication is false.

> There is an absolute constant bounding the lengths of the two aligned
> boundary-clean paths, and the ordered path-attachment sets of the
> components left after their interiors are deleted, using only:
>
> - an order-eight compact boundary split as
>   `I dotunion T dotunion {p,q}`;
> - two boundary-full open shores and a degree-eight vertex `u`;
> - seven-connectivity;
> - fixed merged-root and split-root shore colourings, with the same named
>   singleton Kempe operation failing in opposite directions;
> - the separating-bridge colouring responses; and
> - the fact that both `I` and `T` split in the component-incidence graph
>   after either path interior is deleted.

Thus these extracted local data do not by themselves reduce the residue to
finitely many literal attachment signatures.  A valid finite reduction must
also use `K_7`-minor exclusion, full contraction-criticality, or a new
response-preserving compression theorem.

## 2. The family

Put

\[
 I=\{i_0,i_1,i_2\},\qquad
 T=\{t_0,t_1,t_2\},\qquad
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\}.
\]

Let the boundary graph be

\[
 H=K_3[\{p,i_1,t_1\}]
   \mathbin{\dot\cup}K_3[\{q,i_2,t_2\}]
   \mathbin{\dot\cup}K_2[\{i_0,t_0\}].              \tag{2.1}
\]

In particular, `I,T` are independent, `pq` is a nonedge, and both roots
have a neighbour in both blocks.  The graph `H` has independence number
three and is itself `K_4`-minor-free: every connected minor lies in one of
the three displayed components.  It therefore satisfies the compact
condition that `H-Z` is `K_4`-minor-free for every two-set `Z`.

Fix `n>=2`.  Introduce two internally disjoint paths

\[
 \begin{aligned}
 P_E&=p e_1e_2\cdots e_{2n-1}q,\\
 P_F&=p f_1f_2\cdots f_{2n}q.                         \tag{2.2}
 \end{aligned}
\]

Write `L_E={e_1,...,e_{2n-1}}` and
`L_F={f_1,...,f_{2n}}`.  Join every vertex of `L_E union L_F` to every
vertex of `I union T`.

Choose arbitrary nonempty sets

\[
                         A_E\subseteq L_E,
             \qquad     A_F\subseteq L_F.             \tag{2.3}
\]

Add vertices `d_E,d_F` with

\[
 \begin{aligned}
 N(d_E)&=(S-\{i_0,t_0\})\cup A_E,\\
 N(d_F)&=(S-\{i_0,t_0\})\cup A_F.                    \tag{2.4}
 \end{aligned}
\]

Finally add `u` with `N(u)=S`.  Apart from the edges in (2.1)--(2.4) and
the edges from `u` to `S`, add no others.  In particular the open sets

\[
                 E=L_E\cup\{d_E\},\qquad
                 F=L_F\cup\{d_F\}                     \tag{2.5}
\]

are anticomplete.  They are connected because the sets in (2.3) are
nonempty, and each is adjacent to every vertex of `S`.  Hence `u` has
degree eight and `G-N[u]` has exactly the two boundary-full components
`E,F`.

## 3. Seven-connectivity

### Proposition 3.1

Every graph in the family is seven-connected.

### Proof

Put `C=I union T` and `L=L_E union L_F`.  The bipartite graph between
`C` and `L` is complete, with

\[
                         |C|=6,\qquad |L|=4n-1\ge7.    \tag{3.1}
\]

Let `Z` have order at most six.  If `C subseteq Z`, then `Z=C`: all other
vertices remain.  The union `P_E union P_F` is connected through `p,q`,
each `d_Q` meets its path, and `u` meets `p,q`; hence `G-Z` is connected.

Otherwise both `C-Z` and `L-Z` are nonempty, so their complete bipartite
subgraph lies in one connected component `R` of `G-Z`.  Every other
surviving vertex joins `R` as follows.

- The vertex `u` has a neighbour in `C-Z`.
- If `p` survives and `u` does, use `pu`.  If `u` is deleted, at most five
  further vertices are deleted.  Unless one of
  `i_1,t_1,e_1,f_1` survives, all four have been deleted; then the pair
  `d_E,d_F` includes a survivor, and so does the pair `i_2,t_2`.  This
  gives a path from `p` through the surviving `d_Q` to `R`.  The argument
  for `q` is symmetric.
- A surviving `d_Q` either has a surviving neighbour in
  `\{i_1,i_2,t_1,t_2\} union A_Q`, or both `p,q` would have to be deleted
  in addition to those at least five vertices.  The latter requires at
  least seven deletions.  Thus `d_Q` joins `R` directly or through a
  surviving root.

Therefore deleting at most six vertices never disconnects the graph.  On
the other hand

\[
 N(p)=\{u,i_1,t_1,e_1,f_1,d_E,d_F\},                 \tag{3.2}
\]

so `d(p)=7`.  The connectivity is exactly seven. \(\square\)

## 4. The two named colouring responses

Use six colour names

\[
                         a,b,\gamma,\delta,\eta,\zeta.
\]

On the closed `E`-shore, colour `I` with `a`, `T` with `b`, and both
`p,q` with `gamma`.  Alternate `gamma,delta` along `P_E` and give `d_E`
colour `eta`.  Since `P_E` has even length, this is a proper colouring
`c_E` inducing

\[
                         I\mid T\mid\{p,q\}.           \tag{4.1}
\]

On the closed `F`-shore, use the same colours on `I,T,p`, give `q` colour
`delta`, alternate `gamma,delta` along the odd path `P_F`, and give `d_F`
colour `eta`.  This is a proper colouring `c_F` inducing

\[
                         I\mid T\mid\{p\}\mid\{q\}.   \tag{4.2}
\]

In either colouring, the full `gamma`--`delta` component containing the
roots is exactly the displayed path.  On the boundary, changing only `q`
between `gamma` and `delta` is a singleton Kempe interchange because `pq`
is a nonedge.  It cannot be lifted as that singleton interchange through
either fixed shore: the full two-colour component also contains `p`.
Thus `P_E,P_F` are the two opposite failed lifts of the same named
operation.  Their interiors lie in different shores and their union is a
simple odd cycle.

Every edge `xy` of either `P_Q` is a separating bridge of its full
two-colour component.  Delete `xy` and interchange `gamma,delta` on the
component containing `q`.  The resulting colouring is proper, changes
exactly the equality type of `p,q` on `S`, and makes `x,y`
monochromatic.  It therefore matches the fixed colouring of the opposite
shore.  Gluing the two shore colourings and assigning `zeta` to `u` gives
a proper six-colouring of `G-xy`, equivalently the named contraction
response on `G/xy`.  Hence the complete bridge-response conclusion holds
on every path edge, with the opposite path and the operation label fixed.

## 5. Four incidence splits and unbounded port data

Deleting the open interior of `P_E` from `E` leaves the single component
`{d_E}`.  In its incidence graph with `I`, the vertices `i_1,i_2,d_E`
form one component and `i_0` is isolated.  With `T`, the analogous
components are `\{t_1,t_2,d_E\}` and `\{t_0\}`.  Thus both independent
triples split.  The identical argument in `F` proves all four incidence
splits and shows directly that neither shore has an `I`-carrier or a
`T`-carrier disjoint from its named path interior.

Nevertheless the literal ordered attachment sets are exactly

\[
       N(d_E)\cap P_E^\circ=A_E,
       \qquad
       N(d_F)\cap P_F^\circ=A_F.                     \tag{5.1}
\]

The oriented paths retain the names `p,q`, so (2.3) may encode arbitrary
binary words of unbounded length.  Seven-connectivity records only

\[
 |N(d_Q)|=6+|A_Q|\ge7,                               \tag{5.2}
\]

and supplies no upper bound.  Even the strongest elementary local
minimalizations do not help: taking each `A_Q` to be a singleton makes
`d_Q` a singleton residual component with an exact seven-vertex
neighbourhood and a one-point attachment interval, while the two unique
shortest two-colour paths remain arbitrarily long.

Consequently a complete attachment signature must retain an unbounded
ordered path-port relation.  If colouring behaviour beyond the two named
responses is to be preserved, it must additionally retain the extension
language of each residual component on those unboundedly many literal
ports.  Boundary masks and incidence components alone lose this data.

## 6. Exact trust boundary

This family deliberately does not satisfy the full hypothetical-
counterexample assumptions.  The six vertices of `I union T` are complete
to the `4n-1` internal path vertices.  Choosing seven of the latter gives
a `K_{6,7}` subgraph and the seven branch sets

\[
        \{c_j,\ell_j\}\ (1\le j\le6),
        \qquad \{\ell_7\},                            \tag{6.1}
\]

which form an explicit `K_7`-minor model.  The graphs are not asserted to
be seven-chromatic or minor-minimal, and the two displayed colourings are
named witnesses rather than a classification of all shore responses.

Accordingly, the construction does **not** refute a theorem saying that
unbounded attachment data force an explicit `K_7` model, a common boundary
partition, or a strict response-preserving component descent.  Nor does it
refute a bounded-kernel theorem that genuinely uses `K_7`-minor exclusion
and full contraction-criticality.  It shows that such a theorem is the
missing mathematical work: shortest paths, minimal residual components,
seven-connectivity, four incidence splits, and the named bridge responses
do not provide a finite preprocessing reduction on their own.
