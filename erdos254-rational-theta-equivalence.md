# Erdős #254 — exact rational-theta divergence criterion

**Author:** Jared Wilder  
**Status:** exact child theorem / hypothesis characterization; no parent-close claim  
**Historical novelty:** not asserted

## The theorem

Let

\[
\theta=\frac aq\in(0,1)
\]

be reduced, with `q>=2`, and let `A` be any set of positive integers. Then

\[
\sum_{n\in A}\|\theta n\|=\infty
\]

if and only if `A` contains infinitely many integers not divisible by `q`.

Here `||x||` denotes distance from `x` to the nearest integer.

## Proof

Because `gcd(a,q)=1`,

\[
q\mid an \iff q\mid n.
\]

If `q|n`, then `theta n` is an integer, so

\[
\|\theta n\|=0.
\]

If `q∤n`, write `an≡r (mod q)` with `1<=r<=q-1`. Then

\[
\|\theta n\|
=\left\|\frac rq\right\|
=\frac{\min(r,q-r)}q
\ge\frac1q.
\]

Therefore:

- if only finitely many `n in A` fail to be divisible by `q`, only finitely many terms are nonzero, so the sum is finite;
- if infinitely many `n in A` fail to be divisible by `q`, infinitely many terms are at least `1/q`, so the sum diverges.

This proves the equivalence.

## Boundary

The recovered #254 campaign used this fact to expose the exact modular content of the rational-`theta` part of one of its hypotheses. Later routes found counterexamples to stronger parent-level claims, but those do not affect this elementary equivalence.

This note publishes only the exact rational-parameter characterization above. No novelty claim is made.