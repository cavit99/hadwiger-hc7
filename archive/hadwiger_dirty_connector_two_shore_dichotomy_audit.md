# Adversarial audit of Theorem 8.5 and Corollary 8.6

## Verdict

**GREEN, with the quantifier and adjacency clarifications now inserted
in the source.**  Off-path absorption preserves the complete
$K_7^-$-model data, the same fixed shortest path may be used throughout
the descent, and the two-vertex endpoint reduces to a singleton exactly
as claimed.

## 1. Purity

For the current portal classes

\[
 A=N_K(D_2),\qquad B=N_K(D_1),
\]

Corollary 8.4 gives $A\subseteq W$, or $B\subseteq W$, or says that no
component of $K-W$ contains both labels.  In the first two cases an
off-$W$ component contains no portal of the class contained in $W$;
in the third it cannot contain both.  Thus every component is genuinely
pure.  This inference does not require the three alternatives to be
exclusive.

Because the ambient graph is $K_7$-minor-free, $D_1,D_2$ are
anticomplete: an edge between them would supply the sole unrequired edge
of (8.8).

## 2. Absorbing one component

Let $U$ be a component of $K-W$.

* If $U$ has no shore portal, deleting it from the model removes no
  required adjacency or portal.
* If it has only $D_\ell$-portals, then
  $D'_\ell=D_\ell\cup U$ is connected.  Purity says that it has no
  edge to $D_{3-\ell}$, so the deficient pair remains anticomplete.
* Two-connectivity of $K$ gives at least two distinct neighbours of
  $U$ on $W$.  These become two distinct $K'$-portals to $D'_\ell$.
* Every portal to the opposite shore lies outside $U$, hence remains
  in $K'$.
* The fixed root $r$, fixed $C$-portal $q$, and every specified root in
  the shore bags stay in their original branch-set roles.

The six nonsingleton-bag pairs are

\[
 CK',\ CD'_\ell,\ CD_{3-\ell},\ K'D'_\ell,
 K'D_{3-\ell},\ D'_\ell D_{3-\ell}.
\]

The first five retain or gain required edges; the last remains the sole
deficient pair.  Contacts to the singleton triangle are retained by the
unchanged specified roots.

## 3. Fixed-path iteration

The same $W$ works at every stage.

1. Vertex deletion cannot create a shorter $r$-$q$ path, so $W$
   remains shortest.
2. An absorbed $U$ is a whole component of $K-W$.  It has no edge to
   another off-$W$ component.  Hence absorption can create new portals
   only at attachment vertices on $W$; it does not change the label set
   of any surviving component.
3. Both portal classes retain order at least two, so Corollary 8.4 can
   be reapplied whenever the new root bag is two-connected.

If all off-$W$ components are removed, the root bag induced by $W$ is
exactly a path.  A nonconsecutive chord would shorten $W$.  It is
therefore not two-connected, so the finite descent terminates as stated.

## 4. Two-vertex endpoint

Every root bag throughout the descent contains $W$.  If the terminal
bag has two vertices, Corollary 8.3 and connectedness force

\[
                         K=W=rq.
\]

Portal multiplicity then makes both $r,q$ adjacent to each of
$D_1,D_2$.  Moving $q$ into $C$ preserves:

* connectedness of $C\cup\{q\}$, through the original $qC$-edge;
* the $r$-to-carrier edge, through $rq$;
* both $rD_\ell$ edges;
* every old $CD_\ell$ edge; and
* anticompleteness of $D_1,D_2$.

Thus Corollary 8.6 is valid.  No hidden re-selection of $W$, $q$, or
the specified roots is needed.
