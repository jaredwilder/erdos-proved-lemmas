# Erdős #681 — prime-residual equivalence, witness geometry, and finite atlas

**Author:** Jared Wilder  
**Date:** 2026-09-14  
**Parent status:** OPEN. This file records exact child theorems, formalized reductions, finite evidence, and an analytic theorem candidate without promoting any of them to a parent close.

Erdős #681 asks whether every sufficiently large `n` admits `k>0` such that `n+k` is composite and

\[
P^-(n+k)>k^2,
\]

where `P^-` denotes the least prime factor.

## 1. Exact residual equivalence — kernel checked

The parent problem is equivalent to the following prime-residual statement:

> For every sufficiently large prime `p`, there exists `h>=2` such that `p+h` is composite and
> \[
> P^-(p+h)>(h+1)^2.
> \]

The forward direction takes the hard input `n=p-1` and puts `h=k-1`; `k=1` is impossible because `p` is prime, and `k=2` is eliminated by parity for sufficiently large odd primes.

The reverse direction uses `k=1` whenever `n+1` is composite and invokes the residual witness only when `n+1` is prime.

A twelve-declaration Lean bundle for this reduction was kernel checked in the campaign; the extracted source is published separately as `erdos681-residual-equivalence.lean`.

## 2. Fourth-root necessity and parity

If `k` is a witness and `m=n+k`, then

\[
P^-(m)>k^2,
\qquad
(P^-(m))^2\le m,
\]

so

\[
\boxed{k^4<m.}
\]

On the hard family `n=p-1` with odd prime `p`, every nontrivial witness `k` is odd.

Thus the residual search is finite for each prime and naturally lives at fourth-root scale.

## 3. New exact factor-count hierarchy

Let `m=n+k` be a witness and let `Omega(m)` count prime factors with multiplicity. Every prime factor of `m` is at least its least prime factor and hence is strictly larger than `k^2`. Therefore

\[
\boxed{m>k^{2\Omega(m)}}.
\]

Consequences:

- if `m<k^6`, then `Omega(m)=2` because `m` is composite;
- more generally, `m<k^{2t}` forces `Omega(m)<t`.

This explains why fourth-root-edge witnesses are forced into two-prime geometry rather than merely suggesting it empirically.

## 4. Balanced-semiprime squeeze near the fourth-root edge

In the `Omega(m)=2` case write

\[
m=qr,
\qquad q\le r,
\]

with primes `q,r`. Since `q=P^-(m)>k^2`,

\[
q>k^2,
\qquad
r=\frac{m}{q}<\frac{m}{k^2}.
\]

Hence

\[
\boxed{\frac rq<\frac{m}{k^4}}.
\]

Equivalently, if

\[
\rho=\frac{k}{m^{1/4}}<1,
\]

then

\[
\frac{r}{q}<\rho^{-4},
\qquad
\frac{q}{\sqrt m}>\rho^2.
\]

So as a witness approaches the fourth-root boundary, its two prime factors are *provably forced toward a balanced near-square factorization*. The campaign's record-witness phenomenon is therefore structural, not an accident of the initial data.

## 5. Record witnesses in the extracted atlas

For the record-minimal witness sequence through `k=41`, every recorded endpoint had exactly two prime factors, including prime squares:

```text
p=167       k=3   p-1+k=169       =13^2
p=1069      k=5   p-1+k=1073      =29*37
p=2803      k=7   p-1+k=2809      =53^2
...
p=1216577  k=33  p-1+k=1216609   =1103^2
...
p=2872981  k=41  p-1+k=2873021   =1693*1697
```

This finite observation is now explained by the factor-count and balance lemmas above when the witness lies sufficiently near the fourth-root boundary.

## 6. Clean top-down finite census

The exported campaign contains 85 terminal chunk receipts covering the contiguous range

\[
1.5\times10^{11}\le p<10^{12}.
\]

Across those chunks the exact search processed

\[
\boxed{31,532,474,062}
\]

primes and found

\[
\boxed{637,893}
\]

window-bad primes, where a prime is window-bad if no admissible odd fourth-root-window shift gives a composite endpoint with least prime factor above the required square threshold.

The largest bad prime recorded in the clean terminal chunks is

\[
\boxed{999,997,304,513}.
\]

The C engine was independently recompiled and cross-checked against a separate Python implementation on smaller windows. For example:

```text
[20,000,000,21,000,000): 59,336 primes; 7,742 bad
[1,000,000,000,1,001,000,000): 48,155 primes; 984 bad
```

Both implementations agreed exactly on those checks.

This is finite evidence only. It cannot resolve the eventual quantifier in #681.

The large interrupted bottom-up log in the session export is deliberately excluded from the clean census because it has no terminal range certificate.

## 7. Analytic almost-all route — theorem candidate, not novelty claim

The campaign also assembled an almost-all argument for the prime residuals by fixing an odd `K`, separating prime-shift exceptions, and placing the remaining bad primes in a family of reduced residue classes modulo a primorial.

The campaign's final audit charged an extra logarithm in the reduced-residue variance. Using the Montgomery--Vaughan reduced-residue second-moment scale, the intended bound is instead

\[
\delta(K)\ll \frac{(\log K)^2}{K}+\exp(-cK/\log K),
\]

subject to writing all source/effectivity details cleanly.

Inserted into the campaign's Brun--Titchmarsh dyadic argument, this points to the explicit exceptional-set candidate

\[
\#\{p\le X:p\text{ window-bad}\}
\ll
\pi(X)\frac{(\log\log X)^2}{\sqrt{\log X}}.
\]

**Status:** theorem candidate / proof-writeup debt, not promoted here as a finished theorem.

There is also substantial prior-art risk: the public Erdős #681 discussion already contains an unconditional 'almost all primes' sieve route. Accordingly this repository makes **no novelty claim** for density zero, and any explicit rate must undergo a dedicated literature comparison before publication as a new result.

## 8. KBK route diagnosis

The campaign's route kills are positive information.

A generic pointwise proof cannot rely only on integer rough-number gaps: the needed roughness threshold is tied to the shift and the relevant interval is shorter than the generic Jacobsthal scale. A structured CRT construction based on forcing `p-1` to be divisible by every small prime also dies by a size trap: the required primorial already exceeds the fourth-root-scale ambient prime.

The parent problem therefore concentrates on a genuinely prime-specific exceptional set rather than on a generic finite search.

## Authority boundary

- Prime-residual equivalence: kernel checked.
- Fourth-root necessity and parity: kernel checked / elementary.
- Factor-count hierarchy and balanced-semiprime squeeze: elementary exact deductions.
- `1.5e11` to `1e12` census: computation-supported with 85 terminal range receipts and independent small-window replay.
- Density-zero / explicit-rate section: analytic theorem candidate with source/effectivity and prior-art debt.
- Parent #681 remains open.
