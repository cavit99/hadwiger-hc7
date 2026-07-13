# When protected-web absorption applies to the sole-exterior Moser model

## 1. The dirty rooted model

Use the sole-exterior pure-Moser notation

\[
 I=\{1,3\},\qquad U=\{0,2,4,5,6\}.
\]

The present edges on \(U\) form a \(5\)-cycle and the missing edges form
its complementary \(5\)-cycle. Let

\[
                         (B_u:u\in U)
\tag{1.1}
\]

be a rooted \(K_5\)-model in \(G-v\), with \(u\in B_u\), whose bags
avoid \(I\). Let \(P\) be an \(I\)-connector whose internal vertices
lie in the sole exterior and avoid \(U\). Put

\[
                         C=V(P)
\tag{1.2}
\]

and let \(K_u\) be the component of \(B_u-C\) containing \(u\).

### Lemma 1.1 (the connector is universal to the root cores)

The six sets

\[
                         \{v\},C,(K_u:u\in U)
\tag{1.3}
\]

are pairwise disjoint and connected except that no adjacency among the
\(K_u\)'s is asserted beyond the following:

1. both \(\{v\}\) and \(C\) are adjacent to every \(K_u\);
2. \(\{v\}\sim C\); and
3. if \(uw\) is a present edge of the \(5\)-cycle \(G[U]\), then
   \(K_u\sim K_w\).

#### Proof

The roots \(U\) avoid \(P\), so every \(K_u\) is defined. The sets are
disjoint by construction. The old vertex \(v\) sees \(u\), hence
\(K_u\), and sees the ends \(1,3\) of \(P\). Every root in \(U\) is
adjacent in the Moser spindle to at least one of \(1,3\):

\[
 0\sim1,3,\quad2\sim1,\quad4\sim3,\quad
 5\sim3,\quad6\sim1.
\]

Thus \(C\sim K_u\). Finally, a present edge \(uw\) has both ends in the
retained root cores, proving item 3. \(\square\)

The potentially lost root-core adjacencies are therefore exactly the
five missing-cycle adjacencies originally supplied by the Kempe
packaging.

## 2. Conditional protected-web reduction

### Theorem 2.1 (one-dirty-chord mapping)

Assume \(G\) has no \(K_7\)-minor and that the root-core adjacency graph
on \(\{K_u:u\in U\}\) is \(K_5-ab\), for two roots \(a,b\in U\).
Let \(r,s,t\) be the other three roots.

Suppose

\[
 |N_{K_t}(K_a)|\ge2,\qquad |N_{K_t}(K_b)|\ge2.   \tag{2.1}
\]

Let \(W\subseteq K_t\) be a connected set containing \(t\), an endpoint
of a \(K_tK_r\)-edge, and an endpoint of a \(K_tK_s\)-edge. If
\(|W|\ge2\), then Theorems 3.1 and 4.1 of
*hadwiger_general_protected_web_absorption.md* apply literally. In
particular, every component of \(K_t-W\) can be absorbed into its unique
root shore while the gate remains two-connected. The process ends with

1. a non-two-connected gate and the portal-owner lobe normal form; or
2. the gate equal to \(W\).

If \(W\) is chosen as an induced path, only the first outcome occurs.

#### Proof

Use the notation of the general theorem with

\[
\begin{aligned}
 Q_1&=\{v\},&Q_2&=C,&Q_3&=K_r,\\
 C_{\rm gen}&=K_s,&K_{\rm gen}&=K_t,&
 D_0&=K_a,&D_1&=K_b.
\end{aligned}                                      \tag{2.2}
\]

Lemma 1.1 and the assumed \(K_5-ab\) core say that these seven bags form
the required \(K_7^-\)-model, with deficient pair \(K_aK_b\).
The set \(W\) sees \(K_r,K_s\) by its selected edge endpoints, and it
sees \(\{v\},C\) through its root \(t\). Hence it is precisely the
protected core required in the general theorem. Equation (2.1) is its
two-portal hypothesis. All absorptions are therefore label-preserving,
and the conclusions are those of the protected-web and owner-lobe
theorems. The induced-path conclusion is their two-terminal corollary.
\(\square\)

## 3. Exact applicability boundary

Theorem 2.1 shows that the apex is **not** what blocks protected-web
absorption. Once the near-\(K_7\) model exists, \(\{v\}\) and the dirty
connector \(C\) are simply two protected clique bags, and every
label-preserving absorption preserves their adjacencies.

The theorem cannot, however, be invoked from one crossed Moser frame.
A crossed frame supplies only two adjacent carriers. The conservative
crossing quotient has Hadwiger number six, and it supplies neither:

* a \(K_5^-\) adjacency graph on the five surviving root cores; nor
* two distinct portals from one protected gate to each endpoint of its
  sole deficient pair.

Producing those objects is exactly the missing \(w\)-absorber/four-block
portal realization in the reserved-connector formulation. Assuming them
in order to invoke protected-web absorption would therefore be circular.
The valid division of labour is:

\[
\begin{array}{c}
\text{crossed-frame or transition argument}\\
\Downarrow\\
\text{one-dirty-chord near-clique plus (2.1)}\\
\Downarrow\\
\text{protected-web absorption to owner lobes/cutvertices.}
\end{array}
\]

Thus the new all-\(t\) theorem removes every subsequent bridge-order
case, but it does not itself create the first near-clique gate in the
sole-exterior cell.

