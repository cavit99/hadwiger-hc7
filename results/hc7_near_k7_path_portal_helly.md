# Path-portal Helly dichotomy after wholesale transfer

## Status

This is the exact uniform rooted-model interface left after every
foreign-contacting exterior piece has been absorbed into a foreign row.
It gives a clique minor immediately when all literal portal spans overlap;
otherwise it returns one ordered two-row corridor (or a singleton portal
row), with no carrier enumeration.

## Theorem 1 (uniform path-portal Helly dichotomy)

Let `P=p_0p_1...p_m` be a path and let
`F_1,...,F_s` be pairwise disjoint connected pairwise adjacent sets,
disjoint from `P`.  For every `i`, let

\[
 R_i=N_P(F_i)=\{p_j:E(p_j,F_i)\ne\varnothing\}
\]

be nonempty.  Exactly one of the following structural alternatives holds.

1. Some path edge `p_jp_{j+1}` has a portal of every row on both sides:
   \[
     R_i\cap\{p_0,\ldots,p_j\}\ne\varnothing
       \ne R_i\cap\{p_{j+1},\ldots,p_m\}
                         \qquad(1\le i\le s).             \tag{1.1}
   \]
   Then the two path sides together with `F_1,...,F_s` form a
   `K_{s+2}` minor.
2. Some row has a singleton path portal; or there are distinct rows
   `F_a,F_b` such that every portal of `F_a` occurs weakly before every
   portal of `F_b`:
   \[
       \max\{j:p_j\in R_a\}\le
       \min\{j:p_j\in R_b\}.                              \tag{1.2}
   \]

### Proof

For each row put

\[
 \ell_i=\min\{j:p_j\in R_i\},\qquad
 r_i=\max\{j:p_j\in R_i\}.
\]

A cut edge `p_jp_{j+1}` satisfies (1.1) exactly when

\[
                         \ell_i\le j<r_i
                         \qquad(1\le i\le s).             \tag{1.3}
\]

Thus alternative 1 holds exactly when

\[
                         \max_i\ell_i<\min_i r_i.          \tag{1.4}
\]

In that case the two nonempty path sides are connected, disjoint and
adjacent through their cut edge.  Each has a literal edge to every
`F_i`, and the rows are already pairwise adjacent.  These `s+2` sets are
therefore a clique-minor model.

If (1.4) fails, choose `a` with `r_a=min_i r_i` and `b` with
`ell_b=max_i ell_i`.  Then `r_a<=ell_b`.  If `a!=b`, this is (1.2).
If `a=b`, then

\[
             \ell_a\le r_a\le\ell_a,
\]

so `ell_a=r_a` and `R_a` is a singleton.  This is alternative 2.
The two structural alternatives are mutually exclusive by (1.3).
\(\square\)

## Corollary 2 (`HC_7` one-missing path interface)

After wholesale piece transfer, omit every path-private lobe and use the
nonspanning model whose deficient bag is the normalized path `P`.  Let
the five retained rows be `E,U_1,U_2,U_3,U_4`.  If their portal spans
share an edge, Theorem 1 with `s=5` gives a literal `K_7` model.

In a target-free graph, the sole remaining path geometry is therefore:

* one retained row has exactly one literal path portal; or
* two retained rows have disjoint, ordered portal spans as in (1.2).

The next state theorem must eliminate this ordered corridor by a faithful
minor-colouring splice or identify it with the fixed global two-apex
expansion.  The dichotomy itself does not colour across the ordered gap.

## Generality

No step uses `s=5`.  For a missing-star model at arbitrary order, any
path carrier and clique of `s` foreign rows obey the same alternative:
an overlapping portal-span edge gives `K_{s+2}`, while failure is witnessed
by one singleton row or one ordered pair of rows.
