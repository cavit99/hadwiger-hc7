# Audit: common-deletion dominating-five substrate

**Verdict:** GREEN.  The chromatic bounds, application of the Dominating
4-Colour Theorem, two-singleton normalization, induced cycle in the common
deletion host, and terminal-edge rotation are correct.  No rooted or
labelled-duty allocation follows.

**Audited source:**
`results/hc7_common_deletion_dominating_five_substrate.md`.

**Source SHA-256:**
`9cb15e70cde2d33d1bb433a9b7c3af5b6b1dffd7b0d7ae0ac504b8aafa6224b5`.

**External source checked:** António Girão, Freddie Illingworth, Bojan
Mohar, Sergey Norin, Raphael Steiner, Youri Tamitegama, Jane Tan, David R.
Wood and Jung Hon Yip, *The Dominating 4-Colour Theorem*, Theorem 1.1,
arXiv:2605.10112 (2026), <https://arxiv.org/abs/2605.10112>.

## 1. Proper-minor and chromatic audit

The graph

\[
                         H=G-\{e,f\}
\]

is a proper minor of `G`: edge deletion is a minor operation, and the
vertex-disjoint edges `e,f` are distinct.  Hence the stated proper-minor
minimality gives \(\chi(H)\le 6\).

The lower-bound argument is correct.  If `H` had a colouring with at most
four colours, recolour `z` with a fresh fifth colour and `d` with a fresh
sixth colour.  Vertex-disjointness of `zu` and `dt` makes
`z,u,d,t` four distinct vertices.  Consequently:

* every unchanged edge remains proper;
* every edge incident with exactly one of `z,d` is proper because its
  recoloured endpoint has a fresh colour;
* a possible edge `zd` is proper because its ends receive colours five and
  six; and
* the restored edges `zu` and `dt` are proper because `u,t` retain colours
  from the original four-colour palette.

This would six-colour `G`, contradicting \(\chi(G)=7\).  Thus
\(5\le\chi(H)\le6\).

No contraction colouring is used here, and no assumption stronger than
six-colourability of every proper minor is hidden in this step.

## 2. External theorem audit

The paper defines a dominating \(K_t\)-model as an ordered sequence
\((T_1,\ldots,T_t)\) of pairwise disjoint connected subgraphs such that,
for every \(i<j\), every vertex of \(T_j\) has a neighbour in \(T_i\).
Its Theorem 1.1 states exactly that every graph with no dominating
\(K_5\)-model is four-colourable.

Since \(\chi(H)\ge5\), the contrapositive applies directly and supplies a
dominating \(K_5\)-model in `H`.  The theorem is not restricted to graphs
of chromatic number exactly five, so the possible case \(\chi(H)=6\)
causes no issue.

## 3. Two-singleton normalization

Starting with \((T_1,T_2,T_3,T_4,T_5)\), choose any
\(w\in T_5\).  Domination gives a neighbour \(v\in T_4\) of `w`.
Then

\[
                    (T_1,T_2,T_3,\{v\},\{w\})
\]

is still dominating:

* `v`, as an original vertex of `T_4`, has a neighbour in each of
  `T_1,T_2,T_3`;
* `w`, as an original vertex of `T_5`, has a neighbour in each of
  `T_1,T_2,T_3`; and
* the chosen edge `vw` supplies the fourth-to-fifth domination relation.

All branch sets remain nonempty, connected, and pairwise disjoint.  This
also agrees with the two-singleton observation made explicitly after
Theorem 1.1 in the paper.

## 4. Shortest-path and induced-cycle audit

Both `v` and `w` have a neighbour in the connected branch set `T_3`.
Therefore

\[
                  H[T_3\cup\{v,w\}]-vw
\]

contains a `v`--`w` path.  A shortest such path has length at least two,
so its internal vertices form a nonempty connected path `P` contained in
`T_3`.  Shortestness rules out every chord in this host.  Restoring `vw`
therefore produces a cycle

\[
                         C=vPw v
\]

that is induced in **`H`**.

The source states (1.4) in exactly this safe form:

\[
             H[P\cup\{v,w\}]\text{ contains the induced cycle }
             C=vPw v.
\]

The source also explicitly notes that restored `e` or `f` may be a chord
in `G`, so it makes no inducedness claim in the original host.  Nothing
later in the substrate requires such a claim; all model rotation occurs in
`H`.

Replacing `T_3` by `P` is valid.  Every vertex of `P` still has a neighbour
in each of `T_1,T_2`; the two end edges join `v` and `w` to `P`; and `vw`
remains the last domination edge.

## 5. Terminal-edge rotation, including triangles

Let `xy` be any edge of `C`.  Since `C` has at least three vertices,
deleting the adjacent pair `x,y` leaves a nonempty connected path along
the cycle.  When `C` is a triangle, this path is the single remaining
vertex; that singleton is a valid connected branch set.

Every vertex of `C` came from `T_3`, `T_4`, or `T_5`, and therefore has a
neighbour in each of `T_1,T_2`.  Moreover:

* `x` has its cycle neighbour other than `y` in
  `C-{x,y}`;
* `y` has its cycle neighbour other than `x` in
  `C-{x,y}`; and
* `xy` is an edge of `H`.

Thus

\[
             (T_1,T_2,C-\{x,y\},\{x\},\{y\})
\]

is a dominating \(K_5\)-model in `H` for either orientation of the edge.
This check does not need `C` to remain induced after restoring `e,f`.

## 6. Exact audited scope

After the one-host correction, the result uniformly supplies, for every
pair of vertex-disjoint edges `e,f`:

1. a common edge-deletion host `H` with chromatic number five or six;
2. a dominating \(K_5\)-model in `H` with two adjacent singleton bags;
3. an induced cycle in `H` supporting rotation of the two singleton bags
   to any of its literal edges.

Domination is directional adjacency, not a prescription of boundary
labels.  The proof does not show that any branch set meets a named duty,
that terminal rotation preserves a required reserve carrier, or that the
five bags can be allocated to five literal boundary vertices.  It also
does not identify either restored response edge with an edge of `C`.
Section 3 of the source correctly leaves that allocation problem open.
