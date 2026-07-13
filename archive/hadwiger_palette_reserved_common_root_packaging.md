# Palette-reserved packaging at the common Moser root

## 1. Exact trace and common root

Let \(G\) be a hypothetical minor-minimal \(HC_7\) counterexample,
let \(d(v)=7\), put \(H=G-v\), and take a nonedge
\(dl\subseteq N(v)\).  Colour the minor obtained by contracting the
star \(\{v,d,l\}\), and expand it to a proper six-colouring \(c\) of
\(H\).  Thus

\[
 c(d)=c(l)=\alpha,
\]

while

\[
 U=N(v)-\{d,l\}
\]

is rainbow in the other five colours.  Put

\[
                         F=\overline{G[U]}.
\tag{1.1}
\]

Assume \(F\) has property \((*)\) in the sense of
Kriesell--Mohr.  This holds in every Moser row considered below because
\(F\) is a connected pseudoforest.

For every \(xy\in E(F)\), the roots \(x,y\) lie in one
\(c(x)/c(y)\)-component of \(H\).  Otherwise switch the component
containing \(x\).  The colour formerly unique at \(x\) becomes absent
from \(N(v)\), while the repeated \(\alpha\)-pair is unchanged, so that
colour can be assigned to \(v\), contradicting \(\chi(G)=7\).

Let \(u\in U\) be adjacent to both \(d\) and \(l\), and put
\(\beta=c(u)\).  Denote by \(T\) the
\(\alpha/\beta\)-component of \(H\) containing \(u,d,l\).

## 2. Only the missing edges at \(u\) can be damaged

### Theorem 2.1 (palette-reserved common-root packaging)

Suppose \(T-u\) contains a \(d\)-\(l\) path \(P\).  If, for every
edge \(uw\in E(F)\), the roots \(u,w\) remain in one
\(c(u)/c(w)\)-component of \(H-P\), then \(G\) contains a
\(K_7\)-minor.

#### Proof

The path \(P\) uses only colours \(\alpha,\beta\), and it avoids all
five roots: it avoids \(u\) by hypothesis, the other four roots have
colours outside \(\{\alpha,\beta\}\), and \(d,l\notin U\).

Consider an edge \(xy\in E(F)\) not incident with \(u\).  The original
\(c(x)/c(y)\)-component joining \(x,y\) uses neither \(\alpha\) nor
\(\beta\), and is therefore disjoint from \(P\).  Hence its ends remain
Kempe-connected in \(H-P\).  The same conclusion for the edges of
\(F\) incident with \(u\) is the hypothesis of the theorem.

Apply property \((*)\) to \(F\) inside \(H-P\).  It gives five disjoint
connected bags rooted at \(U\), adjacent for every edge of \(F\).
Every pair not in \(F\) is joined by its root edge in \(G[U]\), so the
five bags form a rooted \(K_5\)-model.

The path \(P\) is disjoint from all five bags.  For every \(x\in U\),
at least one of \(dx,lx\) is an edge, since otherwise
\(\{d,l,x\}\) would be an independent set in \(G[N(v)]\), contrary to
\(\alpha(G[N(v)])\le2\).  Thus \(P\) is adjacent to every rooted bag.
It and the five rooted bags form a \(K_6\)-model in \(H\), and the
additional singleton bag \(\{v\}\) gives a \(K_7\)-model. \(\square\)

The theorem does not first choose an arbitrary rooted \(K_5\) and try
to push it off \(P\).  It reruns the property-\((*)\) construction in
\(H-P\).  Because \(P\) uses only the repeated colour and the colour
of one root, every missing-edge witness not incident with that root is
automatically protected.

### Corollary 2.2 (exact blocker star)

If \(G\) has no \(K_7\)-minor, then at least one of the following
obstructions occurs.

1. The vertex \(u\) separates \(d\) from \(l\) in \(T\).
2. The graph \(T-u\) contains a \(d\)-\(l\) path, and for every such
   path \(P\), at least one edge
   \(uw\in E(F)\) is blocked:
   \[
      u,w\text{ lie in different }c(u)/c(w)
      \text{-components of }H-P.                 \tag{2.1}
   \]

For a blocked edge \(uw\), every \(u\)-\(w\) path in their original
bichromatic component meets \(P\), and every such intersection vertex
has colour \(\beta\).  Hence that bichromatic component has an
inclusion-minimal \(u\)-\(w\) separator

