# Simultaneous bipartite bilateral-exposure barrier

**Status:** computer-assisted finite mechanism barrier;
[separately audited **GREEN**](hc7_simultaneous_bipartite_bilateral_exposure_barrier_audit.md).
This graph is not a counterexample to `HC_7`: it deliberately
contains a `K_7` minor and is not proper-minor-minimal. It refutes only the
claim that one common double-contraction colouring must block both
anticomplete bipartite expansions.

## 1. The exact graph

Let `F` have vertex set `{0,...,7}` and edge set

```text
03 04 06 07 14 15 16 17 24 25 26 27 35 36 37 46 57
```

Its graph6 string is `GCxvvg`. Put

\[
                              X=\{4,6\},\qquad Y=\{5,7\}.
\]

Both induced subgraphs are edges, and `X,Y` are anticomplete. Contracting
both gives

\[
                         F/X/Y=K_{2,4}+03,              \tag{1.1}
\]

where the two degree-four-side vertices are the contraction images. In the
proper three-colouring

\[
 c(X)=c(Y)=0,\quad c(0)=c(1)=c(2)=1,\quad c(3)=2,       \tag{1.2}
\]

the expansion lists are

\[
\begin{array}{c|cc}
 &\text{first end}&\text{second end}\\ \hline
X=46&\{0,2\}&\{0\}\\
Y=57&\{0\}&\{0\}.
\end{array}                                             \tag{1.3}
\]

Hence `X` is list-colourable (`4` gets `2` and `6` gets `0`), whereas `Y`
is not.

## 2. Seven-connected `q=6` form

Let

\[
                              J=K_3\vee F.              \tag{2.1}
\]

The deterministic verifier establishes

\[
 \chi(F)=4,\quad \kappa(F)=4,
 \qquad \chi(J)=7,\quad \kappa(J)=7.                   \tag{2.2}
\]

Colour the added triangle with three new colours. Then (1.2) becomes a
six-colouring of `J/X/Y`; the lists in (1.3) are unchanged because the
three new colours occur at neighbours of every vertex of `X\cup Y`.
Moreover,

\[
                              \chi(J/X/Y)=6.             \tag{2.3}
\]

Thus this is a seven-connected, seven-chromatic instance with an exactly
six-chromatic simultaneous contraction in which only one of the two
expansions is blocked.

The graph has an explicit `K_7` model. In `F`, four branch sets are

\[
                     \{0\},\quad\{3\},\quad
                     \{1,4,5\},\quad\{6\};             \tag{2.4}
\]

adjoining the three singleton vertices of the joined `K_3` gives seven
branch sets. Also `F-1` remains four-chromatic, so `J-1` remains
seven-chromatic. Therefore `J` is not even vertex-minimal, and no
minor-criticality claim is being smuggled into the example.

## 3. Verified scope

The retained script
[`hc7_simultaneous_bipartite_bilateral_exposure_barrier_verify.py`](hc7_simultaneous_bipartite_bilateral_exposure_barrier_verify.py)
checks the exact graph6 encoding, all displayed edges, the two contractions,
chromatic numbers, vertex connectivities, lists, colourability asymmetry,
the `K_7` model and failure of vertex-minimality.

The construction refutes

> In every `q`-colouring after simultaneously contracting two anticomplete
> connected bipartite subgraphs, both expansion-list systems are
> uncolourable.

It does not refute the one-sided conclusion of Theorem 2.1 in
[`../results/hc7_marked_edge_response_coupling.md`](../results/hc7_marked_edge_response_coupling.md),
which says that at least one system is uncolourable. It also does not refute
a theorem that uses full proper-minor six-colourability or global
`K_7`-minor exclusion; this host has neither property.
