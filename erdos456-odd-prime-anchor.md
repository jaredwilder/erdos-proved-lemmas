# Erdős #456 — corrected odd-prime anchor

Author: Jared Wilder  
Public release: 2026-09-11

Let `p_n` be the smallest prime congruent to `1 mod n`, and let `m_n` be the smallest positive integer `m` such that `n | phi(m)`.

## Theorem

For every **odd prime** `p`,

`m_(p-1)=p_(p-1)=p`.

## Proof

Put `n=p-1`. If `m<=p-1`, then

`phi(m) <= m-1 <= p-2 < p-1`,

so `p-1` cannot divide `phi(m)`. Hence `m_(p-1)>=p`.

But `phi(p)=p-1`, so `m_(p-1)=p`.

For `p_(p-1)`, the prime `p` itself is congruent to `1 mod p-1`. No smaller prime can be congruent to `1 mod p-1`, because the positive integers in that residue class below `p` consist only of `1`. Therefore `p_(p-1)=p`.

## Endpoint correction

The historical vault stated the theorem for every prime. At `p=2`, `n=1`: under the standard convention `phi(1)=1`, the least `m` with `1|phi(m)` is `m_1=1`, while `p_1=2`. Thus `p=2` is a genuine endpoint exception.

## Scope

This gives an infinite exact equality family for Erdős #456. It does not settle the almost-all comparison or ratio questions.

## License

Apache-2.0.
