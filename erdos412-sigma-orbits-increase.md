# Erdős #412 — sigma-orbits are strictly increasing above 1

Author: Jared Wilder. Public release: 2026-09-11.

Let `sigma(n)` denote the sum of positive divisors of `n`.

## Theorem

For every integer `n>=2`,

`sigma(n) >= n+1 > n`.

Consequently every forward orbit

`n, sigma(n), sigma(sigma(n)), ...`

starting at `n>=2` is strictly increasing and therefore contains no repeated value.

## Proof

For `n>=2`, the positive divisors `1` and `n` are distinct. Therefore

`sigma(n) >= 1+n > n`.

Applying the same inequality at every iterate proves strict increase of the whole orbit.

## Scope

This rules out self-intersections within a single forward sigma-orbit above 1. It does not determine whether two different sigma-orbits can intersect.

Historical novelty is not claimed.