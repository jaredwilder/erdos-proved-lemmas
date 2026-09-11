# Erdős #413 — logarithmic predecessor window

Author: Jared Wilder  
Public release: 2026-09-11

Let `omega(m)` denote the number of distinct prime divisors of `m`.

## Theorem

For `n>1`, the condition

`m + omega(m) <= n` for every `m<n`

is equivalent to checking only

`omega(n-k) <= k`

for

`1 <= k <= ceil(log_2(n-1))`.

More generally, for fixed `epsilon>0`, the condition

`m + epsilon*omega(m) <= n` for every `m<n`

needs only be checked for

`1 <= k <= ceil(epsilon*log_2(n-1))`, `m=n-k`.

## Proof

A positive integer with `t` distinct prime divisors is at least `2^t`, so

`omega(r) <= log_2 r`.

Writing `m=n-k`, the coefficient-one condition is `omega(n-k)<=k`. If

`k>log_2(n-1)`,

then

`omega(n-k) <= log_2(n-k) <= log_2(n-1) < k`,

so the inequality is automatic. The epsilon form is identical after multiplying the omega bound by `epsilon`.

## Scope

This is an exact certification reduction from `n-1` predecessor checks to `O_epsilon(log n)` checks. It does not prove the infinitude clauses of Erdős #413.

## License

Apache-2.0.
