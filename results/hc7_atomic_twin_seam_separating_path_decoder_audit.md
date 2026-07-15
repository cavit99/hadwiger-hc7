# Audit: separating twin-seam literal first-exit decoder

**Verdict:** GREEN for Lemmas 2.1 and 3.1 at the frozen source hash below.
The four excursion outcomes are exhaustive, direct edges and repeated
portal visits are handled correctly, the connector--`P_D` intersection
bounds are literal, and the matched common-duty packet construction is
valid.  Neither lemma proves the separating-edge branch of the double-lock
exchange theorem.

**Audited source:**
`results/hc7_atomic_twin_seam_separating_path_decoder.md`.

**Source SHA-256:**
`19c6f641640c9db65caf4ec74ed170a7eb1cb4887156c5376087d70ecefc51d6`.

## 1. Set audit

The displayed shore identities are consistent.  From

\[
A=D\mathbin{\dot\cup}E\mathbin{\dot\cup}Z,
\qquad
S=I\mathbin{\dot\cup}A_0\mathbin{\dot\cup}B_0,
\]

and \(\Omega_E=Z\mathbin{\dot\cup}I\mathbin{\dot\cup}B_0\), one obtains

\[
V(G)-(E\cup\Omega_E)
=D\mathbin{\dot\cup}A_0\mathbin{\dot\cup}R=B_E.
\]

Likewise

\[
\Omega_D\cap\Omega_E
=(Z\mathbin{\dot\cup}I)=K.
\]

Thus every region used in the decoder is literally disjoint where the
proof says it is.  The uses of \(N_G(D)=\Omega_D\), the absence of an
\(A\)-\(R\) edge, and \(N_S(Z)\subseteq I\) all match the frozen
separating-gate normal form.

## 2. Lemma 2.1: complete excursion accounting

Orient \(P_E\) from \(t\) to \(r_E\).  Since the path contains
\(f=dt\) and \(t\) is its endpoint, its first edge is \(td\).  After
deleting \(t\), it therefore begins at \(d\in D\), ends at
\(r_E\in\Omega_E\), and all non-end vertices lie in
\(B_E=D\mathbin{\dot\cup}A_0\mathbin{\dot\cup}R\).

If every internal vertex of \(P_E\) is in \(D\), its final edge gives
\(r_E\in N_G(D)=\Omega_D\), hence
\(r_E\in\Omega_D\cap\Omega_E=K\).  The same path is then a legitimate
\(D\)-closed mismatch path.  This includes the endpoint-only exit from
\(D\): the last vertex of \(D\) may be adjacent directly to \(r_E\).

Now decompose the vertices outside \(D\) into maximal excursions along the
simple path.  Every excursion begins at an \(A_0\) vertex: its predecessor
is in \(D\), and a `D-R` edge is forbidden.

If a final excursion does not return to \(D\), choose its last \(A_0\)
vertex \(a\).  No later internal vertex can lie in \(A_0\), and the region
identity leaves only \(R\); hence the suffix from \(a\) to \(r_E\) has all
internal vertices in \(R\).  This is outcome 2.

