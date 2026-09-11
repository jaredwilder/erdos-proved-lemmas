# Erdős #359 — reciprocal-prefix invariant

Author: Jared Wilder  
Public release: 2026-09-11

Let `a_1<a_2<...` be the `n=1` greedy sequence in Erdős #359: `a_{k+1}` is the least positive integer not representable as a sum of consecutive earlier terms.

## Theorem

For every `k>=1`,

`sum_{i=1}^k 1/a_i >= 1`.

## Proof

By the greedy definition, every integer `t<a_{k+1}` is represented by a contiguous block of the prefix `a_1,...,a_k`.

Fix a starting index `i`. Because the sequence is increasing, a block of length `r` starting at `a_i` has sum at least `r a_i`. Hence the number of blocks starting at `i` whose sum is at most `a_{k+1}-1` is at most

`floor((a_{k+1}-1)/a_i)`.

The `a_{k+1}-1` integers from `1` through `a_{k+1}-1` must all occur among these block sums. Therefore

`a_{k+1}-1 <= sum_i floor((a_{k+1}-1)/a_i)`

`<= (a_{k+1}-1) sum_i 1/a_i`.

Division by `a_{k+1}-1` proves the claim.

## Scope

This is a universal invariant of the true greedy sequence. It does not settle the asymptotic density questions in Erdős #359. Historical novelty is not claimed beyond the targeted search recorded in the extraction archive.

## Correction boundary

A historical formal receipt used an incorrect initial value for the sequence. The theorem above does not rely on that receipt; it follows directly from the frozen greedy definition.

## License

Apache-2.0.
