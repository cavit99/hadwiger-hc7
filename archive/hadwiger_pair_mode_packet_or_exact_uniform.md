# Uniform packet-or-exact theorem for palette-tight pair modes

## 1. Statement

Let \(q\ge3\), put \(k=2q+1\), and let \(G\) be a
\(k\)-connected graph with minimum degree at least \(k\). Let \(S\)
be a \(k\)-cut and let \(C\) be a full component of \(G-S\), of
order at least two, with a nonempty far component. Fix a pair mode

\[
 S=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q
   \mathbin{\dot\cup}\{r\},\qquad |B_i|=2.        \tag{1.1}
\]

### Theorem 1.1 (uniform pair-mode ownership)

At least one of the following holds.

1. \(C\) has two-block capacity for (1.1).
2. A nonempty proper connected subset of \(C\) is a component behind
   another exact \(k\)-cut.

For \(q=3\), this is Theorem 1.2 of
hadwiger_atomic_threeblock_nonowner_collapse.md. The proof below shows
that its carrier/face/curvature mechanism is completely label-free and
works for every \(q\ge3\).

## 2. Degree and short-carrier reductions

Assume outcome 1 fails. If some \(x\in C\) has degree exactly \(k\),
then \(N_G(x)\) is an exact \(k\)-cut: \(\{x\}\) is one component
after its deletion and the far shore remains. Since \(|C|\ge2\), this
is outcome 2. We may therefore assume

\[
 d_G(x)\ge k+1=2q+2\qquad(x\in C).                \tag{2.1}
\]

No vertex of \(C\) sees both roots of a block \(B_i\). Such a vertex
would be a singleton \(B_i\)-carrier. The uniform small-carrier theorem
has \(p=q\) and

\[
 1<q-1,
\]

so it would force two-block capacity, with no exact-cut alternative.
Thus every shore vertex sees at most one root in each pair block and
possibly \(r\). Consequently

\[
 |N_S(x)|\le q+1,\qquad d_C(x)\ge q+1.            \tag{2.2}
\]

The small-shore rigidity theorem says that a nonowner with
\(|C|\le q\) is a singleton. Hence

\[
 |C|>q.                                           \tag{2.3}
\]

## 3. Internal connectivity and a bare portal face

Assume outcome 2 also fails. The separator-capacity theorem applied to
(1.1) shows that \(C\) is \(q\)-connected: a separator of order at
most \(q-2\) forces capacity, and a separator of order \(q-1\)
exposes an exact \(k\)-cut.

Choose two blocks \(B_i,B_j\). Their packet fails. Apply the
set-terminal Two Paths Theorem to their four full portal sets. Every
inserted clique part behind a facial triangle would be separated from
the far shore by:

* at most three rib vertices or represented boundary labels; and
* the \(k-4\) omitted boundary labels.

The resulting separator has order at most

\[
 3+(k-4)=k-1,
\]

contrary to \(k\)-connectivity. Hence the web is bare: \(C\) is planar
and has a face \(F_{ij}\) containing the four full portal sets of
\(B_i\cup B_j\).

Since a planar graph has connectivity at most five, the
\(q\)-connectivity of \(C\) already proves the theorem for
\(q\ge6\). It remains that

\[
 q\in\{3,4,5\}.                                   \tag{3.1}
\]

In particular \(C\) is three-connected and its plane embedding is
unique up to reflection.

## 4. All pair-demand faces coincide

For every two block indices \(i,j\), packet failure gives a face
\(F_{ij}\) containing their four full portal sets.

Fix distinct \(i,j,h\). If \(F_{ij}\ne F_{ih}\), their intersection
contains both full portal sets of \(B_i\). In a three-connected plane
graph, two distinct faces meet in at most a vertex or one edge. Hence
the union of the two portal sets of \(B_i\) is contained in a connected
set \(X\) of order at most two.

The set \(X\) is a \(B_i\)-carrier, and \(C-X\ne\varnothing\) by
(2.3). Apply the uniform small-carrier theorem. For \(q=3\), it gives
capacity or an exact cut; for \(q=4,5\), its strict size inequality
forces capacity. Every outcome contradicts the current assumptions.
Thus

\[
 F_{ij}=F_{ih}.
\]

Connectivity of the graph of two-element index sets now shows that all
faces \(F_{ij}\) are one face \(F\). This one face contains every
vertex of every portal set belonging to all \(2q\) pair roots.

## 5. Curvature contradiction

Choose \(F\) as the outer face and triangulate every bounded face.
An interior shore vertex lies in none of the \(2q\) pair-root portal
sets, so among \(S\) it can see only \(r\). By (2.1),

\[
 d_T(x)\ge d_C(x)\ge2q+1\ge7
 \qquad(x\in\operatorname{int}T).                 \tag{5.1}
\]

For an outer vertex, (2.2) gives

\[
 d_T(x)\ge d_C(x)\ge q+1\ge4.                    \tag{5.2}
\]

The triangulated-disk identity

\[
 \sum_{x\in\operatorname{int}T}(6-d_T(x))
 +\sum_{x\in\partial T}(4-d_T(x))=6
\]

now has a nonpositive left side, a contradiction. Thus outcome 1 or
outcome 2 must occur, proving Theorem 1.1. \(\square\)

## 6. Significance and limitation

This is a genuine uniform contact-or-separator theorem. It eliminates
all packet-deficient nonsingleton shores for palette-tight boundaries
consisting of pair blocks plus one singleton; the only escape is an
exact adhesion.

Its limitation is quantitative and explicit: it assumes ambient
\((2q+1)\)-connectivity for a boundary of order \(2q+1\). General
minimal Hadwiger counterexamples are currently known to have much lower
connectivity. A full proof still needs a mechanism producing such a
palette-tight highly connected adhesion, or a relative version in which
failure of connectivity itself becomes a colour-gluable separator.
