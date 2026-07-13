# Operation states at the strict-surplus owner tree

## 1. The finite boundary states

Use the four-vertex owner society from Section 11 of
`hadwiger_near_k7_tree_society_split_2apex.md`:

\[
 E=uv+vr_1+vr_2,
\]

where \(u\) sees \(a,c\), while \(v,r_1,r_2\) are dark to \(c\) and
the latter three vertices supply the amplified \(R\)-portals.  The
singleton boundary is

\[
 S=\{a,c,q_1,q_2,q_3\},
\]

with \(ac\) the only nonedge of \(G[S]\).

### Lemma 1.1 (central-rung states)

Delete or contract \(uv\), and let the two images have colour \(\alpha\)
in a six-colouring of the resulting proper minor.  Then \(\alpha\) is
absent from \(S\), and the equality partition on \(S\) is exactly one of

\[
 \{a,c\}\mid\{q_1\}\mid\{q_2\}\mid\{q_3\},
 \qquad
 \{a\}\mid\{c\}\mid\{q_1\}\mid\{q_2\}\mid\{q_3\}.   \tag{1.1}
\]

#### Proof

The common colour is forbidden at \(a,c\) by the \(u\)-edges and at all
three \(q_i\) by the \(v\)-edges.  The three \(q_i\) form a clique and
both \(a,c\) see all of it.  Hence the only possible equality on the
boundary is the nonedge \(ac\). \(\square\)

### Lemma 1.2 (owner-leaf rung states)

Delete or contract \(vr_i\).  Its common colour \(\alpha\) is absent
from \(a,q_1,q_2,q_3\), while \(c\) may receive \(\alpha\).  The exact
possibilities are

\[
\begin{array}{ll}
\text{(i)}&c=\alpha,\quad a,q_1,q_2,q_3\text{ pairwise distinct};\\
\text{(ii)}&a=c\ne\alpha,\quad q_1,q_2,q_3\text{ distinct};\\
\text{(iii)}&a,c,q_1,q_2,q_3\text{ all distinct and avoid }\alpha.
\end{array}                                               \tag{1.2}
\]

#### Proof

The endpoints collectively see \(a,q_1,q_2,q_3\) and both miss \(c\),
which gives the assertion about \(\alpha\).  Properness of \(G[S]\)
again says that \(ac\) is the only possible repeated boundary pair.
\(\square\)

These lists apply to both deletion and contraction.  In the deletion
colouring the two endpoints receive the contracted vertex's colour.

## 2. What edge-criticality adds

For every state above, deletion-criticality says that for each
\(\beta\ne\alpha\), the \(\alpha/\beta\)-subgraph has a path between
the two endpoints.  It also says that each endpoint sees every other
colour.  This does not force the path for the colour of \(c\) to contain
\(c\), nor to avoid a fixed rooted branch bag.

There is one conditional positive conclusion.  If the central edge
\(uv\) is a genuine donor bridge and the \(\alpha/c(c)\)-component has
a \(v\)-to-\(c\) path whose interior avoids the protected \(u\)-side,
the other reserved branch bags, and the boundary, then the path interior
can be absorbed into the owner side and supplies its missing
\(c\)-contact.  The protected side retains its literal \(uc\)-edge, so
the collective-lobe exchange gives the explicit \(K_7\)-model (10.4).
The finite state itself does not guarantee this avoidance.

## 3. A state-realization countergadget

The failure is already visible in a coloured local gadget.  Give the
two operated endpoints colour \(0\).  For each other colour
\(i\in\{1,2,3,4,5\}\), add a new vertex \(x_i\) of colour \(i\) and
the two edges

\[
                         ux_i,\quad x_iv.             \tag{3.1}
\]

For the central rung, add the boundary edges from \(u\) to \(a,c\) and
from \(v\) to \(q_1,q_2,q_3\), together with the fixed \(K_5^-\)
boundary.  Assign the boundary colours according to either state in
(1.1).  Then every required bichromatic detour is the length-two path
\(ux_iv\).  Nevertheless \(c\) has no path to \(v\) in its two-colour
subgraph avoiding \(u\): its only neighbour of colour zero is \(u\).

