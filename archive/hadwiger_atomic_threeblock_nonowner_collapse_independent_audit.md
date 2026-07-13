# Independent audit: arbitrary-shore three-block ownership

## Verdict

**GREEN.** Theorem 1.2 of
hadwiger_atomic_threeblock_nonowner_collapse.md is correct under its
stated hypotheses. Its application to an accepted normalized Moser mode
is also correct, provided the apex \(v\) is retained as the carrier for
the third pair block. No transfer direction is reversed.

## 1. Degree-seven exit

Let \(C\) be a full component behind the seven-cut \(S\), of order at
least two, and let another component be the far shore. If
\(d_G(x)=7\) for \(x\in C\), then \(N_G(x)\) is genuinely a
seven-cut:

* \(x\) is isolated in \(G-N_G(x)\);
* the far shore is anticomplete to \(C\), hence disjoint from
  \(N_G(x)\), and remains nonempty.

Thus \(\{x\}\) is a proper fragment of \(C\). If no such exact-cut
exit occurs, every vertex of \(C\) has degree at least eight.

## 2. Singleton carriers and the boundary-degree bound

Assume \(C\) has no two-block capacity for

\[
 S=A\dot\cup B\dot\cup C_0\dot\cup\{r\},
 \qquad |A|=|B|=|C_0|=2.
\]

If one shore vertex sees both roots of a pair block, that vertex is a
singleton carrier. Since the shore has another vertex, the uniform
small-carrier theorem applies with \(p=3\) and
\(|X|=1<p-1\). Its packet outcome is forced; there is no exact-cut
alternative at this strict inequality. This contradicts nonownership.

Consequently a shore vertex sees at most one root in each pair block,
and possibly \(r\), for at most four boundary neighbours. In the
no-degree-seven branch,

\[
 d_C(x)\ge 8-4=4.                                \tag{2.1}
\]

This is a count of actual boundary neighbours, not merely colour
classes, so no multiplicity assumption is hidden.

## 3. Orders five and six

For \(|C|\le4\), (2.1) is impossible.

If \(|C|=5\), then \(C=K_5\). The two portal sets of any one pair
block are disjoint, since an intersection would be a singleton
carrier. Choose one representative from each set. Their edge in
\(K_5\) is a connected carrier of order two with nonempty complement.
The small-carrier theorem gives either a packet or a proper exact
seven-cut. Nonownership excludes the packet, leaving the theorem's
exact-cut conclusion.

If \(|C|=6\), the six portal sets belonging to the three pair blocks
have an SDR. The relative Hall lemma applies with \(h=6\): its small
alternative would say \(|C|\le5\). Equation (2.1) makes
\(\overline C\) a matching. For any two demanded pairs:

* use their two edges when present;
* route one absent edge through one unused representative; or
* route two absent edges through the two unused representatives.

Because missing edges of \(C\) form a matching, each unused
representative is adjacent to both ends of an absent demanded edge.
The resulting paths are vertex-disjoint and give a forbidden packet.

## 4. Set-terminal webs and curvature

Let \(|C|\ge7\), and assume neither capacity nor a proper exact
seven-cut exists.

The separator-capacity theorem with \(q=3\) eliminates a cutvertex and
turns every two-separator into the exact-cut outcome. Hence \(C\) is
three-connected.

The three packet failures now satisfy every hypothesis of the
set-terminal synchronization theorem:

* all portal sets are full portal sets, not selected representatives;
* another component lies beyond \(S\);
* \(G\) is seven-connected;
* \(C\) is three-connected and has order at least seven.

The exact-cut outcome is one of the desired conclusions. Otherwise the
same plane embedding has one face containing all six full portal sets
of the pair roots.

Choose that face as the outer face and triangulate every bounded face.
An interior vertex is in none of the six portal sets, so among boundary
labels it can see only \(r\). Its shore degree is therefore at least
seven. An outer vertex still obeys (2.1), so its shore degree is at
least four. Triangulation only increases degrees. The disk identity

\[
 \sum_{\operatorname{int}}(6-d_T(x))
 +\sum_{\partial}(4-d_T(x))=6
\]

then has a nonpositive left side, a contradiction. The curvature step
does not assume that all shore vertices lie on the portal face; it
handles off-face vertices through the stronger interior degree bound.

## 5. Application to an accepted normalized state

Suppose an operated exterior shore \(D\) creates a normalized mode
\(\Pi=A|B|C_0|\{r\}\) which is accepted by another full exterior
shore \(C\) but not by the original \(D\).

If \(C\) had a packet for two pair blocks, enlarge its two carriers
along a shortest connector so they are adjacent. Use the apex
singleton \(\{v\}\), which is complete to \(S=N(v)\), as a carrier
for the third pair block. Contract the three block carriers together
with their roots and retain the singleton block and \(D\).

The four block images form a clique because \(\Pi\) is an optimal
four-colouring of the four-chromatic Moser boundary. A six-colouring
of this proper minor expands to an extension of \(\Pi\) over \(D\),
contradicting its nonextension there. Therefore the accepting shore is
a nonowner, and Theorem 1.2 gives a proper exact seven-adhesion whenever
\(|C|\ge2\).

If \(|C|=1\), its vertex and \(v\) are nonadjacent false twins with
open neighbourhood \(S\). Deleting the exterior singleton, six-colouring
the proper minor, and copying the colour of \(v\) back to it would
six-colour \(G\). Thus the singleton case is impossible.

## 6. Scope

The theorem closes the **ownership-direction** gap for a normalized
four-block state. It does not produce the normalized state; that still
comes from an exact-trace minor operation and Kempe normalization. If
normalization instead yields an exterior support path, absorbing that
path into the target clique model remains a separate geometric step.
