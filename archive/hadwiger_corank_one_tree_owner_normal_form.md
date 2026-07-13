# Tree accessible bags: safe-peel descent and the nested owner corridor

## 1. Scope and verdict

This note continues
`hadwiger_corank_one_portal_basis_descent.md` in the case where the unique
accessible bag \(B\) is a tree.  It proves a sharp normalization of the
remaining two-label split lock.

The correct statement is not an unconditional portal-Helly theorem.  Even
a three-vertex path supports a static lock with two labels owned at each
end and one protected central label.  What the safe-peel theorem does prove
is the following.

* Every branch lobe not containing the protected root either admits a
  label-preserving rotation (a strict Hall descent when it contains a root
  portal), is free of model-label attachments, or wholly owns at least two
  deficient labels.
* Hence two unprotected portal-end lobes each own two fixed, disjoint label
  sets.  These owner sets persist across every cut of the portal-to-portal
  path.
* For a co-rank-one \(HC_7\) circuit there are five deficient labels, so at
  most one label remains mobile.  No other root-free lobe can contain a
  model attachment.

This is an infinite structural normalization, not a finite order check.
It supplies explicit branch sets whenever the owner lock fails and an
explicit safe peel whenever a root-free lobe owns at most one label.  It
also identifies the two genuine exceptional tails: a label-free portal
tail and a portal end protected by the old root.

## 2. Abstract labelled tree

Use the co-rank-one setup of the preceding note.  Thus

\[
                 \mathcal B=(B,B_1,\ldots,B_h),
 \qquad h=r-1,                                          \tag{2.1}
\]

where \(B\) is the only contacted bag, \(a\in B\cap N_G(v)\) is its
protected root, and the deficient labels form the Hall circuit
\(I=[h]\).  Let \(p,q\in P\subseteq B\) be two portal endpoints supplied
by the clean portal-basis theorem.  In this note \(B\) is a tree.

For every deficient label define its actual attachment set in \(B\):

\[
                         A_i=N_B(B_i)\ne\varnothing.       \tag{2.2}
\]

For a connected vertex set \(C\subsetneq B\), put

\[
                         \Omega(C)=\{i\in I:A_i\subseteq C\}.  \tag{2.3}
\]

Thus \(\Omega(C)\) is the set of labels wholly owned by \(C\); the
complementary tree piece has no edge to those bags.

When exact one-portal-per-label data are desired, assume
\(A_i=\{t_i\}\).  None of the main owner lemmas needs that restriction.

## 3. The owner-lobe peel theorem

### Theorem 3.1 (zero-or-two owner rule)

Let \(e\in E(B)\), and let \(C\) be a component of \(B-e\) which does not
contain \(a\).  If \(C\) contains a model attachment, meaning

\[
                         C\cap A_i\ne\varnothing
 \quad\hbox{for some }i,                                \tag{3.1}
\]

then either

1. the model admits a label-preserving lobe rotation moving \(C\) from
   \(B\) into some \(B_i\).  This strictly decreases \(|B|\).  If
   \(C\cap P\ne\varnothing\), the rotation can also absorb an unused-root
   path and hence increases contact or makes the Hall circuit strictly
   smaller; or
2. \(C\) wholly owns at least two deficient labels:

   \[
                         |\Omega(C)|\ge2.                 \tag{3.2}
   \]

#### Proof

Choose \(i\) satisfying (3.1).  The tree piece \(C\) is connected,
\(B-C\) is nonempty and connected, and \(a\notin C\).  It is adjacent to
\(B_i\) through a vertex of \(A_i\cap C\).

If \(\Omega(C)\subseteq\{i\}\), then for every \(j\ne i\) the set
\(A_j\) has a vertex in \(B-C\).  Hence \(B-C\) retains an edge to every
\(B_j\), \(j\ne i\).  Replace

\[
                         B\longmapsto B-C,
 \qquad B_i\longmapsto B_i\cup C.                       \tag{3.2a}
\]

Both new bags are connected.  They are adjacent through the unique tree
edge between \(C\) and \(B-C\); the new \(B_i\) retains all of its old
model adjacencies, and \(B-C\) retains every adjacency except possibly the
one to \(B_i\), which is supplied by that tree edge.  Thus (3.2a) is a
labelled \(K_r\)-model, still contacted at \(a\), with a strictly smaller
accessible bag.

If \(C\cap P\ne\varnothing\), choose \(q\in C\cap P\) and a path from an
unused root through \(U\) to \(q\).  Absorbing that path into
\(B_i\cup C\) gives the contact increase and Hall descent proved in Theorem
5.1 of the preceding note.  If neither rotation outcome is available,
\(\Omega(C)\) is not contained in \(\{i\}\).

This holds for every \(i\) with \(A_i\cap C\ne\varnothing\).  In
particular \(\Omega(C)\) can be neither empty nor a singleton: if it were
empty, any \(i\) from (3.1) would work; if it were \(\{j\}\), choosing
\(i=j\) would work because \(A_j\subseteq C\).  Thus (3.2) holds.
\(\square\)

