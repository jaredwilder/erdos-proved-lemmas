# Erdős #655 — complete regular-polygon counterfamily

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Status:** complete negative answer to the literal frozen statement; no novelty/priority claim

## Frozen question

Let `x_1,...,x_n` be planar points such that no circle whose centre is one of the `x_i` contains three other points. Must there exist a constant `c>0` such that every sufficiently large such configuration determines at least

`(1+c)n/2`

distinct distances?

## Theorem

**No.** For every `n>=3`, a regular `n`-gon satisfies the stated circle condition and determines exactly

`floor(n/2)`

distinct distances.

Consequently no positive constant `c` can satisfy the displayed lower bound for all sufficiently large `n`.

## Proof

Place the vertices on a circle of radius `R`. Fix one vertex. The distances from it to the other vertices are

`2R sin(pi k/n)`

with offsets `k=1,...,n-1`, and the offsets `k` and `n-k` give the same distance. Thus any one distance from the fixed centre is attained by at most two other vertices. Hence no circle centred at one chosen vertex contains three other chosen vertices.

Globally the distinct chord lengths are exactly

`2R sin(pi k/n),  1 <= k <= floor(n/2)`.

These are strictly increasing over that range, so the configuration determines exactly `floor(n/2)` distinct distances.

For even `n` this is exactly `n/2`; for odd `n` it is `(n-1)/2`. Therefore, for every fixed `c>0`,

`floor(n/2) < (1+c)n/2`

for all `n>=3`. The proposed universal improvement is impossible.

## Authority boundary

The estate also contains a historical green Lean receipt attached to this campaign, but that receipt checks only a finite proxy instance. It does **not** certify the universal theorem above. The universal mathematical proof is the elementary argument in this file.

This result answers the literal frozen statement negatively. Because the counterfamily is elementary, this note makes no claim that the observation is historically new; it may instead expose a statement/transcription issue in the source lineage.

## License

Apache-2.0.
