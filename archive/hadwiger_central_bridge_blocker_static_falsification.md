# A central-orbit static falsification for bridge-minimal connector surgery

## 1. Verdict

Bridge minimality, seven-connectivity, one exact pure-Moser trace, and the
complete Kempe path package for that trace do **not** force a reserved rooted
model or a global cut of order at most six.

The construction below uses the central repeated pair

\[
                              6\mid3,
\]

not the exceptional `05` orbit.  Thus it applies directly to the
\(d=6,l=3\) row of the central two-edge exchange.

For its fixed exact trace, every root-avoiding supported \(6\)-\(3\)
connector contains two prescribed vertices \(t_1,t_2\), while every rooted
\(K_5\)-model on the other five Moser roots contains at least one of
\(t_1,t_2\).  Consequently even joint minimization over the connector and
the rooted model cannot make them disjoint.  The full graph is
seven-connected, so the two bichromatic bottlenecks do not promote to a
global separator of order at most six.

The example is deliberately not a hypothetical counterexample to
\(HC_7\): after adding the apex it is six-colourable.  It therefore isolates
the missing hypothesis precisely.  A successful bridge theorem must use the
palette-wall/minor-transition axiom, or \(K_7\)-minor exclusion, rather than
only the static trace and its Kempe paths.

The executable certificate is
`moser_bridge_blocker_counterarchitecture_probe.py`.

## 2. Construction

Let \(L\) be the 42-vertex planar graph whose 120 edges are listed in the
verifier.  The exact algorithms in the verifier certify

\[
                L\text{ planar},\qquad \kappa(L)=5.
\tag{2.1}
\]

The following seven vertices induce exactly the pure Moser spindle:

\[
\begin{array}{c|ccccccc}
\text{Moser label}&0&1&2&3&4&5&6\\ \hline
\text{vertex of }L&31&7&41&9&19&38&37.
\end{array}
\tag{2.2}
\]

Put

\[
 d=37\;(\text{label }6),\qquad l=9\;(\text{label }3),
\]

and let

\[
 U=\{31,7,41,19,38\}
\tag{2.3}
\]

be the five unique roots, with labels \(0,1,2,4,5\), respectively.

Add adjacent vertices \(t_1,t_2\).  Make \(t_1\) adjacent to every vertex
of \(L\) except \(l=9\) and the root \(19\), and make \(t_2\) adjacent to
every vertex of \(L\) except \(d=37\) and the root \(38\).  Call the
resulting graph \(H\).  Finally add an apex \(v\) adjacent precisely to the
seven vertices in (2.2), and call the result \(G\).

The exterior

\[
 C=V(H)-V(M)
\]

is connected and is full to the Moser boundary.  Indeed, every old
exterior vertex sees both \(t_1,t_2\), the two new vertices are adjacent,
and each of the four exceptional boundary contacts is supplied by the
other new vertex.

## 3. Connectivity audit

### Proposition 3.1

\[
                         \kappa(H)=\kappa(G)=7.
\tag{3.1}
\]

### Proof

For \(H\), first delete at most six vertices.  If both \(t_1,t_2\) are
deleted, at most four vertices of the 5-connected graph \(L\) were deleted,
so the remainder is connected.  If both survive, their edge and their
complementary exception pairs connect every surviving vertex of \(L\).

Suppose only \(t_1\) survives.  At most five vertices of \(L\) were
deleted.  Any component of the remaining \(L\) not joined to \(t_1\) would
be contained in \(\{9,19\}\).  But

\[
 d_L(9)=7,\qquad d_L(19)=6,
\]

and the external neighbourhood of \(\{9,19\}\) has order nine.  Isolating
any nonempty subset of this exception pair therefore needs at least six
deletions in \(L\), in addition to the deletion of \(t_2\).  This is
impossible.  The case in which only \(t_2\) survives is even stronger:
its exception pair is \(\{37,38\}\), the two degrees are seven and eight,
and the pair has eleven external neighbours.  Thus deleting at most six
vertices never disconnects \(H\).

The vertices 7 and 41 have degree seven in \(H\), so equality holds.

For \(G\), if \(v\) is deleted, the preceding argument applies.  If \(v\)
survives after at most six deletions, \(H\) remains connected and at least
one of the seven neighbours of \(v\) remains.  Hence \(G\) also remains
connected.  Since \(d_G(v)=7\), equality again holds. \(\square\)

In particular, no cut of order at most six can be obtained from the
bichromatic blockers below.  Notice also that deleting either \(t_i\)
does not disconnect the ambient graph.  Its cutvertex role is confined to
a colour-induced support graph.

## 4. The exact trace and all Kempe connections

The verifier records an explicit proper six-colouring \(c\) of \(H\) with

\[
 c(d)=c(l)=0,
\qquad
 (c(31),c(7),c(41),c(19),c(38))=(1,2,3,4,5),
\tag{4.1}
\]

