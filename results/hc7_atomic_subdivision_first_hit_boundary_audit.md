# Independent audit: first-hit boundaries in an arbitrary atomic `H_0` subdivision

**Verdict:** GREEN.

The first-hit confinement, both explicit `K_7`-minor constructions, the
order-seven and bounded-separator conclusions, and the interval-normalization
argument are correct under their stated hypotheses.  No unresolved assumption
or gap remains within the theorem's declared scope.

## 1. Audited revision and dependency

This audit checks exactly
[`hc7_atomic_subdivision_first_hit_boundary.md`](hc7_atomic_subdivision_first_hit_boundary.md)
at SHA-256
`3e359812caa2fa7fe9206b1be8e44f7b530fd714a06f0a6cba68a648feb15640`.

The mathematical content was first audited at SHA-256
`929ad11be161d1b11133131c9f1fab286ec3f80116e6feb35483438f0a0383f0`.
The finalized source differs only by changing its status from “audit pending”
to “audit GREEN.”  Replacing that final status line by the prior line
reproduces the earlier hash exactly; the theorem statements, proofs,
constructions, and trust boundary are unchanged.

The proof invokes the cross-pair path closure in
[`hc7_atomic_h0_bridge_quadrant_normal_form.md`](hc7_atomic_h0_bridge_quadrant_normal_form.md),
whose separately audited source has SHA-256
`821e79b0a7fbe77a23a77ce15eddb1257c29ebf04d35d7f5c3b8ab0f2458ca0e`.
I checked that each invocation satisfies that theorem's endpoint-support and
clean-`T`-path hypotheses.

This is an independent internal mathematical audit, not external peer review.
No computation is needed for the audited theorem.

## 2. First-hit regions, confinement, and anticompleteness

Deleting `V(T)-{q}` makes `D_q` a component containing no vertex of `T`
other than `q`.  Every neighbour of `D_q` outside it therefore lies in
`V(T)-{q}`, and every such neighbour is the end of a clean `T`-path from
`q`.  The same statements hold for `q'`.  Thus the definitions of
`Omega_q` and `Omega_q'` really are the complete clean first-hit boundaries.

For `q`, the support `{a,d}` crosses a missing pair with any attachment
supported at `b` or `c`.  The audited cross-pair closure therefore gives

\[
                       \Omega_q\subseteq T^{b,c}.
\]

The symmetric argument from the support `{b,c}` of `q'` gives
`Omega_q' subseteq T^{a,d}`.  No maximality or finite-subdivision assumption
is used.

The separator count is also exact.  The subdivision contains the eight
branch vertices and the three distinct internal vertices `q,q',h`.  If
`|Omega_q|<=7`, at least one vertex of `T-(Omega_q union {q})` remains on
the side opposite `D_q`.  Seven-connectivity gives `|Omega_q|>=7`; at
equality

\[
                 (D_q\cup\Omega_q,\;V(G)-D_q)
\]

is an actual separation of order seven with both exclusive sides nonempty.
The argument for `q'` is identical.

Finally, an intersection of `D_q,D_q'`, or an edge between them, produces a
clean `q`--`q'` path.  Its supports `{a,d}` and `{b,c}` cross both missing
pairs, so the cross-pair theorem applies.  Hence the claimed disjointness and
anticompleteness are valid in a `K_7`-minor-free host.

## 3. Common-`fg` first-hit construction

For Theorem 3.1, I checked the model for arbitrary lengths and all relative
orders of `h,u,v` on `T_fg`, including `u=v`.

- The interiors of `R` and `R'` belong to the disjoint regions `D_q,D_q'`.
  They are therefore disjoint, and their only possible common vertex is the
  common endpoint when `u=v`.
- The interval `I` contains `h,u,v` but neither `f` nor `g`.  Its `f`-side
  complement `F` is nonempty even when its boundary vertex `w` is adjacent
  to `f`.
- The seven initial sets `H,B,A,D,C,E,F` are nonempty and pairwise disjoint.
  Their nontrivial connectedness comes respectively from `R union I`,
  `(R'-v) union T_bq'`, `T_ag union (T_aq-q)`, and
  `(T_q'c-q') union T_cx`; the remaining sets are paths or singletons.
- Allocating each unused segment interior to a bag containing one endpoint
  preserves disjointness and connectedness.  On `T_fg`, assigning the
  `g`-side component to `A`, which already contains `g`, is valid and leaves
  every required boundary edge intact.

The six contacts incident with `H` are exactly

\[
 HE:he,\quad HF:T_{fg}\text{ at }w,\quad HA:T_{ad}\text{ at }q,
 \quad HB:R'\text{ at }v,\quad HD:T_{ad}\text{ at }q,\quad HC:hx.
\]

The other fifteen unordered pairs are supplied by

\[
\begin{array}{lllll}
 EF:T_{ef},&EA:T_{ea},&EB:T_{eb},&ED:T_{ed},&EC:T_{ec},\\
 FA:T_{fa},&FB:T_{fb},&FD:T_{fd},&FC:T_{fc},\\
 AB:T_{gb},&AD:T_{gd},&AC:T_{ax},\\
 BD:T_{bd},&BC:T_{bc}\text{ at }q',&DC:T_{dx}.
\end{array}
\]