\[
              Z_{P,w}\subseteq V(P)\cap c^{-1}(\beta).
\tag{2.2}
\]

In particular \(Z_{P,w}\) is an independent set lying in a single
colour class.

#### Proof

If outcome 1 fails, \(T-u\) contains a \(d\)-\(l\) path.  If one such
path blocks no incident edge of \(F\), Theorem 2.1 gives the forbidden
minor.  Thus outcome 2 holds.

For a blocked edge, the intersection of an
\(\alpha/\beta\)-path and a
\(\beta/c(w)\)-path can only have colour \(\beta\).  The finite set
\(P\cap c^{-1}(\beta)\) separates \(u,w\) in their bichromatic
component; take an inclusion-minimal subset.  A colour class is
independent. \(\square\)

This is a genuine reduction in *demand*, not an enumeration of rooted
models: the simultaneous five-bag problem becomes one same-colour
blocker star at the common root.

## 3. Four roots can always be reserved

The same palette separation gives an unconditional partial packing,
even when an incident demand at \(u\) is blocked.

### Theorem 3.1 (four-root reserve and tight adhesion)

Let \(P\subseteq T-u\) be any \(d\)-\(l\) path.  Then \(H-P\) contains
a \(K_4\)-model

\[
                        \mathcal Q=(Q_x:x\in U-\{u\})
\tag{3.1}
\]

rooted at the other four vertices of \(U\).  The bags use only their
four colour classes.

Let \(C\) be the component of

\[
                    H-\left(P\cup\bigcup_xQ_x\right)
\tag{3.2}
\]

containing \(u\).  Then either \(G\) has a \(K_7\)-minor, or all of the
following hold.

1. The component \(C\) misses at least one of the four bags \(Q_x\).
2. Both \(d,l\in N_P(C)\).
3. With \(W=N_H(C)\),
   \[
       W\subseteq V(P)\cup\bigcup_xV(Q_x),\qquad |W|\ge6,
   \tag{3.3}
   \]
   and \(W\) is distributed over \(P\) and at most three rooted bags.
4. If \(|W|=6\), then
   \[
                             W\cup\{v\}
   \tag{3.4}
   \]
   is an exact seven-cut of \(G\).
5. At least one concrete carrier has surplus:
   \[
      |N_P(C)|\ge3
      \quad\text{or}\quad
      |N_{Q_x}(C)|\ge2\text{ for some contacted }Q_x.
   \tag{3.5}
   \]

Thus failure of simultaneous packaging gives either the desired minor,
an actual exact adhesion, or strict portal surplus on one path and at
most three rooted bags.

#### Proof

Every edge of \(F-u\) has a bichromatic component using two colours
outside \(\{\alpha,\beta\}\), hence avoiding \(P\).  The graph \(F-u\)
is a subgraph of a pseudoforest and has property \((*)\).  Apply that
property in the union of the four relevant colour classes in \(H-P\).
The missing adjacencies are supplied by the resulting rooted model and
the complementary adjacencies by root edges, giving (3.1).

The root \(u\) lies outside \(P\) and outside all four bags, so \(C\)
is defined.  If \(C\) were adjacent to all four \(Q_x\), the six bags

\[
                         P,\ C,\ (Q_x:x\ne u)
\tag{3.6}
\]

would form a clique model.  The four \(Q_x\)'s form a \(K_4\); the
component \(C\) sees them by assumption; and \(P\) sees every \(Q_x\)
through at least one of the root edges \(dx,lx\).  Finally \(u\in C\)
is adjacent to both endpoints \(d,l\) of \(P\), so \(C\sim P\).
Adding \(\{v\}\) gives \(K_7\).  This proves item 1 in a
\(K_7\)-minor-free graph.

The same two literal edges \(ud,ul\) prove item 2.  The external
neighbourhood of the component \(C\) is contained in the deleted set
in (3.2), proving the containment in (3.3).  A missed rooted bag lies
on the far side, so \(W\) is a vertex cut of \(H\).  Since \(H=G-v\)
is six-connected, \(|W|\ge6\).  Item 1 says that at most three rooted
bags contribute portals.

