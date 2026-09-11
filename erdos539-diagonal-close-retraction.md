# Erdős #539 — diagonal-close retraction

**Author:** Jared Wilder  
**Release-day audit:** 2026-09-11  
**Status:** correction / retraction of a false historical route

## Canonical quantity

For a finite set `A` of positive integers define

\[
Q(A)=\left\{\frac{a}{\gcd(a,b)}:a,b\in A\right\},
\]

and let `h(n)` be the minimum possible size of `Q(A)` over all `n`-element sets `A`.

## The false route

A historical campaign route claimed that the diagonal pairs inject `A` into `Q(A)` via

\[
a\mapsto \frac{a}{\gcd(a,a)}=a.
\]

That equality is false. In fact

\[
\gcd(a,a)=a,
\qquad
\frac{a}{\gcd(a,a)}=1.
\]

Thus every diagonal pair collapses to the single value `1`; it does not provide `n` distinct quotient values.

The claimed universal lower bound `h(n)>=n` and the resulting claimed exact formula `h(n)=n` therefore do not follow and are retracted.

## Why the error is load-bearing

The accompanying upper construction `A={1,...,n}` does satisfy `Q(A) subseteq {1,...,n}`, but an upper bound alone cannot establish equality. The entire lower-bound argument was the incorrect diagonal map.

Current public work on #539 studies a genuinely sublinear regime; the problem is not made trivial by diagonal pairs.

## Surviving assets

Any independently proved finite value or lower bound for #539 must be rechecked without using the false diagonal injection. In particular, this correction does not invalidate exact computations whose quotient sets were explicitly enumerated; it invalidates only deductions that used `a/gcd(a,a)=a`.

## Release consequence

- Erdős #539 remains **OPEN**.
- Historical branch-close language asserting `h(n)=n` is superseded.
- The diagonal identity is now a permanent regression test:

```text
for every a>0: a / gcd(a,a) = 1
```

This record is intentionally public so the same one-line semantic error cannot be promoted again during later estate mining.