Every named segment exists in `H_0`, and every cut segment retains the
displayed boundary edge.  These lists contain all twenty-one pairs of bags.
When `u=v`, the endpoint belongs to `H`, is removed from `B`, and the last
edge of `R'` still gives `HB`; no overlap is introduced.  Thus Theorem 3.1
is a valid explicit `K_7`-minor construction in an arbitrary subdivision.

## 4. Clean route-star bridge construction

For Theorem 3.2, each point in the open `f`- or `g`-route star has a unique
incident segment label.  I checked separately the four possibilities given
by whether `u=g` and whether `v=f`.

- If neither is exceptional, the `f`--`h` and `h`--`g` portions belong to
  `F` and `G`, with `h` in `X`.
- If exactly one is exceptional, the corresponding route is cut at `p` or
  `r`, and the middle part belongs to `X`.
- If both are exceptional, `p,h,r` occur in that order on `T_fg`; the
  displayed convention partitions the segment into disjoint `F`, `X`, and
  `G` parts.

The omitted edge `yz` partitions `Q` between `F` and `G`.  Its interior
avoids `T`, so it creates no collision with another bag.  The bag `A` is
connected through the whole path `T_ac`; `F` and `G` are connected through
`f` and `g`; and `X` is connected by the literal edge `hx`.  Far suffixes of
the two cut segments attach to the bags containing their labelled endpoints,
including the cases where both suffixes enter the same bag.

The six contacts incident with `X` are

\[
 XE:eh,\quad XA:T_{xa},\quad XB:T_{xb},\quad XD:T_{xd},
 \quad XF:T_{fh},\quad XG:T_{hg}.
\]

The remaining fifteen contacts are

\[
\begin{array}{lllll}
 EA:T_{ea},&EB:T_{eb},&ED:T_{ed},&EF:T_{ef},&EG:T_{eg},\\
 AB:T_{cb},&AD:T_{ad},&AF:T_{af},&AG:T_{ag},\\
 BD:T_{bd},&BF:T_{bf},&BG:T_{bg},\\
 DF:T_{df},&DG:T_{dg},&FG:yz.
\end{array}
\]

All twenty-one pairs are present after the segment allocations, including
when a contact is the surviving boundary edge at `p`, `r`, or `h`.  This
proves the explicit model.  For Corollary 3.3, two attachments of a component
bridge are joined by a path whose internal vertices lie in that component;
an edge bridge is already such a `T`-path.  The one-sided bridge conclusion
therefore follows without an unstated cleanliness assumption.

## 5. Exact normal form and bounded separator

After excluding a `K_7` minor and every order-seven separator, the two
first-hit boundaries have size at least eight, lie in their complementary
quadrants, and have disjoint anticomplete regions.  Theorem 3.1 shows that at
least one boundary misses `int(T_fg)`.  Interchanging the roots together with
`(a,d)` and `(b,c)` is a labelled automorphism of `H_0`, so the normalization
placing this property at `q'` is legitimate.  Corollary 3.3 independently
gives the one-sided support condition for every `T`-bridge.

For any branch-avoiding `q'`--`h` path that also avoids `q`, its initial
section up to the first new vertex `z` of `T` is a clean path inside the
first-hit region.  Hence `z in Omega_q' subseteq T^{a,d}`.  In the normalized
case `z` cannot lie in `int(T_fg)`, so the source correctly concludes only
that the path first meets `T` again outside `T_fg`.

If no such path exists, deleting

\[
                    Z=\{a,b,c,d,e,f,g,x,q\}
\]

separates `q'` from `h`.  An inclusion-minimal separator contained in `Z`
has order at least seven by seven-connectivity and at most nine by
construction.  Once the global order-seven outcome is excluded, its order
is eight or nine.  Thus the path-existence alternative in the stated residue
is exhaustive and does not hide a connectivity assumption stronger than
seven-connectivity.

## 6. Interval normalization

The elementary intervals are precisely the subpaths between consecutive
marked vertices on each segment, including a single edge between consecutive
marks.  The minimizing-shortcut proof of Lemma 5.1 is valid:

1. if a path meets an interval `J` in more than one component, replacing the
   section between its first and last vertices on `J` by the unique subpath
   of `J` makes the new intersection with `J` connected;
2. the replacement has no forbidden marked vertex internally, because an
   elementary interval has no marked internal vertex;
3. the prefix and suffix avoid `J`, so the replacement remains a simple
   path; and
4. distinct elementary intervals have disjoint interiors and at most one
   common marked endpoint, so the shortcut cannot increase the component
   count on another interval.

Consequently an existing branch-avoiding root--`h` path may be chosen to
meet `T` first outside `T_fg` and in at most one connected subpath of each
elementary interval.  Together with the order-eight-or-nine separator
alternative, this is exactly the residue stated by the source.

## 7. Trust boundary

The GREEN verdict establishes only the stated first-hit theorem.  In
particular, it does not prove any of the following:

- that an order-seven, order-eight, or order-nine separator carries the
  proper-minor colouring responses needed by the global programme;
- that the remaining one-sided bridge attachments are laminar, nested, or
  organized by a bounded chain decomposition;
- that a normalized single-path interval trace produces a crossing support,
  an ownership-preserving reduction, or an explicit `K_7`-minor model;
- a decreasing same-form reduction, global collision descent, the full
  atomic-collision theorem, or `HC_7`.

The proof also does not infer an unbounded theorem from the earlier
thirteen-vertex finite saturation.  Its unbounded conclusions come from the
written subdivision arguments audited above.
