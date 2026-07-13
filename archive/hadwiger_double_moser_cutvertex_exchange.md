# Cutvertices in the double-Moser body force a minor or an exact cut

## 1. Setting

Use the double-Moser endpoint of
hadwiger_double_moser_two_component_closure.md. Thus \(u,v\) are
adjacent degree-seven vertices, their four common neighbours
\(X=\{x_1,x_2,x_3,x_4\}\) induce \(2K_2\), and

\[
I=\{x_1,x_2,x_3,x_4,a,b,p,q\}
\]

is the eight-vertex interface of the sole connected body \(R\).
The mandatory core edges are

\[
\begin{aligned}
&uv,\quad uX,\quad vX,\quad up,uq,\quad va,vb,\\
&x_1x_2,\quad x_3x_4,\quad ab,\quad pq,\\
&ax_1,ax_2,\quad bx_3,bx_4,\quad
qx_1,qx_2,\quad px_3,px_4.
\end{aligned}                                                   \tag{1.1}
\]

We prove an infinite-family reduction:

> If \(R\) has a cutvertex, then \(G\) has a \(K_7\)-minor or a
> component of \(R\) lies behind a new exact seven-cut.

The only finite input is a two-row quotient lemma on the fixed
eight-vertex interface.

## 2. Lobe defects

Let \(z\) be a cutvertex of \(R\), and let \(D\) be a component of
\(R-z\). No vertex of \(D\) is adjacent to \(u\) or \(v\), and it has
no edge to another component of \(R-z\). Hence

\[
                         N_G(D)\subseteq I\cup\{z\}.              \tag{2.1}
\]

There is a different component of \(R-z\) on the far side, so
\(N_G(D)\) is a genuine separator. Seven-connectivity gives

\[
                 |N_I(D)|\ge6.                                  \tag{2.2}
\]

Define the defect

\[
                 \Delta(D)=I-N_I(D),\qquad |\Delta(D)|\le2.       \tag{2.3}
\]

Because \(R\) is connected, every component of \(R-z\) has a neighbour
at \(z\). Consequently equality holds in the structural description

\[
                         N_G(D)=N_I(D)\cup\{z\}.                  \tag{2.4}
\]

## 3. The two-lobe quotient lemma

Contract two distinct lobes to nonadjacent vertices \(d_1,d_2\), retain
the cutvertex \(z\) adjacent to both, and retain the core (1.1).
For the conservative maximal rows, each \(d_i\) is adjacent to exactly
six vertices of \(I\), so its defect is a two-subset of \(I\).

### Lemma 3.1 (finite two-lobe atlas)

Among the \(\binom82^2=784\) ordered pairs of two-element defects, the
conservative quotient fails to contain a \(K_7\)-minor for exactly
twenty-two ordered pairs. They form three orbits under the automorphism
group of the double-Moser core and interchange of the two lobes, with
representatives

\[
\begin{aligned}
&\{x_1,x_3\}\mid\{x_2,x_4\},\\
&\{x_1,a\}\mid\{x_3,p\},\\
&\{a,b\}\mid\{p,q\}.                                \tag{3.1}
\end{aligned}
\]

In particular, the two defects in every exceptional pair are disjoint.
The exhaustive audit also verifies the stronger facts that restoring
any omitted contact makes the quotient positive and that the residual
relation is triangle-free, but the cutvertex theorem needs only
disjointness.

#### Verification

The dependency-free program double_moser_cutvertex_lobe_probe.cpp
constructs all \(784\) quotients. For each quotient it enumerates every
nonempty connected vertex subset and performs an exact backtracking
search for seven disjoint pairwise adjacent subsets. It prints the
twenty-two failures, retests every single-contact restoration, and
checks all triples in the residual relation. Its audited summary is:

    profiles=784 negative=22
    single-contact restorations surviving=0
    residual relation triangles=0

The quotient has thirteen vertices, so this is a finite exhaustive
certificate. Every positive quotient model lifts by replacing \(d_i\)
with the original connected lobe \(D_i\). Extra interface contacts and
extra edges incident with \(z\) can only preserve the lifted model.

## 4. Cutvertex closure

### Theorem 4.1

If \(z\) is a cutvertex of \(R\), then either \(G\) contains a
\(K_7\)-minor or some component of \(R-z\) is a component behind an
exact seven-cut.

#### Proof

Let \(D_1,\ldots,D_m\) be the components of \(R-z\), where \(m\ge2\).
By (2.3), every defect has order at most two.

If some \(\Delta(D_i)\) has order two, then

\[
             N_G(D_i)=\{z\}\cup\bigl(I-\Delta(D_i)\bigr),
\]

which has order exactly seven. It separates \(D_i\) from another lobe,
so it is an exact seven-cut.

It remains that all lobe defects have order at most one. Choose any two
lobes \(D_1,D_2\). Since
\(|\Delta(D_1)\cup\Delta(D_2)|\le2<|I|\), choose

\[
e\in I-\bigl(\Delta(D_1)\cup\Delta(D_2)\bigr).
\]

