# Erdős #377 — corrected large-prime Kummer interval criterion

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `p<=n` be prime and suppose

`p > sqrt(2n)`.

Put

`k = floor(n/p)`.

Then

`p ∤ C(2n,n)`

if and only if

`p > 2n/(2k+1)`.

Equivalently, with `n=kp+r`, `0<=r<p`, divisibility by `p` occurs exactly when `2r>=p`.

## Proof

Because `p>sqrt(2n)`, one has `2n<p^2`. Thus the base-`p` addition `n+n` can have at most one carry, from the units digit.

Write

`n=kp+r`, `0<=r<p`.

By Kummer's theorem, `p` divides `C(2n,n)` exactly when adding `n+n` in base `p` creates a carry. Under `2n<p^2`, this happens exactly when

`2r >= p`.

Therefore

`p ∤ C(2n,n)` iff `2r<p`.

Since `r=n-kp`,

`2(n-kp)<p`

is equivalent to

`2n < (2k+1)p`,

or

`p > 2n/(2k+1)`.

## Correction boundary

The large-prime hypothesis is load-bearing. A broader ledger version omitted `p>sqrt(2n)` and is false because higher base-`p` digits can create additional carries.

Historical novelty is not claimed.