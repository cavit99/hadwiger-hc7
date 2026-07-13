# Universal Moser traces close the two-shore ownership-direction gap

## 1. Setting

Let \(G\) be seven-connected and six-minor-critical. Let \(v\) have
degree seven, put \(S=N_G(v)\), and assume \(G[S]\) is the pure Moser
spindle. Let \(D,C\) be two distinct components of \(G-N[v]\). They
are connected, anticomplete, and full to \(S\).

Fix a nonempty matching \(F\) of edges internal to \(D\). Contracting
all edges of \(F\) is the operated-side minor step. The theorem below
also works for any collection of disjoint connected contraction sets,
but a matching is the form needed at an interface lock.

## 2. Every prescribed nonedge normalizes or gives a path

The complement of the Moser spindle has edge set

\[
 Q=\{05,06,13,14,15,23,24,25,36,46\}.            \tag{2.1}
\]

### Lemma 2.1 (matching completion)

Let \(I,J\in Q\) be vertex-disjoint. Among the three remaining labels
there is an edge \(K\in Q\).

#### Proof

If not, the remaining triple is a triangle of the Moser spindle. Its
four triangles and the complement edges induced on the other four
vertices are

\[
\begin{array}{c|c}
012&36,46\\
034&15,25\\
126&05\\
345&06
\end{array}
\]

In every row those complement edges have matching number at most one,
so the other four vertices cannot contain the two disjoint edges
\(I,J\). \(\square\)

### Lemma 2.2 (universal trace production)

For every \(I\in Q\), at least one of the following holds.

1. There is a path joining two nonadjacent roots of \(S\), with its
   interior in one component of \(G-N[v]\), obtained as a two-colour
   Kempe path in \(G-v-F\).
2. There is a four-block matching mode

   \[
   \Pi_I=I\mid J\mid K\mid\{r\}                  \tag{2.2}
   \]

   which extends \(C\) and \(D-F\), but does not extend the original
   shore \(D\).

#### Proof

Simultaneously contract the connected star \(v\cup I\) and every edge
of \(F\). The contraction sets are disjoint, so the result is a proper
minor and has a six-colouring. Delete the contracted apex \(v\), expand
the two roots of \(I\) monochromatically, and expand every contracted
edge of \(F\) after deleting that edge. This gives a colouring of
\(G-v-F\) in which \(I\) is an exact boundary colour block.

Every other boundary colour class has order at most two, since
\(\alpha(G[S])=2\). If the five roots in \(S-I\) already use three
colours, their block sizes are \(2,2,1\), giving (2.2).

If they use five colours, choose any nonedge \(J\) among them. If the
two singleton colours of \(J\) lie in one Kempe component, a shortest
two-colour path between the roots has no other boundary vertex in its
interior. It avoids \(v\), and components of \(G-N[v]\) are
anticomplete, so its interior lies in one exterior component. This is
outcome 1. Otherwise switch one component and merge \(J\) into one
exact block.

There are now four colours on \(S-I\): one pair \(J\) and three
singletons. Lemma 2.1 gives a nonedge \(K\) among those singletons.
The identical Kempe argument either gives outcome 1 or merges \(K\).
The result is (2.2). If the original five roots used four colours, skip
the first switch and apply this last paragraph to their existing pair.
All switches avoid the colour of \(I\), so its trace remains exact.

The final colouring restricts to extensions over every unchanged
component, in particular \(C\), and over \(D-F\). If \(\Pi_I\)
extended the original \(D\), align that extension with the fixed
colouring on all other exterior components. This would six-colour
\(G-v\). Since only four colours occur on \(S=N(v)\), one of the two
remaining colours could then be assigned to \(v\), six-colouring
\(G\). Thus \(\Pi_I\) does not extend \(D\). \(\square\)

## 3. The accepting shore is necessarily packet-deficient

### Lemma 3.1 (correct transfer direction)

For every mode \(\Pi_I\) supplied by Lemma 2.2, the accepting shore
\(C\) has no two-block capacity.

#### Proof

