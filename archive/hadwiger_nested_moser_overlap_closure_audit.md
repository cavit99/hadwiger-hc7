# Adversarial audit: nested Moser overlap closure

## Verdict

**GREEN.**  Both overlap lifts are valid, their branch sets are
pairwise disjoint and pairwise adjacent, and the low-owner descent
supplies all required overlap, matching, fullness, and helper
hypotheses.

The exact resulting theorem is:

> In the hypothetical \(HC_7\) counterexample setting, a
> three-component seven-cut with pure-Moser boundary produces a proper
> nested exact seven-cut with exactly two components.

This is conditional on the already installed inputs:

1. the low-owner finite-or-descent theorem;
2. exclusion of its full-singleton endpoint;
3. the bound of three on the number of components behind a seven-cut;
   and
4. the classification of a three-component seven-cut boundary as the
   pure Moser spindle.

It closes the three-component recursion but does not eliminate the
resulting two-component exact adhesion.

## 1. Five-root Moser certificate

For every five-set \(R\) in a pure Moser spindle there is a
\(K_3\)-model \(L_1,L_2,L_3\) with

\[
|L_i\cap R|=1
\]

for each \(i\), avoiding the other two vertices of \(R\).

If \(R\) contains a triangle, its three vertices are singleton bags.
The only triangle-free five-sets in the standard Moser labelling are

\[
\begin{aligned}
&01356,\quad01456,\quad02356,\quad02456.
\end{aligned}
\]

For these, respectively, the models are

\[
\begin{array}{c|c}
01356&024\mid5\mid6\\
01456&023\mid5\mid6\\
02356&014\mid5\mid6\\
02456&013\mid5\mid6.
\end{array}
\]

The three-vertex bag in each row is connected.  It sees both singleton
bags through one of its vertices, and \(56\) is an edge.  This verifies
all twenty-one five-subsets without relying on the forty-case nested
quotient probe.

## 2. Five-root overlap branch sets

Let \(R=S\cap T\), let \(S-R=\{u,v\}\), and let
\(r_i\) be the unique root in \(L_i\cap R\).  Write the other two roots
as \(r_4,r_5\).  The seven bags are

\[
A_1u,\quad A_2v,\quad C_1r_4,\quad C_2r_5,\quad
L_1,\quad L_2,\quad L_3.
\]

Here concatenation denotes union.

They are disjoint because the four helpers avoid \(S\cup T\), the old
exclusive roots \(u,v\) are outside \(T\), and the \(K_3\)-model avoids
\(r_4,r_5\).  They are connected by fullness.

Every bag containing an old root is adjacent to each \(A_j\)-bag,
because \(A_j\) is full to \(S\).  This includes the two \(C\)-bags,
whose anchors \(r_4,r_5\) lie in \(S\).  Every \(C_j\)-bag is adjacent
to the other \(C\)-bag and to every \(L_i\), because its helper is full
to \(T\).  Finally the \(L_i\) are pairwise adjacent by their
\(K_3\)-model.  No unasserted helper-helper edge is used.

This hand lemma strictly subsumes all forty hard cases in
moser_nested_overlap_probe.py.  It does not require compatibility
between the two induced Moser graphs beyond the fact that their common
vertex set has order five.

## 3. Matched one-root branch sets

For \(S\cap T=\{s\}\), the six edges \(x_i y_i\) make seven disjoint
connected rung bags

\[
\{s\},\quad\{x_i,y_i\}\ (1\le i\le6).
\]

Choose the three rungs whose old roots form a triangle in \(G[S]\).
Leave them unchanged and assign \(A_1,A_2,C_1,C_2\) to the other four
rungs.

An \(A\)-enlarged rung is adjacent to every rung through its old root,
and a \(C\)-enlarged rung is adjacent to every rung through its new
root.  This also verifies every pair of enlarged bags.  The three
unenlarged rungs are pairwise adjacent through the old triangle.
Connectivity holds even when a helper is assigned to the shared rung
\(\{s\}\), since \(s\) belongs to both frames.

Thus every such matched one-root configuration contains a rooted
\(K_7\).  An independent exhaustive check over the three old-vertex
orbits and all \(630\) labelled new Moser frames in each orbit found no
failure, but the displayed branch-set proof makes that computation
unnecessary.

## 4. Helpers supplied by the descent

Let the original cut have components \(D,A_1,A_2\), and let
\(C\subsetneq D\) be the connected exact fragment with boundary
\(T=N_G(C)\).

Since \(T\) is a seven-cut in a seven-connected graph, every component
of \(G-T\) is full to \(T\).  The old sets \(A_1,A_2\) are connected,
disjoint, and full to \(S\).

In either descent geometry, \(S-T\) is nonempty.  Every vertex of
\(S-T\) has a neighbour in each old full shore, so

\[
A_1\cup A_2\cup(S-T)
\]

lies in one component \(O\) of \(G-T\).  If \(G-T\) has three
components, the other two are \(C\) and a component \(C'\).  Neither
contains an old boundary vertex: all of \(S-T\) lies in \(O\), while
\(S\cap T\) was deleted.  Hence \(C,C'\) are disjoint from
\(S\cup T\), and they are disjoint connected full helpers for the new
frame.  This verifies the hypothesis that was implicit in the first
version of the application; it is now explicit in the source.

## 5. The two overlap geometries

For a two-cut descent,

\[
T=\{p,q\}\cup N_S(C),\qquad |N_S(C)|=5,
\]

where \(p,q\in D\).  Therefore \(S\cap T=N_S(C)\) has order five.
If \(G-T\) had three components, its boundary classification gives a
pure Moser graph on \(T\), and the five-root overlap lift gives
\(K_7\).

For a three-face descent,

\[
T=\{s\}\cup\{y_x:x\in S-\{s\}\}.
\]

The six \(y_x\) are distinct shore vertices and satisfy \(xy_x\in
E(G)\).  Thus the frames overlap only in \(s\) and have the six rooted
rungs required by the one-root lemma.  The old pure Moser boundary
contains a triangle, so three components behind \(T\) again force
\(K_7\).

The component bound leaves at most three components behind \(T\), and
the exact fragment \(C\) plus the outer component show that there are at
least two.  Excluding three therefore leaves exactly two.

## 6. Scope

The original forty-case script is a correct positive diagnostic for the
four hard omitted pairs, but it is no longer part of the proof.  The
five-root hand lift covers those cases and the seventeen easy omitted
pairs uniformly.

The matched one-root lift likewise replaces a much larger alignment
enumeration.  The remaining obstruction is genuinely the
two-component exact-cut problem; no claim in this note closes it.

