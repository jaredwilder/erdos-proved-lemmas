# Erdős #295 — exact small values of the reciprocal-representation function

**Author:** Jared Wilder  
**Status:** elementary theorem / exact finite values  
**Parent asymptotic problem:** open

For `N >= 1`, let `k(N)` be the minimum `k` for which there exist strictly increasing integers

\[
N\le n_1<n_2<\cdots<n_k
\]

such that

\[
\sum_{i=1}^k\frac1{n_i}=1.
\]

The recovered campaign contains a much larger asymptotic program. This note promotes only the part that has a short, self-contained proof and survived the later falsification passes.

## The harmonic-window bound

For every such strictly increasing tuple,

\[
n_i\ge N+i-1,
\]

so

\[
\boxed{
\sum_{i=1}^k\frac1{n_i}
\le
\sum_{j=0}^{k-1}\frac1{N+j}
=H_{N+k-1}-H_{N-1}.
}
\]

Consequently, if

\[
H_{N+k-1}-H_{N-1}<1,
\]

then no `k`-term representation is possible.

## Exact values

\[
\boxed{k(1)=1,\qquad k(2)=3,\qquad k(3)=5.}
\]

### `k(1)=1`

The one-term representation is simply

\[
1=\frac11.
\]

### `k(2)=3`

Any two distinct denominators at least 2 satisfy

\[
\frac1{n_1}+\frac1{n_2}
\le \frac12+\frac13
=\frac56<1,
\]

so `k(2)>=3`.

On the other hand,

\[
\frac12+\frac13+\frac16=1,
\]

hence `k(2)<=3` and therefore `k(2)=3`.

### `k(3)=5`

Any four strictly increasing denominators at least 3 satisfy

\[
\frac1{n_1}+\frac1{n_2}+\frac1{n_3}+\frac1{n_4}
\le
\frac13+\frac14+\frac15+\frac16
=\frac{57}{60}=\frac{19}{20}<1.
\]

Therefore `k(3)>=5`.

The five denominators

\[
\{3,4,5,6,20\}
\]

give

\[
\frac13+\frac14+\frac15+\frac16+\frac1{20}
=\frac{20+15+12+10+3}{60}
=1,
\]

so `k(3)<=5`. Thus

\[
\boxed{k(3)=5}.
\]

## Why the note stops at `N=3`

The same recovered source contains conflicting historical claims about `k(4)`. In particular, one banked witness

```text
{4,5,6,7,8,9,230}
```

was later refuted by exact rational arithmetic: its reciprocal sum is

\[
\frac{579590}{579600}<1.
\]

Other campaign rows propose different `k(4)` values and witnesses. They require a separate reconciliation and are deliberately excluded here.

The parent problem concerns the asymptotic behaviour of

\[
k(N)-(e-1)N.
\]

Nothing in these three exact values or in the harmonic-window inequality settles that asymptotic problem.

## Provenance

Recovered from the Pass-3 mathematical paragraph layer for `erdos295-campaign-001`. The campaign's later boundary/falsifier passes independently retained the `N<=3` values and explicitly separated them from the contaminated `N=4` history.

No historical novelty claim is made for these small values; the purpose of this file is to preserve the exact mathematics and its authority boundary in a stable public home.