Enlarge each actual defect to a two-subset
\(\Delta_i'\supseteq\Delta(D_i)\) containing \(e\), and delete the
corresponding surplus lobe-interface edges. The two conservative defects
intersect at \(e\). Lemma 3.1 says that every negative pair has disjoint
defects, so this conservative quotient has a \(K_7\)-model. It lifts to
\(G\), completing the proof. \(\square\)

### Corollary 4.2

In the branch in which \(R\) contains no proper component behind an
exact seven-cut, the eight-interface double-Moser body \(R\) is
2-connected.

This is a local dichotomy. Replacing the current body by a fragment
behind the new cut need not preserve the double-Moser interface, so any
global descent or colour-gluing step must be supplied separately.

### Lemma 4.3 (the rooted exterior is 2-connected)

Put \(C=R\cup\{a,b\}\). If \(R\) is 2-connected, then either \(C\) is
2-connected, \(G\) contains a \(K_7\)-minor, or \(G\) has a proper exact
seven-cut.

#### Proof

Since \(R\) is connected and both \(a,b\) have an \(R\)-neighbour,
neither \(a\) nor \(b\) is a cutvertex of \(C\). Suppose
\(z\in R\) is a cutvertex of \(C\). The graph \(R-z\) is connected.
Because \(ab\) is an edge, \(C-z\) can be disconnected only when

\[
                         N_R(a)=N_R(b)=\{z\}.                    \tag{4.1}
\]

Thus

\[
 N_G(\{a,b\})=\{z,v,x_1,x_2,x_3,x_4\}
               \cup N_{\{p,q\}}(\{a,b\}).                       \tag{4.2}
\]

This is a genuine separator. Seven-connectivity says that the last
term is nonempty. If it has order one, (4.2) is an exact seven-cut.

If both \(p,q\) occur, contract the connected body \(R\) to a vertex
\(h\), which is complete to the interface \(I\). Up to the symmetries
of the double-Moser core, the minimal \(a,b\)-to-\(p,q\) contact
patterns and corresponding \(K_7\)-models are:

\[
\begin{array}{c|l}
ap,aq&
\{u,x_1\}\mid\{v,q,x_2\}\mid\{x_3\}\mid\{x_4\}
\mid\{a,b\}\mid\{p\}\mid\{h\}\\
ap,bq&
\{u,x_3\}\mid\{v,b\}\mid\{x_1\}\mid\{x_2\}
\mid\{a,p\}\mid\{q\}\mid\{h\}\\
aq,bp&
\{u,x_1,a\}\mid\{v,q,x_2\}\mid\{x_3\}\mid\{x_4\}
\mid\{b\}\mid\{p\}\mid\{h\}.
\end{array}                                                       \tag{4.3}
\]

The case in which \(b\) meets both \(p,q\) is symmetric to the first
row. The displayed bags are connected and a direct check with (1.1)
shows that they are pairwise adjacent. Additional contacts only help.
\(\square\)

Consequently, by the standard \(st\)-numbering theorem for 2-connected
graphs, an adhesion-minimal residual admits an \(ab\)-numbering:
an ordering from \(b\) to \(a\) in which every proper prefix and suffix
induces a connected subgraph. This is the natural setting for the
rank-two portal-state exchange.

## 5. Structural significance

The proof does not enumerate bodies \(R\), their orders, or their
internal graphs. It converts a cutvertex into a family of almost-full
anticomplete lobes and uses only one invariant of the fixed finite
interface:

\[
\text{every quotient-negative pair of maximal lobe defects is disjoint.}
\]

Thus the unresolved one-body exchange has moved strictly past block
decomposition. It now lives in a 2-connected body and must be attacked
by an ear, two-path/web, or contraction-critical exchange argument.

## 6. Label-free form

The argument is not intrinsically tied to the Moser labels.

### Proposition 6.1 (intersecting-defect cutvertex principle)

Let \(G\) be \(k\)-connected, let a connected body \(R\) have all its
external neighbours in an interface \(I\) of order \(k+1\), and fix any
minor target whose existence is monotone under adding interface contacts.
Suppose the following finite boundary property holds:

> In the quotient consisting of a cutvertex and two anticomplete lobes,
> each adjacent to exactly \(k-1\) vertices of \(I\), every
> target-negative pair of two-element defects is disjoint.

Then a cutvertex of \(R\) forces either the target minor or a proper
exact \(k\)-cut.

#### Proof

A lobe behind the cutvertex has at least \(k-1\) neighbours in \(I\),
so its defect has order at most two. A two-defect lobe has exactly the
cutvertex plus \(k-1\) interface neighbours and therefore lies behind an
exact \(k\)-cut. If all defects have order at most one, choose two lobes
and enlarge their defects to two-sets sharing a fresh interface element.
The assumed finite boundary property makes that conservative quotient
target-positive, and monotonicity lifts the target to \(G\). \(\square\)

For the double-Moser core, Lemma 3.1 verifies the finite hypothesis with
\(k=7\) and target \(K_7\). This is the reusable mechanism extracted
from the local atlas.
