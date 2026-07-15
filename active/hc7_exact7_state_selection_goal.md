# Active goal: exact-seven one-packet state selection

**Status:** primary research target.

## Decision

The audited tight-lobe transition and its split-audited packet analysis
have located the semantic obstruction precisely. A named contraction on
the actual packet-one shore always regenerates a high-demand exact state,
but neither its block shape nor the orientation needed for strict descent
is forced by local data. The explicit local orientation shell shows that
seven-connectivity, packet fullness, high demand and even the
separating-entry Kempe toggle are insufficient.

The next theorem must therefore use the two hypotheses absent from that
shell: literal `K_7`-minor-freeness and the response of **every** proper
minor. No further boundary census or Moser-labelled casework is part of
this goal.

## Uniform target

Let

\[
                V(G)=L\mathbin{\dot\cup}S
                       \mathbin{\dot\cup}R,
                \qquad |S|=7,
\]

be an actual separation in a seven-connected, strongly
seven-contraction-critical, `K_7`-minor-free graph, with packet vector

\[
                         (\nu_L,\nu_R)=(1,2).
\]

Put `H=G[S]`. Prove that the family of exact states obtained from named
proper-minor operations supported in the packet-one closed shore contains
a state `Pi` with

\[
                              d_H(\Pi)\le2,             \tag{SS}
\]

or that the same named response data constructs a literal `K_7` model or
a fixed pair `{p,q}` with `G-{p,q}` `K_5`-minor-free.

Condition (SS) is terminal: the two full packets in `R` reflect `Pi` onto
the contracted side, and the two intact closed-shore colourings glue. The
theorem is a uniform state-selection/rooted-model principle for all actual
`(1,2)` adhesions, not a list of boundary types.

## First milestone: reversed tight-lobe orientation

Use the tight cell

\[
                 V(G)=D\mathbin{\dot\cup}\Omega
                        \mathbin{\dot\cup}B,
                 \qquad |\Omega|=7,
\]

coming from the shortest-lock transition, and assume

\[
                         (\nu_D,\nu_B)=(2,1).           \tag{M1}
\]

The packet-one shore `B` is connected and `Omega`-full. Prove that some
named proper-minor operation supported in `B` returns, intact on the
two-packet `D` side, an exact state of demand at most two, or yields one of
the literal terminal outcomes above.

This closes the only orientation in which the strict lobe is not the
active packet-one shore. The local shell in
`../barriers/hc7_tight_gate_local_orientation_shell.md` is the mandatory
falsifier: every positive proof must identify the exact step where its
literal `K_7` model or failure of contraction-criticality is used.

## Constructive mechanism

1. Consider the complete transition family produced by boundary-edge
   deletions/contractions and star contractions in the connected
   packet-one shore; do not select one favourable colouring without a
   legality argument.
2. For each named contraction, retain both its exact boundary state and a
   regenerated `K_6` model in the proper minor.
3. If the model has enough labelled contact with the boundary, combine it
   with one of the two opposite full packets to obtain a literal `K_7`.
4. If contact is deficient, use the first deficient branch set to expose
   a literal separator or a new supported minor operation. A separator is
   useful only if its two sides attain the same exact state; a naked cut is
   not an outcome.
5. Show that an all-high-demand transition component either supplies the
   labelled rerouting in step 3 or contains a reversible cycle. In the
   latter case, use a named edge deletion/contraction response to break the
   cycle; merely declaring a rank is not enough.

The Humeau--Pous web theorem and Perfect augmentation may organize the
deficient-contact geometry, but neither transports the exact state. The
state must always come from the named proper-minor operation.

## Success and stopping tests

Success requires an explicit low-demand state and operation, literal
seven branch sets, or a proved fixed pair. A high-demand state, an
unlabelled `K_7^vee`, a naked smaller adhesion, or a reversible root
exchange is not success.

Terminate any proposed proof that uses only the abstract extension
language of the boundary: arbitrary such languages can be realized while
excluding relevant rooted clique minors. Likewise terminate a route whose
state space grows with shore order. Computation may falsify a transition
invariant or verify bounded certificates, but it may not replace the
unbounded theorem.