and

\[
 c(t_1)=4,\qquad c(t_2)=5.
\tag{4.2}
\]

Thus (4.1) is the exact `63` trace.  The five missing edges on the unique
roots have the following bichromatic paths; all internal vertices lie in
the sole exterior:

\[
\begin{array}{c|l}
0\,5&31,t_2,15,38\\
1\,4&7,t_1,21,19\\
1\,5&7,t_2,4,38\\
2\,4&41,t_1,3,19\\
2\,5&41,t_2,13,38.
\end{array}
\tag{4.3}
\]

Whenever two demands in (4.3) have four distinct ends, their displayed
paths are vertex-disjoint.  Hence this is the full Rolek--Song/Kempe
package for the trace, including the required disjointness for disjoint
terminal pairs.

## 5. Every supported connector is dirty

The path

\[
                           P=d\,t_1t_2\,l
\tag{5.1}
\]

is induced.  It is also a shortest \(U\)-avoiding \(d\)-\(l\) connector.
Indeed, the only common neighbour of \(d=37\) and \(l=9\) in \(L\) is
the forbidden root 38, and neither new vertex sees both ends.

More strongly, (5.1) is forced by the exact support state.  In (4.1), the
colour-4 class is

\[
                         \{19,t_1\},
\]

and the colour-5 class is

\[
                         \{38,t_2\}.
\]

After the unique roots are forbidden, \(t_1\) and \(t_2\) are the only
remaining representatives of these two owner colours.  The vertex \(d\)
does not see \(t_2\), and \(l\) does not see \(t_1\).  Since a colour
class is independent, every root-avoiding \(d\)-\(l\) path in the union of
the \(0/4\) and \(0/5\) owner components must leave \(d\) through \(t_1\)
and enter \(l\) through \(t_2\).  Thus

\[
 \boxed{\text{every connector supported by this opposite-owner exchange
 contains both }t_1,t_2.}
\tag{5.2}
\]

This statement is about the exact supported connector class, not about all
uncoloured \(d\)-\(l\) paths in \(H\).

## 6. Every rooted model is dirty

There is a concrete \(U\)-rooted \(K_5\)-model:

\[
 \{31\},\quad \{7\},\quad \{41\},\quad
 \{19,21,t_1\},\quad \{38,14,t_2\}.
\tag{6.1}
\]

The first three singleton bags form the Moser triangle `012`.  Each of the
last two bags is connected, the edge \(t_1t_2\) joins them, and the
near-universality of \(t_1,t_2\) supplies all their adjacencies to the
three singleton bags.

On the other hand,

\[
                           H-\{t_1,t_2\}=L
\tag{6.2}
\]

is planar.  A rooted \(K_5\)-model avoiding both \(t_1,t_2\) would be an
ordinary \(K_5\)-minor of the planar graph \(L\), which is impossible.
Therefore

\[
 \boxed{\text{every }U\text{-rooted }K_5\text{-model meets }
        \{t_1,t_2\}.}
\tag{6.3}
\]

Combining (5.2) and (6.3), every supported connector meets every rooted
model.  This remains true after jointly minimizing their intersection;
it is not an artefact of having chosen the wrong initial certificate.

## 7. Exact lesson and scope

The example proves that the proposed implication

\[
\begin{array}{c}
\text{bridge-minimal connector/model}
 +\text{ seven-connectivity}
 +\text{ exact trace/Kempe paths}
\\[2mm]
\Longrightarrow
\text{reserved model or global cut of order at most six}
\end{array}
\]

is false, even in a central pure-Moser orbit.  A root bottleneck in a
bichromatic component is not a global bottleneck.

This does **not** refute a theorem which also uses the full
counterexample-derived state system.  The verifier supplies an explicit
six-colouring of \(G\).  Hence the shore accepts a boundary state with at
most five colours on the Moser boundary, whereas an actual minimal
\(HC_7\) counterexample forbids every such state.  The construction also
does not impose the one-step deletion/contraction transition for every
internal object, nor \(K_7\)-minor exclusion.

The viable target must therefore be operation-level:

> if the forced colour bottlenecks (5.2) lock every rooted model as in
> (6.3), use a proper internal deletion or contraction to create a common
> five-block boundary state; if that transition cannot be localized, its
> failure must yield the exact adhesion.

Static bridge attachment counts cannot supply this conclusion.

There is one terminological boundary.  Like every degree-seven apex setup,
the construction has the original exact cut (N(v)), isolating the
singleton apex.  If “exact adhesion” is allowed to mean that already-known
cut, the corresponding alternative is vacuous and the example of course
satisfies it.  What is falsified is the intended promotion of the
bichromatic blocker to a **new** global cut of order at most six (or to a
new nontrivial exact two-shore adhesion).  The example does not falsify an
operation-level theorem whose conclusion is a specifically typed new
seven-adhesion.
