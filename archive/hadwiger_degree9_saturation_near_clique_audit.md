# Edge saturation and the bilateral near-\(K_7\) lock

## 1. The general edge-addition certificate

The following elementary lemma is the exact information supplied by
edge-maximality.  It is useful beyond the degree-nine cell.

### Lemma 1.1 (critical nonedge dichotomy)

Let \(G\) have no \(K_t\)-minor, let \(xy\notin E(G)\), and suppose
\(G+xy\) has a \(K_t\)-minor.  Then one of the following holds.

1. \(G\) has a rooted \(K_t^-\)-model whose unique nonrequired pair
   consists of a bag containing \(x\) and a bag containing \(y\).
2. There are pairwise disjoint connected sets
   \[
          X,Y,C_1,\ldots,C_{t-1}
   \]
   such that \(x\in X\), \(y\in Y\), \(X\) and \(Y\) are anticomplete,
   the \(C_i\) form a \(K_{t-1}\)-model, every \(C_i\) meets at least
   one of \(X,Y\), and each of \(X,Y\) misses at least two of the
   \(C_i\).

#### Proof

Take a \(K_t\)-model in \(G+xy\) and make the use of the new edge
minimal.  If \(xy\) joins two different bags, deleting it gives outcome
1.  Otherwise it belongs to a tree in one bag.  Deleting \(xy\) from
that tree splits the bag into connected sets \(X,Y\), containing
\(x,y\), respectively.  There is no old \(X\)-\(Y\) edge, since such
an edge would reconnect the bag in \(G\).  The other \(t-1\) bags are
the \(C_i\); they form a clique model and every one meets \(X\) or
\(Y\).

Neither side meets all \(C_i\), or that side together with the
\(C_i\) is a \(K_t\)-model in \(G\).  If, say, \(X\) misses exactly
one bag \(C_j\), then \(Y\sim C_j\).  Replacing \(C_j\) by
\(C_j\cup Y\) gives a rooted \(K_t^-\)-model: its only nonrequired
pair is \(X,(C_j\cup Y)\).  Thus, outside outcome 1, both sides miss
at least two core bags. \(\square\)

In particular, the often-used inference

\[
       G+xy\succeq K_t\quad\Longrightarrow\quad
       G\text{ has a port-labelled }K_t^-
\]

is valid only after excluding the split-bag outcome 2.

## 2. Three near-cliques are already present

Use the conservative bilateral same-bag quotient with vertices

\[
 v,h,1,2,3,4,U,D,V,C,L,R.
\]

The fixed edges are exactly those in
`degree9_opposite_bypass_quotient_probe.py`: the Moser boundary,
the left and right root contacts, and

\[
 UD,\ VC,\ DC,\ UL,\ VR,\ DR,\ CL,\ LR.                 \tag{2.1}
\]

The three strategically missing edges \(UC,VD,UV\) are all
\(K_7\)-critical.  More strongly, before adding anything the quotient
already has the following port-labelled \(K_7^-\)-models:

\[
\begin{array}{c|l|l}
\text{missing contact}&\text{seven bags}&\text{completing edge}\\ \hline
U-(vC)&h,1,2,U,L,(vC),(DR)&UC\\
V-(vD)&h,3,4,V,R,(vD),(CL)&VD\\
U-(v3V)&U,(v3V),h,1,2,(4DC),(LR)&UV.
\end{array}                                               \tag{2.2}
\]

Parentheses denote unions forming one connected bag.  Direct inspection
of (2.1) audits all twenty adjacencies in each row; the displayed pair
is the only missing one.  Thus a restricted edge-maximal completion
which preserves the degree-nine Moser neighbourhood cannot add any of
these three edges.  Saturation does not create new contact at the live
interfaces; it merely rediscovers three deficiencies already encoded by
the balanced model.

There is an analogous certificate at every ordered prefix row.  With
the notation of `hadwiger_degree9_ordered_spine_prefix.md`, adding a
missing \(P_iD\) edge completes

\[
 \{h\},\{1\},\{2\},P_i,K,D\cup R_5,
             \{v,3\}\cup S_i\cup R_0                     \tag{2.3}
\]

to a \(K_7\)-model.  Without the added edge, (2.3) is a \(K_7^-\)-model.
The existing replacement path \(P_i-K-D\) uses the whole reserved
\(K\)-bag internally.  Hence replacing the artificial edge is exactly
the root-owning split problem, not an automatic path substitution.

Likewise, the old paths \(U-D-C\) and \(U-L-C\) which could replace
\(UC\) run through two different reserved bags in the first row of
(2.2).  They are not label-clean.  The same observation holds
symmetrically for \(VD\).

## 3. The three models do not align statically

