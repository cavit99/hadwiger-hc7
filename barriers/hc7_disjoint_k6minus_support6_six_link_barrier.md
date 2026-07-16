# Six arbitrary linking paths do not compose a disjoint small model and a `K_6^-`

**Status:** explicit hand-checkable counterexample to an intermediate
linkage claim, with a width-five tree-decomposition certificate.  It is not
a counterexample to `HC_7` and is not seven-connected.

## 1. The false intermediate claim

A proposed closure of one zero-overlap support-six configuration was:

> If a six-vertex `K_5`-minor model and a disjoint literal `K_6^-` are
> joined by six pairwise vertex-disjoint paths using all twelve displayed
> endpoints, then their union contains a `K_7` minor.

After shortening and contracting the six paths, their endpoint pairing is
an arbitrary perfect matching between the two six-sets.  The graph below
shows that this information is insufficient.

## 2. Construction

On vertices `0,...,5`, let `Q={0,1,2,3}` induce a `K_4`.  Add the edge
`45`, join `4` to `0,1,2`, and join `5` to `3`.  Then the four singleton
sets indexed by `Q`, together with the connected branch set `{4,5}`, form
a six-vertex `K_5` model.

On vertices `6,...,11`, take `K_6` with the single edge `10 11` deleted.
Add the perfect matching

\[
  0,6,\quad 1,7,\quad 2,8,\quad 3,10,\quad
  4,11,\quad 5,9.                                   \tag{2.1}
\]

The graph6 encoding is

```text
K~w[ACb@wf`]
```

Thus all hypotheses of the false quotient claim hold literally.

## 3. Certificate excluding a `K_7` minor

The following seven bags, joined as a tree in the order indicated below,
form a tree decomposition:

\[
\begin{array}{lll}
B_0=012346,&B_1=123467,&B_2=234678,\\
B_3=346789,&B_4=3459,&B_5=3678910,\\
B_6=4678911.&
\end{array}
\]

Its tree edges are

\[
 B_0B_1, B_1B_2, B_2B_3, B_3B_4, B_3B_5, B_3B_6.
\]

Every graph edge has both ends in one displayed bag, and the bags
containing any fixed vertex induce a connected subtree.  Every bag has at
most six vertices, so the decomposition has width five.  Treewidth is
minor-monotone and `tw(K_7)=6`; therefore this graph has no `K_7` minor.

The adjacent verifier checks the model, the matching, and every axiom of
the displayed tree decomposition:

```text
uv run barriers/hc7_disjoint_k6minus_support6_six_link_barrier_verify.py
```

## 4. Exact implication

The counterexample refutes only composition from an arbitrary six-path
linkage.  Its connectivity is three.  In an actual seven-connected host,
the union of an extremal linkage has additional bridges or reroutings; a
positive theorem may still show that those additions either repair the
bad endpoint pairing or expose a separator of order at most six.

Accordingly, a useful continuation must retain bridge attachments or a
label-preserving augmenting-path certificate.  Replacing the six paths by
an unlabelled perfect matching discards essential information.