If equality holds, \(W\cup\{v\}\) separates \(C\) from the missed bag
in \(G\).  It has order seven.  Seven-connectivity makes every
component behind it full to it, so it is an exact seven-cut.

Finally, item 2 supplies two distinct portals on \(P\).  If there is no
third one, the remaining at least four vertices of \(W\) lie in at most
three rooted bags, and one of those bags is hit twice.  This proves
item 5. \(\square\)

### Corollary 3.2 (aligned transition on the tight cut)

In the \(|W|=6\) outcome, put \(S=W\cup\{v\}\).  For every internal
edge or vertex operation \(\mu\) on the \(C\)-side,
minor-criticality supplies an equality state on the same labelled
seven-set \(S\) which extends the unchanged opposite side and the
modified \(C\)-side.  That state does not extend the original
\(C\)-side.

#### Proof

Colour the proper minor \(G^\mu\) and restrict its colouring to \(S\).
It extends both indicated pieces.  If the same state extended the
original \(C\)-side, align colour names on \(S\) and glue it to the
unchanged opposite-side restriction of the colouring of \(G^\mu\).
This would six-colour \(G\), a contradiction. \(\square\)

This corollary is only a state-transition statement.  It does not claim
that the state is knitted or colour-gluable; that geometric realization
is the remaining exact-adhesion exchange.

### Lemma 3.3 (the connector is an edge-by-edge low-state spine)

Let \(e\) be any edge of \(H\), in particular any edge of the connector
\(P\).  There is a proper six-colouring \(c_e\) of \(H-e\) such that

1. the ends of \(e\) have the same colour;
2. at most five colours occur on \(N(v)\); and
3. the induced equality state on \(N(v)\) does not extend to a
   six-colouring of \(H\);
4. writing \(\alpha_e\) for their common colour, for every
   \(\gamma\ne\alpha_e\) the two ends of \(e\) lie in one
   \(\alpha_e/\gamma\)-component of \(G-e\).

The same low-state conclusion holds after deleting any vertex of
\(H-N(v)\), and after contracting any edge whose ends lie outside
\(N(v)\).

#### Proof

Colour the proper minor \(G-e\).  Restoring \(e\) can fail only when its
ends have the same colour, proving item 1.  The colour assigned to \(v\)
occurs on no member of \(N(v)\), so the neighbourhood uses at most the
other five colours, proving item 2.

If the resulting equality state extended to \(H\), permute its at most
five block colours to agree with \(c_e\) on the neighbourhood and give
\(v\) the sixth colour absent there.  This would six-colour \(G\).
Thus item 3 holds.  Vertex deletion and internal contraction are
identical: colour the corresponding proper minor of \(G\), retain the
colour of \(v\), and restrict to the unchanged labelled neighbourhood.

For item 4, if the component containing one end omitted the other,
interchange its two colours.  The ends of \(e\) would then have
different colours, so \(e\) could be restored, again six-colouring
\(G\). \(\square\)

Accordingly, the strict-surplus alternative of Theorem 3.1 is not a
static bridge web.  Every edge along its reserved path is essential for
excluding all five-block neighbourhood states.  Any final
blocker-to-adhesion theorem must use these transitions jointly; the
counterarchitecture in Section 5 shows that the fixed exact trace alone
does not suffice.

### Theorem 3.4 (ordered connector-edge peel)

Retain Theorem 3.1 and write

\[
                     P=p_0p_1\cdots p_k,
\qquad p_0=d,\quad p_k=l.
\]

For each of the four rooted bags \(Q_j\), define its first and last
portal positions on \(P\):

\[
\begin{aligned}
 f_j&=\min\{i:p_i\sim Q_j\},\\
 \ell_j&=\max\{i:p_i\sim Q_j\}.
\end{aligned}
\tag{3.7}
\]

These numbers exist because \(P\) is adjacent to every rooted bag.
Put

\[
 A=\{j:C\sim Q_j\}.
\tag{3.8}
\]

In the \(K_7\)-minor-free row, \(A\ne[4]\).  If either

\[
 \max_{j\notin A} f_j < \min_{j\in[4]}\ell_j
\tag{3.9}
\]

or

\[
 \max_{j\in[4]} f_j < \min_{j\notin A}\ell_j,
\tag{3.10}
\]

then \(G\) contains a \(K_7\)-minor.

