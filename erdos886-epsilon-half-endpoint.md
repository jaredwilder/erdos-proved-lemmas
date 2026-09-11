# Erdős #886 — exact endpoint for `epsilon >= 1/2`

**Author:** Jared Wilder  
**Release:** 2026-09-11

In the frozen divisor-window formulation, if

\[
\varepsilon\ge\frac12,
\]

then

\[
\left(\sqrt n,\sqrt n+n^{1/2-\varepsilon}\right)
\]

has length at most 1. Hence it contains at most one integer, and therefore

\[
\boxed{K=1}
\]

works uniformly throughout this parameter range.

## Proof

Since `epsilon>=1/2`,

\[
1/2-\varepsilon\le0,
\]

so for every positive `n`,

\[
n^{1/2-\varepsilon}\le1.
\]

An open real interval of length at most 1 contains at most one integer. Thus at most one divisor can lie in the stated interval.

## Scope boundary

This removes the easy endpoint range only. The hard regime is

\[
0<\varepsilon<1/2.
\]

No historical novelty claim is made for this elementary reduction.