### Corollary 3.2 (bounded number of dirty root-free lobes)

Let \(C_1,\ldots,C_s\) be pairwise disjoint edge-lobes of \(B\), none
containing \(a\), and suppose each contains a model attachment.  If no
lobe rotation or safe peel exists, then

\[
                         s\le\left\lfloor\frac h2\right\rfloor. \tag{3.3}
\]

Indeed, the owner sets \(\Omega(C_t)\) are pairwise disjoint and each has
order at least two.  This is a uniform branching bound independent of the
orders of the lobes.

## 4. The nested owner corridor

Let \(T_{pq}\) be the unique \(p\)-\(q\) path in \(B\).  Let \(e_p\) and
\(e_q\) be its end edges, and let \(C_p,C_q\) be the components of
\(B-e_p,B-e_q\) containing \(p,q\), respectively.

### Theorem 4.1 (persistent endpoint owners)

Assume

\[
 a\notin C_p\cup C_q,                                   \tag{4.1}
\]

and that both \(C_p,C_q\) contain model attachments.  If no lobe rotation
or safe peel exists, then there are disjoint fixed label sets

\[
 L=\Omega(C_p),\qquad R=\Omega(C_q),\qquad
 |L|,|R|\ge2,                                           \tag{4.2}
\]

such that for **every** edge \(e\in E(T_{pq})\), writing
\(Y_p(e),Y_q(e)\) for the two components of \(B-e\) containing \(p,q\),

\[
                         L\subseteq\Omega(Y_p(e)),
 \qquad R\subseteq\Omega(Y_q(e)).                       \tag{4.3}
\]

Consequently at most \(h-4\) deficient labels can change owner, cross the
corridor, or occur outside the two endpoint owner lobes.

#### Proof

Theorem 3.1 applied to \(C_p,C_q\) gives (4.2).  The two lobes are
disjoint, so a nonempty attachment set cannot be contained in both; hence
\(L\cap R=\varnothing\).

For every edge \(e\) of the \(p\)-\(q\) path, the endpoint lobe \(C_p\)
is contained in \(Y_p(e)\), and \(C_q\) is contained in \(Y_q(e)\).
Therefore every label whose whole attachment set lies in \(C_p\) remains
wholly on the \(p\)-side of every later cut, and symmetrically at \(q\).
This is (4.3).  The two fixed owner sets use at least four of the \(h\)
labels, proving the last assertion. \(\square\)

The word “nested” refers to the monotonicity

\[
 \Omega(Y_p(e_1))\subseteq\Omega(Y_p(e_2))              \tag{4.4}
\]

when \(e_1\) precedes \(e_2\) from \(p\) to \(q\); the \(q\)-owner sets
are nested in the reverse direction.  The fixed sets \(L,R\) are the two
end anchors of this chain.

### Corollary 4.2 (the \(HC_7\) owner normal form)

For \(r=6\), the Hall circuit has \(h=5\).  Under the hypotheses of
Theorem 4.1, four labels are trapped in two disjoint owner sets of order at
least two and there is at most one mobile label \(m\).

Moreover every edge-lobe disjoint from \(C_p\cup C_q\) and not containing
\(a\) is attachment-free.  Otherwise Theorem 3.1 would make it own two
labels, but only the one mobile label is available outside \(L\cup R\).

Thus, after attachment-free branches are pruned, all label-bearing
geometry consists of

1. the two owner lobes \(C_p,C_q\);
2. the \(p\)-\(q\) corridor;
3. the one component of \(B-T_{pq}\) which may contain \(a\); and
4. at most one mobile label.

This eliminates arbitrary branching and arbitrary portal order in the
co-rank-one tree cell.

## 5. Explicit positive branch sets when the lock breaks

For completeness, the owner language gives the exact target-minor test.
For an edge \(e\in E(T_{pq})\), put

\[
 D_p(e)=\{i:A_i\subseteq Y_q(e)\},\qquad
 D_q(e)=\{i:A_i\subseteq Y_p(e)\}.                       \tag{5.1}
\]

These are precisely the labels missed by the \(p\)- and \(q\)-pieces.
If

\[
                         |D_p(e)\cup D_q(e)|\le1,         \tag{5.2}
\]

omit that one label \(i\) (or any label if the union is empty).  Concatenate
the clean root paths to \(X\) with the far Hall suffixes to
\(B_j\), \(j\ne i\).  Absorb the two clean portal paths into
\(Y_p(e),Y_q(e)\).  The explicit branch sets are

\[
 \bigl(Y_p(e)\cup R_p\bigr),\quad
 \bigl(Y_q(e)\cup R_q\bigr),\quad
 \bigl(B_j\cup F_j\cup R_{x_j}:j\in I-\{i\}\bigr).       \tag{5.3}
\]

They are \(r\) disjoint pairwise adjacent sets, each meeting \(N_G(v)\).
Together with \(\{v\}\) they form a \(K_{r+1}\)-model.  Thus failure of
(5.3) is exactly the owner lock, not a hidden linkage intersection.

