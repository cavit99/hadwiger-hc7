# Audit: simultaneous bipartite bilateral-exposure barrier

**Verdict:** **GREEN** for the exact revisions

```text
c211e32a2987d7e82ed639bc79e75735fd871a576d6d1a7064499b47c66b547e  barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier.md
97cef3a147e9d9ed630e0b13c70010976ad5c4184e5f51acc3719689d8edfeea  barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier_verify.py
```

This is a separate internal mathematical and computational audit completed
on 21 July 2026. It is not external peer review. Any change to the graph,
claims, verifier or stated scope requires renewed audit.

## 1. Replay and independent checks

The verifier was rerun with

```text
.venv/bin/python -B barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier_verify.py
```

and returned

```text
GREEN simultaneous_bipartite_bilateral_exposure_barrier
chi(F)=4; kappa(F)=4; chi(K3 join F)=7; kappa(K3 join F)=7
chi(double quotient)=6; X_lists=colourable; Y_lists=uncolourable
K7_model=true; joined_host_vertex_minimal=false
```

The graph6 decoder reproduces exactly the seventeen displayed edges.
Exhaustive colouring searches establish the three claimed chromatic numbers,
and exhaustive vertex-cut enumeration establishes both connectivities.
Independent NetworkX and direct brute-force checks reproduced those values
and confirmed that `F-1` remains four-chromatic.

## 2. Quotient, lists and minor model

Contracting `46` and `57` gives exactly `K_{2,4}+03`. The displayed quotient
colouring is proper. Directly taking palette complements at the four original
vertices gives

\[
 L(4)=\{0,2\},\qquad L(6)=L(5)=L(7)=\{0\}.
\]

Thus `46` is list-colourable while `57` is not. The four displayed branch
sets in `F` are connected, disjoint and pairwise adjacent; the three joined
triangle vertices complete them to the claimed `K_7` model.

## 3. Scope

The scope statement is exact. The example refutes only unconditional
simultaneous bilateral exposure. It satisfies the proved one-sided conclusion
because the `57` list system is uncolourable. The host contains a `K_7` minor,
and deleting vertex `1` leaves it seven-chromatic, so it does not address any
strengthening using global `K_7`-minor exclusion or full proper-minor
six-colourability.

No unresolved assumption or verifier discrepancy remains in the stated
finite claim.
