# Independent audit: crossed-frame rural obstruction

Audited file: [`hc7_exact7_crossed_frame_rural_obstruction.md`](hc7_exact7_crossed_frame_rural_obstruction.md),
now retained beside this audit in the archive.

## Verdict

**MIXED: Lemma 2.1 is GREEN; Corollary 2.2 and the asserted scope after
Lemma 3.1 are RED.**

The protected crossed frame does prove that the literal five-cycle `U`
cannot bound one disk containing the whole terminal-free shore.  It does
**not** prove that either induced pole society is nonrural.  Both pole
societies may expand perfectly in the selected planar quotient, producing
a planar shore in which `U` is a separating cycle rather than a facial
cycle.

Lemma 3.1 itself is correct.  Its consequence applies only to one sharply
defined carrier move: a connected transferred set `D` containing both an
actual target portal and an actual locked attachment, while `K-D` remains
connected and retains `x,y`.  It does not cover all “usual transfers,”
simultaneous repartitions, disconnected pieces joined through a pole,
changes of the pair carrier, direct-`w` contacts, or first-hit
renormalization.

## 1. Lemma 2.1: GREEN

The traces are exact, so a path in `K_0` joining `x,y` has no other vertex
of `U`, and a path in `A` joining `u,z` has no other vertex of `U`.  The
blocks are disjoint.  Two disjoint nonedges of a five-cycle have alternating
ends on that cycle.  Two disjoint paths joining alternating points cannot
both lie in a disk bounded by the cycle.  The proof is complete.

The same union gives a subdivision of `K_4` rooted at `x,u,y,z`, but this
is the elementary crossed-frame `K_4`; it is not automatically the
four-`Q` rooted certificate produced by a failed pole-tree rotation.

## 2. Corollary 2.2: RED

The first sentence is safe only if “expand to a disk page” includes the
extra demand that `U` be the boundary of that disk.  The second sentence,

> At least the pole containing `A` has a genuine rotation/expansion
> obstruction,

is false.  Failure of `U`-cofaciality is not failure of local disk
substitution at a contracted pole.

Here is a literal counterexample satisfying the rural carrier geometry.
Let `K` be the wheel with hub `h` and rim

\[
                     x,q_1,q_2,q_3,y,p_1,p_2,p_3,x.            \tag{2.1}
\]

Let the target pole `X` be the tree

\[
                         u-m-z-r,                              \tag{2.2}
\]

and add the attachment edges

\[
 xu,xr,yu,yz,\qquad q_i u\quad(1\le i\le3).                   \tag{2.3}
\]

Let the locked pole be the singleton `Y={ell}` with edges
`ell p_i` for `1<=i<=3`.  The five roots induce exactly the cycle

\[
                         x-u-y-z-r-x.                          \tag{2.4}
\]

Take `A=X-r` and `B={r}`.  Then `K,A,B` are connected, disjoint,
pairwise adjacent, and have traces `xy|uz|r`.  The sets

\[
                         Q=\{q_1,q_2,q_3\},\qquad
                         P=\{p_1,p_2,p_3\}
\]

are disjoint and lie on opposite `x-y` arcs of the same carrier face.
There is no `xy|Q-P` linkage in `K`.

Contracting `X,Y` gives the selected planar two-pole quotient.  Conversely,
the displayed graph itself is planar: draw the wheel hub on one side of
its rim and place the two pole societies in the opposite face.  The
occurrence society of `X` is rural in the quotient rotation.  Around its
contracted image use the order

\[
        xr,xu,q_1u,q_2u,q_3u,yu,yz.                            \tag{2.5}
\]

For each edge of the tree (2.2), the occurrences on either side form a
cyclic interval, so the audited tree interval criterion proves rurality.
The singleton `Y` is trivially rural.

Thus both induced poles expand and the whole shore is planar.  It still
has no embedding with (2.4) as the boundary of one disk, because the
`x-y` carrier path and the `u-z` target path lie on opposite sides of that
separating cycle.  This directly falsifies the claimed inference from
Lemma 2.1 to a pole-rotation obstruction.

## 3. Lemma 3.1: GREEN in its exact statement

If `K[R]` and `K[D]` are connected, `x,y in R`, and `q,p in D`, then an
`x-y` path in `R` and a `q-p` path in `D` are disjoint.  This is exactly a
set-terminal cross.  No additional hypothesis is needed.

The valid operational corollary is only:

> There is no **single connected carrier transfer** `D` such that
> `K-D` is connected and retains `x,y`, `D` contains an actual member of
> `Q` funding its contact with the target pole, and `D` contains an actual
> member of `P` funding contact with the unchanged locked pole.

That is useful and label-faithful.  It should replace “every usual
label-faithful peel or exact decoration rotation.”

## 4. The broader transfer claim: RED

Lemma 3.1 does not apply in any of the following situations without a new
argument:

1. the transferred carrier vertices have several components which become
   connected only after absorption into `X`;
2. part of the old carrier is absorbed into `Y` as well as `X`;
3. the retained pair path is rerouted through a pole rather than lying in
   `K-D`;
4. the new decoration contact is supplied by a direct edge from `w`, not
   an original member of `P=N_K(Y)`;
5. the core/model is reselected, so its new `Q,P` are not the old portal
   sets; or
6. the operation exposes an equality state by a proper-minor colouring
   transition without realizing it as a static carrier partition.

Calling all of these “usual transfers” hides the precise duty that still
needs proof.  The source may exclude them only after defining the allowed
move and proving the needed connectivity and endpoint inheritance.

## 5. Section 4: GREEN as a static geometry, RED as a full falsifier

The plane template correctly gives:

* a planar contracted quotient;
* no set-terminal cross in the selected carrier;
* a protected crossed frame; and
* no one-disk embedding with `U` on its boundary.

The family in Section 2 above makes the stronger point that both pole
societies can be rural and the uncontracted graph itself can be planar.
It is therefore an unbounded counterexample to

\[
 \text{planar rural quotient + supported crossed frame}
 \Longrightarrow
 \text{one }U\text{-boundary disk page}.                       \tag{5.1}
\]

But Section 4 does not establish absence of every equality state or every
model reselection, and it supplies no opposite shore on which “common
state” can be evaluated.  It therefore does not by itself falsify a
statement whose alternatives include an arbitrary attained state.

A separate finite certificate in
`barriers/hc7_exact7_crossed_frame_disk_barrier.md` goes further in a
fixed core: it has a three-connected wheel carrier, disjoint portal sets
of orders three and five, the exact locked seven-neighbourhood, a planar
spanning quotient, only the displayed decoration duty, and an explicit
tree decomposition of width five excluding a `K_7` minor.  It still does
not imitate seven-contraction-critical state transitions.

## 6. Corrected remaining target

The remaining obstruction should be called **crossed-frame duty
conversion**, not induced-pole expansion.  Local pole rurality is
compatible with the obstruction.  A positive theorem must spend the
proper-minor transition family or another global HC7 hypothesis to do one
of the following:

1. consume or rotate one of the two protected alternating frame carriers
   into a common attained state;
2. complete the literal rooted `K_4` by three labelled duty carriers to a
   `K_7`; or
3. derive and colour a coherent multi-page structure.

The source's proposed dynamic conversion is a legitimate research target
after this correction, but it remains unproved.  The static rural family
does not select which of the three dynamic outcomes criticality must force.
