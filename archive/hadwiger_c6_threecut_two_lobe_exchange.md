# A forced three-cut has exactly two lobes

## 1. Statement

Retain the minimum all-full-deletion `C_6 dotcup K_1` shore `D`, its
seven-boundary `S`, an opposite full shore `H`, and the forced three-cut

\[
                              T=\{t_1,t_2,t_3\}.                 \tag{1.1}
\]

Let `C_1,...,C_m` be the components of `D-T`, and put

\[
                         A_i=S-N_S(C_i),\qquad
                         B=S-N_S(T).                            \tag{1.2}
\]

The previous three-cut theorem proves `|A_i|<=2` and that some
`|A_i|=2`.  The result below strengthens it without enumerating the
size-two labels.

### Theorem 1.1 (two-lobe three-cut theorem)

If `G` has no `K_7` minor, then

\[
                                  m=2.                           \tag{1.3}
\]

Thus every forced three-cut of the minimum shore is a genuine connected
bipartition

\[
                      C_1\mid T\cup C_2,                        \tag{1.4}
\]

with one side of boundary order eight.  The other side has boundary
order eight or nine.

## 2. Every lobe has a private opposite defect

For each `i`, put

\[
                        E_i=S-N_S(D-C_i).                        \tag{2.1}
\]

Since

\[
              D-C_i=T\cup\bigcup_{j\ne i}C_j,
\]

one has the exact identity

\[
                        E_i=B\cap\bigcap_{j\ne i}A_j.            \tag{2.2}
\]

Fullness of `D` is equivalently

\[
                        B\cap\bigcap_{j=1}^m A_j=\varnothing.   \tag{2.3}
\]

### Lemma 2.1

Every `E_i` is nonempty.

#### Proof

As audited in `hadwiger_c6_threecut_lobe_exchange_audit.md`, both sides
of `C_i | (D-C_i)` are connected and adjacent.  The first defect is
`A_i`, of order at most two.  If `E_i` were empty, the defect pair would
have sizes at most `2|0`.  No negative pair in the exact two-piece atlas
has an empty coordinate and the other coordinate of order at most two:
the minimal empty-coordinate locks have other coordinate of order three
or four.  Therefore the split would be positive and would lift with `H`
to a literal `K_7` model.  This contradicts the hypothesis.  QED.

## 3. A two-set Helly argument bounds the lobe count

For every `i`, choose

\[
                              x_i\in E_i.                       \tag{3.1}
\]

By (2.2),

\[
             x_i\in B,\qquad x_i\in A_j\quad(j\ne i).          \tag{3.2}
\]

Equation (2.3) shows `x_i notin A_i`.  Consequently the vertices `x_i`
are pairwise distinct: if `x_i=x_j` with `i ne j`, then (3.2) for `x_j`
would put `x_i` in `A_i`, a contradiction.

Fix `j`.  The set `A_j` contains all `m-1` distinct vertices
`{x_i:i ne j}`.  Since `|A_j|<=2`,

\[
                                  m\le3.                         \tag{3.3}
\]

This is a uniform capacity statement; no shape of a size-two defect has
yet been used.

## 4. Three lobes would make a triangle in the missing cycle

Suppose `m=3`.  The containments (3.2) and the order-two bound force

\[
       A_1=\{x_2,x_3\},\qquad
       A_2=\{x_1,x_3\},\qquad
       A_3=\{x_1,x_2\}.                                  \tag{4.1}
\]

Using (2.2), the intersection of the other two sets in each case is a
singleton, so

\[
                              E_i=\{x_i\}.                       \tag{4.2}
\]

The low-defect part of the exact two-piece atlas says that a negative
`2|1` defect pair must, after orienting the singleton coordinate, have
the form

\[
                         \{x_i\}\mid N_F(x_i),                  \tag{4.3}
\]

where `F=C_6` is the missing cycle on the six nonuniversal boundary
labels.  The `2|2` antipodal lock cannot be dominated by a singleton,
and the empty-coordinate locks cannot occur.  Therefore every `x_i`
belongs to the missing cycle and

\[
                              A_i=N_F(x_i).                       \tag{4.4}

Equations (4.1) and (4.4) say that each of the three distinct vertices
`x_1,x_2,x_3` is adjacent in `F` to the other two.  This is a triangle
in the chordless six-cycle, impossible.  Hence `m ne3`.

Since `T` is a cut, `m>=2`; together with (3.3) this proves Theorem 1.1.

## 5. Exact residual orientation

With `m=2`, the identities become

\[
                    E_1=B\cap A_2,\qquad
                    E_2=B\cap A_1,                              \tag{5.1}
\]

and both sets are nonempty.  At least one of `A_1,A_2` has order two by
the earlier exact-eight descent.  Thus the only target-free three-cut
geometry is

```text
two connected lobes, each complete to all three gate vertices;
both opposite defects nonempty;
at least one lobe misses exactly two old boundary labels.
```

This is a structural reduction to a bilateral order-eight/eight-or-nine
gate, not a list of portal incidences.  The next operation-state theorem
only has to compare these two literal connected sides.
