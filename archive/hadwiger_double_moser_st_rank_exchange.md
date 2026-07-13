# The one-body obstruction is a rank-two portal exchange

## 1. Purpose

Assume the cut-irreducible double-Moser body has reached the
two-connected branch.  The six low cross-capacity states are not six
unrelated cases: along an \(ab\) st-numbering they are exactly the
independent sets of a rank-two uniform matroid on the four root labels.
This note records the resulting event invariant.

It does not complete the web endpoint.  It reduces that endpoint to a
rank drop, one four-label exchange vertex, or two one-for-one exchange
positions.  The last alternative is the abstract source of the crossed
four-cycle.

## 2. st-numbering and cross capacity

Let \(C\) be two-connected and retain the edge \(ab\).  Choose an
st-numbering

\[
                         w_0=b,w_1,\ldots,w_m=a.                  \tag{2.1}
\]

Thus every set

\[
A_i=\{w_0,\ldots,w_i\},\qquad
B_i=\{w_{i+1},\ldots,w_m\}                                      \tag{2.2}
\]

is connected for \(0\le i<m\).

Recall \(H_1=\{x_1,x_2\}\) and \(H_2=\{x_3,x_4\}\), where \(a\)
already sees \(H_1\) and \(b\) already sees \(H_2\).  Define

\[
\alpha_i=|N_X(A_i)\cap H_1|,\qquad
\beta_i=|N_X(B_i)\cap H_2|.                                     \tag{2.3}
\]

The three-cross certificate in
hadwiger_double_moser_edge_exchange.md says that

\[
\alpha_i+\beta_i\ge3                                             \tag{2.4}
\]

gives a \(K_7\)-minor, provided the two sides have the two required
new-outer contacts.  More generally, (2.4) is precisely the positive
cross-capacity region of that certificate.

## 3. Portal event times

For \(j\in\{1,2\}\), let

\[
f_j=\min\{k:w_kx_j\in E(G)\},
\]

and, for \(j\in\{3,4\}\), let

\[
\ell_j=\max\{k:w_kx_j\in E(G)\}.                                 \tag{3.1}
\]

The full eight-interface body makes all four numbers well defined.
Moreover,

\[
1\le f_1,f_2,\qquad \ell_3,\ell_4\le m-1,                        \tag{3.2}
\]

because \(b\) misses \(H_1\), \(a\) misses \(H_2\), and \(R\) meets
all four root classes.

Then

\[
\alpha_i=|\{j\in\{1,2\}:f_j\le i\}|,\qquad
\beta_i=|\{j\in\{3,4\}:\ell_j>i\}|.                              \tag{3.3}
\]

In particular

\[
(\alpha_0,\beta_0)=(0,2),\qquad
(\alpha_{m-1},\beta_{m-1})=(2,0).                               \tag{3.4}
\]

### Lemma 3.1 (rank-two exchange trichotomy)

If no st-prefix split satisfies (2.4), exactly one of the following
occurs.

1. **Rank drop.**  For some \(i\),
   \[
   \alpha_i+\beta_i\le1.
   \]
2. **One double exchange.**  One vertex \(w_i\) is simultaneously the
   first portal of both labels in \(H_1\) and the last portal of both
   labels in \(H_2\).  In particular \(w_i\) meets all four root
   classes.
3. **Two simple exchanges.**  There are two indices \(i<j\).  At each
   index the corresponding vertex is the first portal of one label in
   \(H_1\) and the last portal of one label in \(H_2\); the two events
   use all four labels.

#### Proof

Put \(r_i=\alpha_i+\beta_i\).  By (3.4), the sequence starts and ends
at two.  The exclusion of (2.4) says \(r_i\le2\) for every \(i\).
If some value is at most one, outcome 1 holds.

Otherwise \(r_i=2\) throughout.  On passing from \(i-1\) to \(i\), let
\(g_i\) be the number of \(H_1\)-labels whose first portal is \(w_i\),
and let \(d_i\) be the number of \(H_2\)-labels whose last portal is
\(w_i\).  Equation (3.3) gives

\[
                         r_i-r_{i-1}=g_i-d_i.                    \tag{3.5}
\]

Hence \(g_i=d_i\) at every step.  Both total sums equal two.  Therefore
either one index has \(g_i=d_i=2\), or two indices have
\(g_i=d_i=1\).  A first or last portal at \(w_i\) is an actual edge
from \(w_i\) to the corresponding root, giving outcomes 2 and 3.
\(\square\)

### Corollary 3.2 (uniform-matroid form)

When rank drop is absent, the active cross-label set

\[
\{x_j\in H_1:f_j\le i\}\cup\{x_j\in H_2:\ell_j>i\}
\]

is a basis of \(U_{2,4}\) at every st-cut.  The only changes are basis
exchanges.  Thus the six low-capacity states are one rank-two exchange
system, not six independent geometries.

## 4. Structural interpretation

The trichotomy points to three different mechanisms.

* At a rank drop, relative seven-connectivity forces additional internal
  frontier vertices; maximal-bad portal peeling should turn their
  failure to exchange into an exact seven-cut.
* A double exchange produces a single vertex meeting all four root
  classes.  If the two old-to-new carriers can be chosen around that
  vertex, the three-root carrier lemma gives a \(K_7\)-minor.
* Two simple exchanges are the ordered precursor of the crossed
  \(C_4\) portal pattern.  If the pieces between the exchange positions
  can be contracted in order, the crossed-four-cycle certificate gives
  a \(K_7\)-minor.  Failure of that ordered contraction is precisely
  where an SPQR leaf or a Two Paths web must occur.

This is the same proof skeleton as the orientation-free SPQR reduction
for the \(C_6\dot\cup K_1\) core: basis exchange handles the unbounded
order, singleton ears handle low-rank leaves, and the crossless residue
is planar.  In the present frame the desired final outcome is

\[
K_7\text{-minor}\quad\text{or}\quad
\text{exact seven-cut}\quad\text{or}\quad
G-\{u,v\}\text{ planar}.                                          \tag{4.1}
\]

The last outcome six-colours \(G\): apply the Four Colour Theorem to
\(G-\{u,v\}\), then give \(u\) and \(v\) two fresh colours.
