# Erdős #291 — corrected leading-base-p harmonic divisibility criterion

Author: Jared Wilder. Public release: 2026-09-11.

Let `L_n = lcm(1,2,...,n)` and `a_n = Σ_{k=1}^n L_n/k`. Fix a prime `p≤n`, let `p^e` be the largest power of `p` not exceeding `n`, and put `q=floor(n/p^e)`.

## Theorem

If `num(H_q)` denotes the numerator of `H_q` in lowest terms, then

`p | gcd(a_n,L_n)` if and only if `p | num(H_q)`.

Equivalently, because the reduced denominator of `H_q` is prime to `p`,

`p | a_n` if and only if `H_q ≡ 0 (mod p)`.

### Proof

Since `v_p(L_n)=e`, all terms `L_n/k` with `v_p(k)<e` vanish modulo `p`. The surviving denominators are exactly `k=p^e j` with `1≤j≤q<p`. Writing `C=L_n/p^e`, one has `p∤C` and

`a_n ≡ C Σ_{j=1}^q j^{-1} ≡ C H_q (mod p)`.

Therefore `p|a_n` exactly when `H_q≡0 (mod p)`.

## Correction record

An earlier version used `H_{floor(n/p)}`. That index is wrong in general: the terms surviving modulo `p` are controlled by the largest power `p^e≤n`, not merely by `p`. The cases `(n,p)=(18,3)` and `(20,3)` separate the false version from the corrected theorem.

A deterministic exact-integer check over `1≤n≤37` and all primes `p≤n` agrees with the corrected formula. The theorem itself is analytic and holds for all `n,p` in the stated range.
