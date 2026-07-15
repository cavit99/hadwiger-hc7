# Direct-reserve one-root substitution

**Status:** proved and independently audited.

## Setup

Use the frozen connected-bipartite atomic separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where `G` is seven-connected, there is no `A-R` edge, `zu` is the
unique `A-u` edge, and the nonsingleton atom satisfies

\[
                       |A|\ge3,
 \qquad A-z\text{ is connected and }W\text{-full}.       \tag{1.1}
\]

Give the boundary the canonical two-carrier lists

\[
 \Lambda(u)=\{0\},\qquad
 1\in\Lambda(w)\ (w\in W),\qquad
 0\in\Lambda(w)\Longleftrightarrow zw\in E(G).          \tag{1.2}
\]

Let `xy` be a bad path of order two in the audited two-list/Menger
certificate; thus `xy` is a literal boundary edge and `x,y` are its two
distinct forced endpoints.

## Lemma 1 (a direct bad edge avoids the compulsory root)

The vertices `x,y` both have singleton list `{1}`.  In particular,

\[
                         x,y\in W,
             \qquad zx,zy\notin E(G).                   \tag{1.3}
\]

### Proof

Fix a bipartition parity `p` of the connected bipartite boundary.  A
singleton-list vertex with forced label `c` has orientation demand

\[
                         \theta=c\mathbin{\mathsf{xor}}p.
\]

The ends of a bad path have different orientation demands.  Since `xy`
is an edge, `p(x) xor p(y)=1`; hence

\[
 \theta(x)\ne\theta(y)
 \quad\Longleftrightarrow\quad c(x)=c(y).                \tag{1.4}
\]

Only `u` has singleton list `{0}` in (1.2), so two distinct forced
vertices with the same singleton label cannot both have label zero.
Thus both labels are one.  Formula (1.2) now gives (1.3).  \(\square\)

## Theorem 2 (one-root substituted diamond)

Let `Q` be the four distinct endpoints of the two disjoint bad paths and
suppose `x,y in Q` are the ends of the direct bad edge.  Choose any

\[
                         r\in Q\cap W-\{x,y\}.
\]

Such an `r` always exists.  Then the graph

\[
                   G[(A-z)\cup\{z,x,y,r\}]              \tag{2.1}
\]

contains a `{z,x,y,r}`-rooted `K_4^-` model.  The model avoids `u` and
the fourth original root in `Q-\{x,y,r\}`.

### Proof

At most one member of `Q` is `u`, while `x,y in W` by Lemma 1.  Hence
`Q cap W-{x,y}` is nonempty.

Reorient the literal seven-separation by putting

\[
 A'=A-z,\qquad S'=W\cup\{z\},\qquad R'=R\cup\{u\}.       \tag{2.2}
\]

These sets partition `V(G)`, and both open shores are nonempty.  There is
no `A'-R'` edge: there is no old `A-R` edge, and uniqueness of `zu`
excludes every `A'-u` edge.  Also `|S'|=7`.

Apply the audited closed-shore rooted-connectivity theorem to (2.2) and
the four-set

\[
                         Q'=\{z,x,y,r\}\subseteq S'.
\]

It says that the rooted pair in (2.1) is internally four-connected.
By (1.1), `|A'|>=2`, so (2.1) has at least six vertices.  Jorgensen's
rooted-diamond theorem therefore supplies the claimed `Q'`-rooted
`K_4^-` model.  Its host vertex set in (2.1) contains neither `u` nor the
omitted original root, proving the final assertion.  \(\square\)

## Exact use and trust boundary

The theorem is a literal model-regeneration move in the sole rural
direct-reserve residue.  It replaces one original root by `z` while
preserving three named boundary roots and avoiding the omitted root.

It does **not** assert that the substituted diamond's missing edge is
repairable without the omitted root, that the omitted root contacts two
specified bags, or that two independently chosen diamonds compose.  The
next theorem must prove precisely that exchange, using a lexicographically
optimal reduced diamond and its literal bridges; palette colours cannot be
identified with the four bag labels.

## Computational boundary check

`active/hc7_direct_reserve_mask_probe.py` exhausts the canonical boundary
languages.  Across 2,636 disjoint bad-path pairs having exactly one
literal edge and one nontrivial path, every direct bad edge has mask pair
`(2,2)`, i.e. two forced-one endpoints, in agreement with Lemma 1.  This
is verification evidence only; the proof above is uniform.
