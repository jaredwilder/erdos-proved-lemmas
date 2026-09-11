# Erdős #859 — the density d_t always exists and is rational

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promotion queue / independent residue recheck

For a fixed positive integer `t`, let `d_t` be the natural density of integers `n` for which `t` can be represented as a sum of distinct positive divisors of `n`.

## Theorem

For every fixed `t>=1`, the defining predicate is periodic. In particular, `d_t` exists and is rational.

Let

\[
L_t=\operatorname{lcm}(1,2,\ldots,t).
\]

Then whether `t` is a sum of distinct divisors of `n` depends only on `n mod L_t`. Consequently

\[
\boxed{d_t=\frac{|R_t|}{L_t}}
\]

for an explicitly computable residue set `R_t subset Z/L_t Z`.

## Proof

Any positive divisor that occurs in a sum of distinct positive divisors equal to `t` is at most `t`. For every `d<=t`, the truth of `d|n` depends only on the residue class of `n` modulo `L_t` because `d|L_t`.

Thus the entire set of available divisors from `{1,...,t}` is determined by `n mod L_t`. Whether some distinct subcollection of those divisors sums to `t` is therefore also determined by `n mod L_t`.

The good integers are a union of residue classes modulo `L_t`, hence have a rational natural density.

## Corrected exact table

Independent exact residue enumeration in the recovery audit gives

| t | d_t |
|---:|:---|
| 1 | 1 |
| 2 | 1/2 |
| 3 | 2/3 |
| 4 | 1/2 |
| 5 | 7/15 |
| 6 | 7/15 |
| 7 | 16/35 |
| 8 | 3/7 |
| 9 | 17/45 |
| 10 | 2/5 |
| 11 | 13/33 |
| 12 | 43/99 |

Several small values recorded in the historical campaign were wrong; this table is the corrected Pass-3 enumeration.

## Scope

This establishes existence and rationality of every fixed-`t` density. It does **not** establish the parent asymptotic question asking whether constants `c_1,c_2>0` exist with

\[
d_t\sim c_1/(\log t)^{c_2}.
\]

That asymptotic remains separate.
