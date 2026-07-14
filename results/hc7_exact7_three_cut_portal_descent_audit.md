# Independent audit: three-cut portal descent

**Verdict:** GREEN.

**Audited source:**
`results/hc7_exact7_three_cut_portal_descent.md`

**Source SHA-256:**
The mathematical body audited before promotion had SHA-256
`015c04acaef6a758846cd179d75bfab87fa4fe6e02ebeb6b714ee6419bd472c4`.
Promotion changed only the status line and file location.
The promoted source hash is
`88ee9b3a82dd0e15914c5090166bba9a2f80a5f14bcb6f79a3a9bcaf4c19432e`.

The requested earlier SHA `681645a842fad06c160089f61f87e79bcf10aa791cd4305fb76684d3b362f2d9`
was no longer present in the shared workspace.  This audit covers the
current source identified above.

## 1. Literal lobe boundary

Let `D` be a component of `G[L]-T`, where `|T|=3`.  Its neighbours inside
`L` all lie in `T`.  If it missed a member of `T`, its `L`-neighbourhood
would have order at most two and would separate `D` from another component
of `G[L]-T`, contradicting three-connectivity.  Therefore

\[
                              N_L(D)=T.
\]

There is no `L-R` edge, and different components of `G[L]-T` have no edge
between them.  Hence

\[
                      N_G(D)=T\cup N_S(D).
\]

This set is a genuine vertex cut: another lobe and the original nonempty
shore `R` remain outside it.  Seven-connectivity gives

\[
                       3+|N_S(D)|\ge7.
\]

Thus every lobe has support at least four.  At equality the displayed
neighbourhood has exactly seven literal vertices.  Every member of `T`
has a neighbour in `D`, and every member of `N_S(D)` does so by definition,
so `D` is full to this exact boundary.  The opposite shore is nonempty and
`D` is a proper nonempty subset of `L`; the claimed actual strict
seven-separation follows.

## 2. Arbitrarily many lobes

A three-cut has at least two lobes, so their family can be partitioned
into two nonempty subfamilies.  With

\[
 X=\{t_1\}\cup\bigcup\mathcal D_X,
 \qquad
 Y=\{t_2,t_3\}\cup\bigcup\mathcal D_Y,
\]

the sets are disjoint and cover `L`.

Every lobe meets every gate vertex.  Consequently all lobes assigned to
`X` are joined through `t_1`, making `G[X]` connected.  Any one lobe
assigned to `Y` contains, together with its incident edges, a connection
between `t_2` and `t_3`; all other assigned lobes attach to both, so
`G[Y]` is connected without assuming `t_2t_3`.  Finally `t_1` has a
literal neighbour in every `Y`-lobe, giving an actual `X-Y` edge.

Each side contains at least one lobe and hence has boundary support at
least five in the non-descent branch.  Since `X union Y=L` and
seven-connectivity makes `L` `S`-full, their two supports cover all of
`S`.

## 3. Anchored two-defect theorem

The four sets `X,Y,P,Q` are pairwise disjoint and connected.  The pairs
`X-Y` and `P-Q` are literal adjacencies; `P,Q` are `S`-full;
`|N_S(X)|,|N_S(Y)|>=5`; and the two supports cover `S`.  These are exactly
the four incidence hypotheses of Theorem 2.1 in
`results/hc7_exact7_binary_gate_near_model.md`.  The boundary hypothesis
also matches: `G[S]` has either a spanning non-path tree or is
`K_{1,3} dotcup K_3`.  The promoted theorem therefore returns the claimed
literal labelled `K_7^vee` model without using a virtual gate edge.

## 4. Corollary and trust boundary

Once the near-model and strict-descent outputs are excluded, the argument
rules out every three-cut.  Together with the assumed three-connectivity
and `|L|>=5`, this is precisely four-connectivity.  The prior bound
`delta(G[L])>=4` indeed implies `|L|>=5` in a finite simple graph.

The source correctly does not claim that the old equality state survives
the descended boundary.  It proves a literal near-model or exact smaller
adhesion handoff only.
