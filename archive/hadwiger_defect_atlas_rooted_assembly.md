# From a bad-split atlas to rooted portal assembly

## 1. A rooted-connectivity parameter

For \(m\ge1\), let \(\rho(m)\) denote any connectivity threshold with the
following property:

> every \(\rho(m)\)-connected graph contains a \(K_m\)-model rooted at
> any prescribed \(m\) distinct vertices.

Only values for which such a theorem has been supplied are to be used.
For the application below, \(\rho(3)=2\): every two-connected graph has
a rooted triangle at any three prescribed vertices.  The notation does
not assume an optimally small threshold for general \(m\).

## 2. Thin portal classes

Use the notation \(\mathcal B_k(J),\beta_k(J)\), and \(\Lambda_1(J)\)
from hadwiger_defect_atlas_connectivity_principle.md.

### Theorem 2.1 (rooted assembly criterion)

Let \(G\) be a \(\lambda\)-connected \(K_k\)-minor-free graph.  Let
\(|S|=k\), \(J=G[S]\), and suppose \(G-S\) has two connected full shores
\(D_1,D_2\).  Put

\[
 q=\beta_k(J),\qquad r=\lambda-q.                   \tag{2.1}
\]

Assume:

1. neither shore is a singleton;
2. \(S\) has a partition
   \[
   S=U\mathbin{\dot\cup}T_1\mathbin{\dot\cup}T_2
   \]
   such that \(J[U]\) is complete and every two vertices in different
   members of \(\{U,T_1,T_2\}\) are adjacent;
3. every \(L\in\Lambda_1(J)\) satisfies
   \[
   |L\cap T_1|\le1,\qquad |L\cap T_2|\le1;           \tag{2.2}
   \]
4. \(r\ge\rho(|T_1|)\) and \(r\ge\rho(|T_2|)\).

Then \(G\) contains a \(K_k\)-minor.

### Proof

The defect-atlas connectivity theorem makes each shore internally
\(r\)-connected, apart from the standard complete-small-graph
convention.  A complete exceptional shore also has every rooted clique
model whose number of roots does not exceed its order.  Fullness and
(2.2) will supply \(|T_i|\) distinct vertices in the relevant shore, so
the exception causes no problem.

Fix \(i\in\{1,2\}\).  For each \(t\in T_i\), choose a portal
\(x_t\in N_{D_i}(t)\).  The shore has no cutvertex (unless it is complete),
so \(D_i-x\) is connected for every \(x\in D_i\).  The portal-locality
theorem with parameter one gives

\[
 N_S(x)\in\Lambda_1(J).                              \tag{2.3}
\]

Condition (2.2) shows that one vertex of \(D_i\) cannot be selected for
two distinct terminals of \(T_i\).  Thus the vertices \(x_t\) are
distinct.  By (2.1), condition 4, and the definition of \(\rho\), the
shore \(D_i\) contains a \(K_{|T_i|}\)-model rooted at these vertices.
Adjoin each boundary terminal \(t\) to the branch set rooted at \(x_t\).
This gives a \(T_i\)-rooted clique model in \(G[D_i\cup T_i]\).

Take the \(T_1\)-rooted bags in \(D_1\), the \(T_2\)-rooted bags in
\(D_2\), and the singleton bags \(\{u\}\) for \(u\in U\).  Bags within
either rooted family are adjacent by construction.  Every two bags from
different families are adjacent through their boundary roots by
condition 2, and the singleton \(U\)-bags form a clique.  There are

\[
 |T_1|+|T_2|+|U|=|S|=k
\]

pairwise adjacent disjoint connected bags, a \(K_k\)-model.

## 3. Exact interpretation of the two seven-boundary cores

For the \(2K_3\dot\cup K_1\) missing-edge graph, take

\[
 T_1=A,\qquad T_2=B,\qquad U=\{c\}.
\]

The maximal bad pairs have a cross-triangle side, so
\(\beta_7(J)=3\), \(r=7-3=4\), and \(\Lambda_1(J)\) consists of subsets
meeting either independent triple at most once.  Since
\(\rho(3)=2\), Theorem 2.1 gives exactly the rooted-triangle proof of the
full closure.

For the \(C_6\dot\cup K_1\) missing-edge graph, two independent
hypotheses fail in a controlled way:

1. balanced \(5\mid5\) bad contact pairs make
   \(\beta_7(J)=5\), so the atlas yields only two-connectivity;
2. the natural two boundary triangles of \(J\) are not completely joined:
   only the three antipodal matching edges run between them.

The first failure is the cyclic balanced transition core isolated in
hadwiger_defect_star_principle.md.  The second says that the shore models
must repair an oriented set of cross-nonedges rather than merely package
two independent terminal triples.  Thus \(C_6\dot\cup K_1\) does not
refute the abstract mechanism: it identifies the exact additional
chain/web assembly lemma needed beyond Theorem 2.1.
