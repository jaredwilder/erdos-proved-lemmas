# Erdős #1049 — Lambert-series divisor identity

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted identity with correction of the historical overclaim

Let `t>1` be real.

## Theorem

\[
\boxed{
\sum_{n=1}^{\infty}\frac1{t^n-1}
=
\sum_{m=1}^{\infty}\tau(m)t^{-m}.
}
\]

## Proof

For every `n>=1`, since `t^{-n}<1`,

\[
\frac1{t^n-1}
=
\frac{t^{-n}}{1-t^{-n}}
=
\sum_{k=1}^{\infty}t^{-nk}.
\]

All terms are nonnegative, so Tonelli's theorem allows rearrangement:

\[
\sum_{n\ge1}\frac1{t^n-1}
=
\sum_{n\ge1}\sum_{k\ge1}t^{-nk}
=
\sum_{m\ge1}\left(\#\{(n,k):nk=m\}\right)t^{-m}.
\]

The number of positive factor pairs `(n,k)` with `nk=m` is exactly `tau(m)`. Hence the identity follows.

The series is absolutely convergent for every `t>1`, since `tau(m)` grows subexponentially and the factor `t^{-m}` decays exponentially.

## Correction record — what this does NOT prove

A historical campaign route tried to infer irrationality for rational `t>1` merely from the fact that `tau(m)` is unbounded, via a claim that the coefficient sequence could not represent a rational base expansion.

That inference is invalid. In positional or rational-base expansions, carries can radically change the visible digit sequence, and the coefficients `tau(m)` are not restricted to a digit alphabet. Unbounded coefficients therefore do **not** imply a nonperiodic digit expansion and do not by themselves imply irrationality.

Accordingly, this release promotes only the exact Lambert-series identity. The historical irrationality argument is rejected rather than laundered into a theorem.

## Scope

This identity is classical Lambert-series mathematics. It is released here for provenance and because it is the correct exact kernel of the #1049 campaign route; no historical novelty claim is made.
