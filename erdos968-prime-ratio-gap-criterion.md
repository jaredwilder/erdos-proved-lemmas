# Erdős #968 — exact prime-ratio / prime-gap criterion

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem, independently rechecked

Let `p_n` denote the `n`-th prime and let

\[
d_n=p_{n+1}-p_n.
\]

## Theorem

For every `n>=1`,

\[
\boxed{
\frac{p_n}{n}<\frac{p_{n+1}}{n+1}
\iff
n d_n>p_n.
}
\]

Moreover equality of the two consecutive ratios never occurs.

## Proof

Cross-multiplication gives

\[
(n+1)p_n<n p_{n+1}
\iff
p_n<n(p_{n+1}-p_n)
\iff
p_n<n d_n.
\]

For equality, suppose

\[
\frac{p_n}{n}=\frac{p_{n+1}}{n+1}.
\]

Then

\[
n(p_{n+1}-p_n)=p_n,
\]

so `n|p_n`. Since `p_n` is prime, this would force `n=1` or `n=p_n`. The latter is impossible because `p_n>n`; for `n=1`, the ratios are `2` and `3/2`, not equal. Hence equality never occurs.

## Scope

This is an exact reformulation of the local increase event in terms of the prime gap `d_n`. It does not establish the positive-density assertion in the parent problem; that remains a prime-gap distribution question.
