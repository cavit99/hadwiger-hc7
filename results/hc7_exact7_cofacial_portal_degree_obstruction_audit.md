# Independent audit: cofacial portal degree obstruction

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_cofacial_portal_degree_obstruction.md`

**Source SHA-256:**
The mathematical body audited before promotion had SHA-256
`436d7875339e16401ed98d476e4d60f8ecaff265c495fc53cbcb375e7d4bfbc2`.
Promotion changed only the status line and file location.
The promoted source hash is
`83f5e5e8beacd8727d6fa914e7b747bcf7d913327ffd202a7fb5a52a192a168e`.

## 1. Facial cycles and curvature

A finite simple four-connected planar graph is three-connected, so every
facial boundary in its plane embedding is a cycle.  Thus the length of the
distinguished face `F` is exactly `f=|V(F)|`, and the facial lengths used
in the proof do not count repeated vertices.

Let `n=|V(L)|`, `m=|E(L)|`, and let `q` be the number of faces other than
`F`.  Euler gives `q=m-n+1`, while face-edge counting gives

\[
 \sum_{D\ne F}\ell(D)=2m-f.
\]

Consequently the source's quantity

\[
 \epsilon=\sum_{D\ne F}(\ell(D)-3)
\]

satisfies

\[
 \epsilon=2m-f-3(m-n+1)=-m+3n-f-3,
\]

which rearranges to the claimed identity

\[
                         m=3n-f-3-\epsilon.
\]

Writing `I=V(L)-V(F)`, the degree-curvature sum is therefore

\[
\begin{aligned}
 \sum_{v\in I}(6-d_L(v))+
 \sum_{v\in V(F)}(4-d_L(v))
 &=6(n-f)+4f-2m\\
 &=6+2\epsilon.
\end{aligned}
\]

This calculation is valid for an arbitrary facial cycle `F`; the other
faces need not be triangles.  Every face of a simple plane graph has
length at least three here, so `epsilon>=0`.

Four-connectivity implies minimum degree at least four.  Every summand
indexed by `V(F)` is therefore nonpositive, whereas the total sum is at
least six.  Hence the interior sum is positive: `I` is genuinely nonempty
and contains a vertex `x` with `6-d_L(x)>0`, equivalently `d_L(x)<=5`.
This verifies both the off-face conclusion and the degree bound.

## 2. Literal adhesion step

The hypothesis

`N_L(S-U) subseteq V(F)`

contains every literal portal belonging to `S-U`, not merely one selected
representative for each boundary vertex.  Hence the selected
`x in L-V(F)` has no neighbour in `S-U`.  The literal separation supplies
no `L-R` edge, so every neighbour of `x` outside `L` lies in `U`.  Because
the host is simple,

\[
                   d_G(x)=d_L(x)+|N_S(x)|
                          \le5+|U|.
\]

For `U={c}`, this says literally that `x` has at most one boundary
neighbour and total degree at most six.  Seven-connectivity implies
minimum degree at least seven, giving the asserted contradiction.

## 3. Scope

The argument adds no completion edges.  The application correctly
requires all six complete portal sets to be cofacial; cofaciality
of six chosen representatives would not suffice.  The note proves only
the planar/common-face output and leaves derivation of the rooted-model
versus complete-cofaciality dichotomy as the stated remaining obligation.
