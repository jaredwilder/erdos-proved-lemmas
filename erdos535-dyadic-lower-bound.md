# Erdős #535 — dyadic lower bound for equal-gcd avoidance

**Author:** Jared Wilder  
**Status:** elementary lower-bound theorem  
**Parent asymptotic estimation problem:** open

For fixed `r>=3`, let `f_r(N)` be the largest size of a subset `A⊆[N]` containing no `r` distinct elements whose pairwise greatest common divisors are all equal.

Equivalently, a forbidden `r`-set `{x_1,...,x_r}` has some integer `d` such that

\[
\gcd(x_i,x_j)=d
\qquad\text{for every }i\ne j.
\]

## Lemma — normalized forbidden sets are pairwise coprime

An `r`-set has all pairwise gcds equal to `d` if and only if every element is divisible by `d` and, after writing

\[
x_i=d a_i,
\]

the integers `a_1,...,a_r` are pairwise coprime.

Indeed,

\[
\gcd(da_i,da_j)=d\gcd(a_i,a_j).
\]

Thus equality of every pairwise gcd to `d` is exactly the condition `gcd(a_i,a_j)=1` for all `i≠j`.

## Theorem — powers of two give a logarithmic construction

For every `N>=1` and every fixed `r>=3`, the set

\[
P_N=\{2^j:2^j\le N\}
\]

contains no forbidden `r`-set. Consequently

\[
\boxed{f_r(N)\ge \lfloor\log_2 N\rfloor+1.}
\]

### Proof

Take any three distinct powers of two from `P_N`, say

\[
2^a<2^b<2^c.
\]

Their pairwise gcds include

\[
\gcd(2^a,2^b)=2^a
\]

and

\[
\gcd(2^b,2^c)=2^b,
\]

which are unequal. Therefore even three distinct powers of two cannot have all pairwise gcds equal. A fortiori no `r`-subset with `r>=3` can do so.

The number of powers of two not exceeding `N` is exactly `floor(log_2 N)+1`. ∎

## Small exact anchor

For `r=3`, the recovered exhaustive finite layer gives

\[
f_3(8)=4,
\]

and the dyadic set

\[
\{1,2,4,8\}
\]

attains that value.

The estate also contains other size-four witnesses at `N=8`, including `{3,4,6,8}`; the dyadic construction matters because it extends uniformly to every `N` and every fixed `r>=3`.

## Scope

This is a one-sided logarithmic lower bound. Erdős #535 asks for an asymptotic estimate of `f_r(N)` for fixed `r`; this note does **not** provide a matching upper bound and does not claim to determine the parent problem.

No historical novelty claim is made for the dyadic construction. It is published here because it was a clean theorem repeatedly present in the recovered campaign but absent from the public theorem surface.
