# The static anchor dichotomy fails in the degree-nine three-shore cell

## 1. Exact obstruction

Let the nine boundary vertices be \(0,1,\ldots,8\).  Put

\[
\begin{aligned}
 E(A)=\{&01,02,12,25,45,37,68\},\tag{1.1}\\
 M_1&=\{0,1\},\qquad M_2=\{0,2\},\qquad
 M_3=\{1,2\}.                                             \tag{1.2}
\end{aligned}
\]

Form the quotient \(Q\) by adding three pairwise nonadjacent shore
vertices \(c_1,c_2,c_3\), where \(c_i\) is adjacent to every boundary
vertex outside \(M_i\).

### Theorem 1.1

The boundary has \(\alpha(A)=4\), but

1. \(Q\) has no \(K_6\)-minor, hence no \(N\)-meeting \(K_6\)-model; and
2. there is no usable star-plus-two-shore anchor partition with zero, one,
   or two boundary singleton blocks.

Thus the finite dichotomy proposed in
`degree9_three_shore_experiment.py` is false.  The obstruction remains
after imposing every degree constraint visible from vertices missed by all
three shores, because

\[
                         M_1\cap M_2\cap M_3=\varnothing.     \tag{1.3}
\]

The independent verifier is
`degree9_three_shore_counterexample_verify.py`.

## 2. Independence number

The boundary is the disjoint union of a triangle with a length-two tail

\[
                  0,1,2\text{ spanning }K_3,qquad 2-5-4,
\]

and the two edges \(37,68\).  Its independence number is

\[
                         2+1+1=4.                            \tag{2.1}
\]

For example, \(\{0,4,6,7\}\) is independent.

## 3. A width-four certificate

Write the shore vertices as \(9,10,11\), corresponding to
\(M_1,M_2,M_3\).  The following eight bags, joined by the displayed tree
edges, form a tree decomposition of \(Q\):

\[
\begin{array}{c|l}
0&\{6,8,9,10,11\}\\
1&\{5,9,10,11\}\\
2&\{4,5,9,10,11\}\\
3&\{7,9,10,11\}\\
4&\{3,7,9,10,11\}\\
5&\{2,5,9,10,11\}\\
6&\{1,2,10,11\}\\
7&\{0,1,2,11\},
\end{array}                                                 \tag{3.1}
\]

with decomposition-tree edges

\[
        01,03,12,15,34,56,67.                               \tag{3.2}
\]

Every quotient edge occurs in a bag.  For every quotient vertex, the bags
containing it induce a subtree.  The largest bag has order five, so

\[
                         \operatorname{tw}(Q)\le4.           \tag{3.3}
\]

Since a graph containing a \(K_6\)-minor has treewidth at least five,
\(Q\) has no \(K_6\)-minor.

## 4. Why every anchor fails

Let \(S,T,P\) be the independent boundary blocks of a proposed anchor,
where \(S\) is joined through \(v\), and \(T,P\) are joined to the two
shores outside each retained side.  First ignore the optional boundary
singletons.

For retained shore \(c_1\), the two assigned miss sets are
\(\{0,2\},\{1,2\}\).  For retained \(c_2\), they are
\(\{0,1\},\{1,2\}\); for retained \(c_3\), they are
\(\{0,1\},\{0,2\}\).  In each row the two miss sets may be assigned to
\(T,P\) in either order.

### Lemma 4.1

If all three retained-side assignments exist, then

\[
                         (T\cup P)\cap\{0,1,2\}=\varnothing. \tag{4.1}
\]

#### Proof

Suppose first that \(2\in T\).  In the retained-\(c_1\) row, both
available shores miss \(2\), so neither can connect \(T\), a
contradiction.  Thus \(2\notin T\cup P\).

If \(0\in T\), then in the retained-\(c_3\) row both available shores
have miss sets containing \(0\), again impossible.  The same argument
with the roles of the blocks exchanged excludes \(0\in P\).  Finally,
the retained-\(c_2\) row excludes \(1\) from both blocks.  \(\square\)

The triangle \(\{0,1,2\}\) must therefore be covered by the independent
star block \(S\) and the optional singleton blocks.  Since \(S\) contains
at most one triangle vertex, zero or one singleton cannot suffice.

With two singletons, exactly two triangle vertices are singleton blocks
and the third lies in \(S\).  At least one singleton is \(0\) or \(1\).
Vertex \(0\) is seen by only \(c_3\), and has no boundary neighbor outside
the triangle.  In the retained-\(c_3\) minor, the assigned shore-blocks
use \(c_1,c_2\), so singleton \(0\) is adjacent to neither one.  Similarly,
singleton \(1\) fails in the retained-\(c_2\) minor.  Hence the required
five contracted images cannot form a clique.

This verifies the exact two-singleton condition: the singletons are
automatically adjacent to the star image through \(v\), and two triangle
singletons are adjacent to one another, but each must additionally meet
both shore-block images.  That last requirement fails.

## 5. What the obstruction means

This is a counterexample to the **static contact quotient**, not to
\(HC_7\).  In a hypothetical critical host the low-degree triangle
vertices force portal multiplicity inside their unique exterior
components:

\[
 |N_{C_3}(0)|\ge4,\qquad |N_{C_2}(1)|\ge4,
 \qquad |N_{C_1}(2)|\ge3.                                  \tag{5.1}
\]

Indeed, \(0,1\) have two boundary neighbors and \(2\) has three, while
each also sees \(v\) and only the indicated exterior component.

The quotient contracts each entire component to one shore vertex and
forgets precisely this multiplicity and its internal placement.  Therefore
the next viable degree-nine lemma is a label-preserving **three-shore portal
split**: use the multiple contacts in (5.1) to split at least one component
into adjacent carriers while retaining its other six boundary labels, or
return an exact small adhesion.  No strengthening based only on the three
two-element miss sets and \(\alpha(A)\le4\) can prove the desired closure,
because Theorem 1.1 is an exact obstruction to that data.
