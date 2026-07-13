# Boundary universality and exclusion of critical planar webs

## 1. Extension sets

Let \(L\) be an \(S\)-boundaried graph and let

\[
 {\cal E}_r(L,S)
\]

denote the set of labelled proper \(r\)-colourings of \(S\) which
extend to \(L\).

### Lemma 1.1 (common-family gluing)

Let \(G=L\cup_S M\) be a proper separation. If there is a nonempty
family \({\cal F}\) of boundary states such that

\[
 {\cal F}\subseteq {\cal E}_r(L,S)\cap{\cal E}_r(M,S),
\]

then \(G\) is \(r\)-colourable.

More generally, it is enough that

\[
 {\cal F}\subseteq{\cal E}_r(L,S)
 \quad\hbox{and}\quad
 {\cal F}\cap{\cal E}_r(M,S)\ne\varnothing.
\tag{1.1}
\]

#### Proof

Choose a state in the displayed intersection, extend it on both sides,
and glue the extensions. \(\square\)

Consequently, in a non-\(r\)-colourable graph,

\[
 {\cal E}_r(L,S)\cap{\cal E}_r(M,S)=\varnothing.
\tag{1.2}
\]

If every proper minor is \(r\)-colourable, an internal operation
\(\mu\) on \(L-S\) further forces

\[
 \bigl({\cal E}_r(L^\mu,S)\setminus{\cal E}_r(L,S)\bigr)
 \cap{\cal E}_r(M,S)\ne\varnothing.                \tag{1.3}
\]

Thus any internal reduction preserving the boundary extension set
immediately contradicts minor-criticality.

## 2. Standard safe-cycle theorems

