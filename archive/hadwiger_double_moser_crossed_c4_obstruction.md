# The smallest strict carrier obstruction is already a (K_7) frame

## 1. Purpose

In the cut-irreducible double-Moser body, relative boundary order at least
eight does **not** by itself force the two desired rooted Steiner carriers.
The smallest obstruction is a crossed four-cycle.  It has no relative
separator of order at most seven, but the double-Moser boundary converts it
directly into a (K_7)-model.  Thus the correct structural statement must
have three outcomes:

\[
 \text{two carriers}\quad\text{or}\quad K_7
 \quad\text{or}\quad\text{an exact seven-adhesion}.       \tag{1.1}
\]

Omitting the middle outcome makes the proposed split-or-cut lemma false.

## 2. The crossed (C_4)

Let

\[
 R=r_0r_1r_2r_3r_0
\]

be an induced or non-induced four-cycle.  Make each of (a,b,p,q)
adjacent to all four vertices of (R), and prescribe the four root portal
sets by

\[
\begin{array}{c|c}
x_1&\{r_0,r_1\}\\
x_2&\{r_2,r_3\}\\
x_3&\{r_1,r_2\}\\
x_4&\{r_0,r_3\}.
\end{array}                                             \tag{2.1}
\]

Additional contacts or chords are harmless for the (K_7)-certificate
below, although they can create the desired carriers.

### Lemma 2.1 (no two cross-saturated carriers)

In the exact graph (2.1), there are no disjoint connected sets

\[
 A\subseteq R\text{ meeting }P_3,P_4,qquad
 B\subseteq R\text{ meeting }P_1,P_2.              \tag{2.2}
\]

Consequently there are no disjoint carriers rooted at (a,b) with the
required opposite portal classes.

#### Proof

Every connected (P_3)--(P_4) set contains one of the two cycle edges

\[
                         r_0r_1,\quad r_2r_3,
\]

because these are exactly the edges crossing from
({r_1,r_2}) to ({r_0,r_3}).  Every connected
(P_1)--(P_2) set similarly contains one of

\[
                         r_1r_2,\quad r_3r_0.
\]

Each edge in the first pair meets each edge in the second pair.  Hence the
two connected sets cannot be disjoint.  Since (a,b) are full to (R),
adjoining the roots does not alter this conclusion. (square)

### Lemma 2.2 (strict relative boundary)

Put (S=\{a,b,x_1,x_2,x_3,x_4,p,q\}).  For every nonempty proper
(Y\subset R),

\[
             |N_R(Y)-Y|+|N_S(Y)|\ge8.              \tag{2.3}
\]

#### Proof

The four labels (a,b,p,q) meet every nonempty (Y).  A singleton has
two internal neighbours and belongs to exactly two of the four root
portal sets, giving (2+4+2=8).  An adjacent pair has two internal
frontier vertices and meets three root labels, giving nine.  An opposite
pair has two frontier vertices and meets all four root labels, giving ten.
A three-vertex set has one frontier vertex and meets all four root labels,
again giving nine.  These are all nonempty proper subsets. (square)

Thus this is a strict relative-eight obstruction, not an example already
disposed of by an exact seven-cut.

## 3. The direct (K_7)-model

### Theorem 3.1 (crossed four-cycle closure)

In the double pure-Moser frame, the portal pattern (2.1) gives a
(K_7)-minor.

#### Proof

Use the seven bags

\[
\begin{aligned}
 &\{u\},\quad\{v\},\quad\{x_1\},\quad\{x_2\},\\
 &\{x_4,a,r_0\},\quad
   \{x_3,q,r_2\},\quad
   \{b,p,r_1,r_3\}.                              \tag{3.1}
\end{aligned}
\]

They are connected: the first two nonsingleton bags use the portal edges
(x_4r_0,x_3r_2) together with the full (a)- and (q)-contacts;
the last uses the full contacts from (b,p) to (r_1,r_3).

The first four bags form a clique through the two stars and (x_1x_2).
Each of the last three sees those four bags as follows:

* ({x_4,a,r_0}) uses (ux_4), (vx_4), (ax_1), and (ax_2);
* ({x_3,q,r_2}) uses (ux_3), (vx_3), (qx_1), and (qx_2);
* ({b,p,r_1,r_3}) uses (up), (vb), (x_1r_1), and
  (x_2r_3).

Finally the three nonsingleton bags are pairwise adjacent through,
respectively, (x_3x_4), (ab), and (pq).  Hence (3.1) is a
(K_7)-model. (square)

## 4. Exact computational check and scope

`double_moser_crossed_c4_probe.cpp` independently exhausts all branch-set
models in the fourteen-vertex conservative quotient and returns the model
(3.1).  The same probe also checks a denser diamond obstruction found by a
strict-relative profile search; it too contains a (K_7)-minor.

Because the live branch already assumes (|R|\ge4), the crossed cycle is
the smallest possible strict carrier counterarchitecture.  It does not
refute the (K_7)-free programme.  Instead it proves that a carrier
packing theorem cannot be the whole argument: a crossless theorem must
separate the direct crossed-frame minor from the web/adhesion outcome.

