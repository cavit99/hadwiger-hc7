# Barrier: colour saturation does not repair a labelled carrier split

**Status:** dependency-free finite certificate.  This graph is not a
hypothetical `HC_7` counterexample.  It is four-colourable, contains a
literal `K_7` model, and its boundary is `K_{3,4}` rather than one of the
final width-two frontiers.

The example isolates three unsafe intermediate inferences.  Even in an
exactly seven-connected graph with an actual packet vector `(1,2)`, a
unique compulsory portal, and a shared double-contraction colouring:

1. a literal path core need not have a list-compatible two-carrier split;
2. failure of that split need not expose a separator of order at most six;
3. five-colour saturation at the thin endpoint, or simultaneously at both
   rich endpoints, does not by itself change a literal carrier list.

The executable certificate is
[`hc7_atomic_connector_saturation_barrier_verify.py`](hc7_atomic_connector_saturation_barrier_verify.py).

## 1. The eleven-vertex graph

Put

\[
 S=\{s,t,w\}\mathbin{\dot\cup}\{a,b,c,d\},\qquad
 A=\{p,q\},\qquad R=\{r_1,r_2\}.
\]

The boundary graph is the complete bipartite graph

\[
               G[S]=K_{\{s,t,w\},\{a,b,c,d\}}.
\]

Inside the open shores add the two edges `pq` and `r1r2`.  Give the thin
vertices the contacts

\[
 N_S(p)=S-\{s\},\qquad N_S(q)=S-\{t\},                 \tag{1.1}
\]

and make each of `r1,r2` complete to `S`.  There are no `A-R` edges.

The verifier exhausts every deletion of at most six vertices and confirms
that the remaining graph is connected.  Deleting `S` disconnects the two
open shores, so

\[
                            \kappa(G)=7.                 \tag{1.2}
\]

It also enumerates every connected `S`-full subset of both shores.  The
only one in `A` is `{p,q}`, whereas both rich singletons are full.  Hence

\[
                         (\nu_A,\nu_R)=(1,2).             \tag{1.3}
\]

## 2. Unique portal and failed carrier orientation

Let

\[
                         e=pt,\qquad z=p.
\]

Equation (1.1) gives `N_A(t)={p}`, so `e` is the unique thin--`t` portal.
The literal path

\[
                             t-p-q-s                       \tag{2.1}
\]

has internal vertex set `A`; its selected core `T=pq` is already a path.

There is only one unordered partition of `T` into two nonempty disjoint
connected adjacent carriers, namely `{p}|{q}`.  Give these carriers labels
`1,2`.  Every boundary vertex has a nonempty literal contact list, but

\[
                         \Lambda(s)=\{2\},\qquad
                         \Lambda(t)=\{1\}.                \tag{2.2}
\]

The vertices `s,t` lie in the same bipartition class of `G[S]` (indeed
`s-a-t` is a path of even length).  Every proper two-colouring of their
component therefore gives them the same carrier label, contradicting
(2.2).  Reversing the carrier names reverses both singleton lists and leaves
the contradiction unchanged.  Thus the exact two-carrier list instance is
not colourable.

By (1.2), this failure cannot yield a vertex separator of order at most
six.

## 3. Saturated double-contraction state

Take the rich edge

\[
                              f=r_1r_2.
\]

The following is a proper six-colouring of `G-{e,f}` and hence the lift of
a colouring of `G/e/f`:

\[
\begin{array}{c|c}
\text{vertices}&\text{colour}\\ \hline
p,t,s&0\\
r_1,r_2,q&1\\
w&2\\
a,b&3\\
c&4\\
d&5.
\end{array}                                                \tag{3.1}
\]

All six colours occur.  Outside its mate `t`, the vertex `z=p` sees all
five alternative colours, respectively at `q,w,a,c,d`.  More strongly,
outside their mutual mate, both `r1` and `r2` see all five colours other
than `1` on the literal boundary.  Thus both saturation signals from the
double-contraction split occur in the same colouring.

They do not alter (1.1), and therefore do not repair the incompatible
lists (2.2).  Saturation records coloured neighbours; it does not assign
those neighbours to a movable labelled carrier piece.

## 4. Exact trust boundary

The construction deliberately triggers a permitted terminal outcome.  The
seven branch sets

\[
 \{d,r_1,r_2\},\quad \{q\},\quad \{p\},\quad
 \{c,t\},\quad \{b,s\},\quad \{a\},\quad \{w\}           \tag{4.1}
\]

are connected, disjoint, and pairwise adjacent.  They form a literal
`K_7` model.  The graph also has the proper four-colouring

\[
 \{s,t,w\}\mid\{p,r_1\}\mid\{q,r_2\}\mid\{a,b,c,d\}.
                                                               \tag{4.2}
\]

Consequently this certificate does **not** falsify the active
terminal-disjunctive composition theorem.  It proves the narrower and
useful dependency statement:

> A positive connector-composition proof must turn saturation into a
> literal list-changing carrier move, or spend `K_7`-minor-freeness and the
> universal minor-critical response to obtain a terminal or descent.
> Saturation, seven-connectivity, and the packet vector alone cannot be
> counted as carrier repair.

There is a separate definitional warning about the path-or-`Y` core.  An
arbitrary inclusion-minimal Steiner subgraph containing `z` and all
vertices of a connector path can have degree four: a new hub may join `z`
and three path vertices while the original path edges are omitted.  The
safe statement is selectional.  Retain the literal connector subpath and
add a shortest `z`-to-path route stopped at its first hit.  That selected
edge union is a path or a `Y`; it need not be induced, and all omitted
chords and external bridges must remain in the bridge decomposition.
