# Fixed-model contraction: portal alignment and its sharp failure

## Status

This note audits the matched tree-list obstruction in the setting of a fixed
labelled clique model.  One positive alignment survives: after the other
bags become a \(K_{r-1}\), the colour of the apex identifies a noncontact
bag.  The forced internal edge labels do not identify portals to that bag.
They have the opposite meaning: an edge carrying bag \(i\)'s colour has
both ends outside the \(i\)-portal class.

An explicit family below realizes a perfectly matched core, a double-foot
bag, one selected noncontact label, and completely concentrated portals,
but no split of the fixed bag preserves its labels.  The family is not
proper-minor-minimal and has the target clique minor through another model.
It therefore falsifies a static alignment claim, not the dynamic
transition-gate conjecture.

## 1. Canonical colours after contracting the model

Let \(G\) have no proper \(r\)-colouring, fix \(v\in V(G)\), put
\(H=G-v\), and fix a \(K_r\)-model

\[
                         (D,B_1,\ldots,B_{r-1}).          \tag{1.1}
\]

Let \(T\subseteq D\) be a connected induced transit society with an edge
to every \(B_i\).  Contract each \(B_i\) to \(b_i\), obtaining
\(\widehat G\), and then contract \(T\) to \(z\).  Let \(c\) be an
\(r\)-colouring of the resulting proper minor \(Q\).  The vertices
\(z,b_1,\ldots,b_{r-1}\) span \(K_r\).  Write

\[
                    c(z)=\alpha,\qquad c(b_i)=p_i.       \tag{1.2}
\]

For \(x\in T\), put, in the partially contracted graph \(\widehat G\),

\[
 P_i=\{x:N_G(x)\cap B_i\ne\varnothing\},\qquad
 L(x)=[r]\setminus c(N_{\widehat G}(x)-T).              \tag{1.3}
\]

Every external neighbour of \(T\) is adjacent to \(z\), so
\(\alpha\in L(x)\) for all \(x\).

### Proposition 1.0 (simultaneous-contraction incompatibility)

The non-\(r\)-colourability of \(G\) does not imply that \(T\) is
non-\(L\)-colourable in this state.  An \(L\)-colouring expands \(c\)
only to \(\widehat G\), not through the original nontrivial bags \(B_i\).

If all \(B_i\) are singleton, then \(\widehat G=G\), and \(T\) is
necessarily non-\(L\)-colourable.  The same conclusion is valid only when
a proper expansion through all contracted bags is separately supplied.

#### Proof

Expanding \(T\) leaves every contracted \(b_i\) untouched.  A single colour
on \(b_i\) has no automatic proper expansion through the connected,
generally nontrivial graph \(B_i\).  In the singleton case no expansion is
needed, and an \(L\)-colouring would colour \(G\), a contradiction.
\(\square\)

Thus canonical bag labels and a forced list obstruction cannot generally be
claimed from the same simultaneous contraction.  Sections 2--3 are
conditional on \(T\) actually being non-\(L\)-colourable; this is automatic
in the singleton-bag case.

### Lemma 1.1 (the apex selects a noncontact label)

If \(T\cap N_G(v)\ne\varnothing\), then

\[
                         c(v)=p_j                         \tag{1.4}
\]

for some bag \(B_j\) which does not meet \(N_G(v)\).

#### Proof

The clique \(z,b_1,\ldots,b_{r-1}\) uses every colour.  The edge \(vz\)
excludes \(\alpha\), so \(c(v)=p_j\) for some \(j\).  If \(B_j\) met
\(N_G(v)\), its contraction would create the edge \(vb_j\), contrary to
properness. \(\square\)

This is genuine fixed-model information: one common contraction colouring
canonically chooses a noncontact bag.

## 2. The tree labels are anti-portals

Assume \(T\) is non-\(L\)-colourable.  If it is a tree, choose an
inclusion-minimal non-\(L\)-colourable subtree \(R\).  The matched-tree
theorem gives a proper edge-colouring
\(\lambda\) such that

