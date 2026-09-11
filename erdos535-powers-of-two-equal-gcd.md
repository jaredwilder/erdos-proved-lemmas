# Erdős #535 — powers-of-two equal-gcd avoidance construction

**Author:** Jared Wilder  
**Release:** 2026-09-11

For every `r>=3` and `N>=1`, the powers of two not exceeding `N` give the campaign lower bound

\[
\boxed{f_r(N)\ge \lfloor\log_2 N\rfloor+1.}
\]

## Proof

Take

\[
A=\{1,2,4,\ldots,2^m\},\qquad m=\lfloor\log_2N\rfloor.
\]

For distinct powers `2^i,2^j`,

\[
\gcd(2^i,2^j)=2^{\min(i,j)}.
\]

In any set of at least three distinct powers of two, order the exponents

\[
i_1<i_2<i_3<\cdots.
\]

Then

\[
\gcd(2^{i_1},2^{i_2})=2^{i_1},
\qquad
\gcd(2^{i_2},2^{i_3})=2^{i_2},
\]

so the pairwise gcds cannot all be equal. Hence the whole power-of-two set avoids the forbidden `r`-tuple configuration for every `r>=3`.

Its cardinality is `m+1`, proving the bound.

## Scope / novelty boundary

This is an elementary universal construction baseline, not a parent-problem close and not a historical novelty claim. It is released because the exact construction was a promoted mathematical asset in the estate rather than research scaffolding.
