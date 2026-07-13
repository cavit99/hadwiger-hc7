# Small nonowner shores collapse to singletons

## Theorem 1 (small-shore rigidity)

Let \(G\) be \(k\)-connected, let \(S\) have order
\(k=2q+1\), where \(q\ge3\), and let \(D\) be a connected component
of \(G-S\) with \(N(D)=S\).  Fix a boundary mode

\[
\Pi=B_1\mid\cdots\mid B_q\mid\{s\},
\qquad |B_i|=2.
\]

If \(D\) has no two-block capacity for \(\Pi\) and \(|D|\le q\), then
\(|D|=1\).

### Proof

Suppose \(n=|D|\ge2\).  For \(x\in D\), \(k\)-connectivity gives
\(d_G(x)\ge k\), and hence

\[
 |S-N_S(x)|\le d_D(x)\le n-1\le q-1.              \tag{1.1}
\]

Let

\[
 {\cal F}(x)=\{i:B_i\subseteq N_S(x)\}.
\]

Every missed root spoils at most one pair block, so (1.1) makes
\({\cal F}(x)\) nonempty.  If distinct \(x,y\in D\) had distinct
representatives \(i\in{\cal F}(x)\), \(j\in{\cal F}(y)\), then the
singleton carriers \(\{x\},\{y\}\), extended along a shortest
\(x\)-\(y\) path, would give two-block capacity.  Consequently, for
every distinct \(x,y\), the two nonempty families
\({\cal F}(x),{\cal F}(y)\) have no distinct representatives.  This
forces

\[
 {\cal F}(x)=\{i_*\}\qquad\text{for every }x\in D. \tag{1.2}
\]

Each \(x\) therefore misses at least one root from each of the other
\(q-1\) pair blocks.  All inequalities in (1.1) are equalities:

\[
 n=q,\qquad d_D(x)=q-1,
\]

so \(D=K_q\).  Moreover every \(x\) sees both roots of \(B_{i_*}\),
sees \(s\), and sees exactly one root of every other pair block.

Fix \(j\ne i_*\).  Fullness supplies vertices \(x,y\in D\) meeting the
two different roots of \(B_j\).  They are distinct.  Since \(q\ge3\),
choose \(z\in D-\{x,y\}\).  The connected carrier \(\{x,y\}\) realizes
\(B_j\), while \(\{z\}\) realizes \(B_{i_*}\); the two carriers are
disjoint and adjacent in the clique \(D\).  This is two-block
capacity, a contradiction. \(\square\)

## Lemma 2 (at most one full singleton shore)

If \(G\) is \(r\)-minor-critical, an exact cut \(S\) has at most one
singleton component full to \(S\).

### Proof

Two such components \(\{x\},\{y\}\) are nonadjacent false twins with

\[
N(x)=S=N(y).
\]

Colour the proper minor \(G-x\) with \(r\) colours and give \(x\) the
colour of \(y\).  This is proper and colours \(G\), a contradiction.
\(\square\)

## Corollary 3 (pair-mode descent is forced)

Assume the exact-ownership theorem for a pair mode with \(q\ge6\).
Then its unique owner leaves \(q-1\) nonowner shores.  The atomic
nonowner theorem says that every nonowner is of order at most \(q\) or
contains a proper exact \(k\)-fragment.  Theorem 1 turns the first
alternative into a singleton, and Lemma 2 permits at most one such
shore.  Therefore at least

\[
q-2
\]

distinct nonowner shores contain nested exact \(k\)-fragments.

This removes the bounded-shore alternative as a source of an
uncontrolled family.  It does not by itself show that a nested exact
cut has fewer components; that overlap problem needs additional
rooted structure in the new boundary.