Consequently every surviving strict-surplus row satisfies the two
ordered locks

\[
\boxed{
\max_{j\notin A} f_j \ge \min_j\ell_j,\qquad
\max_j f_j \ge \min_{j\notin A}\ell_j.}
\tag{3.11}
\]

#### Proof

Assume (3.9), and choose an integer \(i\) with

\[
              \max_{j\notin A}f_j\le i<
              \min_j\ell_j.
\tag{3.12}
\]

Use the six bags

\[
 C\cup P[p_0,p_i],\qquad
 P[p_{i+1},p_k],\qquad Q_1,Q_2,Q_3,Q_4.
\tag{3.13}
\]

They are disjoint.  The first is connected because \(u\in C\) is
adjacent to \(p_0=d\); the second is a path; and the first two bags are
adjacent through \(p_ip_{i+1}\).  The \(Q_j\)'s form a \(K_4\).

For \(j\in A\), the first bag sees \(Q_j\) through \(C\).  If
\(j\notin A\), inequality \(f_j\le i\) gives a portal in its path
prefix.  Thus the first bag sees all four \(Q_j\)'s.  The right-hand
inequality in (3.12) gives \(\ell_j\ge i+1\) for every \(j\), so the
second bag also sees all four.  Hence (3.13) is a \(K_6\)-model in
\(H\).  Each bag contains a member of \(N(v)\): the first contains
\(u,d\), the second contains \(l\), and the others contain their four
roots.  Adding \(\{v\}\) gives \(K_7\).

If (3.10) holds, choose

\[
              \max_jf_j\le i<
              \min_{j\notin A}\ell_j
\]

and use the reversed bags

\[
 P[p_0,p_i],\qquad C\cup P[p_{i+1},p_k],
\qquad Q_1,Q_2,Q_3,Q_4.
\]

Now the prefix sees every rooted bag, while the suffix sees the bags in
\(A\) through \(C\) and every other bag through its last portal.  It is
connected because \(u\sim l=p_k\).  The same adjacency check gives the
minor.  Negating (3.9)--(3.10) gives (3.11). \(\square\)

Theorem 3.4 closes an unbounded family of shores and connector lengths.
It also names what an edge transition must accomplish in the residue:
create an avoiding portal for a late-first or early-last rooted bag so
that one of the strict inequalities (3.9)--(3.10) becomes true.  Merely
creating another unordered portal is insufficient.

### Corollary 3.5 (a clean transition rung is a genuine peel)

Fix an edge \(e_i=p_ip_{i+1}\) of \(P\).  Suppose one of the
edge-critical detours from Lemma 3.3 has an internal connected subgraph
\(R\) such that

* \(R\) is disjoint from \(C\), from \(P\), and from
  \(Q_h\) for \(h\ne j\);
* \(R\cup Q_j\) is connected; and
* \(R\) has a neighbour at both \(p_i,p_{i+1}\).

Replace \(Q_j\) by \(Q_j\cup R\).  This preserves the rooted \(K_4\)
and adds both \(i,i+1\) to the portal positions of \(Q_j\).  If the
resulting first/last positions satisfy (3.9) or (3.10), then \(G\)
contains a \(K_7\)-minor.

#### Proof

The enlarged bag is connected, remains disjoint from the other five
objects, and retains every old rooted-bag adjacency.  Its two displayed
edges to \(P\) give the new portal positions.  Apply Theorem 3.4 to the
enlarged model. \(\square\)

Therefore every transition in the final ordered lock has a concrete
failure certificate: each potentially order-breaking detour must hit
\(C\), hit a wrong rooted bag before reaching the intended bag, or fail
to cross the locked first/last threshold.  This is the
operation-critical first-hit web; it is strictly narrower than the
static portal lock (3.11).

### Lemma 3.6 (the original trace aligns with every internal edge)

Let \(e=xy\) be an edge of \(P\) not incident with \(d\) or \(l\).
There is a six-colouring \(c^e\) of \(H-e\) such that

\[
 \{s\in N(v):c^e(s)=c^e(d)\}=\{d,l\},
\qquad c^e(x)=c^e(y),
\tag{3.14}
\]

and one of the following holds.

1. The five vertices of \(U\) are rainbow.
2. The colouring extends to \(G-e\), and for each of the five colours
   different from \(c^e(x)\) there is a corresponding bichromatic
   \(x\)-\(y\) detour in \(G-e\).

