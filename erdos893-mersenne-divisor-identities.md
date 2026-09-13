# Erdős #893 — Mersenne divisor identities and a killed stronger inequality

**Author:** Jared Wilder  
**Status:** proved child identities + explicit negative theorem  
**Parent target:** the recovered campaign's full-tail divergence question for `f(2n)/f(n)` remains open

Let

\[
f(n)=\sum_{k=1}^{n}\tau(2^k-1),
\]

where `τ` is the divisor-counting function.

## 1. Divisor injection

For every `k≥1`,

\[
\boxed{\tau(2^k-1)\ge \tau(k).}
\]

### Proof

If `a|k`, write `k=am`. Then

\[
2^k-1=(2^a-1)\sum_{i=0}^{m-1}2^{ai}.
\]

Thus `2^a-1 | 2^k-1`. The map

\[
a\mapsto 2^a-1
\]

is injective on positive integers, so the divisors `a` of `k` give `τ(k)` distinct divisors of `2^k-1`.

## 2. Exact doubling factorization and factor-two consequence

For every `m≥1`,

\[
2^{2m}-1=(2^m-1)(2^m+1).
\]

Moreover

\[
\gcd(2^m-1,2^m+1)=1,
\]

because any common divisor divides `2`, while both factors are odd. Hence multiplicativity of `τ` gives

\[
\tau(2^{2m}-1)
 =\tau(2^m-1)\tau(2^m+1)
 \ge 2\tau(2^m-1).
\]

So

\[
\boxed{\tau(2^{2m}-1)\ge2\tau(2^m-1).}
\]

## 3. Multiplicative-order sum identity

For odd `d≥1`, define `ord_d(2)` to be the multiplicative order of `2` modulo `d`, with the convention `ord_1(2)=1`.

Then

\[
d\mid 2^k-1
\quad\Longleftrightarrow\quad
\operatorname{ord}_d(2)\mid k.
\]

Double-counting divisor incidences therefore gives the exact identity

\[
\boxed{
 f(n)=
 \sum_{\substack{d\ \mathrm{odd}\\ \operatorname{ord}_d(2)\le n}}
 \left\lfloor\frac{n}{\operatorname{ord}_d(2)}\right\rfloor .
}
\]

The displayed sum is finite: if `ord_d(2)≤n`, then `d` divides `2^k-1` for some `k≤n`, hence `d≤2^n-1`.

This identity is an exact reformulation of the original divisor sum; it is not an asymptotic estimate.

## 4. A tempting square inequality is false

The stronger-looking claim

\[
\tau(2^{2n}-1)\ge \tau(2^n-1)^2
\]

is false already at `n=4`:

\[
2^4-1=15,
\qquad \tau(15)=4,
\]

while

\[
2^8-1=255=3\cdot5\cdot17,
\qquad \tau(255)=8<16=\tau(15)^2.
\]

The factor-two inequality in Section 2 is the surviving unconditional statement from that route.

A separate campaign guess that `f(2n)/f(n)≤4` was also killed by exact finite data (`n=12` in the recovered record). Neither negative result settles the parent divergence problem.

## Scope

The campaign target requires full-tail divergence of `f(2n)/f(n)` to `+∞`. The identities above provide exact structure and unbounded local ingredients, but **unboundedness or large subsequences are not equivalent to full-tail divergence**. No such upgrade is claimed here.

Historical novelty is not asserted. This note publishes the exact surviving mathematics and keeps the failed stronger inequality adjacent to the theorem it corrects.