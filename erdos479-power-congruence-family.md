# Erdős #479 — an infinite power-congruence family

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Fix `j>=0` and set

`k=2^(2^j)`.

For every odd prime `p`, let

`n=2^j p`.

Then

`2^n ≡ k (mod n)`.

Hence every `k` in the infinite family

`2,4,16,256,...`

has infinitely many corresponding solutions `n`.

## Proof

Modulo `p`, Fermat's theorem gives `2^(p-1)≡1`, and the exponents `2^j p` and `2^j` differ by `2^j(p-1)`. Thus

`2^(2^j p) ≡ 2^(2^j) (mod p)`.

Modulo `2^j`, both sides vanish for `j>=1`; the `j=0` case has modulus 1. Since `gcd(2^j,p)=1`, the Chinese remainder theorem gives the congruence modulo `n=2^j p`.

A formal companion to this family appears in `jaredwilder/erdos-theorems`.
