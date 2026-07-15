# Bounded critical kernels for support-at-most-six families

**Status:** proved.  This is a set-system certificate theorem.  It does not
align split rows or compose the selected models.

## 1. Statement

For a finite set family `F`, write `tau(F)` for its transversal number and
`rank(F)` for the largest order of a member.  Call `F` **3-critical** when

\[
 \tau(F)=3\quad\hbox{and}\quad \tau(F-\{A\})\leq2
 \quad\hbox{for every }A\in F.                         \tag{1.1}
\]

### Theorem 1.1 (bounded critical kernel)

Every 3-critical set family of rank at most six has at most 28 members.
For each member `A_i` one can moreover choose a two-set `P_i` such that

\[
 A_i\cap P_i=\varnothing,
 \qquad A_j\cap P_i\neq\varnothing\quad(i\neq j).       \tag{1.2}
\]

If equality `|F|=28` holds, there is an eight-set `X` such that

\[
 F=\binom{X}{6};                                        \tag{1.3}
\]

the sets `P_i` are the complementary pairs in `X`.

### Corollary 1.2 (live support-six kernel)

Let `G` be a seven-connected graph with no `K_7` minor.  If a family of
supports of `K_5` models on at most six vertices has transversal number
greater than two, then it contains a 3-critical subfamily of order at most
27.

## 2. Proof

Let `F={A_1,...,A_m}` be 3-critical.  For each `i`, choose a transversal
`P_i` of `F-{A_i}` of minimum order.  By (1.1), `|P_i|<=2`.  The set
`P_i` is disjoint from `A_i`; otherwise it would also meet `A_i` and would
be a transversal of `F` of order at most two.  Since `P_i` meets every
other member, (1.2) follows.  In fact `|P_i|=2`: if it had order at most
one, adjoining any vertex of the nonempty set `A_i` would give a
transversal of `F` of order at most two.

Apply Bollobas's Two Families Theorem to the ordered pairs `(A_i,P_i)`
with the uniform upper bounds `a=6` and `b=2`.  Its hypotheses are exactly

\[
 A_i\cap P_i=\varnothing,
 \qquad A_i\cap P_j\neq\varnothing\quad(i\neq j),
\]

and it gives directly

\[
                         m\leq\binom{6+2}{6}=28.        \tag{2.1}
\]

If `m=28`, the equality characterization in Bollobas's Two Families
Theorem says that equality is unique: for one
fixed set `X` of order `6+2`, the pairs `(A_i,P_i)` are all partitions of
`X` into a six-set and a two-set.  This proves (1.3).

For Corollary 1.2, take an inclusion-minimal subfamily with transversal
number greater than two.  Deleting any member leaves a two-transversal,
and adding one vertex of the deleted nonempty support shows that the
minimal family has transversal number exactly three.  The theorem gives
at most 28 members.  Equality would put a transversal-three exact-six-
support subfamily inside the eight-set `X`.  A seven-connected
`K_7`-minor-free graph has at least nine vertices (on eight vertices,
seven-connectivity gives `K_8`), so extend `X` to a nine-set `X'`.  The
same support family lies in `X'`, contradicting the audited nine-vertex
support-six closure theorem.  Hence the kernel has at most 27 members.
\(\square\)

## 3. Source and trust boundary

The set-pairs inequality, including its unique equality case, is
Bollobas's Two Families Theorem.  A convenient precise modern statement is
Theorem 17 of Asier Calbet, *K_r-saturated Graphs and the Two Families
Theorem*, Electronic Journal of Combinatorics 31(4) (2024), P4.68,
which cites the original source: B. Bollobas, *On generalized graphs*,
Acta Mathematica Academiae Scientiarum Hungaricae 16 (1965), 447--452.

The theorem bounds the number of supports in one irredundant witness
kernel.  It does not bound the order of the ambient graph, control the
supports outside that kernel, select compatible split rows, or imply any
of the existing three-model composition hypotheses.  The accompanying
barrier

[`../barriers/hc7_support_six_union_fifteen_extraction_barrier.md`](../barriers/hc7_support_six_union_fifteen_extraction_barrier.md)

shows that even a six-member critical kernel can evade the proposed
spread-out/common-core triple alternatives.
