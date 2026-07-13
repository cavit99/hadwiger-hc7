# The forced three-cut: exact-eight descent

## 1. Setting

Let `D` be the minimum all-full-deletion `C6+K1` shore.  By Theorem 6.3.3
of `hadwiger_full_deletion_propagation.md`, choose a three-cut

\[
                              T=\{t_1,t_2,t_3\}       \tag{1.1}
\]

of `D`, and let `C_1,...,C_m` be the components of `D-T`.  Put

\[
                              A_i=S-N_S(C_i).          \tag{1.2}
\]

The graph `G-S` has no edges from `D` to another shore, so the literal
ambient neighbourhood is

\[
                              N_G(C_i)=T\dot\cup N_S(C_i). \tag{1.3}
\]

Three-connectivity of `D` makes every vertex of `T` adjacent to every
component `C_i`; otherwise a proper subset of `T` separates that component.

## 2. The first uniform lobe dichotomy

### Lemma 2.1 (defect two is an exact-eight gate)

Every lobe has `|A_i|<=2`.  If equality holds, then

\[
                              |N_G(C_i)|=8,           \tag{2.1}
\]

so `N_G(C_i)` is an actual exact order-eight separator.  Consequently,
outside the exact-eight descent every lobe is full or misses one boundary
label.

### Proof

The connected proper set `C_i` has internal boundary exactly `T`.
One-sided atomic surplus gives

\[
                 8\le |N_G(C_i)|=3+|N_S(C_i)|,
\]

which is `|A_i|<=2`.  Equality in the defect bound is exactly (2.1).
QED.

### Theorem 2.2 (a three-cut forces an exact-eight adhesion)

If `G` has no `K_7` minor, some lobe `C_i` has `|A_i|=2`.  Consequently
every forced three-cut of the minimum exact-seven atom exposes a literal
exact order-eight separator.

### Proof

Suppose every lobe has defect at most one.  Fix `i` and choose any
`j != i`.  The split

\[
                         C_i\mid(D-C_i)              \tag{2.2}
\]

has connected adjacent sides: `D-C_i` contains `T`, and every other lobe
meets all of `T`.  Its first defect is `A_i`, of order at most one.  If

\[
                         E_i=S-N_S(D-C_i),           \tag{2.3}
\]

then `C_j` is contained in `D-C_i`, so `E_i` is contained in `A_j` and
`|E_i|<=1`.

The exact two-piece `C6+K1` atlas has no negative contact pair whose two
defect coordinates both have order at most one.  Therefore (2.2), together
with the opposite full shore, gives a `K_7` model.  This contradiction
shows that some `|A_i|=2`; Lemma 2.1 turns its literal neighbourhood into
the exact-eight separator.  QED.

This removes the owner-exchange residue entirely at an exact-seven minimum
atom.  The three-separator theorem is a strict separator lift:

\[
  \text{target rooted model}\quad\text{or}\quad
  \text{an exact order-eight adhesion}.             \tag{2.4}
\]

There is therefore no residual owner-exchange case at the exact-seven
layer.  The only target-free outcome is the exact-eight gate.

### Corollary 2.3 (the gate retains a low-defect polarity)

Let `C=C_i` be a defect-two lobe, put `A=A_i`, and define the defect of
the complementary connected side by

\[
                     E=S-N_S(D-C).
\]

Then `1<=|E|<=2`, `A` and `E` are disjoint subsets of the six cycle
labels, and the ordered pair `(A,E)` is one of the low-defect negative
rows of the exact two-piece atlas.  Concretely, after possibly reversing
the two coordinates, either

\[
              \{w\}\subseteq A,qquad E=N_F(w),
\]

or the same display holds with `A,E` reversed, or

\[
                         A=M_r,qquad E=M_s
                         \quad(r\ne s).
\]

Here `F` is the missing six-cycle and the `M_r` are its three antipodal
pairs.

#### Proof

Choose another lobe `C_j`.  Since `C_j` is contained in `D-C`,

\[
                         E\subseteq A_j,
\]

and Lemma 2.1 gives `|E|<=2`.  The split `C | (D-C)` is connected and
adjacent.  It must be a negative atlas state in a `K_7`-minor-free graph.
An empty-coordinate negative row has its other defect of order at least
three, whereas `|A|=2`; hence `E` is nonempty.  Lemma 4.1 of
`hadwiger_c6_two_piece_locks.md` now gives exactly the displayed list.
The two defects are disjoint because their two sides cover the full shore
`D`, and the low-defect atlas rows use only cycle labels.  QED.

Thus the exact-eight separator is not arbitrary: it inherits a labelled
one-hole or antipodal polarity from the exact-seven atom.

