# Strongest valid derivation after the Hadwiger search

## Verdict

The search did not produce a proof of Hadwiger's Conjecture.  This note
records the strongest package that survived independent adversarial audit and
states the remaining gaps exactly.  In particular, none of the assertions
below is presented as a proof for all \(t\).

The named external inputs are: Hadwiger's Conjecture for \(t\leq 6\),
Dirac's neighbourhood-independence lemma, Mader's connectivity theorem,
the Mader--Jørgensen--Song--Thomas extremal bounds, the
Kriesell--Mohr property-\((*)\) theorems, the seven-vertex Moser-spindle
lemma, and the Norin--Totschnig theorem excluding \(K_7^\vee\).

## 1. Uniform reduction at the least failing parameter

Suppose the conjecture fails, let \(t\) be the least failing parameter, and
choose a \(K_t\)-minor-free graph \(G\), minimal under the proper-minor
relation, with \(\chi(G)\geq t\).  Let \(v\) be a minimum-degree vertex,
put
\[
  H=G-v,\qquad N=N_G(v),\qquad k=t-1.
\]
Then
\[
 \chi(G)=t,\qquad \eta(G)=t-1,qquad
 \delta(G)\geq t,qquad \kappa(G)\geq7,                 \tag{1}
\]
\[
 \chi(H)=\eta(H)=t-1,qquad \kappa(H)\geq6.             \tag{2}
\]
The 2026 Lafferty--Liu--Rolek--Yu strengthening further gives
\(\kappa(G)\geq8,9,10\) for \(t\geq17,29,41\), respectively (and lowers
these bounds by at most one after deleting \(v\)).

Moreover,
\[
  t\leq |N|=d(v)\leq D_t,
  \quad
  D_t:=\max_n\left\lfloor
  \frac{2\operatorname{ex}_{\rm m}(n,K_t)}{n}
  \right\rfloor.                                       \tag{3}
\]
In particular,
\[
  D_7=9,\qquad D_8=11,\qquad D_9=13,
\]
and
\[
  D_t=(0.63817\ldots+o(1))t\sqrt{\log t}.
\]

Here is the part of the proof that materially sharpens the earlier report.
Every proper \(k\)-colouring of \(H\) uses all \(k\) colours on \(N\), or a
missing colour could be assigned to \(v\).  In fact, **no proper subset of
\(N\) is colour-saturating**.  Fix \(w\in N\), colour the proper minor
\(G/vw\) with \(k\) colours, and call its contracted vertex \(q\).  Restore
\(w\) in \(H\) with the colour of \(q\).  Every
\(x\in N-\{w\}\) is adjacent to \(q\) in \(G/vw\), because \(vx\) was an
edge.  Thus \(w\) is the unique vertex of \(N\) with that colour.  Hence
\(N-\{w\}\), and therefore every proper subset of \(N\), fails to be
saturating.

Finally, there is no \(K_k\)-model in \(H\) all of whose bags meet \(N\):
adding the singleton bag \(\{v\}\) would give a \(K_t\)-model in \(G\).

The remaining uniform implication is therefore precisely
\[
 \boxed{\begin{gathered}
 \text{Prove that every counterexample-derived }(G,v,H,N)\text{ satisfying
 (1)--(3),}\\
 \text{full-neighbourhood minimal saturation, and the contraction-colouring
 witnesses}\\
 \text{has an }N\text{-meeting }K_{t-1}\text{-model in }H.
 \end{gathered}}                                                     \tag{U}
\]
No audited argument proves (U).

## 2. Corrected contact-model extremality for \(t=7\)

For a hypothetical minor-minimal counterexample to \(\mathrm{HC}_7\), fix
\(v\) and a \(K_6\)-model
\(\mathcal B=(B_1,\ldots,B_6)\) in \(G-v\).  Let \(s\) be the number of
bags meeting \(N(v)\), let \(Z\) be the unused vertices, and let \(C\) be
the union of the noncontact bags.  Let \(\mu\) be the maximum number of
internally disjoint \(v\)-to-\(C\) paths, allowing a common endpoint in
\(C\), and let \(\ell\) be the minimum total length of a maximum such
family.  Maximise lexicographically
\[
 \Psi(\mathcal B)=
 \left(s,-|Z|,\mu,-\ell,-\sum_i|B_i|^2\right).           \tag{4}
\]

Then the selected model is spanning, and a length-minimum maximum path
family has only rigid portals.  Indeed, moving a direct removable portal
into its first noncontact bag raises \(s\).  Moving a non-direct removable
portal \(\alpha\) preserves \(s,Z\), changes \(C\) to
\(C\cup\{\alpha\}\), and permits its path to be shortened by one edge.
Thus either \(\mu\) rises or \(\ell\) falls, contradicting (4).
Seven-connectivity, applied between \(v\) and any fixed vertex of \(C\),
gives at least seven distinct portals.

