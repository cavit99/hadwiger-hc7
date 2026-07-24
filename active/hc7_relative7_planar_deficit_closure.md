# Planar-deficit closure of the sharp relative-seven quotients

**Status:** active draft with a
[separate GREEN internal audit](hc7_relative7_planar_deficit_closure_audit.md).
Section 3 is a computer-assisted finite classification with a checked-in
certificate catalogue and an independent completeness-and-certificate
checker. This note does not assert that every live order-eight configuration
reduces to the quotient family below.

## 1. A protected-triangle host lemma

### Lemma 1.1

Let \(G\) be a finite simple seven-connected graph with no \(K_7\) minor.
Let \(\Delta=\{t_1,t_2,t_3\}\) induce a triangle, put \(H=G-\Delta\), and
let \(q_1,q_2,q_3,q_4\) be four distinct vertices of \(H\), each adjacent
to every vertex of \(\Delta\).

Suppose that \(V(H)=D\mathbin{\dot\cup}Y\), where

\[
 |N_G(d)\cap\Delta|\leq 1\qquad(d\in D)
 \tag{1.1}
\]

and

\[
 \sum_{y\in Y}\bigl(|N_G(y)\cap\Delta|-1\bigr)\leq 11.
 \tag{1.2}
\]

Then these hypotheses are inconsistent.

### Proof

Deleting three vertices from a seven-connected graph leaves a
four-connected graph, so \(H\) is four-connected. Apply Theorem 6 of
Fabila-Monroy and Wood to \(H\), nominated at
\(q_1,q_2,q_3,q_4\).

If \(H\) has a \(K_4\)-minor rooted at those vertices, append the three
singleton branch sets

\[
 \{t_1\},\quad \{t_2\},\quad \{t_3\}.
\]

They are pairwise adjacent, and each is adjacent to every rooted branch
set through its nominated vertex. This is a \(K_7\)-minor model in \(G\),
a contradiction.

The other outcome of the rooted-\(K_4\) theorem makes \(H\) planar.
Seven-connectivity gives \(\delta(G)\geq 7\), so every \(x\in V(H)\)
satisfies

\[
 d_H(x)=d_G(x)-|N_G(x)\cap\Delta|
 \geq 7-|N_G(x)\cap\Delta|.
 \tag{1.3}
\]

For \(d\in D\), (1.1) gives \(d_H(d)\geq 6\). Therefore

\[
 \sum_{x\in V(H)}(6-d_H(x))
 \leq
 \sum_{y\in Y}\bigl(|N_G(y)\cap\Delta|-1\bigr)
 \leq 11.
 \tag{1.4}
\]

But Euler's inequality for the simple planar graph \(H\) gives

\[
 \sum_{x\in V(H)}(6-d_H(x))
 =6|V(H)|-2|E(H)|\geq 12,
 \tag{1.5}
\]

a contradiction. \(\square\)

