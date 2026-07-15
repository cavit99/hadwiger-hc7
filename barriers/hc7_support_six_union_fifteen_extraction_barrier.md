# A critical-kernel barrier to spread-out triple extraction

**Status:** proved abstract set-system barrier.  It is not asserted to be
realizable by small `K_5` models in a seven-connected graph.

## 1. Construction

On `V={0,1,...,14}`, let `F={E_0,...,E_5}` consist of

\[
\begin{array}{c|l}
0&9,10,11,12,13,14\\
1&3,4,7,9,10,13\\
2&0,1,2,5,8,14\\
3&0,4,5,8,11,12\\
4&1,2,7,11,12,13\\
5&4,6,7,10,12,14.
\end{array}                                             \tag{1.1}
\]

This six-uniform family is inclusion-minimal with transversal number
three, its union has order fifteen, but every three members have union at
most fourteen and intersection at most two.

Consequently it refutes both of the following proposed conclusions, even
under the extra hypothesis that no transversal-three subfamily has union
at most nine:

1. three members have union at least fifteen;
2. three members have a common four-core and pairwise disjoint two-point
   remainders.

## 2. Transversal number and criticality

For a vertex `v`, put

\[
                        J(v)=\{i:v\notin E_i\}.
\]

The distinct values are

\[
\begin{array}{c|c@{\qquad}c|c}
v&J(v)&v&J(v)\\ \hline
0,5,8&0145&1,2&0135\\
3&02345&4&024\\
6&01234&7&023\\
9&2345&10&234\\
11&125&12&12\\
13&235&14&134.
\end{array}                                             \tag{2.1}
\]

These sets are pairwise intersecting.  Here is a short complete check.
Every set in (2.1) contains `1` or `2`.  Sets containing both meet all the
others through one of those symbols.  The sets containing `1` but not `2`
are

\[
                         0145,\quad0135,\quad134,
\]

and those containing `2` but not `1` are

\[
                02345,\quad024,\quad023,\quad2345,
                \quad234,\quad235.
\]

Reading across the latter list, common symbols with the three former
sets may be chosen respectively as

\[
\begin{array}{c|cccccc}
0145&0&0&0&4&4&5\\
0135&0&0&0&3&3&3\\
134 &3&4&3&3&3&3.
\end{array}
\]

Thus, for every vertex pair `{u,v}`, some `i` belongs to
`J(u) cap J(v)`, and `E_i` is disjoint from that pair.  No two vertices
meet all of `F`.

On the other hand, deleting `E_i` leaves the following two-transversal,
which is disjoint from `E_i`:

\[
\begin{array}{c|cccccc}
i&0&1&2&3&4&5\\ \hline
P_i&07&0\,12&3\,12&1\,10&0\,10&0\,13.
\end{array}                                             \tag{2.2}
\]

For example `P_0={0,7}` meets `E_1,...,E_5`; the other five columns are
checked directly from (1.1).  Adding any vertex of `E_i` to `P_i` gives a
three-transversal of the whole family.  Hence `tau(F)=3`, and (2.2) proves
that deleting any member lowers the transversal number to at most two.
Every proper subfamily is contained in one of these deletions, so no
proper subfamily has transversal number three.  Since the union in (1.1)
is all of `V`, the hypothesis excluding a transversal-three subfamily on
at most nine vertices is satisfied.

## 3. Triple unions

For each triple of indices, the following table gives a vertex omitted by
all three corresponding members:

\[
\begin{array}{c|cccccccccc}
I&012&013&014&015&023&024&025&034&035&045\\
v&6&1&0&0&3&3&3&3&1&0\\[1mm]
I&123&124&125&134&135&145&234&235&245&345\\
v&6&6&11&6&1&0&3&3&3&3.
\end{array}                                             \tag{3.1}
\]

Thus every triple union is a proper subset of the fifteen-point ground
set and has order at most fourteen.

## 4. Triple intersections

The support-incidence sets `I(v)={i:v in E_i}` are the complements in
`{0,...,5}` of the sets in (2.1).  Only seven vertices occur in at least
three members:

\[
\begin{array}{c|ccccccc}
v&4&7&10&11&12&13&14\\ \hline
I(v)&135&145&015&034&0345&014&025.
\end{array}                                             \tag{4.1}
\]

No triple of indices occurs in more than two entries of (4.1): the sole
repetition is `034`, at vertices `11,12`.  Therefore every triple
intersection has order at most two.  In particular no three members have
a common four-core, regardless of how their complementary two-point rows
are marked.

## 5. Consequence

The nine-vertex closure is a sharp threshold for *local graph
realizations*, not a set-system extraction theorem that forces the next
three-model composition pattern.  Even an irredundant transversal-three
kernel can spread over fifteen vertices while every triple remains below
the published union threshold.  Any next extraction theorem strong enough
for HC7 must use graph realization, split-row decorations, or the private
pairs as labelled graph objects; bare support incidence is insufficient.