A proper \(k\)-colouring of an induced cycle \(C\) is called **safe** if
it extends to every planar graph containing \(C\) as an induced cycle.
Ajit Diwan proves the following facts in
[Colouring planar graphs with a precoloured induced cycle](https://arxiv.org/abs/2306.04944).

1. For four colours, the only individually safe cycle states are the
   proper colourings of a triangle.
2. For every \(k\ge4\), a proper \(k\)-colouring of a cycle of length
   at most \(2k-5\) which uses at most \(k-1\) colours is safe.

The first statement says in particular that **no fixed four-colour state
of an induced \(C_5\) is universally extendable**. The second gives a
sharp usable distinction:

* with at least six available colours, every state of a \(C_5\) is safe;
* with five available colours, every non-rainbow state of a \(C_5\) is
  safe; and
* with four available colours, no individual \(C_5\) state is safe in
  all planar canvases.

The triangle assertion can also be seen directly from the Four Color
Theorem: colour the planar graph, observe that its triangle receives
three distinct colours, and permute the four-colour palette to match the
prescribed state.

## 3. Palette-separated planar-side gluing

Let

\[
 S=A\mathbin{\dot\cup}V(C),\qquad |A|=a,\qquad k=r-a.
\]

For a boundary state \(\varphi\), say that it is
\((A,C,k)\)-**separated** if

\[
 |\varphi(A)|=a,\qquad
 \varphi(A)\cap\varphi(C)=\varnothing,
\]

so that the colours on \(C\) lie in a residual palette of order \(k\).

### Lemma 3.1 (one planar side)

Let \(G=L\cup_S M\) be a proper separation. Suppose

1. \(A\) is a clique;
2. \(L-A\) is planar with the induced cycle \(C\) bounding a face; and
3. \(M\) has an \(r\)-colouring whose boundary state \(\varphi\) is
   \((A,C,k)\)-separated and whose restriction to \(C\) is safe for
   \(k\) colours.

Then \(G\) is \(r\)-colourable.

#### Proof

Keep the colouring of \(M\). Use the \(k\) colours outside
\(\varphi(A)\) to extend \(\varphi|_C\) over the planar graph \(L-A\).
Every edge from \(A\) to \(L-A\) is proper because the two palettes are
disjoint. The two side-colourings agree on \(S\), so they glue.
\(\square\)

When \(A\) is complete to \(C\), every proper boundary state is
automatically palette-separated.

### Theorem 3.2 (triangle and \(C_5\) elimination)

Assume the setting of Lemma 3.1, assume \(A\) is complete to \(C\), and
assume \(M\) is \(r\)-colourable.

1. If \(C=K_3\) and \(k\ge4\), then \(G\) is \(r\)-colourable.
2. If \(C=C_5\) and \(k\ge6\), then \(G\) is \(r\)-colourable.
3. If \(C=C_5\), \(k=5\), \(L-S\) is a full connected shore, and the
   full-shore exact-trace lemma is available, then \(G\) is
   \(r\)-colourable.

#### Proof

For (1), take any \(r\)-colouring of \(M\). Its state on the triangle is
safe for four, hence also for \(k\), colours.

For (2), any state on \(C_5\) uses at most five colours, and
\(5\le k-1\). Diwan's theorem makes it safe.

For (3), choose a nonedge \(xy\) of \(C_5\). Contract the full shore
together with \(\{x,y\}\), as in the exact-trace lemma. The resulting
proper minor has an \(r\)-colouring of \(M\) in which \(x,y\) have the
same colour. Thus the \(C_5\) uses at most four of the five residual
colours. Diwan's theorem makes this state safe, and Lemma 3.1 glues it.
\(\square\)

Therefore a one-sided planar \(C_5\) web can survive this argument only
in the **four-residual-colour cell**

\[
 r-|A|=4.                                           \tag{3.1}
\]

This conclusion is uniform in \(t\).

## 4. Two planar sides

The four-residual-colour cell also disappears when both sides are
plane-compatible.

### Lemma 4.1 (two-sided planar gluing)

Let \(A\) be a clique and suppose \(G-A\) is planar. Then

\[
 \chi(G)\le |A|+4.
\tag{4.1}
\]

In particular, if \(r\ge |A|+4\), then \(G\) is \(r\)-colourable.

#### Proof

Give the vertices of \(A\) distinct colours, and colour \(G-A\) with a
disjoint four-colour palette using the Four Color Theorem.
\(\square\)

The same conclusion holds when two planar disk sides can be embedded on
opposite sides of their common boundary cycle, since their union after
deleting \(A\) is planar. More generally, \(G-A\) may be merely
\(K_5\)-minor-free: the established \(t=5\) case of Hadwiger gives its
four-colourability.

Hence a critical four-palette \(C_5\) web must be genuinely
**one-sided**: the opposite side cannot be another compatible planar web
after the protected clique is deleted.

## 5. Why a complete canvas classification is unavailable

There is no standard exact classification of nonuniversal four-colour
\(C_5\) canvases which can simply be imported here.

* Diwan's theorem shows that every individual four-colour \(C_5\) state
  is unsafe in some planar supergraph; only triangle states are
  universally safe.
* Dvořák and Lidický,
  [Coloring count cones of planar graphs](https://arxiv.org/abs/1907.04066),
  explain that even deciding whether a fixed precolouring of the outer
  4-cycle of a near-triangulation extends is an unresolved algorithmic
  problem, and that no structural description of the nonextendable
  canvases is known. Their \(C_5\) coloring-count cone conjecture would
  strengthen the Four Color Theorem.
* Dvořák, Moore, Seifrtová, and Šámal give a characterization only for
  the special class of
  [planar near-Eulerian triangulations](https://arxiv.org/abs/2312.13061),
  under parity and boundary-colour hypotheses not forced by the present
  web reduction.

Thus an assertion that the remaining \(k=4\) canvases have a short
explicit list would hide a theorem-strength gap.

## 6. What degree and switching still force

The planar-web curvature bound from
hadwiger_portal_block_web_counterexample.md shows that a web with an
outer \(b\)-cycle, a portal SDR, and protected-boundary exposure at most
\(e\) is impossible when \(t-e\ge8\); for \(b=5\), it is already
impossible when \(t-e=7\). Hence a surviving \(C_5\) web must satisfy

\[
 e\ge t-6.                                          \tag{6.1}
\]

Moreover every internal deletion or contraction must satisfy the
switching condition (1.3). Exact independent-set traces do not imply
this: the uniform pentagonal-web family has every exact trace but is
boundary-universal and \((t-1)\)-colourable.

Combining the proved results leaves one precise critical-canvas cell:

1. residual palette exactly four;
2. only one side plane-compatible;
3. protected exposure at least \(t-6\);
4. no boundary-extension-preserving internal reduction; and
5. every internal minor operation creates a new state compatible with
   the opposite side as in (1.3).

This is the correct formulation of **critical-web exclusion**. It is
strictly narrower than arbitrary \(C_5\) precolouring extension, but it
is not yet proved. The next viable mechanism is to combine a boundary-
aware Four Color reducibility argument with (1.3), rather than attempt
an unavailable classification of all four-colour \(C_5\) canvases.

The 2026 theorem of Inoue, Kawarabayashi, Miyashita, Mohar, Thomassen,
and Thorup,
[The Four Color Theorem with Linearly Many Reducible Configurations and
Near-Linear Time Coloring](https://arxiv.org/abs/2603.24880), is
particularly relevant: it supplies linearly many robust D-reducible
configurations or noncrossing obstructing cycles of length at most five
in a planar triangulation. What is still required here is a
**boundary-relative** version: at least one reduction must preserve the
full extension set on the society cycle, not merely preserve existence
of some four-colouring. Such a reduction would contradict (1.3)
immediately.
