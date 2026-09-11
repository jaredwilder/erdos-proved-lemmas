# Erdős #317 — exact signed-harmonic lattice reduction

**Author:** Jared Wilder  
**Public routing:** 2026-09-11

Let

\[
L_n=\operatorname{lcm}(1,2,\ldots,n)
\]

and let `δ_k∈{-1,0,1}`. Put

\[
S_n(\delta)=\sum_{k=1}^n\frac{\delta_k}{k}.
\]

## Theorem — exact lattice structure

For every `n` and every choice of signs,

\[
\boxed{S_n(\delta)=\frac{M}{L_n}}
\]

for an integer

\[
M=\sum_{k=1}^n\delta_k\frac{L_n}{k}.
\]

Consequently, whenever `S_n(δ)≠0`,

\[
\boxed{|S_n(\delta)|\ge\frac1{L_n}.}
\]

This is an exact universal statement; no computation is required.

## Strict inequality is exactly a numerator-exclusion problem

The second clause of the frozen Erdős #317 question asks whether, for all sufficiently large `n`, every nonzero signed harmonic sum satisfies

\[
|S_n(\delta)|>\frac1{L_n}.
\]

By the theorem above, this is equivalent to the finite arithmetic statement

\[
\boxed{M\ne\pm1}
\]

for every admissible sign vector once `n` is sufficiently large.

Thus the strict problem is not a generic analytic lower-bound problem: it is exactly the eventual nonattainability of the two lattice numerators `+1` and `-1`.

## Small equality witnesses

The strict inequality certainly fails at small `n`:

- `n=2`, `(δ_1,δ_2)=(1,-1)` gives `S=1/2=1/L_2`;
- `n=4`, `δ_3=1, δ_4=-1` gives `|1/3-1/4|=1/12=1/L_4`.

These witnesses are why the historical universal-strict formulations were killed rather than promoted.

## Correction record

The historical registry around #317 contains mutually inconsistent labels. The exact lattice theorem is sound, but two attempted consequences were not:

1. the lattice lower bound by itself does **not** settle the first `c/2^n` question;
2. `1/L_n` is asymptotically on the scale `e^{-n+o(n)}`, which is **smaller** than `2^{-n}`, not larger.

So no asymptotic close is claimed here from the granularity argument alone.

A recovered Lean/cable receipt for route `R003/L1` was kernel-clean only at a bounded Boolean scope (`checkRange 30 = true`). It is supporting finite evidence, **not** a universal formalization of the theorem above. The universal proof is the one-line denominator-clearing argument displayed here.

## Scope

This packet releases the exact reusable theorem and the correct residual formulation. It does not claim either full clause of Erdős #317 is solved.
