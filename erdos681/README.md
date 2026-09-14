# Erdős #681 — prime-residual reduction, finite atlas, and KBK frontier

**Author:** Jared Wilder  
**Status:** parent open; several exact reductions and theorem-sized consequences established  
**Updated:** 2026-09-14

This page is the reader-facing index for the #681 work inside `erdos-proved-lemmas`. The parent problem remains open. The campaign is retained as a theorem/obstruction/KBK program rather than classified by whether the parent closed.

## Parent problem

For every sufficiently large integer `n`, does there exist an integer `k` such that `n+k` is composite and its least prime factor exceeds `k^2`?

## Exact residual reduction

The elementary reduction is in [`../erdos681-fourth-root-search-reduction.md`](../erdos681-fourth-root-search-reduction.md).

The stronger exact residual equivalence and its kernel-checked formal layer are in:

- [`../erdos681-residual-equivalence.lean`](../erdos681-residual-equivalence.lean)
- [`../erdos681-prime-residual-kbk-2026-09-14.md`](../erdos681-prime-residual-kbk-2026-09-14.md)

The hard inputs reduce to `n=p-1` with `p` prime. Writing `h=k-1`, the residual problem asks for an even `h>=2` such that

\[
p+h\text{ is composite},\qquad P^-(p+h)>(h+1)^2.
\]

Any such witness necessarily lies in the fourth-root window

\[
(h+1)^4<p+h.
\]

## Witness geometry extracted from the campaign

If `m=n+k` is a witness endpoint, every prime factor of `m` exceeds `k^2`. Therefore

\[
m>k^{2\Omega(m)}.
\]

In particular,

\[
m<k^6\quad\Longrightarrow\quad \Omega(m)=2.
\]

So any witness near the fourth-root boundary is forced to be a semiprime or prime square. If `m=qr` with `q<=r`, then

\[
\frac rq<\frac{m}{k^4},
\]

so endpoints close to `k^4` are forced toward balanced factorization.

## Finite atlas

The audited top-down campaign contains 85 clean chunks of width `10^10` covering

\[
1.5\times10^{11}\le p<10^{12}.
\]

Across those chunks:

- primes tested: **31,532,474,062**
- window-bad primes: **637,893**
- largest recorded window-bad prime: **999,997,304,513**

A second implementation was independently replayed on smaller windows and matched the C engine exactly. The interrupted giant bottom-up log is not treated as evidence.

## Analytic KBK frontier

The campaign developed a density-zero / exceptional-set route. A later audit unnecessarily lost a logarithm in the reduced-residue second-moment step. With the correct normalization, the intended covering-residue estimate returns to

\[
\delta(K)\ll \frac{\log^2 K}{K}+e^{-cK/\log K}.
\]

The corresponding quantitative target is

\[
\#B(X)\ll \pi(X)\frac{(\log\log X)^2}{\sqrt{\log X}}.
\]

This is currently a **theorem candidate requiring a clean citation/effectivity writeup and priority court**, not a published parent-resolution claim.

## KBK status

The campaign produced:

- an exact prime-residual equivalence;
- a kernel-checked formal reduction bundle;
- a fourth-root candidate window;
- parity pruning;
- a high-authority finite atlas through `10^12` in the recorded top-down range;
- a factor-count hierarchy forcing near-boundary semiprime geometry;
- a quantitative exceptional-set route;
- explicit route kills identifying where present analytic methods stop.

The parent remains open, but none of those outputs disappear because the terminal parent bit is still unknown.