Suppose every excursion returns.  In the last excursion, let \(a,a'\) be
the first and last \(A_0\) vertices.  If \(a\ne a'\), simplicity and
\(|A_0|=2\) exclude any further \(A_0\) vertex from the subpath; all its
internal vertices therefore lie in \(R\).  This is outcome 3, including
the direct edge \(aa'\), whose interior is empty.  If \(a=a'\), the first
and last portal are the same occurrence on the simple path.  The excursion
can contain no other vertex: any return from \(R\) to \(D\) would require
another \(A_0\) occurrence, making the last portal distinct.  Thus the
excursion is exactly `x-a-y` with \(x,y\in D\), which is outcome 4.

After the last returning excursion the path stays in \(D\) until its
endpoint.  The final edge and `N_G(D)=Omega_D` put that endpoint in
`Omega_D cap Omega_E=K`.

This also checks all combinations of excursions.  With no excursion one
has outcome 1.  Any nonreturning last excursion gives outcome 2, even if a
singleton returning excursion occurred earlier.  If all excursions return,
their last member has distinct portals and gives outcome 3, or one portal
and gives outcome 4.  A simple path visits each of the two `A_0` literals
at most once, so there is no fifth pattern.

For the final-excursion branch, the exclusion \(r_E\notin Z\) covers both
endpoint cases:

* with a nonempty interior, the final edge would be an \(R\)-\(Z\) edge,
  forbidden by the absence of \(A\)-\(R\) edges;
* with empty interior, \(ar_E\) would contradict
  \(N_S(Z)\subseteq I\), since \(a\in A_0\).

Hence \(r_E\in I\cup B_0\).  As a subpath of the original lock, \(J\)
retains the named two-colour property.  If \(r_E\in B_0\), neither the
collapsed nor the closed-excursion endpoint case is possible because
\(B_0\cap K=\varnothing\).

Direct edges cause no defect.  In the final branch, `J=ar_E` with
empty interior is allowed when \(r_E\in I\cup B_0\).  In the two-portal
closed branch, `J=aa'` with empty interior is allowed when the literal edge
exists.  A one-vertex returning excursion is precisely outcome 4.

## 3. Disjointness audit

Conditional on obtaining either displayed connector, the claimed
intersection bound is exact.  The internal vertices of \(P_D\) lie in
\(D\), while those of \(J\) lie in \(R\).  The only vertices of `P_D`
outside \(D\) are \(t,r_D\), and the endpoints of \(J\) lie in the old
boundary and do not include \(t\).

For the final connector, the only possible common vertex is therefore
\(r_D=a\) or \(r_D=r_E\).  These alternatives cannot occur simultaneously
because \(A_0\cap(I\cup B_0)=\varnothing\).  For the two-portal closed
connector, its endpoints are the two distinct members of \(A_0\), while
`P_D` has only the one non-`t` boundary endpoint \(r_D\).  Again the
intersection has order at most one.  In both cases any common vertex is an
endpoint of both paths.

Outcome 4 makes no connector-intersection claim.  Treating its singleton
\(\{a\}\) as a path would preserve a numerical intersection bound but
would not produce a connector between two literal duties, and the source
does not do so.

No stronger disjointness is proved: in the collapsed case \(P_D\) and
\(P_E\) may coincide.

## 4. Lemma 3.1: packet construction audit

For alleged disjoint connected \(X_1,X_2\subseteq D\), set

\[
Y_i=X_i\cup\{a_i\}\cup R_i.
\]

The three regions \(D,A_0,R\) are pairwise disjoint; the \(X_i\), the
vertices \(a_i\), and the old packets \(R_i\) are pairwise disjoint within
their respective regions.  Hence \(Y_1,Y_2\) are disjoint and lie in
\(B_E\).

Each \(Y_i\) is connected: one assumed edge joins \(X_i\) to \(a_i\), and
the \(S\)-full packet \(R_i\) has a neighbour of the literal boundary
vertex \(a_i\).  Each \(X_i\) contacts every vertex of \(K\), while each
\(R_i\) contacts both vertices of \(B_0\).  Therefore each \(Y_i\) is
\(\Omega_E=K\mathbin{\dot\cup}B_0\)-full.  This gives two disjoint full
packets in \(B_E\), contradicting \(\nu_{B_E}^{\Omega_E}=1\).  The stated
symmetric substitution is literal and valid.

## 5. Exact audited scope

The source proves the following exhaustive local facts:

1. a final excursion produces a label-faithful
   \(A_0\)-to-\(I\cup B_0\) connector with interior in \(R\);
2. a returning excursion using both \(A_0\) vertices produces the stated
   closed connector with interior in \(R\);
3. all-in-\(D\) paths end in \(K\), while a path whose last returning
   excursion is one \(A_0\) vertex has the explicit singleton-detour
   outcome and also ends in \(K\); and
4. two disjoint, matched \(K\)-full subgraphs in \(D\) are impossible when
   \(\nu_{B_E}^{\Omega_E}=1\).

It does **not** manufacture those two \(K\)-full subgraphs, allocate the
five literal duties of \(K\), force a second carrier, produce a fixed pair,
or close the bridge/bypass exchange.  The remaining allocation implication
in the source stays open exactly as stated.