For an owner-leaf rung, use endpoints \(v,r_i\), join both to the five
vertices \(x_j\), give them the boundary rows from Lemma 1.2, and use
any one of the three states (1.2).  Again all five length-two detours
exist.  If \(c\ne\alpha\), the owner vertex \(c\) is isolated from the
endpoints in the relevant two-colour component except through unrelated
boundary vertices; if \(c=\alpha\), the five required detours can still
all be chosen as (3.1), avoiding \(c\).

The same colouring descends after contracting the operated edge, so the
gadget realizes both deletion and contraction states.  It is not claimed
to be a contraction-critical host.  It proves the exact negative result:

\[
 \boxed{\text{boundary equality state + five Kempe detours}
 \not\Rightarrow\text{owner rerouting}.}
\]

Thus operation-criticality must be used globally--for example, by
comparing the states after several different edge operations or by a
minor-transition minimality argument.  A single edge trace, even on the
minimal strict-surplus tree, does not close the owner.

## 4. Exact remaining operation lemma

The strongest viable target is now:

> **Multi-edge owner exchange.**  In a contraction-critical host, the
> central operation \(uv\) and the two owner-lobe operations \(vr_1,vr_2\)
> cannot realize states (1.1)--(1.2) simultaneously while every
> \(c\)-coloured detour remains contaminated by the same protected core.

The word “simultaneously” is essential.  The countergadget realizes every
one-edge state separately (indeed in one fixed colouring architecture),
so a proof must use compatibility of the three proper-minor colourings or
an additional contraction transition.  No current argument supplies that
compatibility.

## 5. Contracting the whole owner star forces a saturated edge

The one-edge traces are independent, but contraction-criticality also
allows one joint operation which the local countergadget does not encode.
Contract the entire four-vertex tree

\[
                         E=uv+vr_1+vr_2
\]

to a vertex \(z\), and six-colour the resulting proper minor.  Write
\(c(z)=\alpha\).  For \(x\in E\), let

\[
 L(x)=[6]-c(N_G(x)-E)                                \tag{5.1}
\]

be its list after the contraction is expanded but the four vertices of
\(E\) are left uncoloured.

### Theorem 5.1 (joint-contraction saturated rung)

One has

\[
                         L(v)=\{\alpha\},             \tag{5.2}
\]

and at least one leaf \(x\in\{u,r_1,r_2\}\) satisfies

\[
                         L(x)=\{\alpha\}.             \tag{5.3}
\]

Consequently there is a specified tree edge \(vx\) such that the external
neighbourhood of **each** endpoint uses all five colours other than
\(\alpha\).

#### Proof

Every external neighbour of a vertex of \(E\) becomes adjacent to \(z\)
after contraction, so none has colour \(\alpha\).  Hence
\(\alpha\in L(x)\) for all four vertices.

If \(L(v)\) contained \(\beta\ne\alpha\), colour \(v\) with
\(\beta\) and all three leaves with \(\alpha\).  This would extend the
minor colouring to a six-colouring of \(G\), impossible.  Thus (5.2)
holds.

Now suppose every leaf had an alternative colour
\(\beta_x\in L(x)-\{\alpha\}\).  Colour \(v\) with \(\alpha\) and
each leaf \(x\) with \(\beta_x\).  The leaves are independent, so this
again extends to \(G\).  Therefore some leaf has the singleton list
(5.3).  A list is \(\{\alpha\}\) exactly when all other five colours
occur in the external neighbourhood, proving the last assertion.
\(\square\)

This supplies an actual edge, unlike the zero-length portal route exposed
by the dark-bag audit.  It is stronger than five abstract Kempe detours:
both ends are simultaneously colour-saturated by vertices outside the
owner tree in one common minor colouring.  It still does not identify
which of those external neighbours belong to the fixed rooted bags.  The
remaining joint step is to combine (5.2)--(5.3) with a rooted model chosen
from the same contraction colouring, or to show that failure of such a
choice yields a bounded separator.

## 6. The center saturation packages into a rooted \(K_5\)