Suppose \(C\) has disjoint carriers for two pair blocks of
\(\Pi_I\). Enlarge them along a shortest connector in \(C\) so they
are adjacent. The apex singleton \(\{v\}\) is a carrier for the third
pair block, because \(v\) is adjacent to all of \(S\).

Contract the two carriers together with their boundary blocks, contract
\(v\) together with the third pair block, retain the singleton block,
and retain \(D\). The four block images form a clique: (2.2) is an
optimal proper four-colouring of the Moser boundary, so every two
blocks have a boundary edge between them. A six-colouring of this
proper minor expands to an extension of \(\Pi_I\) over \(D\),
contrary to Lemma 2.2. \(\square\)

This is the missing ownership-direction step. Capacity in the accepting
shore would transfer the state back to the operated shore, using the
apex as the carrier for the third block.

## 4. Small accepting shores cannot survive

Assume from now on that Lemma 2.2 never gives a path and that \(C\)
exposes no exact seven-cut.

The separator-capacity theorem with three active pair blocks shows that
\(C\) is three-connected: a cutvertex forces two-block capacity, and a
two-cut gives an exact seven-cut.

We next prove \(|C|\ge7\). A full nonowner of order at most three
collapses to a full singleton by the pair-mode small-shore theorem.
That singleton and \(v\) would be nonadjacent false twins with
neighbourhood \(S\), impossible in a vertex-critical graph. Hence
\(|C|\ge4\).

For every Moser nonedge \(xy\), the family contains a mode in which
\(\{x,y\}\) is a pair block. No vertex of \(C\) can see both \(x,y\):
such a vertex is a singleton carrier, and the small-carrier theorem
would force two-block capacity. Therefore

\[
 N_S(z)\text{ is a clique of the Moser spindle},
 \qquad |N_S(z)|\le3                              \tag{4.1}
\]

for every \(z\in C\). Since \(\delta(G)\ge7\), equation (4.1) gives
\(d_C(z)\ge4\).

If \(|C|=4\), this is impossible. If \(|C|=5\), it makes
\(C=K_5\), while failure of one pair-packet and the bare-web theorem
make \(C\) planar. If \(|C|=6\), planarity and minimum degree four
force \(C\) to be the octahedron. Four portal classes belonging to any
two pair blocks have an SDR by the relative Hall lemma, and the
four-connected maximal-planar octahedron is two-linked by Jung's
theorem. This again gives a forbidden two-block packet. Hence

\[
 |C|\ge7.                                         \tag{4.2}
\]

## 5. Exact two-shore exchange

### Theorem 5.1 (single-trace ownership exchange)

In the setting of Section 1, at least one of the following occurs.

1. A normalization in Lemma 2.2 gives an exterior two-colour path.
2. The accepting shore \(C\) exposes an exact seven-cut.

#### Proof

Fix any one \(I\in Q\). If Lemma 2.2 gives its path outcome, conclusion
1 holds. Otherwise it gives a mode \(\Pi_I\), and Lemma 3.1 says that
\(C\) is a nonowner for this one mode.

If \(|C|=1\), its vertex and \(v\) are nonadjacent false twins with
neighbourhood \(S\), impossible in a vertex-critical graph. Hence
\(|C|\ge2\). The arbitrary-shore packet-or-exact-adhesion theorem
(Theorem 1.2 of hadwiger_atomic_threeblock_nonowner_collapse.md) now
forces a proper exact seven-fragment inside \(C\). This is conclusion
2. \(\square\)

Theorem 5.1 closes the state/capacity **direction** gap for an operated
Moser shore, and in fact needs only one prescribed trace. The universal
ten-trace/antipodal argument remains an independent synchronization
certificate, but is no longer needed for this local exchange. The
theorem does not assert that the exterior path by itself is already a
\(K_7\)-model; that path must still be absorbed into the current
branch-set geometry. A packet-deficient accepting shore is nevertheless
no longer an unbounded alternative: it descends through an exact
adhesion unless the normalization supplies an actual path.