\[
                         L(x)=\{\lambda(e):e\ni x\},      \tag{2.1}
\]

and the \(\alpha\)-labelled edges form a perfect matching.

### Theorem 2.1 (portal exclusion)

For every \(i\),

\[
 P_i\cap V(R)\subseteq
 V(R)\setminus V(\lambda^{-1}(p_i)).                    \tag{2.2}
\]

If \(c(v)=p_j\), then

\[
 N_G(v)\cap V(R)\subseteq
 V(R)\setminus V(\lambda^{-1}(p_j)).                    \tag{2.3}
\]

#### Proof

If \(x\in P_i\), it has an external neighbour in \(B_i\) of colour \(p_i\),
so \(p_i\notin L(x)\).  Equation (2.1) says no incident core edge has label
\(p_i\).  The proof of (2.3) is identical, using the external neighbour
\(v\). \(\square\)

Thus a forced edge colour means that the colour is available at its ends.
A portal has exactly the reverse effect: it makes that colour unavailable.
In particular, a \(p_j\)-edge has neither a \(B_j\)-portal nor a double
foot at either end.

### Corollary 2.2 (shadow accounting)

If \(p_i\notin L(x)\), then at least one of the following occurs:

1. \(x\in P_i\);
2. \(c(v)=p_i\) and \(x\in N_G(v)\);
3. \(x\) has a neighbour of colour \(p_i\) outside
   \(T\cup\{v\}\cup\bigcup B_k\).

The third vertex is a shadow blocker.  It need not be absorbable into
\(B_i\): in the selected colouring it has the same colour as \(b_i\), so
there is no edge between them.

## 3. Arbitrary societies: surplus or a Gallai core

Conditional on non-\(L\)-colourability, the contraction gives a uniform
dichotomy even when \(T\) is not a tree.

### Theorem 3.1 (minimal society dichotomy)

Choose an inclusion-minimal connected induced \(R\subseteq T\) which is not
\(L\)-colourable.  Then

\[
                              |L(x)|\le d_R(x)             \tag{3.1}
\]

for every \(x\).  Hence either

1. some \(x\) has strict internal surplus \(d_R(x)>|L(x)|\); or
2. equality holds everywhere and \(R\) is a Gallai tree, so every block is
   a clique or an odd cycle.

#### Proof

Every component of \(R-x\) is a proper connected induced subgraph and is
therefore list-colourable by minimality.  Combine those colourings.  If
\(|L(x)|>d_R(x)\), a colour unused by the neighbours extends the colouring
to \(x\), a contradiction.  This proves (3.1).  In the equality case,
the degree-choosability theorem of Borodin and Erdős--Rubin--Taylor says
that an uncolourable degree-list graph is a Gallai tree. \(\square\)

In the standard sharpened degree-list description, every clique block has a
common palette of size one less than its order, every odd-cycle block has a
common two-colour palette, and a cutvertex list is the disjoint union of its
block palettes.  Because \(\alpha\) belongs to every list, the blocks whose
palette contains \(\alpha\) are vertex-disjoint and cover all vertices.
For a tree this is exactly the perfect matching.

At a surplus vertex,

\[
 d_R(x)+|c(N_G(x)-T)|=d_R(x)+r-|L(x)|>r.              \tag{3.2}
\]

This is a real internal/external colour-capacity surplus.  It still does
not identify which external colours come from labelled bags instead of
shadow blockers.  In both outcomes the only unconditional portal rule is

\[
                         x\in P_i\Longrightarrow p_i\notin L(x). \tag{3.3}
\]

### Theorem 3.2 (aligned transitions in the Gallai case)

Assume the whole contracted society is the equality core \(T=R\), and use
the block-palette description above.  For every edge \(e=xy\) in a block
\(K\), there is an \(L\)-colouring \(\varphi_e\) of \(R-e\) such that

