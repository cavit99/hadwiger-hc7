# Independent audit: two-component paired-state trichotomy

**Verdict:** **GREEN.**  The concise proof is complete under its exact
two-component and attained paired-state hypotheses.  In particular, the
two-cut argument needs neither an exact two-lobe decomposition nor the
later Kempe constraints: the first lobe plus one pole and its connected
complement already give the two adjacent complementary carriers used by
the spanning near model.

Audited theorem SHA-256:

```text
9be1bcc6b8770b244bb9dadf54d8d6eb9c96f041a261c33808a6e82e41404f94
```

The post-audit change only promoted the status line to “proved and
independently audited.”  The mathematical text is identical to the version
audited under SHA-256
`8bb14e19862e9191d1996351264a4063bb5d7c770267298c1e54709b6eb013cb`.

## 1. Reflection and pullback direction

For Lemma 2.1, `X+B_i`, `Y+B_j`, and `Q+B_k` are disjoint and connected.
The first two are adjacent through the assumed `X-Y` edge, and fullness of
`Q` joins the third bag to each of them.  The named `c-B_h` edges join all
three to the retained singleton `c`.  Hence the contraction produces a
literal `K_4`, so its four vertices receive distinct colours and pull back
to exactly `Pi`, not a coarsening.

The operation is supported on the rich side and leaves the nonempty open
`L`-shore untouched, so it is a proper minor and returns the exact state on
the closed `L`-side.  The operation assumed in the setup was supported in
the opposite closed shore and returned `Pi` on the closed `R`-side.
Aligning the four block colours and gluing is therefore in the correct
direction.

## 2. Small components

For a component `D` of `C-z`, its actual open neighbourhood is contained
in `S+{z}` and separates it from `Q` and the old opposite shore.
Seven-connectivity gives `|N_S(D)|>=6`.  A second component of `C-z` is
contained in the connected adjacent complement `E=C-D` and supplies the
same lower bound for `N_S(E)`.  Thus both availability sets have order at
least two and admit distinct duty representatives.

If `C=xy`, each endpoint has only its mate outside `S`, so minimum degree
seven supplies six boundary neighbours and the same representative
argument.

For a triangle, each singleton defect has order at most two and fullness
is exactly the empty triple intersection.  If the split `x | yz` has no
distinct duty representatives, both nonempty availability sets are the
same singleton.  Thus `Delta_x` hits the other two duties and
`Delta_y intersect Delta_z` also hits both.  The order-two bounds force the
latter intersection to have two elements and force
`Delta_y=Delta_z`.  Cyclic failure of all three splits then makes all three
defects equal, contradicting fullness.  Lemma 3.2 is therefore sound.

The three-connected branch invokes the audited uniform curvature theorem
with exactly its required disjoint full packet `Q`.

## 3. Two-cut defect calculation

For a component `D` of `C-{x,y}`, two-connectivity makes `D` adjacent to
both poles.  The set `X=D+{x}` is connected, while its complement `Y`
contains `y` and every other lobe, each adjacent to `y`; hence `Y` is
connected.  A `D-y` edge makes `X,Y` adjacent.

The actual neighbourhood of raw `D` is contained in `S+{x,y}` and
separates `D` from `Q`, so seven-connectivity gives at least five boundary
contacts.  Therefore `Delta(X)` has order at most two.  A second lobe,
contained in `Y`, gives the symmetric bound for `Delta(Y)`.  Since
`X union Y=C` and `C` is `S`-full, the two defects are disjoint.

Each defect of order at most two leaves at least one of the three paired
duties available.  Two nonempty subsets of a three-set fail to have an SDR
only when both are the same singleton.  If that singleton is duty 3, each
defect must use its full allowance of two labels, one from `B1` and one
from `B2`; disjointness makes the choices complementary.  Relabelling the
ends inside the two independent pairs gives exactly (4.5).  No assertion
about the number of lobes or individual pole contacts is needed after this
point.

## 4. Spanning near model

The seven bags in (4.6) are disjoint and connected.  They span because
`X union Y=C`, the rich shore has exactly the two components `C,Q`, and
the thin shore is the connected set `L`.

Their adjacencies are literal:

- `X-Y` is the lobe-to-opposite-pole edge;
- `X` sees `L+B1` and `Q+B2` through `t1,t2`;
- `Y` sees those bags through `a1,a2`;
- fullness of `L` or `Q` joins the two packet bags;
- both carriers see `c,r,s` because their only defects lie in
  `B1 union B2`, and both full packets see all three;
- `cr` is the selected literal edge.

Thus only `sr` (certainly absent because `B3` is independent) and `sc`
(possibly absent) can fail, and they share singleton centre `s`.  This is a
spanning labelled `K_7^vee` model.  The hypotheses of the audited
both-missing or one-hole trichotomy then follow exactly from spanning and
seven-connectivity, yielding the stated `S1` output.

## 5. Exhaustion and scope

If both rich components are singleton full packets, they are open twins;
delete one, six-colour the proper minor, and copy the other twin's colour.
Otherwise the setup explicitly chooses a nonsingleton `C`.  A cutvertex,
order two/three, or three-connectivity gives outcome 1.  Every remaining
`C` is two-connected but not three-connected and has the two-cut handled
above.  Hence no two-component case is omitted.

The theorem does not close rotation termination, a one-component rich
shore containing two interlaced packets, packet vector `(1,1)`, or an
arbitrary attained demand-three state.
