# Erdős #410 — sigma(n) >= n+1, with equality exactly at primes

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 route candidate; elementary universal theorem independently rechecked

Let `sigma(n)` denote the sum of the positive divisors of `n`.

## Theorem

For every integer `n>=2`,

\[
\boxed{\sigma(n)\ge n+1.}
\]

Moreover

\[
\boxed{\sigma(n)=n+1\iff n\text{ is prime}.}
\]

## Proof

The positive divisors `1` and `n` are always present, so

\[
\sigma(n)\ge1+n.
\]

If `n` is prime, these are its only positive divisors and equality holds.

If `n` is composite, it has a proper divisor `d` with `1<d<n`; hence the divisor sum contains at least `1+d+n`, giving

\[
\sigma(n)>n+1.
\]

Thus equality occurs exactly for primes.

## Orbit consequence

In particular,

\[
\sigma(n)>n
\]

for every `n>=2`, so every forward orbit under repeated application of `sigma` starting above 1 is strictly increasing. That orbit consequence is also recorded separately in the public estate.

## Scope

This elementary theorem eliminates periodic/cyclic behavior of positive sigma-orbits above 1. It does not settle the quantitative growth-rate question in the parent problem.
