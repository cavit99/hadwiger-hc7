# Independent audit: complementary-lock near-`K_7` handoff

**Verdict:** **GREEN.**  The seven displayed bags form the claimed literal
labelled `K_7^vee` model, the exact `(1,2)` complementary-lock hypotheses
supply every abstract assumption, and the standardized trichotomy uses the
spanning and portal hypotheses correctly.  The result is a near-model
handoff, not a `K_7` minor or a proof that rotations terminate.

Audited theorem SHA-256:

```text
c5e05a59aeaad6f2325b7da5f59ba877f5c28bc4788ff5ab3dd0e24758b5cfe9
```

The hash changed after the audit only because the theorem status line was
promoted from “awaiting independent audit” to “proved and independently
audited”; the mathematical statement and proof are unchanged.

## 1. Abstract branch-set check

Write

```text
X=D+{x},  Y=E+{y},  F1=L+B1,  F2=Q+B2,  {c}, {r}, {s}.
```

1. The seven bags are nonempty and disjoint by the set hypotheses.
   `X,Y` are connected because the corresponding lobe meets its retained
   pole.  `F1,F2` are connected because each connected full packet meets
   both literal vertices of its assigned boundary pair.
2. `X-Y` is witnessed by a `D-y` edge (and also by an `E-x` edge).
   The four carrier--packet adjacencies are, in order,
   `D-t1,D-t2,E-a1,E-a2`, exactly as claimed.
3. `F1-F2` does not require an edge between the two old shores: fullness
   of `L` supplies an edge from `L` to `a2 in F2` (fullness of `Q` gives a
   symmetric witness).
4. Each of `c,r,s` meets `X,Y` by (1.2) and meets `F1,F2` by packet
   fullness.  The choice of `r` supplies `cr`.
5. Independence of `B3` makes `rs` absent.  The only other possibly absent
   bag pair is `cs`.  Hence all edges of `K_7` except at most `sr,sc` are
   present, and those two share the named singleton centre `s`.  An extra
   `cs` edge is harmless because a minor model may discard it.

No unproved inter-block adjacency or edge between `D` and `E` is used.

## 2. Exact complementary-lock specialization

The application faithfully supplies the abstract objects.

1. Seven-connectivity makes every component of the old open thin shore
   `S`-full.  Packet number one therefore permits only one such component,
   so `L` is connected and full.
2. `Q` is, by definition, the second connected `S`-full component of the
   rich shore.
3. The two components `D,E` of `C-{x,y}` are nonempty and connected.  Since
   `C` has no cutvertex, each lobe meets both poles.  Equations (3.6)--(3.8)
   give precisely the five literal contacts required from each lobe.
4. There are no unused vertices: the old separation is `L|S|R`, the rich
   shore is the disjoint union of `C,Q`, and
   `C=D union E union {x,y}`.  Thus (2.1) really makes the seven-bag model
   spanning.

The earlier static quotient is not a counterexample.  It has the lobe
system and the single external full packet `Q`, but it has no second
disjoint full packet that can serve as `L`; its connected lobe union cannot
be reused because it is already occupied by `X,Y`.

## 3. Trichotomy audit

### Both missing spokes (`cs` absent)

The centre `{s}` is anticomplete to the singleton twins `{c},{r}` and meets
the four neutral bags `X,Y,F1,F2`.  The other six bags form a `K_6` model.
Because the model is spanning, every literal neighbour of `s` lies in those
six bags; anticompleteness to the twins puts every neighbour in the four
neutral bags.  Seven-connectivity gives `d(s)>=7`, so the literal neutral
portal set has order at least seven.  These are exactly the hypotheses of
the audited uniform seven-root trichotomy.  Its rotated centre is a proper
nonempty connected subset of one of the four advertised neutral bags.

### One missing spoke (`cs` present)

Now `{s}` misses only the row `{r}` and contacts `{c},X,Y,F1,F2`; those six
foreign bags again form a `K_6`.  Spanning gives the essential
all-neighbours hypothesis in the audited singleton one-hole trichotomy.
The singleton row `{c}` cannot contain two selected roots and has no proper
nonempty subset, so every nonterminal rotated centre lies in one of
`X,Y,F1,F2`, as Corollary 2.2 states.

In both branches the separator conclusion is actual.  Seven-connectivity
gives separator order at least seven, and the standard minimum-cut argument
makes every component full only when the order is exactly seven.  The
corollary does not claim fullness at larger order.

## 4. Exact scope

The proof discharges the live complementary-lock transition by handing a
spanning, label-normalized near model to `S1`.  It does not repair either
missing spoke, produce a fixed apex pair, or establish a decreasing measure
for successive deficiency rotations.  Those remain separate obligations.