\[
                         \varphi_e(x)=\varphi_e(y)\in C_K, \tag{3.4}
\]

where \(C_K\) is the palette of \(K\).  Consequently, keeping \(c\)
unchanged on \(\widehat G-T\) and using \(\varphi_e\) on \(T\) gives an
\(r\)-colouring of \(\widehat G-e\).  All these edge-transition colourings
agree literally outside \(T\).  They are colourings of \(G-e\) only in the
valid coexistence case \(\widehat G=G\), in particular when every other
model bag is singleton.

#### Proof

Root the block-cutvertex tree at \(K\).  If \(K\) is a clique of order
\(m\), colour the ends of \(e\) alike with one colour of its
\((m-1)\)-element palette and colour its other \(m-2\) vertices
bijectively with the remaining colours.  If \(K\) is an odd cycle, then
\(K-e\) is an even-length path between \(x,y\); its two-colouring gives
equal colours at the ends.

Proceed away from \(K\).  When a child clique block meets its parent at an
already coloured cutvertex \(q\), the colour on \(q\) belongs to the parent
palette and is outside the disjoint child palette.  Colour the other
vertices of the clique bijectively with the child palette.  For a child odd
cycle, delete the already coloured cutvertex and two-colour the remaining
path with the child palette.  Continue recursively.  This gives the desired
list-colouring of \(R-e\).

Combining it with \(c\) outside \(T\) is proper in \(\widehat G-e\) by the
definition of the lists. \(\square\)

For a tree, every block is \(K_2\), its palette is a singleton, and this
recovers the forced edge labels.  If an endpoint of \(e\) is an
\(i\)-portal, then \(p_i\notin C_K\subseteq L(x)\); the aligned transition
family still obeys the anti-portal rule.

The qualification \(T=R\) is essential.  If \(R\subsetneq T\), a colouring
of \(R-e\) need not extend through the hanging components of \(T-R\).

## 4. Explicit failure of fixed-model splitting

For every \(r\ge3\), construct \(F_r\) using colours
\(\alpha,p_1,\ldots,p_{r-1}\).

Take a clique

\[
                         C=\{a,b_1,\ldots,b_{r-1}\},     \tag{4.1}
\]

and a path

\[
                         T=x_1x_2x_3x_4.                \tag{4.2}
\]

Join \(x_1\) to every \(b_i\).  Add \(v\), adjacent to

\[
                         x_1,x_4,b_2,\ldots,b_{r-1},     \tag{4.3}
\]

but not to \(a,b_1\).  For every \(k\in\{2,3,4\}\) and
\(i\in\{2,\ldots,r-1\}\), add \(y_{k,i}\), join it to \(x_k\), and
join it to every vertex of \(C\) except \(b_i\).  Add no other edges.

### Lemma 4.1

The graph \(F_r\) is not \(r\)-colourable.

#### Proof

The clique \(C\) uses all colours; rename them so that
\(a=\alpha\) and \(b_i=p_i\).  Each \(y_{k,i}\), adjacent to all of
\(C\) except \(b_i\), is forced to \(p_i\).  The vertex \(x_1\), adjacent
to every \(b_i\), is forced to \(\alpha\).  Hence \(v\) cannot be
\(\alpha\); its other neighbours in \(C\) force \(v=p_1\).

Now \(x_4\) sees \(p_1\) at \(v\) and all \(p_i\), \(i\ge2\), at its
shadow vertices, so \(x_4=\alpha\).  Each of \(x_2,x_3\) has only
\(\alpha,p_1\) available.  The two end constraints force
\(x_2=p_1=x_3\), contradicting their edge. \(\square\)

### Lemma 4.2 (exact contraction state)

After contracting \(T\) to \(z\), the proper minor has the colouring

\[
 c(a)=c(z)=\alpha,\quad c(b_i)=p_i,\quad c(v)=p_1,\quad
 c(y_{k,i})=p_i.                                      \tag{4.4}
\]

