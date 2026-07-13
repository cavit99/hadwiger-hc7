# Audit: two-defect disconnected-bag closure

## Verdict

**GREEN.**  Every component neighbourhood used in the proof is an actual
vertex cut, the seven-connectivity count is exact, all possible missed
rows are covered, and the seven bags in Theorem 3.1 remain pairwise
adjacent even when the two components miss different ordinary rows.

## 1. Actual-cut and row classification

For a component `R` of `B-X`, spanningness gives

\[
 N_G(R)\subseteq X\cup L.
\]

Because `B-X` is disconnected, a different component `R'` exists.
Distinct components of `B-X` are anticomplete, so every vertex of `R'`
lies outside `R union N_G(R)`.  Thus `N_G(R)` is a genuine separator, not
merely a contact set, and seven-connectivity applies.

Connectedness of `B` forces `R` to meet at least one of `x_s,x_t`.  If it
meets only one, the bound `|N_G(R)|>=7` forces all six rows of `L`; if it
meets both and sees all of `L`, the same full-row model applies.  The
displayed model

\[
 \{b_s\},\{b_t\},\{q_1\},\{q_2\},\{q_3\},R,
 \{v,x_s,x_t\}
\]

is literal: its last bag is a star at `v`, sees `b_s` through `x_t`, sees
`b_t` through `x_s`, and sees every ordinary singleton directly; `R`
sees the five singleton bags and the star through its witness contact.

Therefore a target-free component meets both witnesses and misses exactly
one row of `L`.  If it misses `v` or `b_s`, the bags in (2.6) work:
`{b_s,v,x_t}` is connected, sees `x_s` through `v`, and sees `R` through
`x_t`; `R` sees `b_t` and all ordinary singleton rows.  The `b_t`-missed
case is the exact `s,t`-symmetric model.  Hence the sole missed row is in
`O`.

## 2. Two-component branch-set audit

Choose distinct components `R_1,R_2`, and let `q` be the row missed by
`R_2`.  The seven bags in (3.1) are

\[
 \{b_s,q,v\},\quad \{b_t\},\quad
 \{q'\}\ (q'\in O-\{q\}),\quad \{x_s\},\quad
 R_1\cup\{x_t\},\quad R_2.
\]

They are disjoint.  The first is connected by `b_s-q-v`, and the enlarged
component bag is connected through an `R_1-x_t` edge.

The only delicate case is when `R_1` misses a different ordinary row
`q'`.  It causes no failure:

* `R_1 union {x_t}` sees that singleton through the literal edge
  `x_tq'`;
* it sees `b_t` through `R_1`, repairing the missing edge `x_tb_t`;
* it sees `R_2` through the edge `x_t-R_2`;
* `R_2` sees every singleton in `O-{q}`, both witnesses, `b_t`, and the
  first bag through `v` or `b_s`; and
* `{x_s}` sees both components through their actual witness contacts and
  sees every required singleton by its row.

All remaining pairs are within the singleton clique or use `v-x_s`,
`v-x_t`.  Thus all 21 branch-bag adjacencies are present for equal or
different missed rows.

The disconnected alternative is therefore impossible in a
`K_7`-minor-free host.  Combined with the independently audited captured
portal theorem, this closes the entire `d=2` low-portal residue under the
two-portal hypothesis of the palette-to-label corollary.
