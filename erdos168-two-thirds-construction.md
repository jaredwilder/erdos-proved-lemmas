# Erdős #168 — a two-thirds construction avoiding `{n,2n,3n}`

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

For every positive integer `N`, let

`A_N={1<=m<=N : 3∤m}`.

Then `A_N` contains no complete triple `{n,2n,3n}`, and

`|A_N| = N-floor(N/3) = ceil(2N/3)`.

Therefore the corresponding extremal function satisfies

`F(N) >= ceil(2N/3)`.

## Proof

Every triple `{n,2n,3n}` contains `3n`, which is divisible by 3, while `A_N` contains no multiple of 3. The cardinality follows by deleting the `floor(N/3)` multiples of 3 from `[N]`.

This is an exact constructive lower bound. A matching upper bound is a separate question.
