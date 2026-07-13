# Final audit: the sole-exterior all-crossless pure-Moser cell

## Verdict

**Valid, under the exact hypotheses below.** In particular, no
simultaneous-embedding assumption is missing: the five separate-looking
frame failures are precisely all crossings of one ordered five-terminal
tuple, and hence one application of the generalized Two Paths Theorem
produces one pentagonal web.

## Exact statement

Let \(G\) be a finite seven-connected graph and let \(v\in V(G)\) have
degree seven. Write

\[
N_G(v)=U\mathbin{\dot\cup}\{a,b\},\qquad |U|=5,
\]

where \(ab\notin E(G)\), \(G[U]\cong C_5\), and \(G-N[v]\) has exactly
one nonempty component \(C\). Index

\[
U=\{u_0,u_1,u_2,u_3,u_4\}
\]

so that the nonedges of \(G[U]\) are \(u_i u_{i+1}\), with indices
modulo five. Thus the cyclic order of the **edges** of \(G[U]\) is

\[
\Omega=(u_0,u_2,u_4,u_1,u_3).
\]

For two vertex-disjoint nonedges \(u_i u_{i+1}\) and
\(u_j u_{j+1}\), call their frame crossed in \(C\) if \(C\) contains
vertex-disjoint paths joining the corresponding two pairs of portal
sets \(N_C(u_i),N_C(u_{i+1})\) and
\(N_C(u_j),N_C(u_{j+1})\). A one-vertex path is allowed when the two
portal sets meet.

If none of the five frames is crossed, then \(G\) is six-colourable.

For the pure Moser spindle with repeated pair \(a=1,b=3\), all the
hypotheses concerning \(G[N(v)]\) hold. Seven-connectivity also implies
\(N_G(C)=N_G(v)\), although the proof below only needs the portal
encoding and the fact that \(v\notin N_G(C)\).

## Proof

Form \(A\) from \(G[C]\) by adjoining independent artificial terminals
\(t_0,\ldots,t_4\), where

\[
N_A(t_i)=N_C(u_i),
\]

and order the terminals as

\[
T=(t_0,t_2,t_4,t_1,t_3).
\tag{1}
\]

A crossing of \(T\) is a pair of vertex-disjoint \(T\)-paths whose four
ends alternate in (1). After any one terminal is omitted, the unique
alternating pairing of the remaining four labels consists of two
vertex-disjoint edges of the complementary cycle
\(u_0u_1u_2u_3u_4u_0\). Conversely, every pair of vertex-disjoint
edges of that complementary cycle occurs for exactly one omitted
terminal. Deleting the artificial ends converts a tuple crossing into
the corresponding two portal paths in \(C\), and adjoining the terminal
edges reverses the operation. Therefore

\[
T\text{ is crossed in }A
\quad\Longleftrightarrow\quad
\text{one of the five Moser frames is crossed in }C.
\tag{2}
\]

Assume all five frames are crossless. By the generalized Two Paths
Theorem (Humeau--Pous, Theorem 1.5), \(A\) has an edge-only completion,
on the same vertex set, to a five-web \(W\) with frame \(T\). Thus
\(W\) consists of a plane five-rib \(R\), whose outer cycle is (1), and
possibly a clique \(X_F\) inserted behind each facial triangle \(F\) of
\(R\). Every vertex of \(X_F\) is adjacent in \(W\) only to
\(X_F\cup V(F)\).

We claim that every \(X_F\) is empty. Artificial terminals are frame
vertices and hence rib vertices, so a nonempty \(X_F\) is a subset of
\(C\). Every original edge incident with \(X_F\) that is represented in
\(A\) has its other end in \(X_F\cup V(F)\). Replace every artificial
terminal \(t_i\in V(F)\) by its actual boundary vertex \(u_i\), leaving
the vertices of \(F\cap C\) unchanged, and call the resulting set
\(\widehat F\). Then \(|\widehat F|=3\). All edges from \(X_F\) to
\(U\) are accounted for in this way, because an edge \(xu_i\) in \(G\)
is represented by \(xt_i\) in \(A\). The only vertices of \(N[v]\)
not represented in \(A\) are \(a,b,v\), and \(v\) has no neighbour in
\(C\). Since \(C\) is the sole component of \(G-N[v]\), there are no
other possible neighbours. Consequently

\[
N_G(X_F)\subseteq \widehat F\cup\{a,b\},
\qquad |N_G(X_F)|\le 5.
\tag{3}
\]

The vertex \(v\) lies outside \(X_F\cup N_G(X_F)\), so (3) is a genuine
vertex cut separating the nonempty set \(X_F\) from \(v\). This
contradicts seven-connectivity. Hence \(W=R\), and in particular all
original vertices and edges of \(A\) lie in one plane rib.

Delete from \(R\) every completion edge except its five outer-frame
edges and the original edges of \(A\). Relabel \(t_i\) as \(u_i\).
Portal edges then become exactly the original \(U\)-to-\(C\) edges, and
the five outer-frame edges become exactly the five edges of \(G[U]\),
because (1) is its cyclic order. The resulting embedded graph is
precisely

\[
G[C\cup U],
\]

drawn in a closed disk with \(G[U]\) as its boundary cycle.

The Four Colour Theorem gives a proper four-colouring of
\(G[C\cup U]\). Give both \(a,b\) a fifth colour and \(v\) a sixth.
This is proper: \(ab\notin E(G)\), \(v\) has no neighbour in \(C\), and
all remaining vertices are in \(C\cup U\cup\{a,b,v\}\). Thus \(G\) is
six-colourable.

## What was essential

1. The tuple order must be the present-cycle (pentagram) order, not the
   missing-cycle order.
2. The generalized theorem must be used in its same-vertex,
   edge-completion form. Adding vertices would invalidate the cut
   argument.
3. Completion edges other than the five frame edges must be deleted
   before relabelling the artificial terminals.
4. The unique-exterior hypothesis is used to make (3) exhaustive; with
   another exterior component, its vertices could be additional
   neighbours unless anticompleteness is separately supplied.

The conclusion eliminates the whole all-crossless family of arbitrary
order. It does **not** eliminate the crossed-frame residue.
