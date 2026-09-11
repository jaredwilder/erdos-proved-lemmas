# Erdős #359 — universal quadratic upper bound for the true greedy sequence

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `a_1,a_2,...` be the true `n=1` greedy consecutive-block-sum sequence: after choosing `a_1,...,a_k`, the next term `a_(k+1)` is the least positive integer not representable as a sum of a contiguous block of the current prefix.

Then for every `k>=1`,

`a_(k+1) <= k(k+1)/2 + 1`.

## Proof

There are exactly

`k(k+1)/2`

nonempty contiguous blocks of a length-`k` sequence. Hence the current prefix can represent at most `k(k+1)/2` distinct positive integers as contiguous block sums.

Among the first

`k(k+1)/2 + 1`

positive integers, at least one is therefore missing. Since `a_(k+1)` is defined as the least missing positive integer,

`a_(k+1) <= k(k+1)/2 + 1`.

## Scope and correction boundary

This theorem is attached to the true greedy definition. A historical green receipt used the wrong initialization `a_2=5`; that receipt is semantically quarantined and is not evidence for this statement.

The theorem is an elementary universal upper bound, not a determination of the true growth rate.