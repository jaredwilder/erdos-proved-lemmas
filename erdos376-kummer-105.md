# Erdős #376 — exact Kummer digit criterion for gcd(C(2n,n),105)=1

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

For every positive integer `n`,

`gcd(C(2n,n),105)=1`

if and only if doubling `n` produces no carries in bases `3`, `5`, and `7`.

Equivalently:

- every base-3 digit of `n` is at most `1`;
- every base-5 digit of `n` is at most `2`;
- every base-7 digit of `n` is at most `3`.

## Proof

Since `105=3·5·7`, the gcd is 1 exactly when none of `3,5,7` divides `C(2n,n)`.

Kummer's theorem says that for a prime `p`,

`v_p(C(2n,n))`

is exactly the number of carries when adding `n+n` in base `p`.

Therefore `p` does not divide `C(2n,n)` exactly when doubling `n` is carry-free in base `p`.

A base-`p` digit `d` creates no carry under doubling exactly when `2d<p`, i.e.

`d <= (p-1)/2`.

Applying this for `p=3,5,7` gives the stated digit bounds.

## Scope

This is an exact characterization of the local `3·5·7` divisibility condition. It does not by itself prove infinitude of integers satisfying all three simultaneous digit restrictions.

Historical novelty is not claimed.