The joint contraction contains more structural information than the
singleton-list statement records.  The following lemma is independent of
the particular four-vertex owner architecture.

### Theorem 6.1 (label-free contracted-star rooted core)

Let \(k\ge5\), let \(G\) be a graph with no proper \(k\)-colouring, and
let \(T\) induce a nontrivial star with center \(h\) and independent leaf
set \(L\).  Suppose that the proper minor \(Q=G/T\) has a
\(k\)-colouring \(c\), and write \(z\) for the contraction image and
\(c(z)=\alpha\).

Choose any four-element palette
\(\Gamma\subseteq[k]-\{\alpha\}\), and put

\[
 J=Q\big[c^{-1}(\Gamma)\big]
   =G\big[c^{-1}(\Gamma)\big],
 \qquad
 X=(N_G(h)-V(T))\cap V(J).                         \tag{6.1}
\]

Then \(X\) is four-colour-saturating in \(J\).  Consequently the proved
four-colour case of the Strong Hadwiger Conjecture gives an
\(X\)-rooted \(K_4\)-model in \(G-V(T)\), and adjoining the singleton
bag \(\{h\}\) gives a \(K_5\)-model.  Every one of its four nonsingleton
bags contains an external neighbour of \(h\).

#### Proof

Every vertex of \(N_G(T)-V(T)\) is adjacent to \(z\) in \(Q\).  Hence
the original \(\alpha\)-class is disjoint from this entire external
neighbourhood, not merely from the external neighbourhood of the center.

Suppose that a proper four-colouring \(\varphi\) of \(J\), using the
named palette \(\Gamma\), omitted some \(\gamma\in\Gamma\) on \(X\).
Keep the original colours on all classes outside \(\Gamma\), and use
\(\varphi\) on \(J\).  This properly colours \(G-V(T)\): the two
palettes are disjoint, so every edge crossing between \(J\) and its
complement remains proper.

Now give the center \(h\) colour \(\gamma\), and give **only the leaves**
of \(T\) colour \(\alpha\).  The leaves are independent.  None of their
external neighbours has colour \(\alpha\), because the old
\(\alpha\)-class missed \(N_G(T)-V(T)\) and the recolouring of \(J\)
uses only \(\Gamma\).  No external neighbour of \(h\) has colour
\(\gamma\): such a neighbour in \(J\) would belong to \(X\), where
\(\gamma\) was assumed absent, while a neighbour outside \(J\) retains
a colour outside \(\Gamma\).  Finally every center--leaf edge has
the colour pair \(\gamma,\alpha\).  We have obtained a proper
\(k\)-colouring of \(G\), a contradiction.

Thus every four-colouring of \(J\) uses all four colours on \(X\).
Strong \(HC_4\) supplies the rooted \(K_4\)-model.  Its bags lie in
\(J\subseteq G-V(T)\), and each contains a root in \(X\subseteq N(h)\),
so adding \(\{h\}\) makes all five bags pairwise adjacent. \(\square\)

### Corollary 6.2 (five palette views of the owner)

For the owner star \(E=uv+vr_1+vr_2\) in the six-colour case, the same
joint-contraction colouring produces one such controlled rooted \(K_5\)
for each choice of the omitted non-\(\alpha\) colour \(\delta\).  In
particular, the
operation-critical output is not merely a collection of coloured
neighbours or Kempe paths: it is a clique minor rooted at the actual
external portals of the owner center \(v\), entirely disjoint from the
owner tree.

This still does not by itself give \(K_7\).  To add two reserved bags one
must control which center portals root the four bags.  However it gives a
precise state-exchange target.  If \(A_1,A_2\) are disjoint connected
sets outside \(V(J)\cup\{h\}\) (they may use leaves of \(T\)) such that
\(\{h\},A_1,A_2\) form a triangle of bags, define

\[
 X_{A_1,A_2}=X\cap N(A_1)\cap N(A_2).               \tag{6.2}
\]