This proves the existence of **one** extremal model and **one** all-rigid
path family.  It does not imply that every maximum fan is rigid, and it does
not validate the old \(s=1\), \(s=2\), or \(R_5\) closures.

## 3. The degree-seven cell

Now assume \(d(v)=7\), put \(S=N(v)\), and fix a proper six-colouring of
\(H=G-v\).  Exactly one colour is repeated on two nonadjacent vertices
\(a,b\in S\); the other five colours occur uniquely on a set
\(U=\{u_1,\ldots,u_5\}\).

### Rooted \(K_5\) theorem

Every two vertices of \(U\) are in the same bichromatic component.  If not,
swapping their two colours on the component containing one root removes its
unique colour from \(S\), contrary to saturation.

Let
\[
  F=\overline{H[U]}.
\]
Dirac's inequality gives \(\alpha(G[S])\leq2\), so \(F\) is triangle-free
and hence has at most six edges.  Kriesell--Mohr's Theorem 7 says that every
five-vertex graph with at most six edges has property \((*)\).  Applied to
the five unique colour classes, it gives disjoint connected bags rooted at
\(U\), adjacent for all edges of \(F\).  For every nonedge of \(F\), the
two roots are adjacent in \(H[U]\), supplying the remaining bag adjacency.
Thus:
\[
 \boxed{\text{the five uniquely coloured neighbours always root a
 }K_5\text{-model in }H.}                                \tag{5}
\]
The bags can be chosen using only the five unique colour classes, so they
avoid \(a,b\).

If \(a,b\) lie in one component of the complement of those five bags, that
component is a sixth bag.  It is adjacent to every rooted bag because, for
each \(u_i\), at least one of \(au_i,bu_i\) is an edge; otherwise
\(\{a,b,u_i\}\) would be independent in \(G[S]\).  This would give an
\(S\)-meeting \(K_6\)-model and then a \(K_7\)-minor with \(\{v\}\).

Consequently the exact degree-seven obstruction is
\[
 \boxed{\text{every rooted }K_5\text{-model furnished by (5) separates
 the repeated pair }a,b.}                                \tag{D7}
\]
Six-connectivity does not contradict (D7), because the separator is the
union of five possibly large bags, not five vertices.

### Exterior components

Every component \(C\) of \(G-N[v]\) has \(N_G(C)=S\); otherwise at most
six vertices separate \(C\) from \(v\).  There are one or two such
components.  Three components, together with a triangle in \(G[S]\), give
three singleton bags and three component-helper bags, hence an
\(S\)-meeting \(K_6\).  If there are two components, a \(K_4\)-model in
\(G[S]\) supported on at most five vertices gives the same conclusion.

Using the seven-vertex Moser-spindle lemma, the only local neighbourhoods
not eliminated in the two-component case are the Moser spindle and its
one-cross-edge extension.  This remains only a local reduction.  Every
exterior component must intersect every model in (5); otherwise
\(C\cup\{a,b\}\) is the required sixth bag.  Proving an avoided component,
or splitting a used component without overlapping the five bags, is the
precise missing operation.

## 4. Near-\(K_7\) normalization

Norin--Totschnig prove that every non-six-colourable graph contains
\(K_7^\vee\) as a minor, where the two missing edges have a common endpoint.
Thus a hypothetical \(\mathrm{HC}_7\) counterexample contains such a model.

Write its deficient bag as \(A\), the two bags not required to meet it as
\(B,C\), and the other four bags as \(D_1,\ldots,D_4\).  An outside
component that meets \(A,B,C\) can be absorbed into \(A\), repairing both
missing adjacencies and producing \(K_7\).  After making the model spanning,
one obtains the following exact dichotomy:

* if a \(K_7^-\)-minor exists, the deficient bag has at least seven
  attachment vertices distributed among five other bags;
* if no \(K_7^-\)-minor exists, both deficient pairs in a spanning
  \(K_7^\vee\)-model are genuinely anticomplete, and the deficient bag has
  at least seven attachment vertices distributed among only the four
  \(D_i\).

Hence some unaffected bag is multiply hit.  The missing theorem is a
branch-set splitting or avoidance lemma that uses those attachments while
preserving every other clique-model adjacency.  Absorbing a whole component
without proving disjointness is invalid because the existing Kempe bags may
already occupy that component.

## 5. Exact endpoint

No complete affirmative proof survived audit.  The strongest endpoints are
the uniform obstruction (U), the degree-seven nonseparating-rooted-\(K_5\)
gap (D7), and the corresponding \(t=7\) near-clique bag-splitting
obstruction.
The old claimed eliminations of contact loads \(s=1,2,5\) cannot be used:
they rely on a reversed quadratic-potential inequality, an invalid
singleton descent, and an unjustified change from “no all-clean fan” to
“every portal is rigid.”
