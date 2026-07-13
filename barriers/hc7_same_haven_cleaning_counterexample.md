# Same-haven agreement still does not clean a transit linkage

There is a finite, independently checkable obstruction to the abstract
upgrade from *haven agreement plus a Rado linkage* to a rooted model.

Let (I) be the icosahedral graph in its standard two-cap presentation:
vertices (T,S,a_0,\ldots,a_4,b_0,\ldots,b_4); (T) sees every
(a_i), (S) sees every (b_i); the (a_i)'s and (b_i)'s form
5-cycles; and (a_i) sees (b_i,b_{i-1}) (indices modulo five).
Let (H=I+TS), and put

\[
                 N=\{T,S,a_0,a_1,b_0\}.
\]

The graph (H) is 5-connected.  It has the following (K_5)-model:

\[
 \{T\},\quad \{S\},\quad \{a_0,b_0\},\quad
 \{a_1,b_1\},\quad \{a_3,a_4,b_2\}.             \tag{1}
\]

The five disjoint paths

\[
 \{T\},\quad\{S\},\quad\{a_0\},\quad\{a_1\},
 \quad b_0b_1b_2                                      \tag{2}
\]

end in a transversal of the five displayed bags.  Notice the genuine
transit: the last path starts in the third bag and passes through the
fourth before ending in the fifth.

There is a proper 5-colouring, written in the order above, given by

\[
\begin{array}{c|cccccccccccc}
x&T&S&a_0&a_1&a_2&a_3&a_4&b_0&b_1&b_2&b_3&b_4\\ \hline
c(x)&0&1&2&3&1&2&1&4&0&3&4&0.
\end{array}                                           \tag{3}
\]

Thus (N) is rainbow.  Since (H-X) is connected for every
(|X|<5), the colour component and the model-haven component agree
for every such (X); moreover that component contains the unique
(N)-vertex of every colour absent from (c(X)).  This is precisely
the full-palette alignment conclusion used before the Rado step.

Nevertheless (H) has no (N)-rooted (K_5)-model.  The exhaustive
certificate

[`verify_icosahedron_haven_cleaning_counterexample.py`](verify_icosahedron_haven_cleaning_counterexample.py)

checks the edge list, colouring, all vertex cuts of order at most four,
the model (1), the linkage (2), and all (6^7=279936) assignments of
the seven nonroots to five rooted branch sets or the unused class.  The
last enumeration is complete: every branch set already contains its
prescribed root, and every other vertex is either assigned to exactly
one bag or unused.

Hence even *full component alignment for every cut below (r)* plus a
full (r)-path transversal does not, as an abstract structural lemma,
force a clean first-hit permutation or an (N)-meeting (K_r)-model.

There is one essential qualification.  Adding an apex adjacent exactly
to this (N) leaves a 5-colourable graph; the certificate is therefore
not a counterexample to the complete non-(r)-colourable-apex setting.
It proves that any successful upgrade must use the global saturation
condition across **all** (r)-colourings (or minor-critical transition
witnesses), not merely the one-colouring haven alignment already proved.