The external input is R. Fabila-Monroy and D. R. Wood,
[*Rooted \(K_4\)-Minors*](https://doi.org/10.37236/3476),
*Electronic Journal of Combinatorics* 20(2) (2013), P64, Theorem 6:
four nominated vertices in a four-connected graph root a \(K_4\)-minor
unless the graph is planar and the four vertices lie on one face.

## 2. The quotient family

Let

\[
 R=K_7-\{01,23,45\}
\]

on vertices \(0,\ldots,6\). For subsets \(A,B,U\subseteq V(R)\), form
\(J(A,B,U)\) by adding vertices \(z,p,v\), making \(z,p,v\) a triangle,
and setting

\[
 N_R(p)=A,\qquad N_R(v)=B,\qquad N_R(z)=U.
\]

Each of \(A,B,U\) is restricted to contain \(6\) and at least one endpoint
of each of \(01,23,45\). These are exactly the 27 subsets meeting every
colour class in every four-colouring of \(R\).

Call \(J(A,B,U)\) **relatively seven-connected at \(z\)** when deleting
any set of at most six vertices not containing \(z\) leaves it connected.
This is the exact ordinary-connectivity condition inherited when \(z\)
is the contraction of a connected subgraph in a seven-connected host.

## 3. Exact finite classification

### Proposition 3.1 (computer-assisted)

Among all \(27^3\) ordered triples \((A,B,U)\), exactly 48 satisfy all of
the following:

1. \(R\) has no \(K_4\)-minor model in which every branch set meets all
   three of \(A,B,U\);
2. \(J(A,B,U)\) is relatively seven-connected at \(z\).

All 48 have chromatic number six. Exactly 24 contain a \(K_7\) minor.
The other 24 have no \(K_7\) minor, and they are precisely the triples
with this form:

- \(A\) and \(B\) contain \(6\) and exactly one endpoint of each of
  \(01,23,45\);
- \(A\) and \(B\) agree on exactly two of those pairs and choose opposite
  endpoints on the third pair; and
- \(U\) consists of \(6\), the unselected endpoint from each agreement
  pair, and both endpoints of the disagreement pair.

The exhaustive verifier generates the finite universe, connected
rooted-minor models, cuts, colourings, and \(K_7\)-minor models. The
checked-in catalogue retains an explicit seven-branch-set \(K_7\)-minor
model for each direct case and the protected-triangle certificate for each
hard case. The separate checker regenerates the exact 48-instance survivor
universe without importing the verifier, checks catalogue completeness, and
checks branch-set nonemptiness, disjointness, connectivity, and all 21
adjacencies in each retained \(K_7\)-minor model:
[`hc7_relative7_planar_deficit_catalogue.json`](hc7_relative7_planar_deficit_catalogue.json).

Run:

```text
python3 active/hc7_relative7_planar_deficit_verify.py
python3 active/hc7_relative7_planar_deficit_certificate_check.py
```

## 4. Literal expansion of every hard quotient

### Theorem 4.1

Let \((A,B,U)\) be one of the 24 hard triples in Proposition 3.1. There
is no seven-connected \(K_7\)-minor-free graph \(G\) obtained by replacing
\(z\) in \(J(A,B,U)\) with a nonempty connected subgraph \(D\), with the
quotient recovered by contracting \(D\).

### Proof

Let the agreement pairs be \(M_1,M_2\), and let \(M_3=\{q,r\}\) be the
disagreement pair. Let \(a_i\) be the common endpoint of \(M_i\) selected
by \(A\) and \(B\), for \(i=1,2\), and put

\[
 \Delta=\{6,a_1,a_2\}.
\]

This is a triangle in \(R\). The four vertices

\[
 p,\quad v,\quad q,\quad r
\]

are each complete to \(\Delta\). By the description of \(U\),
\(\Delta\cap U=\{6\}\). Consequently every vertex of the expanded
subgraph \(D\) has at most one neighbour in \(\Delta\).

The six fixed vertices outside \(D\cup\Delta\) are \(p,v,q,r\) and the
two unselected endpoints of the agreement pairs. The first four have
three neighbours in \(\Delta\), while the last two have two. Hence

\[
 \sum_{y\notin D\cup\Delta}
 \bigl(|N_G(y)\cap\Delta|-1\bigr)
 =4(3-1)+2(2-1)=10.
\]

Lemma 1.1 applies, giving a contradiction. \(\square\)

For the other 24 relatively seven-connected triples, the catalogue gives an
explicit \(K_7\)-minor model in the quotient. Replacing \(z\), wherever it
occurs in its branch set, by its connected preimage \(D\) preserves
connectivity and every certified inter-branch-set adjacency, so the model
lifts to \(G\).
Thus the entire 48-instance quotient residue is closed at the literal-host
level, conditional on reaching exactly this quotient family.

## 5. Fixed regression instance and scope

For

\[
 A=\{0,2,4,6\},\quad
 B=\{0,2,5,6\},\quad
 U=\{1,3,4,5,6\},
\]

the quotient graph has graph6 code `I]~vy}jhw`. The certificate is

\[
 \Delta=\{0,2,6\},\qquad
 (q_1,q_2,q_3,q_4)=(4,5,p,v),
\]

with degree-deficit bound ten.

The theorem closes the 24 sharp marker quotients after literal expansion.
It does **not** prove:

- that every live operated-shore residue reduces to one of these
  quotients;
- that a marker-containing cut automatically gives a strict
  response-preserving restart; or
- the full order-eight response-coupling theorem or \(HC_7\).
