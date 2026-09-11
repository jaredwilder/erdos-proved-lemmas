# Erdős #1073 — divisor shape of `n!+1`

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `u>1` divide `n!+1`. Then every prime divisor `p` of `u` satisfies

`p>n`.

In particular, if `u` is composite, then

`u>n^2`.

## Proof

If a prime `p<=n` divided `u`, then `p|n!`. Because `u|n!+1`, the same prime would divide `n!+1`, hence their difference 1, impossible.

Thus every prime divisor of `u` exceeds `n`. A composite `u` contains at least two prime factors counted with multiplicity, so `u>n^2`.

Stronger counting or Wilson-type consequences require additional arguments; this file records the exact divisor-shape theorem.