### Proposition 3.1 (sharp bilateral saturation obstruction)

The quotient in Section 2 has all three port-labelled \(K_7^-\)-models
in (2.2), but

1. it has treewidth at most five and hence no \(K_7\)-minor;
2. it is not 2-apex; and
3. every \(K_7^-\)-model in it has at least two nonsingleton bags.

#### Proof

For item 1, eliminate in the order

\[
 U,1,2,V,3,4,v,h,D,C,L,R.                                \tag{3.1}
\]

After filling later neighbours, every later-neighbour set has order at
most five.  This is a width-five chordal completion.

For item 2, the graph contains the following nine Kuratowski
subdivisions:

\[
\begin{array}{c|l}
0&K_5[h,1,2,U,L]\\
1&K_5[h,3,4,V,R]\\
2&K_{3,3}[\{1,2,C\};\{D,L,v\}]\\
3&K_{3,3}[\{3,4,D\};\{C,R,v\}]\\
4&K_{3,3}[\{C,R,U\};\{D,L,h\}],\quad Ch\text{ subdivided by }v\\
5&K_5[1,2,D,U,h],\quad Dh\text{ subdivided by }v\\
6&K_5[3,4,C,V,h],\quad Ch\text{ subdivided by }v\\
7&K_5[1,2,D,L,U],\quad DL\text{ subdivided by }R\\
8&K_5[3,4,C,R,V],\quad CR\text{ subdivided by }L.
\end{array}                                               \tag{3.2}
\]

No two vertices meet all nine witnesses.  Indeed, the first two meet
only in \(h\).  If an alleged transversal contains \(h\), its other
vertex would have to lie in the intersection of witnesses 2--8, which
is empty.  Otherwise it has the form

\[
 a\in\{1,2,U,L\},\qquad b\in\{3,4,V,R\}.
\]

For these sixteen possibilities, a witness avoiding both is given by

\[
\begin{array}{c|cccc}
 &3&4&V&R\\ \hline
1&4&4&3&6\\
2&4&4&3&6\\
U&2&2&2&2\\
L&5&5&3&5.
\end{array}                                               \tag{3.3}
\]

The entries are indices from (3.2).  Thus deleting any two vertices
leaves a nonplanar graph.

For item 3, six singleton bags in a \(K_7^-\)-model would induce a
\(K_6^-\) subgraph.  The quotient has no such six-vertex set.  One
quick check is that its only \(K_5\) subgraphs are the first two rows
of (3.2), which intersect only in \(h\); a \(K_6^-\) contains two
\(K_5\)'s sharing four vertices.  Therefore no near-clique model has
only one complex bag. \(\square\)

The dependency-free verifier
`degree9_saturation_near_clique_verify.py` checks the chordal
completion, all three models, all nine Kuratowski subdivisions and
their transversal, and the absence of a \(K_6^-\) subgraph.

The obstruction persists with literal ordered spines and arbitrarily
large strict portal capacity.  Every graph in the family
`build_double_same_spines(m,c)` from
`degree9_complementary_star_probe.py` contracts to the quotient above
(delete the capacity vertices and contract each spine to its ordinary
bag).  Proposition 6.1 of
`hadwiger_degree9_double_same_bag_counterarchitecture.md` gives the
same width-five upper bound for the entire family.  Since being 2-apex
is minor-closed, Proposition 3.1 also shows that every member is
non-2-apex.

## 4. Exact strategic conclusion

The proposed static implication

\[
\begin{split}
 &\text{two ordered frames with arbitrary strict portal capacity}\ +
   \text{the three edge-critical near-cliques}\\
 &\hspace{35mm}\Longrightarrow K_7\text{ or 2-apex}
\end{split}                                               \tag{4.1}
\]

is false.  It fails already in the twelve-role quotient and continues
to fail with arbitrary spine length and portal multiplicity.  The induced
four-web obstruction in this family may be degenerate (so its cell-load
condition is vacuous); consequently this proposition does not refute an
additional hypothesis prescribing a nontrivial loaded facial cell.

This does not refute the route in the hypothetical counterexample,
because the counterarchitecture is neither seven-connected nor
contraction-critical.  It does identify the indispensable input:

* an added edge can only be replaced after a **label-preserving split**
  of a reserved bag;
* the family of three near-cliques has no one-complex-bag member to
  which a one-bag split theorem could be applied directly; and
* neither edge-maximality, ordered web geometry, portal count, global
  model minimality, nor even non-2-apexness supplies that split.

Thus the saturation route can progress only by using the one-step
minor-critical colour transition (or seven-connectivity in a genuinely
path-preserving way) to break the unique carrier ownership.  Completing
the graph first loses precisely that transition data, so unrestricted
edge-maximal completion is strategically counterproductive.
