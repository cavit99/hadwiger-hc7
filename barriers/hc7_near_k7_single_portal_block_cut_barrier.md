# Single-portal and block-cut barriers in a labelled near model

## Status

This pair of explicit graphs isolates the exact residue left by the
protected two-portal exchange.  Both graphs are `K_7`-minor-free,
non-two-apex, and contain a spanning coherent labelled `K_7^vee` model.
In the first graph the concentrated row has one literal carrier portal.
In the second it has two portals, but a cutvertex separates their arm
from the unique vertex attaching the carrier to both path sides.

Neither graph is seven-connected: each is a one-sum.  Thus they do not
falsify the intended global exchange theorem.  They prove that a
block-cut peel cannot follow merely from the labelled model, minor
exclusion, non-two-apexness, and the exact carrier geometry.

The solver-free executable certificate is
`hc7_near_k7_single_portal_block_cut_barrier_verify.py`.

## 1. The coherent shell

Start with six vertices

\[
                      D,E,U_1,U_2,U_3,U_4
\]

forming a clique.  Add the path core `P=p_Lp_R`.  Add a carrier

\[
 K_s=G[\{g,z,w,x\}]\quad(s=1),
 \qquad
 K_s=G[\{g,z,w,x,y\}]\quad(s=2),
\]

with edges

\[
                gz,\ zw,\ wx,
                \quad\hbox{and, for }s=2,\ wy.
\]

Join `g` to both `p_L,p_R` and to every `U_i`.  Join `p_L` to
`U_1,U_2`, and `p_R` to `U_3,U_4`.  Join `x` to `E`, and in the
two-portal version join `y` to `E`.  There are no other shell edges.

Put

\[
                        A=P\cup K_s.
\]

Then

\[
                  A,D,E,U_1,U_2,U_3,U_4                 \tag{1.1}
\]

is a spanning labelled `K_7^vee` model of the shell.  In fact it has
only one absent spoke: `AD`.  The piece `K_s` crosses the path cut
because `g` has neighbours on both sides.

For the concentrated row `Q=E`, the portal set is `{x}` in the first
graph and `{x,y}` in the second.  In the second graph, deleting `z`
separates the portal arm `{w,x,y}` from the path-side attachment set

\[
                  A_L=A_R=\{g\}.                            \tag{1.2}
\]

Thus it is precisely the genuine cutvertex portal-arm outcome in the
audited flexible two-portal theorem.  The side attachment families happen
to coincide at the one vertex `g`, but they are not contained in the
separator `{z}`.

## 2. No literal shore completion

### Proposition 2.1

There are no disjoint connected sets `X,Y subseteq A` which are
adjacent and each adjacent to all five retained foreign rows

\[
                         E,U_1,U_2,U_3,U_4.                 \tag{2.1}
\]

#### Proof

Inside `A`, the only vertices seeing `E` are `x` and, in the second
graph, `y`.  The only vertices seeing both pairs of neutral rows are as
follows: a set sees all four `U_i` only if it contains `g`, or contains
both `p_L` and `p_R`.  This follows directly from the displayed contact
list.

Two disjoint sets cannot both contain `g`.  Hence one of two proposed
shores, say `X`, must contain both `p_L,p_R`.  If `X` also sees `E`, it
contains `x` or `y`.  Every path in `A` from `{p_L,p_R}` to `{x,y}`
uses `g`, because the carrier tail is attached to the path triangle only
at `g`.  Thus connectedness forces `g in X`, leaving the other shore no
way to see all four neutral rows.  This contradiction proves the claim.
\(\square\)

In the one-portal graph the obstruction is even more immediate: two
disjoint shores cannot both contain the unique `E`-neighbour `x`.

## 3. `K_7` exclusion in the shell

Each shell has a tree decomposition of width five.  A central bag is

\[
                       \{D,E,U_1,U_2,U_3,U_4\}.             \tag{3.1}
\]

The remaining bags are listed and checked in the verifier.  They have
order at most six and cover the path triangle and the carrier tail while
preserving the running-intersection property.  Therefore the shell has
treewidth at most five and contains no `K_7` minor.

## 4. Making the obstruction non-two-apex without adding `K_7`

Take a disjoint copy of `K_{3,3,3}` and identify one of its vertices
with the shell vertex `D`.  Absorb all nine tripartite vertices into the
foreign bag labelled `D`.  The model (1.1) is now spanning; the enlarged
`D` bag remains connected and remains anticomplete to `A`.

Call the resulting graph `G_s`.  It is a one-sum of the width-five shell
and `K_{3,3,3}` at `D`.  A clique minor of order at least three cannot
use branch sets essentially on both sides of a one-separation.  The
shell has no `K_7` minor by Section 3, and `K_{3,3,3}` has no `K_7`
minor: a seven-bag model on nine vertices would have at least five
singleton bags, while at most one singleton bag can lie in each of its
three independent parts.  Hence `G_s` is `K_7`-minor-free.

No deletion of two vertices makes `G_s` planar.  The retained
`K_{3,3,3}` loses at most two vertices.  Its three part sizes are then,
up to domination, `(1,3,3)` or `(2,2,3)`, and the remainder contains a
`K_{3,3}` subgraph.  Thus `G_s` is not two-apex.

On the other hand `D` is a cutvertex separating the tripartite summand
from the shell.  This is the exact failed global axiom.  Seven-
connectivity must be used to turn the carrier's external contacts into a
second literal portal, a protected side fan, a colour-gluable adhesion,
or one coherent rural expansion.  None of those conclusions follows
from the local block-cut tree alone.

## 5. Trust boundary

The examples refute either unqualified implication

\[
\begin{aligned}
 &\text{one literal row portal}+\text{coherent labelled near model}
      \Longrightarrow\text{shore completion},\\
 &\text{two portals in one cutvertex arm}+\text{non-two-apex}
      \Longrightarrow\text{a legal block-cut peel}.
\end{aligned}
\]

They do not refute a theorem retaining seven-connectivity or
contraction-critical operation states.  Indeed their one-separation is
deliberate: it makes precise the global input which the next recursion
must exploit.