### Theorem 2.4 (the forced three-cut has exactly two lobes)

In a `K_7`-minor-free minimum atom, `D-T` has exactly two components.

#### Proof

Put

\[
                         A_T=S-N_S(T).
\]

For every lobe `C_i`, the defect of its complementary side is exactly

\[
                 E_i=A_T\cap\bigcap_{j\ne i}A_j.       \tag{2.5}
\]

As in Corollary 2.3, the split `C_i | (D-C_i)` is a negative low-defect
state: `|A_i|,|E_i|<=2`, and therefore both `A_i` and `E_i` are
nonempty and disjoint.  Choose

\[
                 e_i\in E_i\subseteq
                 \left(\bigcap_{j\ne i}A_j\right)-A_i. \tag{2.6}
\]

There cannot be four lobes.  Indeed, for indices `1,2,3,4`, the elements
`e_1,e_2` are distinct, and both belong to each of `A_3,A_4`.  Since
those sets have order at most two,

\[
                         A_3=A_4=\{e_1,e_2\}.
\]

But `e_3` belongs to `A_4` and does not belong to `A_3`, a contradiction.
The same argument excludes any larger number of lobes by selecting four
of them.

It remains to exclude exactly three lobes.  In that case (2.6) forces
three distinct labels `e_1,e_2,e_3` and

\[
 A_1=\{e_2,e_3\},\qquad
 A_2=\{e_1,e_3\},\qquad
 A_3=\{e_1,e_2\}.                                  \tag{2.7}
\]

Moreover (2.5) gives `E_i={e_i}`.  The singleton/pair row of the exact
low-defect atlas then gives

\[
                         A_i=N_F(e_i)
                         \qquad(i=1,2,3).             \tag{2.8}
\]

Thus every two of `e_1,e_2,e_3` are adjacent in the missing cycle `F`.
This would be a triangle in `C_6`, impossible.  A cut has at least two
lobes, so exactly two remain.  QED.

This theorem is entirely order-independent.  The internal complexity of
the minimum atom is now behind a genuine two-shore, three-vertex adhesion;
no multi-lobe case survives.

### Theorem 2.5 (four canonical two-lobe polarities)

Label the missing cycle cyclically by `0,1,...,5`.  Up to a dihedral
symmetry of that cycle and interchange of the two lobes, their defect pair
`(A_1,A_2)` is one of

\[
\begin{array}{c|c|c}
 A_1&A_2&\text{labels necessarily missed by }T\\ \hline
 \{0\}&\{1,5\}&\{0,1,5\}\\
 \{0,2\}&\{1,3\}&\{1,2\}\\
 \{0,2\}&\{1,4\}&\{0,1,2\}\\
 \{0,3\}&\{1,4\}&\{0,1,3,4\}.
\end{array}                                             \tag{2.9}
\]

Within `A_1 union A_2`, the second row may additionally miss `0`, `3`,
or both, and the third may additionally miss `4`.  The table records only
forced misses and makes no assertion about labels outside
`A_1 union A_2`.

#### Proof

Write `E_1=A_T intersection A_2` and `E_2=A_T intersection A_1`.  They are nonempty and
disjoint from `A_1,A_2`, respectively.

First, `A_1,A_2` are disjoint.  Otherwise both have order two and, since
each has a private element, they have the form

\[
                         A_1=\{a,r\},\qquad
                         A_2=\{b,r\}.
\]

Then `E_1={b}` and `E_2={a}`.  The singleton/pair atlas row forces
`A_1=N_F(b)` and `A_2=N_F(a)`, so `a,b,r` form a triangle in the missing
cycle, impossible.

If one defect is a singleton, say `A_1={0}`, the low-defect row forces
`E_1=N_F(0)={1,5}`.  Hence `A_2={1,5}`, and `E_2={0}`.  This is the first
row, including its three forced misses from `A_T`.

Now both defects have order two.  If a matching row of the atlas occurs,
the two defects are distinct antipodal pairs, giving the fourth row and
forcing all four labels into `A_T`.

Otherwise a one-hole row occurs.  After symmetry, one defect is

\[
                         A_1=N_F(1)=\{0,2\}
\]

and `1` belongs to `A_2`.  Disjointness leaves

\[
                         A_2=\{1,y\},
                         \qquad y\in\{3,4,5\}.
\]

Reflection interchanges `y=3` and `y=5`, giving the second row.  The case
`y=4` gives the third.  The reverse low-defect row forces respectively
`1,2` and `0,1,2` to belong to `A_T`; the optional misses are read from
`E_i=A_T intersection A_{3-i}`.  This proves the table.  QED.

Thus all unbounded internal geometry has been compressed to four labelled
capacity states on a two-lobe three-adhesion.