The expansion lists along \(T\) are

\[
 \{\alpha\},\quad\{\alpha,p_1\},\quad
 \{\alpha,p_1\},\quad\{\alpha\},                      \tag{4.5}
\]

so \(T\) is the minimal core and its edge labels are

\[
                         \alpha,\ p_1,\ \alpha.          \tag{4.6}
\]

#### Proof

The only same-colour pair in (4.4) is \(a,z\), which is nonadjacent.
All other asserted edges join different colours.  The external neighbours
give (4.5), and the matched-tree theorem gives (4.6). \(\square\)

### Lemma 4.3 (double foot and no label-preserving split)

In \(H=F_r-v\), the bags

\[
                         D=T,\qquad B_i=\{b_i\}           \tag{4.7}
\]

form a fixed \(K_r\)-model.  The bag \(D\) contains the two feet
\(x_1,x_4\); \(B_1\) is noncontact, while the other \(B_i\) are contact.
Every portal class is

\[
                              P_i=\{x_1\}.               \tag{4.8}
\]

No connected lobe can be moved from \(D\) into \(B_1\) so that the enlarged
\(B_1\) is contact and the residual \(D\) retains its labelled
adjacencies.  Nor can \(D\) be split into two connected pieces both meeting
all portal classes.

#### Proof

All model adjacencies from \(D\) use \(x_1\).  Any moved lobe which meets
\(B_1\) and carries the concentrated portal system contains \(x_1\).
The residual path then has no neighbour in any \(B_i\).  Two disjoint pieces
cannot both contain the unique portal \(x_1\). \(\square\)

The selected noncontact colour \(p_1\) labels the middle edge \(x_2x_3\),
whose ends are neither feet nor \(B_1\)-portals.  This is exact
anti-alignment.

The audit boundary is essential: \(F_r\) is not claimed to be
proper-minor-minimal or \(K_{r+1}\)-minor-free; its forcing structure
provides the target minor through another model.  Therefore it proves only

\[
\boxed{\text{one contraction state + a fixed double-foot model}
\not\Rightarrow\text{a label-preserving split}.}          \tag{4.9}
\]

It does not refute a theorem using contact maximality, join-primality, and
edge-transition novelty for every proper minor.

## 5. Hanging parts have no interval or Helly consequence

Start with any matched uncolourable path core \(R\), attach an arbitrary
tree \(U\) to one core vertex, and put any desired portal classes on
vertices of \(U\).  Forced-colour shadow blockers realize the corresponding
expansion lists.  The old \(R\) remains an inclusion-minimal uncolourable
subtree.

Thus arbitrarily many portal classes can lie wholly in \(T-R\), in any
chosen arrangement.  A selected minimal core has no automatic portal-tree
interval, convexity, or Helly property.

A possible dynamic replacement is to optimize over all minimal cores.  A
forced-\(\alpha\) portal leaf can sometimes replace another
\(\alpha\)-leaf of a matched core.  Whether this core-exchange graph has a
useful basis-exchange or separator theorem is open.

## 6. Exact viable continuation

The contraction supplies three useful facts:

1. \(c(v)\) selects a noncontact bag;
2. a minimal core is strict-surplus or Gallai, with an
   \(\alpha\)-block cover;
3. every failure of portal alignment has a named shadow blocker.

The next theorem must use those shadows dynamically.

> **Shadow exchange target.**  In a least-parameter join-prime
> contraction-critical obstruction, choose a contact-maximal model and a
> contraction core minimizing shadow blockers.  Then either a shadow
> reroutes to improve the model, or an edge incident with a minimum shadow
> creates the same boundary state on both shores of an ambient adhesion.

The second outcome enters the proved transition-splicing theorem.  No
current result proves this target.  The present audit shows why the forced
edge labels alone cannot: they are availability labels and hence
anti-portals.