If this smaller set is four-colour-saturating in \(J\), Strong \(HC_4\)
roots the four bags in \(X_{A_1,A_2}\), and those four bags together
with \(\{h\},A_1,A_2\) are an explicit \(K_7\)-model.  Therefore every
\(K_7\)-minor-free survivor has, for every available completion triangle,
a proper four-colouring of \(J\) with a colour present on \(X\) but absent
from \(X_{A_1,A_2}\).  This is an operation-forced *dark portal class*,
not a static defect count.

## 7. One full iteration on the strict-surplus test society

The literal society of Section 11 of
`hadwiger_near_k7_tree_society_split_2apex.md` is even farther from a
counterexample than the static cut verifier detects.  Recall that every
\(p_i\) is adjacent to all five singleton labels and to both \(u,v\), and
that consecutive \(p_i,p_{i+1}\) are adjacent.

### Proposition 7.1 (the test society already contains \(K_7\))

For every \(i\in\{1,2,3,4\}\), the seven bags

\[
 \{a\},\quad\{q_1\},\quad\{q_2\},\quad\{q_3\},
 \quad\{p_i\},\quad\{p_{i+1}\},\quad E             \tag{7.1}
\]

form a \(K_7\)-model.

#### Proof

The first four singleton vertices form a clique.  Each of \(p_i,p_{i+1}\)
is adjacent to all four, and they are adjacent to one another.  The bag
\(E\) is connected; it sees \(a\) at \(u\), every \(q_j\) at \(v\), and
both \(p_i,p_{i+1}\) at \(u\) or \(v\).  Thus all twenty-one bag pairs
are adjacent. \(\square\)

Equivalently, contracting the owner star \(E\) creates a literal \(K_7\)
on

\[
 z,a,q_1,q_2,q_3,p_i,p_{i+1}.
\]

Hence the test society remains a valid falsifier for the *static statement*
that strict surplus and the displayed local cut inequalities force the
particular protected peel.  It is not a survivor once the ambient
\(K_7\)-minor exclusion is imposed.  No colouring-transition argument is
needed to eliminate this literal architecture.

The reason is label-free and should be retained in the structural
programme.

### Lemma 7.2 (full-row edge split)

Suppose a graph has disjoint bags consisting of a four-clique
\(C=\{s_1,s_2,s_3,s_4\}\), a connected bag \(B\), and adjacent vertices
\(x,y\notin C\cup B\).  If each of \(x,y\) is adjacent to every vertex of
\(C\) and to \(B\), and \(B\) is adjacent to every vertex of \(C\), then

\[
 \{s_1\}\mid\{s_2\}\mid\{s_3\}\mid\{s_4\}
 \mid\{x\}\mid\{y\}\mid B
\]

is a \(K_7\)-model.

Consequently, in every \(K_7\)-minor-free near-clique society, the vertices
of a shore which carry the same complete four-clique row and also see the
opposite bag form an independent set.  On a tree shore, two such full-row
portals can never be consecutive: some deficient state must occur on every
path between them.  This is the first reusable portal-order restriction
obtained from the minor exclusion itself, rather than from connectivity.

There is also a nonvacuous operation-critical version for owner stars not
already killed by Lemma 7.2.  In the notation of Theorem 6.1, suppose
\(A_1,A_2\) are a reserved completion triangle with \(h\), and put
\(Y=X\cap N(A_1)\cap N(A_2)\).  Then exactly one of the following holds:

1. \(Y\) is four-colour-saturating in \(J\), and the rooted core gives the
   explicit \(K_7\) described after (6.2); or
2. some proper four-colouring of \(J\) has a colour represented on the
   center-portal set \(X\) but absent from the fully compatible portal set
   \(Y\).

Thus after full-row edges are removed, the next survivor is not an
unstructured owner: it carries a named dark colour class of center portals
which fails at least one of the two completion incidences.  This is the
operation-critical state that a two-shore capacity exchange must transport.

## 8. Tree compression forces rooted cores on both parity shores

The star argument does not depend on having only one vertex in the first
bipartition class.  This gives a more useful theorem for the all-tree
near-\(K_7\) route.

### Theorem 8.1 (bipartite-bag compression)

