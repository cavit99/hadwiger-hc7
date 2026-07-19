# Internal audit: two-shore Kempe incidence cycle

**Verdict:** **GREEN** for the exact source revision

```text
efd281de3d162f1aeb831503a093fd5651a6199bb0e4fac02ae9db660db262c3
```

of
[`hc7_two_shore_kempe_incidence_cycle.md`](hc7_two_shore_kempe_incidence_cycle.md).
This is a separate internal mathematical audit, not external peer review.
The source differs from the independently line-audited revision
`2fd84830d3905f61bc45a49570174bda551207dda6af5486cb81b4e1ace7ac41`
only by adding its opening link to this audit; its mathematical content is
identical.

## 1. Scope checked

The audit checked the full source, including:

1. the binary equations describing simultaneous full-component Kempe
   switches on both closed shores;
2. the bridge criterion in a bipartite multigraph with retained parallel
   edges;
3. the lift of a simple incidence cycle, including a two-edge parallel cycle
   and paths which revisit the boundary;
4. the nonbipartite literal union and localization of every odd cycle to the
   operated boundary component and both open shores; and
5. the seven-connected order-eight separator/full-component consequence.

## 2. Exact bridge criterion

The boundary `alpha`--`beta` components form a common edge set because
interchanging the two colours on one boundary component changes neither the
two-colour vertex set nor its induced graph.  Each full two-colour component
on a closed shore determines one block of these boundary components, and
different blocks correspond to disjoint full components, so all chosen block
switches are simultaneous legal Kempe interchanges.

For a boundary component `C`, the two switched traces agree exactly when

\[
              x_{P_C}+y_{Q_C}={\bf1}_{C=K}
\]

over `F_2`.  Every non-operated incidence edge forces equal endpoint bits;
the operated edge forces unequal bits.  The system is therefore soluble
exactly when deleting `e_K` separates its endpoints, i.e. exactly when
`e_K` is a bridge.  A solution makes the two literal boundary colourings
identical, so the two closed-shore colourings glue.  Thus in a non-`q`-
colourable host `e_K` is a nonbridge and lies on a cycle.  Retaining parallel
edges is necessary: two parallel edges form the valid length-two cycle
obstruction.

## 3. Literal cycle lift

At a vertex of the incidence cycle, the two incident edges name boundary
components lying in one connected full two-colour component on the
corresponding shore.  Hence a literal two-colour path joins them.  Distinct
cycle vertices in the same bipartition class are distinct full components,
so the selected same-shore paths are vertex-disjoint.  Paths on opposite
shores have disjoint open-shore interiors, though they may share or revisit
boundary components; the source makes no stronger assertion.  Cutting a
path at successive boundary visits correctly yields nontrivial segments
whose interiors lie in one literal open shore.

The two-edge parallel case is covered: its two block vertices supply one
path in each shore between the two distinct boundary components represented
by the parallel edges.

## 4. Odd-cycle parity and localization

Let `H_Z` be the union of the selected full components.  If it were
bipartite, comparison of its two-colouring with each connected shore
colouring would assign one flip bit to every incidence-cycle vertex.  At
every cycle edge other than `e_K` the two traces agree and force xor zero;
at `e_K` they are interchanged and force xor one.  Summing around the cycle
uses every vertex bit twice and yields `0=1`.  Extra intersections and
off-cycle boundary components do not affect these selected cycle equations.
Hence `H_Z` is nonbipartite and contains an odd cycle.

After deleting all vertices of `K`, the two original traces agree on the
remaining common boundary.  Pasting `c_A` on `A union (X-V(K))` with `c_D`
on `D` therefore gives a proper two-colouring of `H_Z-V(K)`.  Each one-
closed-shore intersection is separately two-coloured by its original shore
colouring.  Consequently every odd cycle in `H_Z` meets `K` and uses
vertices from both `A` and `D`.

## 5. Order-eight consequence

Every nonempty boundary-clean path segment has interior in one component
`Q` of `G-X`, so `N_G(Q) subseteq X`.  The other nonempty open shore leaves
a vertex outside `Q union N_G(Q)`.  Seven-connectivity and `|X|=8` therefore
give either `|N_G(Q)|=7`, an actual order-seven separation, or
`N_G(Q)=X`.  Applying this to all cycle-supporting segments gives exactly
the stated trichotomy: common colouring, actual order-seven separator, or
every used complementary component boundary-full.

## 6. Trust boundary

The theorem composes one opposite-shore Kempe transition exactly and yields
a literal alternating odd-cycle certificate.  It does not:

- make a boundary-full complementary component split while retaining all
  eight contacts;
- allocate cycle pieces to inherited clique-minor branch-set labels;
- guarantee that an odd-cycle branch-set decomposition meets prescribed
  contraction requirements; or
- construct a `K_7`-minor model.

No unresolved assumption remains inside the stated theorem.  The live
order-eight residue is precisely its third outcome, where further
operation-specific or label-preserving geometry is required.
