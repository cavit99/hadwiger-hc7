# Independent audit: failed twin-seam RST web planarization

**Verdict:** **GREEN at the frozen source hash below.**  The cell-elimination
argument is valid in the full atomic twin-seam setting, and the resulting
quotient is a literal planar four-root quotient.  Corollary 3.1 is also
valid as a conditional active-face list splice.  It does not show that the
three omitted `I` portal classes lie on the common face, nor does it close
the high-load residue.

An initial draft cited a previously audited single-edge localization theorem
whose formal statement assumed a four-connected carrier, although
Corollary 3.1 does not assume `D` four-connected.  The frozen source now
gives the needed hypothesis-minimal proof directly.  A facial cycle of
length at least four, the displayed list bounds, and the attachment
condition suffice; Section 5 below checks that argument.

**Audited source:**
`results/hc7_twin_seam_failed_rst_web_planarization.md`.

**Source SHA-256:**
`23ff005eaab69c37f9a0d82b6af881d9cbb2f66368294313566dbde029e6f2b0`.

## 1. Exact quotient and web dependency

After contracting the two disjoint connected reserves

\[
 C_i=R_i\cup\{a_i\},
\]

the quotient `Q` has precisely the vertices of `D` together with the four
named vertices `p,q,c_1,c_2`.  In particular, no vertex of `I`, `E`, or an
unused part of the old rich shore survives in `Q`.

Failure of either Robertson--Seymour--Thomas feasibility pairing is exactly
failure of the associated two-disjoint-path crossing on these four distinct
roots.  The same-vertex Two Paths theorem therefore gives an edge completion
of `Q` to a four-web with the roots as its frame in the corresponding cyclic
order.  The completion adds edges only.  This is the required form: no
completion edge is treated as a literal edge of `G`.

The web definition used here is the standard one: each clique cell is
attached exactly to the three vertices of a facial rib triangle.  Hence a
component of literal vertices in a cell has no quotient neighbour outside
that triangle.

## 2. Lifting a clique cell

Let `X` be a nonempty component of literal quotient vertices in one clique
cell behind a triangle `Delta`.  Frame vertices belong to the rib, not to
cell interiors.  Since the only quotient vertices outside `D` are the four
frame roots, `X` is a nonempty connected subset of literal `D` vertices.
It contains neither a contracted reserve root nor a literal gate root.

Every vertex of `Delta` lifts to at most one literal neighbour of `X`:

* an ordinary quotient vertex is one literal vertex;
* `p` and `q` are literal singleton roots; and
* a contracted root `c_i` expands to `R_i union {a_i}`, but old
  thin--rich anticompleteness forbids every `D-R_i` edge.  Thus only the
  single literal vertex `a_i` can be adjacent to `X`.

This verifies the potentially delicate label lift.  The three gate vertices
therefore contribute at most three members of `N_G(X)`.  The frozen identity

\[
 N_G(D)=\{p,q\}\mathbin{\dot\cup}I
          \mathbin{\dot\cup}\{a_1,a_2\}
\]

shows that the only neighbours of `D` omitted from `W` are the three
vertices of `I`.  Consequently

\[
 N_G(X)\subseteq L(\Delta)\cup I,
 \qquad |N_G(X)|\le 6.
\]

## 3. The far side and planarity conclusion

The frame has four distinct roots and `Delta` has only three vertices, so
some frame root is not in `Delta`.  Its literal expansion is disjoint from
`X`.  It is also disjoint from `N_G(X)`: an edge from `X` to that expansion
would give in `Q` an edge from the cell interior to a vertex outside its
attachment triangle.  Thus there is a literal vertex outside
`X union N_G(X)`.  The set `N_G(X)` is a genuine separator with a nonempty
shore on each side, contradicting seven-connectivity.

Every clique cell therefore has empty literal interior.  Because the web
completion is same-vertex, all vertices of the completed web are now rib
vertices.  Deleting the completion-only edges from its fixed plane drawing
leaves a plane drawing of the literal spanning subgraph `Q`; deletion can
merge faces but cannot move a frame root off the outer face.  The four roots
remain cofacial in their certified frame order.  This proves Theorem 2.1.

## 4. Active-face list splice

Corollary 3.1 is explicitly conditional on a literal facial cycle `F` of
`D` containing every vertex incident with the actual boundary
`Omega_D`.  Theorem 2.1 alone does not supply this stronger condition,
especially for the three omitted `I` classes.

Since `D` is connected and has at least two vertices, contracting a spanning
tree of `D` gives a proper minor.  The identity `N_G(D)=Omega_D` means that
the contracted vertex `z_D` is adjacent to every literal boundary vertex.
Thus, in any six-colouring `c` of `G/D`, the colour `c(z_D)` occurs on no
boundary vertex and belongs to every list

\[
 L(x)=[6]-c(N_G(x)\cap\Omega_D).
\]

Every vertex strictly inside `F` has no boundary neighbour and hence a
six-element list.  Under the low-load hypothesis, every facial list has at
least three colours.  Two adjacent facial lists of order at least three
have distinct representatives.  Thomassen's precoloured-outer-edge theorem
then colours `D` from these lists.  The list definition checks every literal
crossing edge, so this colouring glues to `c` on `G-D` and colours all of
`G`.

The heavy-set alternatives are the exact contrapositive of the same
argument.  With no heavy vertex, apply the preceding splice.  With one
heavy vertex, precolour it by `c(z_D)` and a facial neighbour by a distinct
available colour.  With exactly two adjacent heavy vertices, distinct
representatives again splice.  Since both heavy lists contain `c(z_D)`,
failure of distinct representatives occurs exactly when both lists equal
the singleton `{c(z_D)}`.  The remaining alternatives are two nonadjacent
heavy vertices or at least three heavy vertices.  No colour is silently
identified with a named model row.

## 5. Localization qualification

Suppose the adjacent singleton-heavy pair is the facial edge `xy` and
`|F|>=4`.  Contract `xy` in the inherited plane drawing.  The image of
`F` is still a cycle of length at least three.  Give the contracted image
the singleton list `{c(z_D)}`.  Every other outer vertex has list size at
least three (an exposed old interior vertex has the full list), and every
remaining interior vertex has list size at least five.  Precolour an
incident outer edge with two distinct available colours and apply
Thomassen's theorem.  This colours `G/xy` while preserving the exact
boundary state of `c`.

Splitting the contracted image back into `x,y`, giving both the contraction
colour, and deleting only `xy` yields the corresponding colouring of
`G-xy`, again with the same boundary state.  This is precisely the claimed
localization, and it does not require four-connectivity of `D`.  It still
does not manufacture a matching state on the opposite shore.

## 6. Falsification attempts and exact scope

The proof was tested against the three dangerous lift scenarios:

1. a cell containing a contracted root is impossible because frame roots
   are rib vertices;
2. a contracted reserve gate cannot expose several literal neighbours,
   because all of `R_i` is anticomplete to `D`; and
3. the separator cannot consume the whole graph, because one of four frame
   roots lies outside the three-gate triangle and its expansion is outside
   the separator.

None falsifies the argument.  The conclusion is deliberately limited.  A
failed pairing yields a literal planar quotient and, under the additional
active-face hypothesis, a low-load colouring splice.  Off-face `I`
attachments, nonadjacent heavy vertices, three or more heavy vertices, and
the unmatched localized-edge state all remain live.
