# Erdős #385 — parity baseline and reduction to even `n`

**Author:** Jared Wilder  
**Status:** exact universal child theorem / parity reduction; parent eventual-growth questions remain open  
**Historical novelty:** not asserted

## Setup

For `n>=1`, let

\[
F(n)=\max_{\substack{m<n\\ m\text{ composite}}}\bigl(m+p(m)\bigr),
\]

where `p(m)` denotes the least prime divisor of `m`.

The parent problem asks, among other things, whether `F(n)>n` for all sufficiently large `n`, and whether `F(n)-n -> infinity`.

## Theorem

For every `n>=5`,

\[
\boxed{F(n)\ge n.}
\]

Moreover, for every odd `n>=5`,

\[
\boxed{F(n)\ge n+1.}
\]

Consequently the first strict-inequality question `F(n)>n` is automatic on all odd `n>=5`; only even `n` can be obstructive.

## Proof

### Odd `n`

Let `n>=5` be odd and choose

\[
m=n-1.
\]

Then `m` is even and at least `4`, hence composite, and its least prime divisor is `2`. Therefore

\[
F(n)\ge m+p(m)=(n-1)+2=n+1.
\]

### Even `n`

Let `n>=6` be even and choose

\[
m=n-2.
\]

Then `m` is even and at least `4`, hence composite, with least prime divisor `2`. Thus

\[
F(n)\ge m+p(m)=(n-2)+2=n.
\]

The remaining endpoint `n=5` is covered by the odd argument using `m=4`.

This proves the theorem.

## Boundary

The result does not prove `F(n)>n` for all sufficiently large even `n`, and it says nothing by itself about the stronger limit `F(n)-n -> infinity`.

Its exact value is the parity reduction: the first parent question has no odd-number obstruction beyond the trivial finite beginning.

No novelty claim is made for the elementary observation.