Thus every internal edge of a surviving ordered lock has either a new
exact-trace rooted-model witness or five edge-critical detours in a
low state retaining the original block \(\{d,l\}\).

#### Proof

The connected star \(\{v,d,l\}\) and the edge \(xy\) are disjoint.
Contract both sets and six-colour the resulting proper minor.  Delete
\(v\), expand \(d,l\) with the star image's colour, and expand \(x,y\)
after deleting \(xy\).  Every member of \(N(v)-\{d,l\}\) was adjacent
to the star image, proving the exact trace in (3.14); the edge
contraction gives the second equality.

If \(U\) is rainbow, outcome 1 holds.  Otherwise the seven vertices of
\(N(v)\) use at most five colours, so assign to \(v\) a sixth colour
absent there.  This extends the colouring to \(G-e\).  If an
\(c^e(x)/\gamma\)-component separated \(x\) from \(y\), switch it and
restore \(e\), six-colouring \(G\).  Hence all five detours exist.
\(\square\)

### Corollary 3.7 (three-bag order in the one-defect row)

Suppose \(C\) sees exactly three of the four rooted bags, and let
\(Q_j\) be the missed bag.  If \(G\) has no \(K_7\)-minor, there are
rooted bags \(Q_r,Q_s\) such that

\[
                         \ell_r\le f_j\le\ell_j\le f_s.
\tag{3.15}
\]

Thus the missed bag's entire portal interval is locked between an
early-ending rooted bag and a late-starting rooted bag.  In particular,
the residue is a three-bag ordered web, not four arbitrary portal
sets.

#### Proof

Here \([4]-A=\{j\}\).  The first inequality in (3.11) says
\[
 f_j\ge\min_h\ell_h;
\]
choose \(r\) attaining the minimum.  The second says
\[
 \max_hf_h\ge\ell_j;
\]
choose \(s\) attaining the maximum.  The middle inequality
\(f_j\le\ell_j\) follows because \(Q_j\) has a nonempty portal set.
\(\square\)

### Corollary 3.8 (Moser endpoint pinning)

In every central Moser row, the four roots in \(U-\{u\}\) split into
two \(d\)-only roots and two \(l\)-only roots.  Consequently their bags
have, respectively,

\[
                         f_j=0
\quad\text{and}\quad
                         \ell_j=k.
\tag{3.16}
\]

Retain the one-defect hypothesis of Corollary 3.7.

* If the missed bag is rooted at a \(d\)-only root, some rooted bag
  \(Q_r\) satisfies
  \[
                         N_P(Q_r)=\{d\}.
  \tag{3.17}
  \]
* If the missed bag is rooted at an \(l\)-only root, some rooted bag
  \(Q_s\) satisfies
  \[
                         N_P(Q_s)=\{l\}.
  \tag{3.18}
  \]

Thus every surviving one-defect ordered web has a rooted bag pinned to
one endpoint of the connector.

#### Proof

The Moser edge list shows that, after deleting the common root, exactly
two of the remaining roots are adjacent to \(d\) and exactly the other
two are adjacent to \(l\).  Their root edges give (3.16).

If the missed bag \(Q_j\) is \(d\)-only, then \(f_j=0\).  The first
lock in (3.11) gives
\[
                    0=f_j\ge\min_h\ell_h.
\]
All last positions are nonnegative, so some \(\ell_r=0\).  Its nonempty
portal set is therefore exactly the vertex \(p_0=d\), proving (3.17).
The \(l\)-only case is symmetric, using \(\ell_j=k\) and the second
lock in (3.11) to obtain some \(f_s=k\). \(\square\)

## 4. Pure-Moser demand count

Use

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\tag{4.1}
\]

For \(d\in\{1,2,6\}\) and \(l\in\{3,4\}\), take

\[
 u=\begin{cases}
       h=0,&d=1,2,\\
       5,&d=6.
    \end{cases}
\tag{4.2}
\]

This \(u\) is adjacent to both \(d,l\).  Directly from (4.1):

* if \(d=1,2\), then \(F\cong C_5\) and
  \[
                            d_F(u)=2;
  \]
* if \(d=6\), then \(F\) is a \(C_4\) with one pendant edge and
  \[
                            d_F(u)=3.
  \]

