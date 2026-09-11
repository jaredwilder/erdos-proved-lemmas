# Erdős #683 — the entire upper-half k range follows from Sylvester

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** recovered transcript theorem; citation-dependent on the classical Sylvester prime-divisor theorem

Let `P(N)` denote the largest prime divisor of `N>1`.

## Theorem

Let `1<=k<n` and assume

\[
k\ge n/2.
\]

Then

\[
\boxed{
P\!\left({n\choose k}\right)\ge n-k+1.
}
\]

Consequently, on the entire range `k>=n/2`, the Erdős #683 target inequality

\[
P\!\left({n\choose k}\right)
\ge
\min\bigl(n-k+1,k^{1+c}\bigr)
\]

holds for **every** `c>0`.

## Proof

Put

\[
m=n-k.
\]

Then `m<=n/2`, so `n>=2m`, and by symmetry

\[
{n\choose k}={n\choose m}.
\]

Use the classical Sylvester theorem: a product of `m` consecutive integers all exceeding `m` has a prime divisor `p>m`. Apply it to

\[
(n-m+1)(n-m+2)\cdots n.
\]

Since `n>=2m`, its smallest factor is at least `m+1`. Hence the numerator of

\[
{n\choose m}
=
\frac{(n-m+1)\cdots n}{m!}
\]

has a prime divisor `p>m`. Such a prime cannot divide `m!`, so it survives in the binomial coefficient. Therefore

\[
P\!\left({n\choose m}\right)\ge p\ge m+1=n-k+1.
\]

This proves the theorem.

## Scope

This is a complete half-range theorem. It does not address the harder range `k<n/2`, where the `k^{1+c}` arm of the minimum can become load-bearing.

The prime-divisor input is classical and is not claimed as new; the value of this release is the exact reduction of the parent problem's upper-half parameter range.
