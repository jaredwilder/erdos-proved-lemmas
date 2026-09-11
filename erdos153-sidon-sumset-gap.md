# Erdős #153 — universal Sidon sumset bookkeeping and gap inequality

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `A` be a finite Sidon set of size `n`, under the convention that unordered pair sums with repetition are unique. Write

`A+A = {s_1 < ... < s_t}`.

Then

`t = n(n+1)/2`

and

`(s_t-s_1)^2 <= (t-1) * sum_{i=1}^{t-1} (s_(i+1)-s_i)^2`.

## Proof

A Sidon set has one distinct sum for each unordered pair `{a,b}` with repetition allowed. The number of such pairs is

`C(n+1,2)=n(n+1)/2`,

so `t=n(n+1)/2`.

Put

`d_i=s_(i+1)-s_i > 0`.

Then

`sum_i d_i = s_t-s_1`.

Cauchy-Schwarz gives

`(sum_i d_i)^2 <= (t-1) sum_i d_i^2`,

which is the claimed inequality.

## Scope

This is exact bookkeeping plus a universal convexity inequality. It does not settle the parent asymptotic extremal problem.

Historical novelty is not claimed.