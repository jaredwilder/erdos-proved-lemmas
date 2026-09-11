# Erdős #412 — forward sigma-orbits are strictly increasing above 1

Author: Jared Wilder. Public release: 2026-09-11.

Let `sigma(n)` denote the sum of the positive divisors of `n`.

## Theorem

For every `n>=2`,

`sigma(n) >= n+1 > n`.

Consequently every forward orbit

`n, sigma(n), sigma(sigma(n)), ...`

starting from `n>=2` is strictly increasing and has no repetitions.

## Proof

For `n>=2`, the divisors `1` and `n` are distinct and both occur in the divisor sum. Hence `sigma(n)>=n+1>n`. Apply the same inequality at every later point of the orbit.

This rules out cycles and self-intersections within a single forward orbit above 1. Intersections between orbits from distinct starting values are a separate question.

A formal Erdős #412 result also appears in `jaredwilder/erdos-theorems`; this file is the human-readable compact statement.
