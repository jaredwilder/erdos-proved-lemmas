# Erdős #394 — exact prime-window formula

Author: Jared Wilder  
Public release: 2026-09-11

Let `t_k(n)` be the least positive integer `m` such that

`n | m(m+1)...(m+k-1)`.

## Theorem

For every integer `k>=1` and every prime `p>k`,

` t_k(p) = p-k+1 `.

## Proof

If `m <= p-k`, then the entire interval

`m, m+1, ..., m+k-1`

lies in `{1,...,p-1}`. None of its terms is divisible by `p`, so its product is not divisible by `p`. Hence

`t_k(p) >= p-k+1`.

At

`m=p-k+1`,

the final term of the interval is exactly `p`, so the product is divisible by `p`. Therefore

`t_k(p) <= p-k+1`.

Combining the two inequalities proves equality.

## Consequence

For each fixed `k`, primes alone contribute a quadratic-over-logarithmic lower baseline to the summatory function:

`sum_{n<=x} t_k(n) >= sum_{k<p<=x} (p-k+1)`.

Using the prime number theorem for the sum of primes, this is of order `x^2/log x`.

## Literature boundary

The `k=2` specialization `t_2(p)=p-1` is explicitly recorded in the current Erdős #394 literature. The general `p>k` formula above is the direct interval extension of the same mechanism. No historical novelty claim is made without a specialist search.

## Provenance

Recovered from the Day-One route chronology. Later raw `FALSE` rows on the same problem contain off-by-one interval mistakes; those are recorded separately in Semantic Court 07 and do not affect the proof above.

## License

Apache-2.0.
