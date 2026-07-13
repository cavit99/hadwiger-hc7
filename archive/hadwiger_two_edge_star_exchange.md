# Two-edge star contraction and the reserved-connector exchange

## 1. The exact operation

Let \(G\) be a \(7\)-contraction-critical graph, let \(v\) have degree
seven, and let \(d,l\in N(v)\) be nonadjacent.  Contract the connected
star

\[
                         G[\{v,d,l\}]
\]

to a vertex \(q\), and fix a six-colouring of the resulting proper
minor.  Write \(\alpha\) for the colour of \(q\).  Expanding \(q\) gives
simultaneously

* a proper six-colouring \(c\) of \(H=G-v\), in which \(d,l\) both have
  colour \(\alpha\); and
* a proper six-colouring of
  \(F=G-\{vd,vl\}\), in which \(v,d,l\) all have colour \(\alpha\).

Put

\[
                         U=N(v)-\{d,l\}.
\tag{1.1}
\]

### Lemma 1.1 (exact trace)

The five vertices of \(U\) have the five colours different from
\(\alpha\), each exactly once.

#### Proof

Every vertex of \(U\) is adjacent to \(q\) in the contracted minor, so
none has colour \(\alpha\).  If some colour were absent from \(N(v)\) in
the expanded colouring of \(H\), it could be assigned to \(v\), giving
a six-colouring of \(G\).  Thus all six colours occur on the seven
vertices of \(N(v)\).  Since \(d,l\) are the only vertices there with
colour \(\alpha\), the assertion follows. \(\square\)

For every colour \(\beta\ne\alpha\), denote by \(u_\beta\) the unique
vertex of \(U\) with colour \(\beta\), and let \(T_\beta\) be the
\(\alpha/\beta\)-component of \(F\) containing \(v\).  In
\(F[\alpha,\beta]\), the vertex \(v\) has exactly one neighbour,
namely \(u_\beta\).  In particular \(v\) is a leaf of \(T_\beta\).
Define the nonempty owner set

\[
                    O_\beta=T_\beta\cap\{d,l\}.
\tag{1.2}
\]

### Lemma 1.2 (coupled Kempe condition)

For every \(\beta\ne\alpha\), the set \(O_\beta\) is nonempty.

#### Proof

If \(T_\beta\) contained neither \(d\) nor \(l\), interchange
\(\alpha,\beta\) on \(T_\beta\).  The vertex \(v\) would change to
\(\beta\), while \(d,l\) would remain \(\alpha\).  Restoring both deleted
edges \(vd,vl\) would then leave a proper six-colouring of \(G\), a
contradiction. \(\square\)

This is stronger than considering the contractions \(G/vd\) and
\(G/vl\) separately: all five conditions hold in one colouring and
refer to the same two deleted star edges.

## 2. Opposite owners force a reserved connector

A **reserved \(d\)-\(l\) connector** is a \(d\)-\(l\) path in

\[
                         H-U=G-(\{v\}\cup U).
\tag{2.1}
\]

Thus its internal vertices avoid all five uniquely coloured roots.

### Audit warning

In a seven-connected graph, the *bare existence* of such a path is
already immediate: delete the six vertices \(U\cup\{v\}\).  The content
of Theorem 2.1 is therefore not path existence by itself.  It locates a
connector in the union of two specified off-root Kempe components (and
possibly one specified cross-edge).  This support information is the
part that can interact with a rooted-certificate exchange.

### Theorem 2.1 (two-edge Kempe exchange)

Suppose \(O_\beta=\{d\}\) and \(O_\gamma=\{l\}\) for two distinct
colours \(\beta,\gamma\ne\alpha\).  Then \(G\) has a reserved
\(d\)-\(l\) connector.

#### Proof

Let \(L_\beta\) be the \(\alpha/\beta\)-component of \(F\) containing
\(l\), and let \(D_\gamma\) be the \(\alpha/\gamma\)-component of \(F\)
containing \(d\).  The owner assumptions imply

\[
\begin{aligned}
 &L_\beta\cap\{v,d,u_\beta\}=\varnothing,\\
 &D_\gamma\cap\{v,l,u_\gamma\}=\varnothing.
\end{aligned}
\tag{2.2}
\]

Colour considerations exclude every other member of \(U\) as well.
Hence both components avoid \(U\cup\{v\}\), apart from their respective
endpoints \(l,d\).

If \(L_\beta\cap D_\gamma\ne\varnothing\), their intersection consists
only of \(\alpha\)-coloured vertices.  Paths inside the two components
from \(l\) and \(d\) to a common vertex give, after deleting repetitions,
a reserved connector.

We may therefore assume that the two components are disjoint.  If an
edge joins a \(\beta\)-coloured vertex of \(L_\beta\) to a
\(\gamma\)-coloured vertex of \(D_\gamma\), paths to its two endpoints
inside the components, together with that edge, again give a reserved
connector.

Assume neither interaction occurs.  Simultaneously interchange
\(\alpha,\beta\) on \(L_\beta\) and \(\alpha,\gamma\) on
\(D_\gamma\).  Each interchange is proper away from edges between the
two components.  Across the two components, the only possible new
monochromatic edge would have had colours \(\beta,\gamma\) before the
interchange and colour \(\alpha\) at both ends afterwards; precisely
such an edge was excluded.  The resulting colouring is therefore
proper.  It leaves \(v\) with colour \(\alpha\), changes \(l\) to
\(\beta\), and changes \(d\) to \(\gamma\).  Restoring \(vd,vl\) gives a
six-colouring of \(G\), a contradiction. \(\square\)

