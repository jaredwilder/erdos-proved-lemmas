# Erdős #513 — exact maximizer of `r^n/n!`

**Author:** Jared Wilder  
**Status:** proved standalone child theorem; classical  
**Parent Erdős #513:** not closed by this note

## Theorem

For `r>0`, define

\[
a_n(r)=\frac{r^n}{n!},\qquad n=0,1,2,\ldots
\]

Then:

1. if `r` is not an integer, `a_n(r)` has a unique maximum at
   \[
   n=\lfloor r\rfloor;
   \]
2. if `r=m` is a positive integer, the two and only two maximizers are
   \[
   n=m-1\quad\text{and}\quad n=m;
   \]
3. the sequence is strictly decreasing for every `n≥⌈r⌉`.

Consequently,

\[
\max_{n\ge0}\frac{r^n}{n!}
\sim
\frac{e^r}{\sqrt{2\pi r}}
\qquad (r\to\infty).
\]

Equivalently, the largest point mass of a Poisson(`r`) random variable is asymptotic to `1/sqrt(2πr)`.

## Exact proof of the maximizer

The consecutive ratio is

\[
\frac{a_{n+1}(r)}{a_n(r)}=\frac{r}{n+1}.
\]

Thus:

- `a_{n+1}>a_n` exactly when `n+1<r`;
- `a_{n+1}=a_n` exactly when `n+1=r`;
- `a_{n+1}<a_n` exactly when `n+1>r`.

If `r` is nonintegral, the ratios are greater than `1` up to `n=floor(r)-1` and less than `1` from `n=floor(r)` onward. Hence the unique maximizer is `floor(r)`.

If `r=m∈N`, the ratio at `n=m-1` is exactly `1`; all earlier ratios are greater than `1` and all later ratios are less than `1`. Hence precisely `m-1,m` tie for the maximum.

The strict-tail statement follows immediately because `n≥ceil(r)` implies `n+1>r`.

## Asymptotic value

Let `m=floor(r)`. The exact maximizer result reduces the asymptotic to one factorial term. Standard Stirling bounds give

\[
m!=\sqrt{2\pi m}\,(m/e)^m(1+o(1)).
\]

Since `m=r+O(1)`, one obtains

\[
\frac{r^m}{m!}
=
\frac{e^r}{\sqrt{2\pi r}}(1+o(1)).
\]

The same conclusion holds at integer `r`, where the adjacent two terms tie.

The recovered campaign also recorded an explicit Robbins-Stirling error route, with the tail controlled by a rational bound of order `1/(12n-1)`. That quantitative refinement is not needed for the exact argmax theorem itself.

## Relevance to Erdős #513

For `f(z)=e^z`, the Taylor coefficients are `a_n=1/n!` and

\[
M(r)=\max_{|z|=r}|e^z|=e^r.
\]

Therefore

\[
\frac{\max_n r^n/n!}{M(r)}
\sim \frac{1}{\sqrt{2\pi r}}\to0.
\]

So `e^z` is an exact example with Erdős-513 functional value `0`.

This does **not** determine the greatest possible value over all transcendental entire functions; the recovered campaign's closer explicitly refused that leap because the universal upper bound and matching extremal construction were still missing.

## Provenance and novelty boundary

Recovered from route R015 of the 2026 Erdős #513 campaign and re-adjudicated during the 2026-09-13 omitted-family release. The ratio proof and Poisson-mode fact are classical; no historical novelty is asserted. The reason to publish the note is to separate a clean surviving theorem from the unsuccessful parent-problem routes around it.