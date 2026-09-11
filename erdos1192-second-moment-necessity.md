# Erdős #1192 — second-moment necessity bound

**Author:** Jared Wilder  
**Release:** 2026-09-11

Fix `r>=2`. Let `f_r(n)` be the representation-count function used in the frozen #1192 formulation, and suppose that for all `x>=1`

\[
\sum_{n\le x} f_r(n)^2\le Cx.
\]

Assume also the campaign's injective tuple-counting inequality

\[
\sum_{n\le x}f_r(n)
\ge
\left|A\cap\left[1,\left\lfloor\frac xr\right\rfloor\right]\right|^r.
\]

Then the counting function of `A` obeys the uniform necessity bound

\[
\boxed{
|A\cap[1,x]|
\le
(2Cr^2)^{1/(2r)}x^{1/r}
\qquad(x\ge1).
}
\]

## Proof

Cauchy–Schwarz gives

\[
\left(\sum_{n\le x}f_r(n)\right)^2
\le
(x+1)\sum_{n\le x}f_r(n)^2
\le Cx(x+1).
\]

Combining with the injective tuple count yields

\[
\left|A\cap\left[1,\left\lfloor\frac xr\right\rfloor\right]\right|^{2r}
\le Cx(x+1)
\le2Cx^2.
\]

Now apply this with a scale large enough to cover `[1,x]`, for example replacing `x` in the preceding inequality by `rx`; the floor then contains `[1,x]`. This gives

\[
|A\cap[1,x]|^{2r}
\le 2Cr^2x^2,
\]

and taking the `2r`-th root proves the claim.

## Scope boundary

This is the **necessity direction only**: any witness satisfying the prescribed second-moment condition must be sparse at scale `x^(1/r)`. It does not construct the set required by the canonical existential problem.

The estate also records the standard order-2 consequence that a Sidon set cannot be an asymptotic basis of order 2; that is related background rather than the existential close.