## 6. Actual adhesions: what label ownership does and does not imply

Let \(C\) be an edge-lobe of the tree.  Its actual ambient gate is

\[
                         W(C)=N_G(C).                     \tag{6.1}
\]

This is not the set of labels \(\Omega(C)\).  In the Hall setup it
decomposes into the unique tree gate, root-shore neighbours, actual
vertices of foreign bags adjacent to \(C\), a possible apex neighbour,
and any as-yet-unabsorbed outside vertices.

### Lemma 6.1 (honest adhesion alternative)

If a nonempty component \(D\) of \(G-W(C)\) is contained in \(C\), the
opposite tree piece survives, and

\[
                         |W(C)|\le k-1,                   \tag{6.2}
\]

then \(W(C)\) is an explicit vertex cut of \(G\), contradicting
\(k\)-connectivity.

If \(|W(C)|=k\), it is an exact \(k\)-adhesion.  Edge deletions or
boundary-anchored contractions supported in \(D\) and in the opposite
open shore are faithful relative to \(W(C)\), so equal boundary partitions
would colour \(G\) by crossed splicing.

#### Proof

Deleting \(W(C)\) leaves the nonempty component \(D\) and, by hypothesis,
an opposite surviving vertex.  This proves the cut assertion.  The
faithful-operation statement is Theorem 2.1 of
`hadwiger_crossed_arbitrary_minor_operations.md`. \(\square\)

The survival qualification is essential: deleting a boundary set which
contains all of a one-vertex lobe does not exhibit a separation.

There is no valid inequality

\[
                         |W(C)|\le 1+|\Omega(C)|.          \tag{6.3}
\]

A single foreign bag label may contribute arbitrarily many distinct gate
vertices, and a portal vertex may have arbitrarily many root-shore
neighbours.  Therefore label ownership alone cannot yield the requested
small actual adhesion or a repeated boundary state.  It yields either the
safe model exchange of Theorem 3.1 or the nested owner normal form; dynamic
minor-critical states are still needed to dispose of the owner corridor.

## 7. Sharp static counterarchitectures

The following examples falsify the two tempting overstatements while
realizing the exact normal form.

### Example 7.1 (the five-label owner path)

Let

\[
                         B=p-c-q,\qquad a=c,
\]

and take singleton attachment sets

\[
 A_1=A_2=\{p\},\qquad A_3=A_4=\{q\},\qquad A_5=\{c\}.    \tag{7.1}
\]

Neither end is safely peelable: removing \(p\) while transferring it to
label 1 loses label 2 from the remainder, and conversely; the same holds
at \(q\).  A carrier to label 5 contains the protected root \(c\).  Every
connected \(p\)-\(q\) split has at least two label defects.  The fixed
owner sets are \(\{1,2\}\) and \(\{3,4\}\), with label 5 mobile/protected.

Thus “a tree with two clean feet always splits” is false even with one
attachment vertex per label.  This is a static branch-bag architecture,
not a proper-minor-critical counterexample.

### Example 7.2 (one owner on each side is not automatic)

Let \(B=p-c-q\), put \(a=p\), and set

\[
 A_1=A_2=\{q\},\qquad
 A_3=A_4=A_5=\{p,q\}.                                  \tag{7.2}
\]

At the cut \(pc\), the \(q\)-side wholly owns labels 1 and 2, while the
\(p\)-side wholly owns no label.  The \(q\)-lobe is not safely peelable
because it owns two labels, and the opposite lobe is protected by \(a\).
Hence even the assertion

> every \(p\)-\(q\) cut has a wholly owned label on each side

is false without the two unprotected endpoint hypotheses in Theorem 4.1.

These examples also show why a portal-Helly argument cannot finish the
tree cell.  The reusable positive principle is the zero-or-two owner rule,
followed by the nested owner corridor and then a genuinely dynamic
transition argument on that corridor.

## 8. Exact remaining tree residue

After the clean portal-basis and safe-peel descents, a co-rank-one tree
obstruction has one of only three forms.

1. **Two-ended owner corridor.**  Two disjoint endpoint lobes own at least
   two fixed labels each.  For \(HC_7\), only one label remains mobile and
   every other root-free branch is attachment-free.
2. **Empty portal tail.**  An endpoint lobe contains a selected clean
   portal but no model-label attachment.  It cannot be removed by a Hall
   label exchange; a faithful contraction shortens it, but its boundary
   state need not match an opposite operation automatically.
3. **Root-ended lock.**  The protected root \(a\) lies in one endpoint
   lobe.  The zero-or-two rule applies only from the other end, and Example
   7.2 shows that the missing owner side cannot be inferred statically.

Any stronger conclusion must use the proper-minor transition colourings.
In particular it must show that an owner corridor has a clean rotation or
foreign-bag transit, or that two faithful operations repeat a state on an
actual ambient adhesion.  The static tree and portal data alone do not
force one of those dynamic outcomes.
