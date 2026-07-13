# Central exact-two-shore round: audited endpoint

## Standing row

Let \(G\) be a hypothetical minor-minimal \(HC_7\) counterexample with a
degree-seven vertex \(v\) whose neighbourhood is the pure Moser spindle.
In the central exact-cut row,

\[
 S=\{h,1,2,5,6,y,z\}
\]

has two full shores \(C_v,D\), with \(v\in C_v\), and a component \(R\)
of \(C_v-v\) has a unique defect \(d\in\{1,2,6\}\).

## Proved structural package

### 1. There is only one \(v\)-lobe

\[
                              C_v-v=R.
\]

Every component of \(C_v-v\) contains a neighbour of \(v\).  All such
neighbours outside \(S\) lie in \(\{3,4\}-S\), and the two possible
vertices are adjacent by the Moser edge \(34\).  Hence they belong to
one component and no other component exists.

### 2. The defect is an exact portal swap

Put \(U=S-\{d\}\).  Then

\[
\begin{aligned}
 N(R)&=U\cup\{v\},\\
 N(D)&=U\cup\{d\},\\
 E(R,D)&=E(v,D)=E(d,R)=\varnothing,
\end{aligned}
\]

and \(vd\in E(G)\).  Thus \(U\cup\{v\}\) and \(U\cup\{d\}\) are the two
exact seven-cuts obtained by exchanging the unique portal \(v\) with
\(d\).  Contracting \(vd\) to \(p\) leaves the exact seven-cut
\(U\cup\{p\}\), with the same two full shores \(R,D\).

Moreover \(\chi(G/vd)=6\).  In every six-colouring of \(G/vd\), either

* \(U\cup\{p\}\) has an exact one-pair trace; or
* every missing-colour split chain crosses the fixed
  \(\alpha\)-gate
  \[
                    U_\alpha\subseteq\{y,z\},\qquad
                    1\le |U_\alpha|\le2.
  \]

This is an operation-level state, not a quotient contact count.

### 3. The row converges to the sole-exterior Moser cell

Using the installed exterior-component results, three exterior
components give a \(K_7\)-model (a Moser triangle, three anchored full
components, and \(\{v\}\)), and the exact two-exterior pure-Moser case
is excluded by supported-pair transfer.  Hence \(G-N[v]\) is connected.
In the placement \(\{y,z\}=\{3,4\}\), the portal swap is precisely the
singleton apex shore versus the sole exterior component.  In all other
placements it is another exact operation inside that same connected
sole-exterior geometry.

The singleton apex shore accepts normalized states but has no
two-packet.  Therefore packet/state transfer cannot be reversed across
it.

### 4. A common two-edge operation gives a coupled Kempe exchange

Choose \(l\in\{3,4\}\) with \(dl\notin E(G)\), contract the connected
star \(\{v,d,l\}\), and expand a six-colouring to
\(G-\{vd,vl\}\).  The three vertices \(v,d,l\) have one colour
\(\alpha\); the five roots
\[
                       X=N(v)-\{d,l\}
\]
have the other five colours once each.

For a root colour \(\beta\), let \(T_\beta\) be the
\(\alpha/\beta\)-component containing \(v\), and put
\[
                       O_\beta=T_\beta\cap\{d,l\}.
\]
Then \(O_\beta\ne\varnothing\) for all five colours.

If \(O_\beta=\{d\}\) and \(O_\gamma=\{l\}\), the off-root components at
\(l\) and \(d\) must either share an \(\alpha\)-vertex or have a
\(\beta\)-to-\(\gamma\) edge.  Otherwise two simultaneous Kempe
switches repair both deleted star edges and six-colour \(G\).  The
forced intersection/cross-edge gives a \(d\)-\(l\) connector supported
by two specified off-root components and avoiding all five roots.

The bare existence of a root-avoiding connector also follows from
seven-connectivity.  The new content is its exact two-colour support.

### 5. Unanimous ownership is impossible

