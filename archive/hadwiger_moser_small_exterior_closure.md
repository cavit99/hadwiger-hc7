# Eliminating small exteriors in the two-component pure-Moser cell

## Theorem

Let $G$ be a seven-connected graph, let $d(v)=7$, and suppose

\[
G[N(v)]\cong M,
\qquad
G-N[v]=C\mathbin{\dot\cup}Y,
\]

where

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

If $C\cong K_k$ for $k\in\{2,3,4\}$, then $G$ contains a
$K_7$-minor.

Combined with the singleton-exterior lemma and the global cutvertex and
two-cut closures, every exterior component in a surviving two-component
pure-Moser cell has order at least five and is 3-connected.

## Boundary inequalities forced by seven-connectivity

Let $k\in\{2,3,4\}$, write $C=K_k$, and take a nonempty set
$S\subseteq V(C)$.  Its open neighbourhood satisfies

\[
N_G(S)=N_N(S)\mathbin{\dot\cup}(V(C)-S).
\]

Indeed, the two exterior components are anticomplete and no exterior
vertex is adjacent to $v$.  This neighbourhood separates $S$ from
$v$.  Seven-connectivity therefore gives

\[
|N_N(S)|+k-|S|\ge7.                                  \tag{1}
\]

Also $Y$ meets every vertex of $N$, since otherwise its boundary in
$N$ would be a cut of order at most six.

## Certified finite lemma

Contract $Y$ to a helper $y$, retain the $k$ vertices of $C$,
and retain all seven boundary vertices and all Moser edges.  Join $y$
to all of $N$.  Allow the $7k$ incidences between $C$ and $N$ to
vary, subject precisely to (1).

### Lemma

For $k=2,3,4$, every resulting quotient contains an
$N$-meeting $K_6$-model.

### Certificate

The discovery program `moser_two_component_small_probe.py` uses a lazy
exact search.  For each satisfying incidence assignment it exhausts all
connected vertex subsets of the quotient and searches for six disjoint,
pairwise adjacent bags, each containing exactly one of six selected
boundary roots.  It records only the optional boundary incidences needed
by the model and blocks that monotone model in the next iteration.

The independent verifier `moser_two_component_small_verify.py` does not
import the discovery code.  It reconstructs every inequality (1), checks
each recorded bag for disjointness, boundary meeting, connectivity and
all fifteen cross-adjacencies using only fixed edges and its recorded
incidences, and verifies that excluding all recorded models is
unsatisfiable.  The certificates contain respectively

\[
8,\quad84,\quad\hbox{and}\quad552
\]

model clauses.  A complete replay prints

```text
verified K2 exterior with 8 model clauses
verified K3 exterior with 84 model clauses
verified K4 exterior with 552 model clauses
```

The remaining trust boundary is the Z3 kernel; no DRAT or proof-assistant
trace is exported.

## Lifting the model

Replace the helper $y$ in a certified branch set by the connected
component $Y$.  Every used helper-boundary incidence exists because
$Y$ has full attachment to $N$; all other quotient vertices are
actual vertices of $G-v$.  The six bags therefore lift to an
$N$-meeting $K_6$-model in $G-v$.  The singleton bag $\{v\}$ is
adjacent to all six bags and completes a $K_7$-model. $\square$

## Exact residual consequence

The general singleton-exterior lemma excludes order one.  A connected
two-vertex exterior is $K_2$.  A connected three-vertex exterior with
no cutvertex is $K_3$, and the only 3-connected graph on four vertices
is $K_4$.  The theorem excludes all three, while the global
cutvertex and two-cut theorems exclude all vertex cuts of order one or
two.  Hence every remaining exterior component has at least five
vertices and is genuinely 3-connected; no small-order convention remains.
