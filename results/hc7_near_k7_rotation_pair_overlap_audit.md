# Audit: combined-centre rotation model

## Verdict

**GREEN.**  The combined-centre construction, the disjoint-pair
`K_7^-` consequence, and the one-hole/two-hole median are all literal
branch-set statements.

## Checks

1. `X union W` is connected by the explicit `X-W` edge in the rotation
   datum.  The connector `Z` is connected and adjacent to that union via
   the `Z-W` cut edge (and also has the recorded `Z-X` contact).
2. A fixed row outside `D` is met by `X`; a row in `D-E` is met by `W`
   because `W` misses exactly `E`.  Hence the merged bag can miss exactly
   rows in `D cap E`, as claimed.
3. For a row in `D`, `Z` supplies the repair contact used to make
   `X union Z` full in the rotated model.  For a row in `E`, the old donor
   `U=W union Z` met the row while `W` misses it, so `Z` supplies a literal
   contact.  Thus `Z` meets all of `D union E`.
4. If two order-two sets are disjoint, the merged bag is full and `Z`
   is forced to four of five rows.  The seven displayed bags have at most
   one missing pair and therefore form `K_7^-` (or `K_7`).
5. If the old/new deficiency orders are one and two and are disjoint,
   the merged bag is full and `Z` is forced to three rows.  Its two
   possible missing rows form one missing star at `Z`, giving a literal
   `K_7^vee`; one extra contact upgrades it as stated.
6. The overlap corollary assumes absence of a `K_7^-` **minor**, which is
   exactly what Theorem 1 would display.  In the one-common-label case,
   if `Z` met both outside rows, only the merged-bag/common-row edge could
   be absent, again giving `K_7^-`.

## Scope

Pair overlap is an edgewise constraint, not a holonomy theorem.  The
singleton-backtracking theorem supplies one lifted two-step consequence;
cycles changing the five-row frame and nonsingleton/two-piece rotations
remain open.

