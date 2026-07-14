# Audit: prescribed portal extension or exact-seven adhesion

**Verdict:** GREEN with the explicit tiny-shore alternative retained.

**Audited source:**
`results/hc7_exact7_prescribed_portal_extension_or_adhesion.md`

**Source SHA-256:**
The independently audited source had SHA-256
`466089f128c9e7352828c8bda05ea61a19efe9b06747489d550f38f29551bc3a`.
Removing one trailing blank line did not change its mathematical text; the
current source hash is
`47275bcf60d66a7587421b4e30e39963eaf57ea159cf67fbe19c848d81df4061`.

## 1. Necessary scope correction

The tiny-shore outcome cannot be omitted under seven-connectivity alone.
For example, take a clique `S` of order seven and two nonadjacent vertices
`z,r`, each complete to `S`.  With `L={z}` and `R={r}`, the graph is
seven-connected and `S` is an actual seven-boundary.  For any `A subseteq
S` of order at least two, a prescribed edge `sz` cannot extend to a
matching saturating `A`, while `L-N_L(U)` is empty.  Thus no smaller
`L`-side exists.  Outcome 2 records exactly this obstruction.

## 2. Hall calculation

After reserving `sz`, extension is equivalent to a matching saturating
`A-{s}` into `L-{z}`.  If it fails, an inclusion-minimal Hall witness
`U` is nonempty.  For every `u in U`, the proper subset `U-{u}` satisfies
Hall, so

\[
 |U|-1\le |N_{L-\{z\}}(U-\{u\})|
          \le |N_{L-\{z\}}(U)|<|U|.
\]

Hence `|N_{L-{z}}(U)|=|U|-1`.  Restoring the single vertex `z` shows
`|N_L(U)|` is either `|U|-1` or `|U|`.  Also `|U|<=3` because
`U subseteq A-{s}` and `|A|<=4`.  These deductions include the singleton
case `|U|=1`.

Seven-connectivity correctly implies `N_G(L)=S`: any proper external
neighbourhood of `L` would have order at most six and would separate the
nonempty shores `L` and `R`.  Thus `N_L(U)` is nonempty.

If `X=N_L(U)=L`, then `z in X`; the preceding one-vertex restoration
calculation gives `|X|=|U|<=3`.  This is precisely the tiny-shore branch.

## 3. Separator and fullness

Assume `L-X` is nonempty and let `C` be any one of its components.  Every
external neighbour of `C` lies in

\[
                       (S-U)\cup X=\Omega:
\]

* there are no `L-R` edges;
* a member of `U` has no neighbour in `L-X` by the definition
  `X=N_L(U)`; and
* distinct components of `G[L-X]` have no edge between them.

The original nonempty set `R` lies outside `C union N_G(C)`, so `N_G(C)`
is a genuine vertex cut.  The chain

\[
 7\le |N_G(C)|\le|\Omega|
   =7-|U|+|X|\le7
\]

is therefore valid.  Equality forces `|X|=|U|`; combined with the exact
Hall deficit, this also forces `z in X`.  Equality in
`N_G(C) subseteq Omega` gives `N_G(C)=Omega`, so every boundary literal
has an actual neighbour in every component `C`.  Each `C` is therefore
literally `Omega`-full.

The opposite open shore is nonempty because it contains the original
`R`.  Hence each displayed decomposition is an actual order-seven
separation.  Since `X` is nonempty, each selected `C` is strictly smaller
than `L`.

## 4. Four-connected specialization

Under the standard definition, a four-connected graph has at least five
vertices and remains connected after deletion of at most three vertices.
Thus `X=L` with `|X|<=3` is impossible, and `G[L-X]` is nonempty and
connected.  It is consequently the unique descended `L`-component and is
full at the explicit new boundary `(S-U) union X`.

## 5. Trust boundary

The proof establishes a literal matching or an exact boundary descent.  It
does **not** transport a colouring/equality state from `S` to `Omega`, and
it does not close the tiny shore.  Those limitations are stated correctly
in the source note.
