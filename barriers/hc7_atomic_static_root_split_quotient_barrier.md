# Barrier: the canonical two-carrier quotient is not enough

**Status:** explicit local counterexample; not an `HC_7` counterexample.

This barrier rules out the tempting shortcut

> no adaptive return for the canonical carriers implies an
> `S`-rooted `K_5` in the graph obtained by contracting those carriers.

Internal thin-shore geometry is essential.

## Construction

Let the boundary frontier be the path

\[
                         w_0-w_1-u-w_2-w_3-w_4-w_5.
\]

Add adjacent carrier vertices `x,y`.  Join `x` only to `u`, and join `y`
to every `w_i` but not to `u`.  Thus the literal carrier lists are

\[
                         \Lambda(u)=\{x\},
              \qquad \Lambda(w_i)=\{y\}\quad(0\le i\le5).
\]

There is no adaptive empty/singleton reservoir.  With no deletion there is
a monochromatic `w_iw_{i+1}` edge.  Deleting `u` leaves monochromatic path
edges on both sides.  Deleting any one `w_i` still leaves a monochromatic
edge in at least one of the two paths induced by the other five `w`'s.

The quotient has no `K_5` minor.  After deleting `y`, what remains is a
tree: the displayed boundary path plus the leaf edge `xu` (and `x` loses
its edge to `y`).  In any `K_5` model, deleting the branch set containing
`y` would leave a `K_4` model in that forest; if no branch set contains
`y`, the whole `K_5` model already lies in the forest.  Both are impossible.
Therefore there is no `S`-rooted `K_5` either.

The example deliberately fails the full atomic kernel: its thin shore has
only the edge `xy`, the root has internal degree one, and global
seven-connectivity is absent.  It proves only that a positive decoder must
use the uncontracted two-connected/fully-crossed shore, the relative
seven-cut inequalities, or a proper-minor response.

`active/hc7_root_split_frontier_minor_check.py` exhausts the same static
question over every audited connected-bipartite frontier and all canonical
root-split list masks.  That computation is supplementary evidence; the
explicit path construction above is the barrier proof.