Let \(k\ge5\), let \(G\) have no proper \(k\)-colouring, and let
\(T\) be a nontrivial connected induced bipartite subgraph with fixed
bipartition \(U\mathbin{\dot\cup}W\).  Suppose \(Q=G/T\) has a proper
\(k\)-colouring \(c\), with contraction image \(z\) of colour \(\alpha\).
For any four-element palette
\(\Gamma\subseteq[k]-\{\alpha\}\), let

\[
 J=Q[c^{-1}(\Gamma)]
\]

and define the two parity portal sets

\[
 X_U=(N_G(U)-V(T))\cap V(J),\qquad
 X_W=(N_G(W)-V(T))\cap V(J).                         \tag{8.1}
\]

Then both \(X_U\) and \(X_W\) are four-colour-saturating in \(J\).
Consequently \(J\) has an \(X_U\)-rooted \(K_4\)-model and an
\(X_W\)-rooted \(K_4\)-model.  In either case, adjoining the original
connected bag \(T\) gives a \(K_5\)-model all four other bags of which
meet the specified parity side of \(T\).

#### Proof

As before, the original \(\alpha\)-class is disjoint from
\(N_G(T)-V(T)\).  Suppose a four-colouring \(\varphi\) of \(J\) omitted
\(\gamma\in\Gamma\) on \(X_U\).  Keep every old colour class outside
\(\Gamma\), recolour \(J\) by \(\varphi\), give every vertex of \(U\)
colour \(\gamma\), and give every vertex of \(W\) colour \(\alpha\).

There are no edges inside \(U\) or inside \(W\).  Every edge of \(T\)
therefore has colour pair \(\gamma,\alpha\).  No external neighbour of
\(W\) has colour \(\alpha\), and no external neighbour of \(U\) has
colour \(\gamma\), by the two observations above.  Thus this is a proper
\(k\)-colouring of \(G\), a contradiction.  Hence \(X_U\) is
four-colour-saturating.  Interchanging \(U,W\) proves the assertion for
\(X_W\).

Strong \(HC_4\) supplies each rooted \(K_4\)-model.  It lies outside
\(T\), and each bag contains an external neighbour of the named parity
side, hence is adjacent to the connected bag \(T\). \(\square\)

### Corollary 8.2 (operation-critical parity state for tree societies)

In a minor-minimal non-six-colourable graph, every induced tree bag of
order at least two has the conclusion of Theorem 8.1 for all five choices
of a four-colour palette.  In particular, both parity classes—not just the
tree as an unlabelled shore—force controlled rooted \(K_5\)-models.

This is the first contraction-critical invariant in the near-clique route
which records *where inside a tree bag* its external contacts occur.  A
static quotient records only \(N(T)\); (8.1) records the two alternating
portal states separately.  For a nonrural tree-society cut, the next
exchange need only show that one of these two parity-rooted cores can be
chosen on portals compatible with two reserved completion bags.  If it
can, the completion-triangle argument gives \(K_7\); if it cannot, the
failed compatible subset has a named missing colour on each parity side.

### Corollary 8.3 (specified-edge rooted cores)

Let \(xy\) be any edge of a minor-minimal non-\(k\)-colourable graph,
where \(k\ge5\), and fix a \(k\)-colouring of \(G/xy\) with contraction
colour \(\alpha\).  For every four-element
\(\Gamma\subseteq[k]-\{\alpha\}\), both

\[
 (N_G(x)-\{y\})\cap V(J),qquad
 (N_G(y)-\{x\})\cap V(J)
\]

are four-colour-saturating in \(J\).  Hence there is a rooted \(K_4\)
outside \(\{x,y\}\) at each endpoint's actual external neighbours.  One
may adjoin \(\{x\}\) to the first model and \(\{y\}\) to the second,
obtaining two specified-singleton \(K_5\)-models, each avoiding the other
endpoint.

This applies in particular to the named alternating edge returned by the
tree interval criterion.  It strictly strengthens the five independent
Kempe detours formerly attached to that edge: the external neighbours of
each endpoint package into a rooted clique minor in every four-palette
view.  The remaining rotation-repair problem is now a compatibility
problem between this rooted core and two reserved completion bags, rather
than a path-existence problem.
