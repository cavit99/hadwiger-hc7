# Independent audit: bilateral decoration Kempe lock

Audited file: `hc7_exact7_bilateral_decoration_kempe_lock.md`.

## Verdict

**GREEN in the stated exact-order-six cell.**  The source now incorporates
the two Section 1 wording repairs and the colour-count clarification found
during audit.  The proof does not close the self-lock residue, and the
source correctly makes no such claim.

## 1. Proper-minor state returned to the opposite side

Fix `i in Sigma_{3-s}` and choose its supported witness `W_i` on side
`3-s`.  The contraction meant in Section 1 is the following literal one:

* contract the connected star `Z={v,a,b}`;
* contract `C_i^{3-s} union W_i` to one vertex; and
* contract each of the other two core blocks separately.

Delete every unused open-shore vertex on side `3-s`.  The four displayed
images form a clique.  The three core images are pairwise adjacent, while
the star image sees each one through an edge from `v` to a root in its
nonempty `U`-trace.  The contraction is proper already because the star
has three vertices.

A six-colouring of this minor gives the three core images three distinct
colours and the star image a fourth.  On expanding only the untouched
closed side `s`, give every literal vertex of `B_h` the colour of the
corresponding core image, give `w` the colour of the merged `i`-image, and
give the side terminal `t_s` the colour of the star image.  Every relevant
edge of the closed side survived incident with the appropriate contracted
image, so this is proper.  It gives exactly

\[
       (B_i\cup\{w\})\mid B_j\mid B_k\mid\{t_s\}.
\]

Thus the state assertion in (1.2), including the exact fourth colour of
the terminal, is correct.  The source now names the explicit merged
contraction `C_i^{3-s} union W_i` and says “the expanded opposite closed
side”: the literal terminal was part of the contracted star and is validly
restored with the star colour.

## 2. Kempe switch

Put

\[
 \alpha=c_i^s(w)=c_i^s(B_i),\qquad
 \beta=c_i^s(B_j),
\]

and let `Z` be the `alpha/beta` component containing `w`.  If `Z` avoids
`B_i union B_j`, switching the whole component is a standard proper Kempe
switch.  It changes `w` from `alpha` to `beta` and changes no root of `U`:
the `B_i,B_j` roots were excluded, the `B_k` roots have the third core
colour, and the terminal has the fourth colour.  Hence the new interface
state is exactly

\[
                 B_i\mid(B_j\cup\{w\})\mid B_k.
\]

No hidden assumption about colour-class connectivity is used.

If the component meets `B_i union B_j`, a shortest path from `w` to that
literal set has all internal vertices outside `T`.  Indeed every vertex of
`T` carrying `alpha` or `beta` lies in
`B_i union B_j union {w}`, while the terminal has a fourth colour.  The
path therefore avoids the side terminal and has its internal vertices in
the open shore.

Taking the first vertex `z` in the **whole** fixed core is label-faithful.
The prefix with `z` removed is connected, contains `w`, avoids all three
core blocks and the side terminal, has exact trace `{w}`, and has a literal
last edge to the unique block containing `z`.  If that block's trace is
admissible, this prefix is a supported witness and the use of the full set
`Sigma_s` legitimately puts its index in `Sigma_s`; otherwise the failed
independence is exactly the stated boundary certificate.  This verifies
all clauses of Theorem 2.1.

## 3. Gluing and the colour absent at `v`

When the switch succeeds, side `s` is coloured in state `j`.  Contracting
the supported `j`-realization on side `s` returns a colouring of the other
closed side in the same state.  After fixing the three block colours, the
remaining three palette colours may still be permuted, so the two side
terminal colours can be aligned.  The terminals `a,b` are nonadjacent and
may share that fourth colour.  The two closed-side colourings agree on
`T`, and the two open shores are anticomplete, so they glue to a colouring
of `H=G-v`.

Only four colours occur on

\[
                        N(v)=U\cup\{a,b\}:
\]

three on the blocks partitioning `U`, and one common terminal colour.
Therefore at least two of the six palette colours are absent from `N(v)`;
either may colour `v`.  The source now states this stronger count directly.

## 4. Corollary and trust boundary

If all three decorations are admissible, bilateral decorated overlap
indeed gives `Sigma_1 cap Sigma_2=empty`.  Every ordered pair in the
corollary therefore has distinct indices, so Theorem 2.1 applies, and its
inadmissibility branch is unavailable.  The rank-one specialization yields
one terminal-free first-hit path owned by the already supported block on
each side, exactly as claimed.

The source correctly stops there.  A first hit in the already supported
block may be a self-lock rather than a transfer; no `Q-P` carrier, common
state, `K_7`, or smaller witness follows without the proposed gate-descent
argument.  The audit does not strengthen that residue and remains
conditional on the literal exact adhesion `T=U dotcup {w}` and the same
labelled frame on both shores.