There is always a unique root adjacent to both repeated vertices:
\[
 u=h\quad(d=1,2),\qquad u=5\quad(d=6).
\]
The literal paths \(vud,vul\) imply
\[
                            O_{c(u)}=\{d,l\}.
\]
Thus the coupled state has only two possible structural outcomes:

1. a connector supported by the named Kempe components/cross-edge; or
2. the named root \(u\) is a \(d\)-\(l\) cutvertex inside
   \(T_{c(u)}-v\).

For \(d=6\), the literal Moser edges sharpen this further.  The roots
\(1,2,5\) are \(6\)-owned and \(h,m,5\) are \(l\)-owned, where
\(\{l,m\}=\{3,4\}\).  If no opposite-singleton exchange occurs, at
least three distinct root-colour components are bi-owned; absent an
internal bypass, their three roots are three specified bichromatic
bottlenecks.

## Exact live interface

These results do **not** close the central row or \(HC_7\).  The
remaining assertion is simultaneous, not existential:

> Convert the supported connector into a rooted \(K_5\) certificate
> disjoint from it, or convert the named root bottleneck(s) into an
> exact two-shore adhesion whose state transfers in the valid
> direction.

Kriesell--Mohr packages the unreserved five-root missing graph (a
\(C_5\) for \(d=1,2\), a connected unicyclic graph for \(d=6\)), but
its construction does not preserve a separately chosen connector.
Conversely, a root bottleneck in one bichromatic component is not yet a
global cut.  Promoting either object without silently assuming
disjointness or reversing packet transfer is the exact remaining
portal/web-exchange gap.

## Palette-reserved refinement

The arbitrary model/path formulation reduces further.  Let \(u\) be
the unique root adjacent to both repeated vertices \(d,l\), and let
\(T\) be their common \(c(d)/c(u)\)-component.  If \(T-u\) contains a
\(d\)-\(l\) path \(P\), then \(P\) uses only the repeated colour and
\(c(u)\).  Hence every missing-root Kempe connection not incident with
\(u\) is automatically disjoint from \(P\).

It follows that either the rooted \(K_5\) can be rerun in \(H-P\), or
\(P\) blocks a missing edge incident with \(u\).  There are only two
such demands when \(d=1,2\), and three when \(d=6\).  Every resulting
minimal blocker is an independent set of \(c(u)\)-coloured vertices on
\(P\).  The proof and the sharp
\(K_2\vee\overline{C_8}\) counterarchitecture to promoting this
component blocker by connectivity alone are in
hadwiger_palette_reserved_common_root_packaging.md.

More precisely, after reserving such a path \(P\), the other four root
colours always give a rooted \(K_4\) in \(H-P\).  If the component
containing \(u\) sees all four bags, these six objects give \(K_7\).
Otherwise its neighbourhood \(W\) lies on \(P\) and at most three
rooted bags, with \(|W|\ge6\).  Equality makes
\(W\cup\{v\}\) an exact seven-cut; strict inequality forces a third
portal on \(P\) or a double hit in one rooted bag.  Every edge of \(P\)
is additionally state-essential: deleting it unlocks a genuinely new
at-most-five-block state on \(N(v)\).  Thus the surviving object is an
operation-critical surplus web, not an arbitrary bridge web.

This surplus web now has an exact order invariant.  If \(f_j,\ell_j\)
are the first and last contacts of rooted bag \(Q_j\) along \(P\), and
\(A\) is the set of rooted bags contacted directly by the \(u\)-side
component, either

\[
 \max_{j\notin A}f_j<\min_j\ell_j
 \quad\text{or}\quad
 \max_jf_j<\min_{j\notin A}\ell_j
\]

gives an explicit connector-edge peel and hence \(K_7\).  Every survivor
obeys both reversed inequalities.  In the one-missed-bag row this places
the missed bag's portal interval between an early-ending and a
late-starting rooted bag.  A clean edge-critical detour which adds portals
across either threshold breaks the lock and closes the row.  Thus the
remaining operation-level object is a three-bag ordered first-hit web.
