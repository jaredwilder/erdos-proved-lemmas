# Erdős #681 — exact residual program, finite atlas, and parent-close frontier

**Author:** Jared Wilder  
**Status:** parent open; exact parent↔residual equivalence kernel-checked; substantial theorem/KBK estate established  
**Updated:** 2026-09-14

This page is the reader-facing index for the #681 work inside `erdos-proved-lemmas`. The campaign is treated as a theorem/obstruction/KBK program. The only terminal target remains the original eventual statement.

## Parent problem

For every sufficiently large integer `n`, does there exist an integer `k` such that `n+k` is composite and its least prime factor exceeds `k^2`?

## Exact parent ↔ prime-residual equivalence

The central formal object is [`../erdos681-residual-equivalence.lean`](../erdos681-residual-equivalence.lean). Its theorem

`msl_erdos681_bundle_equivalence`

kernel-checks the exact equivalence between the original parent and the residual statement:

> for every sufficiently large prime `p`, there exists an even shift `h>=2` such that `p+h` is composite and
> `(h+1)^2 < minFac(p+h)`.

Thus the parent close mission may work entirely on the prime residual **without weakening the problem**.

The elementary exposition is in [`../erdos681-fourth-root-search-reduction.md`](../erdos681-fourth-root-search-reduction.md).

## Buried kernel theorem cluster

The raw campaign formalized more than its terminal narrative foregrounded. The recovered theorem cluster is published in:

- [`../erdos681-kernel-theorem-cluster-2026-09-14.md`](../erdos681-kernel-theorem-cluster-2026-09-14.md)
- [`../erdos681-local-sieve-kernel.lean`](../erdos681-local-sieve-kernel.lean)

Key exact facts include:

- fixed short shifts automatically satisfy the fourth-root size condition once `p>(K+1)^4`;
- if a prime `q<p` divides `k-1`, it cannot divide `p-1+k`;
- a prime `r>K` can divide at most one member of a `K`-shift window;
- among the 48 reduced classes modulo 105, exactly 33 kill the `k=3` residual shift, giving density `11/16`;
- exact small-modulus residue-decoding lemmas;
- a concrete modulus-growth receipt for the quantitative exceptional-set architecture;
- the `H=41` smooth-covering size trap.

These are now first-class public results rather than formalizer filenames buried in a transcript.

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

forcing increasingly balanced factors as the endpoint approaches the fourth-root boundary.

The full KBK note is [`../erdos681-prime-residual-kbk-2026-09-14.md`](../erdos681-prime-residual-kbk-2026-09-14.md).

## Finite atlas

The audited top-down campaign contains 85 clean chunks of width `10^10` covering

\[
1.5\times10^{11}\le p<10^{12}.
\]

Across those chunks:

- primes tested: **31,532,474,062**
- window-bad primes: **637,893**
- largest recorded window-bad prime: **999,997,304,513**

A second implementation was independently replayed on smaller windows and matched the C engine exactly. The interrupted giant bottom-up log is not evidence.

## Analytic KBK frontier

The campaign developed a density-zero / exceptional-set route. A later audit unnecessarily lost a logarithm in the reduced-residue second-moment step. With the corrected normalization, the intended covering-residue estimate is

\[
\delta(K)\ll \frac{\log^2 K}{K}+e^{-cK/\log K},
\]

with corresponding quantitative target

\[
\#B(X)\ll \pi(X)\frac{(\log\log X)^2}{\sqrt{\log X}}.
\]

This remains a **theorem candidate requiring a clean source/effectivity and priority court**. Even if proved, it is not the parent close: density zero is weaker than eliminating all sufficiently large bad primes.

## Parent-close bottleneck

The exact kernel facts convert a hypothetical bad prime into a constrained deterministic covering object. Across a fourth-root-sized shift window:

- every composite non-witness must have a small prime factor at most the shift square;
- divisors of `k-1` are unavailable to kill that shift;
- primes larger than the window can hit at most one shift;
- any shift escaping all such small factors must be prime, otherwise it is already a witness.

The full close therefore needs a **universalization theorem**: show that this constrained covering-plus-prime-exception object cannot exist for every sufficiently large prime, or construct an infinite bad-prime family and thereby resolve the parent negatively.

No finite census, density-one theorem, conditional theorem, RH statement, or weaker exponent is accepted as terminal closure.