Thus failure of the reserved packaging is confined to two named
bichromatic demands in the first four rows and three in the last two
rows.  All other missing-edge witnesses survive every path
\(P\subseteq T-u\) automatically.

The remaining promotion problem is precise:

> Turn the independent same-colour blocker \(Z_{P,w}\) into a rerouting
> of \(P\), or prove that its attachments define an actual exact
> adhesion.  Separation only inside the bichromatic component is not
> yet separation in \(H\).

## 5. Why a component blocker is not automatically a small adhesion

The following established counterarchitecture from
hadwiger_kempe_removable_round.md audits the last sentence sharply.
Let

\[
 H=K_2\vee\overline{C_8},
\qquad
 C_8=p\,a\,q\,b\,c\,r\,d\,e\,p.
\tag{5.1}
\]

Take the exact trace whose matching of cycle vertices is

\[
                  pa,\ qb,\ cr,\ de.
\tag{5.2}
\]

The repeated pair is \(d,e\), the five roots are
\(h_1,h_2,a,b,c\), and the only missing root edge is \(bc\).
The root \(b\) is adjacent to both \(d,e\).  Its colour class is
\(\{q,b\}\), and

\[
                     d-q-e
\tag{5.3}
\]

is the corresponding repeated/common-root two-colour connector.
The unique \(b\)-\(c\) bichromatic path is

\[
                     b-r-q-c.                    \tag{5.4}
\]

Hence (5.3) blocks (5.4) at the same-colour vertex \(q\).
More globally, every \(d\)-\(e\) path avoiding the five roots uses
\(q\) or \(r\), and

\[
                 U\cup\{q,r\}
\]

is a minimum blocker of order seven, not an adhesion of order at most
six.  Nevertheless \(H\) is seven-connected, the trace is a genuine
star-contraction trace, every colouring saturates the prescribed
neighbourhood, and both accessible pairs occur.

This graph already has a \(K_7\)-minor and the associated apex graph is
not edge-critical.  It therefore does **not** refute a theorem using
the full counterexample hypotheses.  It proves that connectivity,
trace exactness, and the same-colour conclusion (2.2) alone cannot
promote the blocker to a small adhesion.  Minor exclusion or a further
one-step critical transition must be used in that promotion.

## 6. Direct central-orbit static falsification

The stronger construction in
hadwiger_central_bridge_blocker_static_falsification.md uses the actual
central pair \(6\mid3\), an induced pure-Moser boundary, and a sole full
exterior.  It satisfies

\[
                         \kappa(H)=\kappa(G)=7,
\]

has the full exact \(63\)-trace Kempe package, and forces every supported
connector through two vertices \(t_1,t_2\).  Deleting those vertices
leaves a planar graph, so every rooted \(K_5\)-model uses at least one
of them.  Thus even joint connector/model minimization fails, without
producing a cut of order at most six.

The added apex graph in that construction is explicitly six-colourable.
It therefore fails Lemma 3.3: a five-block state already extends the
undeleted shore.  This verifies, in the exact central orbit, that the
edge-by-edge low-state spine is indispensable rather than cosmetic.
The independent executable audit is
moser_bridge_blocker_counterarchitecture_probe.py.

## 7. Transition-only adversarial boundary

The construction in hadwiger_palette_wall_ear_counterarchitecture.md
passes the next operation test that the static construction above
fails.  It is seven-connected, its sole Moser shore admits no
at-most-five-block state, and deleting or contracting every internal
edge unlocks such a state.  Its minimum connector is a genuine
multi-portal ear with no exact cut exposed by the static portal rows.

That graph contains an explicit \(K_7\)-minor, and only one of the ten
exact Moser traces is accessible.  It therefore does not refute
Theorems 3.4--3.6 in the counterexample-derived setting.  It establishes
the sharp logical boundary:

\[
\begin{array}{c}
\text{palette wall + all one-step internal transitions}\\
\text{+ seven-connectivity + ordered portal surplus}
\end{array}
\quad\not\Longrightarrow\quad
\text{peel or exact adhesion}
\]

without also using \(K_7\)-minor exclusion or the full exact-trace
family.  Producing a counterarchitecture with both of those additional
properties would amount to constructing the missing \(HC_7\)
counterexample itself.
