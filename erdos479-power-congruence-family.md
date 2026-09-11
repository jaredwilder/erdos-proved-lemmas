# Erdős #479 — four infinite power-congruence families and a Novák closure

Author: Jared Wilder. Public release: 2026-09-11.

For an integer `k`, write

`W(k)={n>=1 : n | 2^n-k}`.

## 1. The `k=0` family

For every `a>=1`,

`2^a ∈ W(0)`.

Indeed, `2^a` divides `2^(2^a)`.

Thus `W(0)` is infinite.

## 2. The `k=-1` family

For every `a>=1`,

`3^a ∈ W(-1)`.

Equivalently,

`3^a | 2^(3^a)+1`.

By the lifting-the-exponent lemma,

`v_3(2^(3^a)+1)=v_3(2+1)+v_3(3^a)=a+1`,

which is more than enough.

Thus `W(-1)` is infinite.

## 3. The `k=2` family

Every odd prime `p` lies in `W(2)` by Fermat's theorem:

`2^p ≡ 2 (mod p)`.

Hence `W(2)` is infinite.

It also contains composite examples. In particular `341=11*31` lies in `W(2)`, since `2^340≡1` modulo both 11 and 31.

## 4. The family `k=2^(2^j)`

Fix `j>=0` and set

`k=2^(2^j)`.

For every odd prime `p`, let

`n=2^j p`.

Then

`2^n ≡ k (mod n)`.

Modulo `p`, Fermat gives

`2^(2^j p) ≡ 2^(2^j) (mod p)`.

Modulo `2^j`, both sides vanish for `j>=1`; the `j=0` case has modulus 1. Chinese remaindering gives the result modulo `n`.

Hence every `k` in

`2,4,16,256,...`

has infinitely many witnesses.

## 5. Novák closure inside `W(-1)`

If

`n∈W(-1)`

and `p` is an odd prime divisor of `2^n+1`, then

`np∈W(-1)`.

### Proof

For every prime power `q^e||n` with `q!=p`,

`2^n≡-1 (mod q^e)`,

so, because `p` is odd,

`2^(np)=(2^n)^p≡-1 (mod q^e)`.

For the `p`-part, LTE gives

`v_p(2^(np)+1)=v_p(2^n+1)+1`.

This is at least `v_p(n)+1`, which is exactly the exponent of `p` required in `np`. Therefore every prime-power divisor of `np` divides `2^(np)+1`.

Thus `np|2^(np)+1`.

Starting from `1`, this mechanism produces for example

`1,3,9,171,...`.

## Scope

These are exact infinite subfamilies and a closure mechanism. They do not classify all integers `k` for which `W(k)` is infinite.

A broader naive lifting rule for arbitrary `k!=1` is false; none of the statements above uses it. Historical novelty is not claimed.