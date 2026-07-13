# Nested rows on the ordered degree-nine portal spine

## 1. Setting and notation

Assume the corrected, strict-surplus conclusion of
hadwiger_rooted_clique_lobe_exchange.md.  Thus the globally
potential-minimal balanced model lies in the same-bag cell,
\(A=N_{L_0}(K)\), and the unique \(q\)-lobe \(U\) contains the
\(L_0\)-root \(r_0\) and every portal in \(A-\{q\}\).  There are at
least two distinct non-root portals

\[
                         a_1,\ldots,a_k\qquad(k\ge2)          \tag{1.1}
\]

which occur in this order from \(r_0\) to \(q\) on every
\(r_0\)-to-\(q\) path.

For \(i\ge2\), let \(P_i\) be the component of \(L_0-a_i\) containing
\(r_0\), and put

\[
                         S_i=L_0-P_i.                         \tag{1.2}
\]

The set \(S_i\) contains \(a_i\).

### Lemma 1.1 (nested connected splits)

For \(2\le i<j\le k\),

\[
 P_i\subsetneq P_j.                                         \tag{1.3}
\]

Both \(P_i,S_i\) are connected and adjacent.  Moreover:

* \(r_0,a_1,\ldots,a_{i-1}\in P_i\);
* \(a_i,\ldots,a_k,q\in S_i\);
* \(P_i\) is anticomplete to \(R_5\cup R_0\);
* \(S_i\) is adjacent to \(K,R_5,R_0\).

#### Proof

The nesting and the location of the \(a_j\) follow from their order on
the unique block-cut-tree path between \(r_0\) and \(q\).  The set
\(P_i\) is connected by definition.  The complement consists of
\(a_i\) together with all components of \(L_0-a_i\) other than
\(P_i\); every such component has a neighbour at \(a_i\), so \(S_i\)
is connected and adjacent to \(P_i\).

The set \(P_i\) lies in the root-bearing component \(U\) of \(L_0-q\).
The bottleneck theorem makes \(U\) anticomplete to both right bags.
The portal \(a_i\in S_i\) gives \(S_i\sim K\), while every old
\(L_0\)-portal to \(R_5,R_0\) lies outside \(U\), and hence in
\(S_i\). \(\square\)

## 2. Two explicit closures

Write \(D=L_6-K\), so \(D\) is connected, contains \(6\), and is
adjacent to \(K\).

### Lemma 2.1 (a cross-half prefix contact closes)

If \(P_i\) is adjacent to \(3\) or \(4\), then \(G\) has a
\(K_7\)-minor.

#### Proof

Suppose \(P_i\sim3\).  Use

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 D\cup R_5,\quad \{3\}\cup P_i,\quad
 \{4\}\cup K\cup S_i\cup R_0.                               \tag{2.1}
\]

The fifth set is connected through \(65\); the sixth uses the assumed
\(P_i\)-\(3\) edge; and the last is connected through the
\(K\)-\(a_i\), \(S_i\)-\(R_0\), and right-root--\(4\) edges.
The last three sets meet through a right-root--\(3\) edge, \(KD\),
and \(34\), respectively.  Their contacts to \(v,h,1,2\) come from
\(5,6,3,4\) and the roots in \(R_5,P_i,K,R_0\).
Interchanging \(3,4\) proves the other case. \(\square\)

### Lemma 2.2 (a prefix-to-\(D\) contact closes)

If \(P_i\sim D\), then \(G\) has a \(K_7\)-minor.

#### Proof

Since \(i\ge2\), the earlier portal \(a_1\) lies in \(P_i\), so
\(P_i\sim K\).  Use

\[
 \{h\},\quad\{1\},\quad\{2\},\quad P_i,\quad K,\quad
 D\cup R_5,\quad \{v,3\}\cup S_i\cup R_0.                   \tag{2.2}
\]

The sixth set is connected through \(65\).  The last is connected
through \(S_i\)-\(R_0\), the right-root--\(3\) edge, and \(3v\).
Among the four nonsingleton sets use

\[
 P_iK,\quad P_iD,\quad P_iS_i,\quad KD,\quad KS_i,\quad v5
\]

for all six adjacencies.  Their contacts to \(h,1,2\) come from the
roots in \(P_i,K,R_5,R_0\), from \(6\), and from \(v\).
Thus (2.2) is a \(K_7\)-model. \(\square\)

## 3. Exact nested separator rows

### Theorem 3.1 (ordered-prefix row)

If \(G\) has no \(K_7\)-minor, then for every \(i=2,\ldots,k\),

\[
 N_G(P_i)=\{h,1,2,a_i\}\mathbin{\dot\cup}N_K(P_i).           \tag{3.1}
\]

The sets \(N_K(P_i)\) are nested:

\[
 N_K(P_2)\subseteq N_K(P_3)\subseteq\cdots\subseteq N_K(P_k).
                                                                    \tag{3.2}
\]

Furthermore:

* \(|N_K(P_i)|\ge3\);
* equality makes \(N_G(P_i)\) an exact seven-cut;
* outside the exact-adhesion outcome, \(|N_K(P_i)|\ge4\).

#### Proof

Within \(L_0\), the component \(P_i\) can leave only through \(a_i\).
Lemma 1.1 excludes right-bag neighbours.  Lemmas 2.1 and 2.2 exclude
neighbours in \(\{3,4\}\) and in \(D\).  No exterior vertex in
\(L_0\) is adjacent to \(v\).  The root \(r_0\in P_i\) supplies the
three fixed neighbours \(h,1,2\), and every remaining neighbour lies
in \(K\).  This proves (3.1).

Nesting of the \(P_i\) implies (3.2), since \(K\) is disjoint from
every prefix.  The set in (3.1) is a genuine separator: it isolates
\(P_i\) from \(v\).  Seven-connectivity gives
\(4+|N_K(P_i)|\ge7\).  Equality is precisely an exact seven-cut, and
otherwise integrality gives the strict bound four. \(\square\)

Thus the ordered spine does not generate an uncontrolled list of local
cases.  It generates a laminar family of exact rows with one monotone
capacity coordinate \(N_K(P_i)\).

## 4. Sharp transition obstruction

The last alternative in Theorem 3.1 is a genuine obstruction rather
than an omitted quotient argument.  Contract \(P_i,S_i,K,D,R_5,R_0\)
to the six corresponding vertices and retain
\(v,h,1,2,3,4\), with exactly the adjacencies used above except
\(P_iD\).  The dependency-free verifier
degree9_ordered_spine_prefix_probe.py returns no \(K_7\)-minor.
An elimination order of width five is

\[
 3,4,P_i,K,1,2,D,R_0,R_5,S_i,h,v.                           \tag{4.1}
\]

To realize arbitrarily many distinct vertices of \(N_K(P_i)\), attach
new vertices \(x_j\) to the clique consisting of the contracted
\(P_i\)- and \(K\)-vertices, and assign every \(x_j\) to the \(K\)
bag.  These are repeated clique-sums with triangles and do not increase
treewidth.  Hence the contact-level obstruction persists with
\(|N_K(P_i)|\) arbitrarily large.

Consequently the exact strict residue is:

\[
\boxed{\text{a root prefix }P_i\text{ whose only nonfixed exits are
at least four distinct vertices of }K.}                     \tag{4.2}
\]

Connectivity and portal count alone cannot eliminate (4.2).  The next
operation must use the internal structure of \(K\): a flexible linkage
splitting \(K\), a new one-vertex bottleneck inside \(K\), or a
contraction-critical boundary-state transition.