The proof is an exchange axiom: if two off-root Kempe components could
be switched independently, the two bad star edges would be repaired.
Their mandatory failure to be independent is itself the reserved
connector.

## 3. The complete state dichotomy

### Corollary 3.1 (connector, root bottleneck, or unanimous owner)

In the exact trace of Section 1, at least one of the following holds.

1. There is a reserved \(d\)-\(l\) connector.
2. For some colour \(\beta\ne\alpha\), both \(d,l\in T_\beta\), and
   \(u_\beta\) separates \(d\) from \(l\) in \(T_\beta-v\).
3. Every owner set is the same singleton: either
   \(O_\beta=\{d\}\) for all five \(\beta\), or
   \(O_\beta=\{l\}\) for all five \(\beta\).

#### Proof

If \(O_\beta=\{d,l\}\), then \(T_\beta-v\) is connected and contains
\(d,l,u_\beta\), since \(v\) is a leaf.  Unless \(u_\beta\) separates
\(d,l\) there, it contains a \(d\)-\(l\) path avoiding \(u_\beta\).
The other four roots have colours outside \(\{\alpha,\beta\}\), so this
path is reserved.  This gives outcome 1 or 2.

It remains that every owner set is a singleton.  If both singleton
values occur, Theorem 2.1 gives outcome 1.  Otherwise all five values
are equal, which is outcome 3. \(\square\)

No conclusion about a rooted \(K_5\) model disjoint from the connector
is hidden here.  Outcome 1 supplies the connector before the rooted
bags are chosen; proving that the rooted certificate can be chosen
disjointly is a separate packaging step.  Outcome 2 and outcome 3 are
the two exact capacity states that this packaging theorem must handle.

## 4. Pure-Moser specialization

Use the Moser labelling

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\tag{4.1}
\]

Take \(d\in\{1,2,6\}\) and \(l\in\{3,4\}\).  Then \(dl\notin E(M)\), so
the operation above is always legitimate.  On the five unique roots
\(U=N(v)-\{d,l\}\), the graph of missing boundary edges is

* a \(C_5\) when \(d\in\{1,2\}\); and
* a connected unicyclic graph (a \(C_4\) with one pendant edge) when
  \(d=6\).

### Lemma 4.1 (unanimous ownership is impossible)

Outcome 3 of Corollary 3.1 never occurs in the pure-Moser
specialization.  More precisely, put

\[
 u=\begin{cases}
       0=h,&d\in\{1,2\},\\
       5,&d=6.
    \end{cases}
\tag{4.2}
\]

Then \(u\in U\) is adjacent to both \(d\) and \(l\), and hence

\[
                         O_{c(u)}=\{d,l\}.          \tag{4.3}
\]

Consequently, if \(T_{c(u)}-v\) has no \(d\)-\(l\) path avoiding \(u\),
the explicitly named root \(u\) separates \(d\) from \(l\) in that
two-colour component.

#### Proof

For \(d=1,2\), the Moser edges \(01,02,03,04\) show that \(h=0\) is
adjacent to both \(d\) and either choice of \(l\).  For \(d=6\), the
edges \(56,35,45\) show the same with \(u=5\).  The two length-two
paths \(vud\) and \(vul\) belong to \(T_{c(u)}\), proving (4.3).
The final assertion is the bi-owned case in Corollary 3.1. \(\square\)

Thus in every row the missing-edge graph is connected and has at most
one cycle, exactly the range in which the Kriesell--Mohr property-(*)
packaging theorem applies to the unreserved exact trace.  Combining
that packaging with Corollary 3.1 reduces the simultaneous problem to
the following sharply stated residue:

* make the property-(*) rooted \(K_5\) certificate avoid the connector
  in outcome 1;
* use the specified root cut \(u_\beta\) in outcome 2 as the entrance of
  a two-shore adhesion.

This is the precise gain from aligning the contractions \(vd\) and
\((vd)l\): arbitrary independent trace comparison is replaced by one
reserved connector and two named, finite interface states.

There is a further literal sharpening when \(d=6\).  If \(m\) denotes
the member of \(\{3,4\}-\{l\}\), the old Moser edges imply

\[
\begin{aligned}
 6&\in O_{c(1)}\cap O_{c(2)}\cap O_{c(5)},\\
 l&\in O_{c(h)}\cap O_{c(m)}\cap O_{c(5)}.
\end{aligned}
\tag{4.4}
\]

In particular \(O_{c(5)}=\{6,l\}\).  If outcome 1 is not obtained by an
opposite-singleton exchange, then one of the two families
\(\{c(1),c(2)\}\), \(\{c(h),c(m)\}\) consists entirely of bi-owned
colours.  Together with \(c(5)\), at least three distinct two-colour
components are bi-owned.  In the no-reserved-exchange row, their three
distinct roots are therefore \(6\)-\(l\) bottlenecks by outcome 2.
This is the exact first-excursion/web state left by the operation; it is
strictly stronger than an unlabelled two-shore contact count.
