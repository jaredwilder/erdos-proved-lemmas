# Erdős #893 — Mersenne divisor injection, summatory baseline, and order identity

Author: Jared Wilder. Public release: 2026-09-11.

## 1. Divisor injection

If `a|k`, then

`2^a-1 | 2^k-1`.

Indeed, writing `k=am`,

`2^k-1=(2^a-1)(1+2^a+...+2^(a(m-1)))`.

The map `a -> 2^a-1` is injective, so

`tau(2^k-1) >= tau(k)`.

## 2. Summatory lower baseline

Define

`f(N)=sum_{k<=N} tau(2^k-1)`.

Summing the pointwise injection gives

`f(N) >= sum_{k<=N} tau(k)`.

Therefore the classical divisor-summatory theorem yields

`f(N) >= N log N + (2 gamma - 1)N + O(sqrt(N))`.

In particular,

`f(N) >= (1+o(1)) N log N`.

## 3. Exact multiplicative-order identity

For an odd positive integer `d`,

`d | 2^k-1`

if and only if

`ord_d(2) | k`.

Double-counting pairs `(d,k)` with `d|2^k-1` and `k<=N` gives

`sum_{k<=N} tau(2^k-1)`

`= sum_{d odd, ord_d(2)<=N} floor(N/ord_d(2))`,

with the natural convention for `d=1`.

For fixed `N` the right-hand sum is finite because any contributing `d` divides some `2^k-1` with `k<=N`.

## 4. Doubling consequence

Since

`2^(2m)-1=(2^m-1)(2^m+1)`

and the two odd factors are coprime,

`tau(2^(2m)-1) = tau(2^m-1) tau(2^m+1) >= 2 tau(2^m-1)`.

## Scope

These are exact universal infrastructure and a classical-order lower baseline. They do not solve the surrounding asymptotic problem, and historical novelty is not claimed.