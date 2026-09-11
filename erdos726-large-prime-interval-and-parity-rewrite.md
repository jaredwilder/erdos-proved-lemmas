# Erdős #726 — exact indicator rewrite and corrected large-prime interval

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 status-conflict audit; historical endpoint claim corrected

For an odd prime `p`, write `r_p(n)` for the least nonnegative residue of `n` modulo `p`.

The canonical indicator in the campaign is

\[
1_{\{r_p(n)\in(p/2,p)\}}.
\]

## Theorem 1 — parity rewrite

For every odd prime `p`,

\[
\boxed{
1_{\{r_p(n)\in(p/2,p)\}}
=
1_{\{\lfloor 2n/p\rfloor\text{ is odd}\}}.
}
\]

### Proof

Write `n=qp+r` with `0<=r<p`. Then

\[
\left\lfloor\frac{2n}{p}\right\rfloor
=2q+\left\lfloor\frac{2r}{p}\right\rfloor.
\]

The second term is 0 or 1, and for odd `p` it equals 1 exactly when `r>p/2`.

## Theorem 2 — exact contribution from primes p>n/2

If `p` is an odd prime with

\[
\frac n2<p\le n,
\]

then

\[
\boxed{
r_p(n)\in(p/2,p)
\iff
\frac n2<p<\frac{2n}{3}.
}
\]

### Proof

In this range `n<2p`, so `r_p(n)=n-p`. Therefore

\[
r_p(n)>p/2
\iff
n-p>p/2
\iff
p<2n/3.
\]

The condition `r_p(n)<p` is automatic because `n<2p`.

Thus the entire large-prime block contributes exactly

\[
\boxed{
\sum_{n/2<p<2n/3}\frac1p.
}
\]

By Mertens' theorem for prime reciprocals this tends to zero:

\[
\sum_{n/2<p<2n/3}\frac1p=o(1).
\]

## Correction record

An earlier historical route claimed that the block `p>n/2` contributed `log 2+o(1)`. The exact interval calculation above shows that claim is false: only primes in `(n/2,2n/3)` contribute, and their reciprocal mass is `o(1)`.

## Scope

The full parent asymptotic

\[
\sum_{p\le n}1_{\{r_p(n)\in(p/2,p)\}}\frac1p
\sim\frac12\log\log n
\]

remains open in this release. The main difficulty lies among smaller primes; the large-prime endpoint is now exactly resolved.
