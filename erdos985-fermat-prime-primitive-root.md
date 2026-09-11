# Erdős #985 — 3 is primitive modulo every Fermat prime at least 5

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `p>=5` be a Fermat prime. Then `3` is a primitive root modulo `p`.

## Proof

A Fermat prime `p>=5` has the form

`p=1+2^(2^m)` with `m>=1`,

so `p≡5 (mod 12)`. The quadratic-character formula for 3 gives `(3/p)=-1`. By Euler's criterion,

`3^((p-1)/2) ≡ -1 (mod p)`.

Thus the order of 3 modulo `p` does not divide `(p-1)/2`. Since `p-1` is a power of 2, every proper divisor of `p-1` divides `(p-1)/2`. Therefore

`ord_p(3)=p-1`.

This theorem covers the Fermat-prime subfamily